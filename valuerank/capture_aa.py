#!/usr/bin/env python3
"""Capture compact first-party model payloads for AA Intelligence Index v5.0 (owner decision O132)."""

from __future__ import annotations

import concurrent.futures
import hashlib
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from valuerank.clock import iso_z, utcnow

from valuerank.build_aa_metrics import decode_page_model, page_slug, printed_notes

from valuerank.paths import DATA, ROOT
AA_DIR = DATA / "aa"
EXTRACT_PATH = AA_DIR / "aa_extract.json"
OUTPUT_PATH = AA_DIR / "aa_v432_snapshot.json"
PREVIOUS_PATH = AA_DIR / "aa_previous_capture.json"
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
        age_seconds = (utcnow() - captured_at).total_seconds()
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
        # O103: the notes AA prints on the page, verbatim, beside its model object.
        model = {**decode_page_model(html, page_slug(url)), "notes": printed_notes(html)}
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


def previous_capture_digest(document: dict, content: bytes) -> dict:
    """I60 M1: the fields of the capture being replaced that the next release compares against (GDPval-AA's displayed
    Elo, its Index evaluation score and the Index total), with the replaced file's hash, so the movement is generated."""

    pages = []
    for page in document.get("pages", []):
        model = page.get("model") or {}
        evaluations = {item.get("slug"): item.get("score") for item in model.get("intelligenceIndexEvaluations") or []}
        pages.append({"id": page["id"], "gdpval": model.get("gdpval"), "gdpvalEvaluation": evaluations.get("gdpval-aa"),
                      "intelligenceIndex": model.get("intelligenceIndex")})
    return {"schemaVersion": "valuerank-aa-previous-capture/v1", "capturedAt": document.get("capturedAt"),
            "sha256": hashlib.sha256(content).hexdigest(), "pages": pages}


def main() -> int:
    entries = json.loads(EXTRACT_PATH.read_text())
    if not entries or len({item["id"] for item in entries}) != len(entries):
        raise ValueError("AA capture requires a non-empty cohort of unique selected URLs")
    stored_content = OUTPUT_PATH.read_bytes() if OUTPUT_PATH.exists() else b""
    stored_document = json.loads(stored_content) if stored_content else {}
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
        "benchmarkVersion": "Artificial Analysis Intelligence Index v5.0",
        "capturedAt": iso_z(),
        "source": "https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index",
        "concurrency": MAX_WORKERS,
        "pages": pages,
    }
    if isinstance(stored_document, dict) and stored_document.get("pages"):
        PREVIOUS_PATH.write_text(json.dumps(previous_capture_digest(stored_document, stored_content), indent=1) + "\n")
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
