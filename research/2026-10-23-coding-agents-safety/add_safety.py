"""O63: add AA's Coding Agent Index safety-refusal counts to the pinned capture.

The pinned capture (data/aa/coding_agents_capture.json) predates the safety fields in ValueRank's capture. The page
read on 2026-10-23 at 22:15Z carries them; this script copies them in only after checking that every row id, label,
cost, score and attempt count of that page equals the pinned capture's, so the counts describe the same results.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from valuerank import capture_coding_agents as capture
from valuerank.paths import DATA, ROOT

HERE = Path(__file__).resolve().parent
PAGE = HERE / "coding-agents-page-2026-10-23T2215Z.html"
COMPARED = ("label", "totalCostUsd", "meanCostPerTaskUsd", "pricedTaskCount", "indexScore")


def main() -> None:
    target = DATA / "aa" / "coding_agents_capture.json"
    document = json.loads(target.read_text())
    payload = PAGE.read_bytes()
    page = {record["id"]: record for record in (capture.configuration_record(row) for row in
            capture.configuration_rows(capture.flight_values(capture.flight_text(payload.decode("utf-8")))))}
    for record in document["configurations"]:
        other = page[record["id"]]
        if any(record[key] != other[key] for key in COMPARED) or [c["attempts"] for c in record["components"]] != [c["attempts"] for c in other["components"]]:
            raise ValueError(f"{record['label']}: the safety page's results differ from the pinned capture")
        record["isRouter"] = other["isRouter"]
        for component, source in zip(record["components"], other["components"]):
            component["safety"] = source["safety"]
    if set(page) != {record["id"] for record in document["configurations"]}:
        raise ValueError("the safety page lists different rows from the pinned capture")
    document["safetyCapture"] = {
        "artifact": str(PAGE.relative_to(ROOT)), "readAt": "2026-10-23T22:15:00Z", "responseSha256": hashlib.sha256(payload).hexdigest(),
        "rule": "Owner decision O63 (2026-10-23): AA's safety-refusal outcomes (blocked attempts, attempts finished by a fallback model) "
                "are disclosed and flagged, never a cost or quality change. Copied from this read of the page only because every row id, "
                "label, cost, score and attempt count equals the pinned capture's.",
    }
    target.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"rows": len(document["configurations"]), "withRefusals": sum(
        1 for record in document["configurations"] if any((c["safety"]["blocked"] or 0) + (c["safety"]["fallback"] or 0) for c in record["components"]))}))


if __name__ == "__main__":
    main()
