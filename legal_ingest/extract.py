from __future__ import annotations

import io
import re
from dataclasses import dataclass

from bs4 import BeautifulSoup
from docx import Document as DocxDocument
from pypdf import PdfReader

from .models import Page


@dataclass
class Extraction:
    title: str | None
    pages: list[Page]
    metadata: dict[str, str]


def _clean(text: str) -> str:
    text = text.replace("\x00", "")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _pages(texts: list[str], method: str) -> list[Page]:
    result: list[Page] = []
    cursor = 0
    for number, raw in enumerate(texts, 1):
        text = _clean(raw)
        result.append(
            Page(
                page_number=number,
                page_label=str(number),
                text=text,
                extraction_method=method,
                char_start=cursor,
                char_end=cursor + len(text),
            )
        )
        cursor += len(text) + 1
    return result


def extract_pdf(data: bytes, *, ocr: bool = False) -> Extraction:
    reader = PdfReader(io.BytesIO(data))
    texts = [(page.extract_text(extraction_mode="layout") or "") for page in reader.pages]
    if ocr:
        texts = _ocr_empty_pdf_pages(data, texts)
    metadata = {str(k).lstrip("/"): str(v) for k, v in (reader.metadata or {}).items()}
    return Extraction(metadata.get("Title"), _pages(texts, "pdf_text"), metadata)


def _ocr_empty_pdf_pages(data: bytes, texts: list[str]) -> list[str]:
    """OCR only pages that have almost no text; requires the `ocr` extra."""
    try:
        import fitz
        import pytesseract
        from PIL import Image
    except ImportError as exc:
        raise RuntimeError("Install with: pip install 'legal-okf-ingest[ocr]'") from exc
    doc = fitz.open(stream=data, filetype="pdf")
    for i, text in enumerate(texts):
        if len(text.strip()) >= 40:
            continue
        pix = doc[i].get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
        image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        texts[i] = pytesseract.image_to_string(image)
    return texts


def extract_html(data: bytes) -> Extraction:
    soup = BeautifulSoup(data, "html.parser")
    title = soup.title.get_text(" ", strip=True) if soup.title else None
    for tag in soup(["script", "style", "nav", "noscript"]):
        tag.decompose()
    # HTML has no physical page. It is explicitly represented as one logical page.
    return Extraction(title, _pages([soup.get_text("\n")], "html_logical_page"), {})


def extract_docx(data: bytes) -> Extraction:
    doc = DocxDocument(io.BytesIO(data))
    paragraphs = [p.text for p in doc.paragraphs]
    # Word page breaks are not a reliable layout model; split only explicit breaks.
    groups: list[list[str]] = [[]]
    for paragraph in paragraphs:
        if "\f" in paragraph:
            segments = paragraph.split("\f")
            groups[-1].append(segments[0])
            for segment in segments[1:]:
                groups.append([segment])
        else:
            groups[-1].append(paragraph)
    return Extraction(None, _pages(["\n".join(g) for g in groups], "docx_logical_page"), {})


def extract(data: bytes, media_type: str, *, ocr: bool = False) -> Extraction:
    if media_type == "application/pdf" or data[:5] == b"%PDF-":
        return extract_pdf(data, ocr=ocr)
    if media_type in {"text/html", "application/xhtml+xml"}:
        return extract_html(data)
    if media_type.endswith("wordprocessingml.document"):
        return extract_docx(data)
    if media_type.startswith("text/"):
        return Extraction(None, _pages([data.decode("utf-8", errors="replace")], "plain_text"), {})
    raise ValueError(f"Unsupported media type: {media_type}")

