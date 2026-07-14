from __future__ import annotations

import hashlib
import re

from .models import Chunk, LegalDocument


def _chunk_id(document_id: str, start: int, end: int) -> str:
    return hashlib.sha256(f"{document_id}:{start}:{end}".encode()).hexdigest()[:24]


def chunk_document(
    document: LegalDocument, *, target_chars: int = 1800, overlap_chars: int = 250
) -> list[Chunk]:
    """Page-aware chunks. A chunk never loses its page range or source offsets."""
    if target_chars <= overlap_chars:
        raise ValueError("target_chars must exceed overlap_chars")
    chunks: list[Chunk] = []
    for page in document.pages:
        text = page.text
        start = 0
        while start < len(text):
            proposed = min(start + target_chars, len(text))
            if proposed < len(text):
                boundary = max(
                    text.rfind("\n\n", start, proposed),
                    text.rfind(". ", start, proposed),
                )
                if boundary > start + target_chars // 2:
                    proposed = boundary + 1
            fragment = text[start:proposed].strip()
            if fragment:
                global_start = page.char_start + start
                global_end = page.char_start + proposed
                citations = [
                    c.normalized
                    for c in document.citations
                    if c.page_number == page.page_number
                    and re.search(re.escape(c.raw), fragment, re.I)
                ]
                chunks.append(
                    Chunk(
                        chunk_id=_chunk_id(document.document_id, global_start, global_end),
                        document_id=document.document_id,
                        document_type=document.document_type,
                        title=document.title,
                        source_url=document.source_url,
                        content_sha256=document.content_sha256,
                        page_start=page.page_number,
                        page_end=page.page_number,
                        page_labels=[page.page_label],
                        char_start=global_start,
                        char_end=global_end,
                        text=fragment,
                        citation_strings=citations,
                    )
                )
            if proposed == len(text):
                break
            start = max(proposed - overlap_chars, start + 1)
    return chunks

