"""Behaviour tests for the shared ValueRank header renderer and injector in valuerank.site_header."""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from valuerank.site_header import CHART_LABEL_JS, HEADER_CSS, TABLE_SORT_JS, inject_header, render_header

MODE_LINK = re.compile(r'<a class="(vr-mode-btn[^"]*)" href="([^"]*)">([^<]*)</a>')
EXPECTED_MODES = [("/", "LLM Models"), ("/coding-agents/", "Coding Agents"), ("/tb4/", "TB 4")]
STYLE_OPEN = '<style id="site-header-style">'
CHART_OPEN = '<script id="site-chart-labels">'
TABLE_OPEN = '<script id="site-table-sort">'
NAV_MARKER = 'data-vr-shared-header="true"'

PAGE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Sample page</title>
</head>
<body>
  <nav><a href="/old">Old navigation</a></nav>
  <main>Body text</main>
</body>
</html>
"""


def mode_links(header: str) -> list[tuple[str, str, list[str]]]:
    """Return (href, label, classes) for each mode link in rendered header markup."""

    return [(href, label, classes.split()) for classes, href, label in MODE_LINK.findall(header)]


def write_page(tmp_path: Path, html: str = PAGE, name: str = "page.html") -> Path:
    path = tmp_path / name
    path.write_text(html)
    return path


# --- render_header ----------------------------------------------------------


def test_render_header_lists_the_three_modes_in_order():
    links = mode_links(render_header("llm", "meta"))

    assert [(href, label) for href, label, _ in links] == EXPECTED_MODES


@pytest.mark.parametrize(("active", "href"), [("llm", "/"), ("coding", "/coding-agents/"), ("tb4", "/tb4/")])
def test_render_header_marks_only_the_active_mode(active, href):
    links = mode_links(render_header(active, "meta"))

    assert [link_href for link_href, _, classes in links if "active" in classes] == [href]


@pytest.mark.parametrize("active", ["other", "", "<script>alert(1)</script>", 'llm"'])
def test_unknown_or_hostile_active_mode_marks_no_link_and_never_emits_raw_markup(active):
    header = render_header(active, "meta")

    assert [href for href, _, classes in mode_links(header) if "active" in classes] == []
    assert "<script>alert(1)</script>" not in header


def test_render_header_is_the_shared_navigation_contract():
    header = render_header("llm", "meta")

    assert header.startswith('<nav class="vr-site-header" data-vr-shared-header="true">')
    assert header.endswith("</nav>")
    assert 'id="theme-toggle"' in header, "page scripts attach the theme switch to this id"


def test_render_header_escapes_meta_text():
    header = render_header("llm", '<b>x</b> & "y"')

    assert '<div class="vr-nav-meta">&lt;b&gt;x&lt;/b&gt; &amp; &quot;y&quot;</div>' in header
    assert "<b>x</b>" not in header


def test_render_header_escapes_badge_text_and_defaults_to_v1_4_0():
    assert '<span class="vr-nav-badge">v1.4.0</span>' in render_header("llm", "meta")

    header = render_header("llm", "meta", badge='v1 "<beta>"')

    assert '<span class="vr-nav-badge">v1 &quot;&lt;beta&gt;&quot;</span>' in header


# --- inject_header: success path --------------------------------------------


def test_inject_header_replaces_the_nav_and_installs_style_and_scripts_once(tmp_path):
    page = write_page(tmp_path)

    inject_header(page, "coding", "Meta line", "v9.9")

    result = page.read_text()
    assert "Old navigation" not in result
    assert result.count(NAV_MARKER) == 1
    assert '<a class="vr-mode-btn active" href="/coding-agents/">Coding Agents</a>' in result
    assert '<div class="vr-nav-meta">Meta line</div>' in result
    assert '<span class="vr-nav-badge">v9.9</span>' in result
    assert f"{STYLE_OPEN}\n{HEADER_CSS}\n</style>" in result
    assert f"{CHART_OPEN}\n{CHART_LABEL_JS}\n</script>" in result
    assert f"{TABLE_OPEN}\n{TABLE_SORT_JS}\n</script>" in result
    assert "<main>Body text</main>" in result


def test_inject_header_places_head_blocks_before_head_close_and_table_script_before_body_close(tmp_path):
    page = write_page(tmp_path)

    inject_header(page, "llm", "m")

    result = page.read_text()
    assert result.index("<head>") < result.index(STYLE_OPEN) < result.index(CHART_OPEN) < result.index("</head>")
    assert result.index("</head>") < result.index(TABLE_OPEN) < result.index("</body>")
    assert result.index('<nav class="vr-site-header"') < result.index("<main>"), "nav keeps its original position"


def test_inject_header_uses_the_default_badge_and_escapes_meta(tmp_path):
    page = write_page(tmp_path)

    inject_header(page, "llm", "<b>&</b>")

    result = page.read_text()
    assert '<span class="vr-nav-badge">v1.4.0</span>' in result
    assert '<div class="vr-nav-meta">&lt;b&gt;&amp;&lt;/b&gt;</div>' in result


def test_a_page_with_several_navs_is_rejected_unchanged(tmp_path):
    page = write_page(tmp_path, PAGE.replace("<main>", '<nav class="second">Second navigation</nav>\n  <main>'))
    before = page.read_text()

    with pytest.raises(SystemExit, match="expected one nav .* found 2"):
        inject_header(page, "llm", "m")

    assert page.read_text() == before


# --- inject_header: idempotency --------------------------------------------


def test_repeated_injection_is_byte_identical_and_never_duplicates_blocks(tmp_path):
    page = write_page(tmp_path)
    inject_header(page, "tb4", "Same meta", "v1")
    first = page.read_text()

    inject_header(page, "tb4", "Same meta", "v1")

    assert page.read_text() == first
    for marker in (STYLE_OPEN, CHART_OPEN, TABLE_OPEN, NAV_MARKER):
        assert first.count(marker) == 1, marker


def test_repeated_injection_refreshes_the_nav_and_replaces_stale_blocks(tmp_path):
    stale = PAGE.replace(
        "</head>",
        f"{STYLE_OPEN}.stale-rule{{}}</style>\n"
        f"{CHART_OPEN}staleChartHelper()</script>\n"
        f"{TABLE_OPEN}staleSorter()</script>\n</head>",
    )
    page = write_page(tmp_path, stale)

    inject_header(page, "llm", "Fresh meta")

    result = page.read_text()
    for leftover in (".stale-rule{}", "staleChartHelper()", "staleSorter()"):
        assert leftover not in result
    assert f"{STYLE_OPEN}\n{HEADER_CSS}\n</style>" in result
    assert f"{CHART_OPEN}\n{CHART_LABEL_JS}\n</script>" in result
    assert f"{TABLE_OPEN}\n{TABLE_SORT_JS}\n</script>" in result
    assert '<div class="vr-nav-meta">Fresh meta</div>' in result
    for marker in (STYLE_OPEN, CHART_OPEN, TABLE_OPEN, NAV_MARKER):
        assert result.count(marker) == 1, marker


def test_existing_blocks_are_refreshed_in_place_without_head_or_body_markers(tmp_path):
    fragment = (
        f'<nav>old</nav>{STYLE_OPEN}stale</style>'
        f"{CHART_OPEN}stale</script>{TABLE_OPEN}stale</script>"
    )
    page = write_page(tmp_path, fragment, name="fragment.html")

    inject_header(page, "coding", "m")

    result = page.read_text()
    assert f"{STYLE_OPEN}\n{HEADER_CSS}\n</style>" in result
    assert f"{CHART_OPEN}\n{CHART_LABEL_JS}\n</script>" in result
    assert f"{TABLE_OPEN}\n{TABLE_SORT_JS}\n</script>" in result
    assert ">stale<" not in result
    assert "</head>" not in result and "</body>" not in result, "no structural markers were required or added"


# --- inject_header: failure paths -------------------------------------------


def test_a_page_without_a_nav_is_rejected_and_left_untouched(tmp_path):
    page = write_page(tmp_path, PAGE.replace('<nav><a href="/old">Old navigation</a></nav>', ""))
    before = page.read_bytes()

    with pytest.raises(SystemExit) as failure:
        inject_header(page, "llm", "m")

    assert failure.value.code == f"shared header injection expected one nav in {page}, found 0"
    assert page.read_bytes() == before


def test_a_page_without_a_head_close_is_rejected_when_style_is_missing(tmp_path):
    page = write_page(tmp_path, "<html><body><nav>old</nav><main>x</main></body></html>")
    before = page.read_bytes()

    with pytest.raises(SystemExit) as failure:
        inject_header(page, "llm", "m")

    assert failure.value.code == f"shared header CSS injection failed in {page}"
    assert page.read_bytes() == before


def test_a_page_without_a_head_close_is_rejected_when_chart_script_is_missing(tmp_path):
    # The stylesheet block already exists, so only the chart-label script needs </head>.
    page = write_page(tmp_path, '<html><body><style id="site-header-style">x</style><nav>old</nav></body></html>')
    before = page.read_bytes()

    with pytest.raises(SystemExit) as failure:
        inject_header(page, "llm", "m")

    assert failure.value.code == f"shared chart-label injection failed in {page}"
    assert page.read_bytes() == before


def test_a_page_without_a_body_close_is_rejected_when_table_sort_script_is_missing(tmp_path):
    page = write_page(tmp_path, "<html><head><title>t</title></head><nav>old</nav><main>x</main></html>")
    before = page.read_bytes()

    with pytest.raises(SystemExit) as failure:
        inject_header(page, "llm", "m")

    assert failure.value.code == f"shared table-sort injection failed in {page}"
    assert page.read_bytes() == before
