"""Parse an AI Coding Daily leaderboard table (page HTML or Livewire effects.html) into the row layout of the 2026-10-30 read.

    python3 -I parse_aicd.py <in.html> <out.json>

Treats the HTML as data only. One output row per <tr wire:key="row-N">; fields as in
research/2026-10-30-v5-recapture/third-party/aicd/leaderboard-allrows-parsed.json.
"""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser


class Rows(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.rows: list[dict] = []
        self.row: dict | None = None
        self.cell: list[str] | None = None
        self.cells: list[str] = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "tr" and (attrs.get("wire:key") or "").startswith("row-"):
            self.row = {"familyId": attrs.get("data-model-family-id"), "links": [], "time": None, "timeTitle": None}
            self.cells = []
        elif self.row is not None and tag == "td":
            self.cell = []
        elif self.row is not None and tag == "a" and attrs.get("href"):
            self.row["links"].append(attrs["href"])
        elif self.row is not None and tag == "time":
            self.row["time"] = attrs.get("datetime")
            self.row["timeTitle"] = attrs.get("title")
        elif self.cell is not None and tag == "br":
            self.cell.append(" ")

    def handle_endtag(self, tag):
        if self.row is not None and tag == "td" and self.cell is not None:
            self.cells.append(re.sub(r"\s+", " ", "".join(self.cell)).strip())
            self.cell = None
        elif self.row is not None and tag == "tr":
            self.row["cells"] = self.cells
            self.rows.append(self.row)
            self.row = None

    def handle_data(self, data):
        if self.cell is not None:
            self.cell.append(data)


def parse(text: str) -> list[dict]:
    parser = Rows()
    parser.feed(text)
    out = []
    for row in parser.rows:
        cells = row["cells"]
        model_url = next((link for link in row["links"] if "/model/" in link), None)
        video = next((link for link in row["links"] if "youtube" in link or "youtu.be" in link), None)
        # The cell is "<age> <harness>"; the age text is the <time> element's text.
        age_text = re.sub(r"\s+", " ", cells[6]).strip()
        m = re.match(r"^(.*?\bago)\s+(.*)$", age_text)
        if m:
            age, harness = m.group(1), m.group(2)
        else:
            age, harness = None, age_text
        out.append({"rank": cells[0], "model": cells[1], "total": cells[2], "cost": cells[3], "time": cells[4],
                    "tested": row["time"], "testedTitle": row["timeTitle"], "age": age, "harness": harness,
                    "laravel": cells[7] if len(cells) > 7 else None, "react": cells[8] if len(cells) > 8 else None,
                    "bug": cells[9] if len(cells) > 9 else None, "edge": cells[10] if len(cells) > 10 else None,
                    "modelUrl": model_url, "video": video, "familyId": row["familyId"], "rawCells": cells})
    return out


if __name__ == "__main__":
    rows = parse(open(sys.argv[1], encoding="utf-8").read())
    with open(sys.argv[2], "w", encoding="utf-8") as handle:
        json.dump(rows, handle, indent=1, ensure_ascii=False)
        handle.write("\n")
    print(f"{len(rows)} rows -> {sys.argv[2]}")
