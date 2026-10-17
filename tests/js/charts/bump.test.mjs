import { test } from 'node:test';
import assert from 'node:assert/strict';
import { buildBump, rankHistory } from '../../../valuerank/site/assets/js/charts/bump.js';
import { models, changelog, baseOptions } from './_fixtures.mjs';

const input = { versions: changelog.versions, models };

test('history is oldest first and uses only recorded ranks', () => {
  const { labels, ranks } = rankHistory(input.versions, models, 'plan');
  assert.deepEqual(labels, ['v1.0', 'v1.1', 'v1.2']);
  assert.deepEqual(ranks.get('alpha'), [2, 1, 2]);
  assert.deepEqual(ranks.get('delta'), [3, null, 5], 'no inference between records');
});

test('a model absent from an earlier version breaks its line there', () => {
  const spec = buildBump(input, baseOptions);
  const beta = spec.traces.find((t) => t.name === 'beta');
  assert.deepEqual(beta.x, ['v1.0', 'v1.1', 'v1.2']);
  assert.deepEqual(beta.y, [null, null, 1]);
  assert.equal(beta.connectgaps, false);
  const alpha = spec.traces.find((t) => t.name === 'alpha');
  assert.deepEqual(alpha.y, [2, 1, 2]);
});

test('current ranks of the active basis close the series and label the line ends', () => {
  const plan = buildBump(input, baseOptions);
  const api = buildBump(input, { ...baseOptions, basis: 'api' });
  assert.deepEqual(plan.traces.find((t) => t.name === 'alpha').y.at(-1), 2);
  assert.deepEqual(api.traces.find((t) => t.name === 'alpha').y.at(-1), 1);
  assert.ok(plan.layout.annotations.some((a) => a.text === 'alpha' && a.y === 2 && a.xref === 'paper'));
  assert.deepEqual(plan.layout.yaxis.range, [5.5, 0.5]);
  assert.equal(plan.layout.yaxis.tickvals.length, 5);
  assert.equal(plan.layout.xaxis.categoryarray.length, 3);
});

test('styling follows the developer colour and top-three emphasis', () => {
  const spec = buildBump(input, baseOptions);
  const beta = spec.traces.find((t) => t.name === 'beta');
  assert.equal(beta.line.color, '#d4a574');
  assert.equal(beta.line.width, 2.5);
  const delta = spec.traces.find((t) => t.name === 'delta');
  assert.equal(delta.line.width, 1.5);
  assert.equal(delta.opacity, 0.65);
  assert.equal(delta.marker.size, 7);
});

test('a single version and an empty changelog are handled', () => {
  const one = buildBump({ versions: [{ version: 'v9', rankChanges: [] }], models }, baseOptions);
  assert.equal(one.traces.length, 4);
  assert.match(buildBump({ versions: [], models }, baseOptions).empty, /No version history/);
  assert.match(buildBump(undefined, undefined).empty, /No version history/);
  assert.match(one.summary, /v9/);
  assert.match(buildBump(input, baseOptions).label, /3 versions/);
});

test('the oldest version may carry a change, a missing rankChanges list is tolerated, and unranked history has no top-3 emphasis', () => {
  const versions = [
    { version: 'v2' },
    { version: 'v1', rankChanges: [{ slug: 'alpha', from: 4, to: 3 }, { slug: 'delta', from: 2, to: 2 }] },
  ];
  const { ranks } = rankHistory(versions, [], 'plan');
  assert.deepEqual(ranks.get('alpha'), [3, null]);
  const second = [{ version: 'v2', rankChanges: [{ slug: 'alpha', from: 4, to: 3 }] }, { version: 'v1' }];
  assert.deepEqual(rankHistory(second, [], 'plan').ranks.get('alpha'), [4, 3]);
  const retired = { ...models[0], rank: { plan: null, api: null } };
  const spec = buildBump({ versions: second, models: [retired] }, baseOptions);
  assert.equal(spec.traces[0].line.width, 1.5);
  assert.equal(spec.layout.annotations.length, 0);
});
