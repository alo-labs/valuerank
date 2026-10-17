// Chart registry and lazy mounting. Containers carry data-chart="<key>"; a chart is
// drawn when it first becomes visible and redrawn when the view state or theme changes.
import { buildPareto, renderPareto } from './pareto.js';
import { buildLivebenchPareto, renderLivebenchPareto } from './livebench-pareto.js';
import { buildDecomposition, renderDecomposition } from './decomposition.js';
import { buildDisplacement, renderDisplacement } from './displacement.js';
import { buildHeatmap, renderHeatmap } from './heatmap.js';
import { buildBubble, renderBubble } from './bubble.js';
import { buildBump, renderBump } from './bump.js';
import { buildFrontier2, renderFrontier2 } from './frontier2.js';
import { buildTb4, renderTb4 } from './tb4.js';
import { themeTokens } from './theme.js';

/** key -> { build, render, source, options? }. `source` names the input in `inputFor`. */
export const REGISTRY = {
  pareto: { build: buildPareto, render: renderPareto, source: 'rankings' },
  decomposition: { build: buildDecomposition, render: renderDecomposition, source: 'rankings' },
  displacement: { build: buildDisplacement, render: renderDisplacement, source: 'rankings' },
  heatmap: { build: buildHeatmap, render: renderHeatmap, source: 'rankings', options: { height: 540 } },
  heatmapData: { build: buildHeatmap, render: renderHeatmap, source: 'rankings', options: { height: 420 } },
  bubble: { build: buildBubble, render: renderBubble, source: 'rankings' },
  bump: { build: buildBump, render: renderBump, source: 'changelog' },
  frontier2: { build: buildFrontier2, render: renderFrontier2, source: 'rankings' },
  livebenchPareto: { build: buildLivebenchPareto, render: renderLivebenchPareto, source: 'livebench' },
  tb4: { build: buildTb4, render: renderTb4, source: 'tb4' },
};

const INPUTS = {
  rankings: (data, state) => state.models,
  changelog: (data, state) => ({ versions: data.changelog?.versions ?? [], models: state.models }),
  livebench: (data) => data.livebench ?? [],
  tb4: (data) => data.tb4?.rows ?? [],
};

export const defaultObserver = (callback) => new IntersectionObserver(callback, { rootMargin: '200px' });

/**
 * root: element containing [data-chart] containers (and optional tabs/panels).
 * data: { rankings, changelog?, livebench?, tb4? } as in the public JSON.
 * config: { loadPlotly(), observer(callback), onChartChange(key), initialChart,
 *           initialState: {basis, costWeightPct, dark}, getVar, measureText, raf }
 * Events on root: vr:state {basis?, costWeightPct?, models?} and vr:theme {dark}.
 */
export function mountCharts(root, data, config) {
  const rankings = data.rankings ?? {};
  const initial = config.initialState ?? {};
  const state = {
    basis: initial.basis ?? rankings.defaultBasis,
    costWeightPct: initial.costWeightPct ?? rankings.costWeightPct,
    dark: Boolean(initial.dark),
  };
  let models = rankings.models ?? [];

  const elements = new Map();
  root.querySelectorAll('[data-chart]').forEach((el) => elements.set(el.getAttribute('data-chart'), el));
  const rendered = new Set();
  const chains = new Map();
  let plotlyPromise = null;

  const getPlotly = () => {
    plotlyPromise ??= Promise.resolve(config.loadPlotly()).catch((error) => { plotlyPromise = null; throw error; });
    return plotlyPromise;
  };
  const optionsFor = (entry) => ({
    ...entry.options,
    basis: state.basis,
    costWeightPct: state.costWeightPct,
    dark: state.dark,
    tokens: themeTokens({ dark: state.dark, getVar: config.getVar }),
    dimensions: rankings.dimensions,
    categories: rankings.categories,
    bases: rankings.bases,
    measureText: config.measureText,
    raf: config.raf,
  });

  async function draw(key) {
    const el = elements.get(key);
    const entry = REGISTRY[key];
    try {
      const plotly = await getPlotly();
      const input = INPUTS[entry.source](data, { models });
      const ok = await entry.render(el, input, optionsFor(entry), plotly);
      el.setAttribute('data-chart-status', ok ? 'ready' : 'empty');
    } catch {
      rendered.delete(key);
      el.setAttribute('data-chart-status', 'error');
    }
  }
  // Draws for one chart run in order so a stale draw can never overwrite a newer one.
  function queue(key) {
    chains.set(key, (chains.get(key) ?? Promise.resolve()).then(() => draw(key)));
  }
  function ensure(key) {
    if (!REGISTRY[key] || !elements.has(key) || rendered.has(key)) return;
    rendered.add(key);
    queue(key);
  }
  const refresh = () => [...rendered].forEach(queue);

  const observer = (config.observer ?? defaultObserver)((entries) => {
    entries.forEach((entry) => { if (entry.isIntersecting) ensure(entry.target.getAttribute('data-chart')); });
  });
  elements.forEach((el) => observer.observe(el));

  const onState = (event) => {
    const detail = event.detail ?? {};
    if (detail.basis !== undefined) state.basis = detail.basis;
    if (detail.costWeightPct !== undefined) state.costWeightPct = detail.costWeightPct;
    if (detail.models !== undefined) models = detail.models;
    refresh();
  };
  const onTheme = (event) => {
    state.dark = Boolean(event.detail?.dark);
    refresh();
  };
  root.addEventListener('vr:state', onState);
  root.addEventListener('vr:theme', onTheme);

  // Chart tabs: <button data-chart-tab="key" aria-selected> and panels <div data-chart-panel="key">.
  const tabs = [...root.querySelectorAll('[data-chart-tab]')];
  const panels = [...root.querySelectorAll('[data-chart-panel]')];
  const tabKeys = tabs.map((tab) => tab.getAttribute('data-chart-tab'));
  // `reveal` keeps the selected tab visible when the strip scrolls sideways on a narrow screen. The first tab
  // sits at the strip's start, so selecting it on load must not scroll the page to the chart.
  function selectTab(key, notify, reveal = notify) {
    tabs.forEach((tab, i) => {
      const selected = tabKeys[i] === key;
      tab.setAttribute('aria-selected', String(selected));
      tab.setAttribute('tabindex', selected ? '0' : '-1');
      if (selected && reveal) tab.scrollIntoView({ block: 'nearest', inline: 'center' });
    });
    panels.forEach((panel) => { panel.hidden = panel.getAttribute('data-chart-panel') !== key; });
    ensure(key);
    if (notify) config.onChartChange(key);
  }
  tabs.forEach((tab, i) => {
    tab.addEventListener('click', () => selectTab(tabKeys[i], true));
    tab.addEventListener('keydown', (event) => {
      const step = { ArrowRight: 1, ArrowLeft: -1 }[event.key];
      if (step === undefined) return;
      event.preventDefault();
      const next = (i + step + tabs.length) % tabs.length;
      selectTab(tabKeys[next], true);
      tabs[next].focus();
    });
  });
  if (tabs.length) {
    const selected = tabs.find((tab) => tab.getAttribute('aria-selected') === 'true');
    const wanted = tabKeys.includes(config.initialChart) ? config.initialChart : (selected ?? tabs[0]).getAttribute('data-chart-tab');
    selectTab(wanted, false, wanted !== tabKeys[0]);
  }

  return {
    show: ensure,
    rendered: () => [...rendered],
    state: () => ({ ...state }),
    idle: () => Promise.all(chains.values()),
    destroy() {
      root.removeEventListener('vr:state', onState);
      root.removeEventListener('vr:theme', onTheme);
      observer.disconnect();
    },
  };
}
