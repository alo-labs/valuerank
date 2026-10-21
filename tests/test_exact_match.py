"""Tests for exact-configuration matching of Terminal-Bench and Bug Hunt evidence."""

from __future__ import annotations

import pytest

from valuerank import exact_match as em


def test_split_effort():
    assert em.split_effort("Opus 5.5 (max)") == ("Opus 5.5", "max")
    assert em.split_effort("GLM-5.3-Flash (none)") == ("GLM-5.3-Flash", "none")
    assert em.split_effort(" Gemini 3.8 Flash ") == ("Gemini 3.8 Flash", None)


def test_efforts_match_requires_the_same_label_or_a_documented_equivalent():
    assert em.efforts_match("gpt-6.1-sol", "max", "Max") is True
    assert em.efforts_match("gpt-6-astra", "xhigh", "max") is False
    assert em.efforts_match("qwen3.8-max", None, "max") is True
    assert em.efforts_match("mimo-v2-6-pro", None, "enabled") is True
    assert em.efforts_match("qwen3.8-max", None, "high") is False
    assert em.efforts_match("unknown-model", None, "max") is False
    assert em.efforts_match("unknown-model", None, None) is True  # both unlabeled


ROWS = [
    {"model": "Opus 5.5 (max)", "agent": "Claude Code", "resolutionRatePct": 64.8},
    {"model": "GPT-6 Astra (max)", "agent": "Codex", "resolutionRatePct": 58.2},
    {"model": "Gemini 3.8 Flash (high)", "agent": "Gemini CLI", "resolutionRatePct": 22.0},
    {"model": "Gemini 3.8 Flash (high)", "agent": "mini-SWE-agent", "resolutionRatePct": 19.1},
    {"model": "Qwen3.8-Max-0902 (max)", "agent": "Claude Code", "resolutionRatePct": 27.0},
    {"model": "Fable 5.1 (max)", "agent": "Claude Code", "resolutionRatePct": 57.9},
    {"model": "Grok 4.7 (xhigh)", "agent": "Zeta Agent", "resolutionRatePct": 30.0},
    {"model": "Grok 4.7 (xhigh)", "agent": "Alpha Agent", "resolutionRatePct": 37.6},
]


def test_select_tb4_row_exact_configuration_and_agent_preference():
    assert em.select_tb4_row("claude-opus-5-5", "max", ROWS)["resolutionRatePct"] == 64.8
    # GPT-6 Astra is ranked at xhigh; the leaderboard row is max, so the leaf is missing.
    assert em.select_tb4_row("gpt-6-astra", "xhigh", ROWS) is None
    # The vendor-neutral harness wins even though the vendor CLI scored higher.
    assert em.select_tb4_row("gemini-3.8-flash", "high", ROWS)["agent"] == "mini-SWE-agent"
    assert em.select_tb4_row("qwen3.8-max", None, ROWS)["resolutionRatePct"] == 27.0
    # Agents outside the preference list are ordered by name, never by score.
    assert em.select_tb4_row("grok-4.7", "xhigh", ROWS)["agent"] == "Alpha Agent"
    assert em.select_tb4_row("claude-fable-5", "max", ROWS) is None


def test_select_tb4_row_gives_each_ranked_effort_of_a_family_only_its_own_row():
    """O33: a base name shared by several ranked efforts maps each effort to its own row, never to a sibling's."""

    rows = [{"model": "Muse Spark 1.3 (xhigh)", "agent": "Muse Code", "resolutionRatePct": 14.5},
            {"model": "GPT-6.1 Sol (max)", "agent": "Codex", "resolutionRatePct": 58.2}]
    assert em.select_tb4_row("muse-spark-1-3-xhigh", "xhigh", rows) == rows[0]
    assert em.select_tb4_row("muse-spark-1-3", "max", rows) is None
    assert em.select_tb4_row("gpt-6.1-sol", "max", rows) == rows[1]
    assert em.select_tb4_row("gpt-6.1-sol-xhigh", "xhigh", rows) is None
    assert em.tb4_model_ids("Opus 5.5") == ("claude-opus-5-5",)
    assert em.tb4_model_ids("Unknown") == ()


def test_select_tb4_row_handles_rows_without_an_agent():
    rows = [{"model": "GLM-5.3 (max)", "resolutionRatePct": 41.8}]
    assert em.select_tb4_row("glm-5.3", "max", rows) == rows[0]


def test_bug_hunt_matches_owner_matched_exact_effort_records_only():
    assert em.bug_hunt_matches("gpt-6.1-sol", "max", {"matched": True, "effort": "max", "fixedOf105": 44.3}) is True
    assert em.bug_hunt_matches("gpt-6-astra", "xhigh", {"matched": True, "effort": "max", "fixedOf105": 45.0}) is False
    assert em.bug_hunt_matches("mimo-v2-6-flash", None, {"matched": False, "effort": None, "fixedOf105": None}) is False
    assert em.bug_hunt_matches("x", "max", {"matched": True, "effort": "max", "fixedOf105": None}) is False
    assert em.bug_hunt_matches("x", "max", None) is False


def test_a_second_row_for_the_chosen_agent_stops_the_build():
    """E225: two tbench.ai rows for the same model, effort and agent are never chosen between silently."""

    rows = [{"model": "Opus 5.5 (max)", "agent": "Claude Code", "resolutionRatePct": 64.8},
            {"model": "Opus 5.5 (max)", "agent": "Claude Code", "resolutionRatePct": 60.0}]
    with pytest.raises(ValueError, match=r"several rows for agent Claude Code; .*\(E225\)"):
        em.select_tb4_row("claude-opus-5-5", "max", rows)
