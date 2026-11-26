"""Regression tests for independent comparison checks."""
import copy
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location('checker', Path(__file__).with_name('check_comparison.py'))
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)



def test_scoring_helpers_loaded_from_cleaned_temporary_copy():
    for helper in (checker.cost_score, checker.value_score, checker.pareto_set):
        path = Path(helper.__code__.co_filename)
        assert any(part.startswith('valuerank-check-') for part in path.parts)
        assert not path.exists()


def fixture():
    row = {'id': 'model', 'name': 'Model (high)', 'effort': 'high', 'api': {'value': 50}}
    plan = {'id': 'model@plan', 'configurationId': 'model', 'value': 55}
    track = {'rows': [row], 'planRows': [plan]}
    record = {'source': 'scores.v3', 'kind': 'published', 'row': copy.deepcopy(row), 'planRows': [copy.deepcopy(plan)]}
    return record, track


def test_track_rejects_changed_published_value_effort_missing_plan_and_source():
    record, track = fixture()
    assert checker.check_track(record, track, 'Model', 'high', 'scores.v3') == []
    for change in ('value', 'effort', 'plan', 'source'):
        candidate = copy.deepcopy(record)
        if change == 'value': candidate['row']['api']['value'] = 51
        if change == 'effort': candidate['row']['effort'] = 'max'
        if change == 'plan': candidate['planRows'] = []
        if change == 'source': candidate['source'] = 'scores.v3Tracks.common'
        assert checker.check_track(candidate, track, 'Model', 'high', 'scores.v3'), change


def test_pareto_rejects_incorrect_frontier_flag():
    points = [{'configuration': 'A', 'cost': 10, 'quality': 50, 'onFrontierAmongPlotted': True},
              {'configuration': 'B', 'cost': 20, 'quality': 40, 'onFrontierAmongPlotted': False}]
    assert checker.check_pareto(points) == []
    points[1]['onFrontierAmongPlotted'] = True
    assert checker.check_pareto(points)



def test_real_capture_rejects_missing_configuration_and_altered_what_if():
    import json
    read = lambda path: json.loads(path.read_text())
    comparison = read(Path(__file__).with_name('comparison.json'))
    scores = read(checker.ROOT / 'data/scores.json')
    frozen = {key: read(checker.ROOT / 'data' / ('v3_frozen' + ('' if key == 'main' else '_' + key) + '.json')) for key in checker.LOC}
    assert checker.check(comparison, scores, frozen) == []
    altered = copy.deepcopy(comparison)
    del altered['configurations'][0]['tracks']['main']
    assert any('missing' in error for error in checker.check(altered, scores, frozen))
    altered = copy.deepcopy(comparison)
    altered['whatIf']['main']['go']['value'] += 1
    assert any('go what-if mismatch' in error for error in checker.check(altered, scores, frozen))
