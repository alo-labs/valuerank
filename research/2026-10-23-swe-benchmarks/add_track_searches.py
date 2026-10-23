"""Log the O36 searches for the leaves the two rankings add (O53-O55) in data/leaf_evidence.json.

Every cohort configuration without an exact record for an added leaf gets one search entry per leaf, dated 2026-10-23.
The entry records the benchmark's own board as the primary source and the SWE benchmark research as its open-web step
(I28). A source row for the same model at another or an unstated effort is a candidate, rejected as not the exact
configuration. Entries this script wrote before are replaced; other entries are kept.

    python3 research/2026-10-23-swe-benchmarks/add_track_searches.py
"""

import json
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
SEARCHED = "2026-10-23"
MARK = "O53 track leaf search"
RESEARCH = [
    "Claude deep research, three researchers: research/2026-10-23-swe-benchmarks/research_notes/SWE benchmark candidates/ (owner-named sources, Vals AI, other agentic benchmarks)",
    "Perplexity Search with Thinking on research/2026-10-23-swe-benchmarks/brief.md: GPT-6.1 Sol, Grok 4.7, Gemini 3.8 Flash (pplx-*.md)",
    "Coverage capture of every cohort configuration: research/2026-10-23-swe-benchmarks/vals-catalogue-2026-10-23.json and other-coverage-2026-10-23.json (raw pages and JSON in vals-capture/ and other-capture/)",
    "Check of Epoch MirrorCode, SWE-bench-Live and SWE-PolyBench (report addendum)",
]
LEAVES = {
    "vibeCode": ("vals", "vibe-code", "https://www.vals.ai/benchmarks/vibe-code (benchmark_view JSON, updated 2026-10-20)"),
    "codeMigration": ("vals", "code-migration-v1-1", "https://www.vals.ai/benchmarks/code-migration-v1-1 (benchmark_view JSON, updated 2026-10-20)"),
    "livebenchAgentic": ("other", "livebench2-agentic", "https://livebench.ai/data/20261014/table.csv and the site bundle's model metadata (release 2026-10-14, updated 2026-10-18)"),
    "livebenchCoding": ("other", "livebench2-coding", "https://livebench.ai/data/20261014/table.csv and the site bundle's model metadata (release 2026-10-14, updated 2026-10-18)"),
    "aiCodingDaily": ("other", "aicd-non-bug", "https://aicodingdaily.com/leaderboard, every row including hidden older models (updated 2026-10-21)"),
}


def main() -> None:
    vals = {item["slug"]: item for item in json.loads((HERE / "vals-catalogue-2026-10-23.json").read_text())["benchmarks"]}
    other = {item["key"]: item for item in json.loads((HERE / "other-coverage-2026-10-23.json").read_text())["benchmarks"]}
    cohort = [row["id"] for row in json.loads((HERE / "cohort-2026-10-23.json").read_text())["configurations"]]
    records = {(record["modelId"], record["leaf"]) for record in json.loads((ROOT / "data" / "swe_tracks.json").read_text())["records"]}
    path = ROOT / "data" / "leaf_evidence.json"
    evidence = json.loads(path.read_text())
    searches = [entry for entry in evidence["searches"] if entry.get("searchKind") != MARK]
    for leaf, (origin, key, board) in LEAVES.items():
        coverage = (vals if origin == "vals" else other)[key]["coverage"]
        for model_id in cohort:
            if (model_id, leaf) in records:
                continue
            cell = coverage[model_id]
            candidates = []
            if cell["status"] == "plausible":
                candidates.append({
                    "url": board.split(" ")[0], "publisher": board.split("/")[2], "published": SEARCHED,
                    "reports": f"{cell.get('sourceLabel') or cell.get('valsKey')}: {cell['value']} at effort {cell.get('effort') or 'not stated'}",
                    "resolution": "reject", "reason": "not the exact configuration: AA plots this model without an effort label and the source's effort is not established as AA's",
                })
            searches.append({
                "modelId": model_id, "leaf": leaf, "searchedOn": SEARCHED, "result": "not found", "searchKind": MARK,
                "sources": [board],
                "notes": cell.get("note") or f"No {leaf} record for this configuration at its exact effort.",
                "openWeb": {"searchedOn": SEARCHED, "record": "research/2026-10-23-swe-benchmarks/reports/SWE benchmark candidates.md",
                            "queries": RESEARCH, "candidates": candidates},
            })
    evidence["searches"] = searches
    path.write_text(json.dumps(evidence, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"searches": len(searches), "trackSearches": sum(1 for entry in searches if entry.get("searchKind") == MARK)}))


if __name__ == "__main__":
    main()
