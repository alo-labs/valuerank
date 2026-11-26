"""Extend data/livebench.json (the legacy LiveBench snapshot, release 2026-06-25, pinned since 2026-10-17) with the ten
configurations retained under owner decision O145. Its source repository commit no longer serves the release files (404 on
2026-11-01), so the snapshot is extended, not re-fetched: every retained configuration postdates the release, so each gets the
unmatched row valuerank.fetch_livebench writes for a configuration with no verified exact mapping (COHORT_MAP None).

    PYTHONPATH=. python3 research/2026-11-01-recapture/extend_livebench.py
"""

import json
from pathlib import Path

from valuerank.fetch_livebench import COHORT_MAP

ROOT = Path(__file__).resolve().parents[2]
path = ROOT / "data" / "livebench.json"
document = json.loads(path.read_text())
names = {item["id"]: item["displayName"] for item in json.loads((ROOT / "data" / "aa_mapping.json").read_text())}
for model_id, mapped in COHORT_MAP.items():
    if model_id in document["models"]:
        continue
    if mapped is not None:
        raise ValueError(f"{model_id}: a mapped configuration needs the release files, not an extension")
    document["models"][model_id] = {"modelId": model_id, "name": names[model_id], "livebenchModel": None, "matched": False,
                                    "matchStatus": "no_verified_exact_mapping",
                                    "coverageNote": "No exact mapped task-and-cost result in the pinned LiveBench snapshot; no score is imputed.",
                                    "tasks": {}, "categoryScores": {}, "overallScore": None, "instructionFollowingScore": None,
                                    "costPerSuccessfulTaskUsd": None}
document["models"] = {model_id: document["models"][model_id] for model_id in COHORT_MAP}
document["cohortN"] = len(document["models"])
document["matchedN"] = sum(1 for item in document["models"].values() if item["matched"])
document["missingModels"] = [item["name"] for item in document["models"].values() if not item["matched"]]
path.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"cohortN": document["cohortN"], "matchedN": document["matchedN"]}))
