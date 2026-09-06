#!/usr/bin/env python3
"""Extract the current Artificial Analysis model payloads for the v1.5 cohort.

The public model pages contain the current model record in an escaped JSON
payload.  The older v1.3 extractor searched visible labels and consequently
mistook benchmark versions (for example, ``v2.1``) for scores.  This script
decodes the page's ``currentModel`` object and keeps the v4.2 source
components separate from ValueRank's own score dimensions.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[2]
REFRESH = ROOT / ".refresh" / "v1.4"
AA_DIR = REFRESH / "aa"
MAPPING_PATH = REFRESH / "aa_mapping.json"
EXTRACT_PATH = AA_DIR / "aa_extract.json"
SNAPSHOT_PATH = AA_DIR / "aa_v42_snapshot.json"
OUTPUT_PATH = REFRESH / "aa_metrics.json"
COVERAGE_PATH = REFRESH / "coverage_matrix.json"

PRIMARY_EVALUATIONS = [
    {"key": "briefcaseElo", "label": "AA-Briefcase", "aaKey": "briefcaseBreakdown.overall.elo", "weightPct": 15},
    {"key": "gdpvalV2", "label": "GDPval-AA v2", "aaKey": "gdpvalNormalized", "weightPct": 10},
    {"key": "tau3Banking", "label": "τ³-Banking", "aaKey": "tauBanking", "weightPct": 5},
    {"key": "terminalBenchV21", "label": "Terminal-Bench v2.1", "aaKey": "terminalbenchV21", "weightPct": 10},
    {"key": "scicode", "label": "SciCode", "aaKey": "scicode", "weightPct": 10},
    {"key": "hle", "label": "Humanity's Last Exam", "aaKey": "hle", "weightPct": 10},
    {"key": "gdpPdfAllPass", "label": "GDP.pdf", "aaKey": "gdpPdfAllPass", "weightPct": 10},
    {"key": "critpt", "label": "CritPt", "aaKey": "critpt", "weightPct": 10},
    {"key": "omniAccuracy", "label": "AA-Omniscience Accuracy", "aaKey": "omniscienceBreakdown.accuracy", "weightPct": 10},
    {
        "key": "omniNonHallucination",
        "label": "AA-Omniscience Non-Hallucination Rate",
        "aaKey": "omniscienceBreakdown.hallucinationRate",
        "weightPct": 5,
        "transform": "oneMinus",
    },
    {"key": "aaLcr", "label": "AA-LCR v1.1", "aaKey": "lcr", "weightPct": 5},
]

ADDITIONAL_FIELDS = [
    {"key": "gpqaDiamond", "label": "GPQA Diamond (legacy)", "aaKey": "gpqa"},
]

# These fields are exposed by the page when available, but are not part of the
# current v4.2 weighted index.  They are retained for auditability/coverage.
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
]

NUMBER_RE = r"-?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"


def json_value(obj: dict, path: str):
    value = obj
    for part in path.split("."):
        if not isinstance(value, dict):
            return None
        value = value.get(part)
    return value


def decode_current_model(html: str) -> dict:
    """Return the page's escaped ``currentModel`` object."""

    quote = chr(92) + '"'
    marker = quote + "currentModel" + quote + ":{"
    marker_pos = html.find(marker)
    if marker_pos < 0:
        raise ValueError("currentModel marker not found")
    start = html.find("{", marker_pos + len(marker) - 1)
    if start < 0:
        raise ValueError("currentModel opening brace not found")

    # The object is JSON escaped, but braces remain literal.  Model strings do
    # not contain structural braces; depth counting is sufficient and avoids
    # loading the multi-megabyte HTML into a second parser structure.
    depth = 0
    end = None
    for index in range(start, len(html)):
        if html[index] == "{":
            depth += 1
        elif html[index] == "}":
            depth -= 1
            if depth == 0:
                end = index + 1
                break
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
    slug = urlparse(url).path.rstrip("/").split("/")[-1]
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
    snapshot = {
        item["id"]: item
        for item in json.loads(SNAPSHOT_PATH.read_text())
    } if SNAPSHOT_PATH.exists() else {}
    observed_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
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
            current = decode_current_model(html)
            source_url = entry["url"]
        breakdown = current.get("omniscienceBreakdown") or {}
        cost = current.get("intelligenceIndexCost") or {}
        briefcase = current.get("briefcaseBreakdown") or {}
        metrics = {
            "briefcaseElo": clean_number(
                current.get("briefcaseElo", json_value(briefcase, "overall.elo"))
            ),
            "intelligenceIndex": clean_number(current.get("intelligenceIndex")),
            "gdpvalV2": clean_number(current.get("gdpvalNormalized")),
            "tau3Banking": clean_number(current.get("tauBanking")),
            "terminalBenchV21": clean_number(
                current.get("terminalBenchV21", current.get("terminalbenchV21"))
            ),
            "scicode": clean_number(current.get("scicode")),
            "gdpPdfAllPass": clean_number(current.get("gdpPdfAllPass")),
            "aaLcr": clean_number(current.get("lcr")),
            "hle": clean_number(current.get("hle")),
            "gpqaDiamond": clean_number(current.get("gpqa")),
            "critpt": clean_number(current.get("critpt")),
            "omniAccuracy": clean_number(
                current.get("omniscienceAccuracy", breakdown.get("accuracy"))
            ),
            "omniNonHallucination": clean_number(
                current.get("omniscienceNonHallucination")
            ) if current.get("omniscienceNonHallucination") is not None else (
                1.0 - float(breakdown["hallucinationRate"])
                if breakdown.get("hallucinationRate") is not None
                else None
            ),
            "aaEvalCost": clean_number(current.get("aaEvalCost", cost.get("total"))),
            "speed": clean_number(current.get("speed")) if snapshot_entry else summary_speed(text),
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

        models[model_id] = {
            "id": model_id,
            "displayName": mapping.get(model_id, {}).get("displayName", entry["displayName"]),
            "aaSlug": current.get("slug", slug),
            "aaName": current.get("name"),
            "aaShortName": current.get("shortName"),
            "aaVariant": current.get("effort", {}).get("slug"),
            "aaUrl": source_url,
            "release": current.get("release"),
            "isReasoning": current.get("isReasoning"),
            "metrics": metrics,
            "supplemental": supplemental,
            "extraction": {
                "htmlSnapshot": str(html_path.relative_to(ROOT)) if html_path else None,
                "textSnapshot": str(text_path.relative_to(ROOT)) if text_path else None,
                "sourceSnapshot": str(SNAPSHOT_PATH.relative_to(ROOT)) if snapshot_entry else None,
                "method": (
                    "captured currentModel object from first-party page payload"
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
            }

    output = {
        "schemaVersion": "v1.5",
        "source": "https://artificialanalysis.ai/methodology/intelligence-benchmarking",
        "observedAt": observed_at,
        "benchmarkVersion": "Artificial Analysis Intelligence Index v4.2",
        "sourceSnapshot": str(SNAPSHOT_PATH.relative_to(ROOT)) if snapshot else None,
        "primaryEvaluations": PRIMARY_EVALUATIONS,
        "additionalFields": ADDITIONAL_FIELDS,
        "models": models,
    }
    coverage_output = {
        "schemaVersion": "v1.5",
        "observedAt": observed_at,
        "cohort": "DeepSWE Best v1.1 current 21-model roster",
        "cohortN": len(models),
        "primaryEvaluations": PRIMARY_EVALUATIONS,
        "additionalFields": ADDITIONAL_FIELDS,
        "fields": coverage,
        "sourceSnapshot": str(SNAPSHOT_PATH.relative_to(ROOT)) if snapshot else None,
        "note": "Missing values are preserved as null; legacy or supplemental fields are not silently substituted into the v4.2 source components.",
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
