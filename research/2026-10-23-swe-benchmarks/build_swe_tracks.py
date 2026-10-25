"""Build data/swe_tracks.json, the leaf evidence of the two rankings' added software-engineering leaves (O53-O55).

Reads the verified coverage captures in this folder and keeps exact-configuration matches only. MiMo-V2.6-Pro is the one
exception, by owner decision O54 and editor decision E252: AA's configuration is high, so AI Coding Daily's and LiveBench's
"high" rows are exact, and Vals' run (reasoning enabled, no level recorded) is the same single reasoning mode.

    python3 research/2026-10-23-swe-benchmarks/build_swe_tracks.py
"""

import csv
import json
from pathlib import Path

HERE = Path(__file__).parent
# O68 (2026-10-25): every added-leaf board re-read in full on 2026-10-25.
READ = HERE.parent / "2026-10-25-board-reread"
ROOT = HERE.parent.parent
OWNER_MATCHED = {"mimo-v2-6-pro"}  # O54, E252

LEAVES = {
    # leaf key: (coverage key, coverage file, source metadata)
    "vibeCode": ("vibe-code", "vals", {
        "benchmark": "Vibe Code Bench v1.1", "publisher": "Vals AI", "updated": "2026-10-24",
        "url": "https://www.vals.ai/benchmarks/vibe-code", "harness": "OpenHands, the same for every model",
        "metric": "test-workflow pass rate (percent), with Vals' published standard error", "unit": "percent",
        "sampling": {"kind": "publishedStandardError"},
    }),
    "codeMigration": ("code-migration-v1-1", "vals", {
        "benchmark": "Code Migration v1.1", "publisher": "Vals AI", "updated": "2026-10-20",
        "url": "https://www.vals.ai/benchmarks/code-migration-v1-1", "harness": "Pi agent harness, the same for every model",
        "metric": "hidden-test pass rate (percent), with Vals' published standard error", "unit": "percent",
        "sampling": {"kind": "publishedStandardError", "tasks": 130},
    }),
    # O61 (2026-10-23): LiveBench 2.0 Overall replaces the Long Agentic and Coding categories. O67 (2026-10-25): the
    # 2026-10-23 release, whose Overall is LiveBench's weighted mean of its seven categories (the release's
    # _overall_weights), to two decimals. The configuration match is the coverage capture's (one LiveBench row per model,
    # at its top effort); the categories come from the release table.
    "livebench2Overall": ("livebench2-coding", "other", {
        "benchmark": "LiveBench 2.0 Overall (release 2026-10-23)", "publisher": "LiveBench", "updated": "2026-10-24",
        "url": "https://livebench.ai/data/20261023/table.csv", "harness": "LiveBench's own, one run per model at its top effort",
        "metric": "LiveBench's weighted Overall of the seven category scores (Long Agentic 2, Coding 1.5, Design 1.5, Reasoning, Browser, Data Analysis and Research 1; O67), 0-100",
        "unit": "percent",
        "sampling": {"kind": "categories", "tasks": {"long_agentic": 18, "reasoning": 4, "coding": 29, "browser": 25, "data_analysis": 3,
                                                     "research": 22, "design": 25}},
    }),
    "aiCodingDaily": ("aicd-non-bug", "other", {
        "benchmark": "AI Coding Daily LLM Coding Leaderboard (Laravel quality + React-TS quality + edge-case testing, max 60)",
        "publisher": "AI Coding Daily (Povilas Korop)", "updated": "2026-10-24", "url": "https://aicodingdaily.com/leaderboard",
        "harness": "varies by model: Claude Code, Codex CLI, OpenCode, Devin, DeepSeek's harness (named on each record)",
        "metric": "judged points out of 60 (the 10-point bug-finding column is excluded: it overlaps Bug Hunt)", "unit": "points of 60",
        "sampling": {"kind": "tasks", "tasks": 6, "unit": "graded projects (Laravel, React-TS and 4 edge-case projects)"},
    }),
}


def aicd_rows() -> dict[str, list[dict]]:
    """Every captured AI Coding Daily row by its model label (the board can list one model and effort more than once)."""

    rows: dict[str, list[dict]] = {}
    for row in json.loads((READ / "aicd" / "leaderboard-allrows-parsed.json").read_text()):
        rows.setdefault(row["model"], []).append(row)
    return rows


def bug_hunt_harness(model_id: str) -> str | None:
    for model in json.loads((ROOT / "data" / "bug_hunt.json").read_text())["models"]:
        if model["modelId"] == model_id and model.get("matched"):
            return model.get("harness")
    return None


def select_aicd(model_id: str, label: str, board: dict[str, list[dict]]) -> dict:
    """I50 M2: when the board lists a model and effort more than once, the record is the row on the harness the
    configuration's Bug Hunt record uses, else the latest test date; a tie the rule cannot break stops the build. The
    other rows are published beside the leaf."""

    rows = board[label]
    if len(rows) == 1:
        return {"row": rows[0], "alternates": []}
    harness = (bug_hunt_harness(model_id) or "").split(" / ")[0].casefold()
    picked = [row for row in rows if harness and row["harness"].casefold() == harness]
    rule = "the harness of its Bug Hunt record"
    if len(picked) != 1:
        # I51 L5: among the rows on the matched harness if several share it, else among all rows.
        pool = picked or rows
        latest = max(row["tested"] for row in pool)
        picked, rule = [row for row in pool if row["tested"] == latest], "the latest test date"
    if len(picked) != 1:
        raise ValueError(f"{model_id}: AI Coding Daily lists {label!r} {len(rows)} times and the rule cannot pick one (I50 M2)")
    return {"row": picked[0], "rule": rule, "alternates": [row for row in rows if row is not picked[0]]}


def aicd_points(row: dict) -> float:
    return round(float(row["laravel"]) + float(row["react"]) + float(row["edge"]), 2)


def main() -> None:
    vals_document = json.loads((READ / "vals-catalogue-2026-10-25.json").read_text())
    other_document = json.loads((READ / "other-coverage-2026-10-25.json").read_text())
    vals = {item["slug"]: item for item in vals_document["benchmarks"]}
    other = {item["key"]: item for item in other_document["benchmarks"]}
    # O59/O60: each source carries the instant its coverage was captured.
    captured = {"vals": vals_document["capturedAt"], "other": other_document["capturedAt"]}
    cohort = [row["id"] for row in json.loads((READ / "cohort-2026-10-25.json").read_text())["configurations"]]
    table = {row["model"]: row for row in csv.DictReader((READ / "livebench" / "table-20261023.csv").open())}
    weights = json.loads((READ / "livebench" / "weights-20261023.json").read_text())
    board = aicd_rows()
    records, sources = [], {}
    for leaf, (key, origin, meta) in LEAVES.items():
        sources[leaf] = {**meta, "capturedAt": captured[origin]}
        coverage = (vals if origin == "vals" else other)[key]["coverage"]
        for model_id in cohort:
            cell = coverage[model_id]
            if cell["status"] == "exact" or (cell["status"] == "plausible" and model_id in OWNER_MATCHED):
                record = {
                    "modelId": model_id, "leaf": leaf, "value": cell["value"],
                    "sourceLabel": cell.get("valsKey") or cell.get("sourceLabel"), "effort": cell.get("effort"),
                    "locator": f"research/2026-10-25-board-reread/{'vals-catalogue' if origin == 'vals' else 'other-coverage'}-2026-10-25.json"
                               f" benchmarks[{'slug' if origin == 'vals' else 'key'}={key}].coverage[{model_id}]",
                }
                if leaf == "livebench2Overall":
                    categories = {name: float(value) for name, value in table[cell["sourceLabel"]].items() if name != "model"}
                    record["value"] = round(sum(weights[name] * value for name, value in categories.items()) / sum(weights[name] for name in categories), 2)
                    record["categories"] = categories
                    record["weights"] = weights
                if cell.get("stderr") is not None:
                    record["stderr"] = cell["stderr"]
                if cell["status"] == "plausible":
                    record["match"] = "owner (O54): AA's configuration is high; " + (
                        "Vals records reasoning enabled with no level, taken as high (E252)" if origin == "vals" else f"the source labels it {cell.get('effort')}")
                if cell.get("note"):
                    record["note"] = cell["note"]
                if leaf == "aiCodingDaily":
                    chosen = select_aicd(model_id, cell["sourceLabel"], board)
                    record["value"] = aicd_points(chosen["row"])
                    record["harness"] = chosen["row"]["harness"]
                    record["tested"] = chosen["row"]["tested"]
                    if chosen["alternates"]:
                        record["selection"] = f"one of {len(chosen['alternates']) + 1} rows for this configuration, chosen by {chosen['rule']} (I50 M2)"
                        record["alternates"] = [{"harness": row["harness"], "tested": row["tested"], "value": aicd_points(row)}
                                                for row in chosen["alternates"]]
                        record["note"] = (f"Tested {chosen['row']['tested']} with {chosen['row']['harness']}; "
                                          f"{record['selection']}; the other rows are listed under alternates.")
                records.append(record)
    document = {
        "schemaVersion": 1,
        "capturedAt": max(captured.values()),
        "rule": "Owner decisions O53-O55: leaves added by the max-effort and AI Coding Daily rankings; exact configuration only (O36), "
                "MiMo-V2.6-Pro matched at high by owner statement (O54, E252)",
        "sources": sources,
        "records": records,
    }
    (ROOT / "data" / "swe_tracks.json").write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({leaf: sum(1 for record in records if record["leaf"] == leaf) for leaf in LEAVES}))


if __name__ == "__main__":
    main()
