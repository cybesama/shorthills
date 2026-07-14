from __future__ import annotations

from enum import StrEnum
from typing import Any


class SearchMode(StrEnum):
    VECTOR = "vector"
    KEYWORD = "keyword"
    HYBRID = "hybrid"


_KEYWORD_QUERY_FIELDS = ["title^4", "citation_strings.exact^8", "citation_strings", "text"]
_SOURCE_FIELDS = [
    "chunk_id",
    "document_id",
    "document_type",
    "title",
    "source_url",
    "content_sha256",
    "page_start",
    "page_end",
    "page_labels",
    "citation_strings",
    "text",
]


def build_query(
    mode: SearchMode,
    query_text: str,
    query_vector: list[float] | None,
    *,
    size: int = 10,
    document_type: str | None = None,
    document_id: str | None = None,
) -> dict[str, Any]:
    filter_clause: list[dict[str, Any]] = []
    if document_type:
        filter_clause.append({"term": {"document_type": document_type}})
    if document_id:
        filter_clause.append({"term": {"document_id": document_id}})

    if mode is SearchMode.KEYWORD:
        body: dict[str, Any] = {
            "query": {
                "bool": {
                    "must": {"multi_match": {"query": query_text, "fields": _KEYWORD_QUERY_FIELDS}},
                    "filter": filter_clause,
                }
            },
            "size": size,
        }
    elif mode is SearchMode.VECTOR:
        if query_vector is None:
            raise ValueError("vector search requires a query embedding")
        body = {
            "knn": {
                "field": "embedding",
                "query_vector": query_vector,
                "k": size,
                "num_candidates": max(size * 10, 100),
                **({"filter": {"bool": {"filter": filter_clause}}} if filter_clause else {}),
            },
            "size": size,
        }
    else:
        if query_vector is None:
            raise ValueError("hybrid search requires a query embedding")
        body = {
            "retriever": {
                "rrf": {
                    "retrievers": [
                        {
                            "standard": {
                                "query": {
                                    "bool": {
                                        "must": {
                                            "multi_match": {
                                                "query": query_text,
                                                "fields": _KEYWORD_QUERY_FIELDS,
                                            }
                                        },
                                        "filter": filter_clause,
                                    }
                                }
                            }
                        },
                        {
                            "knn": {
                                "field": "embedding",
                                "query_vector": query_vector,
                                "k": max(size * 5, 50),
                                "num_candidates": max(size * 20, 200),
                                **(
                                    {"filter": {"bool": {"filter": filter_clause}}}
                                    if filter_clause
                                    else {}
                                ),
                            }
                        },
                    ],
                    "rank_window_size": max(size * 10, 100),
                    "rank_constant": 60,
                }
            },
            "size": size,
        }
    body["_source"] = _SOURCE_FIELDS
    return body


def run_search(
    client: Any,
    index: str,
    mode: SearchMode,
    query_text: str,
    query_vector: list[float] | None,
    *,
    size: int = 10,
    document_type: str | None = None,
    document_id: str | None = None,
) -> list[dict[str, Any]]:
    body = build_query(
        mode,
        query_text,
        query_vector,
        size=size,
        document_type=document_type,
        document_id=document_id,
    )
    response = client.search(index=index, body=body)
    results = []
    for hit in response["hits"]["hits"]:
        results.append({**hit["_source"], "score": hit["_score"]})
    return results
