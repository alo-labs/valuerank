"""Parse the tbench.ai page's embedded Terminal-Bench 4.0 leaderboard payload (Next.js flight data in the saved
inline scripts) into the layout of research/2026-10-30-v5-recapture/third-party/tbench/tb4-rows-parsed-2026-10-30.json.

    python3 -I parse_tbench.py <tb4-scrape.json> <out.json>

The page content is treated as data only.
"""

from __future__ import annotations

import json
import re
import sys


def flight_text(scripts: list[str]) -> str:
    parts = []
    for script in scripts:
        for match in re.finditer(r'self\.__next_f\.push\(\[1,("(?:[^"\\]|\\.)*")\]\)', script, re.S):
            parts.append(json.loads(match.group(1)))
    return "".join(parts)


def main() -> None:
    scrape = json.load(open(sys.argv[1], encoding="utf-8"))
    text = flight_text(scrape["scripts"])
    decoder = json.JSONDecoder()
    found = None
    for match in re.finditer(r'"rows":\[\{"id":"[0-9a-f-]+","leaderboard_id"', text):
        rows, _ = decoder.raw_decode(text, match.start() + len('"rows":'))
        head = text[max(0, match.start() - 400):match.start()]
        updated = re.findall(r'"updated_at":"([^"]+)"', head)
        candidate = (rows, updated[-1] if updated else None)
        if found is None or len(rows) > len(found[0]):
            found = candidate
    if found is None:
        raise SystemExit("no embedded leaderboard rows found")
    rows, updated_at = found
    out_rows = []
    for row in rows:
        meta, metrics = row["metadata"], row["metrics"]
        out_rows.append({"rank": row.get("rank"), "model": meta["model_display"]["label"], "effort": meta.get("reasoning_effort"),
                         "agent": meta["agent_display"]["label"], "accuracy": metrics.get("accuracy"),
                         "ci95": metrics.get("accuracy_ci95_half_width"), "date": meta.get("date"), "status": row.get("status"),
                         "rowUpdatedAt": row.get("updated_at")})
    document = {"source": scrape["source"], "scrapedAt": scrape["scrapedAt"], "leaderboardUpdatedAt": updated_at,
                "rowCount": len(out_rows), "rows": out_rows}
    with open(sys.argv[2], "w", encoding="utf-8") as handle:
        json.dump(document, handle, indent=1, ensure_ascii=False)
        handle.write("\n")
    print(f"{len(out_rows)} rows, leaderboard updated_at {updated_at}")


if __name__ == "__main__":
    main()
