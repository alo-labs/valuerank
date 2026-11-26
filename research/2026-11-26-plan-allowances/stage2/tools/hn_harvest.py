#!/usr/bin/env python3
"""HN Algolia harvest of comments/stories since a date. usage: hn_harvest.py YYYY-MM-DD out.jsonl q1 q2 ..."""
import sys, json, subprocess, urllib.parse, datetime, time, re, html

after, out = sys.argv[1:3]
queries = sys.argv[3:]
ts = int(datetime.datetime.strptime(after, '%Y-%m-%d').replace(tzinfo=datetime.timezone.utc).timestamp())
seen = {}
def get(url):
    for i in range(4):
        r = subprocess.run(['curl', '-sS', '-L', '--max-time', '60', url], capture_output=True)
        try:
            return json.loads(r.stdout.decode('utf-8', 'replace'))
        except Exception:
            time.sleep(2)
    return None

for q in queries:
    for tag in ('comment', 'story'):
        for page in range(0, 5):
            url = 'https://hn.algolia.com/api/v1/search_by_date?' + urllib.parse.urlencode({
                'query': q, 'tags': tag, 'numericFilters': f'created_at_i>{ts}', 'hitsPerPage': 100, 'page': page})
            d = get(url)
            if not d:
                break
            for h in d.get('hits', []):
                seen[h['objectID']] = h
            if page + 1 >= d.get('nbPages', 0):
                break
            time.sleep(0.3)
with open(out, 'w') as f:
    for k, h in seen.items():
        f.write(json.dumps(h, ensure_ascii=False) + '\n')
print(len(seen), 'items')
