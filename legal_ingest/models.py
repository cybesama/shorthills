from __future__ import annotations

from datetime import datetime, timezone
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field


class DocumentType(StrEnum):
    ACT = "act"
    COURT_JUDGMENT = "court_judgment"
    POV = "pov"
    TAX_DOCUMENT = "tax_document"
    OTHER = "other"


class SourceSpec(BaseModel):
    url: str
    document_type: DocumentType = DocumentType.OTHER
    title: str | None = None
    jurisdiction: str = "US"
    court: str | None = None
    decision_date: str | None = None
    official_citation: str | None = None
    tags: list[str] = Field(default_factory=list)


class CorpusPolicy(BaseModel):
    total_documents: int = Field(default=100, ge=1)
    required_counts: dict[DocumentType, int] = Field(
        default_factory=lambda: {
            DocumentType.ACT: 27,
            DocumentType.COURT_JUDGMENT: 27,
            DocumentType.POV: 26,
            DocumentType.TAX_DOCUMENT: 20,
        }
    )


class Page(BaseModel):
    page_number: int = Field(ge=1)
    page_label: str
    text: str
    extraction_method: str
    char_start: int = Field(ge=0)
    char_end: int = Field(ge=0)


class LegalCitation(BaseModel):
    raw: str
    normalized: str
    citation_type: str
    page_number: int
    target_document_id: str | None = None


class LegalDocument(BaseModel):
    schema_version: str = "legal-okf/1.0"
    document_id: str
    document_type: DocumentType
    title: str
    source_url: str
    canonical_url: str
    retrieved_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    content_sha256: str
    media_type: str
    jurisdiction: str = "US"
    court: str | None = None
    decision_date: str | None = None
    official_citation: str | None = None
    tags: list[str] = Field(default_factory=list)
    pages: list[Page]
    citations: list[LegalCitation] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)


class Chunk(BaseModel):
    chunk_id: str
    document_id: str
    document_type: DocumentType
    title: str
    source_url: str
    content_sha256: str
    page_start: int
    page_end: int
    page_labels: list[str]
    char_start: int
    char_end: int
    text: str
    citation_strings: list[str] = Field(default_factory=list)
    embedding: list[float] | None = None


class GraphNode(BaseModel):
    id: str
    kind: str
    label: str
    properties: dict[str, Any] = Field(default_factory=dict)


class GraphEdge(BaseModel):
    id: str
    source: str
    target: str
    relation: str
    evidence_page: int | None = None
    evidence_text: str | None = None
    properties: dict[str, Any] = Field(default_factory=dict)
