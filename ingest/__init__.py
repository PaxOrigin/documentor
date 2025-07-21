"""Ingestion pipeline modules."""

from .preprocess import preprocess_files
from .chunk import chunk_text
from .embed import embed_chunks
from .index import index_embeddings

__all__ = [
    "preprocess_files",
    "chunk_text",
    "embed_chunks",
    "index_embeddings",
]
