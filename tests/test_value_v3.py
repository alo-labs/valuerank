"""Tests for the v3 integration: evidence, admission, anchors, scores, intervals, scenarios and the CLI."""

from __future__ import annotations

import copy
import json
import runpy
import sys
from datetime import date
from pathlib import Path
from types import SimpleNamespace

import pytest

from valuerank import anchors as anchor_math
from valuerank import basket
from valuerank import diagnostics
from valuerank import plan_routes as pr
from valuerank import quality as q
from valuerank import scenarios
from valuerank import value_v3 as v

DAY = date(2026, 10, 19)
ALL_TASKS = {**basket.INDEX_SDLC_TASKS, **basket.INDEX_RESIDUAL_TASKS}


def page(slug: str, cost_per_task: float, **fields) -> dict:
    evaluations = [{"slug": key, "costPerTask": cost_per_task} for key in ALL_TASKS]
    model = {
        "slug": slug,
        "intelligenceIndexEvaluations": evaluations,
        "intelligenceIndexCost": {"total": cost_per_task * sum(ALL_TASKS.values())},
        "gdpval": 1500.0,
        "automationBenchPartialScore": 0.5,
        "frontierCode": 0.45,
        "lcr": 0.8,
        "hle": 0.3,
        "scicode": 0.4,
        "critpt": 0.2,
        "omniscience": 30.0,
        "omniscienceAccuracy": 0.5,
        "omniscienceHallucinationRate": 0.4,
        "price1mInputTokens": 2.0,
        "price1mOutputTokens": 10.0,
        "cacheHitPrice": 0.2,
    }
    model.update(fields)
    return {"model": model}


def documents(**overrides) -> dict:
    base = {
        "snapshot": {"pages": [page("a-max", 1.0), page("b-max", 4.0, gdpval=2000.0), page("c-max", 0.5)]},
        "deepswe": {"configurations": [
            {"valueRankModelId": "a", "scorePct": 70.0, "effort": "max", "displayLabel": "A", "agent": "x"},
            {"valueRankModelId": "b", "scorePct": 75.0, "effort": "max", "scorePrecision": 0.1},
            {"valueRankModelId": "c", "scorePct": 50.0, "effort": "high"},
            {"valueRankModelId": None, "scorePct": 10.0},
        ]},
        "bugHunt": {"models": [
            {"modelId": "a", "matched": True, "effort": "max", "fixedOf105": 52.0, "sampleN": 3},
            {"modelId": "b", "matched": False, "fixedOf105": None},
        ]},
        "tb4": {"rows": [{"model": "Opus 5.5 (max)", "agent": "Terminus 2", "resolutionRatePct": 60.0}]},
        "codingAgents": {"configurations": [
            {"label": "agent-a", "meanCostPerTaskUsd": 2.0, "totalCostUsd": 600.0, "components": []},
            {"label": "agent-b", "meanCostPerTaskUsd": 6.0, "totalCostUsd": 1800.0, "components": []},
        ]},
        "costCharts": {"evaluations": [
            {"slug": "frontiercode", "rows": [{"model": "A (max)", "totalUsd": 9, "declinedTasks": True}]},
            {"slug": "itbench-aa", "rows": []},
        ]},
        "configurationMap": {"rows": {
            "a": {"coding-agent-index": "agent-a", "frontiercode": "A (max)", "itbench-aa": None},
            "b": {"coding-agent-index": "agent-b", "frontiercode": None, "itbench-aa": None},
            "c": {"coding-agent-index": None, "frontiercode": None, "itbench-aa": None},
        }},
        "planRoutes": {"routes": [
            {"id": "plan-a", "valueMultiple": 10.0, "valueMultipleKind": "controlled_account_workload_projection", "modelIds": ["a"], "planPriceUsd": 20, "checkedOn": "2026-10-10",
             "allocationRegime": "single-model allocation"},
            {"id": "plan-b", "valueMultiple": 2.0, "valueMultipleKind": "controlled_account_workload_projection", "modelIds": ["b"], "planPriceUsd": 20, "checkedOn": "2026-10-10", "allocationRegime": "single-model allocation",
             "identification": "point-identified", "valuationBasis": "release"},
        ]},
        "priceRecords": {"records": []},
    }
    base.update(overrides)
    return base


CONFIGURATIONS = [
    {"id": "a", "name": "A", "effort": "max", "aaSlug": "a-max", "aaNote": "A has higher pricing on long inputs not reflected in cost figures."},
    {"id": "b", "name": "B", "effort": "max", "aaSlug": "b-max"},
    {"id": "c", "name": "C", "effort": "max", "aaSlug": "c-max"},
]


def assembled(**overrides):
    return v.assemble(CONFIGURATIONS, documents(**overrides), release_day=DAY)


def test_leaf_evidence_uses_exact_configurations_only():
    model = page("a-max", 1.0)["model"]
    tb4 = [{"model": "Opus 5.5 (max)", "agent": "Terminus 2", "resolutionRatePct": 60.0}]
    evidence = v.leaf_evidence("claude-opus-5-5", "max", model, {"scorePct": 70.0, "effort": "max", "scorePrecision": 0.1}, tb4, {"matched": True, "effort": "max", "fixedOf105": 52.0})
    observations = evidence["observations"]
    assert set(observations) == {leaf.key for leaf in q.LEAVES}
    assert observations["deepswe"].half_width == pytest.approx(0.05) and observations["terminalBench"].z == 60.0
    assert observations["omniscience"].z == pytest.approx(65.0)
    assert evidence["provenance"]["omniscience"]["indexFromRates"] == pytest.approx(30.0)
    assert evidence["provenance"]["terminalBench"]["agent"] == "Terminus 2"
    # A different effort never transfers; absent fields stay missing.
    sparse = v.leaf_evidence("x", "max", {"gdpval": None}, {"scorePct": 70.0, "effort": "high"}, [], None)
    assert sparse["observations"] == {} and sparse["clipAudit"] == []
    index_only = v.leaf_evidence("x", "max", {"omniscience": -20.0}, None, [], None)
    assert index_only["observations"]["omniscience"].z == 40.0 and index_only["provenance"]["omniscience"]["indexFromRates"] is None
    with pytest.raises(ValueError, match="outside its documented domain"):
        v.leaf_evidence("x", "max", {"hle": 1.5}, None, [], None)


def test_components_and_restricted_cost():
    components, reconciliation = v.row_components(page("a-max", 1.0)["model"], None, {"frontiercode": None, "itbench-aa": None})
    assert set(components) == set(basket.INDEX_SDLC_TASKS) and reconciliation["reconciled"] is True
    assert v.restricted_cost(components, ["scicode"]) == 288.0
    assert v.restricted_cost(components, ["scicode", basket.CODING_AGENT_INDEX]) is None


def test_assemble_admission_subset_rows_and_plan_costs():
    result = assembled()
    assert result["admitted"] == [basket.CODING_AGENT_INDEX, *basket.INDEX_SDLC_TASKS]
    rows = {row["id"]: row for row in result["rows"]}
    assert rows["c"]["cost"]["subset"] is True and rows["a"]["cost"]["fullCost"] is True
    # FrontierCode carries AA's declined-task marker for A and is pending (one row of three).
    assert "frontiercode" in rows["a"]["components"] and result["admission"]["components"]["frontiercode"]["admitted"] is False
    assert rows["a"]["plan"]["costUsd"] == pytest.approx(rows["a"]["cost"]["costUsd"] / 10.0)
    assert rows["c"]["plan"]["fallback"] == "api"
    catalog = v.workload_catalog(result)
    assert [entry["role"] for entry in catalog.values()] == ["main", "subset"]
    with pytest.raises(ValueError, match="missing from the pinned snapshot"):
        v.assemble([{"id": "z", "name": "Z", "aaSlug": "z-max"}], documents(), release_day=DAY)
    unmapped = v.assemble([{"id": "z", "name": "Z", "aaSlug": "a-max"}], documents(), release_day=DAY)
    assert unmapped["rows"][0]["configurationMapped"] is False and basket.CODING_AGENT_INDEX not in unmapped["rows"][0]["components"]


def test_workload_catalog_skips_rows_without_any_cost():
    result = assembled(snapshot={"pages": [page("a-max", 1.0), page("b-max", 4.0), {"model": {"slug": "c-max"}}]})
    rows = {row["id"]: row for row in result["rows"]}
    assert rows["c"]["cost"]["workload"] is None
    assert len(v.workload_catalog(result)) == 1


def test_freeze_anchors_and_bar_reference():
    result = assembled()
    frozen = v.freeze(result, frozen_at="2026-10-19")
    main = frozen["workloads"][result["mainWorkload"]]
    assert main["role"] == "main" and main["anchors"]["api"]["referenceIds"] == ["a", "b"]
    subset = next(entry for entry in frozen["workloads"].values() if entry["role"] == "subset")
    assert subset["anchors"]["api"]["referenceIds"] == ["a", "b", "c"]
    # E192: the bar is the lower-median displayed quality of the non-provisional rows (a 58.28 and b 64.38; c is provisional).
    assert frozen["barReferences"][0]["id"] == v.BAR_ID and frozen["barReferences"][0]["levelConfiguration"] == "a"
    assert frozen["barReferences"][0]["level"] == pytest.approx(58.2804, abs=1e-4) and frozen["barPolicy"]["population"] == ["a", "b"]
    assert frozen["anchorPolicy"]["policyId"] == "complete-evidence-panel" and main["anchorStatus"] == "frozen"
    # E160: the main workload needs at least two complete-evidence references.
    lone = v.assemble(CONFIGURATIONS[:1], documents(), release_day=DAY)
    with pytest.raises(ValueError, match="main workload has 1 complete-evidence anchor references"):
        v.freeze(lone, frozen_at="2026-10-19")


def test_anchor_population_is_the_complete_evidence_panel_and_thin_subsets_have_no_anchors(monkeypatch):
    """E160: incomplete-evidence rows never set anchors; a subset workload below the minimum leaves its rows unscored."""

    result = assembled()
    main = result["mainWorkload"]
    assert v.anchor_population(result, result["admitted"]) == ["a", "b"]
    reordered = dict(result, rows=list(reversed(result["rows"])))
    assert v.freeze(reordered, frozen_at="d")["workloads"] == v.freeze(result, frozen_at="d")["workloads"]
    unresolved = assembled()
    row_b = next(row for row in unresolved["rows"] if row["id"] == "b")
    row_b["components"]["scicode"] = dict(row_b["components"]["scicode"], completeness=basket.UNRESOLVED)
    assert v.anchor_population(unresolved, unresolved["admitted"]) == ["a"]
    original = v.anchor_population

    def thin(assembled_, components):
        population = original(assembled_, components)
        return population if basket.CODING_AGENT_INDEX in components else population[:1]

    monkeypatch.setattr(v, "anchor_population", thin)
    routes = documents()["planRoutes"]
    routes["routes"].append({"id": "plan-c", "valueMultiple": 3.0, "valueMultipleKind": "controlled_account_workload_projection", "modelIds": ["c"], "planPriceUsd": 20})
    with_route = assembled(planRoutes=routes)
    frozen = v.freeze(with_route, frozen_at="d")
    subset = next(workload for workload, entry in frozen["workloads"].items() if entry["role"] == "subset")
    assert frozen["workloads"][subset]["anchors"] == {"api": None, "plan": None}
    assert frozen["workloads"][subset]["anchorStatus"].startswith("unavailable")
    output = v.score(with_route, frozen)
    rows = {row["id"]: row for row in output["rows"]}
    assert rows["c"]["api"]["costScore"] is None and rows["c"]["api"]["value"] is None and rows["c"]["api"]["rank"] is None
    assert [item["workload"] for item in output["gates"]["clip"]["api"]] == [main]
    assert output["measuredOnlyPlanView"]["rows"]["c"]["costScore"] is None
    assert output["workloads"][subset]["anchorStatus"].startswith("unavailable")


def test_plan_boxes_need_an_identified_finite_multiple():
    result = assembled()
    boxes = {box.row: box for box in v.plan_boxes(result)}
    assert set(boxes) == {"b"}
    assert boxes["b"].c_low == pytest.approx(result["rows"][1]["cost"]["lowUsd"] / 2.0)
    open_set = documents()["planRoutes"]
    open_set["routes"][1].update(identification="set-identified", valueMultipleLower=1.0)
    assert v.plan_boxes(assembled(planRoutes=open_set)) == []
    unrecorded = documents()["planRoutes"]
    del unrecorded["routes"][1]["valuationBasis"]
    assert v.plan_boxes(assembled(planRoutes=unrecorded)) == []  # E138: an unrecorded basis is never interval-eligible


def scored(**overrides):
    result = assembled(**overrides)
    return result, v.freeze(result, frozen_at="2026-10-19")


def test_score_ranks_gates_disclosures_and_intervals():
    result, frozen = scored()
    output = v.score(result, frozen)
    rows = {row["id"]: row for row in output["rows"]}
    assert {row["api"]["rank"] for row in output["rows"]} == {1, 2, 3}
    assert rows["c"]["quality"]["status"] == "scored" and rows["a"]["plan"]["selectionReason"] == "only remaining eligible route"
    assert rows["a"]["aaCostCaveat"].startswith("A has higher pricing") and rows["b"]["aaCostCaveat"] is None
    assert output["gates"]["hold"] is False and output["intervals"]["api"]["status"] == "evaluated"
    assert output["intervals"]["plan"]["universe"] == ["b"]
    assert output["costInfluence"]["api"]["commonWorkload"]["panel"] == ["a", "b"]
    manifest = {item["rule"]: item["status"] for item in output["manifest"]}
    assert manifest["subset scoring (O17)"] == "fired" and manifest["Plan exploratory label (E61)"] == "fired"
    assert output["measuredOnlyPlanView"]["rows"]["b"]["status"] == "measured, target-workload identified"
    assert output["measuredOnlyPlanView"]["rows"]["c"]["status"] == "no measured route"
    assert output["diagnostics"]["groupDrift"]["status"] == diagnostics.INSUFFICIENT_PANEL
    assert output["diagnostics"]["qualityDispersion"]["weightedSpread"]["status"] == diagnostics.INSUFFICIENT_PANEL
    assert manifest["configuration map coverage"] == "passed"
    mapping = documents()["configurationMap"]
    del mapping["rows"]["c"]
    unmapped, unmapped_frozen = scored(configurationMap=mapping)
    flagged = {item["rule"]: item for item in v.score(unmapped, unmapped_frozen)["manifest"]}["configuration map coverage"]
    assert flagged["status"] == "fired" and flagged["detail"].endswith(": c")


def test_score_refuses_unfrozen_workloads():
    result, frozen = scored()
    moved = dict(frozen, mainWorkload="elsewhere")
    with pytest.raises(ValueError, match="workload migration"):
        v.score(result, moved)
    trimmed = dict(frozen, workloads={result["mainWorkload"]: frozen["workloads"][result["mainWorkload"]]})
    with pytest.raises(ValueError, match="has no frozen anchors"):
        v.score(result, trimmed)


def test_score_manifest_branches_and_unevaluable_bars():
    result, frozen = scored()
    # A tight anchor object clips every row and holds the release; the reference lost its quality.
    tight = json.loads(json.dumps(frozen))
    for entry in tight["workloads"].values():
        for basis in ("api", "plan"):
            entry["anchors"][basis].update(low=1e6, high=2e6)
    output = v.score(result, tight)
    manifest = {item["rule"]: item["status"] for item in output["manifest"]}
    assert output["gates"]["hold"] is True and manifest["clip gate (E20)"] == "fired"
    zero_quality = assembled(snapshot={"pages": [page("a-max", 1.0), page("b-max", 4.0), page("c-max", 0.5, **{key: None for key in (
        "gdpval", "automationBenchPartialScore", "frontierCode", "lcr", "hle", "scicode", "critpt", "omniscience")})]},
        deepswe={"configurations": []}, bugHunt={"models": []})
    output = v.score(zero_quality, v.freeze(zero_quality, frozen_at="d"))
    row_c = next(row for row in output["rows"] if row["id"] == "c")
    assert row_c["quality"]["status"] == "quality not scoreable — no observed leaves" and row_c["api"]["value"] is None


def test_score_flags_partial_components_dominance_and_saturation():
    routes = documents()["planRoutes"]
    routes["routes"].append({"id": "plan-a-low", "valueMultiple": 1.0, "valueMultipleKind": "controlled_account_workload_projection", "modelIds": ["a"],
                             "planPriceUsd": 20, "checkedOn": "2026-10-10", "identification": "point-identified"})
    routes["routes"].append({"id": "plan-a-high", "valueMultiple": 50.0, "valueMultipleKind": "controlled_account_workload_projection", "modelIds": ["a"],
                             "planPriceUsd": 20, "checkedOn": "2026-10-10", "identification": "point-identified"})
    charts = documents()["costCharts"]
    charts["evaluations"][0]["rows"] = [{"model": "A (max)", "totalUsd": 9, "declinedTasks": True}, {"model": "B (max)", "totalUsd": 30, "declinedTasks": False}]
    mapping = documents()["configurationMap"]
    mapping["rows"]["b"]["frontiercode"] = "B (max)"
    mapping["rows"]["c"]["coding-agent-index"] = "agent-a"
    result, frozen = scored(planRoutes=routes, costCharts=charts, configurationMap=mapping,
                            snapshot={"pages": [page("a-max", 1.0, gdpval=2700.0), page("b-max", 4.0), page("c-max", 0.5)]})
    assert result["admission"]["components"]["frontiercode"]["admitted"] is False
    output = v.score(result, frozen)
    manifest = {item["rule"]: item["status"] for item in output["manifest"]}
    assert manifest["route dominance filter (E88)"] == "fired" and manifest["quality clipping audit (E110)"] == "fired"
    assert manifest["Plan exploratory label (E61)"] == "passed" and manifest["subset scoring (O17)"] == "vacuous"


def test_partial_component_rows_are_flagged():
    agents = documents()["codingAgents"]
    agents["configurations"].append({"label": "agent-c", "meanCostPerTaskUsd": 1.0, "components": []})
    mapping = documents()["configurationMap"]
    mapping["rows"]["c"]["coding-agent-index"] = "agent-c"
    pages = [page("a-max", 1.0), page("b-max", 4.0), page("c-max", 0.5)]
    pages[2]["model"]["intelligenceIndexCost"]["total"] = 1.0  # fails reconciliation: unresolved Index components
    result, frozen = scored(codingAgents=agents, configurationMap=mapping, snapshot={"pages": pages})
    output = v.score(result, frozen)
    assert {item["rule"]: item["status"] for item in output["manifest"]}["partial component flag (E37)"] == "fired"


def test_cost_influence_flag_fires_when_quality_dominates():
    pages = [page("a-max", 1.0, hle=0.0, scicode=0.0, critpt=0.0, lcr=0.0), page("b-max", 1.0001, hle=1.0, scicode=1.0, critpt=1.0, lcr=1.0), page("c-max", 0.5)]
    agents = documents()["codingAgents"]
    agents["configurations"][1]["meanCostPerTaskUsd"] = 2.0
    result, frozen = scored(snapshot={"pages": pages}, codingAgents=agents)
    output = v.score(result, frozen)
    assert {item["rule"]: item["status"] for item in output["manifest"]}["cost influence flag (E91)"] == "fired"


def test_quality_agreement_and_drift_on_real_panels():
    result, frozen = scored()
    agreement = v._quality_agreement(result["rows"])
    assert agreement["panel"] == []  # no synthetic row has both independent leaves
    assert v._group_drift(result["rows"])["panel"] == []

    def row(identifier, displayed, bug, tb):
        observations = {"bugHunt": q.Observation(bug), "terminalBench": q.Observation(tb)}
        return {"id": identifier, "evidence": {"observations": observations}, "summary": q.summarize(observations).__class__(**{**q.summarize(observations).__dict__, "displayed": displayed})}

    matched = v._quality_agreement([row("x", 50.0, 40.0, 40.0), row("y", 60.0, 50.0, 50.0), row("z", 70.0, 60.0, 60.0)])
    assert matched["panel"] == ["x", "y", "z"] and matched["tau"] == pytest.approx(1.0)


def agreement_row(identifier, bug, tb, **aa):
    observations = {"bugHunt": q.Observation(bug), "terminalBench": q.Observation(tb), **{key: q.Observation(z) for key, z in aa.items()}}
    return {"id": identifier, "evidence": {"observations": observations}, "summary": q.summarize(observations)}


def test_quality_substitution_agreement_holds_cost_fixed_and_swaps_quality():
    rows = [agreement_row("x", 40.0, 40.0), agreement_row("y", 50.0, 50.0), agreement_row("z", 60.0, 60.0), agreement_row("solo", 90.0, 90.0)]
    del rows[3]["evidence"]["observations"]["terminalBench"]  # off the matched panel
    # Displayed value orders z > y > x on both bases; with Q_ind swapped in, x's cheap cost puts it first on the Plan basis.
    per_row = {
        "x": {"api": {"value": 10.0, "costScore": 50.0}, "plan": {"value": 10.0, "costScore": 100.0}},
        "y": {"api": {"value": 20.0, "costScore": 50.0}, "plan": {"value": 20.0, "costScore": 0.0}},
        "z": {"api": {"value": 30.0, "costScore": 50.0}, "plan": {"value": 30.0, "costScore": 0.0}},
        "solo": {"api": {"value": 99.0, "costScore": 50.0}, "plan": {"value": 99.0, "costScore": 50.0}},
    }
    result = v._substitution_agreement(rows, per_row)
    assert result["api"]["panel"] == ["x", "y", "z"] and result["api"]["tau"] == pytest.approx(1.0)
    assert result["api"]["label"].startswith("quality-substitution value agreement, api basis")
    # Plan: substituted values x = 0.25*100 + 0.75*40 = 55, y = 37.5, z = 45 -> x > z > y against displayed z > y > x.
    assert result["plan"]["tau"] == pytest.approx(-1.0 / 3.0)


def test_disjoint_evidence_agreement_compares_aa_only_with_independent_only_quality():
    rows = [
        agreement_row("x", 40.0, 40.0, deepswe=30.0, gdpval=30.0),
        agreement_row("y", 50.0, 50.0, deepswe=50.0),
        agreement_row("z", 60.0, 60.0, deepswe=70.0, omniscience=70.0),
        agreement_row("none", 70.0, 70.0),  # no AA-executed leaf: left out of the panel
    ]
    result = v._disjoint_agreement(rows)
    assert result["panel"] == ["x", "y", "z"] and result["excluded"] == ["none"] and result["tau"] == pytest.approx(1.0)
    assert result["label"].startswith("disjoint-evidence agreement (restricted evidence comparison")
    assert result["retainedLeaves"]["independent"] == {"bugHunt": 50.0, "terminalBench": 50.0}
    assert set(result["retainedLeaves"]["aaExecuted"]) == {leaf.key for leaf in q.LEAVES if leaf.source == "aa"}


def test_policy_cohort_bar_is_a_sensitivity_over_frontier_families():
    """E199: the bar recomputed over frontier and near-frontier rows only, with its API result, or unavailable."""

    result, frozen = scored()
    policy = v.policy_cohort_bar(result, frozen)
    assert policy["status"] == "evaluated" and policy["bar"]["id"] == v.POLICY_BAR_ID and policy["api"]["status"] == "certified"
    result["rows"][1]["frontierFamily"] = False
    assert v.policy_cohort_bar(result, frozen)["status"].startswith("unavailable") and v.frontier_anchor_diagnostic(result, frozen, {})["bar"]["status"].startswith("unavailable")
    result["rows"][1]["frontierFamily"] = True
    for row in result["rows"]:
        row["cost"] = dict(row["cost"], fullCost=False)
    assert v.policy_cohort_bar(result, frozen)["api"] == {"status": "unevaluable"}


def test_the_bar_ladder_freezes_three_levels_with_the_median_first():
    """O34: the lower quartile, median and upper quartile of the population, median first (the headline bar)."""

    rows = [{"id": f"r{index}", "summary": SimpleNamespace(displayed=value, provisional=False)} for index, value in enumerate((10.0, 20.0, 30.0, 40.0, 50.0))]
    population, bars = v.bar_levels({"rows": rows})
    assert [bar["id"] for bar in bars] == [v.BAR_ID, "bar:lower-quartile-quality", "bar:upper-quartile-quality"]
    assert [bar["levelConfiguration"] for bar in bars] == ["r2", "r1", "r3"] and population == ["r0", "r1", "r2", "r3", "r4"]


def test_freeze_with_fewer_than_two_population_rows_pins_no_bar():
    """E192: a bar met by one configuration compares nothing, so fewer than two population rows pin no bar."""

    result = assembled()
    result["rows"][1]["summary"] = q.summarize({"deepswe": q.Observation(50.0)})  # b becomes provisional
    frozen = v.freeze(result, frozen_at="d")
    assert frozen["barReferences"] == [] and frozen["barPolicy"]["bars"] == [] and frozen["barPolicy"]["population"] == ["a"]


def test_bar_is_a_quality_level_that_is_never_its_own_answer():
    """E192: at freeze at least two population rows are at or above the level, and the median row competes like any other."""

    result = assembled()
    frozen = v.freeze(result, frozen_at="2026-10-19")
    level = frozen["barReferences"][0]["level"]
    assert sum(row["summary"].displayed >= level for row in result["rows"] if row["id"] in frozen["barPolicy"]["population"]) >= 2
    bar = v.interval_outputs(result, frozen, "api")["bars"][0]
    assert bar["reference"]["id"] == v.BAR_ID and set(bar["rows"]) == {"a", "b"}
    # a qualifies only possibly: its quality interval straddles its own displayed quality, which set the level.
    assert bar["rows"]["a"]["possible"] == "certified" and bar["rows"]["a"]["confirmed"] == "disproved"
    # E198: the result counts the configurations that can qualify and gives each row's displayed margin to the level.
    assert bar["possibleQualifierN"] == 2 and bar["comparison"] == "compares 2 configurations that can qualify"
    assert bar["rows"]["a"]["displayedMargin"] == pytest.approx(0.0) and bar["rows"]["b"]["displayedMargin"] > 0
    high = json.loads(json.dumps(frozen))
    high["barReferences"][0]["level"] = 100.5
    assert v.interval_outputs(result, high, "api")["bars"][0]["comparison"] == v.VACUOUS_COMPARISON
    result["rows"][0]["summary"] = q.summarize({})
    assert v.interval_outputs(result, frozen, "api")["bars"][0]["rows"]["a"]["displayedMargin"] is None


def test_bar_reference_selection_is_registered_and_outcome_independent(monkeypatch):
    """E156: input order cannot change the reference; bar outcomes are never computed at selection; provisional rows are excluded."""

    result = assembled()
    frozen = v.freeze(result, frozen_at="2026-10-19")
    policy = frozen["barPolicy"]
    assert policy["policyId"] == "quality-quartile-ladder" and policy["version"] == 3 and policy["selectionCutoff"] == "2026-10-19"
    assert policy["bars"] == [{key: item[key] for key in ("id", "level", "levelConfiguration")} for item in frozen["barReferences"]]
    reordered = dict(result, rows=list(reversed(result["rows"])))
    assert v.freeze(reordered, frozen_at="2026-10-19")["barReferences"] == frozen["barReferences"]

    def refuse(*_args, **_kwargs):
        raise AssertionError("bar outcomes must not be computed while selecting the reference")

    monkeypatch.setattr(v.intervals, "cheapest_above_bar", refuse)
    assert v.freeze(result, frozen_at="2026-10-19")["barReferences"] == frozen["barReferences"]
    for row in result["rows"]:
        row["summary"] = q.summarize({"deepswe": q.Observation(50.0)})  # every row provisional
    assert v.freeze(result, frozen_at="2026-10-19")["barReferences"] == []


def test_score_handles_rows_without_cost_and_empty_workloads():
    result = assembled(snapshot={"pages": [page("a-max", 1.0), page("b-max", 4.0), {"model": {"slug": "c-max"}}]})
    frozen = v.freeze(result, frozen_at="d")
    frozen["workloads"]["unused"] = json.loads(json.dumps(frozen["workloads"][result["mainWorkload"]]))
    output = v.score(result, frozen)
    row_c = next(row for row in output["rows"] if row["id"] == "c")
    assert row_c["api"]["costScore"] is None and row_c["api"]["rank"] is None
    assert [item["workload"] for item in output["gates"]["clip"]["api"]] == [result["mainWorkload"]]


def test_interval_outputs_without_api_rows():
    result, frozen = scored()
    for row in result["rows"]:
        row["cost"] = dict(row["cost"], fullCost=False)
    assert v.interval_outputs(result, frozen, "api")["reason"] == "no row has FullCost on the main workload"


def test_scenarios_hash_attach_and_bar_labels():
    result, frozen = scored()
    panel = v.scenario_panel(result, "api")
    assert [item.row for item in panel] == ["a", "b"]
    assert panel[0].leaves["deepswe"].family == "fixed" and panel[1].leaves["deepswe"].family == "uniform"
    document = v.run_scenarios(result, frozen, n=200, seed=7)
    assert document["inputHash"] == v.scenario_hash(result, frozen, n=200, seed=7)
    assert [run["stratum"] for run in document["results"]["api"]] == ["S0", "S1", "S2", "S1", "S1M"]
    assert document["streamDescriptions"]["S0"] == "published-record reporting precision" and len(document["notQuantified"]) == 2
    assert document["barLabels"][0]["status"] == "evaluated"
    current = v.attach_scenarios(v.score(result, frozen), document, document["inputHash"])
    assert current["scenarios"]["status"] == "current" and current["gates"]["hold"] is False
    stale = v.attach_scenarios(v.score(result, frozen), document, "other")
    assert stale["scenarios"]["status"].startswith("stale") and stale["gates"]["hold"] is True
    missing = v.attach_scenarios(v.score(result, frozen), None, "x")
    assert missing["scenarios"] == {"status": "missing"} and missing["manifest"][-1]["status"] == "fired"
    assert document["barLabels"][0]["level"] == frozen["barReferences"][0]["level"]
    # E19/E34/E122: the named S2 branches are listed; one agent per configuration leaves the harness band unevaluable.
    band, cache, price = document["namedBranches"]
    assert band["status"] == "unevaluable" and band["width"] is None and "results" not in band
    assert cache["status"] == price["status"] == "unevaluable" and cache["id"].startswith("cache-hit")
    # E87: every row of every stream publishes its dispersion decomposition.
    assert document["results"]["api"][0]["rows"]["a"]["dispersion"]["status"] == "defined"


def test_harness_band_runs_a_named_s2_branch_when_a_configuration_has_two_agents():
    rows = [
        {"model": "M (max)", "agent": "Terminus 2", "resolutionRatePct": 50.0},
        {"model": "M (max)", "agent": "Claude Code", "resolutionRatePct": 58.0},
        {"model": "N (high)", "agent": "Terminus 2", "resolutionRatePct": 40.0},
        {"model": "N (high)", "agent": "Codex", "resolutionRatePct": 44.0},
        {"model": "N (high)", "agent": "Muse Code", "resolutionRatePct": None},
        {"model": "Solo (max)", "agent": "Codex", "resolutionRatePct": 70.0},
    ]
    band = v.harness_band(rows)
    assert band["status"] == "evaluated" and band["spreads"] == {"M (max)": 8.0, "N (high)": 4.0} and band["width"] == 6.0
    result, frozen = scored(tb4={"rows": rows})
    panel = {item.row: item for item in v.scenario_panel(result, "api", harness=6.0)}
    stressed = panel["a"].leaves["bugHunt"]  # a's Bug Hunt z is 52 of 105 bugs, on the 0-100 scale
    observed = result["rows"][0]["evidence"]["observations"]["bugHunt"].z
    assert stressed.params == pytest.approx((observed - 3.0, observed + 3.0)) and stressed.target == scenarios.SPECIFICATION_STRESS
    assert "bugHunt" not in panel["b"].leaves
    document = v.run_scenarios(result, frozen, n=50, seed=7)
    branch = document["namedBranches"][0]
    assert branch["results"]["api"]["stratum"] == "S2" and branch["results"]["plan"]["transfers"] == "off"
    assert document["inputHash"] != v.scenario_hash(scored()[0], frozen, n=50, seed=7)  # the band width is a scenario input


def test_subset_bridges_pair_full_rows_on_both_workloads_and_disclose_missing_shares():
    result, frozen = scored()
    output = v.score(result, frozen)
    (bridge,) = output["diagnostics"]["subsetBridges"]
    assert bridge["subsetRows"] == ["c"] and bridge["pairedRows"] == ["a", "b"] and bridge["missingComponents"] == ["coding-agent-index"]
    share = bridge["missingExpenditureShare"]["coding-agent-index"]
    assert share["n"] == 2 and share["min"] <= share["median"] <= share["max"] and bridge["direction"].startswith("not known")
    api = bridge["bases"]["api"]
    assert api["status"] == "evaluated" and set(api["rows"]) == {"a", "b"} and api["valueDifference"]["n"] == 2
    assert api["rows"]["a"]["fullValue"] == pytest.approx(next(row for row in output["rows"] if row["id"] == "a")["api"]["value"])
    assert api["exchangeRates"]["subset"]["anchorRatio"] != api["exchangeRates"]["main"]["anchorRatio"]
    # A subset workload without anchors reports their status; no expenditure evidence leaves the shares empty.
    unanchored = json.loads(json.dumps(frozen))
    subset = next(key for key, entry in unanchored["workloads"].items() if entry["role"] == "subset")
    unanchored["workloads"][subset].update(anchors={"api": None, "plan": None}, anchorStatus="unavailable: fewer than 2 complete-evidence references")
    per_row = {row["id"]: {basis: {"value": row[key]["value"]} for basis, key in (("api", "api"), ("plan", "planScore"))} for row in output["rows"]}
    (empty,) = v.subset_bridges(result, unanchored, per_row, {})
    assert empty["bases"]["api"] == {"status": "unavailable: fewer than 2 complete-evidence references"}
    assert empty["missingExpenditureShare"]["coding-agent-index"] == {"median": None, "min": None, "max": None, "n": 0}


def test_cost_component_family_registers_one_removal_per_admitted_unit():
    result, frozen = scored()
    family = v.score(result, frozen)["diagnostics"]["costComponentFamily"]
    assert [item["component"] for item in family] == result["admitted"] and {item["status"] for item in family} == {"evaluated"}
    assert all(item["component"] not in item["alternativeWorkload"]["components"] for item in family)


def test_workday_status_needs_an_evidenced_quota_schema():
    assert v.workday_status(None)["status"].startswith("not applicable")
    route = {"route": {"id": "r"}}
    assert v.workday_status(route) == {"status": "not evaluated: no evidenced quota schema for this route", "rule": v.WORKDAY_RULE}
    with pytest.raises(ValueError, match="E70 capacity program"):
        v.workday_status({"route": {"id": "r", "quotaSchema": {"windows": ["5h"]}}})
    result, frozen = scored()
    rows = {row["id"]: row for row in v.score(result, frozen)["rows"]}
    assert rows["b"]["plan"]["workday"]["status"].startswith("not evaluated") and rows["c"]["plan"]["workday"]["status"].startswith("not applicable")


def write_world(root: Path) -> Path:
    data = root / "data"
    for relative, content in {
        "aa/aa_v432_snapshot.json": documents()["snapshot"],
        "aa_deepswe.json": documents()["deepswe"],
        "bug_hunt.json": documents()["bugHunt"],
        "tb4.json": documents()["tb4"],
        "aa/coding_agents_capture.json": documents()["codingAgents"],
        "aa/cost_charts_capture.json": documents()["costCharts"],
        "v3_configuration_map.json": documents()["configurationMap"],
        "plan_cost_routes.json": {**documents()["planRoutes"], "evidencePolicy": {"reportingWindow": {"start": "2026-09-19", "end": "2026-10-19"}, "searchCutoff": "2026-10-19"}},
        "price_records.json": documents()["priceRecords"],
        "aa_frontier_capture.json": {"points": []},
        # The roster is a bare JSON list; the Bug Hunt scoreboard is the O31 roster-check input.
        "aa_mapping.json": [{"id": item["id"], "displayName": item["name"]} for item in CONFIGURATIONS],
        "bug_hunt_scoreboard.json": {"capturedAt": "2026-10-21T06:30:00Z", "rows": [{"model": "A (max effort)", "fixedOf105": 10.0}]},
        "scores.json": {
            "models": [{"id": item["id"], "name": item["name"], "aaVariant": item["effort"], "aaSlug": item["aaSlug"], "rankingEligible": True} for item in CONFIGURATIONS]
            + [{"id": "out", "name": "Out", "aaSlug": "out", "rankingEligible": False}],
        },
    }.items():
        target = data / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(content))
    return data


def test_command_line_freeze_scenarios_and_build(tmp_path, capsys, monkeypatch):
    data = write_world(tmp_path)
    monkeypatch.setenv("VALUERANK_NOW", "2026-10-19T12:00:00Z")
    assert v.main(["freeze"], data=data) == 0
    assert json.loads(capsys.readouterr().out)["wrote"] == "data/v3_frozen.json"
    configurations = v.configurations_from_scores(json.loads((data / "scores.json").read_text()))
    assert v.build(configurations, data, release_day=DAY)["scenarios"]["status"] == "missing"
    assert v.main(["scenarios", "--scenarios", "100"], data=data) == 0
    built = v.build(configurations, data, release_day=DAY)
    assert built["scenarios"]["status"] == "current" and built["scenarios"]["scenarios"] == 100
    assert v.scenario_seed(DAY) == 20261019


def test_dual_run_scores_one_evidence_set_on_two_anchor_versions(tmp_path, capsys, monkeypatch):
    """O12/E197: a re-anchoring publishes old- and new-anchor results side by side, bars included."""

    result, frozen = scored()
    wider = json.loads(json.dumps(frozen))
    wider["anchorVersion"] = "v3-next"
    for entry in wider["workloads"].values():
        for basis in ("api", "plan"):
            entry["anchors"][basis].update(high=entry["anchors"][basis]["high"] * 4)
    document = v.dual_run(result, frozen, wider)
    assert document["previousAnchorVersion"] == frozen["anchorVersion"] and document["anchorVersion"] == "v3-next"
    row = next(item for item in document["rows"] if item["row"] == "a")
    assert row["api"]["current"]["costScore"] > row["api"]["previous"]["costScore"]
    assert document["bars"]["api"]["previous"][0]["reference"]["id"] == v.BAR_ID and "previous" in document["bars"]["plan"]
    data = write_world(tmp_path)
    monkeypatch.setenv("VALUERANK_NOW", "2026-10-19T12:00:00Z")
    assert v.main(["freeze"], data=data) == 0
    capsys.readouterr()
    previous = tmp_path / "previous.json"
    previous.write_text((data / v.FROZEN_FILE).read_text())
    assert v.main(["dual-run", "--previous", str(previous)], data=data) == 0
    assert json.loads(capsys.readouterr().out)["wrote"] == f"data/{v.DUAL_RUN_FILE}"
    assert all(item["api"]["previous"] == item["api"]["current"] for item in json.loads((data / v.DUAL_RUN_FILE).read_text())["rows"])
    with pytest.raises(SystemExit):
        v.main(["dual-run"], data=data)


def test_module_entry_point(tmp_path, monkeypatch):
    data = write_world(tmp_path)
    monkeypatch.setenv("VALUERANK_NOW", "2026-10-19T12:00:00Z")
    monkeypatch.setattr(v, "DATA", data)
    monkeypatch.setattr(sys, "argv", ["value_v3", "freeze"])
    monkeypatch.setattr("valuerank.paths.DATA", data)
    with pytest.raises(SystemExit) as stop:
        runpy.run_module("valuerank.value_v3", run_name="__main__")
    assert stop.value.code == 0


def test_json_default_rejects_unknown_objects():
    with pytest.raises(TypeError, match="not JSON serializable: object"):
        v._json_default(object())


def test_terminal_bench_same_harness_diagnostic():
    """E125: the default-harness variant, harness-mixed rows and their agreement panel."""

    tb4 = [
        {"model": "Opus 5.5 (max)", "agent": "Claude Code", "resolutionRatePct": 64.0},
        {"model": "Sonnet 5.5 (max)", "agent": "Terminus 2", "resolutionRatePct": 50.0},
        {"model": "Haiku 5.5 (max)", "agent": "Terminus 2", "resolutionRatePct": 30.0},
    ]
    rows = []
    for model_id in ("claude-opus-5-5", "claude-sonnet-5-5", "claude-haiku-5-5"):
        evidence = v.leaf_evidence(model_id, "max", {}, None, tb4, None)
        rows.append({"id": model_id, "effort": "max", "evidence": evidence})
    result = v._tb_same_harness(rows, tb4)
    assert result["harnessMixed"] == ["claude-opus-5-5"]
    assert result["restricted"] == {"claude-sonnet-5-5": 50.0, "claude-haiku-5-5": 30.0}
    assert result["agreement"]["panel"] == ["claude-haiku-5-5", "claude-sonnet-5-5"]


def test_abstention_sensitivity_and_demand_registry():
    pages = [page("a-max", 1.0, omniscience=-40.0), page("b-max", 4.0), page("c-max", 0.5)]
    del pages[2]["model"]["omniscience"]
    result, frozen = scored(snapshot={"pages": pages})
    output = v.score(result, frozen)
    sensitivity = output["diagnostics"]["omniscienceAbstentionSensitivity"]
    assert sensitivity["rule"] == "z_pen = max(0, I)" and sensitivity["rankChanges"]["panel"] == ["a", "b", "c"]
    rows = {row["id"]: row for row in output["rows"]}
    assert rows["a"]["quality"]["leaves"]["omniscience"]["abstentionPenalisedZ"] == 0.0
    assert rows["a"]["quality"]["leaves"]["omniscience"]["unansweredOrPartialShare"] == pytest.approx(0.5 * 0.6)
    # E181: the GDPval-AA logistic alternative is published per basis as rank changes on the common panel.
    logistic = output["diagnostics"]["gdpvalLogisticSensitivity"]
    assert logistic["rule"].startswith("z = 100 / (1 + 10^((1600 - E) / 400))") and logistic["api"]["rankChanges"]["panel"] == ["a", "b", "c"]
    # E128: with every question correct nothing is unanswered (the conditional hallucination rate is undefined).
    perfect = [page("a-max", 1.0, omniscience=100.0, omniscienceAccuracy=1.0, omniscienceHallucinationRate=None), page("b-max", 4.0), page("c-max", 0.5, gdpval=None)]
    perfect_rows = {row["id"]: row for row in v.score(*scored(snapshot={"pages": perfect}))["rows"]}
    assert perfect_rows["a"]["quality"]["leaves"]["omniscience"]["unansweredOrPartialShare"] == 0.0
    registry = rows["a"]["demandRegistry"]
    assert set(registry["populations"]) == {"intelligence-index", basket.CODING_AGENT_INDEX}
    index_population = registry["populations"]["intelligence-index"]
    assert index_population["residualComponents"] == list(basket.INDEX_RESIDUAL_TASKS) and index_population["componentOutputTokens"] == {}
    assert index_population["outputEqualsReasoningPlusAnswer"] is None
    stability = output["diagnostics"]["anchorStability"]
    assert stability["exchangeRateSeries"][0]["anchorVersion"] == frozen["anchorVersion"]
    tokens = v.demand_registry(
        {"intelligenceIndexEvaluations": [{"slug": "scicode", "outputTokensPerTask": 10.0}, {"slug": "critpt", "outputTokensPerTask": 1.0}],
         "canonicalIntelligenceIndexTokenCount": {"input": 9, "output": 5, "reasoning": 3, "answer": 2}},
        ["scicode", "gdp-pdf"],
    )
    population = tokens["populations"]["intelligence-index"]
    # Residual (excluded) evaluations keep their demand outside W; the Coding Agent Index is not admitted here.
    assert population["componentOutputTokens"] == {"scicode": 2880.0, "critpt": 70.0} and population["scoredComponents"] == ["gdp-pdf", "scicode"]
    assert population["outputEqualsReasoningPlusAnswer"] is True and set(tokens["populations"]) == {"intelligence-index"}
    assert tokens["tokenOntology"]["canonicalIntelligenceIndexTokenCount.output"]["mapping"] == "inclusive"


def test_unknown_fees_are_written_as_null():
    routes = documents()["planRoutes"]
    del routes["routes"][0]["planPriceUsd"]
    result, frozen = scored(planRoutes=routes)
    row_a = next(row for row in v.score(result, frozen)["rows"] if row["id"] == "a")
    assert row_a["plan"]["comparisonTuples"]["plan-a"][-1] is None
    json.dumps(row_a, allow_nan=False)


def test_deletion_branches_renormalise_the_remaining_observed_leaves():
    """E146: displayed-score deletion sensitivity per registered branch; leave-AA-out is not identifiable today."""

    branches = {item["id"]: item for item in v.deletion_branches()}
    assert len(branches) == len(q.LEAVES) + 2
    # E178: the basket-scope branch removes the leaves of the benchmarks O15 excludes from the cost basket.
    assert sorted(branches["basket-scope"]["removed"]) == ["critpt", "hle", "omniscience"] and len(basket.INDEX_RESIDUAL_TASKS) == 3
    assert branches["leave-out:bugHunt"]["labels"] == ["leave-one-benchmark-out", "leave-one-source-out"]
    assert branches["leave-out:deepswe"]["labels"] == ["leave-one-benchmark-out"]
    observations = {"deepswe": q.Observation(80.0), "bugHunt": q.Observation(20.0)}
    assert v.deletion_quality(observations, {"bugHunt"}) == pytest.approx(80.0)
    assert v.deletion_quality(observations, {"deepswe", "bugHunt"}) is None
    result, frozen = scored()
    sensitivity = {item["id"]: item for item in v.score(result, frozen)["diagnostics"]["deletionSensitivity"]}
    aa_out = sensitivity["leave-source-out:Artificial Analysis"]
    assert aa_out["status"] == "not identifiable under the coverage rule" and aa_out["retainedNominalWeight"] == pytest.approx(0.2)
    deep = sensitivity["leave-out:deepswe"]
    assert deep["status"] == "evaluated" and deep["retainedNominalWeight"] == pytest.approx(0.7)
    assert sensitivity["basket-scope"]["status"] == "evaluated" and sensitivity["basket-scope"]["retainedNominalWeight"] == pytest.approx(0.8667, abs=1e-4)
    assert deep["bases"]["api"]["rankChanges"]["panel"] == ["a", "b", "c"] and deep["unevaluableRows"] == []
    rows = [{"id": "x", "evidence": {"observations": {"deepswe": q.Observation(50.0)}}}]
    per_row = {"x": {"api": {"value": 40.0, "costScore": 20.0}, "plan": {"value": None, "costScore": None}}}
    crafted = {item["id"]: item for item in v._deletion_sensitivity(rows, per_row)}
    assert crafted["leave-out:deepswe"]["unevaluableRows"] == ["x"]
    assert crafted["leave-out:deepswe"]["bases"]["api"]["kendallTauB"] is None
    assert crafted["leave-out:bugHunt"]["bases"]["plan"]["rankChanges"]["panel"] == []


def test_bar_labels_fail_when_the_compiled_dependency_graph_is_not_the_registered_one(monkeypatch):
    """E147: v1 registers singleton components; a shared varying primitive fails the build."""

    result, frozen = scored()
    original = v.scenario_panel

    def linked(assembled_, basis):
        panel = original(assembled_, basis)
        for item in panel:
            item.meta["sharedPrimitives"] = ["price-list"]
        return panel

    monkeypatch.setattr(v, "scenario_panel", linked)
    with pytest.raises(ValueError, match="registered kernel-check object"):
        v.bar_labels(result, frozen, seed=1, batch=50)


def test_standing_cost_removal_has_fixed_and_recalibrated_calculations():
    """E64/E149: AA's Index-run Terminal-Bench cost removed, scored on the original and on rebuilt anchors."""

    result, frozen = scored()
    output = v.score(result, frozen)
    removal = output["diagnostics"]["costRemoval"]
    assert removal["status"] == "evaluated" and removal["component"] == "terminalbench-4-0"
    assert "terminalbench-4-0" not in removal["alternativeWorkload"]["components"]
    api, plan = removal["bases"]["api"], removal["bases"]["plan"]
    assert api["fixedAnchors"]["label"] == v.FIXED_ANCHOR_LABEL and api["multiplePolicy"] is None
    assert plan["multiplePolicy"] == v.FIXED_MULTIPLE_LABEL
    assert api["recalibrated"]["rankChanges"]["panel"] == ["a", "b"]
    assert api["recalibrated"]["anchors"]["high"] < frozen["workloads"][result["mainWorkload"]]["anchors"]["api"]["high"]
    # Uniform per-task costs make the removal proportional: no rank changes on either calculation.
    assert api["fixedAnchors"]["rankChanges"]["maxAbsChange"] == 0 and api["recalibrated"]["rankChanges"]["maxAbsChange"] == 0
    per_row = {row["id"]: {basis: {"value": None} for basis in v.BASES} for row in result["rows"]}
    assert v.cost_removal(result, frozen, per_row, component="frontiercode") == {"component": "frontiercode", "status": "not in the admitted basket"}


def test_cost_removal_is_typed_by_basis():
    """E152 fixture: API basket 100 with Index-run Terminal-Bench 20 and displayed multiple 4 -> Plan 25, removal (100 - 20) / 4 = 20."""

    def component(cost):
        return basket.component_cost(cost, completeness=basket.COMPLETE, source="s")

    route_ = {"id": "p", "valueMultiple": 4.0}
    row = {"components": {"scicode": component(80.0), "terminalbench-4-0": component(20.0)}, "routeSelection": {"selected": {"route": route_}}}
    full, removed = ["scicode", "terminalbench-4-0"], ["scicode"]
    assert v.basis_cost_on(row, full, "plan") == 25.0 and v.basis_cost_on(row, removed, "plan") == 20.0  # never 25 - 20 = 5
    assert v.basis_cost_on(row, removed, "api") == 80.0  # scored only against API anchors
    fallback = dict(row, routeSelection={"selected": None})
    assert v.basis_cost_on(fallback, removed, "plan") == 80.0


def test_cost_kernels_derive_the_basket_cost_from_component_draws():
    """E154: two rounded components are drawn separately and summed with the exact part; never one uniform on the sum."""

    def component(cost, half=0.0):
        return basket.component_cost(cost, half_width=half, completeness=basket.COMPLETE, source="s")

    components = {"scicode": component(100.0), "frontiercode": component(10.0, 0.5), "itbench-aa": component(20.0, 0.5)}
    row = {"components": components, "cost": {**basket.row_cost(components, list(components)), "components": list(components)}}
    kernel = v._cost_kernel(row, 130.0)
    assert kernel.family == "uniform-sum" and kernel.params == (100.0, (9.5, 10.5), (19.5, 20.5))
    halved = v._cost_kernel(row, 65.0)  # a Plan cost at multiple 2 scales every term
    assert halved.params == (50.0, (4.75, 5.25), (9.75, 10.25))
    single = {"components": {"scicode": component(100.0), "frontiercode": component(10.0, 0.5)}}
    single["cost"] = basket.row_cost(single["components"], list(single["components"]))
    assert v._cost_kernel(single, 110.0) == v._kernel(109.5, 110.5, 110.0)


def test_valuation_contract_and_cost_boundary():
    """E157/E158: AA's category-linear valuation; banded tariffs leave tariff-corrected valuation unidentified;
    each component's charge classes, with only documented exclusions."""

    flagged = v.valuation_contract("higher long-context pricing not reflected")
    assert flagged["tariffCorrectedValuation"].startswith("unidentified") and flagged["providerBillingRule"].startswith("banded")
    plain = v.valuation_contract(None)
    assert plain["providerBillingRule"] == "not recorded" and plain["valuationSufficiency"].startswith("category totals sufficient")
    assert v.cost_boundary("gdp-pdf")["preparation"] == "excluded" and v.cost_boundary("gdp-pdf")["contestantModelTokens"] == "included"
    assert v.cost_boundary("scicode")["executionEnvironment"] == "unknown"
    result, frozen = scored()
    output = v.score(result, frozen)
    assert output["costBoundary"]["label"].startswith("contestant-model API token cost")
    assert set(output["costBoundary"]["components"]) == set(result["admitted"])
    rows = {row["id"]: row for row in output["rows"]}
    assert rows["a"]["valuation"]["providerBillingRule"].startswith("banded") and rows["b"]["valuation"]["providerBillingRule"] == "not recorded"


def test_evidence_bundle_hashes_every_input_artifact(tmp_path, monkeypatch):
    """E159: each artifact's content hash, capture time and extractor; each leaf points to its artifact and field."""

    data = write_world(tmp_path)
    monkeypatch.setenv("VALUERANK_NOW", "2026-10-19T12:00:00Z")
    assert v.main(["freeze"], data=data) == 0
    bundle = v.evidence_bundle(data)
    assert [item["key"] for item in bundle["artifacts"]] == [*v.EVIDENCE_FILES, "anchors"]
    snapshot = bundle["artifacts"][0]
    import hashlib
    assert snapshot["sha256"] == hashlib.sha256((data / "aa/aa_v432_snapshot.json").read_bytes()).hexdigest()
    assert snapshot["capturedAt"] is None and bundle["artifacts"][-1]["capturedAt"] == "2026-10-19"
    by_key = {item["key"]: item for item in bundle["artifacts"]}
    assert by_key["roster"]["artifact"] == "data/aa_mapping.json" and by_key["roster"]["capturedAt"] is None  # a list has no capture time
    assert by_key["roster"]["sha256"] == hashlib.sha256((data / "aa_mapping.json").read_bytes()).hexdigest()
    assert by_key["bugHuntScoreboard"]["artifact"] == "data/bug_hunt_scoreboard.json" and by_key["bugHuntScoreboard"]["capturedAt"] == "2026-10-21T06:30:00Z"
    assert len(bundle["bundleHash"]) == 64
    configurations = v.configurations_from_scores(json.loads((data / "scores.json").read_text()))
    built = v.build(configurations, data, release_day=DAY)
    assert built["evidenceBundle"]["bundleHash"] == bundle["bundleHash"]
    leaves = {row["id"]: row["quality"]["leaves"] for row in built["rows"]}
    assert leaves["a"]["gdpval"]["evidence"] == {"artifact": "data/aa/aa_v432_snapshot.json", "locator": "pages[model.slug=a-max].model.gdpval", "publishedValue": 1500.0}
    assert leaves["a"]["bugHunt"]["evidence"]["locator"] == "models[modelId=a].fixedOf105"
    assert leaves["a"]["deepswe"]["evidence"]["artifact"] == "data/aa_deepswe.json"


def test_measurement_stream_draws_the_published_confidence_interval():
    """E162/E165: Terminal-Bench's documented 95% CI enters only the S1M panel, clipped to the leaf's domain, as a conventional range."""

    result, frozen = scored()
    rows = {row["id"]: row for row in result["rows"]}
    rows["a"]["evidence"]["observations"]["terminalBench"] = q.Observation(60.0, 0.05)
    rows["a"]["evidence"]["provenance"]["terminalBench"] = {"source": "tbench", "ci95HalfWidthPct": 3.1}
    rows["b"]["evidence"]["observations"]["terminalBench"] = q.Observation(99.0, 0.05)
    rows["b"]["evidence"]["provenance"]["terminalBench"] = {"source": "tbench", "ci95HalfWidthPct": 3.1}
    plain = {item.row: item for item in v.scenario_panel(result, "api")}
    measured = {item.row: item for item in v.scenario_panel(result, "api", measurement=True)}
    assert plain["a"].leaves["terminalBench"].target == "reporting precision"
    kernel = measured["a"].leaves["terminalBench"]
    assert kernel.params == pytest.approx((56.9, 63.1)) and kernel.target == "published-interval range (conventional)" and kernel.alternative == "endpoint-heavy"
    # E182: b's interval is clipped at 100, so the kernel keeps its published 99 as the median.
    assert measured["b"].leaves["terminalBench"].family == "split-uniform" and measured["b"].leaves["terminalBench"].params == pytest.approx((95.9, 99.0, 100.0))
    assert kernel.family == "uniform"
    assert measured["a"].leaves["deepswe"] == plain["a"].leaves["deepswe"]
    document = v.run_scenarios(result, frozen, n=50, seed=3)
    s1m = document["results"]["api"][-1]
    assert s1m["stratum"] == "S1M" and s1m["variedTargets"] == ["identification convention", "published-interval range (conventional)", "reporting precision"]
    interpretation = document["intervalInterpretation"]["S1M"][0]
    assert interpretation["leaf"] == "terminalBench" and interpretation["kernelStatus"] == "conventional-within-CI"
    assert interpretation["permittedLabel"] == "conventional CI-range sensitivity (endpoint-conditioned; no tail model)"


def calibration_row(row_id, workload, quality, *, partial=(), fallback=None, grade="controlled", gate=None):
    return {
        "id": row_id,
        "cost": {"workload": workload, "partialComponents": list(partial)},
        "plan": {"fallback": fallback, "grade": grade},
        "summary": SimpleNamespace(displayed=quality),
        "valuationGate": {"outcome": gate or v.GATE_COMPATIBLE},
    }


def test_measured_calibration_rescores_measured_rows_on_measured_anchors():
    """E164: holding rows, routes, costs and quality fixed, measured-evidence anchors expose the calibration effect."""

    official = anchor_math.anchor_object({"cheap": 5.0, "dear": 4000.0, "x": 10.0, "gone": 50.0}, basis="plan", workload="w1")
    frozen = {"workloads": {"w1": {"anchors": {"plan": official}}, "w2": {"anchors": {"plan": None}}}}
    rows = [
        calibration_row("x", "w1", 60.0),
        calibration_row("y", "w1", 70.0),
        calibration_row("p", "w1", 65.0, partial=["gdp-pdf"]),
        calibration_row("q", "w1", None),
        calibration_row("cheap", "w1", 40.0, grade="assumption"),
        calibration_row("dear", "w1", 50.0, fallback="api"),
        calibration_row("lone", "w2", 55.0),
    ]
    entries = {}
    for row_id, cost in (("x", 10.0), ("y", 40.0), ("p", 20.0), ("q", 30.0), ("lone", 12.0)):
        anchors = official if row_id != "lone" else None
        score = anchor_math.cost_score(cost, anchors) if anchors else None
        quality = next(row for row in rows if row["id"] == row_id)["summary"].displayed
        entries[row_id] = {"status": "measured, target-workload unmatched", "costUsd": cost, "costScore": score, "value": anchor_math.value_score(score, quality, v.BETA)}
    entries["cheap"] = entries["dear"] = {"status": "no measured route"}
    result = v._measured_calibration(rows, frozen, entries)
    w1, w2 = result["workloads"]["w1"], result["workloads"]["w2"]
    assert result["status"] == "evaluated" and w1["status"] == "evaluated"
    assert w1["references"] == ["q", "x", "y"] and w1["rows"] == ["p", "q", "x", "y"]
    assert w1["anchors"]["low"] == pytest.approx(5.0) and w1["anchors"]["high"] == pytest.approx(80.0)
    assert w1["officialAnchorProvenance"] == {"low": {"row": "cheap", "evidence": "owner-named transfer"}, "high": {"row": "dear", "evidence": "API-cost fallback"}}
    assert w1["exchangeRate"]["anchorRatio"] == pytest.approx(16.0) and w1["officialExchangeRate"]["anchorRatio"] == pytest.approx(3200.0)
    assert w2 == {"rows": ["lone"], "references": ["lone"], "officialAnchorProvenance": None, "status": "measured-evidence calibration unavailable (fewer than two measured references)"}
    assert result["values"]["q"] is None and set(result["values"]) == {"p", "q", "x", "y"}
    # Cheaper, weaker rows gain on the narrow measured anchors: official y > p > x becomes x > p > y.
    assert result["reversals"] == [["p", "x"], ["p", "y"], ["x", "y"]]
    assert result["rankChange"]["changes"] == {"p": 0, "x": -2, "y": 2}
    assert result["maxAbsValueChange"] == pytest.approx(max(abs(result["values"][key] - entries[key]["value"]) for key in ("p", "x", "y")))


def test_measured_calibration_never_takes_a_row_on_a_price_not_in_force_as_reference():
    official = anchor_math.anchor_object({"x": 10.0, "y": 40.0}, basis="plan", workload="w1")
    rows = [calibration_row("x", "w1", 60.0), calibration_row("y", "w1", 70.0), calibration_row("stale", "w1", 45.0, gate=v.GATE_NOT_IN_FORCE)]
    entries = {row_id: {"status": "measured", "costUsd": cost, "costScore": None, "value": None} for row_id, cost in (("x", 10.0), ("y", 40.0), ("stale", 1000.0))}
    w1 = v._measured_calibration(rows, {"workloads": {"w1": {"anchors": {"plan": official}}}}, entries)["workloads"]["w1"]
    assert w1["references"] == ["x", "y"] and w1["rows"] == ["stale", "x", "y"]  # O29: it stays in the view, never an anchor


def test_measured_calibration_without_references_and_unknown_anchor_rows():
    official = anchor_math.anchor_object({"retired": 5.0, "x": 10.0}, basis="plan", workload="w1")
    frozen = {"workloads": {"w1": {"anchors": {"plan": official}}}}
    entries = {"x": {"status": "measured, target-workload unmatched", "costUsd": 10.0, "costScore": 50.0, "value": 55.0}}
    result = v._measured_calibration([calibration_row("x", "w1", 60.0)], frozen, entries)
    assert result["status"] == "measured-evidence calibration unavailable"
    assert result["workloads"]["w1"]["officialAnchorProvenance"]["low"] == {"row": "retired", "evidence": "not in the current table"}
    assert result["values"] == {} and result["reversals"] == [] and result["maxAbsValueChange"] is None
    assert v._plan_evidence(calibration_row("r", "w1", 1.0, grade="reports")) == "concordant reports"


def test_rounded_records_need_a_registered_joint_law():
    """E154: v1 registers only the singleton law; records linked by a sampling identity fail the build."""

    assert v.rounding_components(["frontiercode", "itbench-aa"]) == [["frontiercode"], ["itbench-aa"]]
    assert v.rounding_components(["frontiercode"], (("index-total", "residual"),)) == [["frontiercode"]]
    with pytest.raises(ValueError, match=r"no registered joint rounding law \(E154\) for the rounded-record components \[\['a', 'b', 'c'\]\]"):
        v.rounding_components(["a", "b", "c", "d"], (("a", "b"), ("b", "c")))
    assert v.JOINT_LAWS == {"singleton": "independent uniform within the reporting interval (arcsine alternative)"} and v.SAMPLING_IDENTITIES == ()


def test_core_plan_streams_run_with_transfers_off():
    """E167: a transfer-dependent row is unevaluable in S1, S2 and S1M on the Plan basis; S0 keeps the displayed record."""

    routes = documents()["planRoutes"]
    routes["routes"][0].update(valueMultipleKind="user_assumption", evidenceClass="user_assumption")
    result, frozen = scored(planRoutes=routes)
    rows = {row["id"]: row for row in result["rows"]}
    assert v.transfer_dependent(rows["a"]) and not v.transfer_dependent(rows["b"]) and not v.transfer_dependent(rows["c"])
    assert [item.row for item in v.scenario_panel(result, "plan")] == ["a", "b"]
    assert [item.row for item in v.scenario_panel(result, "plan", transfers=False)] == ["b"]
    assert [item.row for item in v.scenario_panel(result, "api", transfers=False)] == [item.row for item in v.scenario_panel(result, "api")]
    assert v.transfers_on("S0") and not any(v.transfers_on(stratum) for stratum in ("S1", "S2", "S1M"))
    document = v.run_scenarios(result, frozen, n=50, seed=3)
    runs = {(run["stratum"], run["alternative"]): run for run in document["results"]["plan"]}
    assert runs[("S0", False)]["transfers"] == "on (the displayed record)" and runs[("S0", False)]["excluded"] == [] and "a" in runs[("S0", False)]["rows"]
    for key in (("S1", False), ("S2", False), ("S1", True), ("S1M", False)):
        assert runs[key]["transfers"] == "off" and runs[key]["excluded"] == [{"row": "a", "reason": v.TRANSFER_EXCLUSION}]
        assert list(runs[key]["rows"]) == ["b"]
    assert all("transfers" not in run and "excluded" not in run for run in document["results"]["api"])
    assert document["inputHash"] != v.run_scenarios(*scored(), n=50, seed=3)["inputHash"]


def test_plan_amount_is_typed_by_what_the_measurement_establishes():
    """E166/E168: an amount is capacity only when the measurement establishes it, and M x F reproduces it only within one object."""

    route = {"id": "r", "valueMultiple": 10.0, "planPriceUsd": 20, "additionalCashUsd": 5}
    base = {"route": route, "grade": "controlled", "identification": "unidentified", "valuation": "unverified", "donorRouteId": None}
    established = {"measurementCapacityStatus": "capacity established on the measurement workload"}
    capacity = v.plan_amount({**base, **established})
    assert capacity["amountKind"] == "measured-workload capacity" and capacity["amountTarget"] == "measured-workload capacity"
    assert capacity["amountUsd"] == pytest.approx(250.0) and capacity["derivation"] == "measurement identity: U_obs = M_obs x F_obs"
    assert capacity["grossCashUsd"] == 25.0 and capacity["additionalCashUsd"] == 5.0 and capacity["feePeriod"] == "month"
    assert capacity["cashObjectId"] == "r:month cash" and capacity["measurementObjectId"] == "r" and capacity["capacitySolutionId"] is None
    assert capacity["interpretationLabel"] == "measured-workload capacity, API-priced USD per month" and capacity["valuationStatus"] == "unverified"
    recorded = v.plan_amount({**base, **established, "route": {**route, "apiEquivalentUsd": 240.0, "measurementWorkload": "w-meas"}, "measurementObjectId": "m1"})
    assert recorded["amountUsd"] == 240.0 and recorded["derivation"] == "measurement record: its recorded numerator U_obs = M_obs x F_obs (kind not recorded)" and recorded["workload"] == "w-meas"
    projected = v.plan_amount({**base, **established, "route": {**route, "apiEquivalentUsd": 240.0, "numeratorKind": "workload_capacity_projection"}})
    assert projected["derivation"].endswith("(workload capacity projection)")
    assert recorded["measurementObjectId"] == "m1"
    observed = v.plan_amount({**base, "grade": "reports", "measurementCapacityStatus": "eligible delivered consumption observed, capacity not established"})
    assert observed["amountKind"] == "observed eligible consumption (capacity not established)" and observed["amountTarget"] == "measured-workload consumption"
    transfer = v.plan_amount({**base, **established, "grade": "assumption", "donorRouteId": "donor"})
    assert transfer["amountKind"] == "assumed API-equivalent consumption (owner-named transfer)" and transfer["donorRouteId"] == "donor"
    assert transfer["amountUsd"] == pytest.approx(250.0) and transfer["derivation"].startswith("authorised assumption")
    identified = {**base, "identification": "point-identified"}
    fixed = v.plan_amount({**identified, "route": {**route, "paymentRule": "fixed", "feePeriod": "week", "capacitySolutionId": "s1"}}, "w-main")
    assert fixed["amountKind"] == "identified target-workload capacity" and fixed["workload"] == "scored workload w-main" and fixed["feePeriod"] == "week"
    assert fixed["amountUsd"] == pytest.approx(250.0) and fixed["derivation"].startswith("valid multiplication") and fixed["capacitySolutionId"] == "s1"
    solver = v.plan_amount({**identified, "route": {**route, "targetCapacityUsd": 100.0}}, "w-main")
    assert solver["amountUsd"] == 100.0 and solver["derivation"] == "capacity solver projection (U_W*)"
    # A target multiple times another object's cash is never published as capacity (consumption-dependent payment).
    hybrid = v.plan_amount({**identified, "route": {**route, "paymentRule": "consumption-dependent"}}, "w-main")
    assert hybrid["amountUsd"] is None and hybrid["derivation"] == v.NO_TARGET_LINEAGE
    unpriced = v.plan_amount({**base, "route": {"id": "x", "valueMultiple": 1.5}})
    assert unpriced["amountUsd"] is None and unpriced["grossCashUsd"] is None and unpriced["amountKind"] == "observed eligible consumption (capacity not established)"
    assert v.plan_amount({**base, "grade": "assumption", "route": {"id": "x", "valueMultiple": 1.5}})["amountUsd"] is None
    assert v.plan_amount(None) is None


def test_route_alternatives_list_every_admissible_pair_with_its_displayed_score():
    routes = documents()["planRoutes"]
    routes["routes"].append({"id": "plan-a-low", "valueMultiple": 1.0, "valueMultipleKind": "controlled_account_workload_projection", "modelIds": ["a"],
                             "planPriceUsd": 20, "checkedOn": "2026-10-10", "identification": "point-identified"})
    routes["routes"].append({"id": "plan-a-high", "valueMultiple": 50.0, "valueMultipleKind": "controlled_account_workload_projection", "modelIds": ["a"],
                             "planPriceUsd": 20, "checkedOn": "2026-10-10", "identification": "point-identified"})
    result, frozen = scored(planRoutes=routes)
    rows = {row["id"]: row for row in v.score(result, frozen)["rows"]}
    alternatives = rows["a"]["plan"]["routeAlternatives"]
    table = alternatives["pairs"]
    assert [item["routeId"] for item in table] == ["plan-a-high", "plan-a-low", "plan-a"]  # comparator order
    # E179: counts and the leave-selected-out choice (plan-a-low is no longer dominated once plan-a-high leaves).
    assert alternatives["admissiblePairs"] == 3 and alternatives["unidentifiedPairs"] == 1
    assert alternatives["leaveSelectedOut"]["routeId"] == "plan-a-low"
    by_id = {item["routeId"]: item for item in table}
    assert by_id["plan-a-high"]["status"] == "selected" and by_id["plan-a-low"]["status"] == "dominated by plan-a-high (E88)"
    assert by_id["plan-a"]["status"] == "not selected by the comparator" and by_id["plan-a"]["comparisonWithSelected"] == v.ALTERNATIVE_ARITHMETIC
    assert by_id["plan-a-high"]["comparisonWithSelected"] == v.ALTERNATIVE_IDENTIFIED
    assert by_id["plan-a-high"]["displayedPlanValue"] == pytest.approx(rows["a"]["planScore"]["value"])
    assert by_id["plan-a-high"]["displayedPlanValue"] > by_id["plan-a-low"]["displayedPlanValue"]
    assert rows["c"]["plan"]["routeAlternatives"] == {"pairs": [], "admissiblePairs": 0, "unidentifiedPairs": 0, "leaveSelectedOut": None}
    unanchored = result["rows"][0]
    assert v.route_alternatives(unanchored, None)["pairs"][0]["displayedPlanValue"] is None


PRICES = {"input": 2.0, "cacheRead": 0.2, "cacheWrite": 2.0, "output": 10.0}


def priced_page(slug, cost_per_task, prices, **fields):
    """A page whose Index category costs come from 10M uncached, 100M cache-read, 5M cache-write and 2M output tokens
    priced at ``prices`` (no cache-write price is displayed, so cache writes bill at the input rate)."""

    base = page(slug, cost_per_task, **fields)
    base["model"]["intelligenceIndexCost"].update(nonCacheInput=10 * prices["input"], cacheRead=100 * prices["cacheRead"], cacheWrite=5 * prices["cacheWrite"], output=2 * prices["output"])
    base["model"]["canonicalIntelligenceIndexTokenCount"] = {"input": 115e6, "output": 2e6}
    return base


def test_displayed_prices_and_reconciliation():
    model = priced_page("a-max", 1.0, PRICES)["model"]
    assert v.displayed_prices(model) == PRICES  # cache writes at the input rate where none is listed
    assert v.displayed_prices({**model, "cacheWritePrice": 2.5})["cacheWrite"] == 2.5
    assert v.displayed_prices({**model, "cacheHitPrice": None}) is None
    assert v.reconciles(model, PRICES) is True
    assert v.reconciles(model, {**PRICES, "output": 20.0}) is False
    assert v.reconciles(page("a-max", 1.0)["model"], PRICES) is None  # category costs not published


def test_valuation_gate_outcomes():
    model = priced_page("a-max", 1.0, PRICES)["model"]
    assert v.valuation_gate(model, [], "t")["outcome"] == v.GATE_COMPATIBLE
    unpublished = v.valuation_gate(page("a-max", 1.0)["model"], [], "t")
    assert unpublished["outcome"] == v.GATE_COMPATIBLE and unpublished["reason"].startswith("category costs not published")
    record = {"id": "old", "aaSlug": "a-max", "prices": PRICES, "tariffStatus": "superseded", "effectiveFrom": "2026-01-01", "effectiveUntil": "2026-10-10"}
    # Every displayed price doubled since AA's valuation: exact revaluation by k = 2.
    doubled = {**model, "price1mInputTokens": 4.0, "cacheHitPrice": 0.4, "price1mOutputTokens": 20.0}
    stranger = {"id": "other", "aaSlug": "a-max", "prices": {**PRICES, "output": 7.0}}
    revalued = v.valuation_gate(doubled, [stranger, record], "t")  # a record that does not reconcile is skipped
    assert revalued["outcome"] == v.GATE_REVALUED and revalued["factor"] == pytest.approx(2.0) and revalued["appliedRecord"]["id"] == "old"
    # Only the output price moved: not in force at V (O29), with the convex-combination bounds.
    output_only = {**model, "price1mOutputTokens": 15.0}
    flagged = v.valuation_gate(output_only, [record], "t")
    assert flagged["outcome"] == v.GATE_NOT_IN_FORCE and flagged["flag"] == "AA cost at superseded price"
    assert flagged["bounds"]["apiCost"] == pytest.approx([1.0, 1.5]) and flagged["bounds"]["planCost"] == pytest.approx([1 / 1.5, 1.5])
    promotion = v.valuation_gate(output_only, [{**record, "tariffStatus": "promotional"}], "t")
    assert promotion["flag"] == "AA cost at standard price during a promotion"
    assert v.valuation_gate(output_only, [], "t")["outcome"] == v.GATE_UNVERIFIED
    assert v.valuation_gate({**model, "price1mOutputTokens": None}, [], "t")["reason"].startswith("AA displays no complete price vector")
    # The bounds bracket the exact repriced cost for any demand vector (C'/C is a demand-weighted mean of the ratios).
    ratios = flagged["bounds"]["ratios"]
    for demand in ({"input": 1, "cacheRead": 0, "cacheWrite": 0, "output": 9}, {"input": 5, "cacheRead": 50, "cacheWrite": 1, "output": 1}):
        before = sum(PRICES[key] * demand[key] for key in demand)
        after = sum(PRICES[key] * ratios[key] * demand[key] for key in demand)
        assert before * flagged["bounds"]["apiCost"][0] - 1e-9 <= after <= before * flagged["bounds"]["apiCost"][1] + 1e-9


def test_revalue_scales_every_priced_component():
    components = {"x": {"costUsd": 10.0, "halfWidthUsd": 0.5, "completeness": "complete"}, "y": {"costUsd": None, "halfWidthUsd": 0.0}}
    scaled = v.revalue(components, 2.0)
    assert scaled["x"]["costUsd"] == 20.0 and scaled["x"]["halfWidthUsd"] == 1.0 and scaled["y"] == components["y"]


def gated_world(gate_page, records):
    configurations = CONFIGURATIONS + [{"id": "d", "name": "D", "effort": "max", "aaSlug": "d-max"}]
    return v.assemble(configurations, gated_world_documents(gate_page, records), release_day=DAY)


def gated_world_documents(gate_page, records):
    pages = [gate_page, page("b-max", 4.0), page("c-max", 0.5), page("d-max", 2.0)]
    agents = documents()["codingAgents"]
    agents["configurations"].append({"label": "agent-d", "meanCostPerTaskUsd": 3.0, "totalCostUsd": 900.0, "components": []})
    mapping = documents()["configurationMap"]
    mapping["rows"]["d"] = {"coding-agent-index": "agent-d", "frontiercode": None, "itbench-aa": None}
    routes = documents()["planRoutes"]
    routes["routes"][0].update(identification="point-identified", valuationBasis="release")
    return documents(snapshot={"pages": pages}, codingAgents=agents, configurationMap=mapping, planRoutes=routes, priceRecords={"records": records})


def test_gate_effects_on_costs_anchors_routes_and_interval_labels(monkeypatch):
    record = {"id": "old", "aaSlug": "a-max", "prices": PRICES, "tariffStatus": "superseded"}
    base = gated_world(priced_page("a-max", 1.0, PRICES), [record])
    doubled = gated_world(priced_page("a-max", 1.0, PRICES, price1mInputTokens=4.0, cacheHitPrice=0.4, price1mOutputTokens=20.0), [record])
    rows = {row["id"]: row for row in doubled["rows"]}
    assert rows["a"]["valuationGate"]["outcome"] == v.GATE_REVALUED
    assert rows["a"]["cost"]["costUsd"] == pytest.approx(2.0 * next(row for row in base["rows"] if row["id"] == "a")["cost"]["costUsd"])
    flagged = gated_world(priced_page("a-max", 1.0, PRICES, price1mOutputTokens=15.0), [record])
    rows = {row["id"]: row for row in flagged["rows"]}
    assert rows["a"]["valuationGate"]["outcome"] == v.GATE_NOT_IN_FORCE
    assert rows["a"]["routeSelection"]["selected"] is None  # O29: no multiple on the row's own price record
    assert v.anchor_population(flagged, flagged["admitted"]) == ["b", "d"]
    frozen = v.freeze(flagged, frozen_at="2026-10-19")
    output = v.interval_outputs(flagged, frozen, "api")
    assert output["blockers"] == ["a"] and output["frontier"]["a"] == {"status": v.WITHHELD_LABEL}
    assert "a" not in output["universe"] and "a" not in output["unevaluable"]
    box = next(item for item in v.api_boxes(flagged) if item.row == "a")
    assert box.provisional is True and box.c_high == pytest.approx(rows["a"]["cost"]["highUsd"] * 1.5)
    # An unresolved bar (e.g. coupled boxes, E89) carries no row table to withhold from.
    with monkeypatch.context() as patch:
        patch.setattr(v.intervals, "cheapest_above_bar", lambda *_args, **_kwargs: {"status": v.intervals.UNRESOLVED, "reason": "coupled"})
        unresolved_bar = v.interval_outputs(flagged, frozen, "api")
    assert unresolved_bar["bars"][0]["status"] == v.intervals.UNRESOLVED and unresolved_bar["blockers"] == ["a"]
    # O29: a multiple valued on the row's own superseded record stays eligible.
    routes = documents()["planRoutes"]
    routes["routes"][0].update(identification="point-identified", valuationBasis="release", valuationPriceRecord="old")
    kept = v.assemble(
        CONFIGURATIONS + [{"id": "d", "name": "D", "effort": "max", "aaSlug": "d-max"}],
        {**gated_world_documents(priced_page("a-max", 1.0, PRICES, price1mOutputTokens=15.0), [record]), "planRoutes": routes},
        release_day=DAY,
    )
    assert next(row for row in kept["rows"] if row["id"] == "a")["routeSelection"]["selected"]["route"]["id"] == "plan-a"
    unverified = gated_world(priced_page("a-max", 1.0, PRICES, price1mOutputTokens=15.0), [])
    assert "a" not in [item.row for item in v.api_boxes(unverified)]
    assert "a" not in [item.row for item in v.plan_boxes(unverified)]  # never interval-eligible, on either basis
    assert {row["id"]: row for row in unverified["rows"]}["a"]["valuationGate"]["outcome"] == v.GATE_UNVERIFIED


def test_release_publishes_gate_metering_and_source_registry_facts():
    result, frozen = scored()
    output = v.score(result, frozen)
    rows = {row["id"]: row for row in output["rows"]}
    assert rows["a"]["valuationGate"]["outcome"] == rows["a"]["tariffStatus"] == v.GATE_COMPATIBLE
    assert rows["a"]["valuation"]["tokenMeteringBasis"].startswith("not published per configuration")
    assert rows["a"]["valuation"]["cacheRateProvenance"].startswith("AA's live measurement")
    assert output["meteringMix"] == {"provider-reported": 0, "canonical-tokenizer fallback": 0, "not published per configuration": 3}
    gdpval = next(item for item in output["sourceIntervals"] if item["leaf"] == "gdpval")
    assert gdpval["status"] == "published, not captured" and gdpval["level"].startswith("not stated")
    assert output["sourceDates"]["LiveBench 2.0"]["release"] == "2026-10-14"


def test_a_migration_without_two_eligible_references_is_deferred():
    """E184: a newly admissible component stays pending when its workload could not be anchored; no hold."""

    result, frozen = scored()
    charts = documents()["costCharts"]
    charts["evaluations"][0]["rows"] = [{"model": "A (max)", "totalUsd": 9, "declinedTasks": False}, {"model": "B (max)", "totalUsd": 30, "declinedTasks": False}]
    mapping = documents()["configurationMap"]
    mapping["rows"]["b"]["frontiercode"] = "B (max)"
    gained = documents(costCharts=charts, configurationMap=mapping)
    assert "frontiercode" in v.assemble(CONFIGURATIONS, gained, release_day=DAY)["admitted"]
    # Both full rows pass the valuation gate: an ordinary migration, scored only after a new freeze.
    ordinary = v.assemble_for_release(CONFIGURATIONS, gained, frozen, release_day=DAY)
    assert ordinary["mainWorkload"] != frozen["mainWorkload"] and ordinary["deferred"] == []
    # b's AA cost cannot be valued: one eligible reference, so the migration is deferred.
    unpriced = copy.deepcopy(gained)
    unpriced["snapshot"]["pages"][1]["model"]["price1mOutputTokens"] = None
    deferred = v.assemble_for_release(CONFIGURATIONS, unpriced, frozen, release_day=DAY)
    assert deferred["mainWorkload"] == frozen["mainWorkload"] and deferred["deferred"] == [{"component": "frontiercode", "reason": v.DEFERRED_MIGRATION}]
    output = v.score(deferred, frozen)
    manifest = {item["rule"]: item for item in output["manifest"]}
    assert manifest["anchor migration (E184)"]["status"] == "fired" and output["deferredComponents"][0]["component"] == "frontiercode"
    assert output["gates"]["hold"] is False
    # An unchanged workload is returned as assembled.
    assert v.assemble_for_release(CONFIGURATIONS, documents(), frozen, release_day=DAY)["mainWorkload"] == result["mainWorkload"]


def test_bound_domain_checks_and_unconstructible_blockers():
    """E185: a newly priced category leaves no bound; a zero price in force leaves the Plan bound open; both unresolve."""

    model = priced_page("a-max", 1.0, PRICES)["model"]
    free_write = {"id": "free", "aaSlug": "a-max", "prices": {**PRICES, "cacheWrite": 0.0}}
    priced = {**model, "price1mOutputTokens": 15.0, "intelligenceIndexCost": {**model["intelligenceIndexCost"], "cacheWrite": 0.0}}
    gate = v.valuation_gate({**priced, "canonicalIntelligenceIndexTokenCount": {"input": 110e6, "output": 2e6}}, [free_write], "t")
    assert gate["outcome"] == v.GATE_NOT_IN_FORCE and gate["bounds"] == {"status": v.BOUND_UNAVAILABLE}
    assert v.blocker_domain(gate, "api") is None
    # Cache reads became free: r = 0 for them, so the API bound starts at 0 and the Plan bound has no upper end.
    zero_now = v.valuation_gate({**model, "cacheHitPrice": 0.0, "price1mOutputTokens": 15.0}, [{"id": "old", "aaSlug": "a-max", "prices": PRICES}], "t")
    assert zero_now["bounds"]["apiCost"] == pytest.approx([0.0, 1.5]) and zero_now["bounds"]["planCost"][1] is None
    assert v.blocker_domain(zero_now, "api") is None
    assert v.displayed_prices({**model, "price1mOutputTokens": 0.0}) is None and v.displayed_prices({**model, "cacheHitPrice": True}) is None
    assert v.reconciles(model, {**PRICES, "output": 0.0}) is False and v.reconciles(model, {**PRICES, "cacheRead": 0.0}) is False
    open_plan = {"bounds": {"status": "available", "apiCost": [0.0, 1.5], "planCost": [0.0, None]}}
    assert v.blocker_domain(open_plan, "api") is None and v.blocker_domain(open_plan, "plan") is None
    assert v.blocker_domain({"bounds": {"status": "available", "apiCost": [0.5, 1.5], "planCost": [0.3, 3.0]}}, "plan") == (0.3, 3.0)
    record = {"id": "free", "aaSlug": "a-max", "prices": {**PRICES, "cacheWrite": 0.0}}
    page_free = priced_page("a-max", 1.0, {**PRICES, "cacheWrite": 0.0}, price1mOutputTokens=15.0)
    world = gated_world(page_free, [record])
    rows = {row["id"]: row for row in world["rows"]}
    assert rows["a"]["valuationGate"]["bounds"] == {"status": v.BOUND_UNAVAILABLE}
    frozen = v.freeze(gated_world(priced_page("a-max", 1.0, PRICES), []), frozen_at="2026-10-19")
    output = v.interval_outputs(world, frozen, "api")
    assert output["status"] == "unresolved" and output["blockers"] == ["a"] and "a" not in output["unevaluable"]
    assert output["reason"].startswith("a blocker's current-tariff domain cannot be constructed")


def test_anchor_eligibility_table_names_each_exclusion():
    record = {"id": "old", "aaSlug": "a-max", "prices": PRICES, "tariffStatus": "superseded"}
    flagged = gated_world(priced_page("a-max", 1.0, PRICES, price1mOutputTokens=15.0), [record])
    table = {item["row"]: item for item in v.anchor_eligibility(flagged, flagged["admitted"])}
    assert table["a"]["eligible"] is False and table["a"]["reason"] == f"valuation gate: {v.GATE_NOT_IN_FORCE}"
    assert table["c"]["reason"] == "incomplete cost evidence" and table["b"] == {"row": "b", "completeEvidence": True, "valuationGate": v.GATE_COMPATIBLE, "eligible": True, "reason": None}


def test_scenario_labels_never_go_to_or_past_an_unsafe_blocker(monkeypatch):
    """E186: a qualifying, possibly cheaper blocker withholds the scenario label; a blocker is never a candidate."""

    record = {"id": "old", "aaSlug": "a-max", "prices": PRICES, "tariffStatus": "superseded"}
    flagged = gated_world(priced_page("a-max", 1.0, PRICES, price1mOutputTokens=15.0), [record])
    frozen = v.freeze(flagged, frozen_at="2026-10-19")
    # At level 60 b and d can be cheapest, and the blocker a can reach the level and undercut both.
    frozen["barReferences"] = [{"id": v.BAR_ID, "level": 60.0, "levelConfiguration": "b", "rule": "x"}]
    monkeypatch.setattr(v.scenarios, "kernel_robust_cheapest", lambda *args, **kwargs: {"label": True, "reading": "supported"})
    (bar,) = v.bar_labels(flagged, frozen, seed=1, batch=20)
    assert sorted(bar["candidates"]) == ["b", "d"]
    assert all(result == {"label": False, "reading": v.BLOCKER_UNRESOLVED} for result in bar["candidates"].values())
    boxes = v.api_boxes(flagged)
    reference = v.intervals.Reference(v.BAR_ID, 0.0, 0.0)
    assert v.blocker_safe("b", reference, boxes, {"a"}) is False  # the blocker can qualify and be cheaper
    far = [box if box.row != "a" else v.intervals.Box("a", 1e9, 2e9, box.q_low, box.q_high, True) for box in boxes]
    assert v.blocker_safe("b", reference, far, {"a"}) is True
    assert v.blocker_safe("b", reference, [box for box in boxes if box.row != "a"], {"a"}) is False  # no constructible domain
    assert v.blocker_safe("b", v.intervals.Reference(v.BAR_ID, 101.0, 101.0), boxes, {"a"}) is True  # the blocker cannot reach the bar


def test_a_category_free_under_both_tariffs_is_left_out_of_the_bound():
    """E185: free then and free now contributes zero to both valuations; the other ratios still bound the cost."""

    free = {**PRICES, "cacheWrite": 0.0}
    model = priced_page("a-max", 1.0, free)["model"]
    gate = v.valuation_gate({**model, "cacheWritePrice": 0.0, "price1mOutputTokens": 15.0}, [{"id": "old", "aaSlug": "a-max", "prices": free}], "t")
    assert gate["outcome"] == v.GATE_NOT_IN_FORCE and set(gate["bounds"]["ratios"]) == {"input", "cacheRead", "output"}
    assert gate["bounds"]["apiCost"] == pytest.approx([1.0, 1.5])


def test_frontier_anchor_diagnostic_and_subset_intervals():
    """E187: anchors rebuilt from frontier families only; E190: interval outputs on the subset workload."""

    result, frozen = scored()
    output = v.score(result, frozen)
    frontier = output["diagnostics"]["frontierAnchors"]
    assert frontier["status"] == "evaluated" and frontier["references"] == ["a", "b"]
    assert frontier["bases"]["api"]["rankChanges"]["panel"] == ["a", "b"] and "frozenExchangeRate" in frontier["bases"]["plan"]
    (subset,) = output["subsetIntervals"].values()
    assert subset["api"]["universe"] == ["a", "b", "c"] and subset["plan"]["reason"] == v.SUBSET_PLAN_INTERVALS
    assert output["costInfluence"]["api"]["orderingAgreement"]["qualityVsValue"] is not None
    assert output["costInfluence"]["api"]["commonWorkload"]["varianceAllocation"] is not None
    retained = [dict(item, frontierFamily=item["id"] != "b") for item in CONFIGURATIONS]
    narrow = v.assemble(retained, documents(), release_day=DAY)
    per_row = {row["id"]: {basis: {"value": 1.0} for basis in v.BASES} for row in narrow["rows"]}
    assert v.frontier_anchor_diagnostic(narrow, frozen, per_row)["status"].startswith("unavailable")


def test_family_primary_diagnostic_rebuilds_ladder_and_anchors_on_primary_rows():
    """E205: one row per family, beside the frozen ladder and anchors (a diagnostic)."""

    result, frozen = scored()
    family = v.score(result, frozen)["diagnostics"]["familyPrimary"]
    assert family["status"] == "evaluated" and family["references"] == ["a", "b"] and [bar["id"] for bar in family["ladder"]] == [v.BAR_ID]
    assert family["frozenLadder"] == [{"id": bar["id"], "level": bar["level"]} for bar in frozen["barReferences"]]
    assert "frozenExchangeRate" in family["bases"]["plan"]
    siblings = [dict(item, familyPrimary=item["id"] != "b") for item in CONFIGURATIONS]
    narrow = v.assemble(siblings, documents(), release_day=DAY)
    per_row = {row["id"]: {basis: {"value": 1.0} for basis in v.BASES} for row in narrow["rows"]}
    lone = v.family_primary_diagnostic(narrow, frozen, per_row)
    assert lone["status"].startswith("unavailable") and "b" not in lone["population"] and "bases" not in lone


def test_configurations_record_frontier_family_membership():
    scores = {"models": [
        {"id": "f", "name": "F", "aaSlug": "f", "rankingEligible": True, "rankingInclusionReasons": [v.RETAINED_REASON, "Required AA Intelligence Index versus total-evaluation-cost frontier family"]},
        {"id": "r", "name": "R", "aaSlug": "r", "rankingEligible": True, "rankingInclusionReasons": [v.RETAINED_REASON]},
    ]}
    assert [item["frontierFamily"] for item in v.configurations_from_scores(scores)] == [True, False]


def test_configuration_carries_identity_and_frontier_family_flag_for_any_row():
    """E187: build_scores passes every scored row through configuration(), so retained rows reach v3 as non-frontier."""

    frontier = {"id": "f", "name": "F", "aaVariant": "max", "aaSlug": "f-max", "aaFrontierFootnote": "note",
                "rankingInclusionReasons": ["Required AA Intelligence Index versus total-evaluation-cost frontier family"]}
    assert v.configuration(frontier) == {"id": "f", "name": "F", "family": "F", "effort": "max", "aaSlug": "f-max", "aaNote": "note", "frontierFamily": True, "familyPrimary": True}
    retained = {"id": "r", "name": "R", "aaSlug": "r", "rankingInclusionReasons": [v.RETAINED_REASON], "familyPrimary": False}
    assert v.configuration(retained) == {"id": "r", "name": "R", "family": "R", "effort": None, "aaSlug": "r", "aaNote": None, "frontierFamily": False, "familyPrimary": False}
    # O33: an evidenced sibling carries its AA family, which its display name no longer equals.
    sibling = {"id": "f-high", "name": "F (high)", "family": "F", "aaVariant": "high", "aaSlug": "f-high", "rankingInclusionReasons": [v.RETAINED_REASON]}
    assert v.configuration(sibling)["family"] == "F" and v.configuration(sibling)["frontierFamily"] is False
    assert v.configuration({"id": "x", "name": "X", "aaSlug": "x"})["frontierFamily"] is False  # no stated reason


def test_cheaper_siblings_lists_same_family_points_below_the_row_cost():
    """E201: cheaper plotted configurations of the same family, never the row's own effort or another family."""

    configuration = {"name": "Fam", "effort": "max", "aaSlug": "fam"}
    points = [
        {"model_name": "Fam (high)", "family": "Fam", "effort": "high", "total_cost_usd": 5.0},
        {"model_name": "Fam (max)", "family": "Fam", "effort": "max", "total_cost_usd": 4.0},
        {"model_name": "Fam (low)", "family": "Fam", "effort": "low", "total_cost_usd": 50.0},
        {"model_name": "Other", "family": "Other", "effort": None, "total_cost_usd": 1.0},
    ]
    assert v.cheaper_siblings(configuration, {"intelligenceIndexCost": {"total": 10.0}}, points) == ["Fam (high)"]
    assert v.cheaper_siblings(configuration, {}, points) == []


def test_cheaper_siblings_leave_out_ranked_configurations_and_match_on_family():
    """E201/O33: a cheaper configuration of the family that is itself ranked is evaluated, so it is not listed; a
    sibling whose name carries its effort is matched to the chart through its AA family."""

    points = [
        {"model_name": "Fam (high)", "family": "Fam", "effort": "high", "total_cost_usd": 5.0},
        {"model_name": "Fam (medium)", "family": "Fam", "effort": "medium", "total_cost_usd": 3.0},
        {"model_name": "Fam (low)", "family": "Fam", "effort": "low", "total_cost_usd": 1.0},
    ]
    page = {"intelligenceIndexCost": {"total": 10.0}}
    primary = {"name": "Fam", "effort": "max"}
    assert v.cheaper_siblings(primary, page, points, {"max", "high"}) == ["Fam (medium)", "Fam (low)"]
    sibling = {"name": "Fam (high)", "family": "Fam", "effort": "high"}
    assert v.cheaper_siblings(sibling, {"intelligenceIndexCost": {"total": 5.0}}, points, {"max", "high", "low"}) == ["Fam (medium)"]
    assert v.configuration_family({"name": "Solo"}) == "Solo"


def test_displayed_cheapest_reads_the_headline_scale_with_ties_listed():
    """E203: the cheapest non-provisional scored main-workload row reaching each bar, or none."""

    result, frozen = scored()
    ladder = dict(frozen, barReferences=[{"id": "low", "level": 0.0}, {"id": "high", "level": 101.0}])
    low, high = v.displayed_cheapest(result, ladder, "api")["bars"]
    assert low["cheapest"] and low["qualifierN"] >= 1 and low["costUsd"] is not None
    assert high == {"bar": "high", "level": 101.0, "qualifierN": 0, "costUsd": None, "cheapest": []}


def test_bar_currency_flags_a_headline_bar_outside_the_current_interquartile_range():
    """E207: reach of each frozen bar in the current population, and an informational flag (no score changes)."""

    population = {"rows": [{"id": f"r{i}", "summary": SimpleNamespace(displayed=10.0 * i, provisional=False)} for i in range(5)]}
    _ids, bars = v.bar_levels(population)
    frozen = {"barReferences": bars}
    current = v.bar_currency(population, frozen)
    assert current["flag"] is None and current["lifetime"] == v.BAR_LIFETIME
    assert [(item["level"], item["reachN"], item["populationN"]) for item in current["bars"]] == [(20.0, 3, 5), (10.0, 4, 5), (30.0, 2, 5)]

    def moved(level):
        return {"barReferences": [dict(bar, level=level) if bar["id"] == v.BAR_ID else bar for bar in bars]}

    assert v.bar_currency(population, moved(5.0))["flag"] == v.BAR_STALE_LOW and v.bar_currency(population, moved(35.0))["flag"] == v.BAR_STALE_HIGH
    small, frozen_small = scored()
    assert v.bar_currency(small, frozen_small)["flag"] is None  # fewer than four rows: no quartiles to compare with
    empty = v.bar_currency({"rows": []}, {"barReferences": []})
    assert empty["flag"] is None and empty["bars"] == [] and empty["currentLadder"] == []


def test_the_report_window_ends_on_the_release_cutoff():
    """E213: one release cutoff; a window ending elsewhere stops the build."""

    routes = {**documents()["planRoutes"], "evidencePolicy": {"reportingWindow": {"start": "2026-09-08", "end": "2026-10-08"}}}
    with pytest.raises(ValueError, match=r"report window must end on the release cutoff 2026-10-19 \(E213\), not 2026-10-08"):
        v.assemble(CONFIGURATIONS, documents(planRoutes=routes), release_day=DAY)


def test_cost_evidence_is_at_most_45_days_old_at_the_cutoff():
    """E216: the AA model-page snapshot and the price records each pass a 45-day age gate at the release cutoff."""

    fresh = {**documents()["snapshot"], "capturedAt": "2026-09-04T00:00:00Z"}
    assert v.assemble(CONFIGURATIONS, documents(snapshot=fresh, priceRecords={"records": [], "observedAt": "2026-09-04T00:00:00Z"}), release_day=DAY)["rows"]
    with pytest.raises(ValueError, match=r"AA model-page snapshot \(2026-09-03\) is more than 45 days old .* \(E216\)"):
        v.assemble(CONFIGURATIONS, documents(snapshot={**fresh, "capturedAt": "2026-09-03T23:00:00Z"}), release_day=DAY)
    with pytest.raises(ValueError, match=r"price records \(2026-08-01\) is more than 45 days old"):
        v.assemble(CONFIGURATIONS, documents(priceRecords={"records": [], "observedAt": "2026-08-01T00:00:00Z"}), release_day=DAY)


def test_the_chart_capture_and_model_pages_describe_one_aa_state():
    """E217: the chart that defines the cohort and the model-page snapshot are at most 7 days apart."""

    pages = {**documents()["snapshot"], "capturedAt": "2026-10-17T19:25:14Z"}
    near = documents(snapshot=pages, frontierCapture={"captured_at": "2026-10-10T19:25:14Z", "points": []})
    assert v.assemble(CONFIGURATIONS, near, release_day=DAY)["rows"]
    far = documents(snapshot=pages, frontierCapture={"captured_at": "2026-10-10T19:25:13Z", "points": []})
    with pytest.raises(ValueError, match=r"more than 7 days apart \(E217\)"):
        v.assemble(CONFIGURATIONS, far, release_day=DAY)


def test_reports_are_searched_within_7_days_of_the_cutoff():
    """E218: the end-user report search reaches to at most 7 days before the release cutoff."""

    def policy(searched):
        window = {"reportingWindow": {"start": "2026-09-19", "end": "2026-10-19"}}
        return {**documents()["planRoutes"], "evidencePolicy": {**window, **({"searchCutoff": searched} if searched else {})}}

    assert v.assemble(CONFIGURATIONS, documents(planRoutes=policy("2026-10-12")), release_day=DAY)["rows"]
    for searched in ("2026-10-11", None):
        with pytest.raises(ValueError, match=r"more than 7 days before the release cutoff 2026-10-19 \(E218\)"):
            v.assemble(CONFIGURATIONS, documents(planRoutes=policy(searched)), release_day=DAY)


def test_observed_range_bars_bound_missing_leaves_by_the_cohort_range():
    """E219: a sensitivity, not evidence: missing leaves inside the cohort's observed range, bar results recomputed."""

    result, frozen = scored()
    ranges = v.leaf_ranges(result)
    assert set(ranges) == {leaf.key for leaf in q.LEAVES} and all(low <= high for low, high in ranges.values())
    unobserved = v.leaf_ranges({"rows": []})
    assert set(unobserved.values()) == {(0.0, 100.0)}
    for row in result["rows"]:
        band = v.band_summary(row["summary"], ranges)
        assert row["summary"].lower - 1e-9 <= band.lower <= band.upper <= row["summary"].upper + 1e-9
    output = v.observed_range_bars(result, frozen)
    assert output["label"] == v.BAND_LABEL and output["status"] == "evaluated" and [bar["bar"] for bar in output["bars"]] == [bar["id"] for bar in frozen["barReferences"]]
    assert v.score(result, frozen)["observedRangeBars"]["bars"] == output["bars"]


def test_required_missing_scores_say_what_would_settle_each_open_row():
    """E221: u* = (100 H - sum of observed w z) / missing weight, for rows that can but need not reach a bar."""

    summary = SimpleNamespace(observations={leaf.key: SimpleNamespace(z=60.0) for leaf in q.LEAVES if leaf.key != "deepswe"})
    assert v.required_missing_score(summary, 50.0) == pytest.approx((5000.0 - 60.0 * 70.0) / 30.0)
    assert v.required_missing_score(SimpleNamespace(observations={leaf.key: None for leaf in q.LEAVES}), 50.0) is None
    result, frozen = scored()
    output = v.required_missing_scores(result, frozen)
    assert output["label"] == v.REQUIRED_LABEL and output["status"] == "evaluated" and [bar["bar"] for bar in output["bars"]] == [bar["id"] for bar in frozen["barReferences"]]
    assert v.score(result, frozen)["requiredMissingScores"] == output


def test_the_quartile_bars_need_four_configurations():
    """E215: with fewer than four, the quartile positions coincide with the headline's, so only the headline is pinned."""

    def ladder(n):
        return [bar["id"] for bar in v.bar_levels({"rows": [{"id": f"r{i}", "summary": SimpleNamespace(displayed=float(i), provisional=False)} for i in range(n)]})[1]]

    assert ladder(1) == [] and ladder(3) == [v.BAR_ID] and ladder(4) == [item[0] for item in v.BAR_LADDER]


def test_routes_inherit_their_sources_workload_mix():
    """E208: a route's token-mix status uses the category shares its source publishes; never AA's Index-wide shares."""

    routes = documents()["planRoutes"]
    sourced = {**routes, "sourceEvidence": {"lab": {"workloadMix": {"outputPct": 0.3}}},
               "routes": [dict(routes["routes"][0], sourceEvidenceId="lab"), routes["routes"][1]]}
    rows = {row["id"]: row for row in v.assemble(CONFIGURATIONS, documents(planRoutes=sourced), release_day=DAY)["rows"]}
    statuses = {row_id: [item["mixCheck"] for item in rows[row_id]["routeCandidates"]] for row_id in ("a", "b")}
    assert statuses == {"a": [pr.MIX_UNIDENTIFIED], "b": [pr.MIX_NOT_REPORTED]}
