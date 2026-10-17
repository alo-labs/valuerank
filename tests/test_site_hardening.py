"""Regression tests for defects found while reviewing the site generators."""

import json
import re

import pytest

from valuerank import release, tb4_page
from valuerank.site_header import inject_header

PAGE = "<html><head></head><body><nav class='a'>one</nav><main>x</main></body></html>"


def test_inject_header_rejects_a_page_with_two_navs(tmp_path):
    page = tmp_path / "two.html"
    page.write_text(PAGE.replace("<main>", "<nav>two</nav><main>"))

    with pytest.raises(SystemExit, match="expected one nav .* found 2"):
        inject_header(page, "llm", "meta")


def test_inject_header_keeps_backslashes_in_meta_and_badge_literal(tmp_path):
    page = tmp_path / "page.html"
    page.write_text(PAGE)

    inject_header(page, "llm", r"C:\data \new", badge=r"v\1")

    html = page.read_text()
    assert r'<div class="vr-nav-meta">C:\data \new</div>' in html
    assert r'<span class="vr-nav-badge">v\1</span>' in html


def test_tb4_page_escapes_script_breakouts_inside_the_embedded_json(repo_copy, pinned_clock):
    tb4 = repo_copy / "data" / "tb4.json"
    document = json.loads(tb4.read_text())
    document["rows"][0]["model"] = "Evil</script><script>window.PWNED=1</script>"
    document["rows"][0]["baseModel"] = "Evil & <co>"
    tb4.write_text(json.dumps(document))

    tb4_page.main(root=repo_copy, data=repo_copy / "data")

    html = (repo_copy / "site" / "tb4" / "index.html").read_text()
    assert "</script><script>window.PWNED" not in html
    embed = re.search(r"const ENTRIES = (.*?);\n", html).group(1)
    assert "\\u003c/script\\u003e" in embed and "\\u0026" in embed
    assert json.loads(embed)[0]["model"] == "Evil</script><script>window.PWNED=1</script>"


def test_tb4_page_badge_carries_the_release_version(repo_copy, pinned_clock):
    tb4_page.main(root=repo_copy, data=repo_copy / "data")

    html = (repo_copy / "site" / "tb4" / "index.html").read_text()
    assert f'<span class="vr-nav-badge">{release.VERSION}</span>' in html
    assert "v1.6.0" not in html
