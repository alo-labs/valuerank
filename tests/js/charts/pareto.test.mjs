import { test } from 'node:test';
import assert from 'node:assert/strict';
import { buildPareto } from '../../../valuerank/site/assets/js/charts/pareto.js';
import { models, baseOptions } from './_fixtures.mjs';

const byName = (spec, name) => spec.traces.find((t) => t.name === name);

test('plan basis marks only plan-frontier models with the frontier marker', () => {
  const spec = buildPareto(models, baseOptions);
  const frontier = byName(spec, 'Pareto frontier');
  assert.deepEqual(frontier.x, [80]);
  assert.deepEqual(frontier.y, [74.6]);
  assert.equal(frontier.marker.color, '#10b981');
  assert.equal(frontier.marker.size, 14);
  assert.equal(frontier.marker.line.color, '#ecfdf5');
  const dominated = byName(spec, 'Dominated');
  assert.deepEqual(dominated.x.sort((a, b) => a - b), [20, 50, 90]);
  assert.equal(dominated.marker.color.length, 3);
  assert.ok(dominated.marker.color.includes('#64748b'), 'unknown developers fall back');
  assert.equal(spec.traces.length, 3);
  assert.equal(byName(spec, 'frontier-curve').showlegend, false);
});

test('api basis uses the api cost score and flags', () => {
  const spec = buildPareto(models, { ...baseOptions, basis: 'api', dark: true });
  const frontier = byName(spec, 'Pareto frontier');
  assert.deepEqual(frontier.x, [40, 73.3], 'frontier line is ordered by cost score');
  assert.equal(frontier.marker.line.color, '#064e3b');
  assert.match(spec.layout.xaxis.title.text, /API cost/);
  assert.match(spec.layout.title.text, /API cost/);
  assert.match(frontier.hovertemplate, /API cost/);
});

test('axes, hover data and label points', () => {
  const spec = buildPareto(models, baseOptions);
  assert.deepEqual(spec.layout.xaxis.range, [105, 0]); // cheaper on the left, as on AA charts
  assert.deepEqual(spec.layout.yaxis.range, [42, 88]);
  const frontier = byName(spec, 'Pareto frontier');
  assert.match(frontier.customdata[0][2], /per basket run/);
  assert.match(frontier.hovertemplate, /<extra>Frontier<\/extra>/);
  assert.equal(spec.labels.points.length, 4);
  assert.deepEqual(spec.labels.points.filter((p) => p.frontier).map((p) => p.label), ['alpha']);
  assert.equal(spec.labels.options.markerRadius, 11);
});

test('summary and aria label state what is plotted', () => {
  const spec = buildPareto(models, baseOptions);
  assert.match(spec.label, /4 models/);
  assert.match(spec.label, /Plan ranking/);
  assert.match(spec.summary, /Pareto frontier: alpha/);
  assert.match(buildPareto(models.slice(0, 2), { ...baseOptions, basis: 'api' }).summary, /beta, alpha/);
});

test('without plottable models the chart reports an empty state', () => {
  const spec = buildPareto([models[4]], baseOptions);
  assert.match(spec.empty, /No models/);
  assert.equal(buildPareto(undefined, undefined).traces.length, 0);
  const noFrontier = buildPareto([models[2]], baseOptions);
  assert.match(noFrontier.summary, /No model is on the frontier/);
});
