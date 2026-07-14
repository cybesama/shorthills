from __future__ import annotations

import re
from pathlib import Path

import yaml

from .models import LegalDocument


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")[:100] or "document"


def render_okf(document: LegalDocument) -> str:
    """Render an OKF v0.1 concept with a namespaced legal extension."""
    frontmatter = {
        "type": {
            "act": "US Act",
            "court_judgment": "US Court Judgment",
            "pov": "Legal Commentary",
            "tax_document": "US Tax Document",
            "other": "Legal Document",
        }[document.document_type.value],
        "title": document.title,
        "description": f"Page-faithful extraction of {document.title}",
        "resource": document.canonical_url,
        "tags": sorted(set(["legal", document.jurisdiction.lower(), *document.tags])),
        "timestamp": document.retrieved_at.isoformat(),
        "legal": {
            "schema_version": document.schema_version,
            "document_id": document.document_id,
            "document_type": document.document_type.value,
            "jurisdiction": document.jurisdiction,
            "court": document.court,
            "decision_date": document.decision_date,
            "official_citation": document.official_citation,
            "content_sha256": document.content_sha256,
            "page_count": len(document.pages),
            "source_url": document.source_url,
        },
    }
    yaml_text = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).strip()
    body = [f"# {document.title}", "", "## Source", "", f"[Original document]({document.canonical_url})"]
    if document.official_citation:
        body += ["", f"Official citation: {document.official_citation}"]
    body += ["", "## Extracted text"]
    for page in document.pages:
        anchor = f"page-{page.page_number}"
        body += [
            "",
            f'<a id="{anchor}"></a>',
            f"### Page {page.page_label}",
            "",
            page.text or "_No machine-readable text extracted._",
        ]
    if document.citations:
        body += ["", "## Extracted legal citations", ""]
        for citation in document.citations:
            body.append(f"- {citation.normalized} — [page {citation.page_number}](#page-{citation.page_number})")
    return f"---\n{yaml_text}\n---\n\n" + "\n".join(body).rstrip() + "\n"


def write_okf(document: LegalDocument, root: Path) -> Path:
    folder = root / document.document_type.value
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{slugify(document.title)}-{document.document_id[:8]}.md"
    path.write_text(render_okf(document), encoding="utf-8")
    return path


def write_index(documents: list[tuple[LegalDocument, Path]], root: Path) -> None:
    lines = ["# US Tax & Legal Knowledge", "", "Page-faithful source concepts.", ""]
    for document, path in sorted(documents, key=lambda pair: pair[0].title):
        lines.append(f"- [{document.title}]({path.relative_to(root).as_posix()})")
    (root / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

