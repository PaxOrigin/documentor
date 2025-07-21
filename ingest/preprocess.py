"""Preprocessing utilities for DocuMentor ingestion pipeline."""

from pathlib import Path
from typing import List


def preprocess_files(paths: List[Path]) -> List[str]:
    """Load and clean files, returning raw text for further processing.

    Parameters
    ----------
    paths:
        List of file paths to load.

    Returns
    -------
    List[str]
        Raw contents of each file as a string.
    """
    texts = []
    for path in paths:
        with open(path, "r", encoding="utf-8") as f:
            texts.append(f.read())
    return texts
