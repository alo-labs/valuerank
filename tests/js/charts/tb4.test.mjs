import { test } from 'node:test';
import assert from 'node:assert/strict';
import { buildTb4 } from '../../../valuerank/site/assets/js/charts/tb4.js';
import { tb4Rows } from './_fixtures.mjs';

test('log cost axis with frontier rows marked and a frontier line', () => {
  const spec = buildTb4(tb4Rows, {});
  assert.equal(spec.layout.xaxis.type, 'log');
  assert.match(spec.layout.xaxis.title.text, /log scale/);
  const [official, frontier, curve] = spec.traces;
  assert.deepEqual(frontier.x, [1000, 3300]);
  assert.deepEqual(frontier.y, [40, 58.2]);
  assert.equal(frontier.marker.size, 15);
  assert.equal(frontier.marker.color, '#10b981');
  assert.deepEqual(official.x, [1500], 'dominated and non-positive costs are not plotted as rows');
  assert.equal(official.name, 'Official rows');
  assert.deepEqual(curve.x, frontier.x);
  assert.equal(curve.line.shape, 'spline');
});

test('hover carries agent, uncertainty, tokens and rank; labels use the base model', () => {
  const spec = buildTb4(tb4Rows, { dark: true });
  const frontier = spec.traces[1];
  assert.deepEqual(frontier.customdata[1], ['A', 'Codex', 58.2, 2.8, '1.5B', '1', 'A (max)']);
  assert.match(frontier.hovertemplate, /Resolution: %\{customdata\[2\]:\.1f\}% ± /);
  assert.match(frontier.hovertemplate, /<extra>Frontier<\/extra>/);
  assert.equal(frontier.marker.line.color, '#064e3b');
  assert.deepEqual(spec.labels.points.map((p) => p.label), ['A', 'B', 'C']);
  assert.deepEqual(spec.labels.points.map((p) => p.frontier), [true, true, false]);
  assert.equal(spec.layout.yaxis.ticksuffix, '%');
  assert.deepEqual(spec.layout.yaxis.range, [0, 64]);
});

test('y range stretches above the best row; summary and empty state', () => {
  const high = buildTb4([{ ...tb4Rows[0], resolutionRatePct: 80 }], {});
  assert.deepEqual(high.layout.yaxis.range, [0, 88]);
  const spec = buildTb4(tb4Rows, {});
  assert.match(spec.label, /3 official rows/);
  assert.match(spec.summary, /B, A/);
  assert.match(buildTb4([], {}).empty, /No Terminal-Bench/);
  assert.match(buildTb4(undefined, undefined).empty, /No Terminal-Bench/);
});

test('rows without a positive cost or a rate are skipped', () => {
  const rows = [...tb4Rows, { ...tb4Rows[0], model: 'X', costUsd: null }, { ...tb4Rows[0], model: 'Y', resolutionRatePct: null }];
  assert.equal(buildTb4(rows, {}).labels.points.length, 3);
});
