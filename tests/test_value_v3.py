"""Tests for the v3 integration: evidence, admission, anchors, scores, intervals, scenarios and the CLI."""

from __future__ import annotations

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
from valuerank import quality as q
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
            {"id": "plan-a", "valueMultiple": 10.0, "valueMultipleKind": "controlled_account_workload_projection", "modelIds": ["a"], "planPriceUsd": 20, "checkedOn": "2026-10-10"},
            {"id": "plan-b", "valueMultiple": 2.0, "valueMultipleKind": "controlled_account_workload_projection", "modelIds": ["b"], "planPriceUsd": 20, "checkedOn": "2026-10-10",
             "identification": "point-identified", "valuationBasis": "release"},
        ]},
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
    assert frozen["barReferences"][0]["id"] in {"a", "b"}
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
    tight["barReferences"] = [{"id": "gone", "rule": "x"}]
    output = v.score(result, tight)
    manifest = {item["rule"]: item["status"] for item in output["manifest"]}
    assert output["gates"]["hold"] is True and manifest["clip gate (E20)"] == "fired"
    assert output["intervals"]["api"]["bars"][0]["status"] == "unevaluable"
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


def test_freeze_without_definite_members_pins_no_bar():
    result = assembled()
    for item in result["rows"]:
        item["cost"] = dict(item["cost"], fullCost=False)
    frozen = v.freeze(result, frozen_at="d")
    assert frozen["barReferences"] == [] and frozen["barPolicy"]["referenceIds"] == [] and frozen["barPolicy"]["population"] == []


def test_bar_reference_selection_is_registered_and_outcome_independent(monkeypatch):
    """E156: input order cannot change the reference; bar outcomes are never computed at selection; provisional rows are excluded."""

    result = assembled()
    frozen = v.freeze(result, frozen_at="2026-10-19")
    policy = frozen["barPolicy"]
    assert policy["policyId"] == "median-definite-frontier" and policy["selectionCutoff"] == "2026-10-19"
    assert policy["referenceIds"] == [item["id"] for item in frozen["barReferences"]]
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
    outside = dict(frozen, barReferences=[{"id": "c", "rule": "x"}])
    assert v.bar_labels(result, outside, seed=1, batch=50)[0]["status"] == "unevaluable"


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
        "plan_cost_routes.json": documents()["planRoutes"],
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


def test_module_entry_point(tmp_path, monkeypatch):
    data = write_world(tmp_path)
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
    assert len(branches) == len(q.LEAVES) + 1
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
    assert measured["b"].leaves["terminalBench"].params == pytest.approx((95.9, 100.0))
    assert measured["a"].leaves["deepswe"] == plain["a"].leaves["deepswe"]
    document = v.run_scenarios(result, frozen, n=50, seed=3)
    s1m = document["results"]["api"][-1]
    assert s1m["stratum"] == "S1M" and s1m["variedTargets"] == ["identification convention", "published-interval range (conventional)", "reporting precision"]
    interpretation = document["intervalInterpretation"]["S1M"][0]
    assert interpretation["leaf"] == "terminalBench" and interpretation["kernelStatus"] == "conventional-within-CI"
    assert interpretation["permittedLabel"] == "conventional CI-range sensitivity (endpoint-conditioned; no tail model)"


def calibration_row(row_id, workload, quality, *, partial=(), fallback=None, grade="controlled"):
    return {
        "id": row_id,
        "cost": {"workload": workload, "partialComponents": list(partial)},
        "plan": {"fallback": fallback, "grade": grade},
        "summary": SimpleNamespace(displayed=quality),
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


def test_measured_calibration_without_references_and_unknown_anchor_rows():
    official = anchor_math.anchor_object({"retired": 5.0, "x": 10.0}, basis="plan", workload="w1")
    frozen = {"workloads": {"w1": {"anchors": {"plan": official}}}}
    entries = {"x": {"status": "measured, target-workload unmatched", "costUsd": 10.0, "costScore": 50.0, "value": 55.0}}
    result = v._measured_calibration([calibration_row("x", "w1", 60.0)], frozen, entries)
    assert result["status"] == "measured-evidence calibration unavailable"
    assert result["workloads"]["w1"]["officialAnchorProvenance"]["low"] == {"row": "retired", "evidence": "not in the current table"}
    assert result["values"] == {} and result["reversals"] == [] and result["maxAbsValueChange"] is None
    assert v._plan_evidence(calibration_row("r", "w1", 1.0, grade="reports")) == "concordant reports"
