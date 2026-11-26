#!/usr/bin/env python3
"""Fetch the tail of a long Discourse thread. usage: disc_thread.py base topic_id last_n out.json"""
import sys, json, subprocess, time
base, tid, n, out = sys.argv[1:5]
n = int(n)
def get(url):
    for a in range(6):
        r = subprocess.run(['curl', '-sS', '-L', '--max-time', '60', '-A', 'valuerank-research/1.0', url], capture_output=True)
        try:
            d = json.loads(r.stdout.decode('utf-8', 'replace'))
            if 'errors' in d:
                time.sleep(4 + 4 * a); continue
            return d
        except Exception:
            time.sleep(3)
    return None
t = get(f'{base}/t/{tid}.json')
stream = t['post_stream']['stream']
ids = stream[-n:]
posts = []
for i in range(0, len(ids), 20):
    chunk = ids[i:i + 20]
    q = '&'.join(f'post_ids[]={x}' for x in chunk)
    d = get(f'{base}/t/{tid}/posts.json?{q}')
    if d:
        posts.extend(d['post_stream']['posts'])
    time.sleep(1.0)
json.dump({'topic': {k: t.get(k) for k in ('id', 'title', 'created_at', 'posts_count')}, 'posts': posts}, open(out, 'w'))
print(len(posts), 'posts saved')
