import { test } from 'node:test';
import assert from 'node:assert/strict';
import { buildDisplacement } from '../../../valuerank/site/assets/js/charts/displacement.js';
import { models, baseOptions } from './_fixtures.mjs';

test('one bar per ranked model, sign-coded colour and text', () => {
  const spec = buildDisplacement(models, baseOptions);
  const [trace] = spec.traces;
  const byLabel = Object.fromEntries(trace.y.map((label, i) => [label, { d: trace.x[i], color: trace.marker.color[i], text: trace.text[i] }]));
  assert.equal(trace.y.length, 4);
  assert.deepEqual(byLabel.alpha, { d: 0, color: '#64748b', text: '0' });
  assert.deepEqual(byLabel.beta, { d: 0, color: '#64748b', text: '0' });
  assert.deepEqual(byLabel.delta, { d: -1, color: '#ef4444', text: '-1' });
  const api = buildDisplacement(models, { ...baseOptions, basis: 'api' });
  const alpha = api.traces[0].y.indexOf('alpha');
  assert.equal(api.traces[0].x[alpha], 1);
  assert.equal(api.traces[0].marker.color[alpha], '#22c55e');
  assert.equal(api.traces[0].text[alpha], '+1');
  assert.match(api.traces[0].hovertemplate[alpha], /Cost bonus: rises 1 place/);
});

test('hover wording covers a penalty, no change, and the zero line shape spans the bars', () => {
  const spec = buildDisplacement(models, baseOptions);
  const hover = spec.traces[0].hovertemplate;
  const idx = spec.traces[0].y.indexOf('delta');
  assert.match(hover[idx], /Cost penalty: falls 1 place/);
  assert.match(hover[spec.traces[0].y.indexOf('gamma')], /No change/);
  assert.equal(spec.layout.shapes[0].y1, 3.5);
  assert.match(buildDisplacement([{ ...models[3], rank: { plan: 1 }, qualityRank: 4 }], baseOptions).traces[0].hovertemplate[0], /rises 3 places/);
});

test('x range always includes the zero line and every displacement', () => {
  const wide = [{ ...models[0], qualityRank: 15, rank: { plan: 1 } }, { ...models[1], qualityRank: 1, rank: { plan: 12 } }];
  const range = buildDisplacement(wide, baseOptions).layout.xaxis.range;
  assert.ok(range[0] <= -11 && range[1] >= 14);
  assert.deepEqual(buildDisplacement(models, baseOptions).layout.xaxis.range, [-3, 3]);
});

test('summary and empty state', () => {
  const spec = buildDisplacement(models, { ...baseOptions, basis: 'api' });
  assert.match(spec.summary, /lifts 1 and lowers 1/);
  assert.match(spec.label, /4 models/);
  assert.match(buildDisplacement([models[4]], baseOptions).empty, /No ranked models/);
  assert.match(buildDisplacement(undefined, undefined).empty, /No ranked models/);
});
