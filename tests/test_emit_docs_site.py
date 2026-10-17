"""Template-guard branches of the site emitter.

The committed ``site/index.html`` is both template and output, so every
"insert it when absent" guard is exercised by deleting that fragment from a
repo copy and checking that ``main`` puts it back (usually byte-identically).
"""

import re

import pytest

from test_emit_docs_support import (
    CODING,
    SITE,
    committed,
    edit_site,
    emit,
    main_literal,
    site_text,
    strip_block,
)

pytestmark = pytest.mark.usefixtures("pinned_clock")

COST_CSS = r"    /\* API-price versus subscription-plan cost switcher \*/.*?(?=    /\* CA Cost \+ Value columns \*/)"
COST_MARKUP = r'    <div class="cost-basis-control" id="cost-basis-control".*?(?=    <div class="table-controls">)'
LIVEBENCH_FUNCTION = r"function renderLiveBenchPareto\(\) \{.*?\n\}\n\n(?=function renderPareto\(\))"
LIVEBENCH_PANEL = r"       <!-- LiveBench Pareto -->.*?(?=      <!-- Two-frontier / Cost Impact -->)"
LIVEBENCH_CARD = r'    <div class="card mb-6" id="livebench-data">.*?(?=    <!-- BUG HUNT DATA CARD START -->)'
BUG_HUNT_CARD = r"    <!-- BUG HUNT DATA CARD START -->.*?<!-- BUG HUNT DATA CARD END -->\n"


def restored(repo, pattern):
    """Strip ``pattern`` from the copy's page, emit, and return the page after emission."""

    edit_site(repo, lambda html: strip_block(html, pattern))
    emit(repo)
    return site_text(repo)


@pytest.mark.parametrize(
    "pattern",
    [COST_CSS, COST_MARKUP, LIVEBENCH_FUNCTION, BUG_HUNT_CARD],
    ids=["cost-css", "cost-markup", "livebench-function", "bughunt-card"],
)
def test_removed_fragment_is_reinserted_byte_identically(repo_copy, pattern):
    assert restored(repo_copy, pattern) == committed(SITE)


def test_removed_livebench_panel_is_rebuilt_before_the_cost_impact_panel(repo_copy):
    html = restored(repo_copy, LIVEBENCH_PANEL)
    assert html.count('id="panel-livebenchPareto"') == 1
    panel = re.search(r'<div class="chart-panel" id="panel-livebenchPareto">.*?</div>\s*</div>', html, re.S).group(0)
    assert 'id="chart-livebench-pareto"' in panel
    assert html.index("<!-- LiveBench Pareto -->") < html.index("<!-- Two-frontier / Cost Impact -->")


def test_removed_livebench_card_is_rebuilt_at_the_first_data_card(repo_copy):
    html = restored(repo_copy, LIVEBENCH_CARD)
    assert html.count('id="livebench-data"') == 1
    card = '<div class="card mb-6" id="livebench-data">'
    assert html.count(card) == 1
    assert html.index("<!-- DATA -->") < html.index(card)


def test_removed_cost_switcher_is_reinserted_after_speed_index(repo_copy):
    html = restored(repo_copy, r"// COST BASIS SWITCHER START.*?// COST BASIS SWITCHER END\n?")
    assert html.count("// COST BASIS SWITCHER START") == 1
    assert re.search(r"const SPEED_DIM_IDX = \d+;\n\n// COST BASIS SWITCHER START", html)


def test_removed_dim_links_are_added_after_dim_cat(repo_copy):
    html = restored(repo_copy, r"const DIM_LINKS\s*=\s*\[[^\]]*\];\n?")
    assert re.search(r"const DIM_CAT = \[[^\]]*\];\nconst DIM_LINKS = \[", html)
    assert html.count("const DIM_LINKS =") == 1


def test_missing_init_cost_basis_call_is_added_before_the_hero_podium(repo_copy):
    token = "    try { initCostBasis(); } catch (e) { console.error(e); }\n"
    edit_site(repo_copy, lambda html: html.replace(token, "", 1))
    emit(repo_copy)
    assert site_text(repo_copy) == committed(SITE)


def test_missing_chart_tab_and_registrations_are_restored(repo_copy):
    def drop(html):
        html = re.sub(r'\s*<button class="chart-tab" data-chart="livebenchPareto">LiveBench Pareto</button>', "", html, count=1)
        html = html.replace("  livebenchPareto: renderLiveBenchPareto,\n", "", 1)
        return html.replace("'chart-heatmap-data','chart-livebench-pareto'", "'chart-heatmap-data'", 1)

    edit_site(repo_copy, drop)
    emit(repo_copy)
    html = site_text(repo_copy)
    assert "livebenchPareto: renderLiveBenchPareto" in html
    assert "'chart-heatmap-data','chart-livebench-pareto'" in html
    tabs = re.search(r'<div class="chart-tabs">([\s\S]*?)</div>', html).group(1)
    assert re.findall(r'data-chart="([^"]+)"', tabs)[:2] == ["pareto", "livebenchPareto"]


@pytest.mark.parametrize(
    ("name", "copies"),
    [("dynamic_cost_chart_replacements", 1), ("dynamic_hero_replacements", 1), ("post_renderer_cost_replacements", 2)],
)
def test_legacy_cost_strings_are_rewritten_to_the_dynamic_forms(repo_copy, name, copies):
    pairs = main_literal(name)
    # The post-renderer pass only sees strings that an earlier pass left behind, so it needs a spare copy.
    olds = "\n".join(old for old, _new in pairs) * copies
    baseline = committed(SITE)
    edit_site(repo_copy, lambda html: html.replace("<footer>", f"<!--LEGACY\n{olds}\nLEGACY-->\n<footer>", 1))
    emit(repo_copy)
    html = site_text(repo_copy)
    for old, new in pairs:
        assert html.count(new) >= baseline.count(new) + 1, new
        assert old not in html or copies > 1


class TestMissingAnchors:
    def fails(self, repo, transform, message):
        edit_site(repo, transform)
        with pytest.raises(SystemExit, match=message):
            emit(repo)

    def test_root_pareto_renderer_missing(self, repo_copy):
        def drop(html):
            html = strip_block(html, LIVEBENCH_FUNCTION)
            return html.replace("function renderPareto()", "function renderParetoGone()")

        self.fails(repo_copy, drop, "root Pareto renderer missing")

    def test_insight_grid_missing(self, repo_copy):
        self.fails(repo_copy, lambda html: html.replace('class="insight-grid"', 'class="gone"'), "insight grid not found")

    def test_insight_count_mismatch(self, repo_copy):
        def drop(html):
            start = html.index('<div class="insight-grid"')
            end = html.index("</section>", start)
            grid = html[start:end].replace('<div class="insight-body">', '<div class="insight-bodyx">', 1)
            return html[:start] + grid + html[end:]

        self.fails(repo_copy, drop, "insight replacement failed")

    def test_chart_tabs_missing(self, repo_copy):
        self.fails(repo_copy, lambda html: html.replace('<div class="chart-tabs">', '<div class="tabs-gone">'), "chart tab order replacement failed: 0")

    def test_livebench_card_without_following_card(self, repo_copy):
        def drop(html):
            head, tail = html.split('    <div class="card mb-6" id="livebench-data">', 1)
            tail = tail.replace('    <div class="card mb-6">', '    <div class="card mb-6 x">')
            return head + '    <div class="card mb-6" id="livebench-data">' + tail

        self.fails(repo_copy, drop, "next data card not found after existing LiveBench card")

    def test_data_section_marker_missing_when_livebench_card_absent(self, repo_copy):
        self.fails(repo_copy, lambda html: strip_block(html, LIVEBENCH_CARD).replace("<!-- DATA -->", ""), "data section insertion point not found")

    def test_bug_hunt_card_without_end_marker(self, repo_copy):
        # The LiveBench card replacement swallows the original block, so a stray START marker is what is left.
        self.fails(repo_copy, lambda html: html.replace("<footer>", "<!-- BUG HUNT DATA CARD START -->\n<footer>", 1), "Bug Hunt card replacement failed: 0")

    def test_main_closing_tag_missing(self, repo_copy):
        edit_site(repo_copy, lambda html: html.replace("</main>", ""))
        with pytest.raises(ValueError, match="lacks </main>"):
            emit(repo_copy)

    def test_current_copy_pattern_missing(self, repo_copy):
        edit_site(repo_copy, lambda html: html.replace("function computeNewScore(model, costWeightPct) {", "function computeScoreGone() {", 1))
        with pytest.raises(SystemExit, match="current-release copy replacement failed"):
            emit(repo_copy)


def test_coding_agents_page_is_rewritten_in_place(repo_copy):
    page = repo_copy / CODING
    page.write_text(page.read_text().replace("<th>TB2.1 (historical)</th>", "<th>TB2.1</th>"))
    emit(repo_copy)
    assert "<th>TB2.1 (historical)</th>" in page.read_text()
