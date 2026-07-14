import hashlib

import yaml

from legal_ingest.chunk import chunk_document
from legal_ingest.citations import extract_citations
import pytest

from legal_ingest.models import CorpusPolicy, DocumentType, LegalDocument, Page, SourceSpec
from legal_ingest.okf import render_okf
from legal_ingest.pipeline import validate_corpus


def sample_document() -> LegalDocument:
    pages = [
        Page(
            page_number=1,
            page_label="1",
            text="The rule appears at 26 U.S.C. § 61(a).",
            extraction_method="test",
            char_start=0,
            char_end=40,
        ),
        Page(
            page_number=2,
            page_label="2",
            text="See 495 U.S. 552 (1990).",
            extraction_method="test",
            char_start=41,
            char_end=65,
        ),
    ]
    citations = extract_citations(pages)
    return LegalDocument(
        document_id="abc123",
        document_type=DocumentType.COURT_JUDGMENT,
        title="Example v. United States",
        source_url="https://example.gov/case.pdf",
        canonical_url="https://example.gov/case.pdf",
        content_sha256=hashlib.sha256(b"sample").hexdigest(),
        media_type="application/pdf",
        pages=pages,
        citations=citations,
    )


def test_citations_keep_page():
    document = sample_document()
    assert [(c.citation_type, c.page_number) for c in document.citations] == [
        ("usc", 1),
        ("supreme_court", 2),
    ]


def test_chunks_are_page_bound():
    chunks = chunk_document(sample_document(), target_chars=30, overlap_chars=5)
    assert chunks
    assert all(c.page_start == c.page_end for c in chunks)


def test_okf_has_required_type_and_page_anchors():
    rendered = render_okf(sample_document())
    frontmatter = rendered.split("---", 2)[1]
    parsed = yaml.safe_load(frontmatter)
    assert parsed["type"] == "US Court Judgment"
    assert parsed["legal"]["document_id"] == "abc123"
    assert '<a id="page-2"></a>' in rendered


def test_corpus_policy_enforces_ratio():
    counts = {
        DocumentType.ACT: 27,
        DocumentType.COURT_JUDGMENT: 27,
        DocumentType.POV: 26,
        DocumentType.TAX_DOCUMENT: 20,
    }
    sources = [
        SourceSpec(url=f"https://example.gov/{kind}-{i}.pdf", document_type=kind)
        for kind, count in counts.items()
        for i in range(count)
    ]
    validate_corpus(sources, CorpusPolicy())
    with pytest.raises(ValueError, match="tax_document"):
        validate_corpus(sources[:-1], CorpusPolicy())
