"""Behaviour tests for the Terminal-Bench 4.0 page generator in valuerank.tb4_page.

Every render writes under a temporary root (``repo_copy`` or ``tmp_path``); nothing
here touches the committed site/ output.
"""

from __future__ import annotations

import json
import re
import runpy
import sys
from html import escape
from pathlib import Path

import pytest

from valuerank import release

from valuerank import paths, tb4_page


def make_row(
    model,
    cost_usd,
    rate,
    *,
    base=None,
    agent="Codex",
    cohort_id="cohort-x",
    rank_label="1",
    tokens="1M",
    uncertainty=1.5,
):
    return {
        "rankLabel": rank_label,
        "model": model,
        "baseModel": model if base is None else base,
        "agent": agent,
        "resolutionRate": rate,
        "resolutionRatePct": rate * 100,
        "uncertaintyPct": uncertainty,
        "tokens": tokens,
        "costUsd": cost_usd,
        "cohortModelId": cohort_id,
    }


def make_document(rows, **overrides):
    document = {
        "rowN": len(rows),
        "matchedN": 0,
        "cohortN": 1,
        "missingModels": [],
        "rows": rows,
    }
    document.update(overrides)
    return document


def write_data(root: Path, document) -> Path:
    data = root / "data"
    data.mkdir(parents=True, exist_ok=True)
    (data / "tb4.json").write_text(json.dumps(document, ensure_ascii=False))
    return data


def render(root: Path, document, **options) -> int:
    return tb4_page.main(root=root, data=write_data(root, document), **options)


def page_html(root: Path) -> str:
    return (root / "site" / "tb4" / "index.html").read_text()


def committed_document(repo_copy: Path) -> dict:
    return json.loads((repo_copy / "data" / "tb4.json").read_text())


def pareto_frontier_size(rows) -> int:
    """Count rows not dominated on (lower cost, higher resolution); an independent oracle for the page."""

    def dominated(row):
        return any(
            other["costUsd"] <= row["costUsd"]
            and other["resolutionRate"] >= row["resolutionRate"]
            and (other["costUsd"] < row["costUsd"] or other["resolutionRate"] > row["resolutionRate"])
            for other in rows
        )

    return sum(1 for row in rows if not dominated(row))


def tbody(html: str) -> str:
    return re.search(r"<tbody>(.*?)</tbody>", html, re.S).group(1)


# --- committed publication --------------------------------------------------


@pytest.mark.integration
def test_committed_data_reproduces_the_committed_publication_byte_for_byte(repo_copy):
    published = repo_copy / "site" / "tb4" / "index.html"
    committed = published.read_bytes()

    assert tb4_page.main(root=repo_copy, data=repo_copy / "data") == 0

    assert published.read_bytes() == committed


def test_committed_page_reports_the_counts_from_the_committed_document(repo_copy):
    document = committed_document(repo_copy)

    tb4_page.main(root=repo_copy, data=repo_copy / "data")
    html = page_html(repo_copy)

    assert f"<strong>{document['rowN']}</strong><span>official rows</span>" in html
    assert f"<strong>{document['matchedN']}/{document['cohortN']}</strong><span>direct official cohort matches</span>" in html
    assert (
        f"<strong>{document['rankingAvailableN']}/{document['cohortN']}</strong>"
        "<span>eligible values incl. provider claims</span>"
    ) in html
    assert (
        f"<strong>{pareto_frontier_size(document['rows'])}</strong>"
        "<span>official cost / resolution frontier rows</span>"
    ) in html
    assert (
        f"The official snapshot directly matches {document['matchedN']} of the {document['cohortN']} "
        "current ValueRank models."
    ) in html
    assert f"{len(document['rankingMissingModels'])} rows remain without an official result" in html


def test_committed_rows_render_one_table_row_each_with_cohort_coverage(repo_copy):
    document = committed_document(repo_copy)

    tb4_page.main(root=repo_copy, data=repo_copy / "data")
    body = tbody(page_html(repo_copy))

    assert body.count('<tr><td class="mono">') == document["rowN"]
    assert body.count('<td class="covered">ValueRank cohort</td>') == sum(
        1 for row in document["rows"] if row["cohortModelId"]
    )
    assert body.count('<td class="muted">Official-only</td>') == sum(
        1 for row in document["rows"] if not row["cohortModelId"]
    )


def test_committed_provider_claim_is_listed_separately_with_its_caveat(repo_copy):
    document = committed_document(repo_copy)
    claim = document["providerClaims"][0]

    tb4_page.main(root=repo_copy, data=repo_copy / "data")
    html = page_html(repo_copy)

    assert f"<td>{escape(claim['alias'])}</td>" in html
    assert f"<td>{escape(claim['evaluatedModel'])}</td>" in html
    assert f"<td class='mono'>{claim['valuePct']:.1f}%</td>" in html
    assert "<td>Ranking eligible for current alias</td>" in html
    assert (
        f"<a href='{escape(claim['sourceUrl'], quote=True)}' target='_blank' rel='noopener'>"
        f"{escape(claim['publisher'])}</a>"
    ) in html
    assert f"<td>{escape(claim['caveat'])}</td>" in html


def test_committed_page_has_no_unreplaced_template_placeholder(repo_copy):
    tb4_page.main(root=repo_copy, data=repo_copy / "data")

    assert re.findall(r"__[A-Z_]+__", page_html(repo_copy)) == []


def test_summary_printed_to_stdout_describes_the_committed_render(repo_copy, capsys):
    document = committed_document(repo_copy)

    assert tb4_page.main(root=repo_copy, data=repo_copy / "data") == 0

    assert json.loads(capsys.readouterr().out) == {
        "output": "site/tb4/index.html",
        "officialRows": document["rowN"],
        "directMatches": document["matchedN"],
        "providerClaims": document["providerClaimN"],
        "rankingAvailable": document["rankingAvailableN"],
    }


def test_missing_models_key_fails_loudly_and_keeps_the_published_page(repo_copy, tmp_path):
    document = committed_document(repo_copy)
    del document["missingModels"]
    published = repo_copy / "site" / "tb4" / "index.html"
    before = published.read_bytes()

    with pytest.raises(KeyError, match="missingModels"):
        tb4_page.main(root=repo_copy, data=write_data(tmp_path, document))

    assert published.read_bytes() == before


# --- frontier and rows ------------------------------------------------------


def test_frontier_counts_rows_that_improve_resolution_as_cost_rises(tmp_path):
    rows = [
        make_row("A", 1, 0.4),
        make_row("B", 2, 0.4),
        make_row("C", 10, 0.3),
        make_row("D", 10, 0.5),
        make_row("E", 5, 0.2),
        make_row("F", 20, 0.5),
    ]

    render(tmp_path, make_document(rows))

    assert "<strong>2</strong><span>official cost / resolution frontier rows</span>" in page_html(tmp_path)


def test_empty_leaderboard_renders_zero_counts_and_an_empty_table(tmp_path):
    render(tmp_path, make_document([]))
    html = page_html(tmp_path)

    assert "<strong>0</strong><span>official cost / resolution frontier rows</span>" in html
    assert tbody(html) == ""
    assert "const ENTRIES = [];" in html


def test_row_cells_show_rank_model_agent_rate_tokens_and_cost(tmp_path):
    rows = [
        make_row(
            "GPT-6 Astra (max)",
            3300.0,
            0.582,
            base="GPT-6 Astra",
            agent="Codex",
            cohort_id="gpt-6-astra",
            rank_label="1",
            tokens="1.5B",
            uncertainty=2.8,
        )
    ]

    render(tmp_path, make_document(rows))

    assert (
        '<tr><td class="mono">1</td>'
        '<td><strong>GPT-6 Astra</strong><span class="variant">GPT-6 Astra (max)</span></td>'
        "<td>Codex</td>"
        '<td class="mono">58.2% <span class="uncertainty">± 2.8%</span></td>'
        '<td class="mono">1.5B</td>'
        '<td class="mono">$3,300</td>'
        '<td class="covered">ValueRank cohort</td></tr>'
    ) in tbody(page_html(tmp_path))


def test_rows_without_a_cohort_match_are_marked_official_only(tmp_path):
    render(tmp_path, make_document([make_row("Solo", 5.0, 0.1, cohort_id=None)]))

    assert '<td class="muted">Official-only</td>' in tbody(page_html(tmp_path))


def test_model_names_and_tokens_are_html_escaped_in_the_table(tmp_path):
    rows = [make_row('<b>Bad</b> & "Co"', 9.0, 0.2, base="R&D <Lab>", agent="A'B", tokens="1M<2>")]

    render(tmp_path, make_document(rows))
    body = tbody(page_html(tmp_path))

    assert "<b>Bad</b>" not in body
    assert (
        '<strong>R&amp;D &lt;Lab&gt;</strong>'
        '<span class="variant">&lt;b&gt;Bad&lt;/b&gt; &amp; &quot;Co&quot;</span>'
    ) in body
    assert "<td>A&#x27;B</td>" in body
    assert '<td class="mono">1M&lt;2&gt;</td>' in body


def test_chart_data_embeds_the_official_rows_as_json(tmp_path):
    rows = [make_row("A", 1.0, 0.5), make_row("B", 2.0, 0.25, cohort_id=None)]

    render(tmp_path, make_document(rows))
    embedded = re.search(r"^    const ENTRIES = (.*);$", page_html(tmp_path), re.M)

    assert embedded is not None
    assert json.loads(embedded.group(1)) == rows


# --- provider claims --------------------------------------------------------


def test_provider_claim_fields_are_rendered_and_escaped(tmp_path):
    claim = {
        "alias": "alias-<a>",
        "evaluatedModel": "Model & Co",
        "value": 0.25,
        "eligibleForRanking": True,
        "sourceType": "provider_blog",
        "publisher": "Pub <1>",
        "sourceUrl": 'https://e.test/x?a=1&b="2"',
        "caveat": "Caveat & <note>",
    }

    render(tmp_path, make_document([], providerClaims=[claim], providerClaimN=1))

    assert (
        "<tr><td>alias-&lt;a&gt;</td><td>Model &amp; Co</td><td class='mono'>25.0%</td>"
        "<td>Ranking eligible for current alias</td><td>provider_blog</td>"
        "<td><a href='https://e.test/x?a=1&amp;b=&quot;2&quot;' target='_blank' rel='noopener'>Pub &lt;1&gt;</a></td>"
        "<td>Caveat &amp; &lt;note&gt;</td></tr>"
    ) in page_html(tmp_path)


def test_provider_claim_defaults_fill_missing_fields_conservatively(tmp_path):
    render(tmp_path, make_document([], providerClaims=[{}]))

    assert (
        "<tr><td>—</td><td>—</td><td class='mono'>0.0%</td><td>Audit only</td>"
        "<td>model_provider_claim</td>"
        "<td><a href='#' target='_blank' rel='noopener'>Provider source</a></td>"
        "<td>—</td></tr>"
    ) in page_html(tmp_path)


@pytest.mark.parametrize(
    ("claim", "alias", "percent", "status"),
    [
        ({"cohortModelId": "cid", "value": 0.5, "valuePct": 12.36, "eligibleForRanking": True}, "cid", "12.4%", "Ranking eligible for current alias"),
        ({"alias": "a1", "value": 0.5, "eligibleForRanking": "yes"}, "a1", "50.0%", "Audit only"),
        ({"eligibleForRanking": False}, "—", "0.0%", "Audit only"),
    ],
    ids=["value-pct-wins-and-cohort-id-alias", "only-literal-true-is-eligible", "explicitly-ineligible"],
)
def test_provider_claim_precedence_and_eligibility_rules(tmp_path, claim, alias, percent, status):
    render(tmp_path, make_document([], providerClaims=[claim]))

    assert f"<tr><td>{alias}</td>" in page_html(tmp_path)
    assert f"<td class='mono'>{percent}</td><td>{status}</td>" in page_html(tmp_path)


@pytest.mark.parametrize("extra", [{"providerClaims": []}, {}], ids=["empty-list", "missing-key"])
def test_empty_or_missing_provider_claims_render_the_fallback_row(tmp_path, extra):
    render(tmp_path, make_document([], **extra))

    assert (
        '<tr><td colspan="7" class="muted">No eligible provider claims captured.</td></tr>'
    ) in page_html(tmp_path)


# --- coverage note and summary fallbacks ------------------------------------


def test_missing_models_are_escaped_and_comma_separated_in_the_coverage_note(tmp_path):
    render(tmp_path, make_document([], missingModels=["A&B", "<C>"], rankingMissingModels=["A&B"]))

    assert "1 rows remain without an official result or eligible claim: A&amp;B, &lt;C&gt;." in page_html(tmp_path)


def test_summary_counts_fall_back_to_matched_and_missing_lists_when_absent(tmp_path):
    document = make_document([], matchedN=4, cohortN=9, missingModels=["X", "Y", "Z"])

    render(tmp_path, document)
    html = page_html(tmp_path)

    assert "<strong>4/9</strong><span>eligible values incl. provider claims</span>" in html
    assert "3 rows remain without an official result or eligible claim: X, Y, Z." in html
    assert "0 official rows · 0 provider claim · current 4.0" in html, "provider claim count defaults to zero"
    assert f'<span class="vr-nav-badge">{release.VERSION}</span>' in html


def test_navigation_header_is_injected_with_the_render_summary(tmp_path):
    render(tmp_path, make_document([make_row("A", 1.0, 0.5)], providerClaimN=2))
    html = page_html(tmp_path)

    assert html.count('data-vr-shared-header="true"') == 1
    assert '<a class="vr-mode-btn active" href="/tb4/">TB 4</a>' in html
    assert '<div class="vr-nav-meta">1 official rows · 2 provider claim · current 4.0</div>' in html
    assert "<nav></nav>" not in html


# --- return value, output location and script guard -------------------------


def test_out_argument_redirects_the_page_and_is_reported_relative_to_root(tmp_path, capsys):
    target = tmp_path / "preview" / "tb4.html"

    code = render(tmp_path, make_document([]), out=target)

    assert code == 0
    assert target.is_file()
    assert not (tmp_path / "site").exists()
    assert json.loads(capsys.readouterr().out)["output"] == "preview/tb4.html"


def test_running_the_module_as_a_script_renders_the_page_and_exits_zero(repo_copy, monkeypatch, capsys):
    published = repo_copy / "site" / "tb4" / "index.html"
    committed = published.read_bytes()
    monkeypatch.setattr(paths, "ROOT", repo_copy)
    monkeypatch.setattr(paths, "DATA", repo_copy / "data")
    monkeypatch.delitem(sys.modules, "valuerank.tb4_page")

    with pytest.raises(SystemExit) as exit_info:
        runpy.run_module("valuerank.tb4_page", run_name="__main__", alter_sys=True)

    assert exit_info.value.code == 0
    assert published.read_bytes() == committed
    assert json.loads(capsys.readouterr().out)["output"] == "site/tb4/index.html"


def test_importing_the_module_without_running_it_renders_nothing(repo_copy, monkeypatch, capsys):
    published = repo_copy / "site" / "tb4" / "index.html"
    before = published.read_bytes()
    monkeypatch.setattr(paths, "ROOT", repo_copy)
    monkeypatch.setattr(paths, "DATA", repo_copy / "data")
    monkeypatch.delitem(sys.modules, "valuerank.tb4_page")

    namespace = runpy.run_module("valuerank.tb4_page", run_name="imported_for_tests")

    assert callable(namespace["main"])
    assert capsys.readouterr().out == ""
    assert published.read_bytes() == before
