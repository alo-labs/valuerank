"""Re-register AA's Coding Agent Index rows for the v5 cohort (O64 closed world; O132).

Each captured row is the exact record of a cohort configuration when the E267 grammar reads it as that configuration's
model and effort, and otherwise "other" with a reason (kept from the previous review where the row carries over).
"""

import json
from pathlib import Path

from valuerank import value_v3 as v

ROOT = Path(__file__).resolve().parents[2]
capture = json.loads((ROOT / "data/aa/coding_agents_capture.json").read_text())
previous = json.loads((ROOT / "data/aa/coding_agents_manifest.json").read_text())
mapping = json.loads((ROOT / "data/aa_mapping.json").read_text())
labels = [row["label"] for row in capture["configurations"]]
exact = {}
for item in mapping:
    configuration = {"id": item["id"], "name": item["displayName"], "family": item["family"], "effort": item["aaVariant"]}
    for label in v.exact_agent_records(configuration, labels):
        if label in exact:
            raise ValueError(f"{label} reads as two configurations")
        exact[label] = item["id"]
cohort_models = {item["family"] for item in mapping}
rows = {}
for row in capture["configurations"]:
    if row["label"] in exact:
        rows[row["id"]] = {"label": row["label"], "classification": "exact", "configurationId": exact[row["label"]]}
        continue
    parsed = v.parse_agent_label(row["label"])
    model = (parsed or {}).get("model") or ""
    reason = (previous["rows"].get(row["id"]) or {}).get("reason")
    if not reason or (previous["rows"].get(row["id"]) or {}).get("classification") == "exact":
        reason = ("several models in one row (E267)" if parsed is None
                  else "another effort or variant of a cohort model, not a cohort configuration" if any(model in (family, family.removeprefix("Claude ")) or model.startswith(family) for family in cohort_models)
                  else "model outside the cohort (O51)")
    rows[row["id"]] = {"label": row["label"], "classification": "other", "reason": reason}
document = {**previous, "reviewedOn": capture["capturedAt"][:10], "rows": dict(sorted(rows.items(), key=lambda item: item[1]["label"]))}
(ROOT / "data/aa/coding_agents_manifest.json").write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({label: config for label, config in sorted(exact.items())}, indent=1))
