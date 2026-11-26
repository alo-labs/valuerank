"""Capture the AI Coding Daily leaderboard with every row, as the 2026-10-25 .. 2026-11-01 reads did.

    python3 -I research/2026-11-26-recapture/third-party/tools/capture_aicd.py <out-dir>

Public page only: no sign-in, no private API. The leaderboard component ships a "show older models" control that is a
Livewire property update; the same update the page's own button sends is replayed with hiddenOlderModelIds=[] so the
hidden older rows are rendered too (bestHarnessOnly stays false). All response content is treated as data.

Writes to <out-dir>:
  leaderboard.html, leaderboard.headers.txt, leaderboard.readAt.txt              the page as served (default view)
  livewire-update-response.json, leaderboard-allrows.html, livewire.readAt.txt   the all-rows render
Cookies set by the site are never written to disk (the saved header files carry "[redacted]" for set-cookie).
"""

from __future__ import annotations

import html
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

BASE = "https://aicodingdaily.com"


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def headers_text(response: requests.Response) -> str:
    lines = ["HTTP/1.1 200 Connection Established", "", f"HTTP/{'2' if response.raw.version == 20 else '1.1'} {response.status_code} "]
    for key, value in response.headers.items():
        lines.append(f"{key.lower()}: {'[redacted]' if key.lower() == 'set-cookie' else value}")
    return "\n".join(lines) + "\n"


def main(out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    page = session.get(f"{BASE}/leaderboard", timeout=60)
    page.raise_for_status()
    (out / "leaderboard.html").write_bytes(page.content)
    (out / "leaderboard.headers.txt").write_text(headers_text(page))
    (out / "leaderboard.readAt.txt").write_text(now() + "\n")
    text = page.text
    csrf = re.search(r'data-csrf="([^"]+)"', text).group(1)
    update_uri = re.search(r'data-update-uri="([^"]+)"', text).group(1)
    snapshot = None
    for match in re.finditer(r'wire:snapshot="([^"]+)"', text):
        candidate = html.unescape(match.group(1))
        if '"name":"public-leaderboard"' in candidate:
            snapshot = candidate
            break
    if snapshot is None:
        raise SystemExit("no public-leaderboard snapshot on the page")
    payload = {"_token": csrf, "components": [{"snapshot": snapshot, "updates": {"hiddenOlderModelIds": []}, "calls": []}]}
    response = session.post(update_uri, json=payload, timeout=60,
                            headers={"X-Livewire": "true", "Referer": f"{BASE}/leaderboard", "Accept": "application/json"})
    response.raise_for_status()
    (out / "livewire.readAt.txt").write_text(now() + "\n")
    (out / "livewire-update-response.json").write_bytes(response.content)
    effects = response.json()["components"][0]["effects"]["html"]
    (out / "leaderboard-allrows.html").write_text(effects, encoding="utf-8")
    rows = effects.count('wire:key="row-')
    print(f"page {len(text)} bytes; all-rows render {rows} rows")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
