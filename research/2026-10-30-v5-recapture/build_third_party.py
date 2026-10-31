"""Rebuild the third-party leaf data for the v5 cohort from the 2026-10-30 board re-read (O132, O139, O140).

    PYTHONPATH=. python3 research/2026-10-30-v5-recapture/build_third_party.py

Writes data/bug_hunt_scoreboard.json (every row of the owner's combined scoreboard at the re-read commit) and
data/bug_hunt.json (one record per cohort configuration: an exact owner run, else unmatched with the reason). A
configuration whose record carries over keeps it when the board's value is unchanged; a new exact cell becomes a record
read from the board. MiMo-V2.6-Flash's OpenRouter-default run stays unmatched (O140).
"""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
PARTY = HERE / "third-party"
COVERAGE = json.loads((PARTY / "coverage-2026-10-30.json").read_text())
COHORT = [row["id"] for row in json.loads((HERE / "cohort.json").read_text())["configurations"]]


def board(key: str) -> dict:
    return next(item for item in COVERAGE["benchmarks"] if item["key"] == key)


def scoreboard() -> None:
    bug = board("bug-hunt")
    commit = bug["sourceCommit"]
    path = PARTY / "bughunt" / f"combined-{commit}.csv"
    content = path.read_bytes()
    rows = [{"model": row["model"], "harness": row["harness"], "fixedOf105": float(row["fixed_of_105"])}
            for row in csv.DictReader(content.decode("utf-8").splitlines())]
    previous = json.loads((ROOT / "data" / "bug_hunt_scoreboard.json").read_text())
    document = {**previous, "sourceCommit": commit,
                "sourceUrl": f"https://github.com/phuryn/bug-hunt-bench/blob/{commit}/results/combined-scoreboard.csv",
                "capturedAt": bug["readAt"], "sourceUpdated": bug["updated"], "sha256": hashlib.sha256(content).hexdigest(), "rows": rows}
    (ROOT / "data" / "bug_hunt_scoreboard.json").write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")


def bug_hunt() -> None:
    bug = board("bug-hunt")
    commit = bug["sourceCommit"]
    path = ROOT / "data" / "bug_hunt.json"
    document = json.loads(path.read_text())
    previous = {model["modelId"]: model for model in document["models"]}
    models = []
    for model_id in COHORT:
        cell = bug["coverage"][model_id]
        old = previous.get(model_id) or {}
        if cell["status"] == "exact":
            if old.get("matched") and old.get("fixedOf105") == cell["value"] and old.get("evaluatedModel") == cell["sourceLabel"]:
                models.append(old)
                continue
            runs = cell.get("nRuns") or 1
            models.append({
                "modelId": model_id, "matched": True, "matchStatus": "matched", "evaluatedModel": cell["sourceLabel"],
                "fixedOf105": cell["value"], "sampleN": runs, "aggregation": "mean" if runs > 1 else "single run",
                "effort": cell["effort"], "effortStatus": "the board's effort label", "harness": cell["harness"],
                "harnessVersion": cell.get("harnessVersion"), "route": "the harness's own provider route",
                "sourceType": "benchmark_owner", "observedAt": bug["readAt"][:10], "reportedOn": cell["date"], "sourceCommit": commit,
                "sourceUrl": f"https://github.com/phuryn/bug-hunt-bench/blob/{commit}/results/run-notes.md",
                "note": cell.get("note") or f"Owner-published {'mean of ' + str(runs) if runs > 1 else 'single run'}, read 2026-10-30 (O132).",
            })
        else:
            reason = cell.get("note") or "No owner-published run of this exact configuration."
            models.append({"modelId": model_id, "matched": False,
                           "matchStatus": "effort_not_established" if cell["status"] == "plausible" else "no_exact_owner_result",
                           **({"evaluatedModel": cell["sourceLabel"], "fixedOf105": cell["value"]} if cell.get("value") is not None else {}),
                           "note": reason})
    document.update({"snapshotDate": bug["updated"], "sourceCommit": commit, "models": models})
    path.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"bugHuntMatched": sum(1 for model in models if model["matched"]), "cohort": len(models)}))


if __name__ == "__main__":
    scoreboard()
    bug_hunt()
