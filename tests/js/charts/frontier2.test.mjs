import { test } from 'node:test';
import assert from 'node:assert/strict';
import { buildFrontier2 } from '../../../valuerank/site/assets/js/charts/frontier2.js';
import { models, baseOptions } from './_fixtures.mjs';

test('each ranked model is drawn at its API and Plan position with a connector', () => {
  const spec = buildFrontier2(models, baseOptions);
  const connectors = spec.traces.filter((t) => t.mode === 'lines');
  assert.equal(connectors.length, 4);
  const alpha = connectors.find((t) => t.x[0] === 73.3);
  assert.deepEqual(alpha.x, [73.3, 80]);
  assert.deepEqual(alpha.y, [74.3, 75.7]);
  assert.equal(alpha.hoverinfo, 'skip');
  const api = spec.traces.find((t) => t.name === 'API ranking');
  const plan = spec.traces.find((t) => t.name === 'Plan ranking');
  assert.equal(api.marker.symbol, 'circle');
  assert.equal(plan.marker.symbol, 'diamond');
  assert.deepEqual(api.x, [73.3, 40, 55, 90]);
  assert.deepEqual(plan.y, [75.7, 78, 61, 52]);
  assert.equal(api.marker.color[0], '#10a37f');
});

test('connector colour is sign-coded by the plan minus api change', () => {
  const spec = buildFrontier2(models, baseOptions);
  const colors = spec.traces.filter((t) => t.mode === 'lines').map((t) => t.line.color);
  assert.ok(colors.includes('rgba(34,197,94,0.4)'), 'gain');
  assert.ok(colors.includes('rgba(239,68,68,0.4)'), 'loss');
});

test('hover shows both overalls and the plan change; labels sit at the plan point', () => {
  const spec = buildFrontier2(models, baseOptions);
  const plan = spec.traces.find((t) => t.name === 'Plan ranking');
  assert.match(plan.hovertemplate[0], /Change: \+1\.4/);
  assert.equal(spec.labels.points.length, 4);
  assert.deepEqual(spec.labels.points[0], { id: 'alpha', label: 'alpha', x: 80, y: 75.7 });
  assert.equal(spec.labels.options.markerRadius, 12);
  assert.deepEqual(spec.layout.xaxis.range, [0, 105]);
  assert.match(spec.label, /4 models/);
  assert.match(spec.summary, /higher than API score for 3 models and lower for 1/);
});

test('models missing either basis are left out; empty state otherwise', () => {
  const half = { ...models[0], overall: { api: 70, plan: null } };
  assert.equal(buildFrontier2([half, models[1]], baseOptions).labels.points.length, 1);
  assert.match(buildFrontier2([half], baseOptions).empty, /No models/);
  assert.match(buildFrontier2(undefined, undefined).empty, /No models/);
});
