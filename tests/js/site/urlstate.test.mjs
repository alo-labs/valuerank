import test from 'node:test';
import assert from 'node:assert/strict';
import { parseState, serializeState } from '../../../valuerank/site/assets/js/urlstate.js';

const defaults = {
  basis: 'plan', w: 18.9394, sort: 'rank', dir: 'asc', cols: ['rank', 'name'],
  provider: [], grade: [], route: 'all', cov: 0, q: '', compare: [], chart: '',
};

test('empty search yields the defaults and does not alias them', () => {
  const s = parseState('', defaults);
  assert.deepEqual(s, defaults);
  s.cols.push('x');
  assert.deepEqual(defaults.cols, ['rank', 'name']);
});

test('serializeState omits everything at its default', () => {
  assert.equal(serializeState({ ...defaults }, defaults), '');
});

test('serializeState writes only changed keys with a leading ? and comma lists', () => {
  const q = serializeState({ ...defaults, basis: 'api', provider: ['Open AI', 'xAI'], q: 'a&b' }, defaults);
  assert.equal(q, '?basis=api&provider=Open%20AI,xAI&q=a%26b');
});

test('state round-trips through serialize and parse', () => {
  const state = {
    basis: 'api', w: 40.5, sort: 'overall', dir: 'desc', cols: ['rank', 'cost'],
    provider: ['Anthropic'], grade: ['measured', 'claim'], route: 'fallback', cov: 75.5,
    q: 'claude opus', compare: ['a', 'b', 'c'], chart: 'pareto',
  };
  assert.deepEqual(parseState(serializeState(state, defaults), defaults), state);
});

test('w is clamped to [0,100], rounded to one decimal, and invalid values fall back', () => {
  assert.equal(parseState('?w=150', defaults).w, 100);
  assert.equal(parseState('?w=-5', defaults).w, 0);
  assert.equal(parseState('?w=33.349', defaults).w, 33.3);
  assert.equal(parseState('?w=abc', defaults).w, defaults.w);
  assert.equal(parseState('?w=', defaults).w, defaults.w);
});

test('a w equal to the default at one decimal keeps the exact default and is omitted', () => {
  assert.equal(parseState('?w=18.9', defaults).w, 18.9394);
  assert.equal(serializeState({ ...defaults, w: 18.9 }, defaults), '');
});

test('cov is clamped to [0,100]; invalid falls back', () => {
  assert.equal(parseState('?cov=250', defaults).cov, 100);
  assert.equal(parseState('?cov=-1', defaults).cov, 0);
  assert.equal(parseState('?cov=x', defaults).cov, 0);
});

test('enum values are validated and invalid ones fall back to defaults', () => {
  const s = parseState('?basis=zzz&dir=up&route=nope&sort=bad%20key&chart=%3Cscript%3E', defaults);
  assert.equal(s.basis, 'plan');
  assert.equal(s.dir, 'asc');
  assert.equal(s.route, 'all');
  assert.equal(s.sort, 'rank');
  assert.equal(s.chart, '');
  const ok = parseState('?basis=api&dir=desc&route=eligible&sort=deepswePassAt1&chart=pareto', defaults);
  assert.deepEqual([ok.basis, ok.dir, ok.route, ok.sort, ok.chart], ['api', 'desc', 'eligible', 'deepswePassAt1', 'pareto']);
});

test('grade list keeps only known grades; cols keeps only key-shaped tokens; empties fall back', () => {
  assert.deepEqual(parseState('?grade=measured,bogus,claim', defaults).grade, ['measured', 'claim']);
  assert.deepEqual(parseState('?grade=bogus', defaults).grade, []);
  assert.deepEqual(parseState('?cols=rank,,bad key,cost', defaults).cols, ['rank', 'cost']);
  assert.deepEqual(parseState('?cols=', defaults).cols, defaults.cols);
  assert.deepEqual(parseState('?provider=%20,Meta', defaults).provider, ['Meta']);
});

test('compare is limited to 2-4 unique slugs', () => {
  assert.deepEqual(parseState('?compare=a,b,c,d,e,f', defaults).compare, ['a', 'b', 'c', 'd']);
  assert.deepEqual(parseState('?compare=a', defaults).compare, []);
  assert.deepEqual(parseState('?compare=a,a', defaults).compare, []);
  assert.deepEqual(parseState('?compare=a,b!', defaults).compare, []);
  assert.deepEqual(parseState('?compare=a,b', defaults).compare, ['a', 'b']);
});

test('q is trimmed and capped at 100 characters', () => {
  assert.equal(parseState('?q=%20%20hi%20', defaults).q, 'hi');
  assert.equal(parseState('?q=' + 'x'.repeat(300), defaults).q.length, 100);
});

test('unknown keys are ignored and accepted search without ? works', () => {
  const s = parseState('utm=1&basis=api&evil=<x>', defaults);
  assert.equal(s.basis, 'api');
  assert.equal(Object.keys(s).length, Object.keys(defaults).length);
});

test('serialization drops commas from list items so they cannot split', () => {
  const q = serializeState({ ...defaults, provider: ['A,B'] }, defaults);
  assert.equal(q, '?provider=AB');
});

test('serializing an empty list that differs from a non-empty default writes an empty value that parses back as default', () => {
  const d = { ...defaults, cols: ['rank'] };
  assert.equal(serializeState({ ...d, cols: [] }, d), '');
});

test('keys absent from the defaults are treated as having an empty default', () => {
  assert.deepEqual(parseState('?basis=api', {}).basis, 'api');
  assert.equal(serializeState({ basis: 'api' }, {}), '?basis=api');
});

test('a single selected comparison model is not written to the URL', () => {
  assert.equal(serializeState({ ...defaults, compare: ['a'] }, defaults), '');
  assert.equal(serializeState({ ...defaults, compare: ['a', 'b'] }, defaults), '?compare=a,b');
});
