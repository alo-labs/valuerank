#!/usr/bin/env python3
"""Capture compact first-party model payloads for AA Intelligence Index v4.3.2."""

from __future__ import annotations

import concurrent.futures
import hashlib
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from build_aa_metrics import decode_current_model

ROOT = Path(__file__).resolve().parents[2]
AA_DIR = ROOT / ".refresh" / "v1.4" / "aa"
EXTRACT_PATH = AA_DIR / "aa_extract.json"
OUTPUT_PATH = AA_DIR / "aa_v432_snapshot.json"
MAX_WORKERS = 4
PUBLIC_CAPTURE_MAX_AGE_DAYS = 7


def preserved_public_capture(entry: dict, preserved_pages: dict) -> dict:
    """Retain a recent public-browser reading without changing its provenance."""

    model_id = entry["id"]
    existing = preserved_pages.get(model_id)
    recapture_message = (
        f"{model_id} requires a public rendered capture in the built-in browser. "
        "Update its record in aa/aa_v432_snapshot.json with observedAt, method "
        "and metric precision; the automatic payload capture cannot replace it."
    )
    if not isinstance(existing, dict) or existing.get("url") != entry["url"]:
        raise ValueError(recapture_message)
    metadata = existing.get("capture") or {}
    if not isinstance(metadata, dict):
        raise ValueError(recapture_message)
    observed_at = metadata.get("observedAt") or metadata.get("capturedAt")
    if not observed_at or not metadata.get("precision") or not metadata.get("method"):
        raise ValueError(recapture_message)
    try:
        captured_at = datetime.fromisoformat(observed_at.replace("Z", "+00:00"))
        if captured_at.tzinfo is None:
            raise ValueError("capture date requires a timezone")
        age_seconds = (datetime.now(timezone.utc) - captured_at).total_seconds()
    except (TypeError, ValueError, AttributeError) as exc:
        raise ValueError(recapture_message) from exc
    if age_seconds < 0 or age_seconds > PUBLIC_CAPTURE_MAX_AGE_DAYS * 86400:
        raise ValueError(
            f"Public capture is older than {PUBLIC_CAPTURE_MAX_AGE_DAYS} days or future-dated. "
            + recapture_message
        )
    model = existing.get("model")
    if not isinstance(model, dict) or not model.get("slug"):
        raise ValueError(recapture_message)
    return existing


def capture(entry: dict, preserved_pages: dict) -> dict:
    if entry.get("captureMode") == "public-rendered":
        return preserved_public_capture(entry, preserved_pages)
    url = entry["url"]
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "ValueRank/1.6 official-source-refresh"},
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        payload = response.read()
        html = payload.decode("utf-8", errors="replace")
        model = decode_current_model(html)
        return {
            "id": entry["id"],
            "requestedName": entry.get("displayName"),
            "url": url,
            "model": model,
            "capture": {
                "status": response.status,
                "contentType": response.headers.get("Content-Type", ""),
                "responseBytes": len(payload),
                "responseSha256": hashlib.sha256(payload).hexdigest(),
            },
        }


def main() -> int:
    entries = json.loads(EXTRACT_PATH.read_text())
    if not entries or len({item["id"] for item in entries}) != len(entries):
        raise ValueError("AA capture requires a non-empty cohort of unique selected URLs")
    stored_document = json.loads(OUTPUT_PATH.read_text()) if OUTPUT_PATH.exists() else {}
    stored_pages = stored_document.get("pages", []) if isinstance(stored_document, dict) else []
    preserved_pages = {page["id"]: page for page in stored_pages}
    # Validate browser-only records before starting automatic network captures.
    for entry in entries:
        if entry.get("captureMode") == "public-rendered":
            preserved_public_capture(entry, preserved_pages)
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        pages = list(pool.map(lambda entry: capture(entry, preserved_pages), entries))
    document = {
        "schemaVersion": "valuerank-aa-page-snapshot/v2",
        "benchmarkVersion": "Artificial Analysis Intelligence Index v4.3.2",
        "capturedAt": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "source": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index",
        "concurrency": MAX_WORKERS,
        "pages": pages,
    }
    OUTPUT_PATH.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "models": len(pages),
        "uniqueIds": len({item['id'] for item in pages}),
        "benchmarkVersion": document["benchmarkVersion"],
        "capturedAt": document["capturedAt"],
        "output": str(OUTPUT_PATH.relative_to(ROOT)),
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
