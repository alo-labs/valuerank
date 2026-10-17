import { test } from 'node:test';
import assert from 'node:assert/strict';
import { buildDecomposition, contributions } from '../../../valuerank/site/assets/js/charts/decomposition.js';
import { models, dimensions, baseOptions } from './_fixtures.mjs';

test('contributions renormalise over the available dimensions and sum to the weighted mean', () => {
  const alpha = models[0];
  const c = contributions(alpha, dimensions, 'plan', undefined);
  assert.ok(Math.abs(c.cost - 20) < 1e-9, 'cost 80 x 20 / 80');
  assert.ok(Math.abs(c.code - ((100 * 40 + 93.3 * 20) / 80)) < 1e-9);
  assert.equal(c.intel, 0, 'missing hle contributes nothing');
  const full = contributions(models[1], dimensions, 'plan');
  assert.ok(Math.abs(Object.values(full).reduce((a, b) => a + b, 0) - (90 * 20 + 90 * 40 + 80 * 20 + 60 * 20) / 100) < 1e-9);
});

test('cost weight override rescales the other dimensions', () => {
  const heavy = contributions(models[1], dimensions, 'plan', 50);
  const light = contributions(models[1], dimensions, 'plan', 10);
  assert.ok(heavy.cost > light.cost);
  const same = contributions(models[1], dimensions, 'plan', 20);
  assert.deepEqual(same, contributions(models[1], dimensions, 'plan'));
  assert.deepEqual(contributions({ dims: {}, costDims: {} }, dimensions, 'api'), { cost: 0, code: 0, intel: 0 });
});

test('one stacked horizontal bar trace per category, models sorted by overall', () => {
  const spec = buildDecomposition(models, baseOptions);
  assert.equal(spec.layout.barmode, 'stack');
  assert.deepEqual(spec.traces.map((t) => t.name), ['Cost', 'Code/Agentic', 'Intelligence']);
  assert.deepEqual(spec.traces[0].y, ['delta', 'gamma', 'alpha', 'beta']);
  assert.ok(spec.traces.every((t) => t.type === 'bar' && t.orientation === 'h'));
  assert.equal(spec.traces[0].marker.color, '#22c55e');
  assert.match(spec.layout.title.text, /Plan cost/);
  assert.match(spec.label, /4 models/);
  assert.match(spec.summary, /beta leads/);
});

test('unknown categories fall back to key and neutral colour; empty input is reported', () => {
  const odd = [{ key: 'x', label: 'X', category: 'mystery', weightPct: 10 }];
  const spec = buildDecomposition([{ ...models[0], dims: { x: 10 } }], { basis: 'api', dimensions: odd, categories: {} });
  assert.equal(spec.traces[0].name, 'mystery');
  assert.equal(spec.traces[0].marker.color, '#64748b');
  assert.match(buildDecomposition([models[4]], baseOptions).empty, /No ranked models/);
  assert.match(buildDecomposition(undefined, undefined).empty, /No ranked models/);
});

test('models without dims, and a cost weight without a cost dimension, are tolerated', () => {
  const noCost = [{ key: 'x', label: 'X', category: 'code', weightPct: 50 }];
  assert.deepEqual(contributions({ costDims: {} }, noCost, 'plan', 10), { code: 0 });
  assert.ok(Math.abs(contributions({ dims: { x: 40 } }, noCost, 'plan', 10).code - 40) < 1e-9);
});
