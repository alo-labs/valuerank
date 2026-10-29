"""Contract tests for the page shapes the templates and scripts read (docs/site-data-contract.md)."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from valuerank.paths import DATA
from valuerank.site import export, viewmodel


@pytest.fixture(scope="module")
def data(tmp_path_factory) -> Path:
    target = tmp_path_factory.mktemp("pages") / "data"
    target.mkdir()
    for source in DATA.glob("*.json"):
        shutil.copy2(source, target / source.name)
    return target


@pytest.fixture(scope="module")
def bundle(data):
    return viewmodel.build_bundle(data)


def test_livebench_document_lists_matched_rows_with_frontier_flags(bundle, data):
    source = json.loads((data / "livebench.json").read_text())
    doc = bundle.livebench
    assert doc["release"] == source["release"] and doc["observedAt"] == source["observedAt"]
    rows = doc["rows"]
    assert {"id", "name", "livebenchModel", "overallScore", "instructionFollowingScore", "costPerSuccessfulTaskUsd", "pareto"} <= set(rows[0])
    assert all(row["overallScore"] is not None for row in rows)
    assert {row["id"] for row in rows if row["pareto"]} == {viewmodel.slugify(i) for i in source["pareto"]}
    assert "gpt-6-1-sol" not in {row["id"] for row in rows}
    assert rows == sorted(rows, key=lambda row: (row["costPerSuccessfulTaskUsd"] is None, row["costPerSuccessfulTaskUsd"] or 0, row["id"]))


def test_export_writes_livebench_json(data, tmp_path):
    written = export.export_public_data(data, tmp_path / "out")
    assert tmp_path / "out" / "livebench.json" in written
    assert json.loads((tmp_path / "out" / "livebench.json").read_text())["rows"]


def test_export_writes_frontier_tier_fields_and_model_inclusion(data, tmp_path):
    export.export_public_data(data, tmp_path / "out")
    rankings = json.loads((tmp_path / "out" / "rankings.json").read_text())
    assert {"aaFrontierTier", "aaFrontierConfiguration", "aaFrontierIntelligenceGap", "aaFrontierFootnote"} <= set(rankings["models"][0])
    assert "frontierRule" in rankings["modelInclusion"]
    model_doc = json.loads((tmp_path / "out" / "models" / "gpt-6-1-sol.json").read_text())
    assert {"tier", "configuration", "intelligenceGap", "footnote"} <= set(model_doc["frontier"])


def test_models_index_lists_every_roster_model_ranked_first(bundle):
    page = viewmodel.models_page(bundle)
    models = page["models"]
    assert len(models) == 62
    assert {"slug", "name", "developer", "rank", "overall", "grade", "rankingEligible", "coveragePct"} <= set(models[0])
    ranked = [m for m in models if m["rank"]["plan"] is not None]
    plan_ranks = [m["rank"]["plan"] for m in ranked]
    assert plan_ranks == sorted(plan_ranks) and plan_ranks[0] == 1 and len(ranked) == 9
    assert models[:9] == ranked
    assert all(m["rank"]["plan"] is None for m in models[9:])
    # O51: every configuration with the max-effort ranking's full set has a cost and a rank there.
    assert [m["slug"] for m in models[9:] if m["rankingEligible"]] == []
    assert page["rankedCount"] == 9 and page["unrankedCount"] == 53


def test_index_models_carry_the_coverage_object(bundle):
    first = viewmodel.index_page(bundle)["models"][0]
    assert set(first["coverage"]) == {"pct", "costAvailable", "missing", "provisional", "provisionalReasons"}


def test_rankings_columns_use_the_script_catalogue_keys(bundle):
    columns = viewmodel.rankings_page(bundle)["columns"]
    keys = [c["key"] for c in columns]
    assert keys[:7] == ["rank", "name", "overall", "quality", "cost", "grade", "coverage"]
    assert {"developer", "qualityRank", "speed", "ii", "frontierCode", "omniscience"} <= set(keys)
    assert "costComposite" not in keys and "model" not in keys
    assert all(c["sortable"] is True and c["label"] for c in columns)
    assert [c["key"] for c in columns if c["default"]] == keys[:7]


def test_plans_worked_example_has_a_models_list(bundle):
    example = viewmodel.plans_page(bundle)["workedExample"]
    assert [m["slug"] for m in example["models"]] == ["claude-opus-5-5", "gpt-6-1-sol"]
    sol = example["models"][1]
    assert set(sol) >= {"slug", "name", "apiUsd", "valueMultiple", "planUsd", "routeLabel", "grade", "evidenceLabel", "planFeeUsd"}
    assert sol["planUsd"] == pytest.approx(sol["apiUsd"] / sol["valueMultiple"])


def test_methodology_worked_example_lists_steps_and_priorities(bundle):
    example = viewmodel.methodology_page(bundle)["workedExample"]
    assert example["name"] and example["steps"] and "rows" not in example
    assert {"label", "weightPct", "normalized", "contribution", "included", "effectiveWeightPct"} <= set(example["steps"][0])
    assert example["qualityCoveragePct"] == 100 and example["missing"] == []  # O36: every ranked row has every leaf
    cost = next(step for step in example["steps"] if step["key"] == "costComposite")
    assert cost["included"] and cost["effectiveWeightPct"] == 25.0


def test_data_page_links_are_absolute_and_include_livebench(bundle):
    paths = [f["path"] for f in viewmodel.data_page(bundle)["files"]]
    assert paths == [
        "/data/rankings.json", "/data/rankings-aicd.json", "/data/rankings-common.json", "/data/models/<slug>.json", "/data/plans.json", "/data/benchmarks.json",
        "/data/benchmarks/terminal-bench-4.json", "/data/changelog.json", "/data/livebench.json",
    ]


def test_methodology_worked_example_shows_a_missing_leaf_at_zero_weight(bundle):
    """A row with a leaf missing (none is ranked since O36) is the example of choice; the leaf carries no weight."""

    rankings = json.loads(json.dumps(bundle.rankings))
    first = next(m for m in rankings["models"] if m["rank"]["plan"] == 1)
    first["dims"]["frontierCode"], first["coverage"]["pct"] = None, 92.5
    example = viewmodel.methodology_page(viewmodel.Bundle(**{**bundle.__dict__, "rankings": rankings}))["workedExample"]
    step = next(step for step in example["steps"] if step["key"] == "frontierCode")
    assert example["slug"] == first["slug"] and example["missing"] == [step["label"]]
    assert step["included"] is False and step["effectiveWeightPct"] == 0.0 and step["contribution"] == 0.0


def test_leaf_sources_name_the_gap_fill_publisher():
    """O36/O37: a supplement names its publisher; a Terminal-Bench leaf on another agent is tbench.ai's gap fill."""

    filled = {"sourceType": "independent", "source": "Cognition (FrontierCode's author)", "url": "https://example.test/fc"}
    assert viewmodel._leaf_source("frontierCode", filled) == {"name": "Cognition (FrontierCode's author)", "url": "https://example.test/fc"}
    assert viewmodel._leaf_source("bugHunt", {"sourceType": "model_provider_claim", "source": "Xiaomi"})["url"] == viewmodel.LEAF_INFO["bugHunt"]["url"]
    assert viewmodel._leaf_source("terminalBench", {"agent": "Terminus 2"})["name"] == viewmodel.TB_GAP_SOURCE
    assert viewmodel._leaf_source("terminalBench", {"agent": "mini-SWE-agent"})["name"] == viewmodel.SOURCE_NAMES["terminalBench"]
    assert viewmodel._leaf_source("gdpval", {})["name"] == viewmodel.AA_SOURCE
