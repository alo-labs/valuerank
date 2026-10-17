"""Behavior tests for the automatic DeepSWE v1.1 coding-agent capture (valuerank.fetch_deepswe).

``tests/fixtures/aa_coding_agents/coding-agents-reduced.html`` is a reduced copy of
the escaped Next.js flight payload of the Artificial Analysis coding-agents page.
Its rows are real rows cut from the page (heavy percentile/cost blocks removed),
plus four synthetic edge rows: a second agent running Opus 5.5 at a lower score
(duplicate roster mapping), a row without a DeepSWE evaluation, an unavailable
Muse row, and an explicit ``agentVersion`` key. The payload carries the two array
keys of the live page: ``rows`` and ``benchmarkRows``, the latter holding a Next.js
flight reference (``$1c:props:children:props:rows:0``) to the first row of the former.

Nothing here reaches artificialanalysis.ai; ``urllib.request.urlopen`` is patched
at the boundary and all output is written into temporary directories.
"""

from __future__ import annotations

import copy
import hashlib
import json
import runpy
import sys
import urllib.request
from pathlib import Path

import pytest

import valuerank.paths as paths
from valuerank import fetch_deepswe as stage

FIXTURE = Path(__file__).parent / "fixtures" / "aa_coding_agents" / "coding-agents-reduced.html"
PAGE = FIXTURE.read_text(encoding="utf-8")

GEMINI = "ef63fafa9b4a635522183c879ae8435b"
OPUS = "ab5074e4"
UNAVAILABLE_MUSE = "f0000000000000000000000000000003"
SECOND_AGENT = "f0000000000000000000000000000001"
NO_DEEPSWE = "f0000000000000000000000000000002"

ROSTER = {
    "claude-opus-5-5": {"displayName": "Claude Opus 5.5", "aaVariant": "max"},
    "gemini-4-argon": {"displayName": "Gemini 4 Argon", "aaVariant": "high"},
    "qwen3.8-max": {"displayName": "Qwen3.8 Max", "aaVariant": None},
    "kimi-k3": {"displayName": "Kimi K3", "aaVariant": "max"},
    "glm-5.3": {"displayName": "GLM-5.3", "aaVariant": "max"},
    "gpt-6.1-sol": {"displayName": "GPT-6.1 Sol", "aaVariant": "max"},
}


def eval_row(**overrides) -> dict:
    row = {
        "id": "row-1",
        "agentName": "Agent",
        "display": {"agent": "Agent", "model": "Model X"},
        "displayLabel": "Agent - Model X",
        "isUnavailable": False,
        "evals": [
            {
                "datasetIndexName": "deep-swe-v1.1",
                "evaluationDatasetSlug": "DeepSWE v1.1",
                "safety": {"attemptCount": 10},
                "mean": {"reward": 0.5, "inputTokens": 100.0, "outputTokens": 5.0},
            }
        ],
        "versions": {},
    }
    row.update(overrides)
    return row


def page_with(rows_array: str, key: str = "rows") -> str:
    """A minimal flight chunk embedding ``rows_array`` (a JSON text) under ``key``."""

    body = '1c:["$","div",null,{"%s":%s}]' % (key, rows_array)
    return "<script>self.__next_f.push([1,%s])</script>" % json.dumps(body)


# --- extraction -----------------------------------------------------------------


def test_extraction_decodes_both_arrays_and_dedupes_by_id():
    rows = stage.extract_deepswe_rows(PAGE)

    ids = [row["id"] for row in rows]
    assert len(ids) == len(set(ids))
    # `rows` holds 5 rows (one without DeepSWE); `benchmarkRows` holds 8 entries: a
    # reference to rows[0], an inline duplicate of Opus 5.5 and 6 new rows -> 10 distinct.
    assert len(rows) == 10
    assert ids.count(GEMINI) == 1
    assert [row["displayLabel"] for row in rows[:3]] == [
        "Antigravity CLI - Gemini 4 Argon (high)",
        "Claude Code - Opus 5.5 (max)",
        "Claude Code - Fable 5.1 (max) (with fallback)",
    ]


def test_extraction_drops_rows_without_a_deepswe_evaluation_but_keeps_unavailable_rows():
    rows = stage.extract_deepswe_rows(PAGE)

    ids = {row["id"] for row in rows}
    assert NO_DEEPSWE not in ids
    assert UNAVAILABLE_MUSE in ids
    assert next(row for row in rows if row["id"] == UNAVAILABLE_MUSE)["isUnavailable"] is True


def test_extraction_resolves_flight_references_to_the_rows_array():
    rows_array = json.dumps([eval_row(id="a"), eval_row(id="b")])
    bench = json.dumps(["$1c:props:children:props:rows:1", eval_row(id="c")])
    page = page_with(rows_array, "rows") + page_with(bench, "benchmarkRows")

    assert [row["id"] for row in stage.extract_deepswe_rows(page)] == ["a", "b", "c"]


def test_extraction_rejects_an_unresolvable_flight_reference():
    page = page_with(json.dumps([eval_row(id="a")]), "rows") + page_with(
        json.dumps(["$1c:props:children:props:rows:7"]), "benchmarkRows"
    )

    with pytest.raises(ValueError, match="unresolvable flight reference"):
        stage.extract_deepswe_rows(page)


def test_extraction_rejects_a_reference_when_there_is_no_rows_array():
    page = page_with(json.dumps(["$1c:props:children:props:rows:0"]), "benchmarkRows")

    with pytest.raises(ValueError, match="unresolvable flight reference"):
        stage.extract_deepswe_rows(page)


def test_extraction_rejects_unexpected_array_items():
    page = page_with(json.dumps([7]), "rows")

    with pytest.raises(ValueError, match="unexpected item"):
        stage.extract_deepswe_rows(page)


def test_extraction_rejects_a_page_without_row_arrays():
    with pytest.raises(ValueError, match="no coding-agent row arrays"):
        stage.extract_deepswe_rows("<html><body>nothing here</body></html>")


def test_extraction_rejects_a_truncated_array():
    truncated = '1c:{"rows":[{"id":"a"'
    page = "<script>self.__next_f.push([1,%s])</script>" % json.dumps(truncated)

    with pytest.raises(ValueError, match="truncated or malformed"):
        stage.extract_deepswe_rows(page)


def test_extraction_rejects_a_page_where_no_row_has_a_deepswe_evaluation():
    other = eval_row(evals=[{"datasetIndexName": "x", "evaluationDatasetSlug": "Other"}])
    page = page_with(json.dumps([other]), "rows")

    with pytest.raises(ValueError, match="no configuration with a DeepSWE v1.1 evaluation"):
        stage.extract_deepswe_rows(page)


# --- identity parsing -----------------------------------------------------------


def identity(agent: str, model: str, label: str) -> dict:
    return stage.parse_identity(
        eval_row(display={"agent": agent, "model": model}, displayLabel=label)
    )


@pytest.mark.parametrize(
    ("agent", "model", "label", "expected_model", "effort", "fallback"),
    [
        # Effort appears on the model, as on most Claude Code and Codex rows.
        ("Claude Code", "Sonnet 5.5 (max)", "Claude Code - Sonnet 5.5 (max)", "Sonnet 5.5", "max", False),
        # Effort only on the label (Gemini 4 Argon shows no suffix on display.model).
        ("Antigravity CLI", "Gemini 4 Argon", "Antigravity CLI - Gemini 4 Argon (high)", "Gemini 4 Argon", "high", False),
        # Effort only in the Python-dict suffix of the label (the Opencode GLM row).
        ("Opencode", "GLM-5.3", "Opencode - GLM-5.3 ({'reasoning_effort': 'max'})", "GLM-5.3", "max", False),
        # Both a dict suffix and an effort token on the model; the model token wins.
        ("Codex", "GPT-6.1 Sol (xhigh)", "Codex - GPT-6.1 Sol (xhigh) ({'reasoning_effort': 'xhigh'})", "GPT-6.1 Sol", "xhigh", False),
        # Fallback marker after the effort.
        ("Claude Code", "Fable 5.1 (max) (with fallback)", "Claude Code - Fable 5.1 (max) (with fallback)", "Fable 5.1", "max", True),
        # No effort anywhere.
        ("Kimi Code CLI", "Kimi K3", "Kimi Code CLI - Kimi K3", "Kimi K3", None, False),
        # Fallback with no effort.
        ("Agent", "Model Y (with fallback)", "Agent - Model Y (with fallback)", "Model Y", None, True),
        # A parenthetical that is not an effort stays part of the model name.
        ("Agent", "Model Z (Preview)", "Agent - Model Z (Preview)", "Model Z (Preview)", None, False),
        # Composite configurations keep their spelling and carry no effort token.
        ("Devin Fusion CLI", "GPT-6 Astra XHigh + SWE-2 Medium", "Devin Fusion CLI - GPT-6 Astra XHigh + SWE-2 Medium", "GPT-6 Astra XHigh + SWE-2 Medium", None, False),
        # A label that does not repeat the agent prefix still yields the effort.
        ("Agent", "Model Q", "Model Q (low)", "Model Q", "low", False),
    ],
)
def test_parse_identity_reads_model_effort_and_fallback(agent, model, label, expected_model, effort, fallback):
    assert identity(agent, model, label) == {
        "agent": agent,
        "model": expected_model,
        "effort": effort,
        "fallback": fallback,
    }


def test_parse_identity_reports_fallback_from_the_label_alone():
    result = identity("Agent", "Model Y (max)", "Agent - Model Y (max) (with fallback)")

    assert (result["model"], result["effort"], result["fallback"]) == ("Model Y", "max", True)


def test_parse_identity_rejects_a_row_without_display_names():
    with pytest.raises(ValueError, match="row-1 has no display agent/model"):
        stage.parse_identity(eval_row(display={}))


def test_agent_version_prefers_an_explicit_key_then_the_benchmark_version_range():
    explicit = eval_row(agentVersion="9.9.9", versions={"deep-swe-v1.1": {"min": {"version": "1"}, "max": {"version": "2"}}})
    same = eval_row(versions={"deep-swe-v1.1": {"min": {"version": "1.2.10"}, "max": {"version": "1.2.10"}}})
    ranged = eval_row(versions={"deep-swe-v1.1": {"min": {"version": "0.153.2"}, "max": {"version": "0.153.4"}}})
    other_only = eval_row(versions={"terminal-bench-v4": {"min": {"version": "1"}, "max": {"version": "1"}}})
    unset = eval_row(versions={"deep-swe-v1.1": {"min": {"version": None}, "max": {"version": None}}})

    assert stage.agent_version(explicit, "deep-swe-v1.1") == "9.9.9"
    assert stage.agent_version(same, "deep-swe-v1.1") == "1.2.10"
    assert stage.agent_version(ranged, "deep-swe-v1.1") == "0.153.2 to 0.153.4"
    assert stage.agent_version(other_only, "deep-swe-v1.1") is None
    assert stage.agent_version(unset, "deep-swe-v1.1") is None
    assert stage.agent_version({"id": "x", "evals": []}, "deep-swe-v1.1") is None


# --- exact-variant mapping ------------------------------------------------------


def config(model: str, effort: str | None, score: float = 50.0, *, agent: str = "Agent", fallback: bool = False, source_id: str | None = None) -> dict:
    return {
        "sourceId": source_id or f"{agent}-{model}-{effort}",
        "agent": agent,
        "model": model,
        "effort": effort,
        "fallback": fallback,
        "displayLabel": f"{agent} - {model} ({effort})" if effort else f"{agent} - {model}",
        "scorePct": score,
    }


def mapped(configs: list[dict], roster: dict = ROSTER) -> list[dict]:
    return stage.map_to_roster(copy.deepcopy(configs), roster)


def test_mapping_exact_variant_requires_family_and_effort():
    [result] = mapped([config("Gemini 4 Argon", "high")])

    assert result["valueRankModelId"] == "gemini-4-argon"
    assert result["matchStatus"] == "exact_variant"
    assert "Gemini 4 Argon" in result["matchNote"] and "high" in result["matchNote"]


def test_mapping_strips_the_claude_prefix_from_either_side():
    roster = {"claude-x": {"displayName": "Claude Opus 5.5", "aaVariant": "max"}, "plain": {"displayName": "Sonnet 5.5", "aaVariant": "max"}}

    chart_side = mapped([config("Opus 5.5", "max")], roster)[0]
    roster_side = mapped([config("Claude Sonnet 5.5", "max")], roster)[0]

    assert chart_side["valueRankModelId"] == "claude-x"
    assert roster_side["valueRankModelId"] == "plain"


def test_mapping_normalises_case_whitespace_and_hyphens():
    [result] = mapped([config("glm  5.3", "max")])

    assert result["valueRankModelId"] == "glm-5.3"


def test_mapping_treats_null_effort_on_both_sides_as_equal():
    [result] = mapped([config("Qwen3.8 Max", None)])

    assert (result["valueRankModelId"], result["matchStatus"]) == ("qwen3.8-max", "exact_variant")


def test_mapping_reports_effort_mismatch_when_the_chart_effort_is_present_and_differs():
    results = mapped([config("GPT-6.1 Sol", "xhigh"), config("Qwen3.8 Max", "max")])

    assert [r["matchStatus"] for r in results] == ["effort_mismatch"] * 2
    assert [r["valueRankModelId"] for r in results] == [None, None]
    assert "never substitutes" in results[0]["matchNote"]
    assert "max" in results[0]["matchNote"]  # names the roster effort
    assert "no effort" in results[1]["matchNote"]  # roster has no effort


def test_mapping_does_not_confirm_an_unlabelled_row_against_a_roster_effort():
    [result] = mapped([config("Kimi K3", None)])

    assert result["valueRankModelId"] is None
    assert result["matchStatus"] == "effort_unconfirmed"
    assert result["matchNote"] == (
        "The chart row shows no effort; the roster's selected configuration is max, "
        "so the variant cannot be confirmed and no result is transferred."
    )


def test_mapping_accepts_the_family_of_the_roster_short_name():
    roster = {
        "deepseek-v4-pro": {"displayName": "DeepSeek V4 Pro", "aaVariant": "max", "aaShortName": "DeepSeek V4 Pro 0813 (max)"},
        "deepseek-v4-flash": {"displayName": "DeepSeek V4 Flash", "aaVariant": "max", "aaShortName": "DeepSeek V4 Flash 0731 (max)"},
        "glm-flash": {"displayName": "GLM-5.3 Flash", "aaVariant": "max", "aaShortName": "GLM-5.3-Flash"},
        "qwen": {"displayName": "Qwen3.8 Max", "aaVariant": None, "aaShortName": "Qwen3.8 Max (0902)"},
    }

    pro, flash, glm, qwen = mapped(
        [
            config("DeepSeek V4 Pro 0813", "max"),
            config("DeepSeek V4 Flash 0731", "max"),
            config("GLM 5.3 flash", "max"),
            config("Qwen3.8 Max", None),
        ],
        roster,
    )
    [display] = mapped([config("DeepSeek V4 Pro", "max")], roster)

    assert (pro["valueRankModelId"], pro["matchStatus"]) == ("deepseek-v4-pro", "exact_variant")
    assert "AA short name 'DeepSeek V4 Pro 0813'" in pro["matchNote"]
    assert flash["valueRankModelId"] == "deepseek-v4-flash"
    assert "AA short name 'DeepSeek V4 Flash 0731'" in flash["matchNote"]
    # Where the short name has no parenthetical or equals the display name, the display name is reported.
    assert glm["valueRankModelId"] == "glm-flash"
    assert "display name 'GLM-5.3 Flash'" in glm["matchNote"]
    assert qwen["valueRankModelId"] == "qwen"
    assert "display name 'Qwen3.8 Max'" in qwen["matchNote"]
    assert display["valueRankModelId"] == "deepseek-v4-pro"
    assert "display name 'DeepSeek V4 Pro'" in display["matchNote"]


def test_short_name_family_keeps_the_effort_rules():
    roster = {"deepseek-v4-pro": {"displayName": "DeepSeek V4 Pro", "aaVariant": "max", "aaShortName": "DeepSeek V4 Pro 0813 (max)"}}

    mismatch, unconfirmed = mapped([config("DeepSeek V4 Pro 0813", "high"), config("DeepSeek V4 Pro 0813", None)], roster)

    assert mismatch["matchStatus"] == "effort_mismatch"
    assert unconfirmed["matchStatus"] == "effort_unconfirmed"


def test_mapping_reports_models_that_are_not_in_the_roster():
    results = mapped([config("Sonnet 5.5", "max"), config("Opus 5.5 Max + GPT-6 Luna High", None)])

    assert [r["matchStatus"] for r in results] == ["not_in_roster"] * 2
    assert [r["valueRankModelId"] for r in results] == [None, None]
    assert "No ValueRank roster model" in results[0]["matchNote"]
    assert "composite" in results[1]["matchNote"]


def test_mapping_ignores_the_fallback_marker_but_records_it():
    [result] = mapped([config("Opus 5.5", "max", fallback=True)])

    assert result["valueRankModelId"] == "claude-opus-5-5"
    assert "fallback" in result["matchNote"]


def test_mapping_keeps_only_the_higher_scoring_duplicate_configuration():
    low = config("Opus 5.5", "max", 60.0, agent="Second Agent", source_id="low")
    high = config("Opus 5.5", "max", 68.4, agent="Claude Code", source_id="high")

    results = mapped([low, high])
    by_id = {r["sourceId"]: r for r in results}

    assert by_id["high"]["valueRankModelId"] == "claude-opus-5-5"
    assert by_id["high"]["matchStatus"] == "exact_variant"
    assert by_id["low"]["valueRankModelId"] is None
    assert by_id["low"]["matchStatus"] == "duplicate_configuration"
    assert "Claude Code - Opus 5.5 (max)" in by_id["low"]["matchNote"]
    assert "source id high" in by_id["low"]["matchNote"]
    assert len(results) == 2


def test_mapping_duplicate_tie_keeps_the_earlier_row():
    first = config("Opus 5.5", "max", 60.0, agent="A", source_id="first")
    second = config("Opus 5.5", "max", 60.0, agent="B", source_id="second")

    by_id = {r["sourceId"]: r for r in mapped([first, second])}

    assert by_id["first"]["matchStatus"] == "exact_variant"
    assert by_id["second"]["matchStatus"] == "duplicate_configuration"


# --- document ---------------------------------------------------------------------

OBSERVED_AT = "2026-10-18T12:00:00Z"
PAGE_BYTES = FIXTURE.read_bytes()

EXPECTED_ORDER = [
    ("Antigravity CLI - Gemini 4 Argon (high)", 78.8),
    ("Devin Fusion CLI - Claude Opus 5.5 Max + GPT-6 Luna High", 72.6),
    ("Codex - GPT-6.1 Sol (medium) ({'reasoning_effort': 'medium'})", 72.0),
    ("Muse Code - Muse Spark 1.3 (max)", 71.7),
    ("Claude Code - Opus 5.5 (max)", 68.4),
    ("Kimi Code CLI - Kimi K3", 68.4),
    ("Claude Code - Fable 5.1 (max) (with fallback)", 64.3),
    ("Opencode - GLM-5.3 ({'reasoning_effort': 'max'})", 61.4),
    ("Claude Code - Qwen3.8 Max", 51.0),
    ("Second Agent - Opus 5.5 (max)", 50.0),
]

PREVIOUS = {
    "schemaVersion": "valuerank-aa-coding-agent-deepswe/v1",
    "observedAt": "2026-10-08",
    "configurations": [
        {"agent": "Antigravity CLI", "model": "Gemini 4 Argon", "effort": "high", "scorePct": 79, "observedAt": "2026-10-08"},
        {"agent": "Claude Code", "model": "Fable 5.1", "effort": "max with fallback", "scorePct": 64, "observedAt": "2026-10-08"},
        {"agent": "OpenCode", "model": "GLM-5.3", "effort": "max", "scorePct": 61, "observedAt": "2026-10-08"},
        {"agent": "Devin Fusion CLI", "model": "Claude Opus 5.5 max + GPT-6 Luna high", "effort": "composite", "scorePct": 70, "observedAt": "2026-10-08"},
        {"agent": "Claude Code", "model": "Qwen3.8 Max", "effort": None, "scorePct": 51, "observedAt": "2026-09-29"},
        {"agent": "Gone Agent", "model": "Gone Model", "effort": "max", "scorePct": 10, "observedAt": "2026-10-08"},
    ],
}


def build(previous: dict | None = None, roster: dict = ROSTER, page_bytes: bytes = PAGE_BYTES) -> dict:
    return stage.build_document(page_bytes, roster, previous, OBSERVED_AT)


def assert_build_scores_rules(document: dict, roster: dict) -> None:
    """The DeepSWE validation valuerank.build_scores applies to this document."""

    configurations = document["configurations"]
    n = document["observedConfigurationN"]
    assert not isinstance(n, bool) and isinstance(n, int) and n >= 1
    assert len(configurations) == n
    assert document["benchmarkTasks"] == 113
    mapped_ids = set()
    for item in configurations:
        model_id = item["valueRankModelId"]
        if model_id is None:
            continue
        assert item["matchStatus"] == "exact_variant"
        assert model_id not in mapped_ids
        mapped_ids.add(model_id)
        assert isinstance(item["scorePct"], (int, float)) and not isinstance(item["scorePct"], bool)
        assert 0 <= item["scorePct"] <= 100
    assert mapped_ids <= set(roster)


def test_document_header_and_source_metadata():
    document = build()

    assert document["schemaVersion"] == "valuerank-aa-coding-agent-deepswe/v2"
    assert document["benchmark"] == "DeepSWE v1.1"
    assert document["benchmarkTasks"] == 113
    assert document["observedConfigurationN"] == 10
    assert document["observedAt"] == OBSERVED_AT
    assert document["previousObservedAt"] is None
    source = document["source"]
    assert source["publisher"] == "Artificial Analysis"
    assert source["sourceType"] == "benchmark_owner"
    assert source["title"] == "Artificial Analysis Coding Agent Index v1.5 — DeepSWE v1.1"
    assert source["url"] == stage.URL
    assert source["url"].endswith("?coding-agents-performance-chart=deep-swe-v1.1")
    assert source["indexVersion"] == "v1.5"
    assert source["metric"] == "Pass@1 (%)"
    assert "three attempts per task" in source["methodology"]
    assert "full precision" in source["captureMethod"]
    assert source["captureSha256"] == hashlib.sha256(PAGE_BYTES).hexdigest()
    assert source["responseBytes"] == len(PAGE_BYTES)
    assert "Do not transfer scores across model versions" in document["selectionPolicy"]


def test_document_index_version_comes_from_the_page_with_a_default():
    newer = PAGE_BYTES.replace(b"Coding Agent Index v1.5", b"Coding Agent Index v2.0.1")
    bare = page_with(json.dumps([eval_row()]), "rows").encode()

    assert build(page_bytes=newer)["source"]["indexVersion"] == "v2.0.1"
    assert build(page_bytes=bare)["source"]["indexVersion"] == "v1.5"


def test_configurations_are_sorted_ranked_and_carry_full_precision_scores():
    configurations = build()["configurations"]

    assert [(c["displayLabel"], c["scorePct"]) for c in configurations] == EXPECTED_ORDER
    assert [c["sourceOrder"] for c in configurations] == list(range(1, 11))
    gemini = configurations[0]
    assert list(gemini) == [
        "sourceOrder", "sourceId", "agent", "model", "effort", "fallback", "displayLabel",
        "scorePct", "rewardMean", "attemptCount", "meanInputTokens", "meanOutputTokens",
        "scorePrecision", "agentVersion", "valueRankModelId", "matchStatus", "matchNote",
        "observedAt", "previouslyObservedAt", "previousScorePct",
    ]
    assert gemini["sourceId"] == GEMINI
    assert (gemini["agent"], gemini["model"], gemini["effort"], gemini["fallback"]) == (
        "Antigravity CLI", "Gemini 4 Argon", "high", False
    )
    assert gemini["rewardMean"] == 0.787610619469027
    assert gemini["attemptCount"] == 336
    assert gemini["meanInputTokens"] == 19901657.223214287
    assert gemini["meanOutputTokens"] == 152422.96130952382
    assert gemini["scorePrecision"] == "payload_full_precision"
    assert gemini["agentVersion"] == "1.2.10"
    assert gemini["observedAt"] == OBSERVED_AT


def test_configurations_map_against_the_roster_with_one_owner_per_model():
    configurations = {c["displayLabel"]: c for c in build()["configurations"]}

    outcomes = {label: (c["valueRankModelId"], c["matchStatus"]) for label, c in configurations.items()}
    assert outcomes == {
        "Antigravity CLI - Gemini 4 Argon (high)": ("gemini-4-argon", "exact_variant"),
        "Devin Fusion CLI - Claude Opus 5.5 Max + GPT-6 Luna High": (None, "not_in_roster"),
        "Codex - GPT-6.1 Sol (medium) ({'reasoning_effort': 'medium'})": (None, "effort_mismatch"),
        "Muse Code - Muse Spark 1.3 (max)": (None, "not_in_roster"),
        "Claude Code - Opus 5.5 (max)": ("claude-opus-5-5", "exact_variant"),
        "Kimi Code CLI - Kimi K3": (None, "effort_unconfirmed"),
        "Claude Code - Fable 5.1 (max) (with fallback)": (None, "not_in_roster"),
        "Opencode - GLM-5.3 ({'reasoning_effort': 'max'})": ("glm-5.3", "exact_variant"),
        "Claude Code - Qwen3.8 Max": ("qwen3.8-max", "exact_variant"),
        "Second Agent - Opus 5.5 (max)": (None, "duplicate_configuration"),
    }
    assert configurations["Muse Code - Muse Spark 1.3 (max)"]["matchNote"].endswith(
        "AA marks this configuration as unavailable."
    )
    assert "unavailable" not in configurations["Claude Code - Opus 5.5 (max)"]["matchNote"]
    assert "fallback" in configurations["Claude Code - Fable 5.1 (max) (with fallback)"]["matchNote"]
    assert configurations["Second Agent - Opus 5.5 (max)"]["agentVersion"] == "9.9.9"
    assert all(c["matchNote"] for c in configurations.values())


def test_document_satisfies_the_build_scores_validation_rules():
    assert_build_scores_rules(build(PREVIOUS), ROSTER)


def test_previous_capture_carries_over_dates_and_scores_and_drives_the_freshness_note():
    document = build(PREVIOUS)
    configurations = {c["displayLabel"]: c for c in document["configurations"]}

    gemini = configurations["Antigravity CLI - Gemini 4 Argon (high)"]
    assert (gemini["previouslyObservedAt"], gemini["previousScorePct"]) == ("2026-10-08", 79)
    # Legacy "max with fallback" effort, differently-cased agent and composite spellings still match.
    fable = configurations["Claude Code - Fable 5.1 (max) (with fallback)"]
    assert (fable["previouslyObservedAt"], fable["previousScorePct"]) == ("2026-10-08", 64)
    assert configurations["Opencode - GLM-5.3 ({'reasoning_effort': 'max'})"]["previousScorePct"] == 61
    devin = configurations["Devin Fusion CLI - Claude Opus 5.5 Max + GPT-6 Luna High"]
    assert devin["previousScorePct"] == 70
    qwen = configurations["Claude Code - Qwen3.8 Max"]
    assert (qwen["previouslyObservedAt"], qwen["previousScorePct"]) == ("2026-09-29", 51)
    new = configurations["Kimi Code CLI - Kimi K3"]
    assert (new["previouslyObservedAt"], new["previousScorePct"]) == (None, None)
    assert document["previousObservedAt"] == "2026-10-08"
    note = document["freshnessNote"]
    assert note.startswith("All 10 configurations with a DeepSWE v1.1 evaluation were captured automatically on 2026-10-18")
    assert "previous capture of 2026-10-08" in note
    assert "5 retained, 5 new and 1 removed" in note
    assert "4 map to an exact ValueRank roster variant" in note


def test_a_v2_previous_capture_matches_on_the_fallback_flag():
    first = build()
    second = stage.build_document(PAGE_BYTES, ROSTER, first, "2026-10-19T00:00:00Z")

    assert second["previousObservedAt"] == OBSERVED_AT
    assert [c["previousScorePct"] for c in second["configurations"]] == [score for _, score in EXPECTED_ORDER]
    assert "10 retained, 0 new and 0 removed" in second["freshnessNote"]


def test_without_a_previous_capture_the_note_says_so():
    document = build(None)

    assert "No previous capture was available for comparison." in document["freshnessNote"]
    assert all(c["previouslyObservedAt"] is None and c["previousScorePct"] is None for c in document["configurations"])


@pytest.mark.parametrize("reward", [None, True, "0.5", -0.1, 1.2])
def test_document_rejects_an_invalid_reward(reward):
    row = eval_row()
    row["evals"][0]["mean"]["reward"] = reward
    page = page_with(json.dumps([row]), "rows").encode()

    with pytest.raises(ValueError, match="row-1 has an invalid DeepSWE v1.1 reward"):
        build(page_bytes=page)


def test_document_survives_a_row_with_sparse_metrics():
    row = eval_row()
    row["evals"][0] = {"evaluationDatasetSlug": "DeepSWE v1.1", "mean": {"reward": 1}}
    page = page_with(json.dumps([row]), "rows").encode()

    [only] = build(page_bytes=page)["configurations"]

    assert (only["scorePct"], only["attemptCount"], only["meanInputTokens"], only["meanOutputTokens"]) == (100, None, None, None)
    assert only["agentVersion"] is None


# --- fetch and command line -------------------------------------------------------


class FakeResponse:
    def __init__(self, payload: bytes):
        self.payload = payload

    def read(self) -> bytes:
        return self.payload

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def make_data(tmp_path: Path, models: dict | None = None) -> Path:
    data = tmp_path / "data"
    data.mkdir()
    (data / "aa_metrics.json").write_text(json.dumps({"models": ROSTER if models is None else models}), encoding="utf-8")
    return data


def forbid_network(monkeypatch):
    def refuse(*args, **kwargs):
        raise AssertionError("the network must not be touched")

    monkeypatch.setattr(urllib.request, "urlopen", refuse)


def test_fetch_page_sends_the_project_user_agent_and_timeout(monkeypatch):
    seen = {}

    def fake_urlopen(request, timeout=None):
        seen.update(url=request.full_url, agent=request.get_header("User-agent"), timeout=timeout)
        return FakeResponse(b"payload")

    monkeypatch.setattr(urllib.request, "urlopen", fake_urlopen)

    assert stage.fetch_page() == b"payload"
    assert seen == {"url": stage.URL, "agent": "ValueRank/1.6 official-source-refresh", "timeout": 45}


def test_main_reads_a_saved_page_writes_the_document_and_summarises(monkeypatch, tmp_path, capsys, pinned_clock):
    forbid_network(monkeypatch)
    data = make_data(tmp_path)
    out = tmp_path / "out" / "deepswe.json"
    out.parent.mkdir()

    assert stage.main(["--html", str(FIXTURE), "--out", str(out)], data=data) == 0

    document = json.loads(out.read_text(encoding="utf-8"))
    assert document["observedAt"] == pinned_clock
    assert document["source"]["captureSha256"] == hashlib.sha256(PAGE_BYTES).hexdigest()
    assert_build_scores_rules(document, ROSTER)
    assert out.read_text(encoding="utf-8").endswith("}\n")
    assert not (data / "aa_deepswe.json").exists()
    summary = json.loads(capsys.readouterr().out)
    assert summary["observedConfigurationN"] == 10
    assert summary["output"] == str(out)
    assert summary["matchStatusCounts"] == {
        "duplicate_configuration": 1,
        "effort_mismatch": 1,
        "effort_unconfirmed": 1,
        "exact_variant": 4,
        "not_in_roster": 3,
    }
    assert summary["mappedModelIds"] == ["claude-opus-5-5", "gemini-4-argon", "glm-5.3", "qwen3.8-max"]


def test_main_fetches_the_live_page_into_the_data_directory_by_default(monkeypatch, tmp_path, capsys):
    data = make_data(tmp_path)
    seen = {}

    def fake_urlopen(request, timeout=None):
        seen["url"] = request.full_url
        return FakeResponse(PAGE_BYTES)

    monkeypatch.setattr(urllib.request, "urlopen", fake_urlopen)

    assert stage.main([], data=data) == 0

    assert seen["url"] == stage.URL
    document = json.loads((data / "aa_deepswe.json").read_text(encoding="utf-8"))
    assert document["observedConfigurationN"] == 10
    assert json.loads(capsys.readouterr().out)["output"] == str(data / "aa_deepswe.json")


def test_main_compares_against_the_file_it_is_about_to_replace(monkeypatch, tmp_path, capsys):
    forbid_network(monkeypatch)
    data = make_data(tmp_path)
    out = data / "aa_deepswe.json"
    out.write_text(json.dumps(PREVIOUS), encoding="utf-8")

    assert stage.main(["--html", str(FIXTURE)], data=data) == 0

    document = json.loads(out.read_text(encoding="utf-8"))
    assert document["previousObservedAt"] == "2026-10-08"
    assert "5 retained, 5 new and 1 removed" in document["freshnessNote"]
    assert json.loads(capsys.readouterr().out)["previousObservedAt"] == "2026-10-08"


def test_main_rejects_an_empty_roster(monkeypatch, tmp_path):
    forbid_network(monkeypatch)
    data = make_data(tmp_path, models={})

    with pytest.raises(ValueError, match="non-empty comparison roster"):
        stage.main(["--html", str(FIXTURE)], data=data)
    assert not (data / "aa_deepswe.json").exists()


def test_module_entrypoint_runs_main_and_exits_zero(monkeypatch, tmp_path, capsys):
    # runpy re-executes the file as __main__; drop the cached module so it runs fresh.
    monkeypatch.delitem(sys.modules, "valuerank.fetch_deepswe", raising=False)
    forbid_network(monkeypatch)
    data = make_data(tmp_path)
    # The entrypoint re-imports valuerank.paths, so redirecting DATA keeps the real repo untouched.
    monkeypatch.setattr(paths, "DATA", data)
    monkeypatch.setattr(sys, "argv", ["fetch_deepswe", "--html", str(FIXTURE)])

    with pytest.raises(SystemExit) as exit_info:
        runpy.run_module("valuerank.fetch_deepswe", run_name="__main__", alter_sys=True)

    assert exit_info.value.code == 0
    assert json.loads((data / "aa_deepswe.json").read_text(encoding="utf-8"))["observedConfigurationN"] == 10
    assert json.loads(capsys.readouterr().out)["observedConfigurationN"] == 10
