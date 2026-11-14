"""Compare two captures of the OpenCode Go docs page by their visible text (tags, scripts and styles removed)."""

import difflib
import html
import re
import sys
from pathlib import Path


def text(path: str) -> str:
    raw = Path(path).read_text(encoding="utf-8", errors="replace")
    raw = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", "", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", html.unescape(raw)).strip()


old, new = text(sys.argv[1]), text(sys.argv[2])
print("visible text identical:", old == new, "| lengths", len(old), len(new))
matcher = difflib.SequenceMatcher(None, old, new, autojunk=False)
for tag, a0, a1, b0, b1 in matcher.get_opcodes():
    if tag != "equal":
        print(tag, repr(old[max(0, a0 - 40):a1 + 40]), "->", repr(new[max(0, b0 - 40):b1 + 40]))
