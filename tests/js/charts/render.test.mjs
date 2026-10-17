import { test } from 'node:test';
import assert from 'node:assert/strict';
import * as pareto from '../../../valuerank/site/assets/js/charts/pareto.js';
import * as livebench from '../../../valuerank/site/assets/js/charts/livebench-pareto.js';
import * as decomposition from '../../../valuerank/site/assets/js/charts/decomposition.js';
import * as displacement from '../../../valuerank/site/assets/js/charts/displacement.js';
import * as heatmap from '../../../valuerank/site/assets/js/charts/heatmap.js';
import * as bubble from '../../../valuerank/site/assets/js/charts/bubble.js';
import * as bump from '../../../valuerank/site/assets/js/charts/bump.js';
import * as frontier2 from '../../../valuerank/site/assets/js/charts/frontier2.js';
import * as tb4 from '../../../valuerank/site/assets/js/charts/tb4.js';
import { createFakePlotly } from '../helpers/fake-plotly.mjs';
import { FakeElement } from './_fake-dom.mjs';
import { models, changelog, livebench as livebenchRows, tb4Rows, baseOptions } from './_fixtures.mjs';
import { createPlotDiv } from './_fixtures.mjs';

const cases = [
  ['Pareto', pareto, models],
  ['LivebenchPareto', livebench, livebenchRows],
  ['Decomposition', decomposition, models],
  ['Displacement', displacement, models],
  ['Heatmap', heatmap, models],
  ['Bubble', bubble, models],
  ['Bump', bump, { versions: changelog.versions, models }],
  ['Frontier2', frontier2, models],
  ['Tb4', tb4, tb4Rows],
];

for (const [name, mod, data] of cases) {
  test(`render${name} plots the built spec and writes an accessible summary`, async () => {
    const plotly = createFakePlotly();
    const summary = new FakeElement({ 'data-chart-summary': '' });
    const container = createPlotDiv({ parent: new FakeElement({}, [summary]) });
    container.getAttribute = (key) => container.attrs[key];
    const result = await mod[`render${name}`](container, data, baseOptions, plotly);
    assert.equal(result, true);
    const [plot] = plotly.of('newPlot');
    const spec = mod[`build${name}`](data, baseOptions);
    assert.equal(plot.args[0], container);
    assert.deepEqual(plot.args[1], spec.traces);
    assert.deepEqual(plot.args[3], spec.config);
    assert.equal(container.attrs['aria-label'], spec.label);
    assert.ok(spec.label.length > 20);
    assert.equal(summary.textContent, spec.summary);
  });
}

test('every chart that places labels asks for a relayout with annotations', async () => {
  const plotly = createFakePlotly();
  await pareto.renderPareto(createPlotDiv(), models, baseOptions, plotly);
  assert.equal(plotly.of('relayout').length, 1);
  assert.ok(plotly.of('relayout')[0].args[1].annotations.length >= 4);
});
