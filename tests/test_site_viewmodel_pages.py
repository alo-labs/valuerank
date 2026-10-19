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
    assert len(models) == 31
    assert {"slug", "name", "developer", "rank", "overall", "grade", "rankingEligible", "coveragePct"} <= set(models[0])
    ranked = [m for m in models if m["rankingEligible"]]
    plan_ranks = [m["rank"]["plan"] for m in ranked]
    assert plan_ranks == sorted(plan_ranks) and plan_ranks[0] == 1 and len(ranked) == 19
    assert models[:19] == ranked
    assert all(m["rank"]["plan"] is None for m in models[19:])
    assert page["rankedCount"] == 19 and page["unrankedCount"] == 12


def test_index_models_carry_the_coverage_object(bundle):
    first = viewmodel.index_page(bundle)["models"][0]
    assert set(first["coverage"]) == {"pct", "costAvailable", "missing", "provisional", "provisionalReasons"}


def test_rankings_columns_use_the_script_catalogue_keys(bundle):
    columns = viewmodel.rankings_page(bundle)["columns"]
    keys = [c["key"] for c in columns]
    assert keys[:7] == ["rank", "name", "overall", "quality", "cost", "grade", "coverage"]
    assert {"developer", "qualityRank", "speed", "ii", "deepswe", "omniscience"} <= set(keys)
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
    assert 0 < example["qualityCoveragePct"] < 100 and example["missing"]
    cost = next(step for step in example["steps"] if step["key"] == "costComposite")
    assert cost["included"] and cost["effectiveWeightPct"] == 25.0


def test_data_page_links_are_absolute_and_include_livebench(bundle):
    paths = [f["path"] for f in viewmodel.data_page(bundle)["files"]]
    assert paths == [
        "/data/rankings.json", "/data/models/<slug>.json", "/data/plans.json", "/data/benchmarks.json",
        "/data/benchmarks/terminal-bench-4.json", "/data/changelog.json", "/data/livebench.json",
    ]
