"""The Plan view prices subscriptions per SDLC basket run and is the view the site opens on."""

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


def test_public_models_carry_basket_run_plan_costs(repo_copy, tmp_path):
    models = {model["name"]: model for model in public_rankings(repo_copy, tmp_path)["models"]}
    sol = models["GPT-6.1 Sol"]["cost"]
    opus = models["Claude Opus 5.5"]["cost"]
    rows = {row["id"]: row for row in json.loads((repo_copy / "data" / "scores.json").read_text())["v3"]["rows"]}

    assert sol["apiUsd"] == rows["gpt-6.1-sol"]["api"]["costUsd"]
    assert sol["planUsd"] == pytest.approx(rows["gpt-6.1-sol"]["api"]["costUsd"] / 10.772)
    assert opus["planUsd"] > sol["planUsd"]
    assert sol["fallback"] is None and sol["route"]["id"] == "chatgpt-pro500-common-semianalysis-assumption"


def test_readme_prices_each_configuration_per_basket_run_on_both_bases(repo_copy, pinned_clock):
    readme = regenerate(repo_copy)
    rows = {row["id"]: row for row in json.loads((repo_copy / "data" / "scores.json").read_text())["v3"]["rows"]}

    assert "| Plan rank | API rank | Configuration | Plan value | API value | Quality | Quality coverage | API cost (USD per basket run) | Plan cost (USD per basket run) | Plan route | Flags |" in readme
    sol_row = next(line for line in readme.splitlines() if line.startswith("| 3 | 2 | [GPT-6.1 Sol (max)]"))
    assert f"| ${rows['gpt-6.1-sol']['api']['costUsd']:,.2f} | ${rows['gpt-6.1-sol']['api']['costUsd'] / 10.772:,.2f} |" in sol_row
    assert "divides the basket's API cost by the selected subscription route's Value Multiple" in readme
