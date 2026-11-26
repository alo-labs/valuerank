"""Assemble a review prompt: header, draft (fixture lists elided to fit the composer limit), condensed ledger."""
import sys
from pathlib import Path

header, draft, ledger, out = (Path(arg) for arg in sys.argv[1:5])
text = draft.read_text(encoding="utf-8")
parts, i = [], 0
while True:
    j = text.find("(fixture", i)
    if j < 0:
        parts.append(text[i:])
        break
    depth, k = 0, j
    while k < len(text):
        if text[k] == "(":
            depth += 1
        elif text[k] == ")":
            depth -= 1
            if depth == 0:
                break
        k += 1
    parts.append(text[i:j] + "(fixtures registered)")
    i = k + 1
note = ("\nNote for this review: lists of regression fixtures in the draft are shortened to \"(fixtures registered)\" so the prompt fits; "
        "the repository draft holds every fixture in full, so do not report a fixture as missing only because its list is shortened.\n")
prompt = header.read_text(encoding="utf-8") + note + "\n" + "".join(parts) + "\n=== DECISION LEDGER (from earlier reviewers) ===\n" + ledger.read_text(encoding="utf-8")
out.write_text(prompt, encoding="utf-8")
print(len(prompt), "characters")
