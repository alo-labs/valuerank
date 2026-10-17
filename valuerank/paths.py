"""Canonical repository locations shared by every pipeline stage."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
AA_DIR = DATA / "aa"
SITE = ROOT / "site"
