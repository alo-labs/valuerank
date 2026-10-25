"""Owner decisions O66-O68 (2026-10-25): rebuild the added-leaf coverage from the boards re-read on 2026-10-25.

Every board an added leaf uses was re-read in full after the 2026-10-25 cutoff move (O65): Vals Vibe Code Bench v1.1
and Code Migration v1.1, AI Coding Daily (every row, the hidden older ones included), Bug Hunt Bench's owner scoreboard
and LiveBench 2.0's 2026-10-23 release (O67). Each source's own last update predates the cutoff's day, so the reads
stand under O60. The 2026-10-23 coverage files are the template: every cell keeps its reviewed match (model key and
effort) and takes its value from the new read, and the build stops when a matched row has vanished or changed effort.
Kimi K3.1 Pro joins the cohort (a rendered-frontier vertex, O51) and is matched at max, its maximum effort (O66).

    python3 research/2026-10-25-board-reread/rebuild_coverage.py
"""

from __future__ import annotations

import copy
import csv
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
OLD = HERE.parent / "2026-10-23-swe-benchmarks"
READ_AT = "2026-10-25T10:44:11Z"
KIMI = "kimi-k3-1-pro"
O66 = ("Owner decision O66 (2026-10-25): AA plots Kimi K3.1 Pro without an effort; Moonshot's API documents reasoning_effort "
       "low / high / max with max the default, so its configuration is taken at max, its maximum effort.")
CATEGORY_COLUMNS = {"Long Agentic": "long_agentic", "Reasoning": "reasoning", "Coding": "coding", "Browser": "browser",
                    "Data Analysis": "data_analysis", "Research": "research", "Design": "design"}
LIVEBENCH_KEYS = {"livebench2-coding": "coding", "livebench2-agentic": "long_agentic", "livebench2-reasoning": "reasoning",
                  "livebench2-browser": "browser", "livebench2-data-analysis": "data_analysis", "livebench2-research": "research",
                  "livebench2-design": "design"}
AICD_COLUMNS = {"aicd-total": ("total",), "aicd-non-bug": ("laravel", "react", "edge"), "aicd-laravel-quality": ("laravel",),
                "aicd-react-quality": ("react",), "aicd-bug-finding": ("bug",), "aicd-edge-case": ("edge",)}


def cohort() -> dict:
    document = json.loads((OLD / "cohort-2026-10-23.json").read_text())
    document["capturedFrom"] = "data/aa_frontier_capture.json captured 2026-10-25T09:53:28Z (O65)"
    document["configurations"].append({"id": KIMI, "name": "Kimi K3.1 Pro", "aaEffort": None, "aaSlug": KIMI,
                                       "aaFrontierConfiguration": "Kimi K3.1 Pro", "tier": "frontier", "ranked": True,
                                       "ownerStatedEffort": "max (O66)"})
    return document


def vals() -> dict:
    document = json.loads((OLD / "vals-catalogue-2026-10-23.json").read_text())
    document["capturedAt"] = READ_AT
    for board in document["benchmarks"]:
        if board["slug"] not in ("vibe-code", "code-migration-v1-1"):
            board["coverage"][KIMI] = {"status": "not captured", "value": None, "stderr": None, "valsKey": None, "effort": None,
                                       "note": "Board not re-read on 2026-10-25: it feeds no ValueRank leaf."}
            continue
        source = json.loads((HERE / "vals" / f"{board['slug']}.json").read_text())
        rows = source["tasks"]["overall"]
        for model_id, cell in board["coverage"].items():
            if cell["status"] in ("exact", "plausible"):
                row = rows.get(cell["valsKey"])
                if row is None or row.get("accuracy") != cell["value"] or row.get("stderr") != cell["stderr"]:
                    raise ValueError(f"{board['slug']}: {model_id}'s matched row {cell['valsKey']} changed or vanished; review the match")
        row = rows.get("kimi/kimi-k3.1-pro")
        if row and row.get("reasoning_effort") == "max":
            board["coverage"][KIMI] = {"status": "exact", "value": row["accuracy"], "stderr": row.get("stderr"), "valsKey": "kimi/kimi-k3.1-pro",
                                       "effort": "max", "note": O66}
        else:
            board["coverage"][KIMI] = {"status": "absent", "value": None, "stderr": None, "valsKey": None, "effort": None,
                                       "note": "No Kimi K3.1 Pro row (the board has kimi/kimi-k3 only, a different model version; not transferred)."}
        board["updated"] = source["metadata"]["updated"]
        board["models"] = len(rows)
        board["captureFile"] = f"research/2026-10-25-board-reread/vals/{board['slug']}.json"
        board["readAt"] = READ_AT
    return document


def livebench_effort(site: str, label: str) -> str | None:
    match = re.search(r'"' + re.escape(label) + r'":\{[^}]*?effort:"(\w+)"', site)
    return match.group(1) if match else None


def other() -> dict:
    document = json.loads((OLD / "other-coverage-2026-10-23.json").read_text())
    document["capturedAt"] = READ_AT
    table = {row["model"]: row for row in csv.DictReader((HERE / "livebench" / "table-20261023.csv").open())}
    site = (HERE / "livebench" / "site-main.js").read_text()
    aicd = json.loads((HERE / "aicd" / "leaderboard-allrows-parsed.json").read_text())
    for board in document["benchmarks"]:
        key = board["key"]
        if key in LIVEBENCH_KEYS:
            column = LIVEBENCH_KEYS[key]
            board.update(version="LiveBench 2.0 release 20261023", updated="2026-10-24", readAt=READ_AT,
                         sourceUrl="https://livebench.ai/data/20261023/table.csv (shown at https://livebench.ai/new; O67)")
            for model_id, cell in board["coverage"].items():
                if cell["status"] not in ("exact", "plausible"):
                    continue
                row = table.get(cell["sourceLabel"])
                if row is None:
                    board["coverage"][model_id] = {**cell, "status": "absent", "value": None,
                                                   "note": f"{cell['sourceLabel']} is not in the 2026-10-23 release (O67)."}
                    continue
                if livebench_effort(site, cell["sourceLabel"]) != cell["effort"]:
                    raise ValueError(f"{key}: {model_id}'s LiveBench effort changed; review the match")
                board["coverage"][model_id] = {**cell, "value": float(row[column]), "note": "2026-10-23 release (O67); effort from the site bundle's model metadata."}
            effort = livebench_effort(site, "kimi-k3.1-pro")
            board["coverage"][KIMI] = ({"status": "exact", "value": float(table["kimi-k3.1-pro"][column]), "sourceLabel": "kimi-k3.1-pro",
                                        "effort": "max", "note": O66 + " LiveBench's model metadata records effort max."}
                                       if effort == "max" and "kimi-k3.1-pro" in table else
                                       {"status": "absent", "value": None, "sourceLabel": None, "effort": None, "note": "No Kimi K3.1 Pro row at max."})
        elif key in AICD_COLUMNS:
            board.update(updated="2026-10-24", readAt=READ_AT, sourceUrl="https://aicodingdaily.com/leaderboard (every row, hidden older rows included)")
            rows = [row for row in aicd if row["model"] == "Kimi K3.1 Pro (Max)"]
            if len(rows) == 1 and all(rows[0][column] not in (None, "") for column in AICD_COLUMNS[key]):
                row = rows[0]
                board["coverage"][KIMI] = {"status": "exact", "value": round(sum(float(row[column]) for column in AICD_COLUMNS[key]), 2),
                                           "sourceLabel": row["model"], "effort": "max",
                                           "note": f"Tested {row['tested']} with {row['harness']}; cost/prompt {row['cost']}. " + O66
                                                   + " The Kimi K3.1 Pro (High) row is another effort and is not used."}
            else:
                board["coverage"][KIMI] = {"status": "absent", "value": None, "sourceLabel": None, "effort": None, "note": "No Kimi K3.1 Pro (Max) row."}
        else:
            board["coverage"][KIMI] = {"status": "not captured", "value": None, "sourceLabel": None, "effort": None,
                                       "note": "Source not re-read on 2026-10-25: it feeds no ValueRank leaf."}
    return document


def livebench_weights() -> dict:
    categories = json.loads((HERE / "livebench" / "categories-20261023.json").read_text())
    weights = categories.get("_overall_weights") or {}
    return {CATEGORY_COLUMNS[name]: float(weights.get(name, 1.0)) for name in CATEGORY_COLUMNS}


def main() -> None:
    (HERE / "cohort-2026-10-25.json").write_text(json.dumps(cohort(), indent=1, ensure_ascii=False) + "\n")
    (HERE / "vals-catalogue-2026-10-25.json").write_text(json.dumps(vals(), indent=1, ensure_ascii=False) + "\n")
    (HERE / "other-coverage-2026-10-25.json").write_text(json.dumps(other(), indent=1, ensure_ascii=False) + "\n")
    (HERE / "livebench" / "weights-20261023.json").write_text(json.dumps(livebench_weights(), indent=1) + "\n")
    print("rebuilt cohort, Vals and other coverage for 2026-10-25")


if __name__ == "__main__":
    main()
