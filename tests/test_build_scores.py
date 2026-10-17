"""Behavior tests for the scoring stage (valuerank.build_scores)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

from valuerank import build_scores
from valuerank.paths import ROOT

GENERATED = ("scores.json", "coverage_matrix.json", "ranking_summary.json", "run_manifest.json")


CAPTURE = "data/aa_frontier_capture.json"


@pytest.fixture
def world(repo_copy: Path, pinned_clock: str) -> Path:
    """A repo copy with the clock pinned; the frontier capture now lives under data/."""

    return repo_copy


def run_main(root: Path):
    return build_scores.main(root=root, data=root / "data")


def test_golden_outputs_match_committed(world, capsys):
    for name in GENERATED:
        (world / "data" / name).unlink()
        (world / "data" / name).write_bytes(b"")
    # run_manifest.json is read-modify-write, so restore the committed seed first.
    (world / "data" / "run_manifest.json").write_bytes((ROOT / "data" / "run_manifest.json").read_bytes())
    (world / "data" / "coverage_matrix.json").write_bytes((ROOT / "data" / "coverage_matrix.json").read_bytes())
    assert run_main(world) == 0
    for name in GENERATED:
        assert (world / "data" / name).read_bytes() == (ROOT / "data" / name).read_bytes(), name
    summary = json.loads(capsys.readouterr().out)
    assert summary["outputs"] == ["data/scores.json", "data/coverage_matrix.json", "data/ranking_summary.json"]


# --------------------------------------------------------------------------
# helpers for mutating the copied inputs
# --------------------------------------------------------------------------

FILES = {
    "deepswe": "data/aa_deepswe.json",
    "aa": "data/aa_metrics.json",
    "inventory": "data/aa_reconciliation_inventory.json",
    "capture": CAPTURE,
    "livebench": "data/livebench.json",
    "tb4": "data/tb4.json",
    "bughunt": "data/bug_hunt.json",
}


def edit(root: Path, name: str, fn) -> None:
    path = root / FILES[name]
    document = json.loads(path.read_text())
    fn(document)
    path.write_text(json.dumps(document))


def outputs(root: Path) -> dict:
    return {
        name: json.loads((root / "data" / name).read_text())
        for name in ("scores.json", "coverage_matrix.json", "ranking_summary.json", "run_manifest.json")
    }


def first_mapped(document):
    return next(c for c in document["configurations"] if c["valueRankModelId"])


def inv_row(document, family=None, index=0):
    rows = [r for r in document["rows"] if family is None or r["family"] == family]
    return rows[index]


def cap_row(document, url):
    return next(r for r in document["frontier"] if r["url"] == url)


# --------------------------------------------------------------------------
# pure helpers
# --------------------------------------------------------------------------


def test_rank_normalize_best_100_worst_0_and_lower_is_better():
    assert build_scores.rank_normalize([10, 30, 20]) == [0.0, 100.0, 50.0]
    assert build_scores.rank_normalize([10, 30, 20], higher_better=False) == [100.0, 0.0, 50.0]


def test_rank_normalize_ties_receive_average_rank():
    # ranks 1,2.5,2.5,4 -> scores 100, 50, 50, 0
    assert build_scores.rank_normalize([9, 5, 5, 1]) == [100.0, 50.0, 50.0, 0.0]


def test_rank_normalize_edge_sizes():
    assert build_scores.rank_normalize([]) == []
    assert build_scores.rank_normalize([42]) == [100.0]
    assert build_scores.rank_normalize([7, 7]) == [50.0, 50.0]


@pytest.mark.parametrize(
    ("variant", "expected"),
    [
        (None, ""),
        ("  XHigh ", "xhigh"),
        ("high with fallback", "high"),
        ("max (default fallback)", "max"),
    ],
)
def test_frontier_effort_normalizes_and_strips_fallback(variant, expected):
    assert build_scores.frontier_effort(variant) == expected


@pytest.mark.parametrize("value", [None, True, "5", [1], float("nan"), float("inf")])
def test_require_number_rejects_bad_values(value):
    with pytest.raises(ValueError, match="required value: label"):
        build_scores.require_number(value, "label")


def test_require_number_and_optional_number_accept_numbers():
    assert build_scores.require_number(3, "x") == 3.0
    assert isinstance(build_scores.require_number(3, "x"), float)
    assert build_scores.optional_number(None, "x") is None
    assert build_scores.optional_number(2.5, "x") == 2.5
    with pytest.raises(ValueError):
        build_scores.optional_number("bad", "x")


def test_comparison_number_rounds_only_intelligence_index():
    assert build_scores.comparison_number(52.386, "intelligenceIndex", "x") == 52
    assert build_scores.comparison_number(52.386, "hle", "x") == 52.386
    with pytest.raises(ValueError):
        build_scores.comparison_number(None, "hle", "x")


# --------------------------------------------------------------------------
# bug-hunt emphasis view
# --------------------------------------------------------------------------

DOC = {
    "benchmark": "Bug Hunt",
    "benchmarkVersion": "v",
    "sourceCommit": "abc",
    "sources": {},
}
WEIGHTS = [
    {"key": "hle", "label": "HLE", "higherBetter": True, "priority": 10},
    {"key": "costComposite", "label": "Cost", "higherBetter": False, "priority": 20},
]


def bh_row(ident, fixed, hle, cost, deepswe=50.0, matched=True, rank=None):
    return {
        "id": ident,
        "name": ident.upper(),
        "bugHunt": {"matched": matched, "fixedOf105": fixed},
        "deepswePassAt1Pct": deepswe,
        "hle": hle,
        "costComposite": cost,
        "rank": rank,
    }


def test_emphasis_with_fewer_than_two_matched_rows_is_empty():
    rows = [bh_row("a", 10, 0.5, 5), bh_row("b", None, 0.4, 6, matched=False), bh_row("c", 5, 0.1, 7, deepswe=None)]
    ranking, ranked, weights = build_scores.build_bug_hunt_emphasis(rows, WEIGHTS, dict(DOC, excludedResults=[1]))
    assert ranked == []
    assert ranking["matchedN"] == 0
    assert ranking["availableMeasuredN"] == 1
    assert ranking["unscoredMeasuredModels"] == ["A"]
    assert ranking["missingModels"] == ["B", "C"]
    assert ranking["benchmarkWeightPct"] == 100.0
    assert ranking["excludedResults"] == [1]
    assert weights[0]["key"] == "bugHuntFixedOf105" and weights[0]["weightPct"] == 100.0
    assert ranking["ranking"] == []


def test_emphasis_weight_matches_published_percentage_and_scores():
    rows = [
        bh_row("a", 40, 0.9, 30, rank=1),
        bh_row("b", 20, 0.8, 10, rank=2),
        bh_row("c", 30, None, 20, rank=3),  # lacks HLE: its dimension is renormalized away
        bh_row("d", None, 0.1, 1, matched=False),
    ]
    ranking, ranked, weights = build_scores.build_bug_hunt_emphasis(rows, WEIGHTS, DOC)
    # hle has only two matched rows (a, b) so it stays; cost has three.
    assert [w["key"] for w in weights] == ["hle", "costComposite", "bugHuntFixedOf105"]
    assert sum(w["priority"] for w in weights) == 60
    assert ranking["totalPriority"] == 60
    assert ranking["basePrioritySum"] == 30
    assert ranking["benchmarkWeightPct"] == round(100 * 30 / 60, 4) == weights[-1]["weightPct"]
    assert sum(w["weightPct"] for w in weights) == pytest.approx(100.0, abs=1e-3)
    assert ranking["coveragePct"] == 75.0
    assert ranking["missingModels"] == ["D"]
    # a: hle 100, cost(lower better, highest cost -> 0), bh 100 -> (1000+0+3000)/60
    by_id = {item["modelId"]: item for item in ranking["ranking"]}
    assert by_id["a"]["emphasisScore"] == round((100 * 10 + 0 * 20 + 100 * 30) / 60, 1)
    # c has no hle dim: priorities renormalize over cost + bug hunt only
    assert by_id["c"]["emphasisScore"] == round((50 * 20 + 50 * 30) / 50, 1)
    assert [r.pop("rank") for r in ranking["ranking"]] == [1, 2, 3]
    assert [r["id"] for r in ranked] == [item["modelId"] for item in ranking["ranking"]]
    assert by_id["b"]["primaryRank"] == 2


def test_emphasis_skips_dimensions_with_one_measured_row_and_breaks_ties_by_cost_then_name():
    rows = [
        bh_row("a", 10, 0.9, None),
        bh_row("b", 10, None, None),
        bh_row("c", 10, None, 4),
    ]
    ranking, ranked, weights = build_scores.build_bug_hunt_emphasis(rows, WEIGHTS, DOC)
    # hle is measured for one row only -> dropped; cost for one row only -> dropped
    assert [w["key"] for w in weights] == ["bugHuntFixedOf105"]
    assert weights[0]["weightPct"] == 100.0
    assert {r["emphasisScore"] for r in ranking["ranking"]} == {50.0}
    # equal scores: lower cost first, missing cost (inf) last, then name
    assert [r["id"] for r in ranked] == ["c", "a", "b"]


# --------------------------------------------------------------------------
# semantics of the real (copied) data
# --------------------------------------------------------------------------


@pytest.fixture
def built(world):
    run_main(world)
    return outputs(world)


def test_weights_reflect_priorities_and_sum_to_100(built):
    weights = built["scores.json"]["weights"]
    assert sum(w["weightPct"] for w in weights) == pytest.approx(100.0, abs=0.01)
    total = sum(w["priority"] for w in weights)
    for w in weights:
        assert w["weightPct"] == round(100.0 * w["priority"] / total, 4)
    bug = next(w for w in weights if w["key"] == "bugHuntFixedOf105")
    assert bug["priority"] == build_scores.BUG_HUNT_PRIORITY
    assert built["scores.json"]["externalBenchmarks"]["bugHunt"]["primaryWeightPct"] == bug["weightPct"]


def test_bug_hunt_emphasis_weight_matches_published_percentage(built):
    emphasis = built["scores.json"]["bugHuntEmphasisRanking"]
    expected = round(100.0 * build_scores.BUG_HUNT_EMPHASIS_PRIORITY / emphasis["totalPriority"], 4)
    assert emphasis["benchmarkWeightPct"] == expected
    assert built["ranking_summary.json"]["bugHuntEmphasis"]["benchmarkWeightPct"] == expected
    assert built["coverage_matrix.json"]["externalBenchmarks"]["bugHunt"]["emphasisWeightPct"] == expected


def test_metric_coverage_percentage_and_renormalized_priority(built):
    models = built["scores.json"]["models"]
    weights = {w["key"]: w["priority"] for w in built["scores.json"]["weights"]}
    total = sum(weights.values())
    partial = 0
    for row in models:
        coverage = row["metricCoverage"]
        assert coverage["totalPriority"] == total
        assert coverage["availablePriority"] == sum(p for k, p in weights.items() if k in row["dims"])
        assert coverage["coveragePct"] == round(100.0 * coverage["availablePriority"] / total, 2)
        if not row["rankingEligible"]:
            continue
        if coverage["missingKeys"]:
            partial += 1
            assert row["isMissing"] is True
        available = [k for k in weights if k in row["dims"]]
        quality = [k for k in available if k != "costComposite"]
        expected = sum(row["dims"][k] * weights[k] for k in available) / sum(weights[k] for k in available)
        assert row["overallScore"] == round(expected, 1)
        expected_q = sum(row["dims"][k] * weights[k] for k in quality) / sum(weights[k] for k in quality)
        assert row["qualityScore"] == round(expected_q, 1)
    assert partial > 0  # the committed data contains rows with missing metrics


def test_ranked_order_and_exclusions(built):
    scores = built["scores.json"]
    ranked = [m for m in scores["models"] if m["rank"] is not None]
    assert [m["id"] for m in ranked] == scores["rankedModelIds"]
    assert [m["rank"] for m in ranked] == list(range(1, len(ranked) + 1))
    overall = [m["overallScore"] for m in ranked]
    assert overall == sorted(overall, reverse=True)
    assert all(m["rankingStatus"] == "ranked" for m in ranked)
    excluded = [m for m in scores["models"] if not m["rankingEligible"]]
    assert excluded
    for m in excluded:
        assert m["rank"] is None and m["overallScore"] is None and m["vRanks"] == {}
        assert m["rankingStatus"] == "excluded_from_primary_cohort"
        assert "Not a required selected AA frontier family model" in m["rankingExclusionReasons"]
    assert {a["id"] for a in scores["appendixNonRanked"]} == {m["id"] for m in excluded}
    assert [m["name"] for m in scores["models"] if not m["rankingEligible"]] == sorted(m["name"] for m in excluded)


def test_pareto_frontier_excludes_dominated_rows(built):
    scores = built["scores.json"]
    candidates = [
        m for m in scores["models"]
        if m["rankingEligible"] and m["costComposite"] is not None and m["qualityScore"] is not None
    ]
    for m in candidates:
        dominated = any(
            o["id"] != m["id"]
            and o["costComposite"] <= m["costComposite"]
            and o["qualityScore"] >= m["qualityScore"]
            and (o["costComposite"] < m["costComposite"] or o["qualityScore"] > m["qualityScore"])
            for o in candidates
        )
        assert m["pareto"] is (not dominated)
        assert (m["name"] in scores["pareto"]) is (not dominated)
    assert any(m["pareto"] is False for m in candidates)


def test_cost_normalization_is_relative_to_most_expensive_primary_model(built):
    primary = [m for m in built["scores.json"]["models"] if m["rankingEligible"] and m["aaEvalCost"] is not None]
    top = max(m["aaEvalCost"] for m in primary)
    for m in primary:
        assert m["aaCostNorm"] == round(m["aaEvalCost"] / top * 100, 2)
    assert max(m["aaCostNorm"] for m in primary) == 100.0
    assert built["scores.json"]["costMode"] == "aa-only"


def test_manifest_and_outputs_list_expected_relative_paths(world, capsys):
    run_main(world)
    printed = json.loads(capsys.readouterr().out)
    assert printed["outputs"] == ["data/scores.json", "data/coverage_matrix.json", "data/ranking_summary.json"]
    for relative in printed["outputs"]:
        assert (world / relative).is_file()
    manifest = json.loads((world / "data/run_manifest.json").read_text())
    scoring = manifest["scoring"]
    assert scoring["weights"] == json.loads((world / "data/scores.json").read_text())["weights"]
    assert scoring["observedAt"] == "2026-10-07T17:23:20Z"
    assert scoring["providerClaimsUsed"] == []  # the only claim targets a non-primary model
    assert scoring["primaryMissingFields"]
    assert printed["version"] == build_scores.VERSION
    assert printed["n"] == scoring["cohortN"]


def test_score_coverage_matches_counts(built):
    scoring = built["coverage_matrix.json"]["scoring"]
    for key, item in scoring["fields"].items():
        assert item["availableN"] + len(item["missingModels"]) == item["cohortN"]
        assert item["coveragePct"] == round(100.0 * item["availableN"] / item["cohortN"], 2)
    assert scoring["zeroGap"] is False
    assert scoring["noNeutralFills"] is True
    assert scoring["costCoverage"]["selectiveSubstitution"] is False


# --------------------------------------------------------------------------
# validation errors on the inputs
# --------------------------------------------------------------------------


def _set(key, value):
    def fn(document):
        document[key] = value
    return fn


def _mut_dup_config(document):
    mapped = [c for c in document["configurations"] if c["valueRankModelId"]]
    mapped[1]["valueRankModelId"] = mapped[0]["valueRankModelId"]


def _mut_not_exact(document):
    first_mapped(document)["matchStatus"] = "new_model_variant"


def _mut_score_range(document):
    first_mapped(document)["scorePct"] = 101


def _mut_score_text(document):
    first_mapped(document)["scorePct"] = "high"


def _mut_ghost_model(document):
    first_mapped(document)["valueRankModelId"] = "ghost-model"


def _mut_empty_aa(document):
    document["models"] = {}


CASES = [
    ("deepswe", _set("observedConfigurationN", True), "capture-backed configuration count"),
    ("deepswe", _set("observedConfigurationN", 0), "capture-backed configuration count"),
    ("deepswe", _set("observedConfigurationN", 30), "capture-backed configuration count"),
    ("deepswe", _set("benchmarkTasks", 100), "113-task source"),
    ("deepswe", _mut_dup_config, "invalid or duplicate exact AA DeepSWE mapping"),
    ("deepswe", _mut_not_exact, "invalid or duplicate exact AA DeepSWE mapping"),
    ("deepswe", _mut_score_range, "invalid AA DeepSWE score"),
    ("deepswe", _mut_score_text, "non-numeric required value"),
    ("deepswe", _mut_ghost_model, "must belong to the current ValueRank roster"),
    ("aa", _mut_empty_aa, "non-empty comparison roster"),
]


@pytest.mark.parametrize(("name", "mutation", "message"), CASES)
def test_invalid_inputs_are_rejected(world, name, mutation, message):
    edit(world, name, mutation)
    with pytest.raises(ValueError, match=message):
        run_main(world)


def _inv_incomplete(document):
    document["completeness"]["status"] = "partial"


def _inv_no_rows(document):
    document["rows"] = []


def _inv_count_mismatch(document):
    document["sourceUniverse"]["observedFrontierPointN"] += 1


def _inv_no_artifact(document):
    document["captureArtifact"] = ""


def _inv_row_missing_family(document):
    del document["rows"][0]["family"]


def _inv_not_observed(document):
    document["rows"][0]["directlyObservedFrontier"] = False


def _inv_duplicate_url(document):
    document["rows"][1]["sourceUrl"] = document["rows"][0]["sourceUrl"]


def _inv_name(document):
    document["rows"][0]["name"] = "Something else"


def _inv_cost(document):
    document["rows"][0]["totalCostUsd"] += 5


def _inv_unknown_url(document):
    document["rows"][0]["sourceUrl"] = "https://example.invalid/never-captured"


def _inv_inconsistent_ids(document):
    inv_row(document, "GPT-6 Luna", 1)["requiredFamilyModelId"] = "gpt-6-luna-other"


def _inv_ghost_model(document):
    for row in document["rows"]:
        if row["family"] == "GPT-6 Luna":
            row["requiredFamilyModelId"] = "ghost"


CAPTURE_CASES = [
    ("capture", lambda d: d.update(source_url="https://elsewhere.invalid"), "no longer matches its complete direct-observation capture"),
    ("capture", lambda d: d["frontier"].pop(), "no longer matches its complete direct-observation capture"),
    ("capture", lambda d: d["universe"].update(catalog_models=1), "no longer matches its complete direct-observation capture"),
    ("capture", lambda d: d["universe"].update(rendered_pareto_vertices=1), "no longer matches its complete direct-observation capture"),
    ("capture", lambda d: d["universe"].update(plotted_models_with_both_coordinates=1), "no longer matches its complete direct-observation capture"),
]


@pytest.mark.parametrize(("name", "mutation", "message"), CAPTURE_CASES)
def test_capture_must_match_inventory(world, name, mutation, message):
    edit(world, name, mutation)
    with pytest.raises(ValueError, match=message):
        run_main(world)


INVENTORY_CASES = [
    (_inv_incomplete, "complete observed frontier point set"),
    (_inv_no_rows, "complete observed frontier point set"),
    (_inv_count_mismatch, "complete observed frontier point set"),
    (_inv_no_artifact, "must identify its current frontier capture artifact"),
    (_inv_row_missing_family, "must carry its observed family"),
    (_inv_not_observed, "must carry its observed family"),
    (_inv_duplicate_url, "duplicate owner URL"),
    (_inv_name, "inconsistent with its current frontier capture"),
    (_inv_cost, "inconsistent with its current frontier capture"),
    (_inv_unknown_url, "inconsistent with its current frontier capture"),
    (_inv_inconsistent_ids, "inconsistent required model IDs"),
    (_inv_ghost_model, "absent from the selected AA metrics roster"),
]


@pytest.mark.parametrize(("mutation", "message"), INVENTORY_CASES)
def test_inventory_rows_are_validated(world, mutation, message):
    edit(world, "inventory", mutation)
    with pytest.raises(ValueError, match=message):
        run_main(world)


def aa_edit(model_id, **changes):
    def fn(document):
        document["models"][model_id].update(changes)
    return fn


AA_IDENTITY_CASES = [
    (aa_edit("gpt-6-luna", aaUrl="https://artificialanalysis.ai/models/not-a-row"), "must identify one exact selected source URL"),
    (aa_edit("gpt-6.1-sol", aaSlug="other-slug"), "source slug does not match"),
    (aa_edit("gpt-6.1-sol", displayName="GPT-6 Astra"), "family does not match selected catalog identity"),
    (aa_edit("mimo-v2-6-pro", aaVariant="high"), "unexpected selected effort"),
    (aa_edit("gpt-6.1-sol", aaVariant="min"), "effort does not match selected catalog variant"),
    (aa_edit("claude-opus-5-5", aaName="Claude Opus 5.5", aaShortName="Opus"), "fallback does not match"),
]


@pytest.mark.parametrize(("mutation", "message"), AA_IDENTITY_CASES)
def test_frontier_family_must_match_selected_catalog(world, mutation, message):
    edit(world, "aa", mutation)
    with pytest.raises(ValueError, match=message):
        run_main(world)


def test_cohort_files_must_cover_the_exact_aa_roster(world):
    edit(world, "livebench", lambda d: d["models"].pop("gpt-5.5"))
    with pytest.raises(ValueError, match="LiveBench snapshot must contain exactly"):
        run_main(world)


def test_bug_hunt_must_declare_exact_roster(world):
    edit(world, "bughunt", lambda d: d["models"].pop())
    with pytest.raises(ValueError, match="Bug Hunt snapshot must declare exactly"):
        run_main(world)


@pytest.mark.parametrize("fixed", [-1, 106])
def test_bug_hunt_scores_must_be_in_range(world, fixed):
    def fn(document):
        next(m for m in document["models"] if m["matched"])["fixedOf105"] = fixed
    edit(world, "bughunt", fn)
    with pytest.raises(ValueError, match="invalid Bug Hunt score/sample"):
        run_main(world)


def test_bug_hunt_sample_must_be_positive(world):
    def fn(document):
        next(m for m in document["models"] if m["matched"])["sampleN"] = 0
    edit(world, "bughunt", fn)
    with pytest.raises(ValueError, match="invalid Bug Hunt score/sample"):
        run_main(world)


def test_bug_hunt_score_must_be_numeric(world):
    def fn(document):
        next(m for m in document["models"] if m["matched"])["fixedOf105"] = None
    edit(world, "bughunt", fn)
    with pytest.raises(ValueError, match="missing/non-numeric"):
        run_main(world)


def test_unknown_display_name_is_rejected(world):
    edit(world, "aa", aa_edit("gpt-5.5", displayName="Mystery Model"))
    with pytest.raises(ValueError, match="identity mapping missing: Mystery Model"):
        run_main(world)


def test_non_positive_cost_maximum_is_rejected(world):
    def fn(document):
        for model in document["models"].values():
            model["metrics"]["aaEvalCost"] = 0
    edit(world, "aa", fn)
    with pytest.raises(ValueError, match="requires a positive maximum"):
        run_main(world)


def test_frontier_model_without_quality_dimension_is_rejected(world):
    def fn(document):
        metrics = document["models"]["mimo-v2-6-flash"]["metrics"]
        for key in metrics:
            if key != "aaEvalCost":
                metrics[key] = None
    edit(world, "aa", fn)
    edit(world, "livebench", lambda d: d["models"]["mimo-v2-6-flash"].update(instructionFollowingScore=None))
    with pytest.raises(ValueError, match=r"finite non-cost quality score: \['mimo-v2-6-flash'\]"):
        run_main(world)


# --------------------------------------------------------------------------
# alternative scoring scenarios
# --------------------------------------------------------------------------


def unmatch_all_bug_hunt(document):
    for model in document["models"]:
        model["matched"] = False


def test_without_bug_hunt_overlap_the_dimension_is_dropped(world):
    edit(world, "bughunt", unmatch_all_bug_hunt)
    run_main(world)
    out = outputs(world)
    scores = out["scores.json"]
    assert all(w["key"] != "bugHuntFixedOf105" for w in scores["weights"])
    assert scores["cohort"]["exactBenchmarkOverlapN"] == 0
    assert scores["cohort"]["n"] == scores["cohort"]["frontierRequiredModelN"]
    assert scores["externalBenchmarks"]["bugHunt"]["primaryWeightPct"] == 0.0
    dropped = out["ranking_summary.json"]["droppedDimensions"]
    assert dropped[-1]["key"] == "bugHuntFixedOf105"
    assert dropped[-1]["availableN"] == 0
    assert all(d["availableN"] < 2 for d in dropped)
    assert out["coverage_matrix.json"]["scoring"]["zeroGap"] is False
    emphasis = scores["bugHuntEmphasisRanking"]
    assert emphasis["matchedN"] == 0 and emphasis["ranking"] == []
    assert emphasis["benchmarkWeightPct"] == 100.0
    assert out["ranking_summary.json"]["bugHuntEmphasis"]["topFive"] == []
    # every primary weight still normalizes to 100%
    assert sum(w["weightPct"] for w in scores["weights"]) == pytest.approx(100.0, abs=0.01)


def unverified(configs):
    def fn(document):
        record = next(m for m in document["models"] if m["modelId"] == "gpt-5.5")
        record["matchStatus"] = "reasoning_variant_unverified"
        if configs is not None:
            record["availableOwnerConfigurations"] = configs
    return fn


def exclusion_reasons(root, model_id="gpt-5.5"):
    scores = json.loads((root / "data/scores.json").read_text())
    return next(m for m in scores["models"] if m["id"] == model_id)["rankingExclusionReasons"]


def test_unverified_reasoning_variant_reports_owner_default_scores(world):
    edit(world, "bughunt", unverified([{"fixedOf105": 40}, {"fixedOf105": True}, {"fixedOf105": "n/a"}, {}, {"fixedOf105": 12.5}]))
    run_main(world)
    assert exclusion_reasons(world)[0] == (
        "No eligible exact-variant Bug Hunt match; owner default result 40/105, 12.5/105 available; "
        "selected reasoning equivalence is unverified"
    )


def test_unverified_reasoning_variant_without_numeric_scores(world):
    edit(world, "bughunt", unverified(None))
    run_main(world)
    reasons = exclusion_reasons(world)
    assert reasons[0].endswith("owner default result available; selected reasoning equivalence is unverified")
    assert reasons[-1] == "Not a required selected AA frontier family model"


def test_missing_owner_result_has_plain_exclusion_reason(world):
    run_main(world)
    assert exclusion_reasons(world)[:2] == [
        "No eligible exact-model Bug Hunt result in the selected source snapshot",
        "No exact-variant AA DeepSWE result in the selected source snapshot",
    ]


def test_unavailable_cost_drops_the_cost_dimension(world):
    def fn(document):
        for model in document["models"].values():
            model["metrics"]["aaEvalCost"] = None
    edit(world, "aa", fn)
    run_main(world)
    out = outputs(world)
    assert out["scores.json"]["costMode"].startswith("unavailable")
    assert all(w["key"] != "costComposite" for w in out["scores.json"]["weights"])
    assert out["scores.json"]["pareto"] == []
    assert "costComposite" in {d["key"] for d in out["ranking_summary.json"]["droppedDimensions"]}
    assert all(m["costComposite"] is None for m in out["scores.json"]["models"])


def test_single_missing_cost_leaves_that_row_unnormalized(world):
    edit(world, "aa", lambda d: d["models"]["gpt-6.1-sol"]["metrics"].update(aaEvalCost=None))
    run_main(world)
    rows = {m["id"]: m for m in outputs(world)["scores.json"]["models"]}
    assert rows["gpt-6.1-sol"]["aaCostNorm"] is None
    assert "costComposite" in rows["gpt-6.1-sol"]["metricCoverage"]["missingKeys"]
    assert rows["gpt-6.1-sol"]["isMissing"] is True
    assert rows["gpt-6.1-sol"]["pareto"] is None  # no cost, so it never enters the Pareto comparison


def test_provider_claim_for_primary_model_is_recorded(world):
    def fn(document):
        claim = dict(document["providerClaims"][0])
        claim.update(cohortModelId="mimo-v2-6-flash", claimId="mimo-claim", sourceUrl="https://example.invalid/claim")
        document["providerClaims"].append(claim)
    edit(world, "tb4", fn)
    run_main(world)
    out = outputs(world)
    row = next(m for m in out["scores.json"]["models"] if m["id"] == "mimo-v2-6-flash")
    assert row["terminalBenchV4SourceType"] == "model_provider_claim"
    assert row["terminalBenchV4"] == 0.312
    assert out["run_manifest.json"]["scoring"]["providerClaimsUsed"] == [
        {"model": "MiMo-V2.6-Flash", "benchmark": "Terminal-Bench 4.0", "sourceUrl": "https://example.invalid/claim"}
    ]


def test_official_terminal_bench_row_beats_provider_claim(world):
    run_main(world)
    row = next(m for m in outputs(world)["scores.json"]["models"] if m["id"] == "gpt-6-astra")
    assert row["terminalBenchV4SourceType"] == "benchmark_owner"
    assert row["terminalBenchV4Claim"] is None


# --------------------------------------------------------------------------
# command-line entry point
# --------------------------------------------------------------------------


def test_module_entry_point_runs_main_and_exits_zero(world, monkeypatch, capsys):
    import runpy

    import valuerank.paths as paths

    monkeypatch.setattr(paths, "ROOT", world)
    monkeypatch.setattr(paths, "DATA", world / "data")
    (world / "data" / "scores.json").unlink()
    monkeypatch.delitem(sys.modules, "valuerank.build_scores")
    with pytest.raises(SystemExit) as exit_info:
        runpy.run_module("valuerank.build_scores", run_name="__main__", alter_sys=True)
    assert exit_info.value.code == 0
    assert json.loads(capsys.readouterr().out)["version"] == build_scores.VERSION
    assert (world / "data/scores.json").read_bytes() == (ROOT / "data/scores.json").read_bytes()
