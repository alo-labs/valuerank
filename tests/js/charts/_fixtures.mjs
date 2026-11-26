const model = (slug, over) => ({
  slug, name: slug.toUpperCase(), shortName: slug, developer: 'OpenAI', tier: 'Budget', speed: null,
  overall: { api: null, plan: null }, rank: { api: null, plan: null }, quality: null, qualityRank: null,
  dims: {}, costDims: { api: null, plan: null }, cost: { apiUsd: null, planUsd: null }, pareto: { api: false, plan: false },
  ...over,
});

export const models = [
  model('alpha', {
    developer: 'OpenAI', tier: 'Near-Budget', speed: 86, quality: 74.6, qualityRank: 2,
    overall: { api: 74.3, plan: 75.7 }, rank: { api: 1, plan: 2 },
    dims: { deepswe: 100, bug: 93.3, hle: null }, costDims: { api: 73.3, plan: 80 },
    cost: { apiUsd: 1081.55, planUsd: 101.08 }, pareto: { api: true, plan: true },
  }),
  model('beta', {
    developer: 'Anthropic', tier: 'Premium', speed: 40, quality: 80, qualityRank: 1,
    overall: { api: 70, plan: 78 }, rank: { api: 2, plan: 1 },
    dims: { deepswe: 90, bug: 80, hle: 60 }, costDims: { api: 40, plan: 90 },
    cost: { apiUsd: 3000, planUsd: 62.4 }, pareto: { api: true, plan: false },
  }),
  model('gamma', {
    developer: 'Unknown Lab', tier: 'Mystery', speed: null, quality: 60, qualityRank: 3,
    overall: { api: 60, plan: 61 }, rank: { api: 3, plan: 3 },
    dims: { deepswe: 50, bug: 50, hle: 50 }, costDims: { api: 55, plan: 50 },
    cost: { apiUsd: 500, planUsd: 120 }, pareto: { api: false, plan: false },
  }),
  model('delta', {
    developer: 'DeepSeek', tier: 'Budget', speed: 40, quality: 50, qualityRank: 4,
    overall: { api: 55, plan: 52 }, rank: { api: 4, plan: 5 },
    dims: { deepswe: 20, bug: 30, hle: 10 }, costDims: { api: 90, plan: 20 },
    cost: { apiUsd: 100, planUsd: 160 }, pareto: { api: false, plan: false },
  }),
  model('omega', { name: 'Omega (unranked)' }),
];

export const dimensions = [
  { key: 'costComposite', label: 'Cost', category: 'cost', weightPct: 20 },
  { key: 'deepswe', label: 'DeepSWE', category: 'code', weightPct: 40 },
  { key: 'bug', label: 'Bug Hunt', category: 'code', weightPct: 20 },
  { key: 'hle', label: 'HLE', category: 'intel', weightPct: 20 },
];
export const categories = { cost: 'Cost', rely: 'Reliability', code: 'Code/Agentic', intel: 'Intelligence' };
export const bases = { api: { label: 'API ranking', costLabel: 'API cost' }, plan: { label: 'Plan ranking', costLabel: 'Plan cost' } };
export const baseOptions = { basis: 'plan', dimensions, categories, bases, costWeightPct: 20 };

export const changelog = {
  versions: [
    { version: 'v1.2', date: '2026-10-08', rankChanges: [{ slug: 'alpha', from: 1, to: 2 }, { slug: 'beta', from: null, to: 1 }] },
    { version: 'v1.1', date: '2026-09-01', rankChanges: [{ slug: 'alpha', from: 2, to: 1 }] },
    { version: 'v1.0', date: '2026-08-01', ranks: { alpha: 2, delta: 3 }, rankChanges: [] },
  ],
};

export const livebench = [
  { id: 'a', name: 'Model A', livebenchModel: 'a-x', overallScore: 70, instructionFollowingScore: 80, costPerSuccessfulTaskUsd: 0.05, pareto: true },
  { id: 'b', name: 'Model B', livebenchModel: 'b-x', overallScore: 60, instructionFollowingScore: 70, costPerSuccessfulTaskUsd: 0.5, pareto: false },
  { id: 'c', name: 'Model C', livebenchModel: 'c-x', overallScore: 80, instructionFollowingScore: 90, costPerSuccessfulTaskUsd: 2, pareto: true },
  { id: 'd', name: 'No cost', overallScore: 50, costPerSuccessfulTaskUsd: null, pareto: false },
];

export const tb4Rows = [
  { model: 'A (max)', baseModel: 'A', agent: 'Codex', resolutionRatePct: 58.2, uncertaintyPct: 2.8, tokens: '1.5B', rankLabel: '1', costUsd: 3300 },
  { model: 'B (high)', baseModel: 'B', agent: 'Claude', resolutionRatePct: 40, uncertaintyPct: 3, tokens: '1B', rankLabel: '2', costUsd: 1000 },
  { model: 'C (low)', baseModel: 'C', agent: 'Gemini', resolutionRatePct: 35, uncertaintyPct: 3, tokens: '1B', rankLabel: '3', costUsd: 1500 },
  { model: 'D (free)', baseModel: 'D', agent: 'X', resolutionRatePct: 10, uncertaintyPct: 1, tokens: '1M', rankLabel: '4', costUsd: 0 },
];

/** Fake graph div that reports a rendered Plotly layout and annotation text boxes. */
export function createPlotDiv({ boxes = [], rect = { left: 0, right: 1000, top: 0, bottom: 600 }, parent = null, layout } = {}) {
  const axis = (type) => ({ type, _offset: 50, _length: 800, l2p: (v) => v * 8 });
  const div = {
    attrs: {}, parentNode: parent, textContent: '',
    _fullLayout: layout === undefined ? { width: 1000, height: 600, _size: { l: 50, t: 50, w: 800, h: 500 }, xaxis: axis('linear'), yaxis: axis('linear') } : layout,
    setAttribute(name, value) { this.attrs[name] = value; },
    getBoundingClientRect: () => rect,
    boxes,
    querySelectorAll() { return this.boxes.map((box) => ({ textContent: box.text, getBoundingClientRect: () => box.rect })); },
  };
  return div;
}
