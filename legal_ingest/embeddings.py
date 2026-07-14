from __future__ import annotations

import os
from typing import Any

EMBEDDING_MODEL = os.environ.get("EMBEDDING_MODEL", "text-embedding-3-small")
EMBEDDING_BATCH_SIZE = 100


def embed_query(client: Any, text: str, *, model: str = EMBEDDING_MODEL) -> list[float]:
    response = client.embeddings.create(model=model, input=text)
    return response.data[0].embedding


def embed_texts(
    client: Any, texts: list[str], *, model: str = EMBEDDING_MODEL, batch_size: int = EMBEDDING_BATCH_SIZE
) -> list[list[float]]:
    """Batched embedding for many texts (e.g. bulk-indexing chunks)."""
    vectors: list[list[float]] = []
    for start in range(0, len(texts), batch_size):
        batch = texts[start : start + batch_size]
        response = client.embeddings.create(model=model, input=batch)
        vectors.extend(item.embedding for item in response.data)
    return vectors
