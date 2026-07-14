from __future__ import annotations

import hashlib
import ipaddress
import socket
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

import httpx


MAX_BYTES = 100 * 1024 * 1024
ALLOWED_SCHEMES = {"http", "https"}
RETRYABLE_EXCEPTIONS = (httpx.TransportError, httpx.HTTPStatusError)
MAX_ATTEMPTS = 4


@dataclass(frozen=True)
class Download:
    data: bytes
    final_url: str
    media_type: str
    sha256: str


def _assert_public_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in ALLOWED_SCHEMES or not parsed.hostname:
        raise ValueError("Only public http(s) URLs are accepted")
    for result in socket.getaddrinfo(parsed.hostname, parsed.port or 443):
        address = ipaddress.ip_address(result[4][0])
        if not address.is_global:
            raise ValueError(f"Refusing non-public address: {address}")


def _fetch_once(client: httpx.Client, url: str, max_bytes: int) -> Download:
    with client.stream("GET", url) as response:
        response.raise_for_status()
        _assert_public_url(str(response.url))
        declared = int(response.headers.get("content-length", "0") or 0)
        if declared > max_bytes:
            raise ValueError(f"Document exceeds {max_bytes} bytes")
        parts: list[bytes] = []
        size = 0
        for part in response.iter_bytes():
            size += len(part)
            if size > max_bytes:
                raise ValueError(f"Document exceeds {max_bytes} bytes")
            parts.append(part)
        data = b"".join(parts)
        media_type = response.headers.get("content-type", "").split(";")[0].lower()
        return Download(
            data=data,
            final_url=str(response.url),
            media_type=media_type,
            sha256=hashlib.sha256(data).hexdigest(),
        )


def fetch_url(url: str, *, timeout: float = 45, max_bytes: int = MAX_BYTES) -> Download:
    """Download a public document with SSRF and size protections, retrying transient failures."""
    _assert_public_url(url)
    headers = {"User-Agent": "legal-okf-ingest/0.1 (research ingestion)"}
    with httpx.Client(follow_redirects=True, timeout=timeout, headers=headers) as client:
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                return _fetch_once(client, url, max_bytes)
            except RETRYABLE_EXCEPTIONS:
                if attempt == MAX_ATTEMPTS:
                    raise
                time.sleep(2**attempt)
    raise AssertionError("unreachable")


def read_local(path: Path) -> Download:
    data = path.read_bytes()
    media = {
        ".pdf": "application/pdf",
        ".html": "text/html",
        ".htm": "text/html",
        ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ".txt": "text/plain",
        ".md": "text/markdown",
    }.get(path.suffix.lower(), "application/octet-stream")
    return Download(data, path.resolve().as_uri(), media, hashlib.sha256(data).hexdigest())

