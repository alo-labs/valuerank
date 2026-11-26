"""Behaviour tests for the subscription-route cost resolver in valuerank.plan_costs."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

from valuerank import plan_costs
from valuerank.paths import DATA


def make_route(**fields):
    """A minimal valid route; keyword arguments override or add fields."""

    route = {"id": "route-a", "modelIds": ["model-1"], "valueMultiple": 2, "confidence": "medium"}
    route.update(fields)
    return route


def make_document(*routes, **extra):
    return {"routes": list(routes), **extra}


def make_model(model_id, api_cost, variant=None, index=50):
    model = {"id": model_id, "aaEvalCost": api_cost, "intelligenceIndex": index}
    if variant is not None:
        model["aaVariant"] = variant
    return model


def write_json(path: Path, document) -> Path:
    path.write_text(json.dumps(document))
    return path


# --- load_plan_routes -------------------------------------------------------


def test_load_plan_routes_returns_the_committed_route_document(repo_copy):
    path = repo_copy / "data" / "plan_cost_routes.json"

    document = plan_costs.load_plan_routes(path)

    assert document == json.loads(path.read_text())
    assert document["routes"], "the committed document must carry at least one route"


def test_default_path_points_at_the_committed_route_file():
    assert plan_costs.DEFAULT_ROUTE_PATH == DATA / "plan_cost_routes.json"
    assert plan_costs.load_plan_routes() == json.loads((DATA / "plan_cost_routes.json").read_text())


@pytest.mark.parametrize(
    "document",
    [{}, {"routes": None}, {"routes": "route-a"}, {"routes": {"id": "route-a"}}],
    ids=["missing", "null", "string", "object"],
)
def test_load_plan_routes_rejects_a_document_without_a_routes_list(tmp_path, document):
    path = write_json(tmp_path / "routes.json", document)

    with pytest.raises(ValueError, match="plan route document must contain a routes list"):
        plan_costs.load_plan_routes(path)


INVALID_ROUTES = [
    pytest.param({"modelIds": ["m1"], "valueMultiple": 2}, "<missing id>", id="missing-id"),
    pytest.param({"id": "r1", "valueMultiple": 2}, "r1", id="missing-model-ids"),
    pytest.param({"id": "r1", "modelIds": [], "valueMultiple": 2}, "r1", id="empty-model-ids"),
    pytest.param({"id": "r1", "modelIds": ["m1"]}, "r1", id="missing-multiple"),
    pytest.param({"id": "r1", "modelIds": ["m1"], "valueMultiple": "2"}, "r1", id="string-multiple"),
    pytest.param({"id": "r1", "modelIds": ["m1"], "valueMultiple": None}, "r1", id="null-multiple"),
    pytest.param({"id": "r1", "modelIds": ["m1"], "valueMultiple": 0}, "r1", id="zero-multiple"),
    pytest.param({"id": "r1", "modelIds": ["m1"], "valueMultiple": -1.5}, "r1", id="negative-multiple"),
]


@pytest.mark.parametrize(("bad_route", "label"), INVALID_ROUTES)
def test_load_plan_routes_names_the_invalid_route_it_rejects(tmp_path, bad_route, label):
    path = write_json(tmp_path / "routes.json", make_document(make_route(id="valid-first"), bad_route))

    with pytest.raises(ValueError, match=re.escape(f"invalid plan route: {label}")):
        plan_costs.load_plan_routes(path)


@pytest.mark.parametrize("multiple", [0.5, 1, 12.75])
def test_load_plan_routes_accepts_any_positive_numeric_multiple(tmp_path, multiple):
    path = write_json(tmp_path / "routes.json", make_document(make_route(valueMultiple=multiple)))

    assert plan_costs.load_plan_routes(path)["routes"][0]["valueMultiple"] == multiple


# --- select_best_route ------------------------------------------------------


def test_select_best_route_ignores_routes_for_other_models():
    document = make_document(make_route(id="other", modelIds=["m2"], valueMultiple=99))

    assert plan_costs.select_best_route("m1", document) is None


def test_select_best_route_returns_none_for_an_empty_document():
    assert plan_costs.select_best_route("m1", make_document()) is None


def test_variant_restricted_route_is_chosen_only_for_its_exact_variant():
    document = make_document(
        make_route(id="general", valueMultiple=2),
        make_route(id="xhigh-only", valueMultiple=10, requiredVariant="xhigh"),
    )

    assert plan_costs.select_best_route("model-1", document, "xhigh")["id"] == "xhigh-only"
    assert plan_costs.select_best_route("model-1", document, "high")["id"] == "general"
    assert plan_costs.select_best_route("model-1", document, None)["id"] == "general"


def test_variant_restricted_route_alone_is_ineligible_without_an_exact_match():
    document = make_document(make_route(id="xhigh-only", requiredVariant="xhigh"))

    assert plan_costs.select_best_route("model-1", document, "xhigh")["id"] == "xhigh-only"
    assert plan_costs.select_best_route("model-1", document, "high") is None
    assert plan_costs.select_best_route("model-1", document) is None


def test_explicit_null_required_variant_means_the_route_is_unrestricted():
    document = make_document(make_route(id="any", requiredVariant=None))

    assert plan_costs.select_best_route("model-1", document, "xhigh")["id"] == "any"
    assert plan_costs.select_best_route("model-1", document, None)["id"] == "any"


def test_highest_value_multiple_wins():
    document = make_document(
        make_route(id="a-cheap-claim", valueMultiple=2),
        make_route(id="z-generous-claim", valueMultiple=3.5),
    )

    assert plan_costs.select_best_route("model-1", document)["id"] == "z-generous-claim"


@pytest.mark.parametrize(
    ("stronger", "weaker"),
    [("high", "medium-high"), ("medium-high", "medium"), ("medium", "low-medium"), ("low-medium", "low")],
)
def test_confidence_orders_routes_with_equal_multiples(stronger, weaker):
    # The weaker route is listed first and wins the id tie-break, so only confidence can pick the stronger one.
    document = make_document(
        make_route(id="z-weaker", valueMultiple=4, confidence=weaker),
        make_route(id="a-stronger", valueMultiple=4, confidence=stronger),
    )

    assert plan_costs.select_best_route("model-1", document)["id"] == "a-stronger"


def test_unknown_confidence_ranks_below_every_known_level():
    document = make_document(
        make_route(id="z-unknown-label", valueMultiple=4, confidence="verified-by-vibes"),
        make_route(id="a-low", valueMultiple=4, confidence="low"),
    )

    assert plan_costs.select_best_route("model-1", document)["id"] == "a-low"


def test_missing_confidence_is_treated_as_low():
    document = make_document(
        make_route(id="z-unknown-label", valueMultiple=4, confidence="verified-by-vibes"),
        {"id": "a-missing", "modelIds": ["model-1"], "valueMultiple": 4},
    )

    assert plan_costs.select_best_route("model-1", document)["id"] == "a-missing"


def test_missing_confidence_ties_with_explicit_low_and_then_id_decides():
    document = make_document(
        {"id": "a-missing", "modelIds": ["model-1"], "valueMultiple": 4},
        make_route(id="z-explicit-low", valueMultiple=4, confidence="low"),
    )

    assert plan_costs.select_best_route("model-1", document)["id"] == "z-explicit-low"


def test_route_id_breaks_remaining_ties_regardless_of_list_order():
    first = make_route(id="route-a", valueMultiple=3, confidence="medium")
    second = make_route(id="route-b", valueMultiple=3, confidence="medium")

    assert plan_costs.select_best_route("model-1", make_document(first, second))["id"] == "route-b"
    assert plan_costs.select_best_route("model-1", make_document(second, first))["id"] == "route-b"


# --- opencode_go_tiers ------------------------------------------------------


def test_opencode_go_tiers_keeps_only_opencode_go_routes_sorted_by_usage():
    document = make_document(
        {"id": "go-20", "provider": "OpenCode", "plan": "Go", "usageUsd": 20},
        {"id": "go-5", "provider": "OpenCode", "plan": "Go", "usageUsd": 5},
        {"id": "pro-1", "provider": "OpenCode", "plan": "Pro", "usageUsd": 1},
        {"id": "other-go", "provider": "Other", "plan": "Go", "usageUsd": 0.5},
        {"id": "go-10", "provider": "OpenCode", "plan": "Go", "usageUsd": 10},
    )

    assert [route["id"] for route in plan_costs.opencode_go_tiers(document)] == ["go-5", "go-10", "go-20"]


def test_opencode_go_tiers_is_empty_when_no_route_matches():
    assert plan_costs.opencode_go_tiers(make_document()) == []
    assert plan_costs.opencode_go_tiers(make_document(make_route())) == []


# --- effective_cost ---------------------------------------------------------


def test_effective_cost_divides_the_api_cost_by_the_route_multiple():
    cost = plan_costs.effective_cost(100, make_route(valueMultiple=4))

    assert cost == 25.0
    assert isinstance(cost, float)


def test_effective_cost_keeps_a_zero_api_cost_as_a_real_value():
    assert plan_costs.effective_cost(0, make_route(valueMultiple=4)) == 0.0


@pytest.mark.parametrize(
    ("api_cost", "route"),
    [(None, make_route()), (100, None), (None, None)],
    ids=["missing-api-cost", "missing-route", "both-missing"],
)
def test_effective_cost_is_unknown_without_both_inputs(api_cost, route):
    assert plan_costs.effective_cost(api_cost, route) is None


@pytest.mark.parametrize(
    "route",
    [{"id": "no-multiple"}, make_route(valueMultiple="2"), make_route(valueMultiple=0), make_route(valueMultiple=-3)],
    ids=["missing", "string", "zero", "negative"],
)
def test_effective_cost_rejects_an_invalid_multiple(route):
    assert plan_costs.effective_cost(100, route) is None


# --- cost_scores --------------------------------------------------------------


def test_cost_scores_of_nothing_known_is_all_none():
    assert plan_costs.cost_scores([None, None]) == [None, None]
    assert plan_costs.cost_scores([]) == []


def test_a_single_known_cost_gets_a_neutral_score_and_gaps_are_kept():
    assert plan_costs.cost_scores([None, 7, None]) == [None, 50.0, None]


def test_identical_costs_all_score_the_midpoint():
    assert plan_costs.cost_scores([5, 5.0, 5]) == [50.0, 50.0, 50.0]


def test_cheapest_scores_100_and_dearest_0():
    assert plan_costs.cost_scores([1, 100, None]) == [100.0, 0.0, None]


def test_cost_scores_keep_ratios_on_a_log_scale():
    # 10 is ten times 1 and 100 ten times 10, so it sits exactly halfway.
    assert plan_costs.cost_scores([1, 10, 100]) == [100.0, 50.0, 0.0]
    # A tiny gap is a tiny penalty, unlike a rank where any gap is a full step.
    assert plan_costs.cost_scores([1, 1.01, 100]) == [100.0, 99.8, 0.0]


def test_cost_scores_round_to_one_decimal_like_the_score_dimensions():
    # scores.json stores every dimension at one decimal; the cost score must match it exactly
    # so that recomputing the composite from the public data reproduces the committed score.
    assert plan_costs.cost_scores([1, 2, 3]) == [100.0, 36.9, 0.0]


@pytest.mark.parametrize("bad", [0, -1])
def test_cost_scores_reject_non_positive_costs(bad):
    with pytest.raises(ValueError, match="positive costs"):
        plan_costs.cost_scores([1, bad])


# --- blend -------------------------------------------------------------------


def test_cost_carries_a_fixed_quarter_of_the_overall_score():
    assert plan_costs.COST_WEIGHT_PCT == 25.0
    assert plan_costs.blend(100, 60) == 70.0
    assert plan_costs.blend(0, 80) == 60.0


def test_blend_accepts_another_cost_weight():
    assert plan_costs.blend(100, 60, 50) == 80.0
    assert plan_costs.blend(100, 60, 0) == 60.0
    assert plan_costs.blend(100, 60, 100) == 100.0


def test_without_quality_or_without_cost_there_is_no_overall_score():
    # AGENTS.md: a configuration without a cost gets no value score; neither gap is filled in.
    assert plan_costs.blend(90, None) is None
    assert plan_costs.blend(None, 61.25) is None
    assert plan_costs.blend(None, None) is None


# --- cost_per_index_point ---------------------------------------------------


def test_cost_per_index_point_divides_cost_by_the_intelligence_index():
    assert plan_costs.cost_per_index_point(147.85, 57.62) == pytest.approx(147.85 / 57.62)
    assert plan_costs.cost_per_index_point(0, 52) == 0.0


@pytest.mark.parametrize("cost, index", [(None, 52), (100, None), (100, 0), (100, -3), (100, "52")])
def test_cost_per_index_point_is_unknown_without_a_positive_numeric_index_and_a_cost(cost, index):
    assert plan_costs.cost_per_index_point(cost, index) is None


# --- build_cost_fields ------------------------------------------------------


def test_build_cost_fields_of_no_models_is_empty():
    assert plan_costs.build_cost_fields([], make_document()) == []


def test_an_eligible_route_prices_the_plan_in_usd_per_index_point():
    route = make_route(id="route-a", modelIds=["model-1"], valueMultiple=4)

    [field] = plan_costs.build_cost_fields([make_model("model-1", 100, index=50)], make_document(route))

    assert field == {
        "apiCost": 100,
        "apiCostPerPoint": 2.0,
        "intelligenceIndex": 50,
        "planCostPerRun": 25.0,
        "planCost": 0.5,
        "planComparableCost": 0.5,
        "apiCostScore": 50.0,
        "planCostScore": 50.0,
        "planRoute": route,
        "planCostFallback": None,
    }


def test_a_model_without_a_route_falls_back_to_api_cost_per_index_point():
    route = make_route(id="route-a", modelIds=["model-1"], valueMultiple=4)

    covered, uncovered = plan_costs.build_cost_fields(
        [make_model("model-1", 100, index=50), make_model("model-2", 40, index=40)], make_document(route)
    )

    assert uncovered["planRoute"] is None
    assert uncovered["planCostPerRun"] is None
    assert uncovered["planCost"] is None
    assert uncovered["planCostFallback"] == "api"
    assert uncovered["planComparableCost"] == 1.0
    assert covered["planCostFallback"] is None


def test_token_efficiency_offsets_a_larger_allowance():
    # Opus 5.5 on Claude Pro (58.9x) against GPT-6.1 Sol on ChatGPT Pro $500 (10.772x):
    # the 5.5x larger allowance is more than consumed by the 8x larger Index run cost.
    claude = make_route(id="claude-pro", modelIds=["opus"], valueMultiple=58.9)
    openai = make_route(id="chatgpt-pro-500", modelIds=["sol"], valueMultiple=10.772)

    opus, sol = plan_costs.build_cost_fields(
        [make_model("opus", 8708.20, index=57.62), make_model("sol", 1081.55, index=52.0)],
        make_document(claude, openai),
    )

    assert opus["planCostPerRun"] == pytest.approx(147.85, abs=0.01)
    assert sol["planCostPerRun"] == pytest.approx(100.40, abs=0.01)
    assert opus["planCost"] == pytest.approx(2.566, abs=0.001)
    assert sol["planCost"] == pytest.approx(1.931, abs=0.001)
    assert (sol["planCostScore"], opus["planCostScore"]) == (100.0, 0.0)
    assert (sol["apiCostScore"], opus["apiCostScore"]) == (100.0, 0.0)


def test_plan_ranking_can_reverse_the_api_ranking_once_a_route_divides_the_cost():
    route = make_route(id="route-a", modelIds=["model-1"], valueMultiple=4)

    covered, uncovered = plan_costs.build_cost_fields(
        [make_model("model-1", 100, index=50), make_model("model-2", 40, index=50)], make_document(route)
    )

    # On API cost model-2 is cheaper; after dividing model-1 by 4 it is 0.5 against 0.8 per point.
    assert (covered["apiCostScore"], covered["planCostScore"]) == (0.0, 100.0)
    assert (uncovered["apiCostScore"], uncovered["planCostScore"]) == (100.0, 0.0)


def test_a_missing_api_cost_leaves_plan_fields_empty_but_keeps_the_route():
    route = make_route(id="route-a", modelIds=["model-1"], valueMultiple=4)

    covered, other = plan_costs.build_cost_fields(
        [make_model("model-1", None, index=50), make_model("model-2", 40, index=50)], make_document(route)
    )

    assert covered["planRoute"] == route
    assert covered["planCostPerRun"] is None
    assert covered["planCost"] is None
    assert covered["planComparableCost"] is None
    assert covered["apiCostScore"] is None
    assert covered["planCostScore"] is None
    assert covered["planCostFallback"] is None
    assert other["planComparableCost"] == 0.8
    assert other["planCostScore"] == 50.0


def test_a_missing_intelligence_index_keeps_the_run_cost_but_cannot_be_ranked_per_point():
    route = make_route(id="route-a", modelIds=["model-1"], valueMultiple=4)

    [field] = plan_costs.build_cost_fields([make_model("model-1", 100, index=None)], make_document(route))

    assert field["planCostPerRun"] == 25.0
    assert field["intelligenceIndex"] is None
    assert field["planCost"] is None
    assert field["planComparableCost"] is None
    assert field["planCostScore"] is None
    # The API basis also compares cost per Index point, so it cannot be scored either.
    assert field["apiCostPerPoint"] is None
    assert field["apiCostScore"] is None


def test_a_missing_api_cost_without_a_route_has_no_comparable_cost():
    [field] = plan_costs.build_cost_fields([make_model("model-1", None, index=50)], make_document())

    assert field["planComparableCost"] is None
    assert field["planCostScore"] is None
    assert field["planCostFallback"] == "api"


def test_route_summary_counts_supported_and_fallback_models():
    route_a = make_route(id="route-a")
    route_b = make_route(id="route-b")
    document = make_document(route_a, route_b, asOf="2026-10-08", costMix={"id": "mix-1"})
    fields = [{"planRoute": route_a}, {"planRoute": None}, {"planRoute": route_b}]

    assert plan_costs.route_summary(document, fields) == {
        "asOf": "2026-10-08",
        "routeCount": 2,
        "supportedModelCount": 2,
        "fallbackModelCount": 1,
        "mixId": "mix-1",
    }


def test_route_summary_tolerates_missing_metadata():
    assert plan_costs.route_summary(make_document(), []) == {
        "asOf": None,
        "routeCount": 0,
        "supportedModelCount": 0,
        "fallbackModelCount": 0,
        "mixId": None,
    }


def test_summary_of_the_committed_routes_accounts_for_every_model(repo_copy):
    document = plan_costs.load_plan_routes(repo_copy / "data" / "plan_cost_routes.json")
    covered_ids = sorted({model_id for route in document["routes"] for model_id in route["modelIds"]})
    unrestricted_ids = {
        model_id
        for route in document["routes"]
        if route.get("requiredVariant") is None
        for model_id in route["modelIds"]
    }
    models = [make_model(model_id, 100.0) for model_id in covered_ids] + [make_model("not-in-any-route", 5.0)]

    fields = plan_costs.build_cost_fields(models, document)
    summary = plan_costs.route_summary(document, fields)

    assert summary["routeCount"] == len(document["routes"])
    assert summary["asOf"] == document["asOf"]
    assert summary["mixId"] == document["costMix"]["id"]
    assert summary["supportedModelCount"] + summary["fallbackModelCount"] == len(models)
    assert summary["fallbackModelCount"] >= 1
    for model, field in zip(models, fields):
        if model["id"] in unrestricted_ids:
            assert field["planRoute"] is not None, model["id"]
        if field["planRoute"] is None:
            assert field["planCostFallback"] == "api", model["id"]


def test_api_basis_compares_cost_per_index_point_not_run_cost():
    # The cheaper run buys too little intelligence: per point it is the dearer model.
    cheap, strong = plan_costs.build_cost_fields(
        [make_model("cheap", 100, index=10), make_model("strong", 300, index=60)], make_document()
    )
    assert (cheap["apiCostPerPoint"], strong["apiCostPerPoint"]) == (10.0, 5.0)
    assert (cheap["apiCostScore"], strong["apiCostScore"]) == (0.0, 100.0)


# --- owner-authorised Claude shared-plan assumption (2026-10-18) -------------


def test_every_claude_model_resolves_to_a_claude_plan_route_at_opus_55_multiples(repo_copy):
    # Owner decision 2026-10-18 (Option 2): Opus 5.5's measured SemiAnalysis multiples apply to every
    # Claude model as a labelled assumption; Opus 5.5 itself keeps its exact measured routes, and so does
    # Fable 5.1 (SemiAnalysis measured it on Max 5x and Max 20x; it is not offered on Pro).
    routes = plan_costs.load_plan_routes(repo_copy / "data" / "plan_cost_routes.json")
    mapping = json.loads((repo_copy / "data" / "aa_mapping.json").read_text(encoding="utf-8"))
    claude_ids = [entry["id"] for entry in mapping if entry["id"].startswith("claude-")]
    assert "claude-haiku-5-5-high" in claude_ids and "claude-sonnet-5-5" in claude_ids and "claude-opus-5-5" in claude_ids
    opus = plan_costs.select_best_route("claude-opus-5-5", routes)
    assert opus["provider"] == "Anthropic" and opus["evidenceClass"] == "controlled_account_workload_projection"
    for model_id in claude_ids:
        route = plan_costs.select_best_route(model_id, routes)
        assert route is not None, model_id
        assert route["provider"] == "Anthropic"
        if model_id == "claude-fable-5-1":
            continue
        assert route["valueMultiple"] == opus["valueMultiple"] and route["plan"] == opus["plan"]
        if model_id != "claude-opus-5-5":
            assert route["evidenceClass"] == "user_assumption" and route["sourceModel"] == "Opus 5.5"
            assert "2026-10-18" in route["notes"]


def test_fable_5_1_keeps_its_own_measured_max_routes_and_has_no_pro_route(repo_copy):
    routes = plan_costs.load_plan_routes(repo_copy / "data" / "plan_cost_routes.json")
    fable = [route for route in routes["routes"] if "claude-fable-5-1" in route["modelIds"]]
    assert sorted((route["plan"], route["valueMultiple"]) for route in fable) == [("Claude Max 20x", 12.425), ("Claude Max 5x", 12.73)]
    for route in fable:
        assert route["evidenceClass"] == "controlled_account_workload_projection" and route["sourceModel"] == "Fable 5.1"
        assert "semianalysis" in route["id"]
    assert not any("claude-fable-5-1" in route["modelIds"] for route in routes["routes"] if route["evidenceClass"] == "user_assumption")
    best = plan_costs.select_best_route("claude-fable-5-1", routes)
    assert (best["plan"], best["valueMultiple"]) == ("Claude Max 5x", 12.73)
