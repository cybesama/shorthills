from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urldefrag

import yaml

from .chunk import chunk_document
from .citations import extract_citations
from .extract import extract
from .fetch import fetch_url, read_local
from .indexing import build_graph, embed_chunks, write_jsonl
from .models import Chunk, CorpusPolicy, LegalDocument, SourceSpec
from .okf import write_index, write_okf


def _document_id(url: str, sha256: str) -> str:
    canonical = urldefrag(url)[0]
    return hashlib.sha256(f"{canonical}\n{sha256}".encode()).hexdigest()[:32]


def ingest_one(
    spec: SourceSpec,
    *,
    local_path: Path | None = None,
    ocr: bool = False,
) -> LegalDocument:
    download = read_local(local_path) if local_path else fetch_url(spec.url)
    extracted = extract(download.data, download.media_type, ocr=ocr)
    title = spec.title or extracted.title or Path(spec.url).name or "Untitled legal document"
    document = LegalDocument(
        document_id=_document_id(download.final_url, download.sha256),
        document_type=spec.document_type,
        title=title,
        source_url=spec.url,
        canonical_url=download.final_url,
        content_sha256=download.sha256,
        media_type=download.media_type,
        jurisdiction=spec.jurisdiction,
        court=spec.court,
        decision_date=spec.decision_date,
        official_citation=spec.official_citation,
        tags=spec.tags,
        pages=extracted.pages,
        metadata=extracted.metadata,
    )
    return document.model_copy(update={"citations": extract_citations(document.pages)})


def load_manifest(path: Path) -> tuple[list[SourceSpec], CorpusPolicy | None]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    raw_sources = payload["sources"] if isinstance(payload, dict) else payload
    policy = (
        CorpusPolicy.model_validate(payload["corpus_policy"])
        if isinstance(payload, dict) and payload.get("corpus_policy")
        else None
    )
    return [SourceSpec.model_validate(item) for item in raw_sources], policy


def validate_corpus(sources: list[SourceSpec], policy: CorpusPolicy) -> None:
    counts = Counter(source.document_type for source in sources)
    errors: list[str] = []
    if len(sources) != policy.total_documents:
        errors.append(f"expected {policy.total_documents} documents, found {len(sources)}")
    expected_total = sum(policy.required_counts.values())
    if expected_total != policy.total_documents:
        errors.append(
            f"policy counts sum to {expected_total}, not {policy.total_documents}"
        )
    for document_type, expected in policy.required_counts.items():
        actual = counts[document_type]
        if actual != expected:
            errors.append(f"{document_type.value}: expected {expected}, found {actual}")
    unallocated = {
        kind.value: count
        for kind, count in counts.items()
        if kind not in policy.required_counts and count
    }
    if unallocated:
        errors.append(f"unallocated document types: {unallocated}")
    if errors:
        raise ValueError("Corpus policy violation: " + "; ".join(errors))


def run(
    manifest: Path,
    output: Path,
    *,
    ocr: bool = False,
    embedding_model: str | None = None,
) -> tuple[list[LegalDocument], list[Chunk]]:
    output.mkdir(parents=True, exist_ok=True)
    okf_root = output / "okf"
    okf_root.mkdir(exist_ok=True)
    sources, policy = load_manifest(manifest)
    if policy:
        validate_corpus(sources, policy)

    total = len(sources)
    documents: list[LegalDocument] = []
    failures: list[dict[str, str]] = []
    for index, spec in enumerate(sources, start=1):
        label = spec.title or spec.url
        print(f"[{index}/{total}] ingesting {spec.document_type.value}: {label}", flush=True)
        try:
            documents.append(ingest_one(spec, ocr=ocr))
        except Exception as exc:
            print(f"[{index}/{total}] FAILED: {label}: {exc}", flush=True)
            failures.append({"url": spec.url, "title": label, "error": str(exc)})

    written = [(doc, write_okf(doc, okf_root)) for doc in documents]
    write_index(written, okf_root)
    chunks = [chunk for doc in documents for chunk in chunk_document(doc)]
    if embedding_model:
        print(f"embedding {len(chunks)} chunks with {embedding_model}", flush=True)
        chunks = embed_chunks(chunks, embedding_model)
    nodes, edges = build_graph(documents)
    write_jsonl(documents, output / "documents.jsonl")
    write_jsonl(chunks, output / "chunks.jsonl")
    write_jsonl(nodes, output / "graph_nodes.jsonl")
    write_jsonl(edges, output / "graph_edges.jsonl")
    (output / "run.json").write_text(
        json.dumps(
            {"documents": len(documents), "chunks": len(chunks), "failures": failures},
            indent=2,
        )
        + "\n"
    )
    if failures:
        print(f"{len(failures)}/{total} sources failed; see run.json", flush=True)
    return documents, chunks
