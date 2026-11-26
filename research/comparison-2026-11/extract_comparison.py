"""Extract exact published rows and compute a labelled OpenCode what-if.

The scoring and Pareto modules are copied to a temporary directory before import.
"""
import copy
import json
import math
from pathlib import Path
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
REQUESTED = [('DeepSeek V4.1 Flash 1017', 'max'), ('Claude Haiku 5.5', 'high'),
             ('Claude Haiku 5.5', 'xhigh'), ('Claude Haiku 5.5', 'max'),
             ('GPT-6 Luna', 'max'), ('GPT-6.1 Terra', 'low'), ('GPT-6.1 Terra', 'medium'),
             ('Claude Sonnet 5.5', 'medium'), ('Claude Opus 5.5', 'low')]
DEEPSEEK = 'deepseek-v4-1-flash-1017'


def find_row(rows, name, effort):
    matches = [r for r in rows if r.get('effort') == effort and
               (r.get('name') == name or r.get('name') == f'{name} ({effort})')]
    if len(matches) > 1:
        raise ValueError(f'ambiguous configuration: {name} {effort}')
    return matches[0] if matches else None


def clean(value):
    # The input file contains NaN/Infinity, which are not valid JSON values.
    if isinstance(value, float) and not math.isfinite(value):
        return None
    if isinstance(value, list):
        return [clean(x) for x in value]
    if isinstance(value, dict):
        return {k: clean(v) for k, v in value.items()}
    return value


def build():
    with tempfile.TemporaryDirectory(prefix='valuerank-comparison-') as tmp:
        shutil.copytree(ROOT / 'valuerank', Path(tmp) / 'valuerank', ignore=shutil.ignore_patterns('__pycache__'))
        sys.path.insert(0, tmp)
        try:
            from valuerank.anchors import cost_score, value_score
            from valuerank.value_v3 import _anchors_for, competition_ranks
            from valuerank.site.viewmodel import pareto_set
            return _build(cost_score, value_score, _anchors_for, competition_ranks, pareto_set)
        finally:
            sys.path.remove(tmp)


def _build(cost_score, value_score, anchors_for, competition_ranks, pareto_set):
    scores = json.loads((ROOT / 'data/scores.json').read_text())
    tracks = {'main': scores['v3'], 'aicd': scores['v3Tracks']['aicd'], 'common': scores['v3Tracks']['common']}
    loc = {'main': 'v3', 'aicd': 'v3Tracks.aicd', 'common': 'v3Tracks.common'}
    output = {'metadata': {'observedAt': scores['observedAt'], 'version': scores['version'],
                           'source': 'data/scores.json', 'kind': 'published',
                           'nonFiniteInput': 'JSON NaN and Infinity are represented as null'},
              'configurations': [], 'diagnostics': {}, 'whatIf': {}, 'pareto': {}}
    for name, effort in REQUESTED:
        entry = {'requested': {'name': name, 'effort': effort}, 'tracks': {}}
        for track_name, track in tracks.items():
            row = find_row(track['rows'], name, effort)
            if row:
                plans = [p for p in track['planRows'] if p['configurationId'] == row['id']]
                entry['tracks'][track_name] = {'source': f"data/scores.json#{loc[track_name]}.rows[id={row['id']}] and planRows[configurationId={row['id']}]", 'kind': 'published', 'row': row, 'planRows': plans}
        output['configurations'].append(entry)
    for track_name, track in tracks.items():
        workload = track['mainWorkload']
        source = f'data/scores.json#{loc[track_name]}'
        output['diagnostics'][track_name] = {'source': source + '.diagnostics.rankSeparability', 'kind': 'published', 'rankSeparability': track['diagnostics']['rankSeparability'], 'mainWorkload': workload}
        frozen_name = 'v3_frozen' + ('' if track_name == 'main' else '_' + track_name) + '.json'
        frozen = json.loads((ROOT / 'data' / frozen_name).read_text())
        anchors = anchors_for(frozen, workload, 'plan')
        deep = next(r for r in track['rows'] if r['id'] == DEEPSEEK)
        eligible = {r['id'] for r in track['rows'] if r['cost']['workload'] == workload}
        plan_values = {p['id']: p['value'] for p in track['planRows'] if p['configurationId'] in eligible and p['configurationId'] != DEEPSEEK}
        variants = {}
        for label, multiple in [('go', 10.0), ('goPlus', 5.0)]:
            cost = deep['api']['costUsd'] / multiple
            score = cost_score(cost, anchors)
            value = value_score(score, deep['quality']['displayed'], 0.25)
            ranks = competition_ranks({**plan_values, DEEPSEEK + '@what-if': value})
            variants[label] = {'multiple': multiple, 'costUsd': cost, 'costScore': score, 'value': value, 'rank': ranks[DEEPSEEK + '@what-if'], 'otherPlanRanks': {k: v for k, v in ranks.items() if k != DEEPSEEK + '@what-if'}}
        output['whatIf'][track_name] = {'source': f'{source}.rows[id={DEEPSEEK}]; data/{frozen_name}#workloads.{workload}.anchors.plan; valuerank/anchors.py#cost_score,value_score; valuerank/value_v3.py#competition_ranks', 'kind': 'what-if', 'go': variants['go'], 'goPlus': variants['goPlus'], 'publishedFallback': deep['planScore'], 'fallbackSource': f'{source}.rows[id={DEEPSEEK}].planScore', 'description': 'Owner-stated mapping to 1017; provider-published usage limit at OpenCode prices, not measured consumption.'}
    def make_pareto(track_name, basis, what_if=False):
        track = tracks[track_name]; workload = track['mainWorkload']
        rows = copy.deepcopy(track['rows'])
        if what_if:
            next(r for r in rows if r['id'] == DEEPSEEK)['planScore']['costUsd'] = output['whatIf'][track_name]['go']['costUsd']
        selected = [r for r in rows if any(find_row([r], name, effort) for name, effort in REQUESTED) and r['cost']['workload'] == workload]
        subset = pareto_set(selected, workload, basis); full = pareto_set(rows, workload, basis)
        key = 'api' if basis == 'api' else 'planScore'
        result = []
        for row in selected:
            cost, quality = row[key]['costUsd'], row['quality']['displayed']
            if cost is None or quality is None:
                continue
            dominated = [other['id'] for other in selected if other['id'] != row['id'] and other[key]['costUsd'] is not None and other['quality']['displayed'] is not None and other[key]['costUsd'] <= cost and other['quality']['displayed'] >= quality and (other[key]['costUsd'] < cost or other['quality']['displayed'] > quality)]
            result.append({'configuration': row['name'], 'id': row['id'], 'effort': row['effort'], 'track': track_name, 'basis': basis, 'workload': workload, 'cost': cost, 'quality': quality, 'onFrontierAmongPlotted': row['id'] in subset, 'onFullTrackParetoSet': row['id'] in full, 'dominatedBy': dominated, 'source': f'data/scores.json#{loc[track_name]}.rows[id={row["id"]}]' + ('; whatIf.common.go' if what_if else ''), 'kind': 'what-if' if what_if else 'published'})
        return result
    for key, name, basis, hypothetical in [('apiCommon','common','api',False), ('planCommonPublished','common','plan',False), ('planCommonWhatIf','common','plan',True), ('apiMain','main','api',False), ('apiAicd','aicd','api',False)]:
        output['pareto'][key] = make_pareto(name, basis, hypothetical)
    return clean(output)


if __name__ == '__main__':
    destination = Path(__file__).with_name('comparison.json')
    destination.write_text(json.dumps(build(), indent=2, allow_nan=False) + '\n')
    print(destination)
