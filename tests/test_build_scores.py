"""Behavior tests for the scoring stage (valuerank.build_scores)."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import pytest

from valuerank import build_scores, quality
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
    "scoreboard": "data/bug_hunt_scoreboard.json",
    "leaves": "data/leaf_evidence.json",
}


def log_searches(*model_ids):
    """O36: an exhaustive search logged on the cutoff for every leaf of the named configurations, with its open-web step (I28)."""

    def fn(document):
        document["searches"] += [{"modelId": model_id, "leaf": leaf.key, "searchedOn": "2026-10-21", "result": "not found", "sources": [],
                                  "openWeb": {"searchedOn": "2026-10-21", "queries": [f"{model_id} {leaf.key}"], "candidates": []}}
                                 for model_id in model_ids for leaf in quality.ALL_LEAVES.values()]
    return fn


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


@pytest.mark.parametrize(
    ("family", "developer", "short"),
    [
        ("Claude Haiku 5.5", "Anthropic", "Haiku 5.5"),
        ("Claude Sonnet 5.5", "Anthropic", "Sonnet 5.5"),
        ("Gemini 4 Argon", "Google DeepMind", "Gem 4 Argon"),
    ],
)
def test_frontier_and_near_frontier_families_have_identity_mappings(family, developer, short):
    assert build_scores.DEVELOPER[family] == developer
    assert build_scores.SHORT[family] == short


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
    {"key": "costComposite", "label": "Cost", "higherBetter": False, "priority": None},
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
    rows = [bh_row("a", 10, 0.5, 5), bh_row("b", None, 0.4, 6, matched=False), bh_row("c", 5, 0.1, 7, matched=False)]
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
    # Cost keeps its fixed share; hle and Bug Hunt split the rest by quality priority (10 + 30).
    assert ranking["totalPriority"] == 40
    assert ranking["basePrioritySum"] == 10
    assert weights[1]["weightPct"] == build_scores.COST_WEIGHT_PCT == 25.0
    assert ranking["benchmarkWeightPct"] == round(75 * 30 / 40, 4) == weights[-1]["weightPct"]
    assert sum(w["weightPct"] for w in weights) == pytest.approx(100.0, abs=1e-3)
    assert ranking["coveragePct"] == 75.0
    assert ranking["missingModels"] == ["D"]
    # a: cost 30 is the dearest (log score 0); hle 100 and bh 100 -> quality 100
    by_id = {item["modelId"]: item for item in ranking["ranking"]}
    assert by_id["a"]["emphasisScore"] == round(0.25 * 0 + 0.75 * 100, 1)
    # c has no hle dim: quality is Bug Hunt alone (50); cost 20 on the log scale between 10 and 30
    cost_c = round(100 * (math.log(30) - math.log(20)) / (math.log(30) - math.log(10)), 1)
    assert by_id["c"]["emphasisScore"] == round(0.25 * cost_c + 0.75 * 50, 1)
    assert [r.pop("rank") for r in ranking["ranking"]] == [1, 2, 3]
    assert [r["id"] for r in ranked] == [item["modelId"] for item in ranking["ranking"]]
    assert by_id["b"]["primaryRank"] == 2


def test_emphasis_skips_dimensions_with_one_measured_row_and_breaks_ties_by_cost_then_name():
    rows = [
        bh_row("a", 10, None, None),
        bh_row("c", 10, None, 4),
        bh_row("b", 10, None, 4),
        bh_row("d", 10, 0.9, None),
    ]
    ranking, ranked, weights = build_scores.build_bug_hunt_emphasis(rows, WEIGHTS, DOC)
    # hle is measured for one row only -> dropped; cost (two rows) keeps its fixed share
    assert [w["key"] for w in weights] == ["costComposite", "bugHuntFixedOf105"]
    assert weights[1]["weightPct"] == 75.0 == ranking["benchmarkWeightPct"]
    assert {r["emphasisScore"] for r in ranking["ranking"]} == {50.0}
    # equal scores and equal cost: by name
    assert [r["id"] for r in ranked] == ["b", "c"]


def test_emphasis_gives_a_row_without_cost_no_score_and_no_rank():
    """AGENTS.md: a configuration without a cost gets no value score, so it is left out of the emphasis ranking."""

    rows = [bh_row("a", 10, None, None), bh_row("b", 20, None, 4), bh_row("c", 30, None, 8)]
    ranking, ranked, _weights = build_scores.build_bug_hunt_emphasis(rows, WEIGHTS, DOC)
    assert [r["id"] for r in ranked] == ["c", "b"]
    assert rows[0]["bugHuntEmphasisScore"] is None and rows[0]["bugHuntEmphasisRank"] is None
    assert rows[0]["bugHuntEmphasisDims"]["bugHuntFixedOf105"] == 0.0  # it keeps its normalised Bug Hunt value
    assert ranking["matchedN"] == 2 and ranking["coveragePct"] == round(100 * 2 / 3, 2)
    assert [r["rank"] for r in ranking["ranking"]] == [1, 2]


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
    cost = next(w for w in weights if w["key"] == "costComposite")
    assert cost["priority"] is None and cost["weightPct"] == build_scores.COST_WEIGHT_PCT == 25.0
    quality = [w for w in weights if w["key"] != "costComposite"]
    total = sum(w["priority"] for w in quality)
    for w in quality:
        assert w["weightPct"] == round(75.0 * w["priority"] / total, 4)
    bug = next(w for w in weights if w["key"] == "bugHuntFixedOf105")
    assert bug["priority"] == build_scores.BUG_HUNT_PRIORITY
    assert built["scores.json"]["externalBenchmarks"]["bugHunt"]["primaryWeightPct"] == bug["weightPct"]


def test_bug_hunt_emphasis_weight_matches_published_percentage(built):
    emphasis = built["scores.json"]["bugHuntEmphasisRanking"]
    expected = round(75.0 * build_scores.BUG_HUNT_EMPHASIS_PRIORITY / emphasis["totalPriority"], 4)
    assert emphasis["benchmarkWeightPct"] == expected
    assert built["ranking_summary.json"]["bugHuntEmphasis"]["benchmarkWeightPct"] == expected
    assert built["coverage_matrix.json"]["externalBenchmarks"]["bugHunt"]["emphasisWeightPct"] == expected


def test_metric_coverage_percentage_and_renormalized_priority(built):
    models = built["scores.json"]["models"]
    weights = {w["key"]: w["priority"] for w in built["scores.json"]["weights"] if w["key"] != "costComposite"}
    total = sum(weights.values())
    partial = no_cost = 0
    for row in models:
        coverage = row["metricCoverage"]
        has_cost = "costComposite" in row["dims"]
        assert coverage["costAvailable"] is has_cost
        assert coverage["totalPriority"] == total
        assert coverage["availablePriority"] == sum(p for k, p in weights.items() if k in row["dims"])
        expected_coverage = (25.0 if has_cost else 0.0) + 75.0 * coverage["availablePriority"] / total
        assert coverage["coveragePct"] == round(expected_coverage, 2)
        if not row["rankingEligible"]:
            continue
        if coverage["missingKeys"]:
            partial += 1
            assert row["isMissing"] is True
        quality = [k for k in weights if k in row["dims"]]
        expected_q = sum(row["dims"][k] * weights[k] for k in quality) / sum(weights[k] for k in quality)
        assert row["qualityScore"] == round(expected_q, 1)
        if not has_cost:
            # AGENTS.md: a configuration without a cost gets no value score and no rank.
            no_cost += 1
            assert row["overallScore"] is None and row["rank"] is None and row["rankingStatus"] == "unranked_no_cost"
            continue
        # Cost carries exactly 25% whatever quality metrics are missing.
        assert row["overallScore"] == round(0.25 * row["dims"]["costComposite"] + 0.75 * expected_q, 1)
    assert partial > 0  # the committed data contains rows with missing metrics
    assert no_cost == 0  # O51: Muse Wonder Full, the one configuration AA published no cost for, is off the frontier


def test_ranked_order_and_exclusions(built):
    scores = built["scores.json"]
    ranked = [m for m in scores["models"] if m["rank"] is not None]
    assert [m["id"] for m in ranked] == scores["rankedModelIds"]
    assert [m["rank"] for m in ranked] == list(range(1, len(ranked) + 1))
    overall = [m["overallScore"] for m in ranked]
    assert overall == sorted(overall, reverse=True)
    assert all(m["rankingStatus"] == "ranked" for m in ranked)
    # O36: a cohort configuration without the full benchmark set after the logged search is listed, not ranked.
    # O53: it is excluded only when it lacks every ranking's set; each ranking lists the configurations it cannot rank.
    incomplete = [m for m in scores["models"] if m["rankingStatus"] == "excluded_incomplete_benchmarks"]
    listed = [{item["id"] for item in section["incompleteEvidence"]} for section in [scores["v3"], *scores["v3Tracks"].values()]]
    assert {m["id"] for m in incomplete} == set.intersection(*listed)
    for m in incomplete:
        assert not m["rankingEligible"] and m["rank"] is None and m["overallScore"] is None and m["costComposite"] is None
        assert not any(m["rankings"].values())
        assert m["rankingInclusionReasons"] and m["rankingExclusionReasons"][-1].startswith(
            "Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no ")
        assert "; AI Coding Daily ranking: no " in m["rankingExclusionReasons"][-1]
    ranked_somewhere = [m for m in scores["models"] if m.get("rankings") and any(m["rankings"].values())]
    assert ranked_somewhere and all(m["rankingEligible"] for m in ranked_somewhere)
    excluded = [m for m in scores["models"] if not m["rankingEligible"] and m not in incomplete]
    assert excluded
    for m in excluded:
        assert m["rank"] is None and m["overallScore"] is None and m["vRanks"] == {}
        assert m["rankingStatus"] == "excluded_from_primary_cohort"
        assert "Not plotted on or within the near gap of AA's rendered frontier (O51)" in m["rankingExclusionReasons"]
    assert {a["id"] for a in scores["appendixNonRanked"]} == {m["id"] for m in excluded}
    assert [m["name"] for m in scores["models"] if not m["rankingEligible"] and m not in incomplete] == sorted(m["name"] for m in excluded)


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


def test_cost_is_api_cost_per_index_point_on_a_log_scale(built):
    models = built["scores.json"]["models"]
    primary = [m for m in models if m["rankingEligible"] and m["aaEvalCost"] is not None]
    for m in models:
        if m["aaEvalCost"] is not None:
            assert m["aaCostPerIndexPoint"] == m["aaEvalCost"] / m["intelligenceIndex"]
        assert m["costComposite"] == (m["aaCostPerIndexPoint"] if m["rankingEligible"] else None)
    low = math.log(min(m["costComposite"] for m in primary))
    high = math.log(max(m["costComposite"] for m in primary))
    for m in primary:
        expected = 100 * (high - math.log(m["costComposite"])) / (high - low)
        assert m["dims"]["costComposite"] == round(expected, 1)
    assert max(m["dims"]["costComposite"] for m in primary) == 100.0
    assert min(m["dims"]["costComposite"] for m in primary) == 0.0
    assert built["scores.json"]["costMode"] == "aa-per-index-point"


DEEPSEEK_CLAIM = {"model": "DeepSeek V4 Flash", "benchmark": "Terminal-Bench 4.0", "sourceUrl": "https://api-docs.deepseek.com/updates/"}


def test_manifest_and_outputs_list_expected_relative_paths(world, capsys):
    run_main(world)
    printed = json.loads(capsys.readouterr().out)
    assert printed["outputs"] == ["data/scores.json", "data/coverage_matrix.json", "data/ranking_summary.json"]
    for relative in printed["outputs"]:
        assert (world / relative).is_file()
    manifest = json.loads((world / "data/run_manifest.json").read_text())
    scoring = manifest["scoring"]
    assert scoring["weights"] == json.loads((world / "data/scores.json").read_text())["weights"]
    assert scoring["observedAt"] == "2026-10-23T06:26:23Z"
    # O51: DeepSeek V4 Flash is off the frontier, so no committed claim targets a cohort configuration.
    assert scoring["providerClaimsUsed"] == []
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


def _mut_empty_aa(document):
    document["models"] = {}


CASES = [
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


def _capture_point_off_its_vertex(document):
    document["frontier"][0]["svg_x"] += 5


def _capture_path_falls(document):
    points = sorted(document["frontier"], key=lambda item: item["svg_x"])
    points[1]["svg_y"] = points[0]["svg_y"] + 1
    document["rendered_pareto_svg_path"] = "M " + " L ".join(f"{item['svg_x']} {item['svg_y']}" for item in points)


CAPTURE_CASES += [
    ("capture", _capture_point_off_its_vertex, "do not match the rendered Pareto path vertices"),
    ("capture", lambda d: d.update(rendered_pareto_svg_path=d["rendered_pareto_svg_path"].rsplit(" L ", 1)[0]), "do not match the rendered Pareto path vertices"),
    ("capture", lambda d: d.update(rendered_pareto_svg_path="M 1 2 Q 3 4"), "M/L coordinate pairs"),
    ("capture", lambda d: d.pop("rendered_pareto_svg_path"), "M/L coordinate pairs"),
    ("capture", _capture_path_falls, "does not rise strictly"),
    ("capture", lambda d: d["points"].append({**next(item for item in d["points"] if item["fallback"]), "model_name": "Twin", "fallback": None}),
     r"both with and without fallback \(a matching decision is required, E214\): Claude"),
    ("capture", lambda d: d["points"].append({**d["points"][0], "model_name": "Cheaper Model", "svg_x": min(item["svg_x"] for item in d["frontier"]) - 10}),
     r"left of the rendered Pareto path \(an owner decision is required, E204\): Cheaper Model"),
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


def test_non_positive_cost_is_rejected(world):
    edit(world, "aa", lambda d: d["models"]["gpt-6.1-sol"]["metrics"].update(aaEvalCost=0))
    with pytest.raises(ValueError, match="AA evaluation cost must be positive: gpt-6.1-sol"):
        run_main(world)


# --------------------------------------------------------------------------
# alternative scoring scenarios
# --------------------------------------------------------------------------


def unmatch_all_bug_hunt(document):
    for model in document["models"]:
        model["matched"] = False


def defer_near_family(family):
    def fn(document):
        for row in document["nearFrontierRows"]:
            if row["family"] == family:
                row["requiredFamilyModelId"] = None
    return fn


def test_without_bug_hunt_every_configuration_needs_a_logged_search(world):
    """O36: Bug Hunt is a required leaf, so with no match anywhere the build refuses until each gap's search is logged."""

    edit(world, "bughunt", unmatch_all_bug_hunt)
    edit(world, "scoreboard", lambda d: d["rows"].clear())
    edit(world, "inventory", defer_near_family("GPT-5.6 Luna"))
    edit(world, "inventory", defer_near_family("GPT-6 Astra"))
    with pytest.raises(ValueError, match=r"no exhaustive search for bugHunt logged within 7 days of the cutoff \(O36\)"):
        run_main(world)


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
    assert reasons[-1] == "Not plotted on or within the near gap of AA's rendered frontier (O51)"


def test_missing_owner_result_has_plain_exclusion_reason(world):
    run_main(world)
    assert exclusion_reasons(world)[:2] == [
        "No eligible exact-model Bug Hunt result in the selected source snapshot",
        "Not plotted on or within the near gap of AA's rendered frontier (O51)",
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
    assert rows["gpt-6.1-sol"]["aaCostPerIndexPoint"] is None
    assert "costComposite" in rows["gpt-6.1-sol"]["metricCoverage"]["missingKeys"]
    assert rows["gpt-6.1-sol"]["metricCoverage"]["costAvailable"] is False
    # without a cost the row has no value score and no rank (AGENTS.md); its quality still stands
    assert rows["gpt-6.1-sol"]["overallScore"] is None and rows["gpt-6.1-sol"]["qualityScore"] is not None
    assert rows["gpt-6.1-sol"]["rank"] is None and rows["gpt-6.1-sol"]["rankingStatus"] == "unranked_no_cost"
    assert rows["gpt-6.1-sol"]["bugHuntEmphasisRank"] is None
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
# near-frontier policy: pure helpers
# --------------------------------------------------------------------------

AA_URL = "https://artificialanalysis.ai/models/"


def near_inv(slug="near-a", family="Fam A", required="fam-a", gap=2, variant="medium", **extra):
    row = {"aaId": slug, "name": f"{family} ({variant})", "evaluatedVariant": variant, "intelligenceIndex": 50,
           "totalCostUsd": 12.5, "intelligenceGap": gap, "costRatio": 1.5, "nearestFrontierAaId": "front-a",
           "directlyObservedFrontier": False, "sourceUrl": AA_URL + slug, "family": family,
           "requiredFamilyModelId": required, "sourceFootnote": None}
    row.update(extra)
    return row


def near_cap(row, **extra):
    capture = {"model_name": row["name"], "family": row["family"],
               "effort": build_scores.frontier_effort(row["evaluatedVariant"]), "fallback": None, "url": row["sourceUrl"],
               "intelligence_index_display": row["intelligenceIndex"], "total_cost_usd": row["totalCostUsd"],
               "intelligence_gap": row["intelligenceGap"]}
    capture.update(extra)
    return capture


def near_docs(rows=None, caps=None):
    rows = [near_inv()] if rows is None else rows
    caps = [near_cap(row) for row in rows] if caps is None else caps
    inventory = {"nearFrontierRows": rows, "nearFrontierPolicy": {"maxIntelligenceGap": 3, "basis": "b", "text": "t"},
                 "sourceUniverse": {"nearFrontierPointN": len(rows)}}
    capture = {"near_frontier": caps, "near_frontier_policy": {"max_intelligence_gap": 3},
               "universe": {"near_frontier_points": len(caps)}}
    return inventory, capture


AA_MODELS = {"fam-a": {"displayName": "Fam A"}, "fam-b": {"displayName": "Fam B"}}


def select(inventory, capture, frontier_urls=(), frontier_ids=None, aa_models=AA_MODELS):
    return build_scores.near_frontier_selection(inventory, capture, set(frontier_urls), frontier_ids or {}, aa_models)


def test_near_selection_groups_rows_by_family_and_allows_deferred_ids():
    rows = [near_inv(), near_inv("near-a2", variant="high", gap=1),
            near_inv("near-d", family="Phantom", required=None, variant="low")]
    selection = select(*near_docs(rows))
    assert list(selection) == ["Fam A", "Phantom"]
    assert selection["Fam A"] == {"modelId": "fam-a", "rows": rows[:2]}
    assert selection["Phantom"] == {"modelId": None, "rows": rows[2:]}


def test_near_selection_accepts_fallback_variants_and_consistent_frontier_family():
    row = near_inv(variant="high with fallback")
    inventory, capture = near_docs([row], [near_cap(row, effort="high", fallback="with fallback")])
    assert select(inventory, capture, frontier_ids={"Fam A": {"fam-a"}})["Fam A"]["modelId"] == "fam-a"
    capture["near_frontier"][0]["fallback"] = True
    assert "Fam A" in select(inventory, capture)


def test_near_selection_with_no_rows_is_empty():
    assert select(*near_docs([])) == {}


def _drop(container, key):
    def fn(inventory, capture):
        del {"inventory": inventory, "capture": capture}[container][key]
    return fn


@pytest.mark.parametrize("mutation", [
    _drop("inventory", "nearFrontierRows"), _drop("inventory", "nearFrontierPolicy"),
    _drop("capture", "near_frontier"), _drop("capture", "near_frontier_policy"),
    lambda inventory, capture: inventory.update(nearFrontierPolicy="text"),
    lambda inventory, capture: capture.update(near_frontier="rows"),
])
def test_near_selection_requires_policy_and_rows_on_both_sides(mutation):
    inventory, capture = near_docs()
    mutation(inventory, capture)
    with pytest.raises(ValueError, match="must carry the near-frontier policy and rows"):
        select(inventory, capture)


@pytest.mark.parametrize("mutation", [
    lambda inventory, capture: inventory["sourceUniverse"].update(nearFrontierPointN=2),
    lambda inventory, capture: inventory["sourceUniverse"].pop("nearFrontierPointN"),
    lambda inventory, capture: capture["universe"].update(near_frontier_points=2),
    lambda inventory, capture: inventory["nearFrontierRows"].append(near_inv("extra")),
    lambda inventory, capture: capture["near_frontier"].pop(),
])
def test_near_selection_counts_must_reconcile(mutation):
    inventory, capture = near_docs()
    mutation(inventory, capture)
    with pytest.raises(ValueError, match="near-frontier point counts do not reconcile"):
        select(inventory, capture)


@pytest.mark.parametrize("gap", [4, None])
def test_near_selection_policy_gap_must_match_capture(gap):
    inventory, capture = near_docs()
    capture["near_frontier_policy"]["max_intelligence_gap"] = gap
    with pytest.raises(ValueError, match="near-frontier policy differs"):
        select(inventory, capture)


def test_near_selection_policy_gap_must_be_declared():
    inventory, capture = near_docs()
    del inventory["nearFrontierPolicy"]["maxIntelligenceGap"]
    del capture["near_frontier_policy"]["max_intelligence_gap"]
    with pytest.raises(ValueError, match="near-frontier policy differs"):
        select(inventory, capture)


@pytest.mark.parametrize("change", [
    {"family": ""}, {"family": None}, {"sourceUrl": ""}, {"directlyObservedFrontier": True},
    {"directlyObservedFrontier": None}, {"requiredFamilyModelId": ""}, {"requiredFamilyModelId": 5},
])
def test_near_rows_must_carry_family_url_flag_and_id(change):
    row = near_inv(**change)
    with pytest.raises(ValueError, match="near-frontier inventory row must carry"):
        select(*near_docs([row], [near_cap(near_inv())]))


def test_near_row_without_required_id_key_is_rejected():
    row = near_inv()
    del row["requiredFamilyModelId"]
    with pytest.raises(ValueError, match="near-frontier inventory row must carry"):
        select(*near_docs([row], [near_cap(near_inv())]))


def test_near_urls_must_be_unique_across_near_and_frontier_rows():
    twin = near_inv("near-b", sourceUrl=AA_URL + "near-a")
    with pytest.raises(ValueError, match="duplicate owner URL: " + AA_URL + "near-a"):
        select(*near_docs([near_inv(), twin], [near_cap(near_inv()), near_cap(twin)]))
    with pytest.raises(ValueError, match="duplicate owner URL"):
        select(*near_docs(), frontier_urls={AA_URL + "near-a"})


@pytest.mark.parametrize("change", [
    {"model_name": "Other"}, {"family": "Other"}, {"effort": "low"}, {"fallback": "with fallback"},
    {"intelligence_index_display": 51}, {"total_cost_usd": 12.6}, {"intelligence_gap": 1}, {"url": AA_URL + "elsewhere"},
])
def test_near_rows_must_match_their_capture_rows(change):
    row = near_inv()
    with pytest.raises(ValueError, match="near-frontier row is inconsistent with its current frontier capture: " + AA_URL + "near-a"):
        select(*near_docs([row], [near_cap(row, **change)]))


def test_near_row_missing_fallback_in_inventory_is_rejected():
    row = near_inv(variant="high with fallback")
    with pytest.raises(ValueError, match="inconsistent with its current frontier capture"):
        select(*near_docs([row], [near_cap(row, effort="high", fallback=None)]))


def test_near_cost_must_be_numeric_in_the_capture():
    row = near_inv()
    with pytest.raises(ValueError, match="non-numeric required value"):
        select(*near_docs([row], [near_cap(row, total_cost_usd="12.5")]))


def test_near_family_ids_must_be_consistent_and_agree_with_the_frontier():
    rows = [near_inv(), near_inv("near-a2", variant="high", required="fam-b")]
    with pytest.raises(ValueError, match="inconsistent required model IDs: Fam A"):
        select(*near_docs(rows))
    mixed = [near_inv(), near_inv("near-a2", variant="high", required=None)]
    with pytest.raises(ValueError, match="inconsistent required model IDs: Fam A"):
        select(*near_docs(mixed))
    for frontier_id in ("fam-b", None):
        with pytest.raises(ValueError, match="disagrees with its frontier model ID: Fam A"):
            select(*near_docs(), frontier_ids={"Fam A": {frontier_id}})


def test_near_family_model_must_exist_in_roster_with_matching_display_name():
    with pytest.raises(ValueError, match="absent from the selected AA metrics roster: fam-a"):
        select(*near_docs(), aa_models={})
    with pytest.raises(ValueError, match="does not match selected catalog identity for fam-a"):
        select(*near_docs(), aa_models={"fam-a": {"displayName": "Fam B"}})


def test_near_row_errors_precede_family_roster_errors():
    with pytest.raises(ValueError, match="near-frontier row is inconsistent"):
        select(*near_docs([near_inv()], [near_cap(near_inv(), model_name="x")]), aa_models={})


# --------------------------------------------------------------------------
# frontier tiers: per-family annotations and summary rows
# --------------------------------------------------------------------------


def front(name, intelligence, cost, family="Fam A", model_id="fam-a", note=None):
    return {"name": name, "intelligenceIndex": intelligence, "totalCostUsd": cost, "family": family,
            "requiredFamilyModelId": model_id, "sourceFootnote": note}


def test_frontier_tiers_pick_the_highest_intelligence_frontier_configuration():
    """E193: on a rounded-Index tie the dearer point is the higher one, because the rendered line rises strictly (E195)."""

    frontier = {"Fam A": [front("A low", 20, 5), front("A max", 40, 90, note="higher on the line"),
                          front("A high", 40, 80, note="cheaper tie")]}
    annotations, frontier_families, near_families = build_scores.frontier_tiers(frontier, {})
    assert annotations == {"Fam A": {"tier": "frontier", "configuration": "A max", "intelligenceGap": 0,
                                     "footnote": "higher on the line"}}
    assert frontier_families == [{"family": "Fam A", "modelId": "fam-a", "configuration": "A max"}]
    assert near_families == []


def test_frontier_tiers_break_exact_frontier_ties_by_name():
    frontier = {"F": [front("F b", 30, 10, "F", "f"), front("F a", 30, 10, "F", "f")]}
    assert build_scores.frontier_tiers(frontier, {})[0]["F"]["configuration"] == "F a"


def test_frontier_tiers_pick_the_smallest_gap_near_configuration():
    near = {"Fam B": {"modelId": "fam-b", "rows": [
        near_inv("b1", "Fam B", "fam-b", gap=2, sourceFootnote="note b1"),
        near_inv("b2", "Fam B", "fam-b", gap=1, totalCostUsd=30.0, sourceFootnote="note b2"),
        near_inv("b3", "Fam B", "fam-b", gap=1, totalCostUsd=20.0, sourceFootnote="note b3"),
        near_inv("b4", "Fam B", "fam-b", gap=1, totalCostUsd=20.0, variant="low", sourceFootnote=None)]}}
    annotations, frontier_families, near_families = build_scores.frontier_tiers({}, near)
    assert annotations == {"Fam B": {"tier": "near", "configuration": "Fam B (low)",
                                     "intelligenceGap": 1, "footnote": None}}
    assert frontier_families == []
    assert near_families == [{"family": "Fam B", "modelId": "fam-b", "configuration": "Fam B (low)", "intelligenceGap": 1}]


def test_frontier_tiers_prefer_frontier_over_near_and_sort_families():
    frontier = {"Zed": [front("Zed top", 60, 100, "Zed", "zed")], "Fam A": [front("A top", 40, 80)]}
    near = {"Fam A": {"modelId": "fam-a", "rows": [near_inv(gap=3)]},
            "Phantom": {"modelId": None, "rows": [near_inv("p", "Phantom", None, gap=0)]},
            "Beta": {"modelId": "beta", "rows": [near_inv("b", "Beta", "beta", gap=1, sourceFootnote="b note")]}}
    annotations, frontier_families, near_families = build_scores.frontier_tiers(frontier, near)
    assert annotations["Fam A"]["tier"] == "frontier" and annotations["Fam A"]["configuration"] == "A top"
    assert annotations["Beta"] == {"tier": "near", "configuration": "Beta (medium)", "intelligenceGap": 1, "footnote": "b note"}
    assert annotations["Phantom"]["tier"] == "near"
    assert [item["family"] for item in frontier_families] == ["Fam A", "Zed"]
    assert near_families == [
        {"family": "Beta", "modelId": "beta", "configuration": "Beta (medium)", "intelligenceGap": 1},
        {"family": "Fam A", "modelId": "fam-a", "configuration": "Fam A (medium)", "intelligenceGap": 3},
        {"family": "Phantom", "modelId": None, "configuration": "Phantom (medium)", "intelligenceGap": 0}]


def test_frontier_tiers_with_nothing_is_empty():
    assert build_scores.frontier_tiers({}, {}) == ({}, [], [])


# --------------------------------------------------------------------------
# near-frontier policy: pipeline integration on the copied data
# --------------------------------------------------------------------------


def _inv_no_near_rows(document):
    del document["nearFrontierRows"]


def _inv_near_count(document):
    document["sourceUniverse"]["nearFrontierPointN"] += 1


def _inv_near_policy_gap(document):
    document["nearFrontierPolicy"]["maxIntelligenceGap"] = 99


def _inv_near_flag(document):
    document["nearFrontierRows"][0]["directlyObservedFrontier"] = True


def _inv_near_cost(document):
    document["nearFrontierRows"][0]["totalCostUsd"] += 5


def _inv_near_gap(document):
    document["nearFrontierRows"][0]["intelligenceGap"] += 1


def _inv_near_duplicate(document):
    document["nearFrontierRows"][1]["sourceUrl"] = document["nearFrontierRows"][0]["sourceUrl"]


def _inv_near_frontier_url(document):
    document["nearFrontierRows"][0]["sourceUrl"] = document["rows"][0]["sourceUrl"]


NEAR_INVENTORY_CASES = [
    (_inv_no_near_rows, "must carry the near-frontier policy and rows"),
    (_inv_near_count, "near-frontier point counts do not reconcile"),
    (_inv_near_policy_gap, "near-frontier policy differs"),
    (_inv_near_flag, "near-frontier inventory row must carry"),
    (_inv_near_cost, "near-frontier row is inconsistent with its current frontier capture"),
    (_inv_near_gap, "near-frontier row is inconsistent with its current frontier capture"),
    (_inv_near_duplicate, "near-frontier inventory has a duplicate owner URL"),
    (_inv_near_frontier_url, "near-frontier inventory has a duplicate owner URL"),
]


@pytest.mark.parametrize(("mutation", "message"), NEAR_INVENTORY_CASES)
def test_near_inventory_rows_are_validated(world, mutation, message):
    edit(world, "inventory", mutation)
    with pytest.raises(ValueError, match=message):
        run_main(world)


@pytest.mark.parametrize("mutation", [
    lambda d: d.pop("near_frontier"), lambda d: d.pop("near_frontier_policy"),
    lambda d: d["universe"].update(near_frontier_points=0),
    lambda d: d["near_frontier_policy"].update(max_intelligence_gap=1),
])
def test_near_capture_must_match_inventory(world, mutation):
    edit(world, "capture", mutation)
    with pytest.raises(ValueError, match="near-frontier"):
        run_main(world)


def add_near_family(root: Path, *, family: str, model_id, slug: str, gap: int = 1) -> str:
    """Append a consistent synthetic near-frontier row for ``family`` to the copied inventory and capture."""

    inventory_path, capture_path = root / FILES["inventory"], root / FILES["capture"]
    inventory, capture = json.loads(inventory_path.read_text()), json.loads(capture_path.read_text())
    url = AA_URL + slug
    row = {"aaId": slug, "name": f"{family} (medium)", "evaluatedVariant": "medium", "intelligenceIndex": 40,
           "totalCostUsd": 10.0, "intelligenceGap": gap, "costRatio": 1.1,
           "nearestFrontierAaId": inventory["rows"][0]["aaId"], "directlyObservedFrontier": False, "sourceUrl": url,
           "family": family, "requiredFamilyModelId": model_id, "sourceFootnote": f"note for {slug}"}
    inventory["nearFrontierRows"].append(row)
    inventory["sourceUniverse"]["nearFrontierPointN"] += 1
    capture["near_frontier"].append(near_cap(row, fallback=None))
    capture["universe"]["near_frontier_points"] += 1
    inventory_path.write_text(json.dumps(inventory))
    capture_path.write_text(json.dumps(capture))
    return url


def model_rows(root: Path) -> dict:
    return {m["id"]: m for m in outputs(root)["scores.json"]["models"]}


def test_every_model_row_reports_its_aa_frontier_tier(world):
    run_main(world)
    inventory = json.loads((world / FILES["inventory"]).read_text())
    best_near = {}
    for row in inventory["nearFrontierRows"]:
        key = (row["intelligenceGap"], row["totalCostUsd"], row["name"])
        if row["family"] not in best_near or key < best_near[row["family"]][0]:
            best_near[row["family"]] = (key, row)
    best_front = {}
    for row in inventory["rows"]:
        key = (-row["intelligenceIndex"], -row["totalCostUsd"], row["name"])
        if row["family"] not in best_front or key < best_front[row["family"]][0]:
            best_front[row["family"]] = (key, row)
    # O33: the family annotation goes to the family's primary configuration; a sibling reports its own plotted point.
    primary = {row["family"]: row["requiredFamilyModelId"] for row in inventory["rows"] + inventory["nearFrontierRows"]}
    own = {row["sourceUrl"]: ("near", row["name"], row["intelligenceGap"], row.get("sourceFootnote")) for row in inventory["nearFrontierRows"]}
    own.update({row["sourceUrl"]: ("frontier", row["name"], 0, row.get("sourceFootnote")) for row in inventory["rows"]})
    seen_tiers, sibling_tiers = set(), set()
    for model in outputs(world)["scores.json"]["models"]:
        family = model["family"]
        if primary.get(family) != model["id"]:
            want = own.get(model["aaUrl"], (None, None, None, None))
            if family in primary:
                sibling_tiers.add(want[0])
        elif family in best_front:
            row = best_front[family][1]
            want = ("frontier", row["name"], 0, row.get("sourceFootnote"))
        else:
            row = best_near[family][1]
            want = ("near", row["name"], row["intelligenceGap"], row.get("sourceFootnote"))
        got = (model["aaFrontierTier"], model["aaFrontierConfiguration"], model["aaFrontierIntelligenceGap"],
               model["aaFrontierFootnote"])
        assert got == want, family
        seen_tiers.add(want[0])
        assert "frontierSelection" in model  # existing field untouched
    assert seen_tiers == {"frontier", "near", None}
    assert sibling_tiers == {"frontier", "near", None}  # e.g. GPT-6.1 Sol (xhigh), Claude Haiku 5.5 (max), GPT-6.1 Sol (low)
    rows = model_rows(world)
    # O51: a plotted sibling enters the cohort on its own point; an unplotted one (GPT-6.1 Sol (low)) does not.
    assert rows["claude-haiku-5-5-low"]["rankingInclusionReasons"] == ["Plotted on or within the near gap of AA's rendered frontier (O51)"]
    assert rows["claude-haiku-5-5-low"]["frontierSelection"] is None and rows["claude-haiku-5-5-low"]["family"] == "Claude Haiku 5.5"
    assert rows["gpt-6.1-sol-low"]["rankingInclusionReasons"] == [] and rows["gpt-6.1-sol-low"]["rankingEligible"] is False


def test_footnote_of_the_best_configuration_is_passed_through(world):
    def notes(document):
        for row in document["rows"]:
            row["sourceFootnote"] = "note " + row["aaId"]
    edit(world, "inventory", notes)
    run_main(world)
    inventory = json.loads((world / FILES["inventory"]).read_text())
    luna = [r for r in inventory["rows"] if r["family"] == "GPT-6 Luna"]
    best = max(luna, key=lambda r: (r["intelligenceIndex"], -r["totalCostUsd"]))
    assert model_rows(world)["gpt-6-luna"]["aaFrontierFootnote"] == "note " + best["aaId"]
    assert model_rows(world)["gpt-6-luna"]["aaFrontierConfiguration"] == best["name"]


def test_frontier_selection_summarises_near_families(world):
    run_main(world)
    out = outputs(world)
    selection = out["ranking_summary.json"]["frontierSelection"]
    inventory = json.loads((world / FILES["inventory"]).read_text())
    near_families = {r["family"]: r["requiredFamilyModelId"] for r in inventory["nearFrontierRows"]}
    assert selection["nearFrontierPolicy"] == inventory["nearFrontierPolicy"]
    assert selection["nearFrontierPointN"] == len(inventory["nearFrontierRows"])
    assert selection["nearFrontierFamilyN"] == len(near_families)
    assert selection["nearFrontierRequiredModelN"] == len({v for v in near_families.values() if v})
    assert selection["nearFrontierDeferredN"] == sum(v is None for v in near_families.values())
    assert [(f["family"], f["modelId"]) for f in selection["nearFrontierFamilies"]] == sorted(near_families.items())
    assert all(set(f) == {"family", "modelId", "configuration", "intelligenceGap"} for f in selection["nearFrontierFamilies"])
    assert [f["family"] for f in selection["frontierFamilies"]] == sorted({r["family"] for r in inventory["rows"]})
    assert all(set(f) == {"family", "modelId", "configuration"} for f in selection["frontierFamilies"])
    assert selection["familyN"] == len(selection["frontierFamilies"])
    assert out["scores.json"]["frontierSelection"] == selection == out["coverage_matrix.json"]["frontierSelection"]


def test_near_family_without_overlap_coverage_still_ranks(world):
    run_main(world)
    base = outputs(world)
    # gpt-5.5 is not plotted on or near the frontier: excluded until it becomes a near family (O51).
    assert model_rows(world)["gpt-5.5"]["rankingEligible"] is False
    base_frontier_n = base["scores.json"]["cohort"]["frontierRequiredModelN"]
    base_cohort_n = base["scores.json"]["cohort"]["n"]
    add_near_family(world, family="GPT-5.5", model_id="gpt-5.5", slug="gpt-5-5")
    # O36: without Bug Hunt the near family enters the cohort but is listed, not ranked, once its search is logged.
    with pytest.raises(ValueError, match=r"gpt-5.5: no exhaustive search for (bugHunt|frontierCode|vibeCode|aiCodingDaily)"):
        run_main(world)
    edit(world, "leaves", log_searches("gpt-5.5"))
    run_main(world)
    out = outputs(world)
    model = model_rows(world)["gpt-5.5"]
    assert model["rankingEligible"] is False and model["rank"] is None and model["rankingStatus"] == "excluded_incomplete_benchmarks"
    assert model["rankingInclusionReasons"] == [
        "Near-frontier AA family (within 3 Index points of the rendered frontier)"]
    assert model["rankingExclusionReasons"] == [
        "Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no FrontierCode 1.1, Bug Hunt Bench, Vibe Code Bench v1.1 (Vals), "
        "Code Migration v1.1 (Vals), LiveBench 2.0 Long Agentic, LiveBench 2.0 Coding; AI Coding Daily ranking: no FrontierCode 1.1, Bug Hunt Bench, "
        "AI Coding Daily (excl. bug finding)"]
    assert (model["aaFrontierTier"], model["aaFrontierConfiguration"], model["aaFrontierIntelligenceGap"]) == ("near", "GPT-5.5 (medium)", 1)
    assert model["aaFrontierFootnote"] == "note for gpt-5-5"
    assert out["scores.json"]["cohort"]["n"] == base_cohort_n + 1
    assert out["scores.json"]["cohort"]["frontierRequiredModelN"] == base_frontier_n
    assert out["ranking_summary.json"]["frontierRequiredModelN"] == base_frontier_n
    assert out["ranking_summary.json"]["frontierSelection"]["nearFrontierRequiredModelN"] == \
        base["ranking_summary.json"]["frontierSelection"]["nearFrontierRequiredModelN"] + 1


def test_frontier_family_that_is_also_near_keeps_only_the_frontier_inclusion_reason(world):
    run_main(world)
    inventory = json.loads((world / FILES["inventory"]).read_text())
    both = {r["family"] for r in inventory["rows"]} & {r["family"] for r in inventory["nearFrontierRows"]}
    assert both
    names = {m["name"]: m for m in model_rows(world).values()}
    for family in both:
        reasons = names[family]["rankingInclusionReasons"]
        assert "Required AA Intelligence Index versus total-evaluation-cost frontier family" in reasons
        assert not any(reason.startswith("Near-frontier AA family") for reason in reasons)


def test_a_frontier_family_must_rank_its_highest_rendered_frontier_point(world):
    """E193: a catalog that tracks a lower frontier point of a frontier family fails the build."""

    def fn(document):
        document["models"]["claude-haiku-5-5"].update(
            aaUrl=AA_URL + "claude-haiku-5-5-high", aaSlug="claude-haiku-5-5-high", aaVariant="high")
    edit(world, "aa", fn)
    with pytest.raises(ValueError, match=r"must rank its highest rendered-frontier point \(E193\): Claude Haiku 5.5"):
        run_main(world)


def test_a_near_family_must_rank_its_smallest_gap_near_point(world):
    """E193/O51: a near family's primary configuration is its smallest-gap near point, not another tracked configuration."""

    add_near_family(world, family="GPT-5.5", model_id="gpt-5.5", slug="synthetic-gpt-5-5")
    with pytest.raises(ValueError, match=r"must rank its smallest-gap near point as its primary configuration \(E193, O51\): GPT-5.5"):
        run_main(world)


def add_sibling(root: Path, monkeypatch, source_id: str, new_id: str, display: str) -> None:
    """Clone a roster configuration under a new id and display name (an O33 sibling of the same family)."""

    def aa(document):
        document["models"][new_id] = {**document["models"][source_id], "id": new_id, "displayName": display}
    def bughunt(document):
        document["models"].append({**next(m for m in document["models"] if m["modelId"] == source_id), "modelId": new_id})
    def livebench(document):
        document["models"][new_id] = {**document["models"][source_id], "modelId": new_id, "name": display}
    def deepswe(document):
        for item in document["configurations"]:
            if item["valueRankModelId"] == source_id:
                item["valueRankModelId"] = new_id
    for name, fn in (("aa", aa), ("bughunt", bughunt), ("livebench", livebench), ("deepswe", deepswe)):
        edit(root, name, fn)
    monkeypatch.setitem(build_scores.DEVELOPER, display, "Test")
    monkeypatch.setitem(build_scores.SHORT, display, display)


def test_the_cohort_is_every_plotted_frontier_and_near_configuration(world):
    """O51: every rostered configuration AA plots on its rendered frontier or within the near gap is a cohort row, each
    effort its own row; an off-frontier roster entry (Muse Spark 1.3, formerly retained under O31/O33) is not."""

    run_main(world)
    inventory = json.loads((world / FILES["inventory"]).read_text())
    plotted = {row["sourceUrl"] for row in inventory["rows"] + inventory["nearFrontierRows"]}
    for model in model_rows(world).values():
        assert bool(model["rankingInclusionReasons"]) is (model["aaUrl"] in plotted), model["id"]
    rows = model_rows(world)
    assert rows["muse-spark-1-3"]["rankingStatus"] == "excluded_from_primary_cohort"
    # O53: a cohort row is ranked in each ranking whose full set it has, and listed when it has none.
    assert rows["claude-opus-5-5-high"]["rankingEligible"] is True and rows["claude-opus-5-5-high"]["rankings"] == {"max": False, "aicd": True}
    assert rows["gpt-6.1-sol"]["rankings"] == {"max": True, "aicd": False}
    assert rows["gpt-6-luna-low"]["rankingInclusionReasons"] and rows["gpt-6-luna-low"]["rankingStatus"] == "excluded_incomplete_benchmarks"


def test_roster_display_names_must_be_unique(world):
    edit(world, "aa", lambda d: d["models"]["gpt-6.1-sol-low"].update(displayName="GPT-6.1 Sol (high)"))
    with pytest.raises(ValueError, match=r"display names must be unique"):
        run_main(world)


def test_a_bug_hunt_result_at_another_effort_is_not_used():
    record = {"matched": True, "effort": "max", "fixedOf105": 45.0}
    assert build_scores.exact_bug_hunt("gpt-6-astra", "max", record) is record
    moved = build_scores.exact_bug_hunt("gpt-6-astra", "xhigh", record)
    assert moved["matched"] is False and moved["matchStatus"] == "effort_mismatch" and "No result is transferred" in moved["note"]


def test_bug_hunt_selection_is_the_largest_sample_result_at_the_exact_effort():
    """E206: the owner's largest-sample result over every harness at the configuration's effort, unless a reason is recorded."""

    model = {"displayName": "GPT-6 Astra", "aaVariant": "max"}
    rows = [{"model": "GPT-6 Astra (max effort)", "fixedOf105": 40.0}, {"model": "GPT-6 Astra (max effort) - mean of 3", "fixedOf105": 45.0},
            {"model": "GPT-6 Astra (xhigh effort) - mean of 5", "fixedOf105": 41.0}, {"model": "Other Model (max effort) - mean of 9", "fixedOf105": 1.0}]
    record = {"matched": True, "sampleN": 3, "fixedOf105": 45.0}
    assert build_scores.check_bug_hunt_selection("gpt-6-astra", model, record, rows) is None
    for wrong in ({"sampleN": 1, "fixedOf105": 40.0}, {"sampleN": 3, "fixedOf105": 44.0}):
        with pytest.raises(ValueError, match=r"largest-sample result at its effort .*\(E206\)"):
            build_scores.check_bug_hunt_selection("gpt-6-astra", model, {**record, **wrong}, rows)
    assert build_scores.check_bug_hunt_selection("gpt-6-astra", model, {**record, "sampleN": 1, "selectionReason": "reasoning state asserted"}, rows) is None
    assert build_scores.check_bug_hunt_selection("gpt-6-astra", model, {**record, "matched": False, "sampleN": 1}, rows) is None
    assert build_scores.check_bug_hunt_selection("gpt-6-astra", {**model, "aaVariant": "low"}, {**record, "sampleN": 1}, rows) is None  # no candidate
    assert build_scores.scoreboard_sample("X (max effort) - mean of 12") == 12 and build_scores.scoreboard_sample("X (max effort)") == 1


def test_bug_hunt_cross_harness_lists_each_harness_at_the_exact_effort():
    """E224: the largest-sample result per harness, only when two or more harnesses report the configuration's effort."""

    model = {"displayName": "Gemini 4 Argon", "aaVariant": "high"}
    rows = [{"model": "Gemini 4 Argon (high effort)", "harness": "Gemini CLI", "fixedOf105": 33.0},
            {"model": "Gemini 4 Argon (high effort, Antigravity CLI)", "harness": "Antigravity CLI", "fixedOf105": 41.0},
            {"model": "Gemini 4 Argon (high effort, Antigravity CLI) - mean of 3", "harness": "Antigravity CLI", "fixedOf105": 40.7},
            {"model": "Gemini 4 Argon (high effort, Antigravity CLI) - mean of 2", "harness": "Antigravity CLI", "fixedOf105": 39.0},
            {"model": "Gemini 4 Argon (low effort, Antigravity CLI)", "harness": "Antigravity CLI", "fixedOf105": 32.0}]
    assert build_scores.bug_hunt_cross_harness("gemini-4-argon", model, rows) == [
        {"harness": "Antigravity CLI", "fixedOf105": 40.7, "runs": 3}, {"harness": "Gemini CLI", "fixedOf105": 33.0, "runs": 1}]
    assert build_scores.bug_hunt_cross_harness("gemini-4-argon", {**model, "aaVariant": "low"}, rows) is None


def test_the_build_rejects_a_bug_hunt_record_that_is_not_the_largest_sample(world):
    edit(world, "bughunt", lambda d: next(item for item in d["models"] if item["modelId"] == "gpt-6-astra").update(sampleN=1))
    with pytest.raises(ValueError, match=r"gpt-6-astra is not the owner's largest-sample result"):
        run_main(world)


def test_deferred_near_family_counts_but_adds_no_ranked_model(world):
    run_main(world)
    base = outputs(world)
    add_near_family(world, family="Phantom Family", model_id=None, slug="synthetic-phantom", gap=0)
    run_main(world)
    out = outputs(world)
    selection = out["ranking_summary.json"]["frontierSelection"]
    before = base["ranking_summary.json"]["frontierSelection"]
    assert selection["nearFrontierDeferredN"] == before["nearFrontierDeferredN"] + 1
    assert selection["nearFrontierFamilyN"] == before["nearFrontierFamilyN"] + 1
    assert selection["nearFrontierRequiredModelN"] == before["nearFrontierRequiredModelN"]
    assert out["scores.json"]["cohort"]["n"] == base["scores.json"]["cohort"]["n"]
    assert {"family": "Phantom Family", "modelId": None, "configuration": "Phantom Family (medium)",
            "intelligenceGap": 0} in selection["nearFrontierFamilies"]


def test_near_family_with_unknown_roster_model_is_rejected(world):
    add_near_family(world, family="Ghost Family", model_id="ghost-model", slug="synthetic-ghost")
    with pytest.raises(ValueError, match="near-frontier family model is absent from the selected AA metrics roster: ghost-model"):
        run_main(world)


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


def test_frontier_family_diagnostics_use_only_frontier_and_near_frontier_rows():
    """E187/O51: build_scores hands each row's frontier-family flag to the v3 engine; since O51 every cohort row is plotted."""

    from valuerank import value_v3

    scores = json.loads((ROOT / "data" / "scores.json").read_text())
    family = {row["id"] for row in scores["models"] if row["rankingEligible"] and value_v3.configuration(row)["frontierFamily"]}
    retained = {row["id"] for row in scores["models"] if row["rankingEligible"]} - family
    assert retained == set()
    frontier = scores["v3"]["diagnostics"]["frontierAnchors"]
    assert frontier["references"] and set(frontier["references"]) <= family
    assert set(frontier["bar"]["population"]) <= family and frontier["bar"]["bar"]["id"] == value_v3.POLICY_BAR_ID


def test_the_legacy_composite_takes_terminal_bench_only_at_the_configurations_effort(world):
    """AGENTS.md: Claude Opus 5 is ranked at max, but tbench.ai lists Opus 5 at xhigh, so it gets no legacy value."""

    run_main(world)
    rows = model_rows(world)
    assert rows["claude-opus-5"]["terminalBenchV4"] is None and rows["claude-opus-5"]["terminalBenchV4Effort"] is None
    assert rows["gpt-6-astra"]["terminalBenchV4"] == pytest.approx(0.582)  # GPT-6 Astra (max) is exact
