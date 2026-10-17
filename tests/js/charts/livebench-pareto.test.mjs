import { test } from 'node:test';
import assert from 'node:assert/strict';
import { buildLivebenchPareto } from '../../../valuerank/site/assets/js/charts/livebench-pareto.js';
import { livebench } from './_fixtures.mjs';

test('splits rows into dominated and frontier, uses a log cost axis', () => {
  const spec = buildLivebenchPareto(livebench, {});
  const [dominated, frontier, curve] = spec.traces;
  assert.deepEqual(dominated.y, [60]);
  assert.deepEqual(frontier.x, [0.05, 2], 'frontier sorted by cost');
  assert.equal(frontier.marker.color, '#10b981');
  assert.equal(curve.mode, 'lines');
  assert.equal(spec.layout.xaxis.type, 'log');
  assert.match(spec.layout.xaxis.title.text, /log scale/);
  assert.deepEqual(spec.layout.yaxis.range, [58, 82]);
  assert.match(frontier.hovertemplate, /<extra>Frontier<\/extra>/);
  assert.equal(frontier.customdata[0][0], 'Model A');
});

test('rows without cost or score are ignored and labelled by name', () => {
  const spec = buildLivebenchPareto(livebench, { dark: true });
  assert.equal(spec.labels.points.length, 3);
  assert.deepEqual(spec.labels.points.map((p) => p.label), ['Model A', 'Model B', 'Model C']);
  assert.equal(spec.traces[1].marker.line.color, '#064e3b');
  assert.match(spec.label, /3 models/);
  assert.match(spec.summary, /Model A/);
});

test('empty input reports an empty state', () => {
  assert.match(buildLivebenchPareto([], undefined).empty, /No matched LiveBench rows/);
  assert.match(buildLivebenchPareto(undefined, {}).empty, /No matched LiveBench rows/);
});
