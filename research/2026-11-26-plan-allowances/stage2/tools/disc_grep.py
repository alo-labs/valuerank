#!/usr/bin/env python3
"""usage: disc_grep.py dir after regex [context]  -> prints posts after date matching regex with snippet"""
import sys, json, os, re, html
d, after, rx = sys.argv[1:4]
ctx = int(sys.argv[4]) if len(sys.argv) > 4 else 160
rxc = re.compile(rx, re.I)
def strip(s):
    s = re.sub(r'<[^>]+>', ' ', s or '')
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()
n = 0
for fn in sorted(os.listdir(d)):
    if not fn.startswith('topic-'):
        continue
    t = json.load(open(os.path.join(d, fn)))
    for p in t.get('post_stream', {}).get('posts', []):
        if p['created_at'][:10] < after:
            continue
        txt = strip(p.get('cooked'))
        m = rxc.search(txt)
        if m:
            n += 1
            s = max(0, m.start() - ctx); e = min(len(txt), m.end() + ctx)
            print(f"{p['created_at'][:10]} | t{t['id']}#{p['post_number']} | {p['username']} | {t.get('title','')[:60]} | ...{txt[s:e]}...")
print(n, 'matches')
