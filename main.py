"""DocuMentor CLI entry point."""

import typer

from ingest import preprocess_files, chunk_text, embed_chunks, index_embeddings
from query import semantic_search, rerank_results, generate_answer
from evaluate import evaluate_results, prompt_feedback

app = typer.Typer(add_completion=False)


@app.command()
def ingest(paths: list[str] = typer.Argument(...)) -> None:
    """Ingest markdown files."""
    texts = preprocess_files([typer.Path(p) for p in paths])
    for text in texts:
        chunks = chunk_text(text)
        embeddings = embed_chunks(chunks)
        index_embeddings(embeddings)


@app.command()
def query(question: str) -> None:
    """Query indexed data."""
    results = semantic_search(question)
    results = rerank_results(results)
    answer = generate_answer(question, results)
    typer.echo(answer)


@app.command()
def benchmark() -> None:
    """Run evaluation benchmarks."""
    results = []
    ground_truth = []
    metrics = evaluate_results(results, ground_truth)
    typer.echo(metrics)


if __name__ == "__main__":
    app()
