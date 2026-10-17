"""Shared helpers for the emit_docs test modules (no tests live here)."""

from __future__ import annotations

import ast
import json
import re
from pathlib import Path

from valuerank import emit_docs
from valuerank.paths import ROOT

SITE = "site/index.html"
CODING = "site/coding-agents/index.html"


def emit(repo: Path) -> int:
    """Run the emitter against a repo copy."""

    return emit_docs.main(root=repo, data=repo / "data")


def site_text(repo: Path) -> str:
    return (repo / SITE).read_text()


def edit_site(repo: Path, transform) -> str:
    """Apply ``transform`` to the copy's site/index.html and return the original text."""

    path = repo / SITE
    original = path.read_text()
    updated = transform(original)
    assert updated != original, "the variant did not change the page"
    path.write_text(updated)
    return original


def edit_json(repo: Path, relative: str, mutate) -> dict:
    path = repo / "data" / relative
    document = json.loads(path.read_text())
    mutate(document)
    path.write_text(json.dumps(document, ensure_ascii=False, indent=2))
    return document


def main_literal(name: str):
    """Literal value assigned to ``name`` inside ``emit_docs.main`` (read from the source)."""

    tree = ast.parse(Path(emit_docs.__file__).read_text())
    main = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "main")
    for node in ast.walk(main):
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets):
            return ast.literal_eval(node.value)
    raise LookupError(name)


def committed(name: str) -> str:
    return (ROOT / name).read_text()


def strip_block(html: str, pattern: str) -> str:
    return re.sub(pattern, "", html, count=1, flags=re.S)
