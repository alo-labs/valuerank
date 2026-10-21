"""Pure-function tests for the site view-model helpers (grades, picks, changelog, v3 entry helpers)."""

from __future__ import annotations

import pytest

from valuerank.site import changelog, evidence, picks, viewmodel


@pytest.mark.parametrize(
    ("evidence_class", "expected"),
    [
        ("controlled_account_workload_projection", "measured"),
        ("user_reported_projection", "estimate"),
        ("user_assumption", "assumption"),
        ("something_new", "assumption"),
    ],
)
def test_route_grade_maps_evidence_class(evidence_class, expected):
    assert evidence.route_grade(evidence_class) == expected


def test_slugify_replaces_dots_with_hyphens():
    assert viewmodel.slugify("gpt-6.1-sol") == "gpt-6-1-sol"
    assert viewmodel.slugify("kimi-k3") == "kimi-k3"


def test_competition_ranks_share_the_better_rank_and_skip_missing_values():
    assert viewmodel.competition_ranks({"a": 10.0, "b": 10.0, "c": 50.0, "d": None}) == {"c": 1, "a": 2, "b": 2}
    assert viewmodel.competition_ranks({}) == {}


def test_cost_tiers_follow_the_cost_score():
    assert viewmodel._tier(None) is None
    assert [viewmodel._tier(score) for score in (90.0, 80.0, 70.0, 50.0, 30.0)] == ["Budget", "Near-Budget", "Mid-Range", "Premium", "Expensive"]


def test_dimensions_give_cost_a_fixed_share_and_split_the_rest_by_leaf_weight():
    rows = viewmodel.dimensions()
    assert rows[0]["key"] == viewmodel.COST_KEY and rows[0]["weightPct"] == 25.0 and rows[0]["category"] == "cost"
    leaves = rows[1:]
    assert len(leaves) == 11 and sum(row["weightPct"] for row in leaves) == pytest.approx(75.0)
    deepswe = next(row for row in leaves if row["key"] == "deepswe")
    assert deepswe["weightPct"] == 22.5 and deepswe["priority"] == 30.0 and deepswe["category"] == "code"
    assert {row["category"] for row in leaves} == {"code", "prod", "rely", "intel"}


def test_route_view_grades_selected_routes_by_engine_grade_and_others_by_class():
    route = {"id": "r", "planLabel": "Pro", "planPriceUsd": 20, "valueMultiple": 8.0, "evidenceClass": "user_assumption", "sourceModel": "M",
             "sourceUrl": "https://example.test", "sourcePublicationDate": "2026-10-06", "valueMultipleKind": "user_assumption"}
    assert viewmodel._route_view(None) is None
    assert viewmodel._route_view(route)["grade"] == "assumption"
    assert viewmodel._route_view(route, "controlled")["grade"] == "measured"
    assert viewmodel._route_view(route, "reports")["grade"] == "estimate"
    assert viewmodel._route_view(route)["planFeeUsd"] == 20 and viewmodel._route_view(route)["sourceDate"] == "2026-10-06"


def _v3_row(row_id, cost, quality, *, workload="w", plan_cost=None, subset=False, provisional=False, partial=(), caveat=None):
    return {
        "id": row_id,
        "cost": {"subset": subset, "partialComponents": list(partial), "workload": workload},
        "quality": {"displayed": quality, "provisional": provisional, "provisionalReasons": ["coverage 40% below 70%"] if provisional else []},
        "api": {"costUsd": cost},
        "planScore": {"costUsd": plan_cost if plan_cost is not None else cost},
        "aaCostCaveat": caveat,
    }


def test_row_flags_name_subset_provisional_partial_and_caveat_in_order():
    assert viewmodel._row_flags(_v3_row("a", 1.0, 50.0)) == []
    flags = viewmodel._row_flags(_v3_row("a", 1.0, 50.0, subset=True, provisional=True, partial=["x"], caveat="long-context pricing"))
    assert [flag.split(":")[0] for flag in flags] == ["Subset cost", "Provisional quality", "Partial cost component", "AA cost caveat"]
    # A row without a cost says so instead of claiming a subset workload (AGENTS.md: no cost, no value score).
    assert viewmodel._row_flags(_v3_row("a", None, 50.0, subset=True))[0].startswith("No cost: AA publishes no cost")


def test_pareto_set_uses_point_estimates_on_the_main_workload_only():
    rows = [
        _v3_row("cheap", 10.0, 40.0), _v3_row("good", 100.0, 80.0), _v3_row("dominated", 100.0, 60.0),
        _v3_row("tie", 10.0, 40.0), _v3_row("subset", 1.0, 99.0, workload="other"), _v3_row("nocost", None, 99.0),
        _v3_row("plan-only", 50.0, 70.0, plan_cost=5.0),
    ]
    assert viewmodel.pareto_set(rows, "w", "api") == {"cheap", "tie", "good", "plan-only"}
    assert viewmodel.pareto_set(rows, "w", "plan") == {"plan-only", "good"}


def test_scenario_view_reads_the_s1_core_stream_only_when_current():
    assert viewmodel._scenario_view({}) == {"api": {}, "plan": {}}
    assert viewmodel._scenario_view({"scenarios": {"status": "missing"}}) == {"api": {}, "plan": {}}
    shares = {"a": {key: {"share": value} for key, value in (("top1", 0.5), ("top3", 1.0), ("frontier", 0.25))}}
    runs = [{"stratum": "S0", "alternative": False, "rows": {}}, {"stratum": "S1", "alternative": False, "rows": shares}, {"stratum": "S1", "alternative": True, "rows": {}}]
    view = viewmodel._scenario_view({"scenarios": {"status": "current", "results": {"api": runs, "plan": runs}}})
    assert view["api"] == {"a": {"top1": 0.5, "top3": 1.0, "frontier": 0.25}} and view["plan"] == view["api"]


def _model(slug, name, api, plan, quality_rank, cost_api, cost_plan, fallback=None):
    return {
        "slug": slug,
        "name": name,
        "rank": {"api": api, "plan": plan},
        "overall": {"api": 80.0 - (api or 0), "plan": 80.0 - (plan or 0)},
        "quality": 70.0,
        "qualityRank": quality_rank,
        "costDims": {"api": cost_api, "plan": cost_plan},
        "cost": {"apiUsd": 1081.5, "planUsd": 101.5, "fallback": fallback, "subset": False},
    }


BASES = {
    "api": {"label": "API ranking", "pickLabel": "Best at API rates", "pickPhrase": "at API rates"},
    "plan": {"label": "Plan ranking", "pickLabel": "Best on a subscription", "pickPhrase": "on a subscription"},
}


def _slugs(result):
    return tuple(result[key]["slug"] for key in ("value", "other", "budget"))


def test_picks_show_the_leader_the_other_basis_leader_and_a_budget_model():
    models = [
        _model("big", "Big", 1, 3, 1, 0.0, 10.0),
        _model("mid", "Mid", 2, 1, 2, 50.0, 20.0, fallback="api"),
        _model("cheap", "Cheap", 3, 2, 3, 100.0, 90.0),
        _model("dead", "Dead", None, None, None, None, None),
    ]
    api = picks.build_picks(models, "api", BASES)
    assert _slugs(api) == ("big", "mid", "cheap")
    assert [api[key]["label"] for key in ("value", "other", "budget")] == [
        "Best overall value", "Best on a subscription", "Best on a budget",
    ]
    plan = picks.build_picks(models, "plan", BASES)
    assert _slugs(plan) == ("mid", "big", "cheap")
    assert plan["other"]["label"] == "Best at API rates"
    assert "API fallback" in plan["value"]["reason"] and "$101.50 per basket run" in plan["value"]["reason"]
    assert "$1,081.50 per basket run" in api["value"]["reason"] and "API fallback" not in api["other"]["reason"]
    for pick in (*api.values(), *plan.values()):
        assert len(pick["reason"].split()) < 25


def test_other_basis_pick_states_both_ranks_and_scores_on_that_basis():
    models = [_model("a", "Aye", 2, 1, 1, 10.0, 10.0), _model("b", "Bee", 1, 2, 2, 20.0, 20.0), _model("c", "Sea", 3, 3, 3, 90.0, 90.0)]
    plan = picks.build_picks(models, "plan", BASES)["other"]
    assert plan["slug"] == "b" and plan["reason"] == "Bee ranks #1 at API rates and #2 in the Plan ranking."
    assert (plan["score"], plan["unit"]) == (79.0, "overall at API rates")
    api = picks.build_picks(models, "api", BASES)["other"]
    assert api["reason"] == "Aye ranks #1 on a subscription and #2 in the API ranking."
    assert (api["score"], api["unit"]) == (79.0, "overall on a subscription")


def test_value_and_budget_picks_carry_their_score_and_unit():
    models = [_model("a", "Aye", 1, 2, 1, 10.0, 10.0), _model("b", "Bee", 2, 1, 2, 90.0, 90.0)]
    result = picks.build_picks(models, "api", BASES)
    assert (result["value"]["score"], result["value"]["unit"]) == (79.0, "overall")
    assert (result["budget"]["score"], result["budget"]["unit"]) == (78.0, "overall")


def test_other_basis_pick_falls_back_to_the_quality_leader_then_the_runner_up():
    same = [_model("a", "Aye", 1, 1, 2, 0.0, 0.0), _model("b", "Bee", 2, 2, 1, 50.0, 50.0), _model("c", "Sea", 3, 3, 3, 100.0, 100.0)]
    result = picks.build_picks(same, "api", BASES)
    assert _slugs(result) == ("a", "b", "c")
    assert result["other"]["label"] == "Best quality, any cost"
    assert result["other"]["unit"] == "quality" and result["other"]["score"] == 70.0
    assert "best quality score (70.0)" in result["other"]["reason"] and "#2 in the API ranking" in result["other"]["reason"]
    leader = [_model("a", "Aye", 1, 1, 1, 0.0, 0.0), _model("b", "Bee", 2, 2, 2, 50.0, 50.0), _model("c", "Sea", 3, 3, 3, 100.0, 100.0)]
    result = picks.build_picks(leader, "plan", BASES)
    assert _slugs(result) == ("a", "b", "c")
    assert result["other"]["label"] == "Runner-up overall"
    assert result["other"]["reason"] == "Bee is the runner-up in the Plan ranking at 78.0."
    assert (result["other"]["score"], result["other"]["unit"]) == (78.0, "overall")


def test_budget_pick_skips_models_already_picked_when_the_cheapest_third_has_several():
    models = [
        _model("a", "Aye", 1, 1, 1, 100.0, 100.0),
        _model("b", "Bee", 2, 2, 2, 10.0, 10.0),
        _model("c", "Sea", 3, 3, 3, 90.0, 90.0),
        _model("d", "Dee", 4, 4, 4, 0.0, 0.0),
    ]
    assert _slugs(picks.build_picks(models, "api", BASES)) == ("a", "b", "c")


def test_budget_pick_keeps_a_picked_model_when_every_cheap_model_is_already_picked():
    models = [
        _model("a", "Aye", 1, 2, 1, 100.0, 100.0),
        _model("b", "Bee", 2, 1, 2, 90.0, 90.0),
        _model("c", "Sea", 3, 3, 3, 0.0, 0.0),
        _model("d", "Dee", 4, 4, 4, 5.0, 5.0),
    ]
    result = picks.build_picks(models, "api", BASES)
    assert _slugs(result) == ("a", "b", "a")


def test_a_single_ranked_model_has_no_other_pick():
    models = [_model("only", "Only", 1, 1, 1, 50.0, 50.0)]
    result = picks.build_picks(models, "api", BASES)
    assert result["value"]["slug"] == "only" and result["other"] is None and result["budget"]["slug"] == "only"


def test_picks_are_none_when_nothing_is_ranked():
    models = [_model("dead", "Dead", None, None, None, None, None)]
    assert picks.build_picks(models, "api", BASES) == {"value": None, "other": None, "budget": None}


HISTORY = {
    "sourceVersion": "v1.5.0",
    "v150": {"a": 1, "b": 2, "c": 3},
    "v190": {"b": 1, "a": 2},
    "v191": {"b": 1, "a": 2, "d": 3},
}


def _current(**overrides):
    base = {
        "version": "v1.9.6",
        "dateIso": "2026-10-08",
        "dateHuman": "October 8, 2026",
        "modelCount": 3,
        "dimensionCount": 16,
        "ranks": {"b": {"api": 2, "plan": 1}, "a": {"api": 1, "plan": 2}, "d": {"api": 3, "plan": 3}},
        "unranked": ["c"],
    }
    base.update(overrides)
    return base


NAMES = {"a": "Alpha", "b": "Beta", "c": "Gamma", "d": "Delta"}


def test_changelog_is_newest_first_with_rank_changes_between_consecutive_versions():
    result = changelog.build_changelog(HISTORY, _current(), NAMES)
    versions = [entry["version"] for entry in result["versions"]]
    assert versions == ["v1.9.6", "v1.9.1", "v1.9.0", "v1.5.0"]
    by_version = {entry["version"]: entry for entry in result["versions"]}
    assert by_version["v1.5.0"]["rankChanges"] == []
    assert by_version["v1.5.0"]["date"] == "September 6, 2026"
    assert by_version["v1.9.0"]["date"] is None
    assert by_version["v1.9.0"]["rankChanges"] == [
        {"slug": "b", "name": "Beta", "from": 2, "to": 1},
        {"slug": "a", "name": "Alpha", "from": 1, "to": 2},
    ]
    assert by_version["v1.9.0"]["removed"] == ["c"]
    assert by_version["v1.9.1"]["added"] == ["d"]
    assert by_version["v1.9.1"]["rankChanges"] == []
    assert by_version["v1.9.6"]["rankChanges"] == [{"slug": "a", "name": "Alpha", "from": 2, "to": 1}, {"slug": "b", "name": "Beta", "from": 1, "to": 2}]
    assert by_version["v1.9.6"]["models"] == 3
    assert by_version["v1.9.6"]["dimensions"] == 16
    assert by_version["v1.5.0"]["dimensions"] is None
    assert by_version["v1.9.6"]["date"] == "October 8, 2026"
    assert "Alpha" in by_version["v1.9.6"]["summary"]
    assert "Beta" in by_version["v1.9.0"]["summary"]


def test_changelog_falls_back_to_the_id_for_unknown_names_and_handles_an_empty_current():
    result = changelog.build_changelog({"v150": {"x": 1}}, _current(ranks={}), {})
    first = result["versions"][-1]
    assert first["summary"].startswith("1 model ranked")
    assert "x" in first["summary"]
    current = result["versions"][0]
    assert current["rankChanges"] == []
    assert current["removed"] == ["x"]
    assert "No model" in current["summary"]


def test_model_history_omits_versions_without_a_record_and_never_infers_ranks():
    history_a = changelog.model_history(HISTORY, _current(), "a")
    assert [item["version"] for item in history_a] == ["v1.5.0", "v1.9.0", "v1.9.1", "v1.9.6"]
    assert history_a[0] == {"version": "v1.5.0", "date": "2026-09-06", "rank": {"api": 1, "plan": None}}
    assert history_a[1]["date"] is None
    assert history_a[-1] == {"version": "v1.9.6", "date": "2026-10-08", "rank": {"api": 1, "plan": 2}}
    history_d = changelog.model_history(HISTORY, _current(), "d")
    assert [item["version"] for item in history_d] == ["v1.9.1", "v1.9.6"]
    history_c = changelog.model_history(HISTORY, _current(), "c")
    assert [item["version"] for item in history_c] == ["v1.5.0"]


def test_picks_say_so_when_a_pick_has_no_cost_data():
    models = [_model("only", "Only", 1, 1, 1, 50.0, 50.0)]
    models[0]["cost"] = {"apiUsd": None, "planUsd": None, "fallback": None, "subset": False}
    assert "no cost data" in picks.build_picks(models, "api", BASES)["value"]["reason"]
    assert "no cost data" in picks.build_picks(models, "plan", BASES)["value"]["reason"]


def test_subset_cost_picks_say_their_cross_workload_ordering_is_not_identified():
    models = [_model("only", "Only", 1, 1, 1, 50.0, 50.0)]
    models[0]["cost"]["subset"] = True
    result = picks.build_picks(models, "api", BASES)
    assert result["value"]["reason"].endswith("Subset cost: cross-workload ordering not identified.")
    assert len(result["value"]["reason"].split()) < 25


def test_budget_pick_is_none_when_no_ranked_model_has_a_cost_score():
    models = [_model("only", "Only", 1, 1, 1, None, None)]
    result = picks.build_picks(models, "api", BASES)
    assert result["budget"] is None and result["value"]["slug"] == "only"


def test_changelog_versions_carry_recorded_ranks_keyed_by_slug():
    result = changelog.build_changelog(HISTORY, _current(), NAMES)
    by_version = {entry["version"]: entry for entry in result["versions"]}
    assert by_version["v1.5.0"]["ranks"] == {"a": 1, "b": 2, "c": 3}
    assert by_version["v1.9.0"]["ranks"] == {"a": 2, "b": 1}
    assert by_version["v1.9.6"]["ranks"] == {"a": 1, "b": 2, "d": 3}
    assert "c" not in by_version["v1.9.0"]["ranks"]


def test_changelog_slugs_replace_dots_so_links_match_model_pages():
    current = {
        "version": "v2.0.0", "dateIso": "2027-01-01", "dateHuman": "January 1, 2027", "modelCount": 2, "dimensionCount": 4,
        "ranks": {"gpt-6.1-sol": {"api": 1, "plan": 1}, "kimi-k3": {"api": 2, "plan": 2}},
    }
    history = {"v150": {"gpt-6.1-sol": 2, "kimi-k3": 1, "old.model": 3}}
    result = changelog.build_changelog(history, current, {"gpt-6.1-sol": "Sol", "kimi-k3": "Kimi"})
    latest = result["versions"][0]
    assert latest["ranks"] == {"gpt-6-1-sol": 1, "kimi-k3": 2}
    assert [c["slug"] for c in latest["rankChanges"]] == ["gpt-6-1-sol", "kimi-k3"]
    assert latest["removed"] == ["old-model"]


def test_changelog_leaves_a_model_without_an_api_rank_out_of_the_current_snapshot():
    """AGENTS.md: a configuration without a cost has no value score and no rank, so it is neither ranked nor 'added'."""

    current = _current(ranks={"a": {"api": 1, "plan": 1}, "e": {"api": None, "plan": None}})
    result = changelog.build_changelog(HISTORY, current, {**NAMES, "e": "Epsilon"})
    latest = result["versions"][0]
    assert latest["ranks"] == {"a": 1} and "e" not in latest["added"]
    assert latest["summary"].startswith("1 model ranked on 16 dimensions; Alpha")
    assert latest["models"] == 3  # the cohort count is the release's own, not the ranked count
