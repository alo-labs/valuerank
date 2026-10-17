import test from 'node:test';
import assert from 'node:assert/strict';
import {
  bootStatic, bootIndex, bootRankings, bootBenchmarks, bootTb4, bootChangelog,
} from '../../../valuerank/site/assets/js/pages/boot.js';
import { add } from '../helpers/fake-dom.mjs';
import { createFakePlotly } from '../helpers/fake-plotly.mjs';
import { indexPage, rankingsPage } from './pages.mjs';
import { data } from './fixture.mjs';

class FakeObserver {
  constructor(callback, options) {
    this.callback = callback;
    this.options = options;
    this.observed = [];
    FakeObserver.all.push(this);
  }
  observe(target) { this.observed.push(target); }
  disconnect() {}
  show() { this.callback(this.observed.map((target) => ({ isIntersecting: true, target }))); }
}
FakeObserver.all = [];

/** Adds the browser APIs the boot modules reach for. */
function armed(win, { fetch } = {}) {
  win.document.defaultView = win;
  win.Plotly = createFakePlotly();
  win.IntersectionObserver = FakeObserver;
  win.getComputedStyle = () => ({ getPropertyValue: () => '' });
  if (fetch) win.fetch = fetch;
  return win;
}

/** Tabs, panels, containers and summaries in the shape templates/partials/chart.html renders. */
function chartParts(win, keys) {
  const { body } = win.document;
  const card = add(body, 'div', { class: 'chart-card' });
  const tabs = keys.map((key, i) => add(card, 'button', { role: 'tab', 'data-chart-tab': key, 'aria-selected': String(i === 0) }));
  const panels = keys.map((key) => {
    const panel = add(card, 'div', { 'data-chart-panel': key });
    const chart = add(panel, 'div', { 'data-chart': key });
    add(panel, 'p', { 'data-chart-summary': '' });
    return { panel, chart };
  });
  return { tabs, panels };
}

const lastObserver = () => FakeObserver.all.at(-1);
const answer = (payload) => async () => ({ ok: true, json: async () => payload });

test('static pages get the theme, the menu and the FAQ and nothing else', () => {
  const win = armed(indexPage().win);
  const theme = bootStatic(win);
  assert.equal(theme.current(), 'light');
});

test('the answer page starts its chart from the state the script rendered', async () => {
  const page = indexPage({ search: '?basis=api&w=40' });
  armed(page.win);
  const { tabs } = chartParts(page.win, ['pareto']);
  const charts = bootIndex(page.win);
  assert.deepEqual(charts.state(), { basis: 'api', costWeightPct: 40, dark: false });
  assert.equal(lastObserver().options.rootMargin, '200px');
  lastObserver().show();
  await charts.idle();
  assert.equal(page.win.Plotly.of('newPlot').length, 1);
  assert.equal(tabs[0].getAttribute('aria-selected'), 'true');
});

test('moving the slider or the basis re-sends the recomputed models to the charts', async () => {
  const page = indexPage();
  armed(page.win);
  chartParts(page.win, ['pareto']);
  const charts = bootIndex(page.win);
  lastObserver().show();
  await charts.idle();
  page.slider.value = '100';
  page.slider.fire('input');
  await charts.idle();
  assert.equal(charts.state().costWeightPct, 100);
  page.toggle.api.click();
  await charts.idle();
  assert.equal(charts.state().basis, 'api');
  assert.equal(page.win.Plotly.of('newPlot').length, 3); // first draw, then one per state change
});

test('theme changes reach the charts as vr:theme and the chart reads the site colours', async () => {
  const page = indexPage();
  armed(page.win);
  const asked = [];
  page.win.getComputedStyle = () => ({ getPropertyValue: (name) => { asked.push(name); return ''; } });
  const button = add(page.win.document.body, 'button', { 'data-theme-toggle': '' });
  chartParts(page.win, ['pareto']);
  const charts = bootIndex(page.win);
  lastObserver().show();
  await charts.idle();
  assert.deepEqual([...new Set(asked)].sort(), ['--border', '--border-strong', '--surface', '--text', '--text-muted']);
  button.click();
  await charts.idle();
  assert.equal(charts.state().dark, true);
  assert.equal(page.win.document.documentElement.getAttribute('data-theme'), 'dark');
});

test('the chart tab is read from ?chart= and written back, leaving the default tab out of the URL', () => {
  const page = rankingsPage({ search: '?chart=heatmap&q=bolt' });
  armed(page.win);
  const { tabs, panels } = chartParts(page.win, ['pareto', 'heatmap']);
  bootRankings(page.win);
  assert.equal(tabs[1].getAttribute('aria-selected'), 'true');
  assert.equal(panels[0].panel.hidden, true);
  tabs[0].click();
  assert.equal(page.win.location.search, '?q=bolt');
  tabs[1].click();
  assert.equal(page.win.location.search, '?q=bolt&chart=heatmap');
  page.slider.value = '50';
  page.slider.fire('input');
  assert.match(page.win.location.search, /chart=heatmap/);
});

test('unreadable rankings data on the instrument page leaves the error box to the script', () => {
  const page = rankingsPage();
  armed(page.win);
  page.win.document.getElementById('rankings-data').replaceChildren('{');
  chartParts(page.win, ['pareto']);
  assert.equal(bootRankings(page.win), null);
  assert.equal(page.error.hidden, false);
});

test('benchmarks fetch the public JSON and draw the coverage and LiveBench charts', async () => {
  const page = indexPage();
  const payloads = {
    '/data/rankings.json': data,
    '/data/livebench.json': { rows: [{ id: 'a', name: 'A', overallScore: 60, costPerSuccessfulTaskUsd: 1, instructionFollowingScore: 70, pareto: true }] },
  };
  const requested = [];
  armed(page.win, { fetch: async (url) => { requested.push(url); return { ok: true, json: async () => payloads[url] }; } });
  chartParts(page.win, ['heatmapData', 'livebenchPareto']);
  const charts = await bootBenchmarks(page.win);
  assert.deepEqual(requested.sort(), ['/data/livebench.json', '/data/rankings.json']);
  assert.equal(charts.state().basis, 'plan');
  lastObserver().show();
  await charts.idle();
  assert.ok(page.win.Plotly.of('newPlot').length >= 1);
});

test('a failed fetch marks every chart as failed instead of throwing', async () => {
  const bad = armed(indexPage().win, { fetch: async () => ({ ok: false, status: 500 }) });
  const { panels } = chartParts(bad, ['heatmapData']);
  assert.equal(await bootBenchmarks(bad), null);
  assert.equal(panels[0].chart.getAttribute('data-chart-status'), 'error');
  const down = armed(indexPage().win, { fetch: async () => { throw new Error('offline'); } });
  const parts = chartParts(down, ['bump']);
  assert.equal(await bootChangelog(down), null);
  assert.equal(parts.panels[0].chart.getAttribute('data-chart-status'), 'error');
});

test('Terminal-Bench draws from its embedded rows and a single tab needs no URL state', async () => {
  const page = indexPage();
  armed(page.win);
  add(page.win.document.body, 'script', { id: 'page-data', type: 'application/json' }, JSON.stringify({
    rows: [{ model: 'M', baseModel: 'M', agent: 'A', costUsd: 100, resolutionRatePct: 50, uncertaintyPct: 1, tokens: '1B', rankLabel: '1' }],
  }));
  const { tabs } = chartParts(page.win, ['tb4']);
  const charts = bootTb4(page.win);
  lastObserver().show();
  await charts.idle();
  assert.equal(page.win.Plotly.of('newPlot').length, 1);
  tabs[0].click();
});

test('the changelog chart combines the embedded versions with the fetched rankings', async () => {
  const page = indexPage();
  armed(page.win, { fetch: answer(data) });
  const versions = [{ version: 'v2', ranks: { alpha: 1 }, rankChanges: [] }, { version: 'v1', ranks: { alpha: 2 }, rankChanges: [] }];
  add(page.win.document.body, 'script', { id: 'page-data', type: 'application/json' }, JSON.stringify({ versions }));
  chartParts(page.win, ['bump']);
  const charts = await bootChangelog(page.win);
  assert.equal(charts.state().basis, 'api');
  lastObserver().show();
  await charts.idle();
  assert.equal(page.win.Plotly.of('newPlot').length, 1);
});

for (const [entry, build] of [
  ['static', () => indexPage()],
  ['index', () => { const p = indexPage(); chartParts(p.win, ['pareto']); return p; }],
  ['rankings', () => { const p = rankingsPage(); chartParts(p.win, ['pareto']); return p; }],
  ['tb4', () => {
    const p = indexPage();
    add(p.win.document.body, 'script', { id: 'page-data', type: 'application/json' }, JSON.stringify({ rows: [] }));
    chartParts(p.win, ['tb4']);
    return p;
  }],
  ['benchmarks', () => { const p = indexPage(); chartParts(p.win, ['heatmapData']); return p; }],
  ['changelog', () => { const p = indexPage(); chartParts(p.win, ['bump']); return p; }],
]) {
  test(`pages/${entry}.js boots the page with the browser window`, async () => {
    const page = build();
    armed(page.win, { fetch: async () => ({ ok: false, status: 404 }) });
    globalThis.window = page.win;
    try {
      await import(`../../../valuerank/site/assets/js/pages/${entry}.js`);
    } finally {
      delete globalThis.window;
    }
    assert.ok(page.win.document.documentElement.getAttribute('data-theme'));
  });
}
