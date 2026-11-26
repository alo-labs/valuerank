"""Compare the plan table and the usage-limit tables of two OpenCode Go page captures (from 'Go works like any other' to
'Estimated requests'), which hold every figure the O198 routes use."""

import html
import re
import sys
from pathlib import Path


def section(path: str) -> str:
    raw = Path(path).read_text(encoding="utf-8", errors="replace")
    raw = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", "", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    plain = re.sub(r"\s+", " ", html.unescape(raw)).strip()
    start = plain.index("OpenCode Go gives you reliable access")
    end = plain.index("Estimated requests", start)
    return plain[start:end]


old, new = section(sys.argv[1]), section(sys.argv[2])
print("plan, model and limit section identical:", old == new, "| lengths", len(old), len(new))
if old != new:
    import difflib
    for tag, a0, a1, b0, b1 in difflib.SequenceMatcher(None, old, new, autojunk=False).get_opcodes():
        if tag != "equal":
            print(tag, repr(old[max(0, a0 - 60):a1 + 60]), "->", repr(new[max(0, b0 - 60):b1 + 60]))
