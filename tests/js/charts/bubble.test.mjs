import { test } from 'node:test';
import assert from 'node:assert/strict';
import { buildBubble } from '../../../valuerank/site/assets/js/charts/bubble.js';
import { models, baseOptions } from './_fixtures.mjs';

test('one trace per model with a numeric speed, coloured by tier', () => {
  const spec = buildBubble(models, baseOptions);
  assert.deepEqual(spec.traces.map((t) => t.name), ['alpha', 'beta', 'delta']);
  assert.equal(spec.traces[0].marker.color, '#a3e635');
  assert.equal(spec.traces[1].marker.color, '#fb923c');
  assert.deepEqual(spec.traces[0].x, [100], 'fastest model sits at 100');
  assert.deepEqual(spec.traces[1].x, [0]);
  assert.deepEqual(spec.traces[0].y, [74.6]);
  assert.match(spec.traces[0].hovertemplate, /86\.0 tok\/s/);
  assert.match(spec.traces[0].hovertemplate, /Plan cost: 80\.0/);
  assert.equal(spec.traces[0].showlegend, false);
});

test('bubble size grows with how expensive the model is', () => {
  const spec = buildBubble(models, baseOptions);
  const size = Object.fromEntries(spec.traces.map((t) => [t.name, t.marker.size]));
  assert.ok(size.delta > size.alpha, 'delta has the worst plan cost score');
  assert.ok(size.alpha > size.beta);
  assert.equal(size.delta, 40);
  const api = Object.fromEntries(buildBubble(models, { ...baseOptions, basis: 'api' }).traces.map((t) => [t.name, t.marker.size]));
  assert.ok(api.beta > api.alpha);
});

test('identical speeds do not divide by zero; axis title carries the range', () => {
  const same = buildBubble([{ ...models[0], speed: 50 }, { ...models[1], speed: 50 }], baseOptions);
  assert.deepEqual(same.traces.map((t) => t.x[0]), [0, 0]);
  const spec = buildBubble(models, baseOptions);
  assert.match(spec.layout.xaxis.title.text, /40\.0–86\.0 tok\/s/);
  assert.equal(spec.layout.shapes.length, 2);
  assert.ok(spec.layout.annotations.some((a) => /sweet spot/.test(a.text)));
});

test('labels keep the quadrant annotations as the base layer', () => {
  const spec = buildBubble(models, baseOptions);
  assert.equal(spec.labels.points.length, 3);
  assert.equal(spec.labels.base, spec.layout.annotations);
  assert.equal(spec.labels.options.markerRadius, 24);
  assert.match(spec.label, /3 models/);
  assert.match(spec.summary, /Fastest: alpha/);
});

test('empty state when no model has a speed', () => {
  assert.match(buildBubble([models[2], models[4]], baseOptions).empty, /No numeric speed/);
  assert.match(buildBubble(undefined, undefined).empty, /No numeric speed/);
});

test('the fastest model is found wherever it sits and free models do not break scaling', () => {
  const reversed = buildBubble([models[3], models[0]], baseOptions);
  assert.match(reversed.summary, /Fastest: alpha/);
  const free = buildBubble([{ ...models[0], costDims: { plan: 100 } }, { ...models[1], costDims: { plan: 100 } }], baseOptions);
  assert.deepEqual(free.traces.map((t) => t.marker.size), [10, 10]);
});
