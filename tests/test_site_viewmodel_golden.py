"""Golden checks of the site view models against the committed snapshots (copied, never the live tree)."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from valuerank.paths import DATA
from valuerank.plan_costs import build_cost_fields, load_plan_routes
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
def ranked(scores):
    return [m for m in scores["models"] if m["rankingEligible"]]


def by_slug(rankings):
    return {m["slug"]: m for m in rankings["models"]}


# --- rankings.json: identity with the committed scores --------------------------------------


def test_rankings_header_and_bases(bundle, scores):
    rankings = bundle.rankings
    assert rankings["version"] == VERSION and rankings["publishDate"] == DATE
    assert rankings["observedAt"] == scores["observedAt"]
    assert rankings["defaultBasis"] == "plan"
    assert set(rankings["bases"]) == {"api", "plan"}
    assert rankings["bases"]["api"]["costUnit"] == "USD per Index run"
    assert rankings["bases"]["plan"]["costUnit"] == "USD per Index point"
    assert rankings["costWeightPct"] == 18.9394
    assert set(rankings["categories"]) == {"cost", "rely", "code", "prod", "intel", "language"}


def test_dimensions_mirror_the_score_weights(bundle, scores):
    dims = bundle.rankings["dimensions"]
    assert [d["key"] for d in dims] == [w["key"] for w in scores["weights"]]
    assert dims[0]["fullLabel"] == "Cost (selected basis)" and dims[0]["category"] == "cost"
    assert dims[0]["sourceUrl"] is None
    deepswe = next(d for d in dims if d["key"] == "deepswePassAt1")
    assert deepswe["weightPct"] == 18.9394 and deepswe["priority"] == 25 and deepswe["higherBetter"] is True
    assert deepswe["sourceUrl"].startswith("https://artificialanalysis.ai")
    assert all(d["category"] in bundle.rankings["categories"] for d in dims)
    assert all(d["sourceUrl"] for d in dims[1:])


def test_roster_has_28_models_ranked_first(bundle, ranked):
    models = bundle.rankings["models"]
    assert len(models) == 28
    leading = models[: len(ranked)]
    assert all(m["rankingEligible"] for m in leading)
    assert [m["rank"]["plan"] for m in leading] == list(range(1, len(ranked) + 1))
    trailing = models[len(ranked):]
    for model in trailing:
        assert model["rank"] == {"api": None, "plan": None}
        assert model["overall"] == {"api": None, "plan": None}
        assert model["exclusionReasons"] and model["rankingEligible"] is False
        assert model["costDims"] == {"api": None, "plan": None}
        assert model["pareto"] == {"api": False, "plan": False}
        assert all(v is None for v in model["dims"].values())


def test_api_basis_recomputation_reproduces_scores_json_exactly(bundle, ranked):
    """Validates the renormalisation rule: the API-basis composite equals the committed overall and rank."""

    models = by_slug(bundle.rankings)
    for source in ranked:
        model = models[viewmodel.slugify(source["id"])]
        assert model["overall"]["api"] == source["overallScore"]
        assert model["rank"]["api"] == source["rank"]
        assert model["quality"] == source["qualityScore"]
        assert model["qualityRank"] == source["qualityRank"]
        assert model["pareto"]["api"] is source["pareto"]


def test_plan_basis_rank_follows_independent_recomputation(bundle, scores, ranked):
    weights = {w["key"]: w["priority"] for w in scores["weights"]}
    fields = build_cost_fields(ranked, load_plan_routes(bundle.data / "plan_cost_routes.json"))
    expected = {}
    for source, field in zip(ranked, fields):
        dims = dict(source["dims"])
        dims["costComposite"] = field["planCostScore"]
        total = sum(dims[k] * weights[k] for k in dims)
        expected[source["id"]] = round(total / sum(weights[k] for k in dims), 1)
    order = sorted(ranked, key=lambda m: (-expected[m["id"]], m["name"]))
    models = by_slug(bundle.rankings)
    for position, source in enumerate(order, 1):
        model = models[viewmodel.slugify(source["id"])]
        assert model["rank"]["plan"] == position
        assert model["overall"]["plan"] == expected[source["id"]]


def test_cost_numbers_equal_plan_costs_output(bundle, scores):
    routes = load_plan_routes(bundle.data / "plan_cost_routes.json")
    fields = build_cost_fields(scores["models"], routes)
    models = by_slug(bundle.rankings)
    for source, field in zip(scores["models"], fields):
        cost = models[viewmodel.slugify(source["id"])]["cost"]
        assert cost["apiUsd"] == field["apiCost"]
        assert cost["planUsdPerRun"] == field["planCostPerRun"]
        assert cost["planUsdPerPoint"] == field["planCost"]
        assert cost["planComparableUsdPerPoint"] == field["planComparableCost"]
        assert cost["fallback"] == field["planCostFallback"]
        route = field["planRoute"]
        assert (cost["route"] is None) == (route is None)
        if route:
            assert cost["route"]["id"] == route["id"] and cost["route"]["valueMultiple"] == route["valueMultiple"]
            assert cost["route"]["planFeeUsd"] == route["planPriceUsd"]


def test_cost_dims_equal_ranked_cohort_cost_scores(bundle, ranked):
    fields = build_cost_fields(ranked, load_plan_routes(bundle.data / "plan_cost_routes.json"))
    models = by_slug(bundle.rankings)
    for source, field in zip(ranked, fields):
        model = models[viewmodel.slugify(source["id"])]
        assert model["costDims"] == {"api": field["apiCostScore"], "plan": field["planCostScore"]}
        assert model["dims"]["costComposite"] is None


def test_dims_raw_and_coverage_for_a_known_model(bundle, ranked):
    sol = by_slug(bundle.rankings)["gpt-6-1-sol"]
    assert sol["name"] == "GPT-6.1 Sol" and sol["developer"] == "OpenAI"
    assert sol["aaVariant"] == "max" and sol["aaUrl"].endswith("/gpt-6-1-sol")
    assert sol["dims"]["deepswePassAt1"] == 84.6
    assert sol["raw"]["deepswePassAt1"] == 70.0 and sol["raw"]["bugHuntFixedOf105"] == 44.3
    assert sol["raw"]["omniNonHallucination"] == 46.0
    assert sol["dims"]["terminalBenchV4"] is None and sol["raw"]["terminalBenchV4"] is None
    assert sol["coverage"] == {
        "pct": 88.64,
        "availablePriority": 117,
        "totalPriority": 132,
        "missing": ["Terminal-Bench 4.0", "Instruction Following (LiveBench)", "GPQA Diamond (legacy)"],
    }
    assert sol["intelligenceIndex"] == {"value": 52.0, "status": "measured"}
    assert sol["speed"] == 58.3 and sol["grade"] == "measured"


def test_coverage_equals_committed_metric_coverage(bundle, ranked, scores):
    labels = {w["key"]: w["label"] for w in scores["weights"]}
    models = by_slug(bundle.rankings)
    for source in ranked:
        coverage = models[viewmodel.slugify(source["id"])]["coverage"]
        committed = source["metricCoverage"]
        assert coverage["pct"] == committed["coveragePct"]
        assert coverage["availablePriority"] == committed["availablePriority"]
        assert coverage["totalPriority"] == committed["totalPriority"]
        assert coverage["missing"] == [labels[k] for k in committed["missingKeys"]]


def test_plan_meta_and_tiers(bundle, ranked):
    assert bundle.rankings["planMeta"] == {
        "asOf": "2026-10-08",
        "routeCount": 9,
        "supportedModelCount": 10,
        "fallbackModelCount": 6,
        "totalModelCount": 16,
    }
    models = by_slug(bundle.rankings)
    assert {models[s]["tier"] for s in models if models[s]["rankingEligible"]} <= {
        "Budget", "Near-Budget", "Mid-Range", "Premium", "Expensive",
    }
    assert all(m["tier"] is None for m in models.values() if not m["rankingEligible"])


def test_model_grades_follow_the_worst_value_entering_the_score(bundle):
    models = by_slug(bundle.rankings)
    assert models["gemini-3-7-flash"]["grade"] == "estimate"
    assert models["deepseek-v4-flash"]["grade"] == "claim"
    assert models["gpt-6-1-sol"]["grade"] == "measured"
    assert models["gpt-6-1-sol"]["cost"]["route"]["grade"] == "assumption"
    assert models["claude-opus-5-5"]["cost"]["route"]["grade"] == "measured"
    assert models["grok-4-7"]["cost"]["route"]["grade"] == "estimate"
    assert models["mimo-v2-6-pro"]["cost"]["route"]["grade"] == "assumption"
    assert models["kimi-k3"]["cost"]["route"] is None and models["kimi-k3"]["cost"]["fallback"] == "api"
    assert models["claude-opus-5-5"]["cost"]["route"]["evidenceLabel"].startswith("Controlled account")


def test_picks_reference_ranked_models_and_use_plain_reasons(bundle):
    models = by_slug(bundle.rankings)
    picks = bundle.rankings["picks"]
    assert set(picks) == {"api", "plan"}
    for basis in ("api", "plan"):
        value = picks[basis]["value"]
        assert models[value["slug"]]["rank"][basis] == 1
        budget = models[picks[basis]["budget"]["slug"]]
        assert budget["costDims"][basis] is not None
        for pick in picks[basis].values():
            assert len(pick["reason"].split()) < 25
            assert set(pick) == {"slug", "label", "reason", "score", "unit"}


def test_picks_show_three_different_models_with_data_driven_labels(bundle):
    picks = bundle.rankings["picks"]
    for basis in ("api", "plan"):
        assert len({pick["slug"] for pick in picks[basis].values()}) == 3
    assert picks["plan"]["other"]["label"] == "Best at API rates"
    assert models_rank(bundle, picks["plan"]["other"]["slug"]) == {"api": 1, "plan": 2}
    assert picks["api"]["other"]["label"] == "Best on a subscription"
    assert models_rank(bundle, picks["api"]["other"]["slug"]) == {"api": 5, "plan": 1}


def models_rank(bundle, slug):
    return by_slug(bundle.rankings)[slug]["rank"]


# --- models/<slug>.json ----------------------------------------------------------------------


def test_model_documents_cover_the_roster(bundle):
    assert len(bundle.models) == 28
    assert set(bundle.models) == {m["slug"] for m in bundle.rankings["models"]}


def test_model_document_dimensions_values_grades_and_sources(bundle, scores):
    doc = bundle.models["gpt-6-1-sol"]
    assert doc["selectedPage"] == "https://artificialanalysis.ai/models/gpt-6-1-sol"
    assert doc["summary"]["rank"] == {"api": 1, "plan": doc["summary"]["rank"]["plan"]}
    keys = [d["key"] for d in doc["dimensions"]]
    assert keys == [w["key"] for w in sorted(scores["weights"], key=lambda w: -w["weightPct"])]
    dims = {d["key"]: d for d in doc["dimensions"]}
    deepswe = dims["deepswePassAt1"]
    assert deepswe["value"] == 70.0 and deepswe["unit"] == "% pass@1" and deepswe["normalized"] == 84.6
    assert deepswe["grade"] == "measured" and deepswe["observedAt"] == "2026-10-08"
    assert deepswe["evaluatedVariant"] == "Codex / GPT-6.1 Sol / max"
    assert "Exact Codex GPT-6.1 Sol Max" in deepswe["note"]
    assert deepswe["source"]["url"].startswith("https://artificialanalysis.ai/agents")
    bug = dims["bugHuntFixedOf105"]
    assert bug["value"] == 44.3 and bug["grade"] == "measured" and "GPT-6.1 Sol" in bug["evaluatedVariant"]
    assert bug["source"]["url"].startswith("https://github.com/phuryn/bug-hunt-bench")
    missing = dims["terminalBenchV4"]
    assert missing["value"] is None and missing["grade"] == "missing" and missing["normalized"] is None
    assert missing["source"] is None and missing["observedAt"] is None
    cost = dims["costComposite"]
    assert cost["value"] == 1081.55 and cost["grade"] == "measured"
    sol_entry = by_slug(bundle.rankings)["gpt-6-1-sol"]
    assert cost["normalized"] == sol_entry["costDims"]["api"]
    assert cost["normalizedByBasis"] == sol_entry["costDims"]
    index = dims["intelligenceIndex"]
    assert index["value"] == 52.0 and index["source"]["url"].endswith("gpt-6-1-sol")
    assert index["observedAt"] == "2026-10-07"


def test_model_document_provider_claim_and_estimated_index(bundle):
    flash = bundle.models["deepseek-v4-flash"]
    tb4 = next(d for d in flash["dimensions"] if d["key"] == "terminalBenchV4")
    assert tb4["grade"] == "claim" and tb4["source"]["url"] == "https://api-docs.deepseek.com/updates/"
    assert tb4["evaluatedVariant"] == "DeepSeek V4.1-Flash" and tb4["observedAt"] == "2026-09-10"
    assert "current-route claim" in tb4["note"]
    gem = bundle.models["gemini-3-7-flash"]
    index = next(d for d in gem["dimensions"] if d["key"] == "intelligenceIndex")
    assert index["grade"] == "estimate"
    owner = bundle.models["claude-opus-5"]
    tb4_owner = next(d for d in owner["dimensions"] if d["key"] == "terminalBenchV4")
    assert tb4_owner["grade"] == "measured" and tb4_owner["value"] == 51.8
    assert tb4_owner["source"]["url"] == "https://www.tbench.ai/leaderboard/terminal-bench/4.0"
    assert "Claude Code" in tb4_owner["evaluatedVariant"]
    live = next(d for d in owner["dimensions"] if d["key"] == "livebenchInstructionFollowing")
    assert live["value"] == 63.7665 and live["evaluatedVariant"] == "claude-opus-5-max-effort"
    assert live["source"]["url"] == "https://livebench.ai/" and live["observedAt"] == "2026-10-07"


def test_model_document_plans_history_and_frontier(bundle):
    opus = bundle.models["claude-opus-5-5"]
    assert [p["id"] for p in opus["plans"] if p["selected"]] == [opus["cost"]["route"]["id"]]
    assert len(opus["plans"]) == 3
    per_point = [p["usdPerPoint"] for p in opus["plans"]]
    assert per_point == sorted(per_point)
    first = opus["plans"][0]
    assert first["usdPerRun"] == pytest.approx(opus["cost"]["apiUsd"] / first["valueMultiple"])
    assert opus["cost"] == by_slug(bundle.rankings)["claude-opus-5-5"]["cost"]
    assert [h["version"] for h in opus["history"]][-1] == "v1.9.6"
    assert opus["history"][-1]["rank"] == opus["summary"]["rank"]
    assert opus["frontier"]["onAaFrontier"] is True
    assert "frontier" in opus["frontier"]["aaFrontierNote"].lower()
    kimi = bundle.models["kimi-k3"]
    assert kimi["plans"] == [] and kimi["frontier"]["onAaFrontier"] is False
    sol = bundle.models["gpt-6-sol"]
    assert sol["frontier"]["onAaFrontier"] is False and "Not on" in sol["frontier"]["aaFrontierNote"]
    luna = bundle.models["gpt-6-luna"]
    assert luna["frontier"]["onAaFrontier"] is True


def test_models_absent_from_history_only_have_the_current_entry(bundle):
    sol = bundle.models["gpt-6-1-sol"]
    assert [h["version"] for h in sol["history"]] == ["v1.9.6"]
    unranked = bundle.models["claude-fable-5"]
    assert [h["version"] for h in unranked["history"]] == ["v1.5.0"]
    assert unranked["summary"]["rankingEligible"] is False and unranked["summary"]["exclusionReasons"]


# --- plans, benchmarks, tb4, changelog ---------------------------------------------------------


def test_plans_document(bundle):
    plans = bundle.plans
    assert plans["asOf"] == "2026-10-08" and plans["policy"]["reportingWindow"]["start"] == "2026-09-08"
    assert len(plans["routes"]) == 9 and len(plans["candidates"]) == 28
    route = next(r for r in plans["routes"] if r["id"] == "claude-pro-opus55-semianalysis")
    assert route["grade"] == "measured" and route["provider"] == "Anthropic"
    assert route["modelSlugs"] == ["claude-opus-5-5"] and route["planFeeUsd"] == 20
    assert route["sourceDate"] == "2026-10-06" and route["valueMultiple"] == 58.9
    mimo = next(r for r in plans["routes"] if r["id"] == "mimo-provisional-user-assumption")
    assert mimo["grade"] == "assumption" and mimo["sourceUrl"] is None and mimo["planFeeUsd"] is None
    candidate = next(c for c in plans["candidates"] if c["slug"] == "kimi-k3")
    assert candidate["fallback"] == "api" and candidate["routeId"] is None
    assert candidate["rank"] == by_slug(bundle.rankings)["kimi-k3"]["rank"]
    assert plans["workedExample"] == {"slugs": ["claude-opus-5-5", "gpt-6-1-sol"]}


def test_benchmarks_document(bundle, scores):
    doc = bundle.benchmarks
    ids = [s["id"] for s in doc["sources"]]
    assert {"aa-intelligence-index", "deepswe", "bug-hunt", "livebench", "terminal-bench-4", "provider-claims"} <= set(ids)
    deepswe = next(s for s in doc["sources"] if s["id"] == "deepswe")
    assert deepswe["name"] == "DeepSWE v1.1" and deepswe["owner"] == "Artificial Analysis"
    assert deepswe["weightPct"] == 18.9394 and deepswe["coverage"] == {"available": 14, "cohort": 16}
    assert deepswe["observedAt"] == "2026-10-08"
    tb4 = next(s for s in doc["sources"] if s["id"] == "terminal-bench-4")
    assert tb4["coverage"]["cohort"] == 16 and tb4["url"] == "https://www.tbench.ai/leaderboard/terminal-bench/4.0"
    assert sum(c["weightPct"] for c in doc["aaComponents"]) == 100
    assert all(c["url"].startswith("https://") for c in doc["aaComponents"])
    assert doc["coverageMatrix"]["cohortN"] == 28 and "intelligenceIndex" in doc["coverageMatrix"]["fields"]
    frontier = doc["frontier"]
    assert frontier["status"] == "complete" and frontier["checkedAt"] == "2026-10-07T17:23:20+00:00"
    assert len(frontier["rows"]) == 14
    luna = next(r for r in frontier["rows"] if r["aaId"] == "gpt-6-luna")
    assert luna["slug"] == "gpt-6-luna"
    low = next(r for r in frontier["rows"] if r["aaId"] == "gpt-6-luna-low")
    assert low["slug"] is None


def test_tb4_document(bundle, data):
    tb4 = json.loads((data / "tb4.json").read_text())
    doc = bundle.tb4
    assert doc["rows"] == tb4["rows"] and doc["frontierCount"] >= 1
    assert doc["cohortMapping"]["gpt-6-astra"]["rank"] == 1
    assert doc["cohortMapping"]["deepseek-v4-flash"]["status"] == "provider_claim"
    assert doc["cohortMapping"]["gpt-6-1-sol"]["status"] == "missing"
    assert doc["cohortMapping"]["claude-opus-5"]["status"] == "official"
    assert len(doc["cohortMapping"]) == 28


def test_changelog_document(bundle):
    versions = bundle.changelog["versions"]
    assert [v["version"] for v in versions] == ["v1.9.6", "v1.9.2", "v1.9.1", "v1.9.0", "v1.5.0"]
    assert versions[0]["models"] == 16 and versions[0]["dimensions"] == 16
    assert versions[0]["date"] == "October 8, 2026"
    assert versions[-1]["rankChanges"] == []


# --- page view models --------------------------------------------------------------------------


def test_index_page(bundle):
    page = viewmodel.index_page(bundle)
    assert set(page["headline"]) == {"api", "plan"}
    assert page["headline"]["api"] == "GPT-6.1 Sol leads the API ranking at 74.3; Claude Opus 5.5 leads on quality."
    assert page["headline"]["plan"] == "Claude Opus 5.5 leads the Plan ranking at 77.3 and also leads on quality."
    for sentence in page["headline"].values():
        assert len(sentence.split()) <= 18
    assert page["picks"] == bundle.rankings["picks"]
    assert len(page["models"]) == 16
    assert [m["rank"]["plan"] for m in page["models"]] == list(range(1, 17))
    assert next(m for m in page["models"] if m["slug"] == "gpt-6-1-sol")["rank"]["api"] == 1
    assert {"slug", "name", "developer", "rank", "overall", "quality", "grade", "costDims", "cost", "coveragePct"} <= set(page["models"][0])
    assert page["dimensions"] == bundle.rankings["dimensions"]
    assert page["rankingsJson"] is bundle.rankings
    assert len(page["chart"]["api"]) == 16 and len(page["chart"]["plan"]) == 16
    point = page["chart"]["plan"][0]
    assert set(point) == {"slug", "name", "x", "y", "pareto", "costLabel"}


def test_rankings_page(bundle):
    page = viewmodel.rankings_page(bundle)
    assert page["rankingsJson"] is bundle.rankings
    assert page["providers"] == sorted({m["developer"] for m in bundle.rankings["models"]})
    assert page["grades"] == ["measured", "claim", "estimate", "assumption"]
    assert {"rank", "name", "overall", "quality", "cost", "coverage", "grade"} <= {c["key"] for c in page["columns"]}


def test_model_page(bundle):
    page = viewmodel.model_page(bundle, "gpt-6-1-sol")
    assert page["slug"] == "gpt-6-1-sol"
    assert {r["slug"] for r in page["related"]} >= {"gpt-6-astra", "gpt-6-luna"}
    assert all(r["developer"] == "OpenAI" and r["slug"] != "gpt-6-1-sol" for r in page["related"])


def test_plans_page(bundle):
    page = viewmodel.plans_page(bundle)
    assert page["plansJson"] is bundle.plans
    example = page["workedExample"]["models"]
    assert [e["slug"] for e in example] == ["claude-opus-5-5", "gpt-6-1-sol"]
    opus = example[0]
    assert opus["routeLabel"] == bundle.models["claude-opus-5-5"]["cost"]["route"]["planLabel"]
    assert opus["planUsdPerRun"] == pytest.approx(opus["apiUsd"] / opus["valueMultiple"])
    assert opus["planUsdPerPoint"] == pytest.approx(opus["planUsdPerRun"] / opus["indexValue"])
    assert list(page["routesByProvider"]) == sorted(page["routesByProvider"])
    assert {r["provider"] for r in page["routesByProvider"]["OpenAI"]} == {"OpenAI"}


def test_benchmark_pages_wrap_their_documents(bundle):
    assert viewmodel.benchmarks_page(bundle) == {"benchmarksJson": bundle.benchmarks}
    assert viewmodel.tb4_page(bundle) == {"tb4Json": bundle.tb4}
    assert viewmodel.changelog_page(bundle) == {"changelogJson": bundle.changelog}


def test_methodology_page(bundle):
    page = viewmodel.methodology_page(bundle)
    assert page["dimensions"] == bundle.rankings["dimensions"]
    assert page["weights"]["deepswePassAt1"] == 18.9394
    example = page["workedExample"]
    model = by_slug(bundle.rankings)[example["slug"]]
    assert example["basis"] == "plan" and example["overall"] == model["overall"]["plan"]
    rows = example["steps"]
    assert all(r["included"] is (r["normalized"] is not None) for r in rows)
    assert example["missing"] == [r["label"] for r in rows if not r["included"]]
    assert sum(r["contribution"] for r in rows) == pytest.approx(example["overall"], abs=0.1)
    assert sum(r["effectiveWeightPct"] for r in rows if r["included"]) == pytest.approx(100, abs=0.01)
    assert example["availableWeightPct"] == pytest.approx(sum(r["weightPct"] for r in rows if r["included"]), abs=0.01)
    assert page["faq"] and all(set(q) == {"q", "a"} for q in page["faq"])
    assert not any("release" in q["q"].lower() or "included?" in q["q"] for q in page["faq"])
    assert page["limitations"] and all(isinstance(item, str) for item in page["limitations"])


def test_data_page(bundle):
    page = viewmodel.data_page(bundle)
    paths = [f["path"] for f in page["files"]]
    assert paths == [
        "/data/rankings.json", "/data/models/<slug>.json", "/data/plans.json",
        "/data/benchmarks.json", "/data/benchmarks/terminal-bench-4.json", "/data/changelog.json", "/data/livebench.json",
    ]
    assert all(f["description"] and f["schema"] for f in page["files"])


# --- export ------------------------------------------------------------------------------------


def test_export_writes_every_public_file_deterministically(data, tmp_path):
    first = export.export_public_data(data, tmp_path / "one")
    second = export.export_public_data(data, tmp_path / "two")
    relative = sorted(p.relative_to(tmp_path / "one").as_posix() for p in first)
    assert len(first) == 34
    assert relative[:5] == ["benchmarks.json", "benchmarks/terminal-bench-4.json", "changelog.json", "livebench.json", "models/claude-fable-5.json"]
    assert "plans.json" in relative and "rankings.json" in relative
    for left, right in zip(sorted(first), sorted(second)):
        assert left.read_bytes() == right.read_bytes()
    text = (tmp_path / "one" / "rankings.json").read_text()
    assert text.endswith("}\n") and not text.endswith("\n\n") and '\n  "version"' in text
    assert json.loads(text)["version"] == VERSION


def test_export_does_not_escape_non_ascii(data, tmp_path):
    written = export.export_public_data(data, tmp_path / "out")
    plans = (tmp_path / "out" / "plans.json").read_text()
    assert "\\u00" not in plans and "·" in plans
    assert all(p.is_file() for p in written)


def test_no_nan_or_infinity_leaks_into_public_json(data, tmp_path):
    for path in export.export_public_data(data, tmp_path / "out"):
        json.loads(path.read_text(), parse_constant=lambda c: pytest.fail(f"{c} in {path}"))
