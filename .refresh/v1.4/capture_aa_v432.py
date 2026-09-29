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


def capture(entry: dict) -> dict:
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
    if len(entries) != 21 or len({item["id"] for item in entries}) != 21:
        raise ValueError("AA capture requires exactly 21 unique selected cohort URLs")
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        pages = list(pool.map(capture, entries))
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
