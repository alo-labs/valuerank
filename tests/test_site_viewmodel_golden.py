"""Golden checks of the v3 site view models against the committed snapshots (copied, never the live tree)."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from valuerank import plan_routes
from valuerank import quality as q
from valuerank.paths import DATA
from valuerank.release import DATE, VERSION
from valuerank.site import export, viewmodel


def _copy_data(destination: Path) -> Path:
    destination.mkdir(parents=True)
    for source in DATA.glob("*.json"):
        shutil.copy2(source, destination / source.name)
    return destination


@pytest.fixture(scope="module")
def data(tmp_path_factory) -> Path:
    return _copy_data(tmp_path_factory.mktemp("golden") / "data")


@pytest.fixture(scope="module")
def bundle(data):
    return viewmodel.build_bundle(data)


@pytest.fixture(scope="module")
def scores(data):
    return json.loads((data / "scores.json").read_text())


@pytest.fixture(scope="module")
def v3(scores):
    return scores["v3"]


@pytest.fixture(scope="module")
def v3_rows(v3):
    return {row["id"]: row for row in v3["rows"]}


def by_slug(rankings):
    return {m["slug"]: m for m in rankings["models"]}


# --- rankings.json: identity with the v3 section of scores.json ----------------------------------


def test_rankings_header_and_bases(bundle, scores, v3):
    rankings = bundle.rankings
    assert rankings["version"] == VERSION and rankings["publishDate"] == DATE
    assert rankings["observedAt"] == scores["observedAt"] and rankings["defaultBasis"] == "plan"
    assert rankings["methodologyVersion"] == v3["methodologyVersion"] == "3.0.0" and rankings["basketVersion"] == "SDLC basket v1"
    assert {basis: rankings["bases"][basis]["costUnit"] for basis in ("api", "plan")} == {"api": "USD per basket run", "plan": "USD per basket run"}
    assert rankings["costWeightPct"] == 25.0
    assert set(rankings["categories"]) == {"cost", "code", "prod", "rely", "intel"}
    assert rankings["exchangeRate"]["api"]["valuePointsPerCostDoubling"] == v3["exchangeRate"]["api"]["valuePointsPerCostDoubling"]
    assert rankings["planExploratory"] is v3["identificationYield"]["exploratory"] is True


def test_dimensions_are_cost_and_the_leading_rankings_quality_leaves(bundle):
    dims = bundle.rankings["dimensions"]
    assert [d["key"] for d in dims] == [viewmodel.COST_KEY, *(leaf.key for leaf in q.LEAVES)]
    assert all(d["category"] in bundle.rankings["categories"] for d in dims)
    assert all(d["sourceUrl"] for d in dims[1:]) and dims[0]["sourceUrl"] is None


def test_roster_has_61_models_with_the_9_max_effort_rows_ranked_first(bundle, v3_rows):
    models = bundle.rankings["models"]
    assert len(models) == 62 and sum(m["rankingEligible"] for m in models) == len(v3_rows) == 9
    leading, trailing = models[:9], models[9:]
    assert all(m["rankingEligible"] and m["rank"]["plan"] is not None for m in leading)
    plan_ranks = [m["rank"]["plan"] for m in leading]
    assert plan_ranks == sorted(plan_ranks) and plan_ranks[0] == 1
    for model in trailing:
        assert model["rank"] == {"api": None, "plan": None} and model["overall"] == {"api": None, "plan": None}
        assert model["costDims"] == {"api": None, "plan": None} and model["pareto"] == {"api": False, "plan": False}
        if model["rankingEligible"]:
            continue
        assert model["exclusionReasons"] and all(v is None for v in model["dims"].values())
        assert model["grade"] == "missing" and model["coverage"]["pct"] == 0.0
    # O36/O38: a cohort configuration missing a benchmark after the logged search is listed with the gap, not ranked.
    # O53: the reason names what each ranking lacks.
    for slug in ("mimo-v2-6-flash", "minimax-m3-1-flash"):
        model = by_slug(bundle.rankings)[slug]
        assert not model["rankingEligible"] and "(O36, O53): Max-effort ranking: no Bug Hunt Bench" in model["exclusionReasons"][-1]
        assert model["exclusionReasons"][-1].endswith("AI Coding Daily ranking: no Bug Hunt Bench, AI Coding Daily (excl. bug finding)")
    # O51: every cohort configuration has an AA cost today, so no ranked row lacks a value score.
    assert not [m for m in trailing if m["rankingEligible"]]


def test_entries_reproduce_the_v3_rows_exactly(bundle, v3_rows):
    models = by_slug(bundle.rankings)
    for row_id, row in v3_rows.items():
        model = models[viewmodel.slugify(row_id)]
        assert model["overall"] == {"api": row["api"]["value"], "plan": row["planScore"]["value"]}
        assert model["rank"] == {"api": row["api"]["rank"], "plan": row["planScore"]["rank"]}
        assert model["costDims"] == {"api": row["api"]["costScore"], "plan": row["planScore"]["costScore"]}
        assert model["cost"]["apiUsd"] == row["api"]["costUsd"] and model["cost"]["planUsd"] == row["planScore"]["costUsd"]
        assert model["quality"] == row["quality"]["displayed"] and model["cost"]["subset"] is row["cost"]["subset"]
        assert model["coverage"]["pct"] == round(100 * row["quality"]["coverage"], 2)
        assert {key for key, value in model["dims"].items() if value is not None} == set(row["quality"]["leaves"])


def test_value_is_the_fixed_cost_share_rule_on_unrounded_inputs(bundle):
    for model in bundle.rankings["models"]:
        for basis in ("api", "plan"):
            if model["overall"][basis] is not None:
                assert model["overall"][basis] == 0.25 * model["costDims"][basis] + 0.75 * model["quality"]


def test_ranks_are_competition_ranks_on_unrounded_values(bundle):
    ranked = [m for m in bundle.rankings["models"] if m["rankingEligible"] and m["overall"]["plan"] is not None]
    assert len(ranked) == 9
    for model in ranked:
        assert model["rank"]["api"] == 1 + sum(1 for other in ranked if other["overall"]["api"] > model["overall"]["api"])
    # O48: the Plan basis ranks plan rows, so a configuration's Plan rank is its own plan row's rank among every plan row.
    plan_rows = [m for m in bundle.rankings["planModels"] if m["rankingEligible"] and m["overall"]["plan"] is not None]
    assert len(plan_rows) > len(ranked) and len({m["key"] for m in plan_rows}) == len(plan_rows)
    for row in plan_rows:
        assert row["rank"]["plan"] == 1 + sum(1 for other in plan_rows if other["overall"]["plan"] > row["overall"]["plan"])


def test_plan_cost_is_api_cost_over_the_selected_multiple_or_the_api_fallback(bundle, data):
    routes = {route["id"]: route for route in json.loads((data / "plan_cost_routes.json").read_text())["routes"]}
    for model in bundle.rankings["models"]:
        if not model["rankingEligible"]:
            continue
        cost = model["cost"]
        if cost["apiUsd"] is None:  # no cost: no Plan cost either, and no fallback
            assert cost["planUsd"] is None and cost["route"] is None and cost["fallback"] is None
        elif cost["route"] is None:
            assert cost["fallback"] == "api" and cost["planUsd"] == cost["apiUsd"]
        else:
            multiple = plan_routes.comparison_multiple(routes[cost["route"]["id"]])
            assert cost["planUsd"] == pytest.approx(cost["apiUsd"] / multiple)


def test_pareto_flags_follow_the_main_workload_point_estimates(bundle, v3):
    models = by_slug(bundle.rankings)
    for basis in ("api", "plan"):
        expected = {viewmodel.slugify(row_id) for row_id in viewmodel.pareto_set(v3["rows"], v3["mainWorkload"], basis)}
        assert {slug for slug, m in models.items() if m["pareto"][basis]} == expected
    # O17: a subset-workload row is never on the main-workload frontier (the max-effort ranking admits the Coding Agent Index).
    assert not models["mimo-v2-6-pro"]["pareto"]["api"] and models["gpt-6-1-sol"]["pareto"]["api"]


def test_flags_name_subset_rows(bundle):
    mimo = by_slug(bundle.rankings)["mimo-v2-6-pro"]
    # O50/E140: the max-effort ranking admits the Coding Agent Index v2.0 (8 of its 9 rows priced); MiMo-V2.6-Pro has no
    # Coding Agent Index cost, so it is scored on its own subset workload and flagged (O17).
    assert mimo["cost"]["subset"] is True and mimo["coverage"]["provisional"] is False and mimo["flags"][0].startswith("Subset cost")
    haiku = by_slug(bundle.rankings)["claude-haiku-5-5-max"]
    assert any(flag.startswith("AA cost caveat") for flag in haiku["flags"])


def test_picks_reference_ranked_models_with_plain_reasons(bundle):
    models = by_slug(bundle.rankings)
    for basis, picks in bundle.rankings["picks"].items():
        assert len({picks[kind]["slug"] for kind in ("value", "other", "budget")}) == 3
        for pick in picks.values():
            assert models[pick["slug"]]["rankingEligible"] and len(pick["reason"].split()) < 25
        assert "per basket run" in picks["value"]["reason"]
    assert bundle.rankings["picks"]["api"]["value"]["slug"] == "gpt-6-1-sol"
    assert bundle.rankings["picks"]["api"]["value"]["reason"].startswith("GPT-6.1 Sol has the highest overall score")


# --- per-model documents -------------------------------------------------------------------------


def test_model_documents_cover_the_roster(bundle):
    assert set(bundle.models) == {m["slug"] for m in bundle.rankings["models"]} and len(bundle.models) == 62


def test_model_document_leaves_components_routes_and_scenarios(bundle, v3_rows):
    doc = bundle.models["gpt-6-1-sol"]
    row = v3_rows["gpt-6.1-sol"]
    keys = [d["key"] for d in doc["dimensions"]]
    assert keys == [leaf.key for leaf in sorted(q.LEAVES, key=lambda leaf: -leaf.weight)]
    leaves = {d["key"]: d for d in doc["dimensions"]}
    frontiercode = leaves["frontierCode"]
    assert frontiercode["value"] == pytest.approx(0.4912, abs=1e-4) and frontiercode["grade"] == "measured"
    assert frontiercode["normalized"] == row["quality"]["leaves"]["frontierCode"]["z"] and frontiercode["source"]["url"].startswith("https://artificialanalysis.ai")
    assert leaves["bugHunt"]["value"] == 44.3 and "GPT-6.1 Sol" in leaves["bugHunt"]["evaluatedVariant"]
    assert leaves["omniscience"]["unit"].startswith("AA Omniscience Index")
    components = {c["key"]: c for c in doc["cost"]["components"]}
    # O50: the max-effort ranking admits the Coding Agent Index v2.0; FrontierCode is no longer a chart component.
    assert components["coding-agent-index"]["admitted"] is True and "frontiercode" not in components
    assert sum(c["costUsd"] for c in components.values() if c["admitted"]) == pytest.approx(doc["cost"]["apiUsd"])
    assert doc["cost"]["costScore"] == by_slug(bundle.rankings)["gpt-6-1-sol"]["costDims"]
    selected = [plan for plan in doc["plans"] if plan["selected"]]
    assert len(selected) == 1 and selected[0]["id"] == doc["cost"]["route"]["id"] and doc["plans"][0] is selected[0]
    for plan in doc["plans"]:
        # O91: the Pro 500 measurement in OpenAI's acknowledged fault window is listed as a diagnostic (case 5).
        assert plan["usdPerRun"] == pytest.approx(doc["cost"]["apiUsd"] / plan["valueMultiple"])
        assert plan["case"] in (2, 3, "identified") or (plan["case"] == 5 and "pro500" in plan["id"])
    assert doc["scenarios"]["status"] == "current" and {run["stratum"] for run in doc["scenarios"]["api"]} == {"S0", "S1", "S2", "S1M", "S1T"}
    assert doc["intervals"]["api"] == {"definite": "certified", "possible": "certified"}


def test_unranked_and_subset_documents(bundle):
    unranked = bundle.models["claude-fable-5"]
    assert unranked["summary"]["rankingEligible"] is False and unranked["plans"] == [] and unranked["cost"]["components"] == []
    assert all(d["grade"] == "missing" for d in unranked["dimensions"])
    mimo = bundle.models["mimo-v2-6-pro"]
    assert mimo["scenarios"]["api"] == []  # O17: a subset-workload row is outside the main-workload scenario streams
    argon = bundle.models["gemini-4-argon"]  # no subscription route names it, so the row falls back to API cost
    assert argon["plans"] == [] and argon["cost"]["fallback"] == "api" and argon["cost"]["planUsd"] == argon["cost"]["apiUsd"]
    assert argon["cost"]["planAmount"] is None and unranked["cost"]["planAmount"] is None


def test_transfer_rows_are_unevaluable_in_the_transfers_off_plan_streams(bundle):
    """E167: the core Plan streams run with owner-named transfers off; E166: the selected amount says what it measures."""

    sonnet = bundle.models["claude-sonnet-5-5"]
    plan = {(run["stratum"], run["kernel"]): run for run in sonnet["scenarios"]["plan"]}
    assert plan[("S0", "primary")]["unevaluable"] is None and plan[("S0", "primary")]["top1"] is not None
    for key in (("S1", "primary"), ("S2", "primary"), ("S1", "endpoint-heavy"), ("S1M", "primary"), ("S1T", "primary")):
        assert plan[key]["unevaluable"].startswith("owner-named transfer") and plan[key]["top1"] is None
    assert all(run["unevaluable"] is None for run in sonnet["scenarios"]["api"])
    assert sonnet["cost"]["planAmount"]["amountKind"] == "assumed API-equivalent consumption (owner-named transfer)"
    assert sonnet["cost"]["planAmount"]["amountUsd"] == pytest.approx(58.9 * 20) and sonnet["cost"]["planAmount"]["donorRouteId"] == "claude-pro-opus55-semianalysis"
    opus = bundle.models["claude-opus-5-5"]
    assert all(run["unevaluable"] is None for run in opus["scenarios"]["plan"]) and len(opus["scenarios"]["plan"]) == 6
    assert opus["cost"]["planAmount"]["amountKind"] == "measured-workload capacity"


def test_model_history_and_frontier_notes(bundle):
    opus = bundle.models["claude-opus-5-5"]
    assert opus["history"][-1]["version"] == VERSION and opus["history"][-1]["rank"] == opus["summary"]["rank"]
    assert opus["frontier"]["onAaFrontier"] is True and "frontier" in opus["frontier"]["aaFrontierNote"].lower()
    sol = bundle.models["gpt-6-sol"]
    assert sol["frontier"]["onAaFrontier"] is False and "Not on" in sol["frontier"]["aaFrontierNote"]


# --- plans, benchmarks, tb4, changelog -----------------------------------------------------------


def test_plans_document(bundle, v3):
    plans = bundle.plans
    # O45/O46: one route record per model and plan.
    assert plans["asOf"] == "2026-10-08" and len(plans["routes"]) == 137 and len(plans["candidates"]) == 9
    assert plans["identificationYield"] == v3["identificationYield"]
    route = next(r for r in plans["routes"] if r["id"] == "claude-pro-opus55-semianalysis")
    assert route["grade"] == "measured" and route["modelSlugs"] == ["claude-opus-5-5"] and route["valueMultiple"] == 58.9
    argon = next(c for c in plans["candidates"] if c["slug"] == "gemini-4-argon")
    assert argon["fallback"] == "api" and argon["routeId"] is None and argon["measuredOnly"] == {"status": "no measured route"}
    opus = next(c for c in plans["candidates"] if c["slug"] == "claude-opus-5-5")
    assert opus["measuredOnly"]["status"] == "measured, target-workload unmatched" and "workload-unmatched" in opus["flags"]
    assert plans["workedExample"] == {"slugs": ["claude-opus-5-5", "gpt-6-1-sol"]}


def test_benchmarks_document(bundle, v3):
    doc = bundle.benchmarks
    assert [s["id"] for s in doc["sources"]] == [leaf.key for leaf in q.LEAVES]
    frontiercode = next(s for s in doc["sources"] if s["id"] == "frontierCode")
    assert frontiercode["weightPct"] == 11.25 and frontiercode["coverage"] == {"available": 9, "cohort": 9} and frontiercode["execution"] == "AA-run"
    assert next(s for s in doc["sources"] if s["id"] == "bugHunt")["execution"] == "independent"
    # O37: Terminal-Bench is AA's own run; tbench.ai only fills a gap.
    terminal = next(s for s in doc["sources"] if s["id"] == "terminalBench")
    assert terminal["execution"] == "AA-run" and terminal["owner"] == "Artificial Analysis" and terminal["notes"].startswith("AA's own run")
    assert next(s for s in doc["sources"] if s["id"] == "omniscience")["notes"].startswith("Scored as AA's Omniscience Index")
    assert [c["key"] for c in doc["basket"]["admitted"]] == v3["admission"]["admitted"]
    assert {c["key"] for c in doc["basket"]["pending"]} == {"itbench-aa"}  # O50: v2.0 prices 7 of the max-effort ranking's 9 rows
    assert doc["basket"]["referencePanelSize"] >= doc["basket"]["requiredPanelSize"]
    frontier = doc["frontier"]
    assert frontier["status"] == "complete" and len(frontier["rows"]) == 19
    assert next(r for r in frontier["rows"] if r["aaId"] == "gpt-6-luna")["slug"] == "gpt-6-luna"


def test_tb4_document(bundle, data):
    tb4 = json.loads((data / "tb4.json").read_text())
    doc = bundle.tb4
    assert doc["rows"] == tb4["rows"] and doc["frontierCount"] >= 1 and len(doc["cohortMapping"]) == 62
    assert doc["cohortMapping"]["deepseek-v4-flash"]["status"] == "provider_claim"
    assert doc["cohortMapping"]["claude-opus-5"]["status"] == "official"
    # O33: the exact Muse Spark 1.3 (xhigh) row belongs to that effort only.
    assert doc["cohortMapping"]["muse-spark-1-3-xhigh"]["evaluatedModel"] == "Muse Spark 1.3 (xhigh)"
    assert doc["cohortMapping"]["muse-spark-1-3"]["status"] == "missing"


def test_changelog_document(bundle):
    versions = bundle.changelog["versions"]
    assert versions[0]["version"] == VERSION and versions[0]["models"] == 9 and versions[0]["dimensions"] == len(bundle.rankings["dimensions"]) == 14
    assert versions[-1]["version"] == "v1.5.0" and versions[-1]["rankChanges"] == []


# --- page view models ----------------------------------------------------------------------------


def test_index_page(bundle):
    page = viewmodel.index_page(bundle)
    assert page["headline"]["api"] == "GPT-6.1 Sol leads the API ranking at 60.0; Claude Opus 5.5 leads on quality."
    assert page["headline"]["plan"] == "Claude Opus 5.5 leads the Plan ranking at 64.2 and also leads on quality."
    assert page["picks"] == bundle.rankings["picks"] and page["rankingsJson"] is bundle.rankings
    assert len(page["models"]) == 9 and page["dimensions"] == bundle.rankings["dimensions"]
    assert len(page["chart"]["api"]) == len(page["chart"]["plan"]) == 9  # a row without a cost has no point and set(page["chart"]["plan"][0]) == {"slug", "name", "x", "y", "pareto", "costLabel"}
    assert page["chart"]["api"][0]["costLabel"].endswith("per basket run")


def test_rankings_and_models_pages(bundle):
    page = viewmodel.rankings_page(bundle)
    assert page["grades"] == ["measured", "claim", "estimate", "assumption"]
    assert [c["key"] for c in page["columns"] if c["default"]] == ["rank", "name", "overall", "quality", "cost", "grade", "coverage"]
    assert {c["key"] for c in page["columns"]} >= {leaf.key for leaf in q.LEAVES}
    models = viewmodel.models_page(bundle)
    assert models["rankedCount"] == 9 and models["unrankedCount"] == 53


def test_model_page(bundle):
    page = viewmodel.model_page(bundle, "gpt-6-1-sol")
    assert {r["slug"] for r in page["related"]} >= {"gpt-6-astra", "gpt-6-luna"}
    assert all(r["developer"] == "OpenAI" and r["slug"] != "gpt-6-1-sol" for r in page["related"])


def test_plans_page(bundle):
    page = viewmodel.plans_page(bundle)
    assert page["plansJson"] is bundle.plans
    opus, sol = page["workedExample"]["models"]
    assert (opus["slug"], sol["slug"]) == ("claude-opus-5-5", "gpt-6-1-sol")
    assert opus["planUsd"] == pytest.approx(opus["apiUsd"] / opus["valueMultiple"])
    assert list(page["routesByProvider"]) == sorted(page["routesByProvider"])


def test_benchmark_pages_wrap_their_documents(bundle):
    assert viewmodel.benchmarks_page(bundle) == {"benchmarksJson": bundle.benchmarks}
    assert viewmodel.tb4_page(bundle) == {"tb4Json": bundle.tb4}
    assert viewmodel.changelog_page(bundle) == {"changelogJson": bundle.changelog}


def test_methodology_page(bundle, v3):
    page = viewmodel.methodology_page(bundle)
    method = page["method"]
    assert method["costLabel"].startswith("contestant-model API token cost") and method["barLevel"] == "quality 63.5 (the displayed quality of Gemini 4 Argon at freeze)"
    assert method["anchors"]["api"]["low"] == v3["workloads"][v3["mainWorkload"]]["anchors"]["api"]["low"]
    assert method["streamDescriptions"]["S0"] == "published-record reporting precision" and method["notQuantified"]
    example = page["workedExample"]
    model = by_slug(bundle.rankings)[example["slug"]]
    # O36: every ranked row has every leaf, so the example has full coverage.
    assert example["overall"] == model["overall"]["plan"] and example["qualityCoveragePct"] == model["coverage"]["pct"] == 100
    rows = example["steps"]
    assert sum(r["contribution"] for r in rows) == pytest.approx(example["overall"], abs=0.05)
    assert sum(r["effectiveWeightPct"] for r in rows) == pytest.approx(100, abs=0.01)
    assert example["missing"] == [r["label"] for r in rows if not r["included"]]
    assert page["limitations"][-1].startswith("Subscription Value Multiples") and page["faq"]


def test_data_page(bundle):
    page = viewmodel.data_page(bundle)
    assert [f["path"] for f in page["files"]] == [
        "/data/rankings.json", "/data/rankings-aicd.json", "/data/models/<slug>.json", "/data/plans.json",
        "/data/benchmarks.json", "/data/benchmarks/terminal-bench-4.json", "/data/changelog.json", "/data/livebench.json",
    ]
    assert all(f["description"] and f["schema"] for f in page["files"])


# --- export ----------------------------------------------------------------------------------------


def test_export_writes_every_public_file_deterministically(data, tmp_path):
    first = export.export_public_data(data, tmp_path / "one")
    second = export.export_public_data(data, tmp_path / "two")
    relative = sorted(p.relative_to(tmp_path / "one").as_posix() for p in first)
    assert len(first) == 69 and "plans.json" in relative and "rankings-aicd.json" in relative  # 7 site documents and 62 model documents
    for left, right in zip(sorted(first), sorted(second)):
        assert left.read_bytes() == right.read_bytes()
    text = (tmp_path / "one" / "rankings.json").read_text()
    assert text.endswith("}\n") and json.loads(text)["version"] == VERSION


def test_export_does_not_escape_non_ascii(data, tmp_path):
    export.export_public_data(data, tmp_path / "out")
    plans = (tmp_path / "out" / "plans.json").read_text()
    assert "\\u00" not in plans and "·" in plans


def test_no_nan_or_infinity_leaks_into_public_json(data, tmp_path):
    for path in export.export_public_data(data, tmp_path / "out"):
        json.loads(path.read_text(), parse_constant=lambda c: pytest.fail(f"{c} in {path}"))


# --- the second ranking (O53) ------------------------------------------------------------------------


def test_the_ai_coding_daily_ranking_is_a_bundle_of_its_own(bundle, scores):
    other = bundle.extras["tracks"]["aicd"]
    rankings = other.rankings
    assert rankings["track"] == {"key": "aicd", "label": "AI Coding Daily ranking", "href": "/rankings/ai-coding-daily/"}
    assert bundle.rankings["track"]["key"] == "max" and set(bundle.extras["tracks"]) == {"aicd"}
    ranked = {m["slug"] for m in rankings["models"] if m["rankingEligible"]}
    assert len(ranked) == len(scores["v3Tracks"]["aicd"]["rows"]) == 16
    assert "aiCodingDaily" in {d["key"] for d in rankings["dimensions"]} and "vibeCode" not in {d["key"] for d in rankings["dimensions"]}
    # A configuration ranked only there takes its model page from that ranking, and every page lists both rankings.
    opus_high = bundle.models["claude-opus-5-5-high"]
    assert opus_high["summary"]["rankingEligible"] is True and "aiCodingDaily" in {d["key"] for d in opus_high["dimensions"]}
    assert [(r["track"], r["shown"], r["rankingEligible"]) for r in opus_high["rankings"]] == [("max", False, False), ("aicd", True, True)]
    sol = bundle.models["gpt-6-1-sol"]
    assert [(r["track"], r["shown"], r["rankingEligible"]) for r in sol["rankings"]] == [("max", True, True), ("aicd", False, False)]
    page = viewmodel.rankings_page(other)
    assert page["heading"] == "AI Coding Daily ranking" and page["action"] == "/rankings/ai-coding-daily/"
    assert [link["current"] for link in page["trackLinks"]] == [False, True]
    assert viewmodel.rankings_page(bundle)["heading"] == "Rankings"
