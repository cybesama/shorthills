from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Iterable

from .models import Chunk, GraphEdge, GraphNode, LegalDocument


def embed_chunks(chunks: list[Chunk], model_name: str) -> list[Chunk]:
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:
        raise RuntimeError(
            "Install with: pip install 'legal-okf-ingest[embeddings]'"
        ) from exc
    model = SentenceTransformer(model_name)
    vectors = model.encode(
        [chunk.text for chunk in chunks],
        normalize_embeddings=True,
        show_progress_bar=True,
    )
    return [
        chunk.model_copy(update={"embedding": vector.tolist()})
        for chunk, vector in zip(chunks, vectors, strict=True)
    ]


def write_jsonl(items: Iterable[object], path: Path) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for item in items:
            payload = item.model_dump(mode="json", exclude_none=True)  # type: ignore[attr-defined]
            handle.write(json.dumps(payload, ensure_ascii=False) + "\n")


def build_graph(documents: list[LegalDocument]) -> tuple[list[GraphNode], list[GraphEdge]]:
    nodes: dict[str, GraphNode] = {}
    edges: list[GraphEdge] = []
    citation_owner = {
        doc.official_citation.casefold(): doc.document_id
        for doc in documents
        if doc.official_citation
    }
    for doc in documents:
        nodes[doc.document_id] = GraphNode(
            id=doc.document_id,
            kind="document",
            label=doc.title,
            properties={"document_type": doc.document_type.value, "url": doc.canonical_url},
        )
        for citation in doc.citations:
            target = citation_owner.get(citation.normalized.casefold())
            if target is None:
                target = "citation:" + hashlib.sha256(
                    citation.normalized.casefold().encode()
                ).hexdigest()[:24]
                nodes.setdefault(
                    target,
                    GraphNode(
                        id=target,
                        kind=citation.citation_type,
                        label=citation.normalized,
                    ),
                )
            edge_key = f"{doc.document_id}:{target}:{citation.page_number}:{citation.normalized}"
            edges.append(
                GraphEdge(
                    id=hashlib.sha256(edge_key.encode()).hexdigest()[:24],
                    source=doc.document_id,
                    target=target,
                    relation="CITES",
                    evidence_page=citation.page_number,
                    evidence_text=citation.raw,
                )
            )
    return list(nodes.values()), edges


def bulk_index(chunks: list[Chunk], elastic_url: str, index: str) -> None:
    try:
        from elasticsearch import Elasticsearch, helpers
    except ImportError as exc:
        raise RuntimeError("Install with: pip install 'legal-okf-ingest[elastic]'") from exc
    api_key = os.environ.get("ELASTIC_API_KEY")
    client = (
        Elasticsearch(elastic_url, api_key=api_key, request_timeout=120)
        if api_key
        else Elasticsearch(elastic_url, request_timeout=120)
    )
    actions = (
        {"_index": index, "_id": chunk.chunk_id, "_source": chunk.model_dump(exclude_none=True)}
        for chunk in chunks
    )
    helpers.bulk(client, actions, chunk_size=200, request_timeout=120)

