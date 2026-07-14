from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any

from .answer import generate_answer
from .graph import expand_via_citation_graph
from .search import SearchMode, run_search

JUDGE_MODEL = os.environ.get("JUDGE_MODEL", "claude-opus-4-8")

JUDGE_SYSTEM_PROMPT = (
    "You are an impartial evaluator of legal-research answers. You will be given a "
    "question, a reference (ground truth) answer written by a human from the source "
    "document, and a system-generated answer produced by a separate RAG pipeline. "
    "Judge only faithfulness: does the system answer avoid contradicting or inventing "
    "facts beyond what the reference answer supports? Ignore differences in phrasing, "
    "completeness, or style; only unsupported or contradictory claims count against it.\n\n"
    'Respond with strict JSON only, no other text: '
    '{"verdict": "faithful" | "partially_faithful" | "unfaithful", "explanation": "<one sentence>"}'
)

CITATION_RE = re.compile(r"\[SOURCE (\d+)\]")


def load_golden_set(path: Path) -> list[dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def retrieval_hit(
    client: Any,
    index: str,
    embedder: Any,
    mode: SearchMode,
    query: str,
    expected_document_id: str,
    *,
    k: int,
) -> bool:
    query_vector = (
        None if mode is SearchMode.KEYWORD else embedder.encode(query, normalize_embeddings=True).tolist()
    )
    hits = run_search(client, index, mode, query, query_vector, size=k)
    return any(hit["document_id"] == expected_document_id for hit in hits)


def evaluate_retrieval(
    golden_set: list[dict[str, Any]],
    client: Any,
    index: str,
    embedder: Any,
    *,
    k: int = 5,
    modes: tuple[SearchMode, ...] = (SearchMode.HYBRID,),
) -> tuple[list[dict[str, Any]], dict[str, float]]:
    rows: list[dict[str, Any]] = []
    for item in golden_set:
        row: dict[str, Any] = {
            "id": item["id"],
            "query": item["query"],
            "expected_document": item["source_document"],
        }
        for mode in modes:
            row[f"hit_{mode.value}"] = retrieval_hit(
                client, index, embedder, mode, item["query"], item["source_document_id"], k=k
            )
        rows.append(row)

    summary = {
        mode.value: sum(1 for row in rows if row[f"hit_{mode.value}"]) / len(rows) for mode in modes
    }
    return rows, summary


def citation_grounding(
    answer_text: str, chunks: list[dict[str, Any]], expected_document_id: str
) -> dict[str, Any]:
    """Deterministic check: does the generated answer cite the expected source document?

    Every [SOURCE N] necessarily points at a retrieved chunk (the model can't invent an
    index), so the meaningful signal is whether the *correct* document was among what it
    cited, not merely whether it cited something.
    """
    cited_indices = sorted({int(m) for m in CITATION_RE.findall(answer_text)})
    cited_expected_document = any(
        1 <= idx <= len(chunks) and chunks[idx - 1]["document_id"] == expected_document_id
        for idx in cited_indices
    )
    return {
        "cited_any": bool(cited_indices),
        "cited_indices": cited_indices,
        "cited_expected_document": cited_expected_document,
    }


def judge_faithfulness(
    anthropic_client: Any, query: str, ground_truth: str, generated_answer: str
) -> dict[str, Any]:
    response = anthropic_client.messages.create(
        model=JUDGE_MODEL,
        max_tokens=300,
        system=JUDGE_SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": (
                    f"QUESTION: {query}\n\n"
                    f"REFERENCE ANSWER: {ground_truth}\n\n"
                    f"SYSTEM ANSWER: {generated_answer}"
                ),
            }
        ],
    )
    text = next(block.text for block in response.content if block.type == "text")
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"verdict": "unparseable", "explanation": text[:200]}


def evaluate_faithfulness(
    golden_set: list[dict[str, Any]],
    client: Any,
    index: str,
    embedder: Any,
    openai_client: Any,
    anthropic_client: Any | None,
    *,
    k: int,
    answer_mode: SearchMode,
    graph: dict[str, list[dict]] | None = None,
    use_graph: bool = True,
) -> tuple[list[dict[str, Any]], dict[str, float]]:
    """If anthropic_client is None, judge_verdict/judge_explanation are left as None —
    generation and citation-grounding still run, and the caller (or a human judge) can
    fill in verdicts afterward via apply_manual_judgments().

    When graph is provided and use_graph is True, this exercises the identical 1-hop
    citation-graph expansion the live /answer endpoint uses (via graph.expand_via_citation_graph),
    so faithfulness testing reflects real /answer behavior rather than plain retrieval.
    """
    rows: list[dict[str, Any]] = []
    for item in golden_set:
        query_vector = embedder.encode(item["query"], normalize_embeddings=True).tolist()
        anchors = run_search(client, index, answer_mode, item["query"], query_vector, size=k)
        expansions = (
            expand_via_citation_graph(client, index, answer_mode, item["query"], query_vector, anchors, graph)
            if use_graph and graph
            else []
        )
        chunks = anchors + expansions
        generated = generate_answer(openai_client, item["query"], chunks)
        grounding = citation_grounding(generated, chunks, item["source_document_id"])
        judge = (
            judge_faithfulness(anthropic_client, item["query"], item["ground_truth_answer"], generated)
            if anthropic_client is not None
            else {"verdict": None, "explanation": None}
        )
        graph_expected_document_id = item.get("graph_expected_document_id")
        graph_hit = (
            any(chunk["document_id"] == graph_expected_document_id for chunk in chunks)
            if graph_expected_document_id
            else None
        )
        rows.append(
            {
                "id": item["id"],
                "query": item["query"],
                "expected_document": item["source_document"],
                "expected_document_id": item["source_document_id"],
                "graph_expected_document": item.get("graph_expected_document"),
                "graph_expected_document_id": graph_expected_document_id,
                "graph_hit": graph_hit,
                "ground_truth_answer": item["ground_truth_answer"],
                "generated_answer": generated,
                "sources": summarize_sources(chunks),
                **grounding,
                "judge_verdict": judge.get("verdict"),
                "judge_explanation": judge.get("explanation"),
            }
        )

    return rows, summarize_faithfulness(rows)


def summarize_sources(chunks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Citation metadata for each retrieved chunk, indexed to match [SOURCE N] in the answer."""
    sources = []
    for i, chunk in enumerate(chunks, start=1):
        page = (
            f"p. {chunk['page_start']}"
            if chunk["page_start"] == chunk["page_end"]
            else f"pp. {chunk['page_start']}-{chunk['page_end']}"
        )
        sources.append(
            {
                "index": i,
                "title": chunk["title"],
                "source_url": chunk["source_url"],
                "page": page,
                "content_sha256": chunk["content_sha256"],
                "document_id": chunk["document_id"],
            }
        )
    return sources


def summarize_faithfulness(rows: list[dict[str, Any]]) -> dict[str, float]:
    total = len(rows)
    judged = [r for r in rows if r["judge_verdict"] is not None]
    summary = {
        "cited_expected_document_rate": sum(1 for r in rows if r["cited_expected_document"]) / total,
        "judged_count": len(judged),
        "pending_manual_judgment": total - len(judged),
    }
    graph_rows = [r for r in rows if r.get("graph_expected_document_id")]
    if graph_rows:
        summary["graph_expansion_items"] = len(graph_rows)
        summary["graph_expansion_hit_rate"] = sum(1 for r in graph_rows if r["graph_hit"]) / len(graph_rows)
    if judged:
        summary["faithful_rate"] = sum(1 for r in judged if r["judge_verdict"] == "faithful") / len(judged)
        summary["partially_faithful_rate"] = (
            sum(1 for r in judged if r["judge_verdict"] == "partially_faithful") / len(judged)
        )
        summary["unfaithful_rate"] = sum(1 for r in judged if r["judge_verdict"] == "unfaithful") / len(judged)
    return summary


def apply_manual_judgments(rows: list[dict[str, Any]], judgments: dict[str, dict[str, str]]) -> list[dict[str, Any]]:
    """judgments maps golden-set id -> {"verdict": ..., "explanation": ...}."""
    for row in rows:
        if row["id"] in judgments:
            row["judge_verdict"] = judgments[row["id"]]["verdict"]
            row["judge_explanation"] = judgments[row["id"]]["explanation"]
    return rows


def render_markdown_report(report: dict[str, Any]) -> str:
    lines = [
        "# Evaluation Report — Golden Set",
        "",
        f"Golden set size: {report['golden_set_size']} queries, k={report['k']}",
        "",
        "## Retrieval Accuracy (Hit@k, did the correct document appear in the top-k results)",
        "",
        "| Mode | Accuracy |",
        "| --- | --- |",
    ]
    for mode, acc in report["retrieval_accuracy"].items():
        lines.append(f"| {mode} | {acc:.0%} |")

    lines += [
        "",
        f"## Faithfulness (answers generated with `{report['answer_mode_used_for_faithfulness']}` retrieval)",
        "",
        "| Metric | Value |",
        "| --- | --- |",
    ]
    for metric, value in report["faithfulness_summary"].items():
        formatted = f"{value:.0%}" if isinstance(value, float) else str(value)
        lines.append(f"| {metric} | {formatted} |")

    lines += ["", "## Per-query detail", ""]
    for row in report["faithfulness_rows"]:
        retrieval_row = next(r for r in report["retrieval_rows"] if r["id"] == row["id"])
        hit_keys = [k for k in retrieval_row if k.startswith("hit_")]
        hits = ", ".join(
            f"{key[len('hit_'):]}={'hit' if retrieval_row[key] else 'miss'}" for key in hit_keys
        )
        expected_source = next(
            (s for s in row.get("sources", []) if s["document_id"] == row.get("expected_document_id")), None
        )
        expected_line = (
            f"- Expected document: [{row['expected_document']}]({expected_source['source_url']}) "
            f"({expected_source['page']}, sha256 {expected_source['content_sha256'][:12]}…)"
            if expected_source
            else f"- Expected document: {row['expected_document']} (not among retrieved sources below)"
        )
        graph_line = (
            [f"- Graph-expansion expected: **{row['graph_expected_document']}** — "
             f"{'hit' if row['graph_hit'] else 'MISS'}"]
            if row.get("graph_expected_document_id")
            else []
        )
        lines += [
            f"### {row['id']}: {row['query']}",
            expected_line,
            f"- Retrieval: {hits}",
            *graph_line,
            f"- Cited expected document: {row['cited_expected_document']}",
            f"- Judge verdict: **{row['judge_verdict']}** — {row['judge_explanation']}",
            "",
            f"**Expected answer:** {row['ground_truth_answer']}",
            "",
            f"**Generated answer:** {row['generated_answer']}",
            "",
            "**Sources provided to the model:**",
            "",
        ]
        for source in row.get("sources", []):
            marker = " (expected)" if source["document_id"] == row.get("expected_document_id") else ""
            lines.append(
                f"{source['index']}. [{source['title']}]({source['source_url']}) — {source['page']}, "
                f"sha256 {source['content_sha256'][:12]}…{marker}"
            )
        lines.append("")
    return "\n".join(lines)


def run_evaluation(
    golden_set_path: Path,
    output_dir: Path,
    *,
    elastic_url: str,
    elastic_api_key: str | None,
    elastic_index: str,
    embedding_model: str,
    openai_client: Any,
    anthropic_client: Any | None = None,
    k: int = 5,
    answer_mode: SearchMode = SearchMode.HYBRID,
    graph_dir: Path | None = None,
    use_graph: bool = True,
) -> dict[str, Any]:
    from elasticsearch import Elasticsearch
    from sentence_transformers import SentenceTransformer

    from .graph import load_citation_graph

    golden_set = load_golden_set(golden_set_path)
    client = (
        Elasticsearch(elastic_url, api_key=elastic_api_key) if elastic_api_key else Elasticsearch(elastic_url)
    )
    embedder = SentenceTransformer(embedding_model)
    graph = load_citation_graph(graph_dir) if graph_dir else {}

    retrieval_rows, retrieval_summary = evaluate_retrieval(golden_set, client, elastic_index, embedder, k=k)
    faithfulness_rows, faithfulness_summary = evaluate_faithfulness(
        golden_set,
        client,
        elastic_index,
        embedder,
        openai_client,
        anthropic_client,
        k=k,
        answer_mode=answer_mode,
        graph=graph,
        use_graph=use_graph,
    )

    report = {
        "golden_set_size": len(golden_set),
        "k": k,
        "answer_mode_used_for_faithfulness": answer_mode.value,
        "retrieval_accuracy": retrieval_summary,
        "retrieval_rows": retrieval_rows,
        "faithfulness_summary": faithfulness_summary,
        "faithfulness_rows": faithfulness_rows,
    }

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "evaluation_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    (output_dir / "evaluation_report.md").write_text(render_markdown_report(report), encoding="utf-8")
    return report
