import os
from pathlib import Path
from typing import Annotated

import typer
from dotenv import load_dotenv

from .indexing import bulk_index
from .pipeline import load_manifest, run, validate_corpus
from .search import SearchMode

load_dotenv()

app = typer.Typer(no_args_is_help=True)


@app.callback()
def main() -> None:
    """Page-faithful legal document ingestion."""


@app.command()
def ingest(
    manifest: Annotated[Path, typer.Option(exists=True, readable=True)],
    output: Annotated[Path, typer.Option()] = Path("output"),
    ocr: Annotated[bool, typer.Option(help="OCR image-only PDF pages")] = False,
    embedding_model: Annotated[
        str | None,
        typer.Option(help="SentenceTransformers model; omit to embed in Elasticsearch"),
    ] = None,
    elastic_url: Annotated[str | None, typer.Option()] = None,
    elastic_index: Annotated[str, typer.Option()] = "legal-chunks-v1",
) -> None:
    """Download, parse, cite, chunk, and export a manifest of legal sources."""
    documents, chunks = run(
        manifest, output, ocr=ocr, embedding_model=embedding_model
    )
    if elastic_url:
        bulk_index(chunks, elastic_url, elastic_index)
    typer.echo(f"Ingested {len(documents)} documents into {len(chunks)} chunks at {output}")


@app.command("validate-manifest")
def validate_manifest(
    manifest: Annotated[Path, typer.Option(exists=True, readable=True)],
) -> None:
    """Validate manifest shape and corpus ratio without downloading documents."""
    sources, policy = load_manifest(manifest)
    if policy:
        validate_corpus(sources, policy)
        typer.echo(f"Manifest OK: {len(sources)} documents match the corpus policy.")
        return
    typer.echo(f"Manifest OK: {len(sources)} documents. No corpus_policy was provided.")


@app.command()
def evaluate(
    golden_set: Annotated[Path, typer.Option(exists=True, readable=True)] = Path("golden_set.json"),
    output: Annotated[Path, typer.Option()] = Path("evaluation_assignment"),
    elastic_url: Annotated[str | None, typer.Option()] = None,
    elastic_index: Annotated[str, typer.Option()] = "legal-chunks-v1",
    embedding_model: Annotated[str, typer.Option()] = "sentence-transformers/all-mpnet-base-v2",
    k: Annotated[int, typer.Option(help="Top-k for retrieval-accuracy and answer context")] = 5,
    answer_mode: Annotated[SearchMode, typer.Option(help="Search mode used to generate answers for faithfulness")] = SearchMode.HYBRID,
    graph_dir: Annotated[Path, typer.Option(help="Directory containing graph_nodes.jsonl/graph_edges.jsonl")] = Path("output"),
    use_graph: Annotated[bool, typer.Option(help="Apply 1-hop citation-graph expansion, matching /answer")] = True,
) -> None:
    """Run the golden set against the system and produce an evaluation report.

    Faithfulness verdicts are left blank (judged_count=0) unless ANTHROPIC_API_KEY is
    set; otherwise fill them in afterward with legal_ingest.evaluate.apply_manual_judgments.
    """
    from openai import OpenAI

    from .evaluate import run_evaluation

    anthropic_client = None
    if os.environ.get("ANTHROPIC_API_KEY"):
        from anthropic import Anthropic

        anthropic_client = Anthropic()

    report = run_evaluation(
        golden_set,
        output,
        elastic_url=elastic_url or os.environ["ELASTIC_URL"],
        elastic_api_key=os.environ.get("ELASTIC_API_KEY"),
        elastic_index=elastic_index,
        embedding_model=embedding_model,
        openai_client=OpenAI(),
        anthropic_client=anthropic_client,
        k=k,
        answer_mode=answer_mode,
        graph_dir=graph_dir,
        use_graph=use_graph,
    )
    typer.echo(
        f"Retrieval accuracy: {report['retrieval_accuracy']} | "
        f"Faithfulness: {report['faithfulness_summary']}"
    )
    typer.echo(f"Report written to {output}/evaluation_report.{{json,md}}")


if __name__ == "__main__":
    app()
