#!/usr/bin/env python3
"""Scan comment harvest. usage: c_scan.py file.jsonl [min_dollar]"""
import sys, json, re, datetime
fn = sys.argv[1]
mind = int(sys.argv[2]) if len(sys.argv) > 2 else 1
dollar = re.compile(r'\$\s?\d[\d,\.]*[kKmM]?|\bUSD\b', re.I)
pct = re.compile(r'\d+(?:\.\d+)?\s?%')
lim = re.compile(r'weekly|5.?hour|five.?hour|window|quota|usage|allowance|per week', re.I)
model = re.compile(r'opus|sonnet|haiku|fable|gpt-?6|codex|astra|\bsol\b|luna|terra|gemini|neon|carbon|argon|antigravity|muse|ember|mimo', re.I)
rows = []
for l in open(fn):
    c = json.loads(l)
    b = c.get('body') or ''
    nd = len(dollar.findall(b)); npc = len(pct.findall(b))
    if nd >= mind and npc >= 1 and lim.search(b) and model.search(b) and len(b) > 120:
        day = datetime.datetime.fromtimestamp(c['created_utc'], datetime.UTC).strftime('%Y-%m-%d')
        rows.append((day, c['id'], c['link_id'], c['author'], nd, npc, len(b), b.replace('\n', ' ')[:210]))
for r in sorted(rows):
    print(*r, sep=' | ')
print(len(rows), 'candidates', file=sys.stderr)
