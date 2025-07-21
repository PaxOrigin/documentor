"""Text chunking utilities."""

from typing import List


def chunk_text(text: str, max_tokens: int = 512) -> List[str]:
    """Split text into roughly token-sized chunks.

    Parameters
    ----------
    text:
        The full text to split.
    max_tokens:
        Rough upper bound for tokens in each chunk.
    """
    # Placeholder simple line-based chunking
    words = text.split()
    chunks = []
    current = []
    for word in words:
        current.append(word)
        if len(current) >= max_tokens:
            chunks.append(" ".join(current))
            current = []
    if current:
        chunks.append(" ".join(current))
    return chunks
