# Legal OKF — Hybrid Search & Citation-Graph RAG over US Legal & Tax Documents

A retrieval-augmented Q&A system over 95 US legal and tax documents (Acts,
Supreme Court judgments, legal commentary, and IRS publications): page-faithful
ingestion, hybrid (keyword/vector/RRF) search, 1-hop citation-graph expansion,
and cited, LLM-generated answers — evaluated against a 40-item golden set.

See `ARCHITECTURE.md` for the full pipeline diagram and design decisions, and
`evaluation_assignment/evaluation_report.md` for the evaluation results.

## Live demo

- **UI**: https://shorthills.vercel.app
- **API**: https://shorthills-api.onrender.com (`/health`, `/search`, `/answer`)

## Project layout

```
legal_ingest/       Ingestion pipeline, search, answer generation, evaluation
static/index.html   Single-page demo UI (deployed separately on Vercel)
config/             Elasticsearch mapping + hybrid-query template
examples/           Manifests: a smoke-test source and the full 100-doc corpus
output/okf/          OKF markdown bundle (extracted, page-faithful documents)
output/graph_*.jsonl Citation graph (nodes/edges) — loaded by /answer at runtime
golden_set.json/csv  40-item evaluation golden set
evaluation_assignment/  Evaluation report (retrieval accuracy, faithfulness)
tests/              Unit tests
Dockerfile           Render deployment (API only)
render.yaml          Render Blueprint (one-click deploy config)
```

## Run the API locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[api,elastic]'
```

Create a `.env` (never committed) with:

```
ELASTIC_URL=...
ELASTIC_API_KEY=...
ELASTIC_INDEX=legal-chunks-v1
OPENAI_API_KEY=...
ALLOWED_ORIGINS=http://localhost:3000   # or * for local dev
```

```bash
uvicorn legal_ingest.api:app --reload
```

Serves `/search`, `/answer`, `/health`, and the demo UI at `/` (same-origin,
no separate deploy needed for local use).

## Ingest the corpus

```bash
pip install -e '.[dev]'
legal-ingest ingest --manifest examples/sources.yaml --output output   # smoke test
pytest
```

For scanned PDFs, install `.[ocr]` and pass `--ocr`. Embeddings are generated
via the OpenAI embeddings API (requires `OPENAI_API_KEY`):

```bash
pip install -e '.[api]'
legal-ingest ingest \
  --manifest examples/corpus_100.yaml \
  --output output \
  --embedding-model text-embedding-3-small \
  --elastic-url "$ELASTIC_URL"
```

The Elasticsearch mapping expects 1536-dimensional vectors (matching
`text-embedding-3-small`). Change `dims` in `config/elasticsearch-index.json`
if you select another model.

## Evaluate against the golden set

```bash
legal-ingest evaluate --golden-set golden_set.json --output evaluation_assignment
```

Runs retrieval-accuracy (Hit@k) and faithfulness checks (citation grounding +
LLM-judged verdicts) across all golden-set items, writing
`evaluation_report.{json,md}`. Faithfulness verdicts are left blank unless
`ANTHROPIC_API_KEY` is set; otherwise fill them in via
`legal_ingest.evaluate.apply_manual_judgments`.

## Deployment

Backend (FastAPI + Elasticsearch client) deploys on Render from the included
`Dockerfile`/`render.yaml`; the static UI deploys separately on Vercel (root
directory `static/`) and talks to the Render API over CORS
(`ALLOWED_ORIGINS` env var on Render must match the Vercel origin exactly,
including scheme). See `ARCHITECTURE.md` for the full request flow.

## Manifest format

Each source explicitly records its legal class and known authoritative metadata:

```yaml
sources:
  - url: https://...
    document_type: court_judgment
    title: Example v. United States
    court: Supreme Court of the United States
    decision_date: 1990-05-21
    official_citation: 495 U.S. 552 (1990)
```

Accepted types: `act`, `court_judgment`, `pov`, `tax_document`, `other`.

For the assignment's 100-document ratio, enable this policy at the top of the
manifest:

```yaml
corpus_policy:
  total_documents: 100
  required_counts:
    act: 27
    court_judgment: 27
    pov: 26
    tax_document: 20
```

This implements 80% Acts/Judgments/POV and 20% tax documents, with the non-tax
80 split as evenly as integer counts allow. Ingestion validates the complete
manifest before downloading anything.

## Accuracy and citation contract

PDF pages retain physical page order. Printed labels inside a PDF are not always
the same as PDF page indices, so both the one-based `page_number` and a
`page_label` are modeled. HTML, plain text, and DOCX do not reliably contain
physical pagination; those formats are marked `*_logical_page` and must not be
presented to users as printed-page citations.

Chunks do not cross page boundaries. Every generated answer cites, per claim:
`title`, `source_url`, `page_start`, `page_end`, and `content_sha256`. The hash
lets the application prove which downloaded source version supported an answer.

Citation extraction is deterministic and conservative. It creates useful graph
edges but does not claim to resolve every Bluebook citation. Production systems
should add CourtListener/CAP/Crossref-style authority resolution and human review.

## Outputs and search

Chunks live in Elasticsearch (`legal-chunks-v1`) with both a `text` field (BM25)
and an `embedding` field (kNN). `config/hybrid-query.json` demonstrates
reciprocal rank fusion (RRF), avoiding incomparable raw BM25 and cosine scores.
All three modes (keyword/vector/hybrid) are independently selectable via
`/search`'s `mode` parameter.

`graph_nodes.jsonl` and `graph_edges.jsonl` can be loaded into Neo4j, Amazon
Neptune, or Elasticsearch graph workflows. Unresolved citations become explicit
citation-stub nodes; matching an `official_citation` resolves them to ingested
documents. `/answer` uses this graph for 1-hop expansion, re-ranked by query
relevance before capping.

OKF is the portable knowledge representation, not the search engine. Each
concept is conformant Markdown with required `type` frontmatter and ordinary
links. The namespaced `legal` object is a backward-compatible domain extension
carrying provenance needed by legal RAG.

Only ingest material you are entitled to copy and index. Respect site terms,
robots policies, rate limits, copyright, and privacy obligations.
