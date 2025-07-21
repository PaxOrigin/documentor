"""File loader helpers."""

from pathlib import Path
from typing import List


def load_markdown_files(directory: Path) -> List[Path]:
    """Return a list of markdown files in the directory."""
    return list(directory.glob("*.md"))
