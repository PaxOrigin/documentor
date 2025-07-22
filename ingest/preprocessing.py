"""Text preprocessing strategies for ingestion."""

from __future__ import annotations

import re
from typing import Callable, Dict


# Registry mapping strategy names to callables
_PREPROCESSORS: Dict[str, Callable[[str], str]] = {}


def register(name: str) -> Callable[[Callable[[str], str]], Callable[[str], str]]:
    """Decorator to register a preprocessing strategy."""

    def decorator(func: Callable[[str], str]) -> Callable[[str], str]:
        _PREPROCESSORS[name] = func
        return func

    return decorator


@register("basic")
def basic_preprocess(text: str) -> str:
    """Basic cleaning: remove table of contents, strip lines and collapse blanks."""

    lines = []
    skip = False
    for line in text.splitlines():
        stripped = line.strip()
        lower = stripped.lower()
        if not skip and "table of contents" in lower:
            skip = True
            continue
        if skip:
            if stripped == "":
                skip = False
            continue
        lines.append(stripped)

    cleaned = "\n".join(lines)
    cleaned = re.sub(r"\n{2,}", "\n\n", cleaned)
    return cleaned.strip()


@register("enrich")
def enrich_preprocess(text: str) -> str:
    """Basic cleaning with heading hierarchy appended."""
    cleaned = basic_preprocess(text)

    # extract headings hierarchy
    headings = []
    for line in cleaned.splitlines():
        match = re.match(r"(#+)\s+(.*)", line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            headings.append((level, title))

    if headings:
        hierarchy_lines = ["\n", "Headings:"]
        for level, title in headings:
            prefix = "  " * (level - 1) + "- "
            hierarchy_lines.append(f"{prefix}{title}")
        cleaned += "\n" + "\n".join(hierarchy_lines)

    return cleaned


def apply_preprocessing(strategy: str, text: str) -> str:
    """Apply the selected preprocessing strategy to text."""
    if strategy not in _PREPROCESSORS:
        available = ", ".join(sorted(_PREPROCESSORS))
        raise ValueError(f"Unknown preprocessing strategy '{strategy}'. Available: {available}")
    return _PREPROCESSORS[strategy](text)


__all__ = ["apply_preprocessing"]
