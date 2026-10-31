#!/usr/bin/env python3
"""Extract the current Artificial Analysis model payloads for the v1.6 cohort.

The public model pages contain the current model record in an escaped JSON
payload.  The older v1.3 extractor searched visible labels and consequently
mistook benchmark versions (for example, ``v2.1``) for scores.  This script
decodes the page's own full model object (see ``decode_page_model``) and keeps
the v5.0 source components separate from ValueRank's own score dimensions.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from valuerank.clock import iso_z
from urllib.parse import urlparse


from valuerank.paths import DATA, ROOT
AA_DIR = DATA / "aa"
MAPPING_PATH = DATA / "aa_mapping.json"
EXTRACT_PATH = AA_DIR / "aa_extract.json"
SNAPSHOT_PATH = AA_DIR / "aa_v432_snapshot.json"
OUTPUT_PATH = DATA / "aa_metrics.json"
COVERAGE_PATH = DATA / "coverage_matrix.json"

# AA Intelligence Index v5.0's evaluations and weights (AA's Intelligence Benchmarking methodology, read 2026-10-30; O132).
PRIMARY_EVALUATIONS = [
    {"key": "briefcaseElo", "label": "AA-Briefcase", "aaKey": "briefcaseBreakdown.overall.elo", "weightPct": 15},
    {"key": "automationBenchAA", "label": "AutomationBench-AA", "aaKey": "automationBenchPartialScore", "weightPct": 5},
    {"key": "gdpPdfAllPass", "label": "GDP.pdf", "aaKey": "gdpPdfAllPass", "weightPct": 5},
    {"key": "frontierCode20", "label": "FrontierCode 2.0", "aaKey": "frontierCode20", "weightPct": 15},
    {"key": "terminalBenchV40", "label": "Terminal-Bench 4.0 (AA evaluation)", "aaKey": "terminalBench40", "weightPct": 10},
    {"key": "terminalBenchScience", "label": "Terminal-Bench-Science 0.1", "aaKey": "terminalBenchScience", "weightPct": 15},
    {"key": "critptV2Hard", "label": "CritPt v2 (hard subset)", "aaKey": "critptAgenticHard", "weightPct": 10},
    {"key": "omniAccuracy", "label": "AA-Omniscience v1.1 Accuracy", "aaKey": "omniscienceBreakdown.accuracy", "weightPct": 10},
    {
        "key": "omniNonHallucination",
        "label": "AA-Omniscience v1.1 Non-Hallucination Rate",
        "aaKey": "omniscienceBreakdown.hallucinationRate",
        "weightPct": 5,
        "transform": "oneMinus",
    },
    {"key": "hleDiamond", "label": "HLE-Diamond", "aaKey": "hleDiamond", "weightPct": 10},
]

ADDITIONAL_FIELDS = [
    {"key": "gpqaDiamond", "label": "GPQA Diamond (legacy)", "aaKey": "gpqa"},
    {"key": "briefcaseNormalized", "label": "AA-Briefcase normalized (Elo-500)/2000", "aaKey": "briefcaseNormalizedDisplay"},
    {"key": "gdpvalV21Normalized", "label": "GDPval-AA v2.1 normalized (Elo-500)/2000", "aaKey": "gdpvalNormalizedDisplay"},
    # O136: run by AA outside the v5 Index and still published on its model pages; quality leaves of ValueRank's own.
    {"key": "gdpvalV21", "label": "GDPval-AA v2.1 Elo", "aaKey": "gdpval"},
    {"key": "aaLcr", "label": "AA-LCR v1.1", "aaKey": "lcr"},
]

# These fields are exposed by the page when available, but are not part of the
# current v5.0 weighted index. They are retained for auditability/coverage.
SUPPLEMENTAL_FIELDS = [
    "mlcrOverall",
    "harveyLab",
    "apexAgents",
    "mmmuPro",
    "livecodebench",
    "aime25",
    "analystAgent",
    "automationBenchPartialScore",
    "enterpriseOpsGym",
    "itBenchSre",
    "briefcaseRubricPassRate",
    "briefcaseTotalCost",
    "tauBanking",
    "terminalBenchV21",
]

NUMBER_RE = r"-?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
QUOTE = chr(92) + '"'  # a JSON-escaped double quote as it appears in the flight payload
LEGACY_MARKER = QUOTE + "currentModel" + QUOTE + ":{"


def json_value(obj: dict, path: str):
    value = obj
    for part in path.split("."):
        if not isinstance(value, dict):
            return None
        value = value.get(part)
    return value


def object_end(html: str, start: int):
    """Index just past the brace-balanced object opening at ``start`` (None if unterminated).

    The object is JSON escaped, but braces remain literal.  Model strings do
    not contain structural braces; depth counting is sufficient and avoids
    loading the multi-megabyte HTML into a second parser structure.
    """

    depth = 0
    for index in range(start, len(html)):
        if html[index] == "{":
            depth += 1
        elif html[index] == "}":
            depth -= 1
            if depth == 0:
                return index + 1
    return None


def decode_current_model(html: str) -> dict:
    """Return the page's escaped ``currentModel`` object."""

    marker_pos = html.find(LEGACY_MARKER)
    if marker_pos < 0:
        raise ValueError("currentModel marker not found")
    start = marker_pos + len(LEGACY_MARKER) - 1  # the marker ends with the object's opening brace
    end = object_end(html, start)
    if end is None:
        raise ValueError("currentModel object is unterminated")

    escaped = html[start:end]
    try:
        decoded = json.loads('"' + escaped + '"')
        model = json.loads(decoded)
    except json.JSONDecodeError as exc:
        raise ValueError(f"currentModel JSON decode failed: {exc}") from exc
    if not isinstance(model, dict) or not model.get("slug"):
        raise ValueError("decoded currentModel has no slug")
    return model


def slug_keyed_models(html: str, slug: str) -> list[dict]:
    """Decode every full model object in ``html`` whose ``slug`` is ``slug``.

    Artificial Analysis embeds one full model record per page (91-92 keys,
    including ``intelligenceIndexCost``) in the Next.js flight payload.  The same
    payload also repeats the slug in short catalogue entries
    (``{slug, name, releaseSlug}``), release summaries and nested ``release``
    blocks.  A candidate therefore counts only when the object that directly
    encloses an escaped ``"slug":"<slug>"`` has that slug *and* an
    ``intelligenceIndexCost`` key; undecodable fragments are skipped.
    """

    marker = QUOTE + "slug" + QUOTE + ":" + QUOTE + slug + QUOTE
    found: list[dict] = []
    position = html.find(marker)
    while position >= 0:
        start = html.rfind("{", 0, position)
        if start >= 0:
            end = object_end(html, start)
            if end is not None:
                try:
                    candidate = json.loads(json.loads('"' + html[start:end] + '"'))
                except json.JSONDecodeError:
                    candidate = None
                if (
                    isinstance(candidate, dict)
                    and candidate.get("slug") == slug
                    and "intelligenceIndexCost" in candidate
                ):
                    found.append(candidate)
        position = html.find(marker, position + 1)
    return found


def decode_page_model(html: str, slug: str) -> dict:
    """Return the full model object that an AA model page embeds for ``slug``.

    Current pages no longer wrap it in ``"currentModel":{``; the object is found
    by its slug (see ``slug_keyed_models``).  Pages that still carry the legacy
    marker are read with ``decode_current_model``; its object is accepted when
    its slug matches and must agree with any slug-keyed object.  A marker object
    for another slug is ignored when the slug-keyed object exists.

    Raises ``ValueError`` when no full object for ``slug`` exists, the legacy
    object belongs to a different slug or has none, or candidates disagree.
    """

    candidates = slug_keyed_models(html, slug)
    if LEGACY_MARKER in html:
        legacy = decode_current_model(html)
        if legacy["slug"] == slug:
            candidates.append(legacy)
        elif not candidates:
            raise ValueError(
                f"currentModel slug {legacy['slug']!r} does not match page slug {slug!r}"
            )
    if not candidates:
        raise ValueError(f"no full model object for slug {slug!r} found in page payload")
    if any(candidate != candidates[0] for candidate in candidates[1:]):
        raise ValueError(f"full model objects for slug {slug!r} disagree")
    return candidates[0]


def page_slug(url: str) -> str:
    """The model slug named by a model-page URL: its last path segment."""

    return urlparse(url).path.rstrip("/").split("/")[-1]


def summary_speed(text: str):
    """Extract only the current page's model-summary speed, preserving N/A."""

    summary = text.split("Model summary", 1)[-1][:2500]
    match = re.search(
        r"\bSpeed\s+(?:#\d+\s*/\s*\d+\s+)?(N/A|Unknown|" + NUMBER_RE + r")\s+Output tokens per second",
        summary,
        flags=re.IGNORECASE,
    )
    if not match or match.group(1).lower() in {"n/a", "unknown"}:
        return None
    return float(match.group(1))


def selected_page(entry: dict):
    url = entry["url"]
    slug = page_slug(url)
    html = AA_DIR / f"{entry['id']}__{slug}.html"
    text = AA_DIR / f"{entry['id']}__{slug}.txt"
    if not html.exists():
        matches = sorted(AA_DIR.glob(f"{entry['id']}__{slug}*.html"))
        if matches:
            html = matches[0]
    if not text.exists():
        matches = sorted(AA_DIR.glob(f"{entry['id']}__{slug}*.txt"))
        if matches:
            text = matches[0]
    if not html.exists() or not text.exists():
        raise FileNotFoundError(f"raw page snapshot missing for {entry['id']}: {url}")
    return slug, html, text


def clean_number(value):
    if value is None or isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return float(value)
    return None


def main() -> int:
    mapping = {item["id"]: item for item in json.loads(MAPPING_PATH.read_text())}
    extracted = json.loads(EXTRACT_PATH.read_text())
    claim_document = json.loads((DATA / "provider_claims.json").read_text())
    all_provider_claims = claim_document.get("claims", [])
    snapshot_document = json.loads(SNAPSHOT_PATH.read_text()) if SNAPSHOT_PATH.exists() else {}
    snapshot_pages = (
        snapshot_document.get("pages", [])
        if isinstance(snapshot_document, dict)
        else snapshot_document if isinstance(snapshot_document, list) else []
    )
    snapshot = {item["id"]: item for item in snapshot_pages}
    observed_at = iso_z()
    models = {}

    for entry in extracted:
        model_id = entry["id"]
        snapshot_entry = snapshot.get(model_id)
        html_path = None
        text_path = None
        if snapshot_entry:
            current = snapshot_entry["model"]
            source_url = snapshot_entry["url"]
            slug = current.get("slug") or model_id
            html = ""
            text = ""
        else:
            slug, html_path, text_path = selected_page(entry)
            html = html_path.read_text(errors="ignore")
            text = text_path.read_text(errors="ignore")
            current = decode_page_model(html, slug)
            source_url = entry["url"]
        expected_identity = mapping.get(model_id, {})
        expected_slug = expected_identity.get("aaSlug")
        expected_variant = expected_identity.get("aaVariant")
        if expected_slug and current.get("slug") != expected_slug:
            raise ValueError(f"AA source slug mismatch for {model_id}: expected {expected_slug}, got {current.get('slug')}")
        if expected_variant and (current.get("effort") or {}).get("slug") != expected_variant:
            raise ValueError(f"AA source variant mismatch for {model_id}: expected {expected_variant}")
        breakdown = current.get("omniscienceBreakdown") or {}
        cost = current.get("intelligenceIndexCost") or {}
        briefcase = current.get("briefcaseBreakdown") or {}
        metrics = {
            "briefcaseNormalized": clean_number(current.get("briefcaseNormalizedDisplay")),
            "gdpvalV21Normalized": clean_number(current.get("gdpvalNormalizedDisplay", current.get("gdpvalNormalized"))),
            "briefcaseElo": clean_number(
                current.get("briefcaseElo", json_value(briefcase, "overall.elo"))
            ),
            "intelligenceIndex": clean_number(current.get("intelligenceIndex")),
            "gdpvalV21": clean_number(current.get("gdpval")),
            "automationBenchAA": clean_number(current.get("automationBenchPartialScore")),
            "terminalBenchV40": clean_number(current.get("terminalBench40", current.get("terminalbench40"))),
            "frontierCode20": clean_number(current.get("frontierCode20")),
            "terminalBenchScience": clean_number(current.get("terminalBenchScience")),
            "gdpPdfAllPass": clean_number(current.get("gdpPdfAllPass")),
            "aaLcr": clean_number(current.get("lcr")),
            "hleDiamond": clean_number(current.get("hleDiamond")),
            "gpqaDiamond": clean_number(current.get("gpqa")),
            "critptV2Hard": clean_number(current.get("critptAgenticHard")),
            "omniAccuracy": clean_number(
                current.get("omniscienceAccuracy", breakdown.get("accuracy"))
            ),
            "omniNonHallucination": (
                clean_number(current.get("omniscienceNonHallucination"))
                if current.get("omniscienceNonHallucination") is not None
                else 1.0 - float(current["omniscienceHallucinationRate"])
                if current.get("omniscienceHallucinationRate") is not None
                else 1.0 - float(breakdown["hallucinationRate"])
                if breakdown.get("hallucinationRate") is not None
                else None
            ),
            "aaEvalCost": clean_number(current.get("aaEvalCost") if current.get("aaEvalCost") is not None else cost.get("total")),
            "speed": clean_number(
                current.get("speed") if current.get("speed") is not None else json_value(current, "outputSpeedVariance.median")
            ) if snapshot_entry else summary_speed(text),
        }
        if metrics["briefcaseNormalized"] is None and metrics["briefcaseElo"] is not None:
            metrics["briefcaseNormalized"] = (metrics["briefcaseElo"] - 500.0) / 2000.0
        selected_variant = (current.get("effort") or {}).get("slug")
        index_is_estimated = current.get("intelligenceIndexIsEstimated") is True
        source_observed_at = (
            snapshot_entry.get("capture", {}).get("observedAt")
            or snapshot_entry.get("capture", {}).get("capturedAt")
            or (snapshot_document.get("capturedAt") if isinstance(snapshot_document, dict) else None)
        ) if snapshot_entry else None
        metric_sources = {
            key: {
                "sourceType": "benchmark_owner",
                "sourceUrl": (
                    snapshot_entry.get("capture", {}).get("metricSourceUrls", {}).get(key)
                    or source_url
                ) if snapshot_entry else source_url,
                "observedAt": source_observed_at,
                "precision": (
                    snapshot_entry.get("capture", {}).get("metricPrecision", {}).get(key)
                    or snapshot_entry.get("capture", {}).get("precision")
                ) if snapshot_entry else None,
            }
            for key, value in metrics.items() if value is not None
        }
        if index_is_estimated and "intelligenceIndex" in metric_sources:
            metric_sources["intelligenceIndex"]["sourceType"] = "benchmark_owner_estimate"
            metric_sources["intelligenceIndex"]["status"] = "estimated"
        model_claims = [
            claim for claim in all_provider_claims
            if claim.get("cohortModelId") == model_id
        ]
        for claim in model_claims:
            key = claim.get("componentKey") or claim.get("component")
            exact_version = claim.get("benchmarkVersion") == "Artificial Analysis Intelligence Index v5.0"
            exact_variant = claim.get("providerVariant") == selected_variant
            if (
                key in metrics
                and metrics[key] is None
                and claim.get("eligibleForRanking") is True
                and exact_version
                and exact_variant
                and isinstance(claim.get("value"), (int, float))
            ):
                metrics[key] = float(claim["value"])
                metric_sources[key] = {
                    "sourceType": "model_provider_claim",
                    "sourceUrl": claim.get("sourceUrl"),
                    "claimId": claim.get("claimId"),
                }
        supplemental = {
            field: clean_number(current.get(field))
            for field in SUPPLEMENTAL_FIELDS
        }
        supplemental["briefcaseElo"] = clean_number(
            current.get("briefcaseElo", json_value(briefcase, "overall.elo"))
        )
        supplemental["briefcaseRubricPassRate"] = clean_number(briefcase.get("rubricPassRate"))
        supplemental["briefcaseTotalCost"] = clean_number(briefcase.get("totalCost"))
        supplemental["tauBanking"] = clean_number(current.get("tauBanking"))
        supplemental["terminalBenchV21"] = clean_number(
            current.get("terminalBenchV21", current.get("terminalbenchV21"))
        )

        display_name = mapping.get(model_id, {}).get("displayName", entry["displayName"])
        models[model_id] = {
            "id": model_id,
            "displayName": display_name,
            # O33: several efforts of one AA family can be ranked; each carries the family its chart points use.
            "family": mapping.get(model_id, {}).get("family", display_name),
            "aaSlug": current.get("slug", slug),
            "aaName": current.get("name"),
            "aaShortName": current.get("shortName"),
            "aaVariant": (current.get("effort") or {}).get("slug"),
            "aaUrl": source_url,
            "release": current.get("release"),
            "isReasoning": current.get("isReasoning"),
            "metrics": metrics,
            "metricSources": metric_sources,
            "intelligenceIndexStatus": (
                "missing" if metrics["intelligenceIndex"] is None
                else "estimated" if index_is_estimated
                else "measured"
            ),
            "providerClaims": model_claims,
            "supplemental": supplemental,
            "extraction": {
                "captureMode": (
                    snapshot_entry.get("capture", {}).get("captureMode")
                    or entry.get("captureMode")
                ) if snapshot_entry else entry.get("captureMode"),
                "htmlSnapshot": str(html_path.relative_to(ROOT)) if html_path else None,
                "textSnapshot": str(text_path.relative_to(ROOT)) if text_path else None,
                "sourceSnapshot": str(SNAPSHOT_PATH.relative_to(ROOT)) if snapshot_entry else None,
                "sourceObservedAt": source_observed_at,
                "precision": snapshot_entry.get("capture", {}).get("precision") if snapshot_entry else None,
                "note": snapshot_entry.get("capture", {}).get("note") if snapshot_entry else None,
                "responseSha256": snapshot_entry.get("capture", {}).get("responseSha256") if snapshot_entry else None,
                "method": (
                    snapshot_entry.get("capture", {}).get("method")
                    or snapshot_entry.get("capture", {}).get("captureMethod")
                    or "captured currentModel object from first-party page payload; raw HTML not retained"
                    if snapshot_entry
                    else "decoded currentModel object from first-party page payload"
                ),
            },
        }

    primary_fields = [item["key"] for item in PRIMARY_EVALUATIONS] + [
        "intelligenceIndex",
        "aaEvalCost",
        "speed",
    ]
    additional_fields = [item["key"] for item in ADDITIONAL_FIELDS]
    supplemental_fields = list(SUPPLEMENTAL_FIELDS) + [
        "briefcaseRubricPassRate",
        "briefcaseTotalCost",
    ]
    coverage = {}
    for group, fields in (
        ("primary", primary_fields),
        ("additional", additional_fields),
        ("supplemental", supplemental_fields),
    ):
        for field in fields:
            container = "supplemental" if group == "supplemental" else "metrics"
            available = [
                model_id
                for model_id, item in models.items()
                if item[container].get(field) is not None
            ]
            missing = [model_id for model_id in models if model_id not in available]
            coverage[field] = {
                "group": group,
                "availableN": len(available),
                "cohortN": len(models),
                "coveragePct": round(100 * len(available) / len(models), 2),
                "missingModels": missing,
                "includedInPrimaryScore": group == "primary" and not missing,
                "providerClaimN": sum(
                    1 for model_id in available
                    if models[model_id].get("metricSources", {}).get(field, {}).get("sourceType") == "model_provider_claim"
                ),
            }

    output = {
        "schemaVersion": "v1.6",
        "source": "https://artificialanalysis.ai/methodology/intelligence-benchmarking",
        "observedAt": observed_at,
        "benchmarkVersion": "Artificial Analysis Intelligence Index v5.0",
        "sourceSnapshot": str(SNAPSHOT_PATH.relative_to(ROOT)) if snapshot else None,
        "primaryEvaluations": PRIMARY_EVALUATIONS,
        "additionalFields": ADDITIONAL_FIELDS,
        "providerClaimPolicy": claim_document.get("policy"),
        "models": models,
    }
    coverage_output = {
        "schemaVersion": "v1.6",
        "observedAt": observed_at,
        "cohort": f"Artificial Analysis current {len(models)}-model ValueRank comparison roster",
        "cohortN": len(models),
        "primaryEvaluations": PRIMARY_EVALUATIONS,
        "additionalFields": ADDITIONAL_FIELDS,
        "providerClaimPolicy": claim_document.get("policy"),
        "fields": coverage,
        "sourceSnapshot": str(SNAPSHOT_PATH.relative_to(ROOT)) if snapshot else None,
        "note": "Missing values are preserved as null. Provider claims are separately source-typed and only eligible when benchmark version and evaluated model variant match; no legacy-version value is substituted into v5.0 components.",
    }
    OUTPUT_PATH.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    COVERAGE_PATH.write_text(json.dumps(coverage_output, indent=2, ensure_ascii=False) + "\n")

    missing_primary = {field: data["missingModels"] for field, data in coverage.items() if data["group"] == "primary" and data["missingModels"]}
    print(json.dumps({
        "models": len(models),
        "primaryFields": len(primary_fields),
        "additionalFields": len(additional_fields),
        "missingPrimary": missing_primary,
        "outputs": [str(OUTPUT_PATH.relative_to(ROOT)), str(COVERAGE_PATH.relative_to(ROOT))],
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
