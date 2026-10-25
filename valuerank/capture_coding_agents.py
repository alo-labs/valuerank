#!/usr/bin/env python3
"""Capture AA's Coding Agent Index cost table: one record per agent + model configuration.

The page is a Next.js app whose data travels in ``self.__next_f.push([1, "..."])``
script chunks.  Concatenated, the chunks form "flight" lines of the shape
``<hex id>:<json>``; the configuration rows are the JSON objects that carry a
``displayLabel`` together with ``sums`` and ``mean`` blocks.

AA publishes, per configuration, the total cost across the index
(``sums.costUsd``) and the mean cost per task (``mean.costUsd``).  Their ratio
is the number of tasks the total prices; the capture keeps both so the basket
builder can test cost completeness against the required task count rather than
assume it.
"""

from __future__ import annotations

import hashlib
import json
import re
import urllib.request

from valuerank.clock import iso_z
from valuerank.paths import DATA, ROOT

SOURCE_URL = "https://artificialanalysis.ai/agents/coding-agents"
OUTPUT_PATH = DATA / "aa" / "coding_agents_capture.json"
PUSH_RE = re.compile(r'self\.__next_f\.push\(\[1,(".*?")\]\)</script>', re.S)
LINE_RE = re.compile(r"(?m)^[0-9a-f]+:(?=[\[{])")


def flight_text(html: str) -> str:
    """The page's flight payload: every pushed string chunk, decoded and joined in order."""

    return "".join(json.loads(chunk) for chunk in PUSH_RE.findall(html))


def flight_values(text: str) -> list:
    """Every JSON value that starts a flight line; lines that are not valid JSON are skipped."""

    decoder = json.JSONDecoder()
    values = []
    for match in LINE_RE.finditer(text):
        try:
            value, _end = decoder.raw_decode(text, match.end())
        except json.JSONDecodeError:
            continue
        values.append(value)
    return values


def configuration_rows(values: list) -> list[dict]:
    """Configuration objects (an ``id`` and ``displayLabel`` with costs or evaluations), first occurrence per id; a row
    without costs is kept (I56 M1) so the reviewed manifest (O64) sees every row AA lists."""

    rows: dict[str, dict] = {}

    def walk(value):
        if isinstance(value, dict):
            if "displayLabel" in value and value.get("id") and ("sums" in value or "mean" in value or "evals" in value):
                rows.setdefault(value["id"], value)
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(values)
    return list(rows.values())


def _number(value):
    return value if isinstance(value, (int, float)) and not isinstance(value, bool) else None


def safety_record(safety: dict) -> dict:
    """O63: blocked attempts (AA's hard stops) and attempts finished by a fallback model, with the fallback models."""

    models = sorted({link.get("releaseName") or link.get("model") for refusal in safety.get("refusals") or []
                     if refusal.get("outcome") == "fallback" for link in refusal.get("chain") or []} - {None})
    return {"refused": safety.get("refusedAttemptCount"), "blocked": safety.get("hardStopAttemptCount"),
            "fallback": safety.get("fallbackAttemptCount"), "fallbackModels": models}


def configuration_record(row: dict) -> dict:
    """The fields ValueRank keeps for one configuration, with the implied priced-task count."""

    total = _number((row.get("sums") or {}).get("costUsd"))
    mean = _number((row.get("mean") or {}).get("costUsd"))
    display = row.get("display") or {}
    components = []
    for evaluation in row.get("evals") or []:
        safety = evaluation.get("safety") or {}
        components.append(
            {
                "name": evaluation.get("datasetIndexName"),
                "dataset": evaluation.get("refDatasetName"),
                "weight": evaluation.get("weight"),
                "attempts": safety.get("attemptCount"),
                "reward": (evaluation.get("mean") or {}).get("reward"),
                # O63: AA's safety-refusal outcomes, disclosed and flagged, never a cost or quality change.
                "safety": safety_record(safety),
            }
        )
    return {
        "id": row["id"],
        "label": row["displayLabel"],
        "agent": display.get("agent") or row.get("agentName"),
        "model": display.get("model"),
        "isDefault": bool(row.get("isDefault")),
        "isUnavailable": bool(row.get("isUnavailable")),
        "isRouter": bool(row.get("isRouter")),
        "indexScore": _number(row.get("indexScore")),
        "totalCostUsd": total,
        "meanCostPerTaskUsd": mean,
        "pricedTaskCount": round(total / mean, 6) if total is not None and mean else None,
        "components": components,
    }


def capture_document(html: str, *, captured_at: str, response_bytes: bytes) -> dict:
    rows = configuration_rows(flight_values(flight_text(html)))
    if not rows:
        raise ValueError("no Coding Agent Index configuration rows found in the page payload")
    records = sorted((configuration_record(row) for row in rows), key=lambda record: record["label"])
    return {
        "schemaVersion": "valuerank-aa-coding-agents/v1",
        "source": SOURCE_URL,
        "capturedAt": captured_at,
        "costFields": {
            "total": "sums.costUsd (AA 'Total Cost Across the Artificial Analysis Coding Agent Index')",
            "perTask": "mean.costUsd (AA average pay-per-token API cost per task)",
        },
        "responseSha256": hashlib.sha256(response_bytes).hexdigest(),
        "configurations": records,
    }


def main() -> int:
    request = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "ValueRank/3 official-source-refresh"})
    with urllib.request.urlopen(request, timeout=60) as response:
        payload = response.read()
    document = capture_document(payload.decode("utf-8", errors="replace"), captured_at=iso_z(), response_bytes=payload)
    OUTPUT_PATH.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "configurations": len(document["configurations"]),
        "priced": sum(1 for record in document["configurations"] if record["totalCostUsd"] is not None),
        "output": str(OUTPUT_PATH.relative_to(ROOT)),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
