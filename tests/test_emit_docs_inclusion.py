"""The generated Markdown states the two-part model-inclusion policy from the snapshot data."""

import pytest

from test_emit_docs_support import edit_json, emit
from test_emit_docs_units import FOOTNOTE, SELECTION

pytestmark = pytest.mark.integration


def with_policy(document):
    document["frontierSelection"] = {**document["frontierSelection"], **SELECTION}
    document["models"][0]["aaFrontierFootnote"] = FOOTNOTE


def test_readme_and_methodology_carry_the_model_inclusion_passage(repo_copy, pinned_clock):
    edit_json(repo_copy, "scores.json", with_policy)

    emit(repo_copy)

    for name in ("README.md", "methodology.md"):
        text = (repo_copy / name).read_text()
        assert text.count("## Model inclusion") == 1, name
        assert "**Near-frontier rule.**" in text and "Within 3 Index points of the frontier at its cost." in text
        assert "- Gemini 4 Argon: Gemini 4 Argon (high), 2 Index points below the frontier" in text
        assert FOOTNOTE in text
    assert "near-frontier" in (repo_copy / "scores.md").read_text()
    assert "see Model inclusion" in (repo_copy / "README.md").read_text()


def without_policy_data(document):
    document.pop("frontierSelection", None)
    for model in document["models"]:
        model.pop("aaFrontierFootnote", None)


def test_passage_without_new_data_states_only_the_rules(repo_copy, pinned_clock):
    edit_json(repo_copy, "scores.json", without_policy_data)

    emit(repo_copy)

    text = (repo_copy / "methodology.md").read_text()
    assert "## Model inclusion" in text and "**Frontier rule.**" in text
    assert "Near-frontier families" not in text and "AA footnote" not in text


def test_emitter_stays_idempotent_with_the_passage(repo_copy, pinned_clock):
    edit_json(repo_copy, "scores.json", with_policy)
    emit(repo_copy)
    first = {name: (repo_copy / name).read_bytes() for name in ("README.md", "methodology.md", "scores.md")}

    emit(repo_copy)

    assert {name: (repo_copy / name).read_bytes() for name in first} == first
