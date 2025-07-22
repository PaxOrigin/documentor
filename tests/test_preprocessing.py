import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from ingest.preprocessing import apply_preprocessing

SAMPLE_MD = """# Title

## Table of Contents
- [Intro](#intro)
- [Usage](#usage)

# Intro

Some text.

# Usage
More text.
"""

def test_basic_strategy() -> None:
    cleaned = apply_preprocessing("basic", SAMPLE_MD)
    assert "Table of Contents" not in cleaned
    assert "- [Intro]" not in cleaned
    assert cleaned.startswith("# Title")


def test_enrich_strategy() -> None:
    enriched = apply_preprocessing("enrich", SAMPLE_MD)
    assert "Headings:" in enriched
    assert "- Intro" in enriched
    assert enriched.count("# Intro") == 1


def test_unknown_strategy() -> None:
    try:
        apply_preprocessing("unknown", SAMPLE_MD)
    except ValueError as e:
        assert "Unknown preprocessing strategy" in str(e)
    else:
        assert False, "Expected ValueError"
