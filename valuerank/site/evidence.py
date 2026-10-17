"""Evidence grades and per-dimension provenance for the multi-page site.

Public entry points
-------------------
``GRADES``                         ordered grade names, best to worst (``measured`` .. ``assumption``).
``worst_grade(grades)``            the worst grade among values that enter a score (``missing`` when none do).
``grade_for_source_type(...)``     grade of one metric value from its source type and status.
``route_grade(evidence_class)``    grade of one subscription route from its ``evidenceClass``.
``DIMENSION_META``                 per-dimension category, unit, benchmark link label and raw-value reader.
``dimension_evidence(...)``        source, date, evaluated variant, note and grade of one present value.

Grading rules (docs/site-data-contract.md, "Evidence grades"):

* Artificial Analysis metrics are ``measured`` unless the source type is an owner estimate or the model's
  ``intelligenceIndexStatus`` is ``estimated`` (``estimate``).
* Provider-published values (``model_provider_claim``) are ``claim``.
* Plan routes: ``controlled_account_workload_projection`` is ``measured``; ``user_reported_projection`` is
  ``estimate``; ``user_assumption`` and any unknown class are ``assumption``.
* A model's grade is the worst grade among the values that enter its score (subscription routes are graded
  separately on ``cost.route.grade``). Missing values never enter the grade.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import Any

from valuerank.emit_docs import BENCHMARK_URLS

GRADES = ("measured", "claim", "estimate", "assumption")

_ROUTE_GRADES = {
    "controlled_account_workload_projection": "measured",
    "user_reported_projection": "estimate",
    "user_assumption": "assumption",
}


def worst_grade(grades) -> str:
    """Return the worst of ``grades`` ignoring ``missing``; ``missing`` when nothing remains."""

    present = [grade for grade in grades if grade in GRADES]
    return max(present, key=GRADES.index) if present else "missing"


def grade_for_source_type(source_type: str | None, status: str | None = None) -> str:
    """Grade one metric value: owner estimate or ``estimated`` status, provider claim, else measured."""

    if status == "estimated" or source_type == "benchmark_owner_estimate":
        return "estimate"
    if source_type == "model_provider_claim":
        return "claim"
    return "measured"


def route_grade(evidence_class: str | None) -> str:
    """Grade a subscription route; unknown evidence classes are conservatively ``assumption``."""

    return _ROUTE_GRADES.get(evidence_class, "assumption")


def _percent(value):
    return None if value is None else round(value * 100, 2)


def _field(name: str, scale: Callable[[Any], Any] = lambda value: value) -> Callable[[Mapping], Any]:
    return lambda model: scale(model.get(name))


def _bug_hunt(model: Mapping):
    record = model.get("bugHunt") or {}
    return record.get("fixedOf105") if record.get("matched") is True else None


DIMENSION_META: dict[str, dict[str, Any]] = {
    "costComposite": {"category": "cost", "unit": "USD per Index run", "urlLabel": None, "raw": _field("aaEvalCost")},
    "omniNonHallucination": {"category": "rely", "unit": "% non-hallucination", "urlLabel": "AA-Omniscience Non-Hallucination Rate", "raw": _field("omniNonHallucination", _percent)},
    "omniAccuracy": {"category": "rely", "unit": "% accuracy", "urlLabel": "AA-Omniscience Accuracy", "raw": _field("omniAccuracy", _percent)},
    "terminalBenchV4": {"category": "code", "unit": "% resolved", "urlLabel": "Terminal-Bench 4.0", "raw": _field("terminalBenchV4Pct")},
    "deepswePassAt1": {"category": "code", "unit": "% pass@1", "urlLabel": "DeepSWE pass@1", "raw": _field("deepswePassAt1Pct")},
    "bugHuntFixedOf105": {"category": "code", "unit": "bugs fixed of 105", "urlLabel": "Bug Hunt Bench", "raw": _bug_hunt},
    "gdpvalV21": {"category": "prod", "unit": "Elo", "urlLabel": "GDPval-AA v2.1", "raw": _field("gdpvalV21")},
    "automationBenchAA": {"category": "prod", "unit": "% score", "urlLabel": "AutomationBench-AA", "raw": _field("automationBenchAA", _percent)},
    "speed": {"category": "prod", "unit": "tokens per second", "urlLabel": "AA output speed (tok/s)", "raw": _field("speed")},
    "intelligenceIndex": {"category": "intel", "unit": "Index points", "urlLabel": "AA Intelligence Index", "raw": _field("intelligenceIndex")},
    "hle": {"category": "intel", "unit": "% accuracy", "urlLabel": "HLE", "raw": _field("hle", _percent)},
    "gpqaDiamond": {"category": "intel", "unit": "% accuracy", "urlLabel": "GPQA Diamond (legacy)", "raw": _field("gpqaDiamond", _percent)},
    "scicode": {"category": "intel", "unit": "% score", "urlLabel": "SciCode", "raw": _field("scicode", _percent)},
    "critpt": {"category": "intel", "unit": "% score", "urlLabel": "CritPt", "raw": _field("critpt", _percent)},
    "aaLcr": {"category": "language", "unit": "% accuracy", "urlLabel": "AA-LCR v1.1", "raw": _field("aaLcr", _percent)},
    "livebenchInstructionFollowing": {"category": "language", "unit": "score", "urlLabel": "LiveBench", "raw": _field("livebenchInstructionFollowing")},
}


def dimension_url(key: str) -> str | None:
    """Public benchmark page for a dimension (``None`` for the cost dimension)."""

    label = DIMENSION_META[key]["urlLabel"]
    return BENCHMARK_URLS[label] if label else None


def raw_value(key: str, model: Mapping):
    """Raw display value of ``key`` for a ``data/scores.json`` model row (``None`` when missing)."""

    return DIMENSION_META[key]["raw"](model)


def _day(timestamp: str | None) -> str | None:
    return timestamp[:10] if timestamp else None


def _join(*parts) -> str | None:
    return " / ".join(str(part) for part in parts if part) or None


def dimension_evidence(key: str, model: Mapping, context: Mapping) -> dict[str, Any]:
    """Source, observation date, evaluated variant, note and grade for a *present* value.

    ``context`` carries ``scores`` (data/scores.json), ``aaSources`` (this model's AA ``metricSources``),
    ``livebench`` (data/livebench.json) and ``tb4`` (data/tb4.json).
    """

    scores = context["scores"]
    if key == "deepswePassAt1":
        config = model["deepsweScoreConfig"]
        return {
            "source": {"name": scores["deepsweSource"]["title"], "url": config.get("sourceUrl") or scores["deepsweSource"]["url"]},
            "observedAt": config.get("observedAt"),
            "evaluatedVariant": _join(config.get("agent"), config.get("model"), config.get("effort")),
            "note": config.get("matchNote"),
            "grade": "measured",
        }
    if key == "bugHuntFixedOf105":
        record = model["bugHunt"]
        return {
            "source": {"name": "Bug Hunt Bench", "url": record.get("sourceUrl")},
            "observedAt": record.get("observedAt"),
            "evaluatedVariant": record.get("evaluatedModel"),
            "note": record.get("note"),
            "grade": grade_for_source_type(record.get("sourceType")),
        }
    if key == "terminalBenchV4":
        if model.get("terminalBenchV4SourceType") == "model_provider_claim":
            claim = model["terminalBenchV4Claim"]
            return {
                "source": {"name": f"{claim['publisher']} provider claim", "url": claim["sourceUrl"]},
                "observedAt": claim.get("publishedOn"),
                "evaluatedVariant": claim.get("evaluatedModel"),
                "note": claim.get("caveat"),
                "grade": "claim",
            }
        return {
            "source": {"name": "Terminal-Bench 4.0 leaderboard", "url": context["tb4"]["source"]["targetUrl"]},
            "observedAt": _day(context["tb4"].get("observedAt")),
            "evaluatedVariant": _join(model.get("terminalBenchV4Agent"), model.get("terminalBenchV4Model")),
            "note": None,
            "grade": grade_for_source_type(model.get("terminalBenchV4SourceType")),
        }
    if key == "livebenchInstructionFollowing":
        document = context["livebench"]
        return {
            "source": {"name": f"LiveBench release {document['release']}", "url": document["source"]["homepage"]},
            "observedAt": _day(document.get("observedAt")),
            "evaluatedVariant": model.get("livebenchModel"),
            "note": None,
            "grade": "measured",
        }
    if key == "costComposite":
        selection = model.get("frontierSelection") or {}
        return {
            "source": {"name": "Artificial Analysis total cost to run the Intelligence Index", "url": selection.get("url") or model["aaUrl"]},
            "observedAt": _day((scores.get("frontierSelection") or {}).get("capturedAt")),
            "evaluatedVariant": model.get("aaVariant"),
            "note": model.get("aaFrontierFootnote"),
            "grade": "measured",
        }
    source = context["aaSources"].get(key) or {}
    status = model.get("intelligenceIndexStatus") if key == "intelligenceIndex" else None
    return {
        "source": {"name": scores.get("benchmarkVersion", "Artificial Analysis"), "url": source.get("sourceUrl") or model["aaUrl"]},
        "observedAt": _day(source.get("observedAt")),
        "evaluatedVariant": model.get("aaVariant"),
        "note": f"Display precision: {source['precision']}." if source.get("precision") else None,
        "grade": grade_for_source_type(source.get("sourceType"), status),
    }
