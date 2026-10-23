"""E268: the AI Coding Daily row chosen when the board lists a configuration twice (research build script)."""

from __future__ import annotations

import importlib.util

import pytest

from valuerank.paths import ROOT

SPEC = importlib.util.spec_from_file_location("build_swe_tracks", ROOT / "research" / "2026-10-23-swe-benchmarks" / "build_swe_tracks.py")
tracks = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(tracks)


def row(harness, tested, total=1.0):
    return {"harness": harness, "tested": tested, "laravel": total, "react": 0, "edge": 0}


def test_selection_prefers_the_bug_hunt_harness_then_the_latest_date_then_stops(monkeypatch):
    monkeypatch.setattr(tracks, "bug_hunt_harness", lambda model_id: "DeepSeek Harness / DeepSeek API")
    one, other = row("deepseek harness", "2026-10-01"), row("OpenCode", "2026-10-05")
    assert tracks.select_aicd("m", "M", {"M": [other, one]})["row"] is one
    assert tracks.select_aicd("m", "M", {"M": [one]}) == {"row": one, "alternates": []}
    late = row("DeepSeek Harness", "2026-10-09")
    chosen = tracks.select_aicd("m", "M", {"M": [one, late, other]})
    assert chosen["row"] is late and chosen["rule"] == "the latest test date" and chosen["alternates"] == [one, other]
    monkeypatch.setattr(tracks, "bug_hunt_harness", lambda model_id: None)
    assert tracks.select_aicd("m", "M", {"M": [one, other]})["row"] is other
    with pytest.raises(ValueError, match="the rule cannot pick one"):
        tracks.select_aicd("m", "M", {"M": [row("A", "2026-10-05"), other]})


def test_the_real_board_selects_deepseeks_harness_row():
    chosen = tracks.select_aicd("deepseek-v4-1-flash-1017", "Deepseek-V4.1-Flash-1017 (Max)", tracks.aicd_rows())
    assert chosen["row"]["harness"] == "DeepSeek Harness" and tracks.aicd_points(chosen["row"]) == 52.24
