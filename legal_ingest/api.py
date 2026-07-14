from __future__ import annotations

import os
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .answer import generate_answer
from .graph import expand_via_citation_graph, load_citation_graph
from .search import SearchMode, run_search

load_dotenv()

ELASTIC_URL = os.environ.get("ELASTIC_URL", "http://localhost:9200")
ELASTIC_API_KEY = os.environ.get("ELASTIC_API_KEY")
ELASTIC_INDEX = os.environ.get("ELASTIC_INDEX", "legal-chunks-v1")
EMBEDDING_MODEL = os.environ.get("EMBEDDING_MODEL", "sentence-transformers/all-mpnet-base-v2")
OUTPUT_DIR = Path(os.environ.get("LEGAL_OUTPUT_DIR", "output"))
# Comma-separated list, e.g. "https://shorthills.vercel.app,http://localhost:3000"
ALLOWED_ORIGINS = [origin.strip() for origin in os.environ.get("ALLOWED_ORIGINS", "*").split(",")]

_state: dict[str, Any] = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    from elasticsearch import Elasticsearch
    from openai import OpenAI
    from sentence_transformers import SentenceTransformer

    _state["client"] = (
        Elasticsearch(ELASTIC_URL, api_key=ELASTIC_API_KEY) if ELASTIC_API_KEY else Elasticsearch(ELASTIC_URL)
    )
    _state["embedder"] = SentenceTransformer(EMBEDDING_MODEL)
    _state["openai"] = OpenAI()
    _state["graph"] = load_citation_graph(OUTPUT_DIR)
    yield
    _state.clear()


app = FastAPI(title="Legal OKF Search", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


class SearchRequest(BaseModel):
    query: str
    mode: SearchMode = SearchMode.HYBRID
    size: int = 10
    document_type: str | None = None


class SearchResult(BaseModel):
    chunk_id: str
    document_id: str
    document_type: str
    title: str
    source_url: str
    content_sha256: str
    page_start: int
    page_end: int
    page_labels: list[str]
    citation_strings: list[str] = []
    text: str = ""
    score: float
    via_graph: bool = False


class AnswerRequest(BaseModel):
    query: str
    mode: SearchMode = SearchMode.HYBRID
    size: int = 5
    document_type: str | None = None
    use_graph: bool = True


class AnswerResponse(BaseModel):
    answer: str
    citations: list[SearchResult]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


def _embed(request: SearchRequest | AnswerRequest) -> list[float] | None:
    if request.mode is SearchMode.KEYWORD:
        return None
    return _state["embedder"].encode(request.query, normalize_embeddings=True).tolist()


def _run(
    request: SearchRequest | AnswerRequest,
    query_vector: list[float] | None,
    *,
    size: int | None = None,
    document_id: str | None = None,
) -> list[dict[str, Any]]:
    try:
        return run_search(
            _state["client"],
            ELASTIC_INDEX,
            request.mode,
            request.query,
            query_vector,
            size=size if size is not None else request.size,
            document_type=request.document_type,
            document_id=document_id,
        )
    except Exception as exc:  # elasticsearch raises its own exception hierarchy
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.post("/search", response_model=list[SearchResult])
def search(request: SearchRequest) -> list[dict[str, Any]]:
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="query must not be empty")
    return _run(request, _embed(request))


@app.post("/answer", response_model=AnswerResponse)
def answer(request: AnswerRequest) -> dict[str, Any]:
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="query must not be empty")

    query_vector = _embed(request)
    anchors = _run(request, query_vector)
    expansions = (
        expand_via_citation_graph(
            _state["client"], ELASTIC_INDEX, request.mode, request.query, query_vector, anchors, _state["graph"]
        )
        if request.use_graph
        else []
    )
    chunks = anchors + expansions

    try:
        text = generate_answer(_state["openai"], request.query, chunks)
    except Exception as exc:  # openai raises its own exception hierarchy
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    return {"answer": text, "citations": chunks}


# Registered last so it never shadows the API routes above; catches "/" and any
# other unmatched GET with the static single-page UI.
app.mount("/", StaticFiles(directory="static", html=True), name="ui")
