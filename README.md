# DocuMentor

DocuMentor is an AI-powered developer assistant designed to help engineers, QA analysts, and service desk professionals navigate technical documentation efficiently.

Its goal is to answer technical questions about a codebase or system by parsing and understanding well-structured documentation (Markdown or PDF), and serving semantic search results that are context-aware and developer-friendly.

## MVP Scope (v0.1)

The MVP is a command-line tool (Typer-based) that allows you to:

- Ingest one or more `.md` files
- Parse and split them into smart, token-controlled chunks
- Extract and attach rich metadata to each chunk:
  - Section hierarchy
  - Presence of code or tables
  - Token count
  - Line numbers
- Embed those chunks using one or more embedding models
- Store them in a Pinecone vector DB
- Run semantic queries over the indexed chunks
- Perform automatic evaluation and ask for manual feedback
- Print final benchmark results in table format (per model/chunker/query)

## Architecture Overview

```
                    ┌────────────┐
                    │ Markdown   │
                    │  / PDF     │
                    └────┬───────┘
                         │
               ┌─────────▼──────────┐
               │ Parsing & Chunking │ ◄── (smart + token aware)
               └─────────┬──────────┘
                         │
               ┌─────────▼────────────┐
               │   Metadata Enriched  │
               │       Chunks         │
               └─────────┬────────────┘
                         │
               ┌─────────▼────────────┐
               │    Embedding Model   │ ◄── (OpenAI, MiniLM, etc.)
               └─────────┬────────────┘
                         │
               ┌─────────▼────────────┐
               │     Pinecone DB      │
               └─────────┬────────────┘
                         │
               ┌─────────▼────────────┐
               │  Query + Evaluation  │
               └──────────────────────┘
```

## Technologies

- CLI: Typer
- Embedding: OpenAI `text-embedding-3`, HuggingFace `MiniLM`, etc.
- Vector DB: Pinecone
- Tokenizer: `tiktoken`, `transformers.AutoTokenizer`, etc
- Auto Evaluation: Precision@k, token statistics, metadata scoring
- Manual Review: Console-based feedback prompt

## Sample Usage

```bash
# Ingest a Markdown file
python main.py ingest docs/fastapi.md --chunker heading --embedder openai

# Run queries
python main.py query "How is JWT authentication handled?"

# Benchmark all combinations
python main.py benchmark --questions queries/fastapi.jsonl
```

## Roadmap & Milestones

| Phase | Target Date | Notes |
|-------|-------------|-------|
| MVP (CLI, embeddings, query, auto-eval) | July 20, 2025 | Ingestion + Evaluation ready |
| Benchmarking + Manual Feedback | July 20, 2025 | Test set defined, feedback loop implemented |
| Frontend Prototype + RAG & ReRanking | July 30, 2025 | Basic React interface, reranking and LLM generation |
| Final Thesis Text & Polish | August 5, 2025 | Final cleanup, report writing, polishing |

## Planned Extensions

After the MVP, we plan to add:

- Reranking (cross-encoder or LLM-based)
- RAG generation (LLM-generated answer with citations)
- Code tracing + architecture inference
- Web interface (React + FastAPI)
- Multi-project and user authentication
- Golden Book support (for eval with expected answers)
- NER- or LLM-based tag generation
- Advanced feedback system (stored and visualized)

## Contributing

We’ll open contribution guidelines after the MVP is completed. For now, feel free to clone the repo, test locally, and suggest ideas or improvements via issues.

## License

MIT License – see [LICENSE](LICENSE) file for details.
