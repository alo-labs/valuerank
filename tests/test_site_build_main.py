"""End-to-end generation of the site into a temporary directory."""

import json
import re
import runpy
import shutil

import pytest

from valuerank.paths import ROOT
from valuerank.site import build

SITE_DIR = ROOT / "site"
ARCHIVE_PATH = "/archive/coding-agents-v0.3/"
CORE_CARD_KEYS = {
    "/": "index",
    "/rankings/": "rankings",
    "/rankings/ai-coding-daily/": "rankings",  # O53: every ranking's page shares the rankings card
    "/rankings/common-leaves/": "rankings",  # O121: the diagnostic ranking's page too
    "/models/": "models",
    "/plans/": "plans",
    "/benchmarks/": "benchmarks",
    "/benchmarks/terminal-bench-4/": "tb4",
    "/methodology/": "methodology",
    "/changelog/": "changelog",
    "/data/": "data",
}


def expected_share_card(path: str) -> str:
    """The share card, as a site path, that the generated page at ``path`` must reference."""

    if path in CORE_CARD_KEYS:
        return f"/og/{CORE_CARD_KEYS[path]}.png"
    if path == ARCHIVE_PATH:
        return "/og/archive.png"
    assert path.startswith("/models/"), path
    return f"/og/models/{path.split('/')[2]}.png"


def catalogued_paths() -> list[str]:
    from valuerank.site import viewmodel

    return [path for path, _template, _page in build.pages(viewmodel.build_bundle())] + [ARCHIVE_PATH]


def meta_content(html: str, attribute: str) -> str:
    match = re.search(rf'<meta {attribute} content="([^"]*)"', html)
    assert match is not None, attribute
    return match.group(1)


@pytest.fixture(scope="module")
def generated(tmp_path_factory):
    out = tmp_path_factory.mktemp("site")
    # Generate from the committed snapshots; nothing is written into the repository.
    assert build.main(out=out) == 0
    return out


def test_every_page_in_the_catalogue_is_written_once(generated):
    from valuerank.site import viewmodel

    bundle = viewmodel.build_bundle()
    for path, _template, _page in build.pages(bundle):
        target = generated.joinpath(*[part for part in path.split("/") if part]) / "index.html"
        assert target.is_file(), path
        html = target.read_text()
        assert html.count("<h1") == 1, path
        assert f'<link rel="canonical" href="{build.BASE_URL}{path}">' in html, path
    assert len([d for d in (generated / "models").iterdir() if d.is_dir()]) == len(bundle.models)
    assert (generated / "models" / "index.html").is_file()


def test_public_data_assets_redirects_archive_and_sitemap_are_written(generated):
    rankings = json.loads((generated / "data" / "rankings.json").read_text())
    assert rankings["defaultBasis"] == "plan"
    assert (generated / "data" / "models" / "gpt-6-1-sol.json").is_file()
    assert (generated / "assets" / "css" / "site.css").is_file()
    assert (generated / "assets" / "js" / "app.js").is_file()
    assert 'url=/benchmarks/terminal-bench-4/' in (generated / "tb4" / "index.html").read_text()
    assert 'url=/archive/coding-agents-v0.3/' in (generated / "coding-agents" / "index.html").read_text()
    archived = (generated / "archive" / "coding-agents-v0.3" / "index.html").read_text()
    assert "archive-banner" in archived and "2026-10-18" in archived
    sitemap = (generated / "sitemap.xml").read_text()
    assert sitemap.count("<url>") == len(build.pages(__import__("valuerank.site.viewmodel", fromlist=["x"]).build_bundle())) + 1
    assert (generated / "robots.txt").read_text().startswith("User-agent: *")


def test_catalogue_gives_every_page_a_key_and_its_boot_module(generated):
    from valuerank.site import viewmodel

    pages = {path: page for path, _template, page in build.pages(viewmodel.build_bundle())}
    assert len(pages) == 73 and "/models/" in pages and "/rankings/ai-coding-daily/" in pages
    assert pages["/rankings/ai-coding-daily/"]["scripts"] == ["/assets/js/pages/rankings.js"] and pages["/rankings/ai-coding-daily/"]["heading"] == "AI Coding Daily ranking"
    assert pages["/"]["scripts"] == ["/assets/js/pages/index.js"]
    assert pages["/rankings/"]["scripts"] == ["/assets/js/pages/rankings.js"]
    assert pages["/benchmarks/terminal-bench-4/"]["scripts"] == ["/assets/js/pages/tb4.js"]
    assert pages["/models/gpt-6-1-sol/"]["scripts"] == ["/assets/js/pages/static.js"]
    assert pages["/methodology/"]["key"] == "methodology" and pages["/models/gpt-6-1-sol/"]["key"] == "model"
    for path, page in pages.items():
        for script in page["scripts"]:
            assert (generated / script.lstrip("/")).is_file(), (path, script)
    nav = {item["key"]: item["href"] for item in build.NAV}
    assert nav["models"] == "/models/"


def test_redirects_and_archive_banner_use_the_page_variables(generated):
    stub = (generated / "tb4" / "index.html").read_text()
    assert f'<link rel="canonical" href="{build.BASE_URL}/benchmarks/terminal-bench-4/">' in stub
    archived = (generated / "archive" / "coding-agents-v0.3" / "index.html").read_text()
    assert 'href="/benchmarks/"' in archived and "archived on 2026-10-18" in archived


def test_pages_embed_the_data_the_scripts_read(generated):
    for path in ("index.html", "rankings/index.html"):
        html = (generated / path).read_text()
        start = html.index('<script type="application/json" id="rankings-data">') + len('<script type="application/json" id="rankings-data">')
        payload = json.loads(html[start:html.index("</script>", start)])
        assert payload["version"] == build.VERSION and len(payload["models"]) == 62


def test_stale_model_pages_are_removed_on_rebuild(tmp_path):
    out = tmp_path / "site"
    stale = out / "models" / "retired-model" / "index.html"
    stale.parent.mkdir(parents=True)
    stale.write_text("old")
    (out / "models" / "note.txt").write_text("not a page dir")

    removed = build.remove_stale_model_pages(out, {"gpt-6-1-sol"})

    assert removed == [out / "models" / "retired-model"]
    assert not stale.exists() and (out / "models" / "note.txt").exists()
    assert build.remove_stale_model_pages(tmp_path / "missing", set()) == []


def test_module_entry_point_generates_into_a_copy(repo_copy, monkeypatch, capsys):
    # runpy executes build.py afresh, so its ``from valuerank.paths import ...`` must see the patched paths.
    monkeypatch.setattr("valuerank.paths.ROOT", repo_copy)
    monkeypatch.setattr("valuerank.paths.DATA", repo_copy / "data")
    monkeypatch.setattr("valuerank.paths.SITE", repo_copy / "site")
    monkeypatch.setattr("sys.argv", ["valuerank.site.build"])
    shutil.rmtree(repo_copy / "site")  # the entry point must regenerate the copy, not inherit its files

    with pytest.raises(SystemExit) as exit_info:
        runpy.run_module("valuerank.site.build", run_name="__main__", alter_sys=True)

    assert exit_info.value.code == 0
    assert json.loads(capsys.readouterr().out)["pages"] == 73
    assert (repo_copy / "site" / "rankings" / "index.html").is_file()


def test_og_image_meta_points_each_generated_page_at_its_share_card(generated):
    cards = set()
    for path in catalogued_paths():
        html = generated.joinpath(*[part for part in path.split("/") if part], "index.html").read_text()
        card = expected_share_card(path)
        assert meta_content(html, 'property="og:image"') == build.BASE_URL + card, path
        assert meta_content(html, 'name="twitter:image"') == build.BASE_URL + card, path
        cards.add(card)
    # 10 core pages (the three rankings share one card), one card per roster model (61) and the archive page.
    assert len(cards) == 72


def test_share_cards_on_disk_are_exactly_the_ones_the_pages_reference():
    referenced = {expected_share_card(path) for path in catalogued_paths()}
    on_disk = {"/" + card.relative_to(SITE_DIR).as_posix() for card in (SITE_DIR / "og").rglob("*.png")}

    assert on_disk == referenced
