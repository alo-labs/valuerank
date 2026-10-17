"""Write the public JSON files (``site/data/``) from the committed snapshots.

``export_public_data(data, out)`` returns the sorted list of files written: ``rankings.json``,
``plans.json``, ``benchmarks.json``, ``changelog.json``, ``livebench.json``, ``benchmarks/terminal-bench-4.json`` and
``models/<slug>.json``. Output is deterministic: two-space indent, UTF-8 without escapes, a
trailing newline, ``NaN``/``Infinity`` rejected, and field order fixed by the view models.
"""

from __future__ import annotations

import json
from pathlib import Path

from valuerank.paths import DATA
from valuerank.site.viewmodel import build_bundle


def _write(path: Path, document) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(document, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    return path


def export_public_data(data: Path = DATA, out: Path = DATA.parent / "site" / "data") -> list[Path]:
    bundle = build_bundle(data)
    documents = {
        "rankings.json": bundle.rankings,
        "plans.json": bundle.plans,
        "benchmarks.json": bundle.benchmarks,
        "benchmarks/terminal-bench-4.json": bundle.tb4,
        "changelog.json": bundle.changelog,
        "livebench.json": bundle.livebench,
        **{f"models/{slug}.json": document for slug, document in bundle.models.items()},
    }
    return sorted(_write(out / relative, document) for relative, document in documents.items())
