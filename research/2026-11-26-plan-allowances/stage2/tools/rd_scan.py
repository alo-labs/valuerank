#!/usr/bin/env python3
"""Scan reddit dumps for report-like posts. usage: rd_scan.py file.jsonl [mindollar] """
import sys, json, re, datetime
fn = sys.argv[1]
mind = int(sys.argv[2]) if len(sys.argv) > 2 else 2
dollar = re.compile(r'\$\s?\d[\d,\.]*[kKmM]?|\bUSD\b|\d[\d,\.]*\s?(?:dollars|USD)\b', re.I)
pct = re.compile(r'\d+(?:\.\d+)?\s?%')
plan = re.compile(r'\b(pro|max|ultra|plus|20x|5x|10x|plan|subscription|tier)\b', re.I)
model = re.compile(r'opus|sonnet|haiku|fable|gpt-?6|codex|astra|\bsol\b|luna|terra|gemini|neon|carbon|argon|antigravity|muse|ember|mimo', re.I)
lim = re.compile(r'weekly|5.?hour|five.?hour|session|quota|usage limit|allowance|meter|ccusage|burn', re.I)
rows = []
for l in open(fn):
    p = json.loads(l)
    txt = (p.get('title') or '') + ' ' + (p.get('selftext') or '')
    nd = len(dollar.findall(txt)); npc = len(pct.findall(txt))
    if nd >= mind and npc >= 1 and lim.search(txt) and model.search(txt) and plan.search(txt):
        day = datetime.datetime.fromtimestamp(p['created_utc'], datetime.UTC).strftime('%Y-%m-%d')
        rows.append((day, p['id'], p.get('author'), nd, npc, len(txt), (p.get('title') or '')[:90]))
for r in sorted(rows):
    print(*r, sep=' | ')
print(len(rows), 'candidates', file=sys.stderr)
