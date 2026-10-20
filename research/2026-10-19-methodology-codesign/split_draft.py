"""Split a draft into parts small enough for Perplexity's GitHub connector to return whole.

The connector truncates a file after about 27,900 characters, so each part holds at most
MAX_CHARS characters, cut at line boundaries (a line is a paragraph or list item). Earlier
parts in the output directory are removed so only the current draft's parts remain.

usage: python3 split_draft.py <draft-rNN.md> <output dir>
prints one line per part: <path>\t<last 12 words>
"""

import sys
from pathlib import Path

MAX_CHARS = 22_000

draft = Path(sys.argv[1])
out = Path(sys.argv[2])
text = draft.read_text()
parts, current = [], []
for line in text.split("\n"):
    candidate = "\n".join(current + [line])
    if current and len(candidate) > MAX_CHARS:
        # A part never ends on a heading or blank line: they move with the text they introduce.
        carried = []
        while current and (not current[-1].strip() or current[-1].startswith("#")):
            carried.insert(0, current.pop())
        parts.append("\n".join(current))
        current = carried + [line]
    else:
        current.append(line)
parts.append("\n".join(current))
assert all(len(part) <= MAX_CHARS for part in parts), "a single line exceeds the part size"
assert "\n".join(parts) == text, "parts do not reassemble the draft"
out.mkdir(parents=True, exist_ok=True)
for old in out.glob("*.md"):
    old.unlink()
stem = draft.stem
for index, part in enumerate(parts, 1):
    path = out / f"{stem}-part-{index}-of-{len(parts)}.md"
    path.write_text(part.rstrip("\n") + "\n")
    words = part.split()
    print(f"{path}\t{' '.join(words[-12:])}")
