"""Regression tests for defects found while reviewing the site generators."""

import json
import re
from pathlib import Path

from valuerank.site import build

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "site" / "templates"
EVIL = "Evil</script><script>alert(1)</script>"


def fixture(name):
    return json.loads((FIXTURES / f"{name}.json").read_text())


def test_embedded_page_json_cannot_break_out_of_its_script_element():
    page = fixture("benchmark_tb4")
    page["tb4Json"]["rows"][0]["model"] = EVIL
    page["tb4Json"]["rows"][0]["baseModel"] = "Evil & <co> 'quoted'"

    html = build.render(build.jinja_env(), "benchmark_tb4.html", {"site": fixture("_site"), "page": page})

    assert "</script><script>alert(1)" not in html
    embed = re.search(r'<script type="application/json" id="page-data">(.*?)</script>', html, re.S).group(1)
    assert "<" not in embed and ">" not in embed
    assert "\\u003c/script\\u003e" in embed and "\\u0026" in embed
    parsed = json.loads(embed)
    assert parsed["rows"][0]["model"] == EVIL
    assert parsed["rows"][0]["baseModel"] == "Evil & <co> 'quoted'"
