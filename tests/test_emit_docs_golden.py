"""Characterization of the Markdown emitter: ``main`` against a repo copy
must reproduce the committed Markdown byte for byte and leave site/ alone."""

import pytest

from test_emit_docs_support import MARKDOWN_OUTPUTS
from valuerank import emit_docs
from valuerank.paths import ROOT


def site_snapshot(root):
    return {str(path.relative_to(root)): path.read_bytes() for path in sorted((root / "site").rglob("*")) if path.is_file()}


@pytest.mark.integration
def test_main_reproduces_committed_markdown_and_never_touches_the_site(repo_copy, pinned_clock, capsys):
    site_before = site_snapshot(repo_copy)

    status = emit_docs.main(root=repo_copy, data=repo_copy / "data")

    assert status == 0
    for name in MARKDOWN_OUTPUTS:
        assert (repo_copy / name).read_bytes() == (ROOT / name).read_bytes(), name
    assert site_snapshot(repo_copy) == site_before
    assert '"version": "v2.0.0"' in capsys.readouterr().out


def test_importing_the_module_has_no_side_effects(tmp_path, monkeypatch):
    import importlib

    monkeypatch.chdir(tmp_path)
    before = sorted(p.name for p in ROOT.glob("*.md"))
    importlib.reload(emit_docs)
    assert sorted(p.name for p in ROOT.glob("*.md")) == before
    assert callable(emit_docs.main)
