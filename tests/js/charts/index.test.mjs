import { test } from 'node:test';
import assert from 'node:assert/strict';
import { REGISTRY, defaultObserver, mountCharts } from '../../../valuerank/site/assets/js/charts/index.js';
import { createFakePlotly } from '../helpers/fake-plotly.mjs';
import { FakeElement, createObserverFactory } from './_fake-dom.mjs';
import { models, dimensions, categories, bases, changelog, livebench, tb4Rows } from './_fixtures.mjs';

const data = {
  rankings: { defaultBasis: 'plan', costWeightPct: 20, dimensions, categories, bases, models },
  changelog, livebench, tb4: { rows: tb4Rows },
};

function setup({ keys = ['pareto', 'tb4'], tabs = false, plotly = createFakePlotly(), config = {} } = {}) {
  const containers = Object.fromEntries(keys.map((k) => [k, new FakeElement({ 'data-chart': k })]));
  const panels = keys.map((k) => new FakeElement({ 'data-chart-panel': k }, [containers[k], new FakeElement({ 'data-chart-summary': '' })]));
  const buttons = tabs ? keys.map((k, i) => new FakeElement({ 'data-chart-tab': k, 'aria-selected': i === 0 ? 'true' : 'false' })) : [];
  const root = new FakeElement({}, [...buttons, ...panels]);
  const observer = createObserverFactory();
  let loads = 0;
  const changes = [];
  const mount = (extra = {}) => mountCharts(root, data, {
    loadPlotly: async () => { loads += 1; return plotly; }, observer, onChartChange: (k) => changes.push(k), ...config, ...extra,
  });
  return { root, containers, panels, buttons, observer, plotly, mount, loads: () => loads, changes };
}

test('registry exposes build, render and source for every chart', () => {
  assert.deepEqual(Object.keys(REGISTRY).sort(), ['bubble', 'bump', 'decomposition', 'displacement', 'frontier2', 'heatmap', 'heatmapData', 'livebenchPareto', 'pareto', 'tb4']);
  for (const entry of Object.values(REGISTRY)) {
    assert.equal(typeof entry.build, 'function');
    assert.equal(typeof entry.render, 'function');
    assert.ok(['rankings', 'changelog', 'livebench', 'tb4'].includes(entry.source));
  }
  assert.equal(REGISTRY.heatmapData.options.height, 420);
});

test('a chart renders only once its container becomes visible, with one Plotly load', async () => {
  const t = setup();
  const mount = t.mount();
  assert.equal(t.plotly.of('newPlot').length, 0);
  t.observer.show(t.containers.pareto);
  await mount.idle();
  t.observer.show(t.containers.pareto);
  t.observer.show(t.containers.tb4);
  await mount.idle();
  assert.equal(t.plotly.of('newPlot').length, 2);
  assert.equal(t.loads(), 1);
  assert.equal(t.containers.pareto.getAttribute('data-chart-status'), 'ready');
  assert.match(t.containers.pareto.getAttribute('aria-label'), /4 models/);
  assert.equal(t.panels[0].querySelector('[data-chart-summary]').textContent.startsWith('Quality against Plan cost'), true);
  assert.deepEqual(mount.rendered().sort(), ['pareto', 'tb4']);
});

test('hidden containers do not render and unknown chart keys are ignored', async () => {
  const t = setup({ keys: ['pareto', 'mystery'] });
  const mount = t.mount();
  t.observer.hide(t.containers.pareto);
  t.observer.show(t.containers.mystery);
  await mount.idle();
  assert.equal(t.plotly.calls.length, 0);
  assert.deepEqual(mount.rendered(), []);
  mount.show('mystery');
  assert.deepEqual(mount.rendered(), []);
});

test('basis and cost-weight changes re-render drawn charts with the new state', async () => {
  const t = setup();
  const mount = t.mount();
  t.observer.show(t.containers.pareto);
  await mount.idle();
  const before = t.plotly.of('newPlot')[0].args[1][1].x.slice();
  t.root.dispatch('vr:state', { basis: 'api', costWeightPct: 35 });
  await mount.idle();
  const plots = t.plotly.of('newPlot');
  assert.equal(plots.length, 2);
  assert.notDeepEqual(plots[1].args[1][1].x, before);
  assert.match(plots[1].args[2].xaxis.title.text, /API cost/);
  assert.deepEqual(mount.state(), { basis: 'api', costWeightPct: 35, dark: false });
  t.root.dispatch('vr:state', { models: [models[0]] });
  await mount.idle();
  assert.match(t.containers.pareto.getAttribute('aria-label'), /1 models/);
  t.root.dispatch('vr:state', undefined);
  await mount.idle();
  assert.equal(t.plotly.of('newPlot').length, 4);
});

test('theme changes re-render with the dark tokens', async () => {
  const t = setup();
  const mount = t.mount({ getVar: () => '' });
  t.observer.show(t.containers.pareto);
  await mount.idle();
  t.root.dispatch('vr:theme', { dark: true });
  await mount.idle();
  const dark = t.plotly.of('newPlot')[1].args[2];
  assert.equal(dark.paper_bgcolor, '#111827');
  t.root.dispatch('vr:theme', undefined);
  await mount.idle();
  assert.equal(t.plotly.of('newPlot')[2].args[2].paper_bgcolor, '#ffffff');
});

test('initial state comes from the caller, then the rankings defaults', async () => {
  const t = setup();
  const mount = t.mount({ initialState: { basis: 'api', costWeightPct: 5, dark: true } });
  assert.deepEqual(mount.state(), { basis: 'api', costWeightPct: 5, dark: true });
  const fresh = setup().mount();
  assert.deepEqual(fresh.state(), { basis: 'plan', costWeightPct: 20, dark: false });
});

test('tabs select a panel, mark aria-selected, render at once and report the chart param', async () => {
  const t = setup({ keys: ['pareto', 'tb4', 'bump'], tabs: true });
  const mount = t.mount();
  assert.deepEqual(t.buttons.map((b) => b.getAttribute('aria-selected')), ['true', 'false', 'false']);
  assert.deepEqual(t.panels.map((p) => p.hidden), [false, true, true]);
  t.buttons[1].dispatch('click');
  await mount.idle();
  assert.deepEqual(t.buttons.map((b) => b.getAttribute('aria-selected')), ['false', 'true', 'false']);
  assert.deepEqual(t.panels.map((p) => p.hidden), [true, false, true]);
  assert.deepEqual(t.changes, ['tb4']);
  assert.equal(t.plotly.of('newPlot').length, 2, 'the initial tab and the newly selected tab');
  assert.equal(t.buttons[1].getAttribute('tabindex'), '0');
  assert.equal(t.buttons[0].getAttribute('tabindex'), '-1');
});

test('the initial tab honours the caller choice and falls back to the first tab', () => {
  const chosen = setup({ keys: ['pareto', 'tb4'], tabs: true });
  chosen.mount({ initialChart: 'tb4' });
  assert.deepEqual(chosen.panels.map((p) => p.hidden), [true, false]);
  assert.deepEqual(chosen.changes, [], 'initial selection is not reported as a change');
  const unknown = setup({ keys: ['pareto', 'tb4'], tabs: true });
  unknown.mount({ initialChart: 'nope' });
  assert.deepEqual(unknown.panels.map((p) => p.hidden), [false, true]);
});

test('arrow keys move between tabs and wrap around', async () => {
  const t = setup({ keys: ['pareto', 'tb4', 'bump'], tabs: true });
  const mount = t.mount();
  t.buttons[0].dispatch('keydown', undefined, { key: 'ArrowLeft' });
  assert.equal(t.buttons[2].getAttribute('aria-selected'), 'true');
  t.buttons[2].dispatch('keydown', undefined, { key: 'ArrowRight' });
  assert.equal(t.buttons[0].getAttribute('aria-selected'), 'true');
  t.buttons[0].dispatch('keydown', undefined, { key: 'ArrowRight' });
  assert.equal(t.buttons[1].getAttribute('aria-selected'), 'true');
  const before = t.changes.length;
  t.buttons[1].dispatch('keydown', undefined, { key: 'Enter' });
  assert.equal(t.changes.length, before);
  await mount.idle();
});

test('a failed Plotly load marks the chart as errored and the next visit retries', async () => {
  let attempts = 0;
  const plotly = createFakePlotly();
  const t = setup({ plotly });
  const mount = t.mount({ loadPlotly: async () => { attempts += 1; if (attempts === 1) throw new Error('offline'); return plotly; } });
  t.observer.show(t.containers.pareto);
  await mount.idle();
  assert.equal(t.containers.pareto.getAttribute('data-chart-status'), 'error');
  assert.deepEqual(mount.rendered(), []);
  t.observer.show(t.containers.pareto);
  await mount.idle();
  assert.equal(t.containers.pareto.getAttribute('data-chart-status'), 'ready');
  assert.equal(attempts, 2);
});

test('a failing plot call is reported on the container', async () => {
  const t = setup({ plotly: createFakePlotly({ failOn: 'newPlot' }) });
  const mount = t.mount();
  t.observer.show(t.containers.pareto);
  await mount.idle();
  assert.equal(t.containers.pareto.getAttribute('data-chart-status'), 'error');
});

test('charts with missing data sources render their empty states', async () => {
  const t = setup({ keys: ['bump', 'livebenchPareto', 'tb4'] });
  const bare = mountCharts(t.root, { rankings: undefined }, { loadPlotly: async () => t.plotly, observer: t.observer });
  Object.values(t.containers).forEach((el) => t.observer.show(el));
  await bare.idle();
  assert.equal(t.plotly.calls.length, 0);
  assert.match(t.containers.tb4.textContent, /No Terminal-Bench/);
  assert.match(t.containers.livebenchPareto.textContent, /No matched LiveBench/);
  assert.match(t.containers.bump.textContent, /No version history/);
  assert.deepEqual(bare.state(), { basis: undefined, costWeightPct: undefined, dark: false });
});

test('destroy stops listening and disconnects the observer', async () => {
  const t = setup();
  const mount = t.mount();
  t.observer.show(t.containers.pareto);
  await mount.idle();
  mount.destroy();
  assert.equal(t.observer.created[0].disconnected, true);
  t.root.dispatch('vr:state', { basis: 'api' });
  t.root.dispatch('vr:theme', { dark: true });
  await mount.idle();
  assert.equal(t.plotly.of('newPlot').length, 1);
});

test('defaultObserver wraps the browser IntersectionObserver', () => {
  const seen = [];
  globalThis.IntersectionObserver = class { constructor(cb, opts) { seen.push([cb, opts]); } };
  try {
    const cb = () => {};
    defaultObserver(cb);
    assert.equal(seen[0][0], cb);
    assert.equal(seen[0][1].rootMargin, '200px');
  } finally {
    delete globalThis.IntersectionObserver;
  }
});

test('mounting without an explicit observer uses the browser IntersectionObserver; no selected tab defaults to the first', () => {
  const created = [];
  globalThis.IntersectionObserver = class { constructor(cb) { created.push(cb); } observe() {} disconnect() {} };
  try {
    const t = setup({ keys: ['pareto', 'tb4'], tabs: true });
    t.buttons.forEach((b) => b.setAttribute('aria-selected', 'false'));
    mountCharts(t.root, data, { loadPlotly: async () => t.plotly, onChartChange: () => {} });
    assert.equal(created.length, 1);
    assert.deepEqual(t.panels.map((p) => p.hidden), [false, true]);
  } finally {
    delete globalThis.IntersectionObserver;
  }
});
