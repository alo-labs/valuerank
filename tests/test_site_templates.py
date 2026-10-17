"""Render every site template against hand-written fixture view models and check the DOM contract."""

from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from pathlib import Path

import pytest
from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "valuerank" / "site" / "templates"
FIXTURES = Path(__file__).resolve().parent / "fixtures" / "site" / "templates"

FULL_PAGES = [
    "index", "rankings", "model", "models", "plans", "benchmarks",
    "benchmark_tb4", "methodology", "changelog", "data",
]
VOID = {"meta", "link", "img", "br", "hr", "input", "source", "col", "wbr"}


class Node:
    def __init__(self, tag, attrs, parent):
        self.tag, self.attrs, self.parent = tag, dict(attrs), parent
        self.children, self.text = [], ""

    def walk(self):
        yield self
        for c in self.children:
            yield from c.walk()

    def all_text(self):
        return self.text + "".join(c.all_text() for c in self.children)


class Dom(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root", [], None)
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs, self.cur)
        self.cur.children.append(n)
        if tag not in VOID:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, attrs, self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is not self.root:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.text += data

    def find_all(self, tag=None, **attrs):
        out = []
        for n in self.root.walk():
            if tag and n.tag != tag:
                continue
            if all((k.replace("_", "-") in n.attrs and (v is True or n.attrs[k.replace("_", "-")] == v)) for k, v in attrs.items()):
                out.append(n)
        return out

    def one(self, tag=None, **attrs):
        found = self.find_all(tag, **attrs)
        assert len(found) == 1, f"expected exactly one {tag} {attrs}, found {len(found)}"
        return found[0]


@pytest.fixture(scope="module")
def env():
    return Environment(
        loader=FileSystemLoader(str(TEMPLATES)),
        autoescape=select_autoescape(["html"]),
        undefined=StrictUndefined,
    )


def load(name):
    return json.loads((FIXTURES / f"{name}.json").read_text())


def render(env, name, template=None):
    site = load("_site")
    page = load(name)
    html = env.get_template(f"{template or name}.html").render(site=site, page=page)
    dom = Dom()
    dom.feed(html)
    return html, dom, page


@pytest.fixture(scope="module")
def pages(env):
    return {n: render(env, n) for n in FULL_PAGES}


@pytest.mark.parametrize("name", FULL_PAGES)
def test_exactly_one_h1_and_ordered_headings(pages, name):
    _, dom, _ = pages[name]
    heads = [int(n.tag[1]) for n in dom.root.walk() if re.fullmatch(r"h[1-6]", n.tag)]
    assert heads.count(1) == 1
    assert heads[0] == 1
    for prev, cur in zip(heads, heads[1:]):
        assert cur <= prev + 1, f"heading jump {prev}->{cur} in {name}"


@pytest.mark.parametrize("name", FULL_PAGES)
def test_head_meta_and_skip_link(pages, name):
    html, dom, page = pages[name]
    assert dom.one("title").all_text().strip() == page["title"]  # page titles carry the product name; no suffix is appended
    assert dom.one("link", rel="canonical").attrs["href"] == page["canonical"]
    names = {n.attrs.get("name") or n.attrs.get("property") for n in dom.find_all("meta")}
    assert {"description", "og:title", "og:description", "og:image", "og:url", "twitter:card"} <= names
    skip = dom.one("a", **{"class": "skip-link"})
    target = skip.attrs["href"].lstrip("#")
    mains = dom.find_all("main")
    assert len(mains) == 1 and mains[0].attrs["id"] == target
    assert "data-theme" in html and "localStorage" in html  # theme init snippet


@pytest.mark.parametrize("name", FULL_PAGES)
def test_chrome_nav_theme_footer(pages, name):
    html, dom, page = pages[name]
    btn = dom.one("button", **{"class": "nav-menu"})
    assert btn.attrs["aria-controls"] == "site-nav-links" and btn.attrs["aria-expanded"] == "false"
    ul = dom.one("ul", id="site-nav-links")
    labels = [a.all_text().strip() for a in ul.walk() if a.tag == "a"]
    assert labels == ["Rankings", "Models", "Plans", "Benchmarks", "Methodology", "Changelog", "Data"]
    assert ul.walk() and [a.attrs["href"] for a in ul.walk() if a.tag == "a"][1] == "/models/"
    assert dom.one("button", id="theme-toggle").attrs["aria-label"] == "Toggle theme"
    assert dom.find_all("footer")
    srcs = [n.attrs.get("src", "") for n in dom.find_all("script", type="module")]
    assert srcs == page["scripts"]  # each page loads exactly its boot module
    assert dom.one("body").attrs["data-page"] == page["key"]
    assert "data-nav-toggle" in btn.attrs and "data-theme-toggle" in dom.one("button", id="theme-toggle").attrs
    assert "vr-theme" in html  # the inline snippet reads the key the scripts write


@pytest.mark.parametrize("name", FULL_PAGES)
def test_images_have_alt_and_no_inline_handlers(pages, name):
    html, dom, _ = pages[name]
    for img in dom.find_all("img"):
        assert "alt" in img.attrs
    for n in dom.root.walk():
        for a in n.attrs:
            assert not a.startswith("on"), f"inline handler {a} on {n.tag}"
    assert "javascript:" not in html


@pytest.mark.parametrize("name", FULL_PAGES)
def test_untrusted_strings_escaped(pages, name):
    html, _, _ = pages[name]
    assert "<b>x</b>" not in html
    if name not in ("rankings", "methodology", "data", "benchmarks"):
        assert "&lt;b&gt;x&lt;/b&gt;" in html


# template -> (view-model key, id of the embedded <script type="application/json">):
# rankings-data is rankings.json (answer page, instrument); page-data is the page's own document
EMBED = {
    "index": ("rankingsJson", "rankings-data"), "rankings": ("rankingsJson", "rankings-data"), "plans": ("plansJson", "page-data"),
    "benchmarks": ("benchmarksJson", "page-data"), "benchmark_tb4": ("tb4Json", "page-data"), "changelog": ("changelogJson", "page-data"),
}


@pytest.mark.parametrize("name,spec", sorted(EMBED.items()))
def test_embedded_json_equals_fixture(pages, name, spec):
    key, element_id = spec
    _, dom, page = pages[name]
    data = dom.one("script", id=element_id)
    assert data.attrs["type"] == "application/json"
    assert json.loads(data.all_text()) == page[key]
    assert "<" not in data.all_text()  # tojson must not emit raw tags


def test_basis_toggle_and_headlines(pages):
    for name in ("index", "rankings"):
        _, dom, _ = pages[name]
        group = dom.one("div", id="basis-toggle")
        assert "basis-toggle" in group.attrs["class"]
        assert group.attrs["role"] == "group" and group.attrs["aria-label"] == "Cost basis"
        btns = [n for n in group.walk() if n.tag == "button"]
        assert [(b.attrs["data-basis"], b.attrs["aria-pressed"]) for b in btns] == [("plan", "true"), ("api", "false")]
        assert [b.all_text().strip() for b in btns] == ["Plan ranking", "API ranking"]
        assert dom.find_all(**{"data-basis-label": True})
    _, dom, page = pages["index"]
    text = "".join(n.all_text() for n in dom.find_all(**{"data-basis-only": True}))
    assert page["headline"]["plan"] in text and page["headline"]["api"] in text


def test_cost_slider(pages):
    for name in ("index", "rankings"):
        _, dom, _ = pages[name]
        r = dom.one("input", id="cost-weight")
        assert r.attrs["type"] == "range" and r.attrs["min"] == "0" and r.attrs["max"] == "100" and r.attrs["step"] == "0.1"
        assert r.attrs["value"] == "18.9394" and r.attrs["aria-describedby"] == "cost-weight-note"
        assert dom.one("output", id="cost-weight-value").attrs["for"] == "cost-weight"
        assert dom.one(id="cost-weight-note")


def test_rankings_instrument(pages):
    _, dom, page = pages["rankings"]
    table = dom.one("table", id="rankings-table")
    assert table.attrs["data-basis"] == "plan"
    head = dom.one("thead", id="rankings-head")  # server-rendered skeleton: default columns only; the script refills it
    ths = [n for n in head.walk() if n.tag == "th"]
    assert [t.attrs["data-col"] for t in ths] == [c["key"] for c in page["columns"] if c["default"]]
    for th in ths:
        assert th.attrs["scope"] == "col" and "aria-sort" in th.attrs
        assert any(c.tag == "button" and "sort-btn" in c.attrs.get("class", "") for c in th.walk())
    assert dom.one("th", **{"data-col": "overall"}).attrs["aria-sort"] == "descending"
    assert dom.one("tbody", id="rankings-body")
    assert dom.find_all(**{"data-state": "loading"})
    assert "hidden" in dom.one(id="rankings-empty").attrs and dom.one(id="rankings-error").attrs["role"] == "alert"
    assert not dom.find_all("template")  # rows are built by assets/js/rankings.js
    form = dom.one("form", id="filters")
    assert form.attrs["method"] == "get"
    names = {}
    for n in form.walk():
        if n.tag == "input":
            names.setdefault(n.attrs.get("name"), []).append(n)
    assert len(names["provider"]) == 3 and len(names["grade"]) == 5
    assert not any("checked" in n.attrs for n in names["provider"] + names["grade"])  # none selected = no filter
    assert {r.attrs["value"] for r in names["route"]} == {"all", "eligible", "fallback"}
    assert names["cov"][0].attrs["type"] == "range" and names["q"]
    assert dom.one("output", id="filter-cov-value")
    picker = dom.one("fieldset", id="column-picker")
    assert any(n.attrs.get("id") == "column-picker-list" for n in picker.walk())
    assert len(dom.find_all(**{"data-action": "reset-filters"})) == 2
    drawer = dom.one(id="compare-drawer")
    assert any(n.attrs.get("id") == "compare-body" for n in drawer.walk())
    assert any(n.attrs.get("id") == "compare-clear" for n in drawer.walk())
    assert dom.one("a", id="export-csv") and dom.one("a", id="export-json")
    assert dom.one("button", **{"data-share": True})
    tabs = [n.attrs["data-chart-tab"] for n in dom.find_all("button", role="tab")]
    assert tabs == ["pareto", "decomposition", "displacement", "frontier2", "bubble", "heatmap"]
    for key in tabs:
        panel = dom.one("div", **{"data-chart-panel": key})
        assert any(n.attrs.get("data-chart") == key for n in panel.walk())  # the summary sits beside the chart in its panel
        assert any("data-chart-summary" in n.attrs for n in panel.walk())


def test_models_index(pages):
    _, dom, page = pages["models"]
    rows = [n for n in dom.one("tbody").walk() if n.tag == "tr"]
    assert [r.attrs["data-slug"] for r in rows] == [m["slug"] for m in page["models"]]
    links = [n.attrs["href"] for n in dom.one("tbody").walk() if n.tag == "a"]
    assert links == [f"/models/{m['slug']}/" for m in page["models"]]
    assert "not ranked" in rows[2].all_text()
    assert [c.tag for c in dom.one("tr", **{"data-slug": "gamma"}).children].count("td") == 5


def test_answer_page(pages):
    _, dom, page = pages["index"]
    picks = dom.one("section", id="picks")
    arts = [n for n in picks.walk() if n.tag == "article"]
    assert [a.attrs["data-pick"] for a in arts] == ["value", "other", "budget"]
    for a in arts:
        for hook in ("data-pick-label", "data-pick-name", "data-pick-reason", "data-pick-score"):
            assert any(hook in n.attrs for n in a.walk()), hook
    plan = page["picks"]["plan"]
    labels = [n.all_text().strip() for n in picks.walk() if "data-pick-label" in n.attrs]
    assert labels == [plan[kind]["label"] for kind in ("value", "other", "budget")]
    assert len(set(labels)) == 3
    scores = [n.all_text().strip() for n in picks.walk() if "data-pick-score" in n.attrs]
    assert scores == [f"{plan[kind]['score']:.1f}{plan[kind]['unit']}" for kind in ("value", "other", "budget")]
    table = dom.one("table", id="answer-table")
    assert [t.attrs["scope"] for t in table.walk() if t.tag == "th"]
    assert not dom.find_all("template")
    assert dom.one("tbody", id="index-body")
    assert all("data-col" in n.attrs and "data-label" in n.attrs for n in table.walk() if n.tag == "td")
    chart = dom.one("div", **{"data-chart": "pareto"})
    assert chart.attrs["role"] == "img" and chart.attrs["aria-label"]
    assert chart.attrs["data-chart-summary-target"] == "pareto-summary"
    summary = dom.one("p", id="pareto-summary")
    assert "data-chart-summary" in summary.attrs
    tabs = dom.one("div", role="tablist")
    tab = [n for n in tabs.walk() if n.tag == "button"][0]
    assert len(dom.find_all("a", **{"data-pick-name": True})) == 3  # the script rewrites the name link in place
    assert tab.attrs["role"] == "tab" and tab.attrs["data-chart-tab"] == "pareto" and tab.attrs["aria-selected"] == "true"
    # server-rendered fallback rows, plan order, names escaped
    assert "Alpha <b>x</b> One" in "".join(n.all_text() for n in table.walk())


def test_badge_partial(env):
    t = env.from_string('{% from "partials/badge.html" import badge %}{{ badge("claim") }}{{ badge("missing") }}')
    dom = Dom()
    dom.feed(t.render())
    spans = dom.find_all("span")
    assert [s.attrs["class"] for s in spans] == ["badge badge-claim", "badge badge-missing"]
    assert all(s.attrs["title"] for s in spans)


def test_model_page(pages):
    _, dom, page = pages["model"]
    table = dom.one("table", id="dimension-table")
    heads = [t.all_text().strip() for t in table.walk() if t.tag == "th" and t.attrs.get("scope") == "col"]
    assert heads[:4] == ["Dimension", "Value", "Unit", "Normalised"]
    badges = [n.attrs["class"] for n in table.walk() if n.tag == "span" and "badge" in n.attrs.get("class", "")]
    assert "badge badge-measured" in badges and "badge badge-missing" in badges
    assert any(n.tag == "a" and n.attrs.get("href") == "https://example.test/deepswe" for n in table.walk())
    assert any(n.tag == "details" for n in table.walk())
    assert dom.one("section", id="plan-routes") and dom.one("section", id="rank-history")


def test_methodology_and_faq(pages):
    _, dom, page = pages["methodology"]
    faqs = dom.find_all("details", **{"class": "faq"})
    assert len(faqs) == len(page["faq"])
    assert dom.one("section", id="worked-example")
    assert "75.7" in dom.one("section", id="worked-example").all_text()
    assert dom.one("section", id="limitations")


def test_data_page_lists_files(pages):
    _, dom, page = pages["data"]
    hrefs = [n.attrs["href"] for n in dom.find_all("a")]
    for f in page["files"]:
        assert f["path"] in hrefs


def test_tb4_sections(pages):
    _, dom, _ = pages["benchmark_tb4"]
    for sid in ("score-vs-cost", "official-rows", "provider-claims", "coverage"):
        assert dom.one("section", id=sid)
    assert dom.one("div", **{"data-chart": "tb4"})


def test_tb4_row_without_a_published_cost_renders_not_published(env):
    page = load("benchmark_tb4")
    page["tb4Json"]["rows"][1]["costUsd"] = None
    html = env.get_template("benchmark_tb4.html").render(site=load("_site"), page=page)
    dom = Dom()
    dom.feed(html)
    cells = [n.all_text().strip() for n in dom.one("section", id="official-rows").walk() if n.tag == "td" and "cell-num" in n.attrs.get("class", "")]
    assert "Not published" in cells and "$3,300" in cells


def test_redirect_stub(env):
    _, dom, page = render(env, "redirect")
    meta = [n for n in dom.find_all("meta") if n.attrs.get("http-equiv", "").lower() == "refresh"]
    assert len(meta) == 1 and meta[0].attrs["content"] == "0; url=" + page["target"]
    assert dom.one("link", rel="canonical").attrs["href"] == page["canonical"]
    assert any(n.attrs.get("href") == page["target"] for n in dom.find_all("a"))


def test_archive_banner_names_date(env):
    _, dom, page = render(env, "archive_banner")
    text = dom.one(**{"class": "archive-banner"}).all_text()
    assert "2026-07-15" in text or "July 15, 2026" in text
    assert dom.one("a", href="/benchmarks/")


def render_with(env, name, change):
    page = load(name)
    change(page)
    html = env.get_template(f"{name}.html").render(site=load("_site"), page=page)
    dom = Dom()
    dom.feed(html)
    return html, dom


def test_model_page_shows_the_aa_tier_badge_and_footnote(pages):
    _, dom, page = pages["model"]
    tier = dom.one("span", **{"data-aa-tier": "near"})
    assert tier.all_text().strip() == "Near frontier"  # text, not colour alone
    assert "Alpha Three (high)" in tier.attrs["title"] and "2 Index points" in tier.attrs["title"]
    note = dom.one("p", id="aa-footnote")
    assert page["frontier"]["footnote"] in note.all_text()
    assert dom.one("section", id="plan-routes").walk() and any(n is note for n in dom.one("section", id="plan-routes").walk())


def test_model_page_frontier_tier_labels_and_absence(env):
    _, dom = render_with(env, "model", lambda p: p["frontier"].update(tier="frontier", intelligenceGap=0))
    badge = dom.one("span", **{"data-aa-tier": "frontier"})
    assert badge.all_text().strip() == "AA frontier" and "on the rendered AA frontier" in badge.attrs["title"]
    _, dom = render_with(env, "model", lambda p: p["frontier"].update(tier=None, configuration=None, intelligenceGap=None, footnote=None))
    assert not dom.find_all("span", **{"data-aa-tier": "near"}) and not dom.find_all(id="aa-footnote")
    assert not [n for n in dom.root.walk() if "data-aa-tier" in n.attrs]


def test_rankings_legend_explains_the_frontier_badge(pages):
    _, dom, _ = pages["rankings"]
    legend = dom.one("section", id="frontier-legend")
    text = legend.all_text()
    assert "AA frontier" in text and "Near frontier" in text and "within 3 Index points" in text


def test_rankings_legend_gap_follows_the_view_model(env):
    _, dom = render_with(env, "rankings", lambda p: p.update(nearFrontierGap="4"))
    assert "within 4 Index points" in dom.one("section", id="frontier-legend").all_text()


def test_methodology_model_inclusion_section(pages, env):
    _, dom, page = pages["methodology"]
    section = dom.one("section", id="model-inclusion")
    text = section.all_text()
    for expected in ("Frontier rule text.", "Near rule text within 3 points.", "Policy sentence.", "Chart observed 2026-10-17T18:48:27Z.",
                     "2 required, 0 deferred", "GPT-6 Luna (max)", "Gemini 4 Argon (high)", "2 Index points below", "Pricing footnote.", "Alpha Three"):
        assert expected in text, expected
    assert any(a.attrs.get("href") == "#model-inclusion" for a in dom.find_all("a"))
    empty = {"frontierRule": "R.", "nearFrontierRule": "N.", "policyText": None, "observation": None, "nearFrontierStatus": None,
             "frontierFamilies": [], "nearFrontierFamilies": [], "footnotes": []}
    _, bare = render_with(env, "methodology", lambda p: p.update(modelInclusion=empty))
    bare_text = bare.one("section", id="model-inclusion").all_text()
    assert "R." in bare_text and "families" not in bare_text and "footnote" not in bare_text.lower()


def test_tier_badge_uses_singular_wording_for_a_one_point_gap(env):
    macros = env.get_template("partials/badge.html").module
    assert "within 1 Index point of the rendered AA frontier" in str(macros.tier_badge("near", "Alpha (low)", 1))
    assert "within 2 Index points of the rendered AA frontier" in str(macros.tier_badge("near", "Alpha (low)", 2))
