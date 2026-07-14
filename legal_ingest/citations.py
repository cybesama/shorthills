from __future__ import annotations

import re

from .models import LegalCitation, Page


PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("usc", re.compile(r"\b\d+\s+U\.?\s?S\.?\s?C\.?\s+§{1,2}\s*[\w().\-–]+", re.I)),
    ("cfr", re.compile(r"\b\d+\s+C\.?\s?F\.?\s?R\.?\s+§{1,2}\s*[\w().\-–]+", re.I)),
    ("irc", re.compile(r"\b(?:I\.?\s?R\.?\s?C\.?\s+)?§{1,2}\s*\d+[A-Za-z]?(?:\([a-zA-Z0-9]+\))*", re.I)),
    ("supreme_court", re.compile(r"\b\d+\s+U\.\s?S\.\s+\d+(?:,\s*\d+)?\s*(?:\(\d{4}\))?")),
    ("federal_reporter", re.compile(r"\b\d+\s+F\.\s?(?:2d|3d|4th)\s+\d+(?:,\s*\d+)?(?:\s*\([^)]+\d{4}\))?", re.I)),
    ("tax_court", re.compile(r"\b\d+\s+T\.\s?C\.\s+\d+(?:,\s*\d+)?(?:\s*\(\d{4}\))?", re.I)),
    ("revenue_ruling", re.compile(r"\bRev\.\s+Rul\.\s+\d{2,4}-\d+\b", re.I)),
]


def normalize(raw: str) -> str:
    text = re.sub(r"\s+", " ", raw).strip().rstrip(".,;")
    # Canonicalize spaced reporter abbreviations ("U. S." -> "U.S.") so
    # citations extracted from historical OCR text match official_citation
    # strings for graph resolution.
    return re.sub(r"(?<=\b[A-Za-z])\.\s(?=[A-Za-z]\.)", ".", text)


def extract_citations(pages: list[Page]) -> list[LegalCitation]:
    found: dict[tuple[str, int, str], LegalCitation] = {}
    for page in pages:
        for citation_type, pattern in PATTERNS:
            for match in pattern.finditer(page.text):
                raw = match.group(0)
                normalized = normalize(raw)
                key = (normalized.casefold(), page.page_number, citation_type)
                found[key] = LegalCitation(
                    raw=raw,
                    normalized=normalized,
                    citation_type=citation_type,
                    page_number=page.page_number,
                )
    return list(found.values())

