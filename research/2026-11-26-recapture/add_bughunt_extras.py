"""O163 (2026-11-01): carry Bug Hunt Bench's genuine unplanted fixes ("extras", the board's per-run mean) beside the
planted count, so the leaf can be their sum. Reads the pinned board captures in third-party/bughunt/ and writes
data/bug_hunt.json (models[].extras, models[].totalFound) and data/bug_hunt_scoreboard.json (rows[].extras). Idempotent.
"""

import csv
import glob
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BOARD = ROOT / "research/2026-11-01-recapture/third-party/bughunt"


def main() -> None:
    runs = {row["id"]: row for row in json.loads((BOARD / "benchmark.json").read_text())["runs"]}
    path = ROOT / "data/bug_hunt.json"
    document = json.loads(path.read_text())
    for model in document["models"]:
        if not model.get("matched"):
            continue
        row = runs.get(model["evaluatedModel"])
        if row is None or row.get("fixed") != model["fixedOf105"]:
            raise ValueError(f"{model['modelId']}: board row {model['evaluatedModel']!r} missing or its planted count differs")
        model["extras"] = row["extras"]
        model["totalFound"] = round(model["fixedOf105"] + row["extras"], 4)
    path.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n")
    combined = list(csv.DictReader(open(glob.glob(str(BOARD / "combined-*.csv"))[0])))
    path = ROOT / "data/bug_hunt_scoreboard.json"
    board = json.loads(path.read_text())
    if len(combined) != len(board["rows"]):
        raise ValueError("the pinned combined scoreboard and data/bug_hunt_scoreboard.json differ in length")
    for row, source in zip(board["rows"], combined):
        if (row["model"], row["harness"], row["fixedOf105"]) != (source["model"], source["harness"], float(source["fixed_of_105"])):
            raise ValueError(f"scoreboard row {row['model']!r} does not match the pinned combined CSV")
        row["extras"] = float(source["genuine_extras_total"])
    path.write_text(json.dumps(board, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"matched": sum(1 for model in document["models"] if model.get("matched")), "scoreboardRows": len(board["rows"])}))


if __name__ == "__main__":
    main()
