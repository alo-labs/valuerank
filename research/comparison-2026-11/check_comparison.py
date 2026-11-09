"""Independently check the comparison against captured scores and scoring helpers."""
import copy
import json
import math
from pathlib import Path
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]


def load_helpers():
    """Load scoring helpers from an isolated temporary repository copy."""
    with tempfile.TemporaryDirectory(prefix='valuerank-check-') as temporary:
        shutil.copytree(ROOT / 'valuerank', Path(temporary) / 'valuerank',
                        ignore=shutil.ignore_patterns('__pycache__'))
        previous = {key: sys.modules.pop(key) for key in list(sys.modules)
                    if key == 'valuerank' or key.startswith('valuerank.')}
        sys.path.insert(0, temporary)
        try:
            from valuerank.anchors import cost_score, value_score
            from valuerank.site.viewmodel import pareto_set
            return cost_score, value_score, pareto_set
        finally:
            sys.path.remove(temporary)
            for key in list(sys.modules):
                if key == 'valuerank' or key.startswith('valuerank.'):
                    del sys.modules[key]
            sys.modules.update(previous)


cost_score, value_score, pareto_set = load_helpers()

REQUESTED = [('DeepSeek V4.1 Flash 1017', 'max'), ('Claude Haiku 5.5', 'high'), ('Claude Haiku 5.5', 'xhigh'), ('Claude Haiku 5.5', 'max'), ('GPT-6 Luna', 'max'), ('GPT-6.1 Terra', 'low'), ('GPT-6.1 Terra', 'medium'), ('Claude Sonnet 5.5', 'medium'), ('Claude Opus 5.5', 'low')]
LOC = {'main': 'v3', 'aicd': 'v3Tracks.aicd', 'common': 'v3Tracks.common'}
DEEP = 'deepseek-v4-1-flash-1017'


def clean(value):
    if isinstance(value, float) and not math.isfinite(value): return None
    if isinstance(value, dict): return {k: clean(v) for k, v in value.items()}
    if isinstance(value, list): return [clean(v) for v in value]
    return value


def matches(row, name, effort):
    return row.get('effort') == effort and row.get('name') in (name, f'{name} ({effort})')


def check_track(record, track, name, effort, source):
    found = [r for r in track['rows'] if matches(r, name, effort)]
    if len(found) != 1: return ['source row absent or ambiguous']
    row = found[0]
    plans = [p for p in track['planRows'] if p['configurationId'] == row['id']]
    errors = []
    if record.get('source') != source or record.get('kind') != 'published': errors.append('wrong source or kind')
    if record.get('row') != clean(row): errors.append('published row mismatch')
    if record.get('planRows') != clean(plans): errors.append('plan rows mismatch')
    return errors


def check_pareto(points):
    rows = [{'id': str(i), 'cost': {'workload': 'w'}, 'api': {'costUsd': p['cost']}, 'quality': {'displayed': p['quality']}} for i, p in enumerate(points)]
    frontier = pareto_set(rows, 'w', 'api')
    return [f'wrong frontier: {p["configuration"]}' for i, p in enumerate(points) if p['onFrontierAmongPlotted'] != (str(i) in frontier)]


def check(comparison, scores, frozen):
    errors = []
    def require(condition, message):
        if not condition: errors.append(message)
    tracks = {'main': scores['v3'], **scores['v3Tracks']}
    metadata = comparison['metadata']
    require(metadata['observedAt'] == scores['observedAt'] and metadata['version'] == scores['version'] and metadata['source'] == 'data/scores.json' and metadata['kind'] == 'published', 'metadata mismatch')
    entries = comparison['configurations']
    require([(e['requested']['name'], e['requested']['effort']) for e in entries] == REQUESTED, 'requested configuration list mismatch')
    for entry in entries:
        name, effort = entry['requested']['name'], entry['requested']['effort']
        for key in LOC:
            track = tracks[key]
            found = [r for r in track['rows'] if matches(r, name, effort)]
            record = entry['tracks'].get(key)
            require(len(found) <= 1, f'{key}: ambiguous {name} {effort}')
            if not found:
                require(record is None, f'{key}: unexpected {name} {effort}')
                continue
            if record is None:
                errors.append(f'{key}: missing {name} {effort}')
                continue
            rid = found[0]['id']
            source = f'data/scores.json#{LOC[key]}.rows[id={rid}] and planRows[configurationId={rid}]'
            errors.extend(f'{key} {name} {effort}: {e}' for e in check_track(record, track, name, effort, source))
    for key in LOC:
        track = tracks[key]
        workload = track['mainWorkload']
        require(comparison['diagnostics'][key] == clean({'source': f'data/scores.json#{LOC[key]}.diagnostics.rankSeparability', 'kind': 'published', 'rankSeparability': track['diagnostics']['rankSeparability'], 'mainWorkload': workload}), f'{key}: diagnostics mismatch')
        deep = next(r for r in track['rows'] if r['id'] == DEEP)
        anchors = frozen[key]['workloads'][workload]['anchors']['plan']
        hypothetical = comparison['whatIf'][key]
        require(hypothetical['publishedFallback'] == clean(deep['planScore']), f'{key}: fallback mismatch')
        require(hypothetical['fallbackSource'] == f'data/scores.json#{LOC[key]}.rows[id={DEEP}].planScore', f'{key}: fallback source mismatch')
        filename = 'v3_frozen' + ('' if key == 'main' else '_' + key) + '.json'
        source = f'data/scores.json#{LOC[key]}.rows[id={DEEP}]; data/{filename}#workloads.{workload}.anchors.plan; valuerank/anchors.py#cost_score,value_score; valuerank/value_v3.py#competition_ranks'
        require(hypothetical['source'] == source and hypothetical['kind'] == 'what-if', f'{key}: what-if source mismatch')
        eligible = {r['id'] for r in track['rows'] if r['cost']['workload'] == workload}
        others = {p['id']: p['value'] for p in track['planRows'] if p['configurationId'] in eligible and p['configurationId'] != DEEP}
        for label, multiple in [('go', 10.0), ('goPlus', 5.0)]:
            cost = deep['api']['costUsd'] / multiple
            cs = cost_score(cost, anchors)
            value = value_score(cs, deep['quality']['displayed'], .25)
            values = {**others, DEEP + '@what-if': value}
            ranks = {k: 1 + sum(v2 > v for v2 in values.values() if v2 is not None) for k, v in values.items() if v is not None}
            expected = {'multiple': multiple, 'costUsd': cost, 'costScore': cs, 'value': value, 'rank': ranks.pop(DEEP + '@what-if'), 'otherPlanRanks': ranks}
            require(hypothetical[label] == expected, f'{key}: {label} what-if mismatch')
    specs = [('apiCommon', 'common', 'api', False), ('planCommonPublished', 'common', 'plan', False), ('planCommonWhatIf', 'common', 'plan', True), ('apiMain', 'main', 'api', False), ('apiAicd', 'aicd', 'api', False)]
    for chart, key, basis, whatif in specs:
        track = tracks[key]
        rows = copy.deepcopy(track['rows'])
        if whatif: next(r for r in rows if r['id'] == DEEP)['planScore']['costUsd'] = comparison['whatIf'][key]['go']['costUsd']
        workload = track['mainWorkload']
        metric = 'api' if basis == 'api' else 'planScore'
        selected = [r for r in rows if any(matches(r, *identity) for identity in REQUESTED) and r['cost']['workload'] == workload and r[metric]['costUsd'] is not None and r['quality']['displayed'] is not None]
        plotted, full = pareto_set(selected, workload, basis), pareto_set(rows, workload, basis)
        expected = []
        for row in selected:
            cost, quality = row[metric]['costUsd'], row['quality']['displayed']
            dominated = [o['id'] for o in selected if o['id'] != row['id'] and o[metric]['costUsd'] <= cost and o['quality']['displayed'] >= quality and (o[metric]['costUsd'] < cost or o['quality']['displayed'] > quality)]
            expected.append({'configuration': row['name'], 'id': row['id'], 'effort': row['effort'], 'track': key, 'basis': basis, 'workload': workload, 'cost': cost, 'quality': quality, 'onFrontierAmongPlotted': row['id'] in plotted, 'onFullTrackParetoSet': row['id'] in full, 'dominatedBy': dominated, 'source': f'data/scores.json#{LOC[key]}.rows[id={row["id"]}]' + ('; whatIf.common.go' if whatif else ''), 'kind': 'what-if' if whatif else 'published'})
        require(comparison['pareto'].get(chart) == clean(expected), f'{chart}: chart points mismatch')
        errors.extend(check_pareto(comparison['pareto'].get(chart, [])))
    return errors


def main():
    read = lambda p: json.loads(p.read_text())
    comparison = read(Path(__file__).with_name('comparison.json'))
    scores = read(ROOT / 'data/scores.json')
    frozen = {key: read(ROOT / 'data' / ('v3_frozen' + ('' if key == 'main' else '_' + key) + '.json')) for key in LOC}
    errors = check(comparison, scores, frozen)
    if errors:
        print('\n'.join(errors))
        return 1
    print('Comparison matches score capture, frozen anchors, ranks and Pareto sets.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
