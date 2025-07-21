"""Embedding utilities."""

from typing import List


def embed_chunks(chunks: List[str]) -> List[List[float]]:
    """Embed text chunks into vectors.

    Parameters
    ----------
    chunks:
        Text chunks to embed.
    """
    # Placeholder: return zero vectors
    return [[0.0] * 3 for _ in chunks]
