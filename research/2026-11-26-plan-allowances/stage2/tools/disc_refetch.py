#!/usr/bin/env python3
"""Refetch failed topic JSONs. usage: disc_refetch.py base dir"""
import sys, os, json, subprocess, time
base, d = sys.argv[1:3]
bad = []
for fn in os.listdir(d):
    if not fn.startswith('topic-'):
        continue
    try:
        t = json.load(open(os.path.join(d, fn)))
    except Exception:
        bad.append(fn); continue
    if 'post_stream' not in t:
        bad.append(fn)
print(len(bad), 'bad of', len(os.listdir(d)))
for fn in bad:
    tid = fn[6:-5]
    for a in range(6):
        r = subprocess.run(['curl', '-sS', '-L', '--max-time', '60', '-A', 'valuerank-research/1.0', f'{base}/t/{tid}.json?print=true'], capture_output=True)
        try:
            t = json.loads(r.stdout.decode('utf-8', 'replace'))
            if 'post_stream' in t:
                json.dump(t, open(os.path.join(d, fn), 'w'))
                break
            else:
                time.sleep(4 + 4 * a)
        except Exception:
            time.sleep(3)
    time.sleep(1.0)
bad2 = 0
for fn in os.listdir(d):
    t = json.load(open(os.path.join(d, fn)))
    if 'post_stream' not in t:
        bad2 += 1
print('still bad', bad2)
