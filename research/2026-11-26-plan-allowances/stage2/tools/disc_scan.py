#!/usr/bin/env python3
"""Scan harvested Discourse topics for posts with dollar figures + quota words, in window. usage: disc_scan.py dir after(YYYY-MM-DD) [extra_regex]"""
import sys, json, os, re, html

d, after = sys.argv[1:3]
extra = sys.argv[3] if len(sys.argv) > 3 else None
def strip(s):
    s = re.sub(r'<[^>]+>', ' ', s or '')
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()

dollar = re.compile(r'\$\s?\d[\d,\.]*|\bUSD\b|\bdollars?\b', re.I)
quota = re.compile(r'quota|limit|allowance|usage|weekly|five.?hour|5.?h', re.I)
hits = []
for fn in sorted(os.listdir(d)):
    if not fn.startswith('topic-'):
        continue
    t = json.load(open(os.path.join(d, fn)))
    title = t.get('title')
    for p in t.get('post_stream', {}).get('posts', []):
        day = p['created_at'][:10]
        if day < after:
            continue
        txt = strip(p.get('cooked'))
        nd = len(dollar.findall(txt))
        if nd >= 2 and quota.search(txt) and (extra is None or re.search(extra, txt, re.I)):
            hits.append((day, t['id'], p['post_number'], p['username'], nd, len(txt), title))
for h in sorted(hits):
    print(*h, sep=' | ')
print(len(hits), 'hits')
