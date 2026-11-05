"""O52 trade-off: how many cohort configurations each candidate benchmark set would rank.

A configuration is ranked when it has every chosen benchmark at its exact effort (O36, O52). The nine AA leaves
cover every cohort configuration; Bug Hunt misses MiMo-V2.6-Flash and MiniMax-M3.1-Flash. Candidates come from the
Vals catalogue and the other-source coverage file. Usage:

    python3 tradeoff.py [--plausible] [--max-size N] [--only key1,key2,...]

``--plausible`` also counts plausible matches (same model, effort unlabelled by AA or the source).
"""

import argparse
import itertools
import json
from pathlib import Path

HERE = Path(__file__).parent
BUG_HUNT_MISSING = {"mimo-v2-6-flash", "minimax-m3-1-flash"}


def candidates(plausible: bool) -> dict:
    """Candidate benchmark key -> set of cohort ids it covers."""

    accepted = {"exact", "plausible"} if plausible else {"exact"}
    result = {}
    vals = HERE / "vals-catalogue-2026-10-23.json"
    if vals.exists():
        for item in json.loads(vals.read_text())["benchmarks"]:
            if item.get("archived"):
                continue
            result["vals:" + item["slug"]] = {cid for cid, cell in item["coverage"].items() if cell["status"] in accepted}
    other = HERE / "other-coverage-2026-10-23.json"
    if other.exists():
        for item in json.loads(other.read_text())["benchmarks"]:
            result[item["key"]] = {cid for cid, cell in item["coverage"].items() if cell["status"] in accepted}
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plausible", action="store_true")
    parser.add_argument("--max-size", type=int, default=4)
    parser.add_argument("--only", default="")
    parser.add_argument("--min-ranked", type=int, default=2)
    args = parser.parse_args()

    cohort = [row["id"] for row in json.loads((HERE / "cohort-2026-10-23.json").read_text())["configurations"]]
    base = set(cohort) - BUG_HUNT_MISSING
    pool = candidates(args.plausible)
    if args.only:
        pool = {key: pool[key] for key in args.only.split(",")}
    print(f"cohort {len(cohort)}; current ten leaves rank {len(base)}")
    for key, covered in sorted(pool.items(), key=lambda kv: -len(kv[1] & base)):
        print(f"  {key}: {len(covered & set(cohort))} of cohort, {len(covered & base)} with the current leaves")
    best = {}
    keys = [key for key, covered in pool.items() if len(covered & base) >= args.min_ranked]
    for size in range(1, args.max_size + 1):
        for combo in itertools.combinations(keys, size):
            ranked = set(base)
            for key in combo:
                ranked &= pool[key]
            if len(ranked) > len(best.get(size, ((), set()))[1]):
                best[size] = (combo, ranked)
    for size, (combo, ranked) in sorted(best.items()):
        print(f"best set of {size} added: {', '.join(combo)} -> {len(ranked)} ranked: {', '.join(sorted(ranked))}")


if __name__ == "__main__":
    main()
