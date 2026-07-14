from __future__ import annotations

import os
from typing import Any

ANSWER_MODEL = os.environ.get("ANSWER_MODEL", "gpt-4o-mini")

SYSTEM_PROMPT = (
    "You are a legal research assistant. Answer the user's question using ONLY the "
    "numbered SOURCE excerpts provided below the question. Every factual claim in your "
    "answer must be followed by a bracketed citation to the source(s) that support it, "
    "e.g. [SOURCE 2]. If the excerpts do not contain enough information to answer fully, "
    "say so explicitly instead of using outside knowledge or guessing. Never state a legal "
    "conclusion that is not directly supported by a SOURCE excerpt."
)


def _page_label(chunk: dict[str, Any]) -> str:
    if chunk["page_start"] == chunk["page_end"]:
        return f"p.{chunk['page_start']}"
    return f"pp.{chunk['page_start']}-{chunk['page_end']}"


def build_context_block(chunks: list[dict[str, Any]]) -> str:
    parts = []
    for index, chunk in enumerate(chunks, start=1):
        parts.append(
            f"[SOURCE {index}] {chunk['title']} ({chunk['document_type']}), {_page_label(chunk)}\n"
            f"URL: {chunk['source_url']}\n"
            f"SHA256: {chunk['content_sha256']}\n"
            f"{chunk['text']}"
        )
    return "\n\n".join(parts)


def generate_answer(client: Any, query: str, chunks: list[dict[str, Any]]) -> str:
    if not chunks:
        return "No relevant sources were found for this question."
    context = build_context_block(chunks)
    response = client.chat.completions.create(
        model=ANSWER_MODEL,
        max_tokens=1024,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"SOURCES:\n\n{context}\n\nQUESTION: {query}",
            },
        ],
    )
    return response.choices[0].message.content
