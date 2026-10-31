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


def test_row_dates_follow_o69():
    """O69: a row after the cutoff's day stops; a cutoff-day row needs a recorded instant before the cutoff."""

    cutoff = "2026-10-25T09:56:47Z"
    assert tracks.check_row_date({"model": "M", "harness": "H", "tested": "2026-10-24"}, cutoff) is None
    kimi = {"model": "Kimi K3.1 Pro (Max)", "harness": "OpenCode", "tested": "2026-10-25", "rawCells": ["8", "10 hours ago OpenCode"]}
    # I60 L2, reviewer 72: the bound the archived read supports (read at 10:44:11Z, shown "10 hours ago": at least 9 hours), not a typed minute.
    read = ("research/2026-10-25-board-reread/aicd/leaderboard-allrows-parsed.json", "2026-10-25T10:44:11Z")  # the 2026-10-25 read
    assert "tested between 2026-10-25T00:00:00Z and 2026-10-25T01:44:11Z" in tracks.check_row_date(kimi, cutoff, read)
    assert "and 2026-10-25T10:15:11Z" in tracks.check_row_date({**kimi, "rawCells": ["30 minutes ago"]}, "2026-10-25T10:30:00Z", read)
    for row, message in (({"model": "M", "harness": "H", "tested": "2026-10-26"}, "after the cutoff's day"),
                         ({"model": "M", "harness": "H", "tested": "2026-10-25"}, "without a recorded instant")):
        with pytest.raises(ValueError, match=message):
            tracks.check_row_date(row, cutoff)
    with pytest.raises(ValueError, match="without a recorded instant"):
        tracks.check_row_date(kimi, "2026-10-25T00:30:00Z", read)
