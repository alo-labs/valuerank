"""E177: score-swing attribution by replaying the build one input class at a time."""

from __future__ import annotations

import copy

import pytest

from test_value_v3 import ALL_TASKS, CONFIGURATIONS, DAY, documents, fixture_ranking, page  # noqa: F401 (fixture_ranking is autouse)
from valuerank import swing_bridge as sb
from valuerank import value_v3 as v


def release(configurations, docs, frozen):
    state = {"configurations": configurations, "documents": docs}
    return {**state, "published": sb.replay_values(state, frozen, DAY)}


def baseline():
    docs = documents()
    frozen = v.freeze(v.assemble(CONFIGURATIONS, docs, release_day=DAY), frozen_at="2026-10-19")
    return docs, frozen


def test_replay_attributes_each_change_to_its_class_with_named_fields():
    docs, frozen = baseline()
    for item in docs["snapshot"]["pages"]:
        item["model"]["canonicalIntelligenceIndexTokenCount"] = {"input": 1e6, "output": 1e5}
    previous = release(CONFIGURATIONS, docs, frozen)
    changed = copy.deepcopy(docs)
    pages = {item["model"]["slug"]: item["model"] for item in changed["snapshot"]["pages"]}
    pages["b-max"]["gdpval"] = 2500.0  # a benchmark-record update
    for item in pages["a-max"]["intelligenceIndexEvaluations"]:
        item["costPerTask"] = 0.25  # token use
    pages["a-max"]["intelligenceIndexCost"].update(total=0.25 * sum(ALL_TASKS.values()), cacheRead=1.0)  # the Index total still reconciles
    changed["planRoutes"]["routes"][1]["valueMultiple"] = 4.0  # Plan evidence
    current = release(CONFIGURATIONS[:2], changed, frozen)  # c leaves the cohort
    result = sb.bridge(previous, current, frozen, DAY)
    assert result["order"] == [sb.METHOD_STEP, "price", "tokenUse", "benchmarkRecord", "planEvidence", "cohort"]
    assert result["exits"] == [{"row": "c", "status": "cohort exit"}] and result["admissions"] == []
    a, b = result["rows"]["a"], result["rows"]["b"]
    assert a["api"]["steps"][sb.METHOD_STEP] == pytest.approx(0.0) and a["api"]["replayResidual"] == pytest.approx(0.0)
    assert a["api"]["steps"]["tokenUse"] > 0 and a["api"]["steps"]["price"] == pytest.approx(0.0)
    assert a["api"]["tokenUseLabel"] == sb.CACHE_RATE_LABEL and b["api"]["tokenUseLabel"] == "token use"
    # Without published token totals a cache-read change is not separable from token use.
    assert sb._cache_rate_rows(release(CONFIGURATIONS, documents(), frozen), current) == set()
    assert b["api"]["steps"]["benchmarkRecord"] > 0 and b["plan"]["steps"]["planEvidence"] != 0
    assert sum(value for value in a["api"]["steps"].values()) == pytest.approx(a["api"]["swing"])
    assert set(a["api"]["orderDependence"]) == set(sb.ORDER)
    assert "snapshot:pages[model.slug=b-max].model.gdpval" in result["changedFields"]["benchmarkRecord"]
    assert result["changedFields"]["planEvidence"] == ["planRoutes"] and "snapshot:pages[model.slug=c-max]" not in result["changedFields"]["cohort"]
    assert "configurations" in result["changedFields"]["cohort"]
    assert result["status"] == "passed" and result["held"] == [] and all(item["attributed"] for item in a.values())


def test_an_unreproduced_swing_is_held_and_admissions_are_listed():
    docs, frozen = baseline()
    previous = release(CONFIGURATIONS[:2], docs, frozen)
    current = release(CONFIGURATIONS, docs, frozen)
    current["published"]["a"]["api"] += 10.0  # the published score no longer matches its own inputs
    result = sb.bridge(previous, current, frozen, DAY)
    assert result["admissions"] == [{"row": "c", "status": "cohort admission (no prior score)"}]
    assert result["rows"]["a"]["api"]["replayResidual"] == pytest.approx(-10.0) and result["rows"]["a"]["api"]["held"] is True
    assert result["status"] == "held: unattributed score swing" and result["held"] == ["a"]
    assert result["changedFields"]["cohort"] == ["configurations"]


def test_a_large_step_without_changed_fields_is_not_attributed():
    docs, frozen = baseline()
    previous = release(CONFIGURATIONS, docs, frozen)
    current = release(CONFIGURATIONS, docs, frozen)
    previous["published"]["a"]["api"] -= 8.0  # the method-and-clock step carries 8 points
    result = sb.bridge(previous, current, frozen, DAY)
    item = result["rows"]["a"]["api"]
    assert item["steps"][sb.METHOD_STEP] == pytest.approx(8.0) and item["swing"] == pytest.approx(8.0)
    assert item["attributed"] is True  # the method step is the versioned code change, not a data class
    assert result["rows"]["a"]["plan"]["swing"] == pytest.approx(0.0)


def test_unscoreable_values_and_class_ownership():
    assert sb._difference(None, 1.0) is None and sb._difference(2.0, 1.0) == 1.0
    assert sb._owner("price1mOutputTokens") == "price" and sb._owner("intelligenceIndexCost") == "tokenUse" and sb._owner("gdpval") == "benchmarkRecord"
    state = {"configurations": CONFIGURATIONS, "documents": documents()}
    current = {"configurations": CONFIGURATIONS, "documents": documents(snapshot={"pages": [page("a-max", 1.0, gdpval=None), page("b-max", 4.0), page("c-max", 0.5), page("d-max", 2.0)]})}
    del current["documents"]["snapshot"]["pages"][0]["model"]["gdpval"]
    applied = sb.apply_class(state, current, "benchmarkRecord")
    assert "gdpval" not in sb._pages(applied["documents"])["a-max"] and "d-max" not in sb._pages(applied["documents"])
    joined = sb.apply_class(applied, current, "cohort")
    assert "d-max" in sb._pages(joined["documents"])
    # A page the current release dropped is untouched until the cohort step removes it.
    shrunk = {"configurations": CONFIGURATIONS[:2], "documents": documents(snapshot={"pages": [page("a-max", 3.0), page("b-max", 4.0)]})}
    priced = sb.apply_class(state, shrunk, "tokenUse")
    assert "c-max" in sb._pages(priced["documents"]) and "c-max" not in sb._pages(sb.apply_class(priced, shrunk, "cohort")["documents"])
    with pytest.raises(ValueError, match="unclassified evidence documents"):
        sb._classified({**documents(), "extra": {}})
    # Every document the release bundle loads belongs to a class.
    from valuerank.paths import DATA
    sb._classified(v.load_documents(DATA))


def test_an_admitted_workload_change_is_a_migration():
    docs, frozen = baseline()
    previous = release(CONFIGURATIONS, docs, frozen)
    changed = copy.deepcopy(docs)
    # E267: the record is derived from the capture, so b loses it only when AA drops it; coverage falls below admission.
    changed["codingAgents"]["configurations"] = [item for item in changed["codingAgents"]["configurations"] if item["label"] != "Agent - B (max)"]
    changed["codingAgentsManifest"]["rows"].pop("Agent - B (max)")  # O64: the reviewed manifest records the removal
    current = {"configurations": CONFIGURATIONS, "documents": changed, "published": previous["published"]}
    result = sb.bridge(previous, current, frozen, DAY)
    assert result["status"] == sb.MIGRATION and result["rows"] == {} and "codingAgents" in result["changedFields"]["tokenUse"] and "codingAgentsManifest" in result["changedFields"]["tokenUse"]


def test_other_build_errors_propagate(monkeypatch):
    docs, frozen = baseline()
    previous = release(CONFIGURATIONS, docs, frozen)

    def broken(*_args, **_kwargs):
        raise ValueError("something else")

    monkeypatch.setattr(sb, "replay_values", broken)
    with pytest.raises(ValueError, match="something else"):
        sb.bridge(previous, previous, frozen, DAY)


def test_the_footnote_register_is_replayed_as_a_method_input():
    """I84 L1, I85 L2: every replay state reads the union of both releases' registers, current entries first."""

    old = {"configurations": [], "documents": {"aaFootnotes": {"notes": [{"text": "Old.", "kind": "not a pricing omission"}, {"text": "Both.", "kind": "pricing omission", "factor": 2.0}]}}}
    new = {"configurations": [], "documents": {"aaFootnotes": {"notes": [{"text": "Both.", "kind": "pricing omission", "factor": 3.0}, {"text": "New.", "kind": "not a pricing omission"}]}}}
    previous, current = sb._with_method(old, new)
    assert previous["documents"]["aaFootnotes"] == current["documents"]["aaFootnotes"]
    assert [(item["text"], item.get("factor")) for item in current["documents"]["aaFootnotes"]["notes"]] == [("Both.", 3.0), ("New.", None), ("Old.", None)]
    bare = {"configurations": [], "documents": {}}
    assert sb._with_method(bare, bare) == (bare, bare)
    only_old, _ = sb._with_method(old, bare)
    assert [item["text"] for item in only_old["documents"]["aaFootnotes"]["notes"]] == ["Old.", "Both."]


def test_a_swing_built_from_small_steps_must_name_the_steps_that_carry_it():
    """E275: three steps of 2.4, 2.4 and 2.2 make a 7-point swing; the largest steps covering 80% of it must be named."""

    steps = {sb.METHOD_STEP: 0.0, "price": -2.4, "tokenUse": -2.4, "benchmarkRecord": -2.2, "cohort": None}
    assert sb.covering_steps(steps, -7.0) == ["price", "tokenUse", "benchmarkRecord"]
    assert sb.covering_steps(steps, -4.0) == [] and sb.covering_steps(steps, None) == []
    assert sb.covering_steps({"price": -6.0, "tokenUse": -1.0}, -7.0) == ["price"]
