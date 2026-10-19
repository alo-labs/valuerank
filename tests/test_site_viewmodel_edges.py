"""Edge branches of the v3 site view models, driven by small mutations of a copied data directory."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from valuerank.paths import DATA
from valuerank.site import viewmodel


@pytest.fixture
def data(tmp_path) -> Path:
    destination = tmp_path / "data"
    destination.mkdir()
    for source in DATA.glob("*.json"):
        shutil.copy2(source, destination / source.name)
    return destination


def edit(data: Path, name: str, change) -> None:
    path = data / name
    document = json.loads(path.read_text())
    change(document)
    path.write_text(json.dumps(document))


def v3_row(scores, model_id):
    return next(row for row in scores["v3"]["rows"] if row["id"] == model_id)


def test_duplicate_slugs_and_an_empty_ranked_cohort_are_refused(data):
    edit(data, "scores.json", lambda scores: scores["models"].append(dict(scores["models"][0], id=scores["models"][0]["id"].replace("-", "."))))
    with pytest.raises(ValueError, match="duplicate model slug"):
        viewmodel.build_bundle(data)


def test_no_ranked_rows_is_refused(data):
    edit(data, "scores.json", lambda scores: scores["v3"].__setitem__("rows", []))
    with pytest.raises(ValueError, match="no ranked models"):
        viewmodel.build_bundle(data)


def test_stale_scenarios_leave_shares_empty_and_documents_report_the_status(data):
    edit(data, "scores.json", lambda scores: scores["v3"].__setitem__("scenarios", {"status": "stale (inputs changed since the scenario run)"}))
    bundle = viewmodel.build_bundle(data)
    sol = next(m for m in bundle.rankings["models"] if m["slug"] == "gpt-6-1-sol")
    assert sol["scenario"] == {"api": None, "plan": None}
    assert bundle.models["gpt-6-1-sol"]["scenarios"] == {"status": "stale (inputs changed since the scenario run)", "api": [], "plan": []}
    assert bundle.extras["method"]["streamDescriptions"] == {} and bundle.extras["method"]["notQuantified"] == []


def test_an_empty_bar_population_names_no_reference(data):
    edit(data, "scores.json", lambda scores: scores["v3"]["barPolicy"].__setitem__("referenceIds", []))
    assert viewmodel.build_bundle(data).extras["method"]["barReference"] is None


def test_a_row_without_observed_leaves_grades_as_missing_and_saturated_leaves_carry_a_note(data):
    def change(scores):
        row = v3_row(scores, "gpt-6.1-sol")
        row["quality"]["leaves"] = {}
        row["quality"]["clipAudit"] = []
        other = v3_row(scores, "gpt-6-luna")
        other["quality"]["clipAudit"][0]["anchorPosition"] = "at or above the upper anchor"
        other["quality"]["leaves"][other["quality"]["clipAudit"][0]["leaf"]].pop("configuration", None)
    edit(data, "scores.json", change)
    bundle = viewmodel.build_bundle(data)
    sol = next(m for m in bundle.rankings["models"] if m["slug"] == "gpt-6-1-sol")
    assert sol["grade"] == "missing" and all(value is None for key, value in sol["dims"].items())
    assert all(leaf["grade"] == "missing" and leaf["source"] is None for leaf in bundle.models["gpt-6-1-sol"]["dimensions"])
    saturated = [leaf for leaf in bundle.models["gpt-6-luna"]["dimensions"] if leaf["note"]]
    assert len(saturated) == 1 and saturated[0]["note"] == "Saturates the scoring anchor (at or above the upper anchor)."


def test_route_costs_need_an_api_cost_and_a_positive_multiple(data):
    def change(routes):
        for route in routes["routes"]:
            if route["id"] == "chatgpt-plus-common-semianalysis-assumption":
                route["valueMultiple"] = 0.0
    edit(data, "plan_cost_routes.json", change)
    edit(data, "scores.json", lambda scores: v3_row(scores, "gpt-6-luna")["api"].__setitem__("costUsd", None))
    bundle = viewmodel.build_bundle(data)
    plus = next(plan for plan in bundle.models["gpt-6-1-sol"]["plans"] if plan["id"] == "chatgpt-plus-common-semianalysis-assumption")
    assert plus["usdPerRun"] is None
    assert all(plan["usdPerRun"] is None for plan in bundle.models["gpt-6-luna"]["plans"])


def test_the_plans_worked_example_needs_routed_models(data):
    bundle = viewmodel.build_bundle(data)
    bundle.plans["workedExample"]["slugs"] = ["glm-5-3"]
    with pytest.raises(ValueError, match="glm-5-3 has no plan route"):
        viewmodel.plans_page(bundle)


def test_terminal_bench_mapping_marks_models_without_rows_or_claims_missing(data):
    def change(tb4):
        tb4["rows"] = [r for r in tb4["rows"] if r.get("cohortModelId") != "claude-opus-5"]
        tb4["cohortRows"].pop("claude-opus-5")
    edit(data, "tb4.json", change)
    bundle = viewmodel.build_bundle(data)
    assert bundle.tb4["cohortMapping"]["claude-opus-5"] == {"status": "missing", "rank": None, "resolutionRatePct": None, "evaluatedModel": None}


def test_history_with_an_empty_version_is_summarised_as_no_model(data):
    edit(data, "ranking_history_v1.5.json", lambda h: h.__setitem__("v192", {}))
    bundle = viewmodel.build_bundle(data)
    entry = next(v for v in bundle.changelog["versions"] if v["version"] == "v1.9.2")
    assert entry["models"] == 0 and entry["summary"].startswith("No model")


def test_a_plan_exploratory_label_only_when_the_identification_yield_says_so(data):
    edit(data, "scores.json", lambda scores: scores["v3"]["identificationYield"].__setitem__("exploratory", False))
    bundle = viewmodel.build_bundle(data)
    page = viewmodel.methodology_page(bundle)
    assert bundle.rankings["planExploratory"] is False and not any(item.startswith("Subscription Value Multiples") for item in page["limitations"])
