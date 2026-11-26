#!/usr/bin/env python3
"""Discourse harvest. usage: disc_harvest.py base outdir after 'q1' 'q2' ...
Searches each query (paging up to 3 pages), collects topic ids, fetches each topic JSON (all posts) and saves."""
import sys, json, subprocess, urllib.parse, os, time, re

base, outdir, after = sys.argv[1:4]
queries = sys.argv[4:]
os.makedirs(outdir, exist_ok=True)

def get(url, tries=4):
    for i in range(tries):
        r = subprocess.run(['curl', '-sS', '-L', '--max-time', '60', '-A', 'valuerank-research/1.0', url], capture_output=True)
        txt = r.stdout.decode('utf-8', 'replace')
        try:
            return json.loads(txt)
        except Exception:
            time.sleep(2 + i * 2)
    return None

topics = {}
for q in queries:
    for page in (1, 2, 3):
        url = f'{base}/search.json?q=' + urllib.parse.quote(f'{q} after:{after}') + f'&page={page}'
        d = get(url)
        if not d:
            break
        ts = d.get('topics', [])
        for t in ts:
            topics.setdefault(t['id'], t['title'])
        if len(d.get('posts', [])) < 20:
            break
        time.sleep(0.4)
print('topics found', len(topics))
for tid, title in topics.items():
    fn = os.path.join(outdir, f'topic-{tid}.json')
    if os.path.exists(fn):
        continue
    d = get(f'{base}/t/{tid}.json?print=true')
    if d:
        json.dump(d, open(fn, 'w'))
    time.sleep(0.3)
print('saved', len(os.listdir(outdir)))
