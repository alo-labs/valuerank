#!/usr/bin/env python3
import sys, json, re
dollar = re.compile(r'\$\s?\d[\d,\.]*[kKmM]?')
pct = re.compile(r'\d+\s?%')
for l in open(sys.argv[1]):
    p = json.loads(l)
    t = p.get('record', {}).get('text', '')
    if len(dollar.findall(t)) >= 1 and len(pct.findall(t)) >= 1:
        print(p['record'].get('createdAt', '')[:10], p['author']['handle'], p['uri'].split('/')[-1], '|', t.replace('\n', ' ')[:260])
