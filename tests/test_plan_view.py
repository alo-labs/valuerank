"""The Plan Costs view prices subscriptions in USD per AA Intelligence Index point
and is the view the site opens on."""

import json
import re

import pytest

from valuerank import emit_docs


def regenerate(repo_copy):
    emit_docs.main(root=repo_copy, data=repo_copy / "data")
    return (repo_copy / "README.md").read_text(), (repo_copy / "site" / "index.html").read_text()


def test_site_opens_on_plan_costs_with_plan_as_the_first_button(repo_copy, pinned_clock):
    _readme, html = regenerate(repo_copy)

    buttons = re.findall(r'<button type="button" class="cost-basis-btn( active)?" data-cost-basis="(api|plan)" aria-pressed="(true|false)">', html)
    assert buttons == [(" active", "plan", "true"), ("", "api", "false")]
    assert "let costBasis = 'plan';" in html
    assert "localStorage.getItem('vr-cost-basis') || 'plan'" in html
    assert '<span id="cost-basis-table-label">(Plan Costs)</span>' in html


def test_site_models_carry_per_point_and_per_run_plan_costs(repo_copy, pinned_clock):
    _readme, html = regenerate(repo_copy)
    models = json.loads(re.search(r"const MODELS = (\[.*?\]);\n", html, re.S).group(1))
    sol = next(model for model in models if model["name"] == "GPT-6.1 Sol")
    opus = next(model for model in models if model["name"] == "Claude Opus 5.5")

    assert sol["planCostPerRun"] == pytest.approx(1081.55 / 10.772)
    assert sol["planCost"] == pytest.approx(1081.55 / 10.772 / 52.0)
    assert opus["planCost"] > sol["planCost"]
    assert sol["planCostScore"] > opus["planCostScore"]
    assert "per Index point" in html


def test_readme_candidate_table_shows_cost_per_index_point(repo_copy, pinned_clock):
    readme, _html = regenerate(repo_copy)

    assert "| Effective Plan cost per Index point |" in readme
    sol_row = next(line for line in readme.splitlines() if line.startswith("| GPT-6.1 Sol |"))
    assert "| $100.40 | $1.93 |" in sol_row
    opus_row = next(line for line in readme.splitlines() if line.startswith("| Claude Opus 5.5 |"))
    assert "| $147.85 | $2.57 |" in opus_row
    assert "divided by the model's AA Intelligence Index" in readme


def test_site_table_compares_every_model_in_usd_per_index_point_on_the_plan_basis(repo_copy, pinned_clock):
    _readme, html = regenerate(repo_copy)

    # Models without a route must not show raw API dollars beside per-point values.
    assert "const value = costBasis === 'plan' ? model.planComparableCost : model.apiCost;" in html
    assert "per Index point (API fallback)" in html
