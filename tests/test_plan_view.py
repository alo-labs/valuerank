"""The Plan Costs view prices subscriptions in USD per AA Intelligence Index point
and is the view the site opens on."""

import json

import pytest

from valuerank import emit_docs
from valuerank.site.export import export_public_data


def regenerate(repo_copy):
    emit_docs.main(root=repo_copy, data=repo_copy / "data")
    return (repo_copy / "README.md").read_text()


def public_rankings(repo_copy, tmp_path):
    """``rankings.json`` as the site build exports it for the public data downloads."""

    export_public_data(data=repo_copy / "data", out=tmp_path / "public")
    return json.loads((tmp_path / "public" / "rankings.json").read_text())


def test_public_rankings_open_on_the_plan_basis(repo_copy, tmp_path):
    rankings = public_rankings(repo_copy, tmp_path)

    assert rankings["defaultBasis"] == "plan"
    assert "plan" in rankings["bases"] and rankings["defaultBasis"] in rankings["bases"]


def test_public_models_carry_per_point_and_per_run_plan_costs(repo_copy, tmp_path):
    models = {model["name"]: model for model in public_rankings(repo_copy, tmp_path)["models"]}
    sol = models["GPT-6.1 Sol"]["cost"]
    opus = models["Claude Opus 5.5"]["cost"]
    scored = {m["name"]: m for m in json.loads((repo_copy / "data" / "scores.json").read_text())["models"]}["GPT-6.1 Sol"]

    assert sol["planUsdPerRun"] == pytest.approx(scored["aaEvalCost"] / 10.772)
    assert sol["planUsdPerPoint"] == pytest.approx(scored["aaEvalCost"] / 10.772 / scored["intelligenceIndex"])
    assert opus["planUsdPerPoint"] > sol["planUsdPerPoint"]
    assert sol["fallback"] is None


def test_readme_candidate_table_shows_cost_per_index_point(repo_copy, pinned_clock):
    readme = regenerate(repo_copy)

    assert "| Effective Plan cost per Index point |" in readme
    sol_row = next(line for line in readme.splitlines() if line.startswith("| GPT-6.1 Sol |"))
    assert "| $100.40 | $1.94 |" in sol_row
    opus_row = next(line for line in readme.splitlines() if line.startswith("| Claude Opus 5.5 |"))
    assert "| $147.85 | $2.57 |" in opus_row
    assert "divided by the model's AA Intelligence Index" in readme
