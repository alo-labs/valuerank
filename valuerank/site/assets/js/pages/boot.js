// Page boot modules: wire the shared behaviour, the page's public JSON and the chart layer together.
// Each entry file in this directory is two lines (import + call with the browser window), so everything
// here takes the window and can be driven by a fake DOM in tests.
import { createUrlSync, defaultState, initApp } from '../app.js';
import { initIndex, initRankings, loadData } from '../rankings.js';
import { mountCharts } from '../charts/index.js';
import { loadPlotly } from '../charts/plotly-loader.js';

/** Chart colour tokens (charts/theme.js names) mapped to the site's CSS custom properties. */
const CHART_VARS = {
  '--bg-card': '--surface',
  '--text-secondary': '--text-muted',
  '--border': '--border',
  '--text-primary': '--text',
  '--border-hover': '--border-strong',
};

const isDark = (doc) => doc.documentElement.getAttribute('data-theme') === 'dark';
const embedded = (doc, id) => JSON.parse(doc.getElementById(id).textContent);

async function fetchJson(win, url) {
  const response = await win.fetch(url);
  if (!response.ok) throw new Error(`${url}: ${response.status}`);
  return response.json();
}

function emitter(win) {
  const root = win.document.body;
  return (type, detail) => root.dispatchEvent(new win.CustomEvent(type, { detail }));
}

/** Mounts the page's charts on <body>; resolves `config` defaults for the browser. */
function mount(win, data, config = {}) {
  const doc = win.document;
  const getVar = (name) => win.getComputedStyle(doc.documentElement).getPropertyValue(CHART_VARS[name]);
  return mountCharts(doc.body, data, {
    loadPlotly: () => loadPlotly(doc),
    observer: (callback) => new win.IntersectionObserver(callback, { rootMargin: '200px' }),
    getVar,
    onChartChange: () => {},
    ...config,
    initialState: { ...config.initialState, dark: isDark(doc) },
  });
}

function markChartsFailed(doc) {
  doc.querySelectorAll('[data-chart]').forEach((el) => el.setAttribute('data-chart-status', 'error'));
}

/** Pages with no behaviour of their own: theme, menu and FAQ. */
export function bootStatic(win) {
  return initApp(win);
}

function bootRanked(win, init) {
  const doc = win.document;
  const emit = emitter(win);
  initApp(win, (dark) => emit('vr:theme', { dark }));
  let rankings;
  try {
    rankings = loadData(doc);
  } catch {
    init(win);
    return null;
  }
  const sync = createUrlSync(win, defaultState(rankings));
  const urlState = sync.read();
  const firstTab = doc.querySelector('[data-chart-tab]').getAttribute('data-chart-tab');
  // The script renders first so the charts start from the recomputed models (URL basis and cost weight),
  // then follow every later change through vr:statechange -> vr:state.
  let latest = null;
  let charts = null;
  doc.addEventListener('vr:statechange', (event) => {
    latest = event.detail;
    if (charts) emit('vr:state', { basis: latest.state.basis, costWeightPct: latest.state.w, models: latest.models });
  });
  init(win);
  charts = mount(win, { rankings: { ...rankings, models: latest.models } }, {
    initialChart: urlState.chart,
    initialState: { basis: latest.state.basis, costWeightPct: latest.state.w },
    // The default tab keeps the URL clean; any other tab is written as ?chart=<key>.
    onChartChange: (key) => sync.write({ ...sync.read(), chart: key === firstTab ? '' : key }),
  });
  return charts;
}

export const bootIndex = (win) => bootRanked(win, initIndex);
export const bootRankings = (win) => bootRanked(win, initRankings);

export async function bootBenchmarks(win) {
  const emit = emitter(win);
  initApp(win, (dark) => emit('vr:theme', { dark }));
  try {
    const [rankings, livebench] = await Promise.all([fetchJson(win, '/data/rankings.json'), fetchJson(win, '/data/livebench.json')]);
    return mount(win, { rankings, livebench: livebench.rows }, { initialState: { basis: rankings.defaultBasis } });
  } catch {
    markChartsFailed(win.document);
    return null;
  }
}

export function bootTb4(win) {
  const emit = emitter(win);
  initApp(win, (dark) => emit('vr:theme', { dark }));
  return mount(win, { rankings: {}, tb4: embedded(win.document, 'page-data') });
}

export async function bootChangelog(win) {
  const emit = emitter(win);
  initApp(win, (dark) => emit('vr:theme', { dark }));
  try {
    const rankings = await fetchJson(win, '/data/rankings.json');
    // Recorded history predates the plan basis, so the chart closes on the current API ranks.
    return mount(win, { rankings, changelog: embedded(win.document, 'page-data') }, { initialState: { basis: 'api' } });
  } catch {
    markChartsFailed(win.document);
    return null;
  }
}
