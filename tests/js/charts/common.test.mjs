import { test } from 'node:test';
import assert from 'node:assert/strict';
import { announce, baseLayout, costText, defaultRaf, emptySpec, finite, frontierIds, makeSpec, money, pick, renderSpec, resolveOptions } from '../../../valuerank/site/assets/js/charts/common.js';
import { createFakePlotly } from '../helpers/fake-plotly.mjs';
import { createPlotDiv } from './_fixtures.mjs';
import { FakeElement } from './_fake-dom.mjs';

test('pick reads per-basis objects and plain values', () => {
  assert.equal(pick({ api: 1, plan: 2 }, 'plan'), 2);
  assert.equal(pick({ api: 1 }, 'plan'), null);
  assert.equal(pick(5, 'api'), 5);
  assert.equal(pick(undefined, 'api'), null);
  assert.equal(finite(1), true);
  assert.equal(finite(NaN), false);
  assert.equal(finite(null), false);
});

test('resolveOptions defaults to the plan basis and resolves labels', () => {
  const plan = resolveOptions();
  assert.equal(plan.basis, 'plan');
  assert.equal(plan.costLabel, 'Plan cost');
  assert.equal(plan.basisLabel, 'Plan ranking');
  assert.deepEqual(plan.dimensions, []);
  const api = resolveOptions({ basis: 'api', dark: true });
  assert.equal(api.costLabel, 'API cost');
  assert.equal(api.basisLabel, 'API ranking');
  assert.equal(api.tokens.dark, true);
  const custom = resolveOptions({ basis: 'api', bases: { api: { label: 'X', costLabel: 'Y' } }, tokens: { t: 1 }, dimensions: [1], categories: { a: 1 } });
  assert.deepEqual([custom.costLabel, custom.basisLabel, custom.tokens, custom.dimensions, custom.categories], ['Y', 'X', { t: 1 }, [1], { a: 1 }]);
  assert.equal(resolveOptions({ costLabel: 'Z' }).costLabel, 'Z');
});

test('money and costText follow the basis unit', () => {
  assert.equal(money(1081.5, 0), '$1,082');
  assert.equal(money(null), '—');
  assert.equal(costText({ cost: { apiUsd: 1000, apiUsdPerPoint: 19.3 } }, 'api'), '$19.300 per Index point');
  assert.equal(costText({ cost: { planUsdPerPoint: 1.9308 } }, 'plan'), '$1.931 per Index point');
  assert.equal(costText({}, 'plan'), '— per Index point');
});

test('baseLayout and specs', () => {
  const opts = resolveOptions();
  assert.equal(baseLayout(opts, 'T', 13).title.font.size, 13);
  assert.equal(baseLayout(opts, 'T').title.text, 'T');
  const spec = makeSpec(opts, { traces: [1], layout: {}, label: 'l', summary: 's' });
  assert.equal(spec.config.displaylogo, false);
  const empty = emptySpec(opts, 'l', 'nothing');
  assert.deepEqual([empty.empty, empty.traces], ['nothing', []]);
});

test('announce labels the container and fills the summary element when present', () => {
  const summary = new FakeElement({ 'data-chart-summary': '' });
  const container = new FakeElement();
  new FakeElement({}, [container, summary]);
  announce(container, { label: 'LABEL', summary: 'SUM' });
  assert.equal(container.getAttribute('aria-label'), 'LABEL');
  assert.equal(container.getAttribute('role'), 'img');
  assert.equal(summary.textContent, 'SUM');
  const lone = new FakeElement();
  announce(lone, { label: 'L', summary: 'S' });
  assert.equal(lone.getAttribute('aria-label'), 'L');
  const orphanParent = new FakeElement();
  const child = new FakeElement();
  new FakeElement({}, [child, orphanParent]);
  announce(child, { label: 'L', summary: 'S' });
});

test('frontierIds keeps strictly improving rows in both directions', () => {
  const rows = [{ id: 'a', x: 1, y: 1 }, { id: 'b', x: 2, y: 3 }, { id: 'c', x: 3, y: 2 }, { id: 'd', x: 2, y: 1 }];
  const run = (dir) => [...frontierIds(rows, (r) => r.id, (r) => r.x, (r) => r.y, dir)].sort();
  assert.deepEqual(run('lower'), ['a', 'b']);
  assert.deepEqual(run('higher'), ['b', 'c']);
  assert.deepEqual([...frontierIds([{ id: 1, x: 1, y: 2 }, { id: 2, x: 1, y: 3 }], (r) => r.id, (r) => r.x, (r) => r.y, 'lower')], [2]);
});

test('defaultRaf schedules the callback', async () => {
  await new Promise((resolve) => defaultRaf(resolve));
});

const labelSpec = (extra = {}) => ({
  traces: [{}], layout: { annotations: [{ text: 'base' }] }, config: {}, label: 'l', summary: 's',
  labels: { points: [{ label: 'P', x: 10, y: 10 }], options: { fontSize: 9 }, dark: false, ...extra },
});

test('renderSpec plots, then relayouts base plus label annotations', async () => {
  const plotly = createFakePlotly();
  const div = createPlotDiv();
  assert.equal(await renderSpec(div, labelSpec({ base: [{ text: 'quad' }] }), {}, plotly), true);
  assert.equal(plotly.of('newPlot').length, 1);
  const [first] = plotly.of('relayout');
  assert.deepEqual(first.args[1].annotations.map((a) => a.text), ['quad', 'P']);
  assert.equal(div.attrs['aria-label'], 'l');
});

test('renderSpec without labels or geometry stops after newPlot', async () => {
  const plotly = createFakePlotly();
  assert.equal(await renderSpec(createPlotDiv(), { ...labelSpec(), labels: undefined }, undefined, plotly), true);
  assert.equal(plotly.of('relayout').length, 0);
  assert.equal(await renderSpec(createPlotDiv({ layout: null }), labelSpec(), { measureText: () => 5 }, plotly), true);
  assert.equal(plotly.of('relayout').length, 0);
});

test('renderSpec shows the empty message instead of plotting', async () => {
  const plotly = createFakePlotly();
  const div = createPlotDiv();
  assert.equal(await renderSpec(div, { ...labelSpec(), empty: 'No data' }, {}, plotly), false);
  assert.equal(div.textContent, 'No data');
  assert.equal(plotly.calls.length, 0);
});

test('renderSpec repairs colliding rendered labels using the injected raf', async () => {
  const plotly = createFakePlotly();
  const rect = { left: 0, right: 1000, top: 0, bottom: 600 };
  const boxes = [
    { text: 'A', rect: { left: 100, right: 140, top: 100, bottom: 112 } },
    { text: 'B', rect: { left: 110, right: 150, top: 102, bottom: 114 } },
  ];
  const div = createPlotDiv({ boxes, rect });
  const spec = labelSpec();
  spec.labels.points = [{ label: 'A', x: 10, y: 10 }, { label: 'B', x: 11, y: 10 }];
  let ticks = 0;
  div.querySelectorAll = () => {
    ticks += 1;
    return ticks > 1 ? [{ textContent: 'A', getBoundingClientRect: () => boxes[0].rect }, { textContent: 'B', getBoundingClientRect: () => ({ left: 400, right: 440, top: 300, bottom: 312 }) }] : boxes.map((b) => ({ textContent: b.text, getBoundingClientRect: () => b.rect }));
  };
  await renderSpec(div, spec, { raf: (cb) => cb() }, plotly);
  assert.ok(plotly.of('relayout').length >= 2);
});

test('resolveOptions tolerates a bases map that lacks the active basis', () => {
  const opts = resolveOptions({ basis: 'plan', bases: { api: { label: 'A', costLabel: 'B' } } });
  assert.deepEqual([opts.costLabel, opts.basisLabel], ['Plan cost', 'Plan ranking']);
});

test('nameOf prefers the short name and weightSuffix needs a finite weight', async () => {
  const { nameOf, weightSuffix } = await import('../../../valuerank/site/assets/js/charts/common.js');
  assert.equal(nameOf({ shortName: 'S', name: 'N' }), 'S');
  assert.equal(nameOf({ name: 'N' }), 'N');
  assert.equal(weightSuffix({ costWeightPct: 18.9394 }), ' (cost weight 18.9%)');
  assert.equal(weightSuffix({}), '');
});
