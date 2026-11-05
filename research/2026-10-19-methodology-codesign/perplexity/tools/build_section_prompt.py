"""Sectional linked prompt: a reviewer whose answer can read only a few parts reviews one section of the draft."""
import re, sys
from pathlib import Path
header_path, draft_path, parts_path, ledger_path, repo, sha, first, last, out = sys.argv[1:10]
first, last = int(first), int(last)
draft = Path(draft_path)
parts = [line.split("\t")[0] for line in Path(parts_path).read_text().splitlines() if line.strip()]
chosen = parts[first - 1:last]
header = re.sub(r"the (artifact|methodology draft|draft) below", r"the \1 section linked above", Path(header_path).read_text())
header = re.sub(r"=== [A-Z ]+ ===\s*$", "", header.rstrip()).rstrip()
listing = "\n".join(f"{index}. {part}" for index, part in enumerate(chosen, first))
prompt = f"""@GitHub The draft under review is {draft.name} ({len(draft.read_text()):,} characters) in the public GitHub repository {repo} at commit {sha}, split into {len(parts)} consecutive parts. Your answer's tool budget cannot read all of them, so this is a sectional review: you review parts {first}–{last} only (other parts are reviewed in separate passes of this same model). Read these parts:
{listing}
Open each listed part through the GitHub connector and read it to its end. Your tool calls are limited: start immediately with part {first} and spend every call on one GitHub connector file read per listed part, in order. Do not fetch raw.githubusercontent.com URLs, do not search the repository or discover tools first, and do not open other parts. Do not review from a summary or from search snippets.

Begin your answer with a section "## 0. Read check" that quotes, for each listed part in order, its first line and its last 12 words. If any listed part could not be read to its end, say which one and stop.

Review only what these parts state. A rule they cite from another part counts as defined there; do not report it as missing.

{header}

=== DECISION LEDGER ===
{Path(ledger_path).read_text().strip()}
"""
assert len(prompt) <= 40_000, len(prompt)
Path(out).write_text(prompt)
print(len(prompt), "->", out)
