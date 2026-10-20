"""Build a reviewer prompt that links the draft's parts on GitHub instead of pasting the draft.

Perplexity accepts at most 40,000 characters of typed query text; longer pastes become a file
upload, which the plan's weekly upload limit can block. Its GitHub connector truncates a file
after about 27,900 characters, so the draft is read as parts of at most 20,000 characters
(split_draft.py) from a pushed commit of the public repository, and the reviewer proves it read
every part to its end by quoting each part's last words.

usage: python3 build_github_review.py <reviewer-prompt.md> <draft-rNN.md> <parts.tsv> <ledger-brief.md> <commit sha> <out>
"""

import sys
from pathlib import Path

REPO = "alo-labs/valuerank"
LIMIT = 40_000

header_path, draft_path, parts_path, ledger_path, sha, out = sys.argv[1:7]
draft = Path(draft_path)
parts = [line.split("\t")[0] for line in Path(parts_path).read_text().splitlines() if line.strip()]
header = Path(header_path).read_text()
header = header.replace("Review the methodology draft below", "Review the methodology draft linked above")
header = header.replace("=== METHODOLOGY DRAFT ===", "").rstrip()
assert "linked above" in header, "reviewer header wording changed; update the substitution"
listing = "\n".join(
    f"{index}. {part} (raw: https://raw.githubusercontent.com/{REPO}/{sha}/{part})" for index, part in enumerate(parts, 1)
)
prompt = f"""@GitHub The methodology draft under review is {draft.name} ({len(draft.read_text()):,} characters) in the public GitHub repository {REPO} at commit {sha}. Because the GitHub connector truncates long files, read it as these {len(parts)} consecutive parts, each under 20,000 characters, which together are the whole draft in order:
{listing}
Open every part through the GitHub connector and read each one to its end before reviewing. Do not review from a summary or from search snippets.

Begin your answer with a section "## 0. Read check" that quotes exactly the draft's first line and then, for each part in order, its last 12 words. If any part could not be read to its end, say which one and stop.

{header}

=== DECISION LEDGER (condensed; the full ledger is ledger.md in the same folder) ===
{Path(ledger_path).read_text().strip()}
"""
assert len(prompt) <= LIMIT, f"prompt is {len(prompt)} characters; Perplexity accepts at most {LIMIT}"
Path(out).write_text(prompt)
print(len(prompt), "characters ->", out)
