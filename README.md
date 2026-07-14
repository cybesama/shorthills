# Legal OKF ingestion

A page-faithful ingestion pipeline for US acts, judgments, commentary, and tax
documents. It downloads public HTTP(S) sources and produces:

- an OKF v0.1 bundle (`okf/**/*.md`);
- document and page-aware chunk JSONL for Elasticsearch/BM25 and vector search;
- citation nodes and `CITES` edges for graph import;
- stable document/chunk IDs, source URLs, hashes, page numbers, and character offsets.

## Install and run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
legal-ingest ingest --manifest examples/sources.yaml --output output
pytest
```

For scanned PDFs, install `.[ocr]` and pass `--ocr`. For local embeddings:

```bash
pip install -e '.[embeddings]'
legal-ingest ingest \
  --manifest examples/sources.yaml \
  --output output \
  --embedding-model sentence-transformers/all-mpnet-base-v2
```

The included Elasticsearch mapping expects 768-dimensional vectors (matching
`all-mpnet-base-v2`). Change `dims` if you select another model. Create the index
with `config/elasticsearch-index.json`, then pass `--elastic-url`.

## Manifest

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
manifest before downloading anything. Change the three non-tax counts if the
assignment owner specifies a different internal split, but keep their sum at 80.

## Accuracy and citation contract

PDF pages retain physical page order. Printed labels inside a PDF are not always
the same as PDF page indices, so both the one-based `page_number` and a
`page_label` are modeled. HTML, plain text, and DOCX do not reliably contain
physical pagination; those formats are marked `*_logical_page` and must not be
presented to users as printed-page citations.

Chunks do not cross page boundaries. A generated answer should cite at least:
`title`, `source_url`, `page_start`, `page_end`, and `content_sha256`. The hash
lets the application prove which downloaded source version supported an answer.

Citation extraction is deterministic and conservative. It creates useful graph
edges but does not claim to resolve every Bluebook citation. Production systems
should add CourtListener/CAP/Crossref-style authority resolution and human review.

## Outputs and search

`chunks.jsonl` is the shared indexing record. Use text fields for BM25 and the
`embedding` field for kNN. `config/hybrid-query.json` demonstrates reciprocal
rank fusion (RRF), avoiding incomparable raw BM25 and cosine scores.

`graph_nodes.jsonl` and `graph_edges.jsonl` can be loaded into Neo4j, Amazon
Neptune, or Elasticsearch graph workflows. Unresolved citations become explicit
citation nodes; matching an `official_citation` resolves them to ingested
documents.

OKF is the portable knowledge representation, not the search engine. Each concept
is conformant Markdown with required `type` frontmatter and ordinary links. The
namespaced `legal` object is a backward-compatible domain extension carrying
provenance needed by legal RAG.

Only ingest material you are entitled to copy and index. Respect site terms,
robots policies, rate limits, copyright, and privacy obligations.
