FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml ./
COPY legal_ingest ./legal_ingest
RUN pip install --no-cache-dir -e '.[api,embeddings,elastic]'

COPY static ./static
COPY output/graph_nodes.jsonl output/graph_edges.jsonl ./output/

ENV LEGAL_OUTPUT_DIR=/app/output
EXPOSE 8000

CMD uvicorn legal_ingest.api:app --host 0.0.0.0 --port ${PORT:-8000}
