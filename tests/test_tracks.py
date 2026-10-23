"""O53-O55: the two rankings' leaf sets, their evidence file, per-ranking files and the added leaves' noise."""

from __future__ import annotations

import pytest

from valuerank import quality as q
from valuerank import value_v3 as v

DOCUMENT = {
    "sources": {
        "vibeCode": {"benchmark": "Vibe Code Bench v1.1", "publisher": "Vals AI", "updated": "2026-10-20", "url": "https://www.vals.ai/benchmarks/vibe-code",
                     "harness": "OpenHands", "unit": "percent"},
        "aiCodingDaily": {"benchmark": "AI Coding Daily", "publisher": "AI Coding Daily", "updated": "2026-10-21", "url": "https://aicodingdaily.com/leaderboard",
                          "harness": "varies", "unit": "points of 60"},
    },
    "records": [
        {"modelId": "a", "leaf": "vibeCode", "value": 90.0, "stderr": 1.5, "sourceLabel": "vendor/a", "effort": "max"},
        {"modelId": "a", "leaf": "aiCodingDaily", "value": 45.0, "sourceLabel": "A (High)", "effort": "high", "match": "owner (O54)"},
    ],
}


def evidence(track: str) -> dict:
    page = {"slug": "a-max", "terminalBench40": None}
    with q.active_track(track):
        return v.leaf_evidence("a", "max", page, [], None, {}, v.track_records({"sweTracks": DOCUMENT}))


def test_track_records_attach_their_source_and_score_only_in_their_ranking():
    max_effort, aicd = evidence("max"), evidence("aicd")
    assert set(max_effort["observations"]) == {"vibeCode"} and set(aicd["observations"]) == {"aiCodingDaily"}
    vibe = max_effort["provenance"]["vibeCode"]
    assert max_effort["observations"]["vibeCode"].z == 90.0 and vibe["stderr"] == 1.5 and vibe["source"] == "Vals AI: Vibe Code Bench v1.1"
    assert vibe["evidence"] == {"artifact": "data/swe_tracks.json", "locator": "records[modelId=a, leaf=vibeCode].value", "publishedValue": 90.0}
    assert aicd["observations"]["aiCodingDaily"].z == pytest.approx(75.0) and aicd["provenance"]["aiCodingDaily"]["match"] == "owner (O54)"
    assert v.track_records({}) == {}


def test_a_published_standard_error_is_the_leaf_noise():
    assert v.sampling_sd("vibeCode", q.Observation(90.0), {"stderr": 1.5}) == 1.5
    # LiveBench 2.0 Long Agentic: 18 tasks under the independent-task approximation.
    p = (0.5 * 18 + 0.5) / 19
    assert v.sampling_sd("livebenchAgentic", q.Observation(50.0), {}) == pytest.approx(100 * (p * (1 - p) / 18) ** 0.5)


def test_each_ranking_keeps_its_own_files_and_summary():
    assert v.track_file("v3_frozen.json", "max") == "v3_frozen.json"
    assert v.track_file("v3_scenarios.json", "aicd") == "v3_scenarios_aicd.json"
    summary = v.track_summary("aicd")
    assert summary["key"] == "aicd" and summary["default"] is False and summary["label"] == "AI Coding Daily ranking"
    assert sum(leaf["weight"] for leaf in summary["leaves"]) == pytest.approx(100.0)
    assert v.track_summary("max")["default"] is True
    with q.active_track("aicd"):
        assert {leaf.key for leaf in v.aa_leaves()} | {leaf.key for leaf in v.independent_leaves()} == set(q.LEAF_BY_KEY)
        assert "aiCodingDaily" in {leaf.key for leaf in v.independent_leaves()}
        assert v.source_leaves()["Artificial Analysis"][:2] == ("frontierCode", "terminalBench")


def test_a_publisher_of_two_leaves_is_a_source_branch():
    """E258: in the max-effort ranking Vals AI and LiveBench each publish two leaves, so each has a leave-one-source-out
    branch, and their leaves carry only the leave-one-benchmark-out label; Bug Hunt stays a single-leaf source."""

    branches = {branch["id"]: branch for branch in v.deletion_branches()}
    assert branches["leave-source-out:Vals AI"]["removed"] == ["vibeCode", "codeMigration"]
    assert branches["leave-source-out:LiveBench"]["removed"] == ["livebenchAgentic", "livebenchCoding"]
    assert branches["leave-out:vibeCode"]["labels"] == ["leave-one-benchmark-out"]
    assert branches["leave-out:bugHunt"]["labels"] == ["leave-one-benchmark-out", "leave-one-source-out"]
    with q.active_track("aicd"):
        assert set(v.source_leaves()) == {"Artificial Analysis"}
