#!/usr/bin/env python3
"""Arctic Shift comments body search by day windows. usage: as_cbody_days.py sub startdate enddate out.jsonl term..."""
import sys, json, subprocess, time, urllib.parse, datetime
sub, start, end, out = sys.argv[1:5]
terms = sys.argv[5:]
seen = {}
def fetch(url):
    for a in range(4):
        r = subprocess.run(['curl', '-sS', '-L', '--max-time', '60', '-A', 'valuerank-research/1.0', url], capture_output=True)
        try:
            d = json.loads(r.stdout.decode('utf-8', 'replace'))
            if d.get('data') is not None:
                return d['data']
        except Exception:
            pass
        time.sleep(2 + 2 * a)
    return None
d0 = datetime.date.fromisoformat(start); d1 = datetime.date.fromisoformat(end)
fails = 0
day = d0
while day < d1:
    nxt = day + datetime.timedelta(days=1)
    for term in terms:
        cur = day.isoformat()
        for page in range(30):
            params = {'subreddit': sub, 'body': term, 'after': cur, 'before': nxt.isoformat(), 'limit': '100', 'sort': 'asc'}
            data = fetch('https://arctic-shift.photon-reddit.com/api/comments/search?' + urllib.parse.urlencode(params))
            if data is None:
                fails += 1; break
            for c in data:
                seen[c['id']] = c
            if len(data) < 100:
                break
            cur = datetime.datetime.fromtimestamp(data[-1]['created_utc'], datetime.UTC).strftime('%Y-%m-%dT%H:%M:%S')
            time.sleep(0.3)
        time.sleep(0.3)
    day = nxt
with open(out, 'w') as f:
    for c in seen.values():
        f.write(json.dumps(c, ensure_ascii=False) + '\n')
print(sub, len(seen), 'comments, fails', fails, '->', out)
