"""Shared fixtures for the ValueRank test suite.

Tests must never write into the real repository. ``repo_copy`` builds a
temporary checkout containing the tracked ``data/`` snapshots, the committed
``site/`` output and the research manifest, mirroring the real layout so each
stage can run against ``root``/``data`` arguments that point at the copy.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

from valuerank.paths import ROOT

TRACKED_COPY_PATHS = ("valuerank", "data", "site", "research/2026-09-29-valuerank-refresh-v4-3-2")


def tracked_files(*paths: str) -> list[Path]:
    """Return the tracked and untracked-but-not-ignored files below ``paths`` (relative to the repo root)."""

    output = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard", "--", *paths],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout
    return [Path(item) for item in output.decode().split("\0") if item]


@pytest.fixture
def repo_copy(tmp_path: Path) -> Path:
    """A temporary repository root holding copies of the tracked data and site files."""

    root = tmp_path / "repo"
    for relative in tracked_files(*TRACKED_COPY_PATHS):
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / relative, target)
    return root


@pytest.fixture
def pinned_clock(monkeypatch: pytest.MonkeyPatch) -> str:
    """Pin ``VALUERANK_NOW`` to the instant stamped into the committed publication."""

    instant = "2026-10-23T06:26:23Z"
    monkeypatch.setenv("VALUERANK_NOW", instant)
    return instant
