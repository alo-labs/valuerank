"""Changed-text extract for a targeted review (O209): the sentences of draft B that differ from draft A, each with its paragraph's
opening words and the old wording beside it, so a reviewer reads only what changed.

usage: python3 changed_text.py <review copy A> <review copy B> <out.md> [title]
"""

import difflib
import re
import sys
from pathlib import Path

a_lines = Path(sys.argv[1]).read_text().split("\n")
b_lines = Path(sys.argv[2]).read_text().split("\n")
SPLIT = re.compile(r"(?<=[.;:])\s+(?=[A-Z*`(\[{|])")


def sentences(text: str) -> list[str]:
    return [s for s in SPLIT.split(text) if s.strip()]


def pair_lines(a: list[str], b: list[str]):
    """Yield (old paragraph or '', new paragraph) for every changed line of b."""

    matcher = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        olds = a[i1:i2]
        for offset, new in enumerate(b[j1:j2]):
            if not new.strip():
                continue
            best = max(olds, key=lambda old: difflib.SequenceMatcher(None, old[:3000], new[:3000], autojunk=False).quick_ratio(), default="")
            yield best, new


out = [f"# {sys.argv[4] if len(sys.argv) > 4 else 'Changed text'}", "",
       "Each entry names the paragraph by its opening words, then lists the sentences that are new or reworded, with the previous wording of the replaced sentences after \"was:\". "
       "Review only these sentences against the decision ledger; text not shown here is unchanged and was reviewed in earlier rounds.", ""]
count = 0
for old, new in pair_lines(a_lines, b_lines):
    old_s, new_s = sentences(old), sentences(new)
    sm = difflib.SequenceMatcher(None, old_s, new_s, autojunk=False)
    entries = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        entries.append((" ".join(new_s[j1:j2]), " ".join(old_s[i1:i2])))
    if not entries:
        continue
    count += 1
    out.append(f"## {count}. {new[:110].strip()}…")
    for fresh, was in entries:
        out.append(f"- NEW: {fresh}")
        if was:
            out.append(f"  - was: {was}")
    out.append("")
Path(sys.argv[3]).write_text("\n".join(out))
print(count, "paragraphs;", len("\n".join(out)), "characters")
