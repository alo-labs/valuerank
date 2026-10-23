"""Build data/swe_tracks.json, the leaf evidence of the two rankings' added software-engineering leaves (O53-O55).

Reads the verified coverage captures in this folder and keeps exact-configuration matches only. MiMo-V2.6-Pro is the one
exception, by owner decision O54 and editor decision E252: AA's configuration is high, so AI Coding Daily's and LiveBench's
"high" rows are exact, and Vals' run (reasoning enabled, no level recorded) is the same single reasoning mode.

    python3 research/2026-10-23-swe-benchmarks/build_swe_tracks.py
"""

import json
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
OWNER_MATCHED = {"mimo-v2-6-pro"}  # O54, E252

LEAVES = {
    # leaf key: (coverage key, coverage file, source metadata)
    "vibeCode": ("vibe-code", "vals", {
        "benchmark": "Vibe Code Bench v1.1", "publisher": "Vals AI", "updated": "2026-10-20",
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
    "livebenchAgentic": ("livebench2-agentic", "other", {
        "benchmark": "LiveBench 2.0 Long Agentic (release 2026-10-14)", "publisher": "LiveBench", "updated": "2026-10-18",
        "url": "https://livebench.ai/data/20261014/table.csv", "harness": "LiveBench's own, one run per model at its top effort",
        "metric": "mean task score (0-100)", "unit": "percent", "sampling": {"kind": "tasks", "tasks": 18},
    }),
    "livebenchCoding": ("livebench2-coding", "other", {
        "benchmark": "LiveBench 2.0 Coding (release 2026-10-14)", "publisher": "LiveBench", "updated": "2026-10-18",
        "url": "https://livebench.ai/data/20261014/table.csv", "harness": "LiveBench's own, one run per model at its top effort",
        "metric": "mean task score (0-100)", "unit": "percent", "sampling": {"kind": "tasks", "tasks": 29},
    }),
    "aiCodingDaily": ("aicd-non-bug", "other", {
        "benchmark": "AI Coding Daily LLM Coding Leaderboard (Laravel quality + React-TS quality + edge-case testing, max 60)",
        "publisher": "AI Coding Daily (Povilas Korop)", "updated": "2026-10-21", "url": "https://aicodingdaily.com/leaderboard",
        "harness": "varies by model: Claude Code, Codex CLI, OpenCode, Devin, DeepSeek's harness (named on each record)",
        "metric": "judged points out of 60 (the 10-point bug-finding column is excluded: it overlaps Bug Hunt)", "unit": "points of 60",
        "sampling": {"kind": "tasks", "tasks": 6, "unit": "graded projects (Laravel, React-TS and 4 edge-case projects)"},
    }),
}


def main() -> None:
    vals = {item["slug"]: item for item in json.loads((HERE / "vals-catalogue-2026-10-23.json").read_text())["benchmarks"]}
    other = {item["key"]: item for item in json.loads((HERE / "other-coverage-2026-10-23.json").read_text())["benchmarks"]}
    cohort = [row["id"] for row in json.loads((HERE / "cohort-2026-10-23.json").read_text())["configurations"]]
    records, sources = [], {}
    for leaf, (key, origin, meta) in LEAVES.items():
        sources[leaf] = meta
        coverage = (vals if origin == "vals" else other)[key]["coverage"]
        for model_id in cohort:
            cell = coverage[model_id]
            if cell["status"] == "exact" or (cell["status"] == "plausible" and model_id in OWNER_MATCHED):
                record = {
                    "modelId": model_id, "leaf": leaf, "value": cell["value"],
                    "sourceLabel": cell.get("valsKey") or cell.get("sourceLabel"), "effort": cell.get("effort"),
                    "locator": f"research/2026-10-23-swe-benchmarks/{'vals-catalogue' if origin == 'vals' else 'other-coverage'}-2026-10-23.json"
                               f" benchmarks[{'slug' if origin == 'vals' else 'key'}={key}].coverage[{model_id}]",
                }
                if cell.get("stderr") is not None:
                    record["stderr"] = cell["stderr"]
                if cell["status"] == "plausible":
                    record["match"] = "owner (O54): AA's configuration is high; " + (
                        "Vals records reasoning enabled with no level, taken as high (E252)" if origin == "vals" else f"the source labels it {cell.get('effort')}")
                if cell.get("note"):
                    record["note"] = cell["note"]
                records.append(record)
    document = {
        "schemaVersion": 1,
        "capturedAt": "2026-10-23T08:00:00Z",
        "rule": "Owner decisions O53-O55: leaves added by the max-effort and AI Coding Daily rankings; exact configuration only (O36), "
                "MiMo-V2.6-Pro matched at high by owner statement (O54, E252)",
        "sources": sources,
        "records": records,
    }
    (ROOT / "data" / "swe_tracks.json").write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({leaf: sum(1 for record in records if record["leaf"] == leaf) for leaf in LEAVES}))


if __name__ == "__main__":
    main()
