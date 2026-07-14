from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .search import SearchMode, run_search

MAX_GRAPH_EXPANSIONS = 2
GRAPH_RELEVANCE_RATIO = 0.5  # an expanded chunk must score >= this fraction of the weakest anchor


def load_citation_graph(output_dir: Path) -> dict[str, list[dict]]:
    """Map document_id -> outgoing CITES edges resolved to another ingested document.

    Unresolved citation stubs (kind != "document") are dropped: there is no
    document to expand into for those.
    """
    nodes_path = output_dir / "graph_nodes.jsonl"
    edges_path = output_dir / "graph_edges.jsonl"
    if not nodes_path.exists() or not edges_path.exists():
        return {}

    document_node_ids: set[str] = set()
    with nodes_path.open(encoding="utf-8") as handle:
        for line in handle:
            node = json.loads(line)
            if node["kind"] == "document":
                document_node_ids.add(node["id"])

    edges: dict[str, list[dict]] = {}
    with edges_path.open(encoding="utf-8") as handle:
        for line in handle:
            edge = json.loads(line)
            if edge["relation"] != "CITES" or edge["target"] not in document_node_ids:
                continue
            edges.setdefault(edge["source"], []).append(
                {
                    "target_document_id": edge["target"],
                    "evidence_text": edge.get("evidence_text"),
                    "evidence_page": edge.get("evidence_page"),
                }
            )
    return edges


def cited_documents(graph: dict[str, list[dict]], document_id: str, *, limit: int | None = None) -> list[str]:
    """Distinct documents `document_id` cites, in first-seen order, optionally capped at `limit`."""
    seen: list[str] = []
    for edge in graph.get(document_id, []):
        target = edge["target_document_id"]
        if target not in seen:
            seen.append(target)
        if limit is not None and len(seen) >= limit:
            break
    return seen


def expand_via_citation_graph(
    client: Any,
    index: str,
    mode: SearchMode,
    query: str,
    query_vector: list[float] | None,
    anchors: list[dict[str, Any]],
    graph: dict[str, list[dict]],
    *,
    max_expansions: int = MAX_GRAPH_EXPANSIONS,
    relevance_ratio: float = GRAPH_RELEVANCE_RATIO,
) -> list[dict[str, Any]]:
    """1-hop citation-graph expansion, re-ranked against the query before inclusion.

    Every document any anchor cites is collected first (uncapped), each is scored
    against the query, and only the highest-scoring `max_expansions` candidates that
    clear the relevance threshold are kept. This ensures the cap is applied *after*
    ranking by relevance, not by whichever citation happened to be encountered first.

    Shared by the live /answer endpoint and the evaluation harness so both exercise
    identical graph-expansion behavior.
    """
    if not graph or not anchors:
        return []

    min_anchor_score = min(chunk["score"] for chunk in anchors)
    seen_document_ids = {chunk["document_id"] for chunk in anchors}

    candidate_ids: list[str] = []
    for anchor in anchors:
        for target_id in cited_documents(graph, anchor["document_id"]):
            if target_id not in seen_document_ids and target_id not in candidate_ids:
                candidate_ids.append(target_id)

    scored_candidates: list[dict[str, Any]] = []
    for target_id in candidate_ids:
        hits = run_search(client, index, mode, query, query_vector, size=1, document_id=target_id)
        if not hits:
            continue
        hit = hits[0]
        if hit["score"] < relevance_ratio * min_anchor_score:
            continue
        scored_candidates.append(hit)

    scored_candidates.sort(key=lambda hit: hit["score"], reverse=True)
    expansions = scored_candidates[:max_expansions]
    for hit in expansions:
        hit["via_graph"] = True
    return expansions
