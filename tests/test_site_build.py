"""Mechanics of the site generator that do not depend on the view models."""

import json
from pathlib import Path

import pytest
from jinja2 import UndefinedError

from valuerank.site import build


def write(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return path


@pytest.fixture
def templates(tmp_path):
    root = tmp_path / "templates"
    write(root / "page.html", "<h1>{{ page.title }}</h1>{{ page.data | tojson }}")
    write(root / "redirect.html", '<meta http-equiv="refresh" content="0; url={{ page.target }}"><link rel="canonical" href="{{ page.canonical }}">{{ page.title }}')
    write(root / "archive_banner.html", '<aside class="archive-banner">Archived {{ page.archiveDate }} ({{ page.archiveHref }}): {{ page.note }}</aside>')
    return root


def test_jinja_environment_escapes_and_fails_on_undefined(templates):
    env = build.jinja_env(templates)

    assert build.render(env, "page.html", {"page": {"title": "<b>x</b>", "data": {"a": 1}}}) == "<h1>&lt;b&gt;x&lt;/b&gt;</h1>{\"a\": 1}"
    with pytest.raises(UndefinedError):
        build.render(env, "page.html", {"page": {"data": {}}})


def test_copy_assets_mirrors_the_tree_and_removes_stale_files(tmp_path):
    source = tmp_path / "assets"
    write(source / "css" / "site.css", "body{}")
    write(source / "js" / "charts" / "pareto.js", "export {}")
    target = tmp_path / "site" / "assets"
    write(target / "js" / "old.js", "stale")

    copied = build.copy_assets(source, target)

    assert sorted(path.relative_to(target).as_posix() for path in copied) == ["css/site.css", "js/charts/pareto.js"]
    assert not (target / "js" / "old.js").exists()
    assert (target / "css" / "site.css").read_text() == "body{}"
    fresh = build.copy_assets(source, tmp_path / "fresh")
    assert [path.name for path in fresh] == ["site.css", "pareto.js"]


def test_write_redirect_renders_a_stub_pointing_at_the_new_location(templates, tmp_path):
    env = build.jinja_env(templates)
    out = tmp_path / "site" / "tb4" / "index.html"

    build.write_redirect(env, out, target="/benchmarks/terminal-bench-4/", title="Terminal-Bench 4.0 moved", canonical="https://x.test/benchmarks/terminal-bench-4/")

    text = out.read_text()
    assert 'content="0; url=/benchmarks/terminal-bench-4/"' in text
    assert 'rel="canonical" href="https://x.test/benchmarks/terminal-bench-4/"' in text
    assert "Terminal-Bench 4.0 moved" in text


def test_archive_legacy_page_injects_the_banner_after_the_body_tag(templates, tmp_path):
    env = build.jinja_env(templates)
    legacy = write(tmp_path / "legacy.html", '<html><body class="x">\n<nav>old</nav><main>content</main></body></html>')
    out = tmp_path / "site" / "archive" / "coding-agents-v0.3" / "index.html"

    build.archive_legacy_page(env, legacy, out, archive_date="2026-10-18", archive_href="/benchmarks/", note="Frozen v0.3 snapshot.")

    text = out.read_text()
    assert text.index('<body class="x">') < text.index('<aside class="archive-banner">Archived 2026-10-18 (/benchmarks/): Frozen v0.3 snapshot.</aside>') < text.index("<nav>old</nav>")
    assert "<main>content</main>" in text


def test_archive_legacy_page_requires_a_body_tag(templates, tmp_path):
    env = build.jinja_env(templates)
    legacy = write(tmp_path / "legacy.html", "<html>no body here</html>")

    with pytest.raises(ValueError, match="<body"):
        build.archive_legacy_page(env, legacy, tmp_path / "out.html", archive_date="2026-10-18", archive_href="/benchmarks/", note="n")


def test_sitemap_and_robots_list_every_page_once(tmp_path):
    out = tmp_path / "site"

    build.write_sitemap(out, "https://valuerank.alolabs.dev", ["/", "/rankings/", "/models/gpt-6-1-sol/", "/rankings/"], lastmod="2026-10-08")
    build.write_robots(out, "https://valuerank.alolabs.dev")

    sitemap = (out / "sitemap.xml").read_text()
    assert sitemap.count("<url>") == 3
    assert "<loc>https://valuerank.alolabs.dev/models/gpt-6-1-sol/</loc>" in sitemap
    assert "<lastmod>2026-10-08</lastmod>" in sitemap
    assert (out / "robots.txt").read_text() == "User-agent: *\nAllow: /\nSitemap: https://valuerank.alolabs.dev/sitemap.xml\n"


def test_write_page_creates_directories_and_returns_the_site_path(tmp_path):
    out = tmp_path / "site"

    path = build.write_page(out, "/models/gpt-6-1-sol/", "<html></html>")

    assert path == out / "models" / "gpt-6-1-sol" / "index.html"
    assert path.read_text() == "<html></html>"
    assert build.write_page(out, "/", "x") == out / "index.html"


def test_write_json_is_deterministic_and_ends_with_a_newline(tmp_path):
    path = build.write_json(tmp_path / "data" / "x.json", {"b": 1, "a": "é"})

    assert path.read_text() == '{\n  "a": "é",\n  "b": 1\n}\n'
    assert json.loads(path.read_text()) == {"a": "é", "b": 1}
