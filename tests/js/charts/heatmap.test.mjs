import { test } from 'node:test';
import assert from 'node:assert/strict';
import { buildHeatmap } from '../../../valuerank/site/assets/js/charts/heatmap.js';
import { models, baseOptions } from './_fixtures.mjs';

test('missing values use the missing colour underlay and a no-data marker', () => {
  const spec = buildHeatmap(models, baseOptions);
  const [underlay, data] = spec.traces;
  assert.equal(underlay.hoverinfo, 'skip');
  assert.deepEqual(underlay.colorscale, [[0, '#e5e7eb'], [1, '#e5e7eb']]);
  assert.ok(underlay.z.flat().every((v) => v === 0));
  const row = data.y.indexOf('alpha');
  const col = data.x.indexOf('HLE');
  assert.equal(data.z[row][col], null);
  assert.equal(data.z[row][data.x.indexOf('DeepSWE')], 100);
  const cell = spec.layout.annotations.find((a) => a.x === 'HLE' && a.y === 'alpha');
  assert.equal(cell.text, '⊘');
  assert.equal(data.customdata[row][col].score, 'Not available');
  assert.equal(data.customdata[row][col].missing, true);
  assert.equal(data.customdata[row][1].missing, false);
});

test('cost column uses the basis score and rows are sorted by overall descending', () => {
  const plan = buildHeatmap(models, baseOptions).traces[1];
  assert.deepEqual(plan.y, ['beta', 'alpha', 'gamma', 'delta']);
  assert.equal(plan.x[0], 'Plan cost');
  assert.equal(plan.z[0][0], 90);
  const api = buildHeatmap(models, { ...baseOptions, basis: 'api' }).traces[1];
  assert.equal(api.x[0], 'API cost');
  assert.equal(api.z[api.y.indexOf('alpha')][0], 73.3);
  assert.deepEqual(api.colorscale[0], [0, '#1e3a8a']);
});

test('category dividers and group labels follow the dimension order', () => {
  const spec = buildHeatmap(models, baseOptions);
  assert.deepEqual(spec.layout.shapes.map((s) => s.x0), [0.5, 2.5]);
  const groups = spec.layout.annotations.filter((a) => a.yref === 'paper').map((a) => a.text);
  assert.deepEqual(groups, ['<b>Cost</b>', '<b>Code/Agentic</b>', '<b>Intelligence</b>']);
  const unknown = buildHeatmap(models.slice(0, 1), { ...baseOptions, categories: {} });
  assert.ok(unknown.layout.annotations.some((a) => a.text === '<b>cost</b>'));
});

test('text colour adapts to the cell value and height is optional', () => {
  const spec = buildHeatmap(models, { ...baseOptions, height: 540 });
  const low = spec.layout.annotations.find((a) => a.x === 'DeepSWE' && a.y === 'delta');
  const high = spec.layout.annotations.find((a) => a.x === 'DeepSWE' && a.y === 'beta');
  assert.equal(low.text, '20');
  assert.match(low.font.color, /255,255,255/);
  assert.match(high.font.color, /0,0,0/);
  assert.equal(spec.layout.height, 540);
  assert.equal(buildHeatmap(models, { ...baseOptions, height: 'x' }).layout.height, undefined);
  assert.equal(buildHeatmap(models, baseOptions).layout.height, undefined);
});

test('summary mentions the matrix size and gaps; empty state', () => {
  const spec = buildHeatmap(models, baseOptions);
  assert.match(spec.label, /4 models/);
  assert.match(spec.summary, /4 dimensions/);
  assert.match(spec.summary, /Cells without data: 1/);
  assert.match(buildHeatmap([models[1]], baseOptions).summary, /every cell has a value/i);
  assert.match(buildHeatmap([], baseOptions).empty, /No ranked models/);
  assert.match(buildHeatmap(undefined, undefined).empty, /No ranked models/);
});

test('full labels and cost weight come from the dimensions when supplied; no dimensions leaves only the cost column', () => {
  const dims = [{ key: 'costComposite', label: 'Cost', fullLabel: 'Cost (selected basis)', category: 'cost', weightPct: 18.94 }, { key: 'bug', label: 'Bug', fullLabel: 'Bug Hunt full', category: 'code', weightPct: 10 }];
  const spec = buildHeatmap(models, { basis: 'plan', dimensions: dims });
  const cd = spec.traces[1].customdata[0];
  assert.equal(cd[0].dim, 'Cost (selected basis)');
  assert.equal(cd[0].weight, '18.94');
  assert.equal(cd[1].dim, 'Bug Hunt full');
  const bare = buildHeatmap(models, { basis: 'plan' });
  assert.deepEqual(bare.traces[1].x, ['Plan cost']);
  assert.equal(bare.traces[1].customdata[0][0].weight, '0.00');
  const weighted = buildHeatmap(models, { basis: 'plan', costWeightPct: 30, dimensions: dims });
  assert.equal(weighted.traces[1].customdata[0][0].weight, '30.00');
});

test('categories without a palette colour use the neutral group colour', () => {
  const spec = buildHeatmap(models, { basis: 'plan', dimensions: [{ key: 'bug', label: 'Bug', category: 'mystery', weightPct: 10 }] });
  const note = spec.layout.annotations.find((a) => a.text === '<b>mystery</b>');
  assert.equal(note.font.color, '#94a3b8');
});
