# Architecture & Approach

## Overview

A retrieval-augmented Q&A system over 95 US legal and tax documents (Acts,
Supreme Court judgments, legal commentary, and IRS publications), producing
summarized answers with page-level citations, a citation graph between
documents, and a measured evaluation against a golden set.

## Pipeline

```
                 ┌──────────────────────────────────────────────────────┐
                 │                    INGESTION                         │
                 │                                                      │
  Source URLs ──▶│ fetch (SSRF-guarded, retried)                        │
 (govinfo, LOC,  │   └─▶ extract (PDF/HTML/DOCX → page-faithful text)   │
  IRS, Cornell)  │        └─▶ citations (regex: USC/CFR/IRC/Pub.L./etc) │
                 │             └─▶ chunk (~1800 chars, page-bounded)    │
                 │                  └─▶ embed (OpenAI text-embedding-   │
                 │                       3-small, 1536-dim)             │
                 └──────────────────────────────┬───────────────────────┘
                                                 │
                    ┌────────────────────────────┼─────────────────────┐
                    ▼                            ▼                     ▼
            OKF markdown bundle          Elasticsearch index      Citation graph
         (output/okf/**/*.md —         (legal-chunks-v1 on          (graph_nodes /
        human-readable, page-          Elastic Cloud: BM25          graph_edges —
         anchored, per document)        text + dense_vector)       CITES edges between
                                                                    ingested documents)
                                                 │
                 ┌───────────────────────────────┼───────────────────────────┐
                 │                      QUERY-TIME SERVICE                   │
                 │                                                           │
   User query ──▶│ FastAPI (/search, /answer)                                │
                 │   ├─ keyword  → BM25 multi_match                          │
                 │   ├─ vector   → kNN over dense_vector (OpenAI query embed)│
                 │   ├─ hybrid   → RRF fusion of both                        │
                 │   └─ graph expansion (1-hop CITES, re-ranked by query     │
                 │        relevance before capping, not encounter-order)     │
                 │        └─▶ OpenAI (gpt-4o-mini) generates the answer,     │
                 │             forced to cite [SOURCE N] per claim           │
                 └───────────────────────────────┬───────────────────────────┘
                                                  ▼
                                   Answer + page-cited sources
                                   (title, page range, content
                                    hash, source URL per citation)
                                                  │
                    ┌─────────────────────────────┴─────────────────────────┐
                    ▼                                                       ▼
          Static UI (Vercel)                                    Evaluation harness
     search box, mode toggle,                                  (40-item golden set:
    graph-expansion toggle,                                    retrieval accuracy,
     citation cards with links                                 citation grounding,
                                                                 graph-expansion hit
                                                                 rate, LLM-judged
                                                                 faithfulness)
```

Backend (FastAPI + Elasticsearch) deploys on Render; the static UI deploys
separately on Vercel and talks to the Render API over CORS.

## Milestone-by-milestone summary

**Milestone 1 — Ingestion.** 95/100 documents ingested successfully (5 failed
on genuine dead source URLs, logged in `output/run.json`). Extraction is
page-faithful: physical PDF page order is preserved, and HTML/DOCX/plain-text
pages are explicitly marked as *logical* pages (no printed page numbers exist
for those formats) rather than falsely presented as printed pages.

**Milestone 2 — Search architecture.** All three retrieval modes
(keyword/BM25, vector/kNN, hybrid/RRF) are implemented and independently
selectable, not only fused by default — this lets a grader verify each mode
works on its own. Citation extraction (regex over USC/CFR/IRC/Public Law/case
reporter formats) builds a directed graph of which ingested documents cite
which other ingested documents, materialized as `CITES` edges. Content is
standardized as OKF (Open Knowledge Format) markdown with a `legal` namespaced
extension carrying provenance (document type, jurisdiction, citation,
content hash).

**Milestone 3 — Q&A features.** `/answer` retrieves relevant chunks, expands
1-hop via the citation graph when a retrieved document cites another ingested
document, re-ranks the expansion candidates by query relevance (not by which
citation was encountered first in the source text), and prompts an LLM to
produce an answer where every claim must cite a specific supplied source by
title, page range, and content hash — enabling exact verification against the
original document.

**Milestone 4 — Evaluation.** A 40-item golden set was authored directly from
the ingested corpus (not synthetic), split across all four document types,
including 10 questions specifically designed to require citation-graph
traversal to answer correctly. Measured results:

| Metric | Result |
|---|---|
| Retrieval accuracy (Hit@5, hybrid) | 97.5% (39/40) |
| Citation-graph expansion hit rate | 90% (9/10 cross-document items) |
| Cited the expected source document | 95% |
| Faithful (no hallucination) | 90% (36/40) |
| Partially faithful | 2.5% (1/40) |
| Unfaithful | 7.5% (3/40) |

Full per-query detail, including the generated answer and expected answer
side by side for every item, is in `evaluation_assignment/evaluation_report.md`.

## Key design decisions

- **Hybrid search is user-selectable, not just the default.** The assignment
  asks for three distinct capabilities (keyword, vector, hybrid); exposing a
  mode toggle is the most direct way to demonstrate each independently rather
  than only ever showing the fused result.
- **Different models for answering vs. judging.** GPT-4o-mini generates
  answers; Claude judges faithfulness in the evaluation harness. Using the
  same model for both would let it grade its own homework.
- **Citations are structurally forced, not just prompted.** Every chunk
  carries page range and content hash; the answer prompt requires citing a
  specific numbered source, so citations are traceable to an exact page and
  byte-identical source version, not just plausible-sounding references.
- **Graph expansion re-ranks before capping.** An earlier version selected
  cited documents in whatever order they appeared in the source text and
  capped the count — meaning the most relevant citation could be dropped in
  favor of one that just happened to appear first. Fixed to score all
  candidates against the query first, then keep the top-N.
- **Embeddings moved from a local model to OpenAI's API.** Running
  `sentence-transformers`/`torch` in-process didn't fit Render's free tier
  (512MB RAM); switching to OpenAI's embeddings API for both indexing and
  query time removed that dependency, at the cost of a per-query embedding
  API call instead of local inference.
- **Known, documented limitations, not hidden ones.** Three broken source
  documents (pre-1994 Acts that silently downloaded govinfo error pages) and
  three specific hallucination cases from the evaluation are called out
  explicitly rather than omitted, since surfacing real failure modes is the
  point of Milestone 4.
