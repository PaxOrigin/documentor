"""Tokenization helpers."""


def get_token_count(text: str) -> int:
    """Return rough token count for text."""
    return len(text.split())
