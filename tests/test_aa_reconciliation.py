"""Behavior tests for the AA frontier reconciliation gate."""

from __future__ import annotations

import copy
import json
import runpy
import sys
from datetime import datetime, timezone

import pytest

from valuerank import aa_reconciliation as rec

NOW = datetime(2026, 10, 7, 17, 23, 20, tzinfo=timezone.utc)
OBSERVED = "2026-10-06T17:23:20Z"
VERSION = "Artificial Analysis Intelligence Index v4.3.2"


def row(aa_id="model-a", name="Model A (high)", **extra):
    base = {"aaId": aa_id, "name": name, "sourceUrl": f"https://artificialanalysis.ai/models/{aa_id}",
            "evaluatedVariant": "high", "isReasoning": True, "intelligenceIndex": 70, "totalCostUsd": 100.0,
            "directlyObservedFrontier": True, "family": "Family A", "requiredFamilyModelId": "m-a"}
    base.update(extra)
    return base


def inventory(**overrides):
    doc = {"observedAt": OBSERVED, "benchmarkVersion": VERSION, "sourceUrl": "https://artificialanalysis.ai/models",
           "scope": "Intelligence vs total cost", "completeness": {"status": "complete", "note": "all points read"},
           "mode": "observedFrontier",
           "sourceUniverse": {"selectedModelN": 5, "plottedPointN": 3, "observedFrontierPointN": 1},
           "rows": [row()]}
    doc.update(overrides)
    return doc


ROSTER = {"m-a": {"aaSlug": "model-a", "aaVariant": "high", "aaName": "Model A (high)", "aaShortName": "A",
                  "isReasoning": True}}
SCORES = {"models": [{"id": "m-a", "rankingEligible": True, "rankingExclusionReasons": []}]}


@pytest.fixture
def world(tmp_path, monkeypatch):
    root = tmp_path / "root"
    data = root / "data"
    data.mkdir(parents=True)
    monkeypatch.setattr(rec, "ROOT", root)
    monkeypatch.setattr(rec, "DATA", data)
    monkeypatch.setattr(rec, "INVENTORY", data / "aa_reconciliation_inventory.json")
    monkeypatch.setattr(rec, "REPORT", data / "aa_reconciliation_report.json")

    class World:
        pass

    w = World()
    w.root, w.data = root, data

    def setup(doc=None, roster=ROSTER, scores=SCORES, version=VERSION):
        if doc is not None:
            (data / "aa_reconciliation_inventory.json").write_text(json.dumps(doc))
        if roster is not None:
            (data / "aa_metrics.json").write_text(json.dumps({"benchmarkVersion": version, "models": roster}))
        if scores is not None:
            (data / "scores.json").write_text(json.dumps(scores))

    w.setup = setup
    return w


def run(world, doc=None, **kwargs):
    world.setup(inventory() if doc is None else doc, **kwargs)
    return rec.reconcile(NOW)


def has_issue(report, fragment):
    return any(fragment in issue for issue in report["issues"])


# --------------------------------------------------------------------------- small helpers


@pytest.mark.parametrize("value, expected", [(1, True), (1.5, True), (True, False), (float("nan"), False),
                                              (float("inf"), False), ("1", False), (None, False)])
def test_number_accepts_only_finite_real_numbers(value, expected):
    assert rec.number(value) is expected


@pytest.mark.parametrize("value, expected", [("https://artificialanalysis.ai/models/x", True),
                                              ("http://artificialanalysis.ai/models/x", False),
                                              ("https://evil.example/models/x", False), (None, False), (5, False)])
def test_aa_url_requires_https_first_party_host(value, expected):
    assert rec.aa_url(value) is expected


def test_read_json_and_variant_key(tmp_path):
    path = tmp_path / "x.json"
    path.write_text('{"a": 1}')
    assert rec.read_json(path) == {"a": 1}
    assert rec.variant_key({"aaId": "a", "name": "N"}) == ("a", "N")
    assert rec.variant_key({"aaId": "a", "name": "N", "evaluatedVariant": "high"}) == ("a", "high")


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Model (High)", {"effort": "high", "ambiguous": False, "reasoning": None, "fallback": False}),
        ("gpt_x-xhigh", {"effort": "xhigh", "ambiguous": False, "reasoning": None, "fallback": False}),
        ("Claude Non-Reasoning", {"effort": None, "ambiguous": False, "reasoning": False, "fallback": False}),
        ("claude non reasoning low", {"effort": "low", "ambiguous": False, "reasoning": False, "fallback": False}),
        ("Adaptive Reasoning Max", {"effort": "max", "ambiguous": False, "reasoning": True, "fallback": False}),
        ("high or low", {"effort": None, "ambiguous": True, "reasoning": None, "fallback": False}),
        ("Fallback mini", {"effort": "mini", "ambiguous": False, "reasoning": None, "fallback": True}),
        (None, {"effort": None, "ambiguous": False, "reasoning": None, "fallback": False}),
    ],
)
def test_canonical_variant_splits_effort_reasoning_and_fallback(text, expected):
    assert rec.canonical_variant(text) == expected


@pytest.mark.parametrize(
    "declared, label, reasoning, expected",
    [
        ("high", "Model (high)", None, {"effort": "high", "reasoning": None, "fallback": False}),
        (None, "Model (low)", True, {"effort": "low", "reasoning": True, "fallback": False}),
        ("reasoning", "Model", None, {"effort": None, "reasoning": True, "fallback": False}),
        ("fallback", "Model", None, {"effort": None, "reasoning": None, "fallback": True}),
        (None, "Model (fallback)", None, {"effort": None, "reasoning": None, "fallback": True}),
        ("gibberish", "Model", None, None),  # declared text carrying no recognised facet
        ("high low", "Model", None, None),  # ambiguous declaration
        ("high", "Model (low, medium)", None, None),  # ambiguous label
        ("high", "Model (low)", None, None),  # effort contradiction
        ("reasoning", "Model non-reasoning", None, None),  # mode contradiction
        ("reasoning", "Model", False, None),  # explicit boolean contradiction
    ],
)
def test_combined_variant_merges_or_rejects_contradictions(declared, label, reasoning, expected):
    assert rec.combined_variant(declared, label, reasoning) == expected


# --------------------------------------------------------------------------- exact_roster_match


def roster_item(**overrides):
    base = {"aaSlug": "model-a", "aaVariant": "high", "aaName": "Model A (high)", "aaShortName": "A", "isReasoning": True}
    base.update(overrides)
    return base


def test_exact_roster_match_single_match_returns_model_id():
    assert rec.exact_roster_match(row(), [("m-a", roster_item()), ("other", roster_item(aaSlug="other"))]) == "m-a"


def test_exact_roster_match_matches_by_short_name_or_declared_variant():
    short = roster_item(aaName="Other Name", aaShortName="Model A (high)")
    assert rec.exact_roster_match(row(evaluatedVariant=None), [("s", short)]) == "s"
    # With a declared variant, display-name equality is not required.
    assert rec.exact_roster_match(row(name="Renamed (high)"), [("m", roster_item(aaName="x", aaShortName="y"))]) == "m"


def test_exact_roster_match_ambiguous_returns_none():
    pair = [("one", roster_item()), ("two", roster_item())]
    assert rec.exact_roster_match(row(), pair) is None


def test_exact_roster_match_none_for_unmatched_inputs():
    assert rec.exact_roster_match(row(), []) is None
    assert rec.exact_roster_match(row(), [("m", roster_item(aaSlug="elsewhere"))]) is None  # slug differs
    assert rec.exact_roster_match(row(), [("m", roster_item(aaVariant="low", aaName="Model A (low)"))]) is None  # effort differs
    assert rec.exact_roster_match(row(), [("m", roster_item(aaVariant="nonsense", aaName="x"))]) is None  # unsupported roster label
    assert rec.exact_roster_match(row(), [("m", roster_item(aaVariant="high (fallback)"))]) is None  # fallback differs
    assert rec.exact_roster_match(row(isReasoning=True), [("m", roster_item(isReasoning=False))]) is None  # mode differs
    assert rec.exact_roster_match(row(name="Model A (low)", evaluatedVariant="high"), []) is None
    assert rec.exact_roster_match(row(name="Model A (high)", evaluatedVariant="low"), [("m", roster_item())]) is None  # captured contradicts itself
    # Without a declared variant a differing display name is not an exact match.
    assert rec.exact_roster_match(row(evaluatedVariant=None), [("m", roster_item(aaName="Other (high)", aaShortName="Z"))]) is None


def test_exact_roster_match_unknown_capture_reasoning_matches_any_roster_mode():
    unknown = row(isReasoning=None)
    assert rec.exact_roster_match(unknown, [("m", roster_item(isReasoning=False))]) == "m"


# --------------------------------------------------------------------------- reconcile: happy path


def test_reconciled_report_for_complete_observed_frontier(world):
    report = run(world)
    assert report["status"] == "reconciled" and report["issues"] == []
    assert report["checkedAt"] == NOW.isoformat() and report["maxAgeDays"] == 7
    assert report["ageDays"] == 1.0
    assert report["inventoryPath"] == "data/aa_reconciliation_inventory.json"
    assert [item["aaId"] for item in report["frontier"]] == ["model-a"]
    assert report["frontier"][0]["valueRankModelId"] == "m-a"
    assert report["frontier"][0]["rankStatus"] == "Primary ranked"
    assert report["frontier"][0]["metricGap"] is None
    assert report["requiredFamilies"] == [{"family": "Family A", "modelId": "m-a",
                                           "selectedFrontierConfigurationN": 1, "primaryRanked": True}]
    assert report["comparisonCandidates"] == [] and report["missingFrontierIds"] == []
    assert report["unresolvedFrontierIds"] == [] and report["deferredFrontierIds"] == []
    assert (report["observedRowN"], report["validRowN"]) == (1, 1)
    assert "directly observed" in report["frontierDefinition"].lower()


def test_age_days_is_rounded_to_three_decimals(world):
    doc = inventory(observedAt="2026-10-07T00:00:00Z")
    report = run(world, doc)
    assert report["ageDays"] == round((NOW - datetime(2026, 10, 7, tzinfo=timezone.utc)).total_seconds() / 86400, 3)
    assert report["ageDays"] == 0.725


# --------------------------------------------------------------------------- reconcile: inventory problems


def test_missing_inventory_blocks(world):
    world.setup(None)
    report = rec.reconcile(NOW)
    assert report["status"] == "blocked"
    assert report["frontier"] == [] and report["completeness"] == {"status": "missing"}
    assert has_issue(report, "Missing or invalid inventory")


def test_invalid_json_inventory_blocks(world):
    (world.data / "aa_reconciliation_inventory.json").write_text("{not json")
    report = rec.reconcile(NOW)
    assert report["status"] == "blocked" and has_issue(report, "Missing or invalid inventory")


def test_non_object_inventory_blocks(world):
    world.setup([1, 2])
    report = rec.reconcile(NOW)
    assert report["status"] == "blocked" and has_issue(report, "inventory root must be an object")


def test_reconcile_defaults_to_the_pinned_clock(world, monkeypatch):
    monkeypatch.setenv("VALUERANK_NOW", "2026-10-07T17:23:20Z")
    world.setup(inventory())
    assert rec.reconcile()["checkedAt"] == NOW.isoformat()


def test_stale_inventory_is_blocked_with_age_in_message(world):
    report = run(world, inventory(observedAt="2026-09-29T17:23:20Z"))
    assert report["status"] == "blocked" and report["ageDays"] == 8.0
    assert "Inventory is stale or future-dated (8.00 days); recapture within 7 days." in report["issues"]


def test_inventory_exactly_seven_days_old_is_fresh(world):
    assert run(world, inventory(observedAt="2026-09-30T17:23:20Z"))["status"] == "reconciled"


def test_future_dated_inventory_is_blocked_but_small_skew_is_tolerated(world):
    future = run(world, inventory(observedAt="2026-10-08T17:23:20Z"))
    assert has_issue(future, "stale or future-dated (-1.00 days)")
    skew = run(world, inventory(observedAt="2026-10-07T18:00:00Z"))  # 37 minutes ahead
    assert not has_issue(skew, "future-dated")


@pytest.mark.parametrize("observed", ["2026-10-06T17:23:20", "garbage", 12345, None])
def test_observed_at_must_be_timezone_qualified_iso(world, observed):
    report = run(world, inventory(observedAt=observed))
    assert "Inventory observedAt must be a timezone-qualified ISO 8601 timestamp." in report["issues"]
    assert "ageDays" not in report


def test_missing_observed_at_key_is_reported(world):
    doc = inventory()
    del doc["observedAt"]
    assert has_issue(run(world, doc), "observedAt must be a timezone-qualified")


@pytest.mark.parametrize("mode", ["partial", None])
def test_unknown_mode_is_flagged(world, mode):
    assert has_issue(run(world, inventory(mode=mode)), "mode must be observedFrontier or fullNumericUniverse")


@pytest.mark.parametrize("completeness", [{"status": "partial", "note": "n"}, "complete", None])
def test_incomplete_or_malformed_completeness_is_flagged(world, completeness):
    report = run(world, inventory(completeness=completeness))
    assert has_issue(report, "partial or completeness is unknown")


def test_scope_and_completeness_note_are_required(world):
    no_note = run(world, inventory(completeness={"status": "complete"}))
    no_scope = run(world, inventory(scope=""))
    assert has_issue(no_note, "Document the chart universe/filter scope")
    assert has_issue(no_scope, "Document the chart universe/filter scope")
    assert has_issue(run(world, inventory(completeness="complete")), "Document the chart universe/filter scope")


@pytest.mark.parametrize("override", [{"sourceUrl": "http://artificialanalysis.ai/x"}, {"sourceUrl": None},
                                      {"benchmarkVersion": ""}])
def test_first_party_source_and_version_required(world, override):
    assert has_issue(run(world, inventory(**override), version=override.get("benchmarkVersion", VERSION) or VERSION),
                     "first-party AA source URL and exact benchmark version")


@pytest.mark.parametrize("rows", [None, [], "rows", {}])
def test_rows_must_be_a_nonempty_array(world, rows):
    report = run(world, inventory(rows=rows))
    assert "Inventory rows must be a nonempty array." in report["issues"]
    assert report["observedRowN"] == 0 and report["frontier"] == []


def test_benchmark_version_must_match_metrics(world):
    report = run(world, inventory(), version="Artificial Analysis Intelligence Index v9")
    assert has_issue(report, "differs from aa_metrics.json")


@pytest.mark.parametrize("missing", ["metrics", "scores"])
def test_unavailable_roster_or_ranking_blocks(world, missing):
    world.setup(inventory(), roster=None if missing == "metrics" else ROSTER, scores=None if missing == "scores" else SCORES)
    report = rec.reconcile(NOW)
    assert has_issue(report, "Source roster or ranking unavailable")
    assert report["status"] == "blocked"


def test_malformed_scores_block(world):
    report = run(world, scores={"models": "bad"})
    assert has_issue(report, "Source roster or ranking unavailable")


# --------------------------------------------------------------------------- observed-frontier universe counts


@pytest.mark.parametrize("universe", [None, "x", {}, {"selectedModelN": 5, "plottedPointN": 3, "observedFrontierPointN": 0},
                                      {"selectedModelN": True, "plottedPointN": 3, "observedFrontierPointN": 1},
                                      {"selectedModelN": 5, "plottedPointN": 3, "observedFrontierPointN": "1"}])
def test_observed_frontier_requires_positive_integer_source_counts(world, universe):
    report = run(world, inventory(sourceUniverse=universe))
    assert has_issue(report, "positive selectedModelN, plottedPointN, and observedFrontierPointN")


@pytest.mark.parametrize("counts", [(5, 3, 2), (2, 3, 1), (5, 0, 1)])
def test_inconsistent_source_counts_are_flagged(world, counts):
    selected, plotted, frontier = counts
    universe = {"selectedModelN": selected, "plottedPointN": plotted, "observedFrontierPointN": frontier}
    if plotted == 0:  # non-positive counts fall under the positivity rule instead
        assert has_issue(run(world, inventory(sourceUniverse=universe)), "positive selectedModelN")
    else:
        assert has_issue(run(world, inventory(sourceUniverse=universe)), "does not reconcile with displayed frontier/plotted/catalog counts")


def test_equal_source_counts_reconcile(world):
    universe = {"selectedModelN": 1, "plottedPointN": 1, "observedFrontierPointN": 1}
    assert not has_issue(run(world, inventory(sourceUniverse=universe)), "does not reconcile")


# --------------------------------------------------------------------------- roster decisions


def decision(**overrides):
    base = {"aaId": "model-b", "name": "Model B (low)", "evaluatedVariant": "low", "decision": "defer",
            "reason": "Not evaluated by ValueRank.", "reviewedAt": "2026-10-07T00:00:00Z"}
    base.update(overrides)
    return base


def frontier_pair():
    return [row(), row("model-b", "Model B (low)", evaluatedVariant="low", family="Family B", requiredFamilyModelId="m-b",
                       intelligenceIndex=50, totalCostUsd=20.0)]


def pair_doc(**extra):
    return inventory(rows=frontier_pair(), sourceUniverse={"selectedModelN": 9, "plottedPointN": 4, "observedFrontierPointN": 2},
                     **extra)


def test_unresolved_frontier_entrant_blocks_with_ids_and_ordering(world):
    report = run(world, pair_doc())
    assert [item["aaId"] for item in report["frontier"]] == ["model-b", "model-a"]  # ascending cost
    assert report["missingFrontierIds"] == ["model-b :: Model B (low)"]
    assert report["unresolvedFrontierIds"] == ["model-b :: Model B (low)"]
    assert [item["aaId"] for item in report["comparisonCandidates"]] == ["model-b"]
    assert report["frontier"][0]["rankStatus"] == "Missing from source roster"
    assert report["frontier"][0]["primaryRankingGaps"] == ["Exact evaluated variant absent from source roster"]
    assert has_issue(report, "Frontier entrants missing from exact source roster without a dated review decision: model-b :: Model B (low)")
    assert has_issue(report, "Required AA frontier family Family B (m-b) must resolve")
    assert report["status"] == "blocked"


def test_deferred_entrant_is_marked_but_family_requirement_still_blocks(world):
    report = run(world, pair_doc(rosterDecisions=[decision()]))
    deferred = report["frontier"][0]
    assert deferred["rankStatus"] == "Deferred comparison candidate" and deferred["rosterDecision"]["reason"].startswith("Not evaluated")
    assert report["deferredFrontierIds"] == ["model-b :: Model B (low)"] and report["unresolvedFrontierIds"] == []
    assert not has_issue(report, "Frontier entrants missing")
    assert has_issue(report, "Required AA frontier family Family B")  # a defer cannot waive family inclusion


@pytest.mark.parametrize(
    "bad",
    [
        {"reviewedAt": "2026-10-05T00:00:00Z"},  # before capture
        {"reviewedAt": "2026-10-08T00:00:00Z"},  # future-dated
        {"reviewedAt": "2026-10-07T00:00:00"},  # naive
        {"reviewedAt": None},
        {"decision": "include"},
        {"reason": "  "},
        {"reason": 5},
    ],
)
def test_invalid_roster_decisions_are_reported(world, bad):
    report = run(world, pair_doc(rosterDecisions=[decision(**bad)]))
    assert has_issue(report, "Invalid exact-variant roster decision")
    assert report["frontier"][0]["rosterDecision"] is None


def test_decision_missing_required_key_and_duplicate_are_reported(world):
    broken = decision()
    del broken["reviewedAt"]
    report = run(world, pair_doc(rosterDecisions=[broken, decision(), decision()]))
    messages = [issue for issue in report["issues"] if issue.startswith("Invalid exact-variant roster decision")]
    assert len(messages) == 2 and any("duplicate decision" in message for message in messages)


def test_rosterdecisions_must_be_array(world):
    assert has_issue(run(world, pair_doc(rosterDecisions="nope")), "rosterDecisions must be an array.")


def test_decision_for_unobserved_variant_is_reported(world):
    report = run(world, inventory(rosterDecisions=[decision(aaId="ghost", name="Ghost", evaluatedVariant=None)]))
    assert has_issue(report, "Roster decision does not match an observed evaluated variant: ('ghost', 'Ghost')")


# --------------------------------------------------------------------------- row validation


@pytest.mark.parametrize(
    "bad_row, fragment",
    [
        ("text", "Inventory row 0 is not an object."),
        ({"name": "x"}, "Inventory row 0 lacks an exact AA model URL slug."),
        (row(aaId="Bad_ID"), "Inventory row 0 lacks an exact AA model URL slug."),
        (row(name=""), "model-a: name and matching exact model source URL required."),
        (row(name=5), "model-a: name and matching exact model source URL required."),
        (row(sourceUrl="https://artificialanalysis.ai/models/other"), "name and matching exact model source URL required."),
        (row(evaluatedVariant=""), "evaluatedVariant must be a nonempty string"),
        (row(evaluatedVariant=7), "evaluatedVariant must be a nonempty string"),
        (row(isReasoning="yes"), "isReasoning must be boolean when supplied."),
        (row(evaluatedVariant="low"), "declared variant contradicts its displayed label"),
        (row(directlyObservedFrontier=False), "Model A (high): direct observation of displayed AA frontier membership required."),
        (row(intelligenceIndex="70"), "Model A (high): invalid optional numeric metric."),
        (row(totalCostUsd=-1), "Model A (high): invalid optional numeric metric."),
        (row(totalCostUsd="1"), "Model A (high): invalid optional numeric metric."),
    ],
)
def test_invalid_rows_are_skipped_with_specific_issue(world, bad_row, fragment):
    report = run(world, inventory(rows=[bad_row]))
    assert has_issue(report, fragment)
    assert report["validRowN"] == 0 and report["frontier"] == [] and report["observedRowN"] == 1


def test_duplicate_exact_variant_rows_are_rejected(world):
    report = run(world, inventory(rows=[row(), row()]))
    assert has_issue(report, "Duplicate exact AA evaluated variant: ('model-a', 'high').")
    assert report["validRowN"] == 1


def test_optional_metrics_may_be_null_and_become_explicit_gaps(world):
    report = run(world, inventory(rows=[row(intelligenceIndex=None, totalCostUsd=None)]))
    assert report["status"] == "reconciled"
    assert report["metricGaps"] == [{"aaId": "model-a", "name": "Model A (high)",
                                     "gap": "Numeric intelligence/cost values not fully available in the public chart capture"}]
    assert report["frontier"][0]["metricGap"] is not None


def test_family_fields_are_required_on_frontier_rows(world):
    for missing in ({"family": ""}, {"requiredFamilyModelId": None}, {"family": 3}):
        report = run(world, inventory(rows=[row(**missing)]))
        assert has_issue(report, "Model A (high): frontier family and requiredFamilyModelId are required.")
        assert report["requiredFamilies"] == []


def test_conflicting_required_family_ids_are_reported(world):
    second = row(evaluatedVariant="max", name="Model A (max)", requiredFamilyModelId="m-other")
    report = run(world, inventory(rows=[row(), second], sourceUniverse={"selectedModelN": 4, "plottedPointN": 3, "observedFrontierPointN": 2}))
    assert has_issue(report, "Family A: conflicting required family model IDs.")
    assert report["requiredFamilies"] == []


def test_unranked_roster_model_fails_family_inclusion(world):
    scores = {"models": [{"id": "m-a", "rankingEligible": False, "rankingExclusionReasons": ["too few evals"]}]}
    report = run(world, scores=scores)
    assert report["frontier"][0]["rankStatus"] == "Unranked source candidate"
    assert report["frontier"][0]["primaryRankingGaps"] == ["too few evals"]
    assert report["requiredFamilies"][0]["primaryRanked"] is False
    assert has_issue(report, "Required AA frontier family Family A (m-a) must resolve to one exact selected frontier configuration")


# --------------------------------------------------------------------------- fullNumericUniverse mode


def full_row(aa_id, intelligence, cost, **extra):
    fields = {"intelligenceIndex": intelligence, "totalCostUsd": cost, "directlyObservedFrontier": None,
              "family": aa_id, "requiredFamilyModelId": f"id-{aa_id}", **extra}
    return row(aa_id, f"{aa_id.title()} (high)", **fields)


def test_full_universe_computes_pareto_frontier_in_cost_order(world):
    rows = [full_row("cheap", 40, 10), full_row("mid", 60, 50), full_row("best", 80, 200),
            full_row("dominated", 50, 100), full_row("tie", 60, 50)]
    report = run(world, inventory(mode="fullNumericUniverse", sourceUniverse=None, rows=rows), roster={}, scores={"models": []})
    ids = [item["aaId"] for item in report["frontier"]]
    assert ids == ["cheap", "mid", "tie", "best"]  # exact ties survive; strictly dominated rows drop out
    assert "dominated" not in ids
    assert {item["aaId"] for item in report["comparisonCandidates"]} == {"cheap", "mid", "best", "dominated", "tie"}
    assert report["frontierDefinition"].startswith("Higher AA intelligence index")
    assert not has_issue(report, "source counts")  # counts are only demanded for observedFrontier mode


@pytest.mark.parametrize("bad", [{"intelligenceIndex": None}, {"totalCostUsd": None}, {"totalCostUsd": -3},
                                 {"intelligenceIndex": "x"}])
def test_full_universe_requires_numeric_metrics(world, bad):
    report = run(world, inventory(mode="fullNumericUniverse", rows=[full_row("a", 1, 1, **bad)]))
    assert has_issue(report, "a: intelligence index or total evaluation cost missing/invalid; dominance cannot be established.")
    assert report["validRowN"] == 0


# --------------------------------------------------------------------------- publication


def test_publication_renders_escaped_markdown_and_html(world):
    odd = row("model-b", "Model [B] | <x>", evaluatedVariant=None, intelligenceIndex=69.6, totalCostUsd=1234.5,
              family="B", requiredFamilyModelId="m-b", intelligenceIndexPrecision="rounded_whole_public_label")
    odd["sourceUrl"] = "https://artificialanalysis.ai/models/model-b"
    doc = inventory(rows=[row(), odd], sourceUniverse={"selectedModelN": 9, "plottedPointN": 4, "observedFrontierPointN": 2},
                    rosterDecisions=[{**decision(), "evaluatedVariant": None, "name": "Model [B] | <x>", "reviewedAt": "2026-10-07T00:00:00Z"}])
    report = run(world, doc)
    markdown, html = rec.publication(report)
    assert markdown.startswith("\n\n## AA intelligence and total-cost comparison")
    assert "Reconciliation: blocked" in markdown and "Gaps: " in markdown
    assert "Source selected 9 models, plotted 4 eligible points, and displayed 2 frontier points." in markdown
    assert "All 2 distinct frontier model families are required" in markdown and "1 are included." in markdown
    assert "[Model &#91;B&#93; \\| <x>](https://artificialanalysis.ai/models/model-b)" in markdown
    assert "70 (rounded)" in markdown and "$1,234.50" in markdown
    assert "Observed AA frontier" in markdown and "Reviewed 2026-10-07T00:00:00Z: Not evaluated by ValueRank." in markdown
    assert html.startswith("<!-- aa-reconciliation:start -->") and html.endswith("<!-- aa-reconciliation:end -->")
    assert "Model [B] | &lt;x&gt;" in html and "<x>" not in html
    assert 'href="https://artificialanalysis.ai/models/model-b" target="_blank" rel="noopener"' in html
    assert html.count("<tr>") == 3  # header + two rows
    assert 'scope="col"' in html


def test_publication_formats_numbers_by_mode_and_flags_comparison_rows():
    report = {"status": "reconciled", "issues": [], "mode": "fullNumericUniverse", "observedAt": "2026-10-06", "benchmarkVersion": "v",
              "scope": "chart",
              "frontier": [{"aaId": "a", "name": "A", "sourceUrl": "https://artificialanalysis.ai/models/a", "intelligenceIndex": 61.234,
                            "totalCostUsd": 5, "rankStatus": "Primary ranked", "primaryRankingGaps": []}],
              "comparisonCandidates": [{"aaId": "c", "name": "C", "sourceUrl": "https://artificialanalysis.ai/models/c",
                                        "intelligenceIndex": None, "totalCostUsd": None, "rankStatus": "Missing from source roster",
                                        "primaryRankingGaps": ["gap one", "gap two"]}]}
    markdown, html = rec.publication(report)
    assert "| 61.23 | $5.00 | Observed AA frontier | Primary ranked | None |" in markdown
    assert "Not publicly captured | Not publicly captured | Comparison candidate | Missing from source roster | gap one; gap two" in markdown
    assert "Gaps:" not in markdown and "directly observed displayed frontier" not in markdown
    observed = dict(report, mode="observedFrontier", sourceUniverse="bad", requiredFamilies=[], observedAt=None, benchmarkVersion=None, scope=None)
    observed["frontier"] = [dict(report["frontier"][0], aaId="a")]
    text, _ = rec.publication(observed)
    assert "Observed unknown date; unknown version. Scope: unknown." in text
    assert "Source selected unknown models" in text and "All 0 distinct frontier model families" in text
    assert "| 61.234 |" in text  # observed-frontier values are shown verbatim


# --------------------------------------------------------------------------- main / CLI


def run_main(world, monkeypatch, capsys, args=()):
    monkeypatch.setattr(sys, "argv", ["aa_reconciliation", *args])
    status = rec.main()
    return status, capsys.readouterr().out, json.loads((world.data / "aa_reconciliation_report.json").read_text())


def test_main_exit_zero_when_reconciled(world, monkeypatch, capsys, pinned_clock):
    world.setup(inventory(observedAt="2026-10-07T00:00:00Z"))
    status, out, report = run_main(world, monkeypatch, capsys)
    assert status == 0 and report["status"] == "reconciled"
    assert out == "AA reconciliation reconciled: data/aa_reconciliation_report.json\n"


def test_main_exit_one_when_blocked_and_lists_issues(world, monkeypatch, capsys, pinned_clock):
    world.setup(pair_doc(observedAt="2026-10-07T00:00:00Z"))
    status, out, report = run_main(world, monkeypatch, capsys)
    assert status == 1 and report["status"] == "blocked"
    assert out.startswith("AA reconciliation blocked: data/aa_reconciliation_report.json\n- ")
    assert all(f"- {issue}" in out for issue in report["issues"])


def test_main_report_only_exits_zero_even_when_blocked(world, monkeypatch, capsys, pinned_clock):
    world.setup(pair_doc(observedAt="2026-10-07T00:00:00Z"))
    status, _, report = run_main(world, monkeypatch, capsys, ["--report-only"])
    assert status == 0 and report["status"] == "blocked"


def test_main_blocks_when_inventory_is_missing(world, monkeypatch, capsys, pinned_clock):
    status, out, report = run_main(world, monkeypatch, capsys)
    assert status == 1 and "Missing or invalid inventory" in out and report["inventoryPath"].endswith("inventory.json")


def test_module_guard_exits_with_main_status(world, monkeypatch, pinned_clock):
    import valuerank.paths as paths

    world.setup(inventory(observedAt="2026-10-07T00:00:00Z"))
    monkeypatch.setattr(paths, "ROOT", world.root)
    monkeypatch.setattr(paths, "DATA", world.data)
    monkeypatch.setattr(sys, "argv", ["aa_reconciliation"])
    with pytest.warns(RuntimeWarning), pytest.raises(SystemExit) as exit_info:
        runpy.run_module("valuerank.aa_reconciliation", run_name="__main__", alter_sys=True)
    assert exit_info.value.code == 0
    assert json.loads((world.data / "aa_reconciliation_report.json").read_text())["status"] == "reconciled"
