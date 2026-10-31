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


NEAR_POLICY = {"maxIntelligenceGap": 3, "basis": "Within 3 Index points of the rendered frontier at its cost.",
               "text": "Near-frontier families are required or explicitly deferred."}


def inventory(**overrides):
    doc = {"observedAt": OBSERVED, "benchmarkVersion": VERSION, "sourceUrl": "https://artificialanalysis.ai/models",
           "scope": "Intelligence vs total cost", "completeness": {"status": "complete", "note": "all points read"},
           "mode": "observedFrontier",
           "sourceUniverse": {"selectedModelN": 5, "plottedPointN": 3, "observedFrontierPointN": 1, "nearFrontierPointN": 0},
           "nearFrontierPolicy": NEAR_POLICY, "nearFrontierRows": [],
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
                                           "selectedFrontierConfigurationN": 1, "primaryRanked": True,
                                           "incompleteEvidence": False}]
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


def test_reconcile_defaults_to_the_pinned_clock(world, pinned_clock):
    world.setup(inventory())
    pinned = datetime.fromisoformat(pinned_clock.replace("Z", "+00:00"))
    assert rec.reconcile()["checkedAt"] == pinned.isoformat()


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


@pytest.mark.parametrize("universe", [None, "x", {}, {"selectedModelN": 5, "plottedPointN": 3, "observedFrontierPointN": 0, "nearFrontierPointN": 0},
                                      {"selectedModelN": True, "plottedPointN": 3, "observedFrontierPointN": 1, "nearFrontierPointN": 0},
                                      {"selectedModelN": 5, "plottedPointN": 3, "observedFrontierPointN": "1", "nearFrontierPointN": 0}])
def test_observed_frontier_requires_positive_integer_source_counts(world, universe):
    report = run(world, inventory(sourceUniverse=universe))
    assert has_issue(report, "positive selectedModelN, plottedPointN, and observedFrontierPointN")


@pytest.mark.parametrize("counts", [(5, 3, 2), (2, 3, 1), (5, 0, 1)])
def test_inconsistent_source_counts_are_flagged(world, counts):
    selected, plotted, frontier = counts
    universe = {"selectedModelN": selected, "plottedPointN": plotted, "observedFrontierPointN": frontier, "nearFrontierPointN": 0}
    if plotted == 0:  # non-positive counts fall under the positivity rule instead
        assert has_issue(run(world, inventory(sourceUniverse=universe)), "positive selectedModelN")
    else:
        assert has_issue(run(world, inventory(sourceUniverse=universe)), "does not reconcile with displayed frontier/plotted/catalog counts")


def test_equal_source_counts_reconcile(world):
    universe = {"selectedModelN": 1, "plottedPointN": 1, "observedFrontierPointN": 1, "nearFrontierPointN": 0}
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
    return inventory(rows=frontier_pair(), sourceUniverse={"selectedModelN": 9, "plottedPointN": 4, "observedFrontierPointN": 2, "nearFrontierPointN": 0},
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
    report = run(world, inventory(rows=[row(), second], sourceUniverse={"selectedModelN": 4, "plottedPointN": 3, "observedFrontierPointN": 2, "nearFrontierPointN": 0}))
    assert has_issue(report, "Family A: conflicting required family model IDs.")
    assert report["requiredFamilies"] == []


def test_unranked_roster_model_fails_family_inclusion(world):
    scores = {"models": [{"id": "m-a", "rankingEligible": False, "rankingExclusionReasons": ["too few evals"]}]}
    report = run(world, scores=scores)
    assert report["frontier"][0]["rankStatus"] == "Unranked source candidate"
    assert report["frontier"][0]["primaryRankingGaps"] == ["too few evals"]
    assert report["requiredFamilies"][0]["primaryRanked"] is False
    assert has_issue(report, "Required AA frontier family Family A (m-a) must resolve to one exact selected frontier configuration")


def test_logged_incomplete_evidence_exclusion_satisfies_family_inclusion(world):
    # O36/O38: the score build lists a family whose selected configuration lacks a benchmark after the logged search.
    reason = "Incomplete benchmark evidence after an exhaustive search (O36): no Bug Hunt Bench"
    scores = {"models": [{"id": "m-a", "rankingEligible": False, "rankingStatus": rec.INCOMPLETE_STATUS, "rankingExclusionReasons": [reason]}]}
    report = run(world, scores=scores)
    assert report["status"] == "reconciled" and report["issues"] == []
    assert report["frontier"][0]["rankStatus"] == "Unranked: incomplete benchmark evidence (O36)"
    assert report["frontier"][0]["primaryRankingGaps"] == [reason]
    assert report["requiredFamilies"][0] == {"family": "Family A", "modelId": "m-a", "selectedFrontierConfigurationN": 1,
                                             "primaryRanked": False, "incompleteEvidence": True}


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


# --------------------------------------------------------------------------- near-frontier policy


def near_row(aa_id="model-a", name="Model A (medium)", **extra):
    base = {"aaId": aa_id, "name": name, "sourceUrl": f"https://artificialanalysis.ai/models/{aa_id}",
            "evaluatedVariant": "medium", "isReasoning": True, "intelligenceIndex": 68, "totalCostUsd": 120.0,
            "intelligenceGap": 2, "costRatio": 1.2, "nearestFrontierAaId": "model-a", "directlyObservedFrontier": False,
            "family": "Family A", "requiredFamilyModelId": "m-a", "sourceFootnote": None}
    base.update(extra)
    return base


def near_doc(near_rows, **extra):
    doc = inventory(sourceUniverse={"selectedModelN": 9, "plottedPointN": 4, "observedFrontierPointN": 1,
                                    "nearFrontierPointN": len(near_rows)},
                    nearFrontierRows=near_rows, **extra)
    return doc


C_ITEM = {"aaSlug": "model-c", "aaVariant": "high", "aaName": "Model C (high)", "aaShortName": "C", "isReasoning": True}
C_ROSTER = {**ROSTER, "m-c": C_ITEM}
C_SCORES = {"models": [*SCORES["models"], {"id": "m-c", "rankingEligible": True, "rankingExclusionReasons": []}]}


def test_near_family_in_roster_may_differ_from_the_near_configuration(world):
    report = run(world, near_doc([near_row()]))
    assert report["status"] == "reconciled" and report["issues"] == []
    assert report["nearFrontierPolicy"] == NEAR_POLICY
    assert [item["aaId"] for item in report["nearFrontier"]] == ["model-a"]
    near = report["nearFrontier"][0]
    assert near["valueRankModelId"] is None and near["rankStatus"] == "Missing from source roster"
    assert near["rosterDecision"] is None and near["intelligenceGap"] == 2
    assert near["primaryRankingGaps"] == ["Exact evaluated variant absent from source roster"]
    assert report["nearFrontierFamilies"] == [{"family": "Family A", "modelId": "m-a", "configurationN": 1,
                                               "inRoster": True, "primaryRanked": True, "deferred": False, "incompleteEvidence": False}]
    assert report["missingNearFrontierIds"] == ["model-a :: Model A (medium)"]
    assert report["unresolvedNearFrontierIds"] == ["model-a :: Model A (medium)"]
    assert report["deferredNearFrontierIds"] == []
    assert [item["aaId"] for item in report["frontier"]] == ["model-a"]  # near rows never join the frontier


def test_near_row_resolves_to_exact_roster_configuration(world):
    far = near_row("model-c", "Model C (high)", evaluatedVariant="high", family="Family C", requiredFamilyModelId="m-c")
    report = run(world, near_doc([far]), roster=C_ROSTER, scores=C_SCORES)
    assert report["status"] == "reconciled"
    near = report["nearFrontier"][0]
    assert (near["valueRankModelId"], near["rankStatus"]) == ("m-c", "Primary ranked")
    assert report["missingNearFrontierIds"] == [] and report["unresolvedNearFrontierIds"] == []


def test_near_rows_are_sorted_by_cost_and_families_grouped(world):
    rows = [near_row(totalCostUsd=300.0),
            near_row("model-c", "Model C (high)", evaluatedVariant="high", family="Family C", requiredFamilyModelId="m-c", totalCostUsd=110.0),
            near_row("model-a", "Model A (low)", evaluatedVariant="low", totalCostUsd=90.0)]
    report = run(world, near_doc(rows), roster=C_ROSTER, scores=C_SCORES)
    assert [item["name"] for item in report["nearFrontier"]] == ["Model A (low)", "Model C (high)", "Model A (medium)"]
    assert report["nearFrontierFamilies"] == [
        {"family": "Family A", "modelId": "m-a", "configurationN": 2, "inRoster": True, "primaryRanked": True, "deferred": False, "incompleteEvidence": False},
        {"family": "Family C", "modelId": "m-c", "configurationN": 1, "inRoster": True, "primaryRanked": True, "deferred": False, "incompleteEvidence": False}]


def test_deferred_near_family_needs_a_dated_decision_per_row(world):
    cheap = near_row("model-d", "Model D (low)", evaluatedVariant="low", family="Family D", requiredFamilyModelId=None)
    both = [cheap, near_row("model-d", "Model D (max)", evaluatedVariant="max", family="Family D", requiredFamilyModelId=None,
                            totalCostUsd=200.0)]
    decisions = [decision(aaId="model-d", name="Model D (low)", evaluatedVariant="low"),
                 decision(aaId="model-d", name="Model D (max)", evaluatedVariant="max")]
    report = run(world, near_doc(both, rosterDecisions=decisions))
    assert report["status"] == "reconciled" and report["issues"] == []
    assert report["nearFrontierFamilies"] == [{"family": "Family D", "modelId": None, "configurationN": 2,
                                               "inRoster": False, "primaryRanked": False, "deferred": True, "incompleteEvidence": False}]
    assert report["deferredNearFrontierIds"] == ["model-d :: Model D (low)", "model-d :: Model D (max)"]
    assert report["unresolvedNearFrontierIds"] == []
    assert report["nearFrontier"][0]["rankStatus"] == "Deferred comparison candidate"
    assert report["nearFrontier"][0]["rosterDecision"]["reason"].startswith("Not evaluated")
    partial = run(world, near_doc(both, rosterDecisions=decisions[:1]))
    assert partial["status"] == "blocked"
    assert has_issue(partial, "Near-frontier AA family Family D is deferred without a dated roster decision for: Model D (max)")
    undecided = run(world, near_doc(both))
    assert has_issue(undecided, "deferred without a dated roster decision for: Model D (low), Model D (max)")


def test_decision_for_near_row_counts_as_observed_variant(world):
    report = run(world, near_doc([near_row("model-d", "Model D (low)", evaluatedVariant="low", family="Family D",
                                           requiredFamilyModelId=None)],
                                 rosterDecisions=[decision(aaId="model-d", name="Model D (low)", evaluatedVariant="low")]))
    assert not has_issue(report, "Roster decision does not match an observed evaluated variant")


def test_near_family_with_required_id_must_be_in_roster_and_ranked(world):
    absent = near_row("model-c", "Model C (high)", evaluatedVariant="high", family="Family C", requiredFamilyModelId="m-c")
    report = run(world, near_doc([absent]))
    assert report["status"] == "blocked"
    assert has_issue(report, "Near-frontier AA family Family C (m-c) must appear in the primary ranking")
    assert report["nearFrontierFamilies"][0]["inRoster"] is False and report["nearFrontierFamilies"][0]["primaryRanked"] is False
    unranked = {"models": [*SCORES["models"], {"id": "m-c", "rankingEligible": False, "rankingExclusionReasons": ["few evals"]}]}
    report = run(world, near_doc([absent]), roster=C_ROSTER, scores=unranked)
    assert has_issue(report, "Near-frontier AA family Family C (m-c) must appear in the primary ranking")
    assert report["nearFrontierFamilies"][0]["inRoster"] is True and report["nearFrontierFamilies"][0]["primaryRanked"] is False
    assert report["nearFrontier"][0]["rankStatus"] == "Unranked source candidate"
    # O36/O38: a logged incomplete-evidence exclusion lists the family explicitly instead of blocking.
    listed = {"models": [*SCORES["models"], {"id": "m-c", "rankingEligible": False, "rankingStatus": rec.INCOMPLETE_STATUS,
                                             "rankingExclusionReasons": ["no FrontierCode"]}]}
    report = run(world, near_doc([absent]), roster=C_ROSTER, scores=listed)
    assert not has_issue(report, "Near-frontier AA family Family C (m-c) must appear in the primary ranking")
    assert report["nearFrontierFamilies"][0]["incompleteEvidence"] is True and report["nearFrontierFamilies"][0]["primaryRanked"] is False


@pytest.mark.parametrize("override, fragment", [
    ({"nearFrontierPolicy": None}, "nearFrontierPolicy"),
    ({"nearFrontierPolicy": "text"}, "nearFrontierPolicy"),
    ({"nearFrontierPolicy": {**NEAR_POLICY, "maxIntelligenceGap": 0}}, "nearFrontierPolicy"),
    ({"nearFrontierPolicy": {**NEAR_POLICY, "maxIntelligenceGap": "3"}}, "nearFrontierPolicy"),
    ({"nearFrontierPolicy": {**NEAR_POLICY, "maxIntelligenceGap": True}}, "nearFrontierPolicy"),
    ({"nearFrontierPolicy": {**NEAR_POLICY, "basis": " "}}, "nearFrontierPolicy"),
    ({"nearFrontierPolicy": {**NEAR_POLICY, "text": ""}}, "nearFrontierPolicy"),
    ({"nearFrontierPolicy": {k: v for k, v in NEAR_POLICY.items() if k != "text"}}, "nearFrontierPolicy"),
    ({"nearFrontierRows": None}, "nearFrontierRows"),
    ({"nearFrontierRows": "rows"}, "nearFrontierRows"),
])
def test_observed_frontier_requires_near_policy_and_rows(world, override, fragment):
    doc = inventory()
    doc.update(override)
    report = run(world, doc)
    assert report["status"] == "blocked" and has_issue(report, fragment)
    assert report["nearFrontier"] == []


def test_fractional_policy_gap_is_accepted(world):
    report = run(world, inventory(nearFrontierPolicy={**NEAR_POLICY, "maxIntelligenceGap": 2.5}))
    assert report["status"] == "reconciled" and report["nearFrontierPolicy"]["maxIntelligenceGap"] == 2.5


@pytest.mark.parametrize("count", [None, -1, True, "0", 1.0, 2])
def test_near_point_count_must_be_nonnegative_int_matching_rows(world, count):
    universe = {"selectedModelN": 5, "plottedPointN": 3, "observedFrontierPointN": 1}
    if count is not None:
        universe["nearFrontierPointN"] = count
    report = run(world, inventory(sourceUniverse=universe))
    assert report["status"] == "blocked"
    assert has_issue(report, "sourceUniverse.nearFrontierPointN")


def test_near_point_count_mismatch_with_rows_is_flagged(world):
    doc = near_doc([near_row()])
    doc["sourceUniverse"]["nearFrontierPointN"] = 2
    assert has_issue(run(world, doc), "Near-frontier row count 1 does not match sourceUniverse.nearFrontierPointN 2")


def test_near_point_count_requires_object_universe(world):
    assert has_issue(run(world, inventory(sourceUniverse="x")), "sourceUniverse.nearFrontierPointN")


@pytest.mark.parametrize(
    "bad_row, fragment",
    [
        ("text", "Near-frontier row 0 is not an object."),
        ({"name": "x"}, "Near-frontier row 0 lacks an exact AA model URL slug."),
        (near_row(aaId="Bad_ID"), "Near-frontier row 0 lacks an exact AA model URL slug."),
        (near_row(name=""), "Near-frontier model-a: name and matching exact model source URL required."),
        (near_row(sourceUrl="https://artificialanalysis.ai/models/other"), "Near-frontier model-a: name and matching exact model source URL"),
        (near_row(evaluatedVariant=""), "Near-frontier model-a: evaluatedVariant must be a nonempty string"),
        (near_row(isReasoning="yes"), "Near-frontier model-a: isReasoning must be boolean"),
        (near_row(evaluatedVariant="low"), "Near-frontier model-a: declared variant contradicts its displayed label"),
        (near_row(directlyObservedFrontier=True), "Model A (medium): near-frontier rows must not claim direct frontier observation."),
        (near_row(directlyObservedFrontier=None), "Model A (medium): near-frontier rows must not claim direct frontier observation."),
        (near_row(intelligenceIndex=None), "Model A (medium): near-frontier intelligenceIndex and totalCostUsd must be numeric."),
        (near_row(intelligenceIndex="68"), "Model A (medium): near-frontier intelligenceIndex and totalCostUsd must be numeric."),
        (near_row(totalCostUsd=-1), "Model A (medium): near-frontier intelligenceIndex and totalCostUsd must be numeric."),
        (near_row(totalCostUsd=None), "Model A (medium): near-frontier intelligenceIndex and totalCostUsd must be numeric."),
        (near_row(intelligenceGap=None), "Model A (medium): intelligenceGap must be a number between 0 and 3."),
        (near_row(intelligenceGap=-0.5), "Model A (medium): intelligenceGap must be a number between 0 and 3."),
        (near_row(intelligenceGap=3.5), "Model A (medium): intelligenceGap must be a number between 0 and 3."),
        (near_row(intelligenceGap="2"), "Model A (medium): intelligenceGap must be a number between 0 and 3."),
        (near_row(costRatio="1.2"), "Model A (medium): costRatio must be null or a nonnegative number."),
        (near_row(costRatio=-1), "Model A (medium): costRatio must be null or a nonnegative number."),
        (near_row(nearestFrontierAaId="elsewhere"), "Model A (medium): nearestFrontierAaId must name a frontier row."),
        (near_row(nearestFrontierAaId=None), "Model A (medium): nearestFrontierAaId must name a frontier row."),
        (near_row(sourceFootnote=""), "Model A (medium): sourceFootnote must be a nonempty string or null."),
        (near_row(sourceFootnote=3), "Model A (medium): sourceFootnote must be a nonempty string or null."),
    ],
)
def test_invalid_near_rows_are_skipped_with_specific_issue(world, bad_row, fragment):
    report = run(world, near_doc([bad_row]))
    assert has_issue(report, fragment)
    assert report["nearFrontier"] == [] and report["status"] == "blocked"


def test_near_cost_ratio_may_be_null_or_zero(world):
    report = run(world, near_doc([near_row(costRatio=None), near_row(evaluatedVariant="low", name="Model A (low)", costRatio=0)]))
    assert report["status"] == "reconciled" and len(report["nearFrontier"]) == 2


def test_near_gap_bounds_are_inclusive_and_follow_the_declared_policy(world):
    edge = [near_row(intelligenceGap=0), near_row(evaluatedVariant="low", name="Model A (low)", intelligenceGap=3)]
    assert run(world, near_doc(edge))["status"] == "reconciled"
    wide = near_doc([near_row(intelligenceGap=4.5)], nearFrontierPolicy={**NEAR_POLICY, "maxIntelligenceGap": 5})
    assert run(world, wide)["status"] == "reconciled"


def test_near_gap_upper_bound_skipped_when_policy_invalid(world):
    report = run(world, near_doc([near_row(intelligenceGap=9)], nearFrontierPolicy=None))
    assert has_issue(report, "nearFrontierPolicy") and not has_issue(report, "intelligenceGap must be")


def test_near_row_duplicating_a_frontier_or_near_variant_is_rejected(world):
    frontier_dup = near_row(evaluatedVariant="high", name="Model A (high)")
    report = run(world, near_doc([frontier_dup]))
    assert has_issue(report, "Duplicate exact AA evaluated variant: ('model-a', 'high').")
    assert report["nearFrontier"] == []
    report = run(world, near_doc([near_row(), near_row()]))
    assert has_issue(report, "Duplicate exact AA evaluated variant: ('model-a', 'medium').")
    assert len(report["nearFrontier"]) == 1


def test_near_family_fields_are_required_and_ids_must_be_consistent(world):
    for bad in ({"family": ""}, {"family": 3}):
        report = run(world, near_doc([near_row(**bad)]))
        assert has_issue(report, "Model A (medium): near-frontier family is required.")
        assert report["nearFrontierFamilies"] == []
    for bad in ({"requiredFamilyModelId": ""}, {"requiredFamilyModelId": 5}):
        report = run(world, near_doc([near_row(**bad)]))
        assert has_issue(report, "Model A (medium): near-frontier requiredFamilyModelId must be a model ID string or null.")
        assert report["nearFrontierFamilies"] == []
    missing = near_row()
    del missing["requiredFamilyModelId"]
    assert has_issue(run(world, near_doc([missing])), "requiredFamilyModelId must be a model ID string or null")
    mixed = [near_row(), near_row(evaluatedVariant="low", name="Model A (low)", requiredFamilyModelId=None)]
    report = run(world, near_doc(mixed))
    assert has_issue(report, "Near-frontier AA family Family A: conflicting requiredFamilyModelId values.")
    assert report["nearFrontierFamilies"] == []


def test_source_footnotes_pass_through_to_report_rows(world):
    note = "Claude Haiku 5.5 has 5x higher pricing on longer-context inputs."
    doc = near_doc([near_row(sourceFootnote=note)])
    doc["rows"][0]["sourceFootnote"] = note
    report = run(world, doc)
    assert report["status"] == "reconciled"
    assert report["frontier"][0]["sourceFootnote"] == note and report["nearFrontier"][0]["sourceFootnote"] == note


@pytest.mark.parametrize("bad", ["", 4])
def test_frontier_row_footnote_must_be_nonempty_string_or_null(world, bad):
    report = run(world, inventory(rows=[row(sourceFootnote=bad)]))
    assert has_issue(report, "Model A (high): sourceFootnote must be a nonempty string or null.")
    assert report["frontier"] == []


def test_full_universe_mode_ignores_near_frontier_fields(world):
    rows = [full_row("cheap", 40, 10)]
    report = run(world, inventory(mode="fullNumericUniverse", nearFrontierPolicy=None, nearFrontierRows=None, rows=rows),
                 roster={}, scores={"models": []})
    assert not has_issue(report, "nearFrontier") and report["nearFrontier"] == []
    assert report["nearFrontierFamilies"] == [] and report["nearFrontierPolicy"] is None


def test_missing_inventory_report_carries_empty_near_sections(world):
    world.setup(None)
    report = rec.reconcile(NOW)
    assert report["nearFrontier"] == [] and report["nearFrontierFamilies"] == []



# --------------------------------------------------------------------------- publication


def test_publication_renders_escaped_markdown_and_html(world):
    odd = row("model-b", "Model [B] | <x>", evaluatedVariant=None, intelligenceIndex=69.6, totalCostUsd=1234.5,
              family="B", requiredFamilyModelId="m-b", intelligenceIndexPrecision="rounded_whole_public_label")
    odd["sourceUrl"] = "https://artificialanalysis.ai/models/model-b"
    doc = inventory(rows=[row(), odd], sourceUniverse={"selectedModelN": 9, "plottedPointN": 4, "observedFrontierPointN": 2, "nearFrontierPointN": 0},
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


def test_publication_flags_near_rows_and_summarises_families(world):
    deferred = near_row("model-d", "Model [D] | <x>", evaluatedVariant=None, family="Family D", requiredFamilyModelId=None,
                        intelligenceIndex=68.4, totalCostUsd=2000.0, intelligenceGap=1.5)
    deferred["sourceUrl"] = "https://artificialanalysis.ai/models/model-d"
    dec = decision(aaId="model-d", name="Model [D] | <x>", evaluatedVariant=None)
    report = run(world, near_doc([near_row(), deferred], rosterDecisions=[dec],
                                 intelligenceIndexPrecision="rounded_whole_public_label"))
    assert report["status"] == "reconciled"
    markdown, html = rec.publication(report)
    assert "2 plotted configurations from 2 families lie within 3 Index points of the rendered frontier; 1 of those families are in the main ranking, 1 are deferred." in markdown
    assert "Near AA frontier (within 3 Index points)" in markdown and "Observed AA frontier" in markdown
    assert "[Model &#91;D&#93; \\| <x>](https://artificialanalysis.ai/models/model-d)" in markdown
    assert "Deferred comparison candidate" in markdown and "Reviewed 2026-10-07T00:00:00Z: Not evaluated by ValueRank." in markdown
    assert "Model [D] | &lt;x&gt;" in html and "<x>" not in html
    assert "Near AA frontier (within 3 Index points)" in html
    assert html.count("<tr>") == 4  # header + frontier + two near rows
    assert markdown.count("| Near AA frontier (within 3 Index points) |") == 2


def test_publication_near_summary_tolerates_missing_policy_and_fractional_gap():
    base = {"status": "blocked", "issues": [], "mode": "observedFrontier", "observedAt": "2026-10-06", "benchmarkVersion": "v",
            "scope": "chart", "sourceUniverse": {}, "requiredFamilies": [], "frontier": [], "comparisonCandidates": []}
    markdown, _ = rec.publication(base)
    assert "0 plotted configurations from 0 families lie within unknown Index points" in markdown
    fractional = dict(base, nearFrontierPolicy={"maxIntelligenceGap": 2.5},
                      nearFrontier=[{"aaId": "n", "name": "N", "sourceUrl": "https://artificialanalysis.ai/models/n",
                                     "intelligenceIndex": 5, "totalCostUsd": 1, "rankStatus": "Primary ranked", "primaryRankingGaps": []}],
                      nearFrontierFamilies=[{"family": "N", "primaryRanked": True, "deferred": False, "incompleteEvidence": False}])
    text, _ = rec.publication(fractional)
    assert "1 plotted configurations from 1 families lie within 2.5 Index points" in text
    assert "| Near AA frontier (within 2.5 Index points) |" in text
    full, _ = rec.publication({**base, "mode": "fullNumericUniverse"})
    assert "lie within" not in full


# --------------------------------------------------------------------------- main / CLI


def run_main(world, monkeypatch, capsys, args=()):
    monkeypatch.setattr(sys, "argv", ["aa_reconciliation", *args])
    status = rec.main()
    return status, capsys.readouterr().out, json.loads((world.data / "aa_reconciliation_report.json").read_text())


def test_main_exit_zero_when_reconciled(world, monkeypatch, capsys, pinned_clock):
    world.setup(inventory(observedAt="2026-10-30T00:00:00Z"))
    status, out, report = run_main(world, monkeypatch, capsys)
    assert status == 0 and report["status"] == "reconciled"
    assert out == "AA reconciliation reconciled: data/aa_reconciliation_report.json\n"


def test_main_exit_one_when_blocked_and_lists_issues(world, monkeypatch, capsys, pinned_clock):
    world.setup(pair_doc(observedAt="2026-10-30T00:00:00Z"))
    status, out, report = run_main(world, monkeypatch, capsys)
    assert status == 1 and report["status"] == "blocked"
    assert out.startswith("AA reconciliation blocked: data/aa_reconciliation_report.json\n- ")
    assert all(f"- {issue}" in out for issue in report["issues"])


def test_main_report_only_exits_zero_even_when_blocked(world, monkeypatch, capsys, pinned_clock):
    world.setup(pair_doc(observedAt="2026-10-30T00:00:00Z"))
    status, _, report = run_main(world, monkeypatch, capsys, ["--report-only"])
    assert status == 0 and report["status"] == "blocked"


def test_main_blocks_when_inventory_is_missing(world, monkeypatch, capsys, pinned_clock):
    status, out, report = run_main(world, monkeypatch, capsys)
    assert status == 1 and "Missing or invalid inventory" in out and report["inventoryPath"].endswith("inventory.json")


def test_module_guard_exits_with_main_status(world, monkeypatch, pinned_clock):
    import valuerank.paths as paths

    world.setup(inventory(observedAt="2026-10-30T00:00:00Z"))
    monkeypatch.setattr(paths, "ROOT", world.root)
    monkeypatch.setattr(paths, "DATA", world.data)
    monkeypatch.setattr(sys, "argv", ["aa_reconciliation"])
    with pytest.warns(RuntimeWarning), pytest.raises(SystemExit) as exit_info:
        runpy.run_module("valuerank.aa_reconciliation", run_name="__main__", alter_sys=True)
    assert exit_info.value.code == 0
    assert json.loads((world.data / "aa_reconciliation_report.json").read_text())["status"] == "reconciled"
