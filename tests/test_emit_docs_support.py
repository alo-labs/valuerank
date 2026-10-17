"""Shared helpers for the emit_docs test modules (no tests live here)."""

from __future__ import annotations

import json
from pathlib import Path

from valuerank import emit_docs
from valuerank.paths import ROOT

MARKDOWN_OUTPUTS = ("README.md", "methodology.md", "scores.md", "raw-data.md")


def emit(repo: Path) -> int:
    """Run the emitter against a repo copy."""

    return emit_docs.main(root=repo, data=repo / "data")


def edit_json(repo: Path, relative: str, mutate) -> dict:
    path = repo / "data" / relative
    document = json.loads(path.read_text())
    mutate(document)
    path.write_text(json.dumps(document, ensure_ascii=False, indent=2))
    return document


def committed(name: str) -> str:
    return (ROOT / name).read_text()
