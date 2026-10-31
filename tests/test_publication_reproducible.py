"""The committed publication must be a pure function of the committed snapshots.

Runs every offline stage as a subprocess inside a temporary copy of the
repository with the clock pinned to the committed observation instant and
asserts that each generated file, and the whole site/ tree, is byte-identical to the committed one.
"""

import subprocess
import sys

import pytest

from valuerank.paths import ROOT

OFFLINE_STAGES = (
    ("valuerank.build_scores",),
    ("valuerank.aa_reconciliation",),
    ("valuerank.emit_docs",),
    ("valuerank.site.build",),
)
GENERATED_FILES = (
    "data/scores.json",
    "data/coverage_matrix.json",
    "data/ranking_summary.json",
    "data/run_manifest.json",
    "data/aa_reconciliation_report.json",
    "README.md",
    "methodology.md",
    "scores.md",
    "raw-data.md",
)


def tree(root):
    """Every file under ``site/`` keyed by its path relative to ``root``."""

    return {str(path.relative_to(root)): path.read_bytes() for path in sorted((root / "site").rglob("*")) if path.is_file()}


def run_stage(root, module):
    completed = subprocess.run([sys.executable, "-m", module], cwd=root, capture_output=True, text=True)
    assert completed.returncode == 0, f"{module} failed:\n{completed.stderr}"
    return completed.stdout


@pytest.mark.integration
def test_offline_stages_regenerate_the_committed_publication(repo_copy, pinned_clock):
    for stage in OFFLINE_STAGES:
        run_stage(repo_copy, *stage)

    differing = [name for name in GENERATED_FILES if (repo_copy / name).read_bytes() != (ROOT / name).read_bytes()]
    assert differing == [], f"regenerated files differ from the committed publication: {differing}"
    regenerated, committed = tree(repo_copy), tree(ROOT)
    assert sorted(regenerated) == sorted(committed), "the build wrote a different set of site files"
    changed_site_files = [name for name in committed if regenerated[name] != committed[name]]
    assert changed_site_files == [], f"regenerated site files differ from the committed site: {changed_site_files}"


@pytest.mark.integration
def test_reconciliation_gate_blocks_a_stale_inventory(repo_copy, monkeypatch):
    # The committed AA inventory was observed 2026-10-30T22:15:18Z; more than MAX_AGE_DAYS (7) later it is stale.
    monkeypatch.setenv("VALUERANK_NOW", "2026-11-10T00:00:00Z")

    completed = subprocess.run(
        [sys.executable, "-m", "valuerank.aa_reconciliation"], cwd=repo_copy, capture_output=True, text=True
    )

    assert completed.returncode == 1
    assert "AA reconciliation blocked" in completed.stdout
    assert "Inventory is stale or future-dated" in completed.stdout
    report_only = subprocess.run(
        [sys.executable, "-m", "valuerank.aa_reconciliation", "--report-only"],
        cwd=repo_copy,
        capture_output=True,
        text=True,
    )
    assert report_only.returncode == 0
