"""Characterization of the publication emitter: ``main`` against a repo copy
must reproduce the committed outputs byte for byte."""

import pytest

from valuerank import emit_docs
from valuerank.paths import ROOT

OUTPUTS = (
    "README.md",
    "methodology.md",
    "scores.md",
    "raw-data.md",
    "site/index.html",
    "site/coding-agents/index.html",
)


@pytest.mark.integration
def test_main_reproduces_committed_publication(repo_copy, pinned_clock, capsys):
    status = emit_docs.main(root=repo_copy, data=repo_copy / "data")

    assert status == 0
    for name in OUTPUTS:
        assert (repo_copy / name).read_bytes() == (ROOT / name).read_bytes(), name
    assert '"version": "v1.9.6"' in capsys.readouterr().out


def test_importing_the_module_has_no_side_effects(tmp_path, monkeypatch):
    import importlib

    monkeypatch.chdir(tmp_path)
    before = sorted(p.name for p in ROOT.glob("*.md"))
    importlib.reload(emit_docs)
    assert sorted(p.name for p in ROOT.glob("*.md")) == before
    assert callable(emit_docs.main)
