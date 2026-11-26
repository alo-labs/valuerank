#!/usr/bin/env python3
"""Dump all posts (or comments) of a subreddit in a window via Arctic Shift, ascending, into a JSONL file.
usage: as_dump.py posts|comments subreddit after before outdir"""
import sys, json, subprocess, time, os, urllib.parse

def fetch(url):
    for attempt in range(6):
        r = subprocess.run(['curl', '-sS', '-L', '--max-time', '90', '-A', 'valuerank-research/1.0', url], capture_output=True)
        txt = r.stdout.decode('utf-8', 'replace')
        try:
            d = json.loads(txt)
            if d.get('data') is not None:
                return d['data']
        except Exception:
            pass
        time.sleep(3 + attempt * 3)
    return None

def main():
    kind, sub, after, before, outdir = sys.argv[1:6]
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, f'{kind}-{sub}.jsonl')
    cur = after
    total = 0
    seen = set()
    with open(out, 'w') as f:
        while True:
            params = {'subreddit': sub, 'after': cur, 'before': before, 'limit': '100', 'sort': 'asc'}
            url = f'https://arctic-shift.photon-reddit.com/api/{kind}/search?' + urllib.parse.urlencode(params)
            data = fetch(url)
            if data is None:
                print('FAIL at', cur, file=sys.stderr)
                break
            if not data:
                break
            new = 0
            for it in data:
                if it['id'] in seen:
                    continue
                seen.add(it['id'])
                f.write(json.dumps(it, ensure_ascii=False) + '\n')
                new += 1
            total += new
            last = data[-1]['created_utc']
            if new == 0 or len(data) < 100:
                break
            cur = str(int(last))
            time.sleep(0.5)
    print(sub, kind, total, 'saved to', out)

main()
