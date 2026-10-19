import test from 'node:test';
import assert from 'node:assert/strict';
import { compareRows } from '../../../valuerank/site/assets/js/compare.js';
import { dimensions, models } from './fixture.mjs';

test('compareRows returns a row per dimension with one value per selected model, in slug order', () => {
  const out = compareRows(models, ['gamma', 'alpha'], dimensions, 'api');
  assert.deepEqual(out.models.map((m) => m.slug), ['gamma', 'alpha']);
  assert.deepEqual(out.rows.map((r) => r.key), ['costComposite', 'a', 'b']);
  const a = out.rows.find((r) => r.key === 'a');
  assert.deepEqual(a.values, [50, 80]);
  assert.equal(a.label, 'Alpha bench');
  assert.deepEqual(a.best, [1]);
});

test('cost row reads the chosen basis and best marks every tied maximum', () => {
  const cost = (basis) => compareRows(models, ['alpha', 'gamma'], dimensions, basis).rows[0];
  assert.deepEqual(cost('api').values, [50, 90]);
  assert.deepEqual(cost('api').best, [1]);
  assert.deepEqual(cost('plan').values, [70, 80]);
  const tie = compareRows([models[0], { ...models[0], slug: 'alpha2' }], ['alpha', 'alpha2'], dimensions, 'api');
  assert.deepEqual(tie.rows[1].best, [0, 1]);
});

test('missing values are null and never best; an all-missing row has no best', () => {
  const out = compareRows(models, ['beta', 'eps'], dimensions, 'api');
  const b = out.rows.find((r) => r.key === 'b');
  assert.deepEqual(b.values, [null, null]);
  assert.deepEqual(b.best, []);
  const a = out.rows.find((r) => r.key === 'a');
  assert.deepEqual(a.values, [84, null]);
  assert.deepEqual(a.best, [0]);
});

test('compare caps at four models, skips unknown slugs, and defaults to the plan basis', () => {
  const many = Array.from({ length: 6 }, (_, i) => ({ ...models[0], slug: `m${i}`, name: `M${i}` }));
  const out = compareRows(many, ['m0', 'nope', 'm1', 'm2', 'm3', 'm4', 'm5'], dimensions);
  assert.deepEqual(out.models.map((m) => m.slug), ['m0', 'm1', 'm2', 'm3']);
  assert.deepEqual(out.rows[0].values, [70, 70, 70, 70]);
});

test('bestIndexes returns every maximum and ignores nulls', async () => {
  const { bestIndexes } = await import('../../../valuerank/site/assets/js/compare.js');
  assert.deepEqual(bestIndexes([1, null, 3, 3]), [2, 3]);
  assert.deepEqual(bestIndexes([null, null]), []);
});
