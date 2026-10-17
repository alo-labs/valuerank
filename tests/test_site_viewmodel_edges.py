"""Edge branches of the site view models, driven by small mutations of a copied data directory."""

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


def model(document, model_id):
    return next(m for m in document["models"] if m["id"] == model_id)


def dim(bundle, slug, key):
    return next(d for d in bundle.models[slug]["dimensions"] if d["key"] == key)


def test_missing_bug_hunt_deepswe_and_aa_source_degrade_to_missing_or_fallback(data):
    def change(scores):
        sol = model(scores, "gpt-6.1-sol")
        sol["bugHunt"]["matched"] = False
        sol["deepswePassAt1Pct"] = None
        sol["livebenchInstructionFollowing"] = None
    edit(data, "scores.json", change)
    bundle = viewmodel.build_bundle(data)
    assert dim(bundle, "gpt-6-1-sol", "bugHuntFixedOf105")["grade"] == "missing"
    assert dim(bundle, "gpt-6-1-sol", "deepswePassAt1")["grade"] == "missing"
    sol = next(m for m in bundle.rankings["models"] if m["slug"] == "gpt-6-1-sol")
    assert sol["raw"]["bugHuntFixedOf105"] is None and sol["raw"]["deepswePassAt1"] is None


def test_metric_without_source_record_falls_back_to_the_model_page(data):
    edit(data, "aa_metrics.json", lambda aa: aa["models"]["gpt-6.1-sol"]["metricSources"].pop("hle"))
    bundle = viewmodel.build_bundle(data)
    hle = dim(bundle, "gpt-6-1-sol", "hle")
    assert hle["source"]["url"] == "https://artificialanalysis.ai/models/gpt-6-1-sol"
    assert hle["observedAt"] is None and hle["grade"] == "measured"


def test_estimated_status_without_a_source_type_still_grades_the_index_as_estimate(data):
    def change(aa):
        record = aa["models"]["gpt-6.1-sol"]
        record["metricSources"]["intelligenceIndex"]["sourceType"] = "benchmark_owner"
    edit(data, "aa_metrics.json", change)
    edit(data, "scores.json", lambda s: model(s, "gpt-6.1-sol").__setitem__("intelligenceIndexStatus", "estimated"))
    bundle = viewmodel.build_bundle(data)
    assert dim(bundle, "gpt-6-1-sol", "intelligenceIndex")["grade"] == "estimate"
    assert bundle.models["gpt-6-1-sol"]["summary"]["grade"] == "estimate"


def test_a_model_without_cost_or_index_has_no_plan_numbers_and_a_missing_cost_dimension(data):
    def change(scores):
        pro = model(scores, "deepseek-v4-pro")
        pro["aaEvalCost"] = None
        pro["frontierSelection"] = None
    edit(data, "scores.json", change)
    bundle = viewmodel.build_bundle(data)
    pro = next(m for m in bundle.rankings["models"] if m["slug"] == "deepseek-v4-pro")
    assert pro["costDims"] == {"api": None, "plan": None}
    cost = dim(bundle, "deepseek-v4-pro", "costComposite")
    assert cost["grade"] == "missing" and cost["value"] is None and cost["source"] is None
    assert pro["tier"] is None
    assert pro["rank"]["api"] is not None


def test_unranked_model_with_a_cost_keeps_its_values_but_no_scores(data):
    bundle = viewmodel.build_bundle(data)
    fable = dim(bundle, "claude-fable-5", "costComposite")
    assert fable["value"] is not None and fable["normalized"] is None and fable["grade"] == "measured"
    assert fable["source"]["url"].startswith("https://artificialanalysis.ai")
    assert bundle.models["claude-fable-5"]["summary"]["grade"] == "measured"


def test_models_with_no_values_at_all_grade_as_missing(data):
    def change(scores):
        fable = model(scores, "claude-fable-5")
        for key in list(fable):
            if key in {"omniNonHallucination", "deepswePassAt1Pct", "gdpvalV21", "automationBenchAA", "aaLcr", "omniAccuracy", "hle", "gpqaDiamond", "scicode", "critpt", "intelligenceIndex", "speed", "terminalBenchV4Pct", "livebenchInstructionFollowing", "aaEvalCost"}:
                fable[key] = None
        fable["bugHunt"]["matched"] = False
    edit(data, "scores.json", change)
    bundle = viewmodel.build_bundle(data)
    assert bundle.models["claude-fable-5"]["summary"]["grade"] == "missing"
    assert bundle.models["claude-fable-5"]["summary"]["coverage"]["pct"] == 0.0


def test_terminal_bench_without_an_official_row_url_or_claim_still_names_the_leaderboard(data):
    def change(tb4):
        tb4["rows"] = [r for r in tb4["rows"] if r["cohortModelId"] != "claude-opus-5"]
        tb4["cohortRows"].pop("claude-opus-5")
    edit(data, "tb4.json", change)
    bundle = viewmodel.build_bundle(data)
    assert bundle.tb4["cohortMapping"]["claude-opus-5"] == {
        "status": "missing", "rank": None, "resolutionRatePct": None, "evaluatedModel": None,
    }
    assert dim(bundle, "claude-opus-5", "terminalBenchV4")["source"]["name"] == "Terminal-Bench 4.0 leaderboard"


def test_a_claim_without_a_recorded_publisher_or_caveat_still_renders(data):
    def change(scores):
        claim = model(scores, "deepseek-v4-flash")["terminalBenchV4Claim"]
        claim.pop("caveat")
        claim.pop("publishedOn")
    edit(data, "scores.json", change)
    bundle = viewmodel.build_bundle(data)
    tb4 = dim(bundle, "deepseek-v4-flash", "terminalBenchV4")
    assert tb4["note"] is None and tb4["observedAt"] is None and tb4["grade"] == "claim"


def test_history_missing_a_current_model_and_current_unranked_models_are_handled(data):
    edit(data, "ranking_history_v1.5.json", lambda h: h.__setitem__("v192", {}))
    bundle = viewmodel.build_bundle(data)
    versions = [v["version"] for v in bundle.changelog["versions"]]
    assert "v1.9.2" in versions
    entry = next(v for v in bundle.changelog["versions"] if v["version"] == "v1.9.2")
    assert entry["models"] == 0 and entry["summary"].startswith("No model")


def test_duplicate_slugs_are_rejected(data):
    def change(scores):
        model(scores, "gpt-6.1-sol")["id"] = "gpt-6-1-sol"
        clone = json.loads(json.dumps(model(scores, "gpt-6-1-sol")))
        clone["id"] = "gpt-6.1-sol"
        scores["models"].append(clone)
    edit(data, "scores.json", change)
    with pytest.raises(ValueError, match="duplicate model slug"):
        viewmodel.build_bundle(data)


def test_model_page_for_an_unknown_slug_raises(data):
    bundle = viewmodel.build_bundle(data)
    with pytest.raises(KeyError):
        viewmodel.model_page(bundle, "no-such-model")


def test_methodology_example_falls_back_to_the_top_model_when_everyone_is_complete(data):
    bundle = viewmodel.build_bundle(data)
    for item in bundle.rankings["models"]:
        item["coverage"]["pct"] = 100.0
    page = viewmodel.methodology_page(bundle)
    top = min((m for m in bundle.rankings["models"] if m["rank"]["plan"]), key=lambda m: m["rank"]["plan"])
    assert page["workedExample"]["slug"] == top["slug"]


def test_plans_page_ignores_worked_example_models_that_are_not_in_the_roster(data):
    bundle = viewmodel.build_bundle(data)
    bundle.plans["workedExample"]["slugs"].append("ghost")
    with pytest.raises(KeyError):
        viewmodel.plans_page(bundle)


def test_headline_when_no_model_is_ranked_is_explicit(data):
    def change(scores):
        for source in scores["models"]:
            source["rankingEligible"] = False
    edit(data, "scores.json", change)
    with pytest.raises(ValueError, match="no ranked models"):
        viewmodel.build_bundle(data)


def test_plans_page_requires_a_plan_route_for_each_worked_example_model(data):
    bundle = viewmodel.build_bundle(data)
    bundle.plans["workedExample"]["slugs"] = ["kimi-k3"]
    with pytest.raises(ValueError, match="no plan route"):
        viewmodel.plans_page(bundle)


def test_terminal_bench_rows_without_a_cost_stay_null_and_are_not_a_cost_frontier_point(data):
    baseline = viewmodel.build_bundle(data).tb4

    def change(tb4):
        tb4["rows"].append(dict(tb4["rows"][0], model="Unpriced (max)", baseName="Unpriced", cohortModelId=None, costUsd=None, resolutionRate=0.99, resolutionRatePct=99.0))
    edit(data, "tb4.json", change)
    updated = viewmodel.build_bundle(data).tb4
    assert updated["rows"][-1]["costUsd"] is None
    assert updated["frontierCount"] == baseline["frontierCount"]


def test_frontier_tier_fields_pass_through_to_rankings_and_model_documents(data):
    def change(scores):
        sol = model(scores, "gpt-6.1-sol")
        sol.update(aaFrontierTier="frontier", aaFrontierConfiguration="GPT-6.1 Sol (max)", aaFrontierIntelligenceGap=0, aaFrontierFootnote=None)
        luna = model(scores, "gpt-6-luna")
        luna.update(aaFrontierTier="near", aaFrontierConfiguration="GPT-6 Luna (high)", aaFrontierIntelligenceGap=2.5, aaFrontierFootnote="Footnote text.")
    edit(data, "scores.json", change)
    bundle = viewmodel.build_bundle(data)
    row = next(m for m in bundle.rankings["models"] if m["slug"] == "gpt-6-luna")
    assert (row["aaFrontierTier"], row["aaFrontierConfiguration"], row["aaFrontierIntelligenceGap"], row["aaFrontierFootnote"]) == (
        "near", "GPT-6 Luna (high)", 2.5, "Footnote text.")
    frontier = bundle.models["gpt-6-luna"]["frontier"]
    assert (frontier["tier"], frontier["configuration"], frontier["intelligenceGap"], frontier["footnote"]) == (
        "near", "GPT-6 Luna (high)", 2.5, "Footnote text.")
    sol = bundle.models["gpt-6-1-sol"]["frontier"]
    assert sol["tier"] == "frontier" and sol["intelligenceGap"] == 0 and sol["footnote"] is None


def test_frontier_tier_fields_default_to_null_when_the_snapshot_lacks_them(data):
    def change(scores):
        for m in scores["models"]:
            for key in ("aaFrontierTier", "aaFrontierConfiguration", "aaFrontierIntelligenceGap", "aaFrontierFootnote"):
                m.pop(key, None)
    edit(data, "scores.json", change)
    bundle = viewmodel.build_bundle(data)
    assert all(m["aaFrontierTier"] is None and m["aaFrontierFootnote"] is None for m in bundle.rankings["models"])
    assert all(
        (d["frontier"]["tier"], d["frontier"]["configuration"], d["frontier"]["intelligenceGap"], d["frontier"]["footnote"]) == (None,) * 4
        for d in bundle.models.values()
    )


def test_rankings_page_exposes_the_near_frontier_gap_from_the_policy(data):
    edit(data, "scores.json", lambda scores: scores["frontierSelection"].update(nearFrontierPolicy={"maxIntelligenceGap": 4}))
    assert viewmodel.rankings_page(viewmodel.build_bundle(data))["nearFrontierGap"] == "4"


def test_methodology_page_carries_the_model_inclusion_section_from_the_snapshot(data):
    def change(scores):
        scores["frontierSelection"]["nearFrontierPolicy"] = {"maxIntelligenceGap": 3, "text": "Policy text."}
        scores["frontierSelection"]["nearFrontierFamilies"] = [{"family": "Gemini 4 Argon", "modelId": "x", "configuration": "Gemini 4 Argon (high)", "intelligenceGap": 2}]
        model(scores, "gpt-6-luna")["aaFrontierFootnote"] = "Footnote text."
    edit(data, "scores.json", change)
    bundle = viewmodel.build_bundle(data)
    inclusion = viewmodel.methodology_page(bundle)["modelInclusion"]
    assert inclusion["policyText"] == "Policy text."
    assert inclusion["nearFrontierFamilies"] == [{"family": "Gemini 4 Argon", "configuration": "Gemini 4 Argon (high)", "gap": "2"}]
    assert inclusion["footnotes"][0]["text"] == "Footnote text."
    assert inclusion["frontierRule"] and "3 points" in inclusion["nearFrontierRule"]


def test_aa_footnote_becomes_the_note_on_the_cost_evidence(data):
    edit(data, "scores.json", lambda scores: model(scores, "gpt-6-luna").update(aaFrontierFootnote="Footnote text."))
    bundle = viewmodel.build_bundle(data)
    assert dim(bundle, "gpt-6-luna", "costComposite")["note"] == "Footnote text."
    assert dim(bundle, "gpt-6-1-sol", "costComposite")["note"] is None
