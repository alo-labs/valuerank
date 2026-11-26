#!/usr/bin/env python3
import sys, json, re, html, datetime
fn = sys.argv[1]
def strip(s):
    s = re.sub(r'<[^>]+>', ' ', s or '')
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()
dollar = re.compile(r'\$\s?\d[\d,\.]*[kKmM]?')
pct = re.compile(r'\d+\s?%')
plan = re.compile(r'\b(pro|max|ultra|plus|20x|5x|plan|subscription)\b', re.I)
model = re.compile(r'opus|sonnet|haiku|fable|gpt-?6|codex|astra|sol\b|luna|terra|gemini|neon|carbon|argon|antigravity|muse|ember|mimo', re.I)
lim = re.compile(r'weekly|5.?hour|five.?hour|session|quota|limit|allowance', re.I)
rows = []
for l in open(fn):
    h = json.loads(l)
    txt = strip(h.get('comment_text') or h.get('story_text') or h.get('title'))
    nd = len(dollar.findall(txt)); npc = len(pct.findall(txt))
    if nd >= 1 and npc >= 1 and lim.search(txt) and model.search(txt) and plan.search(txt):
        day = datetime.datetime.fromtimestamp(h['created_at_i'], datetime.UTC).strftime('%Y-%m-%d')
        rows.append((day, h['objectID'], h.get('author'), nd, npc, len(txt), txt[:200]))
for r in sorted(rows):
    print(*r, sep=' | ')
print(len(rows), 'candidates')
