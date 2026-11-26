#!/usr/bin/env python3
"""Bluesky search harvest. usage: bsky.py since out.jsonl q1 q2 ..."""
import sys, json, subprocess, urllib.parse, time
since, out = sys.argv[1:3]
qs = sys.argv[3:]
seen = {}
def get(url):
    for i in range(3):
        r = subprocess.run(['curl', '-sS', '-L', '--max-time', '60', '-A', 'valuerank-research/1.0', url], capture_output=True)
        try:
            return json.loads(r.stdout.decode('utf-8', 'replace'))
        except Exception:
            time.sleep(2)
    return None
for q in qs:
    cursor = None
    for page in range(5):
        params = {'q': q, 'since': since + 'T00:00:00Z', 'limit': 100, 'sort': 'latest'}
        if cursor:
            params['cursor'] = cursor
        d = get('https://api.bsky.app/xrpc/app.bsky.feed.searchPosts?' + urllib.parse.urlencode(params))
        if not d or 'posts' not in d:
            print('ERR', q, str(d)[:200]); break
        for p in d['posts']:
            seen[p['uri']] = p
        cursor = d.get('cursor')
        if not cursor or not d['posts']:
            break
        time.sleep(0.4)
with open(out, 'w') as f:
    for u, p in seen.items():
        f.write(json.dumps(p, ensure_ascii=False) + '\n')
print(len(seen), 'posts')
