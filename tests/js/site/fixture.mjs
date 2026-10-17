// Hand-built fixture with the rankings.json shape. Committed overall/rank values were
// calculated by hand from the weights below (cost 20, a 48, b 32).
export const dimensions = [
  { key: 'costComposite', label: 'Cost', category: 'cost', weightPct: 20, higherBetter: false },
  { key: 'a', label: 'Alpha bench', category: 'code', weightPct: 48, higherBetter: true },
  { key: 'b', label: 'Beta bench', category: 'rely', weightPct: 32, higherBetter: true },
];

const base = (o) => ({
  rankingEligible: true, exclusionReasons: [], aaUrl: '#', raw: {}, grade: 'measured',
  pareto: { api: false, plan: false }, tier: 'Mid-Range', speed: null,
  coverage: { pct: 100, availablePriority: 100, totalPriority: 100, missing: [] },
  intelligenceIndex: { value: 50, status: 'measured' },
  cost: { apiUsd: 100, planUsdPerRun: 10, planUsdPerPoint: 0.5, fallback: null, route: { planLabel: 'Plan X' } },
  ...o,
});

export const models = [
  base({
    slug: 'alpha', name: 'Alpha', shortName: 'Alpha', developer: 'Acme',
    rank: { api: 2, plan: 1 }, overall: { api: 67.6, plan: 71.6 }, quality: 70.4, qualityRank: 2,
    dims: { a: 80, b: 60 }, costDims: { api: 50, plan: 70 },
  }),
  base({
    slug: 'beta', name: 'Beta', shortName: 'Beta', developer: 'Bolt AI', grade: 'estimate',
    rank: { api: 1, plan: 2 }, overall: { api: 75.3, plan: 69.4 }, quality: 90, qualityRank: 1,
    dims: { a: 90, b: null }, costDims: { api: 40, plan: 20 },
    coverage: { pct: 68, availablePriority: 68, totalPriority: 100, missing: ['Beta bench'] },
    cost: { apiUsd: 2500, planUsdPerRun: 40, planUsdPerPoint: null, planComparableUsdPerPoint: 2.25, fallback: 'api', route: null },
    speed: 80,
  }),
  base({
    slug: 'gamma', name: 'Gamma', shortName: 'Gamma', developer: 'Acme', grade: 'assumption',
    rank: { api: 3, plan: 3 }, overall: { api: 58, plan: 56 }, quality: 50, qualityRank: 3,
    dims: { a: 50, b: 50 }, costDims: { api: 90, plan: 80 },
  }),
  base({
    slug: 'delta', name: 'Delta', shortName: 'Delta', developer: 'Delta Labs', grade: 'claim', rankingEligible: false,
    exclusionReasons: ['no quality metrics'],
    rank: { api: null, plan: null }, overall: { api: null, plan: null }, quality: null, qualityRank: null,
    dims: { a: null, b: null }, costDims: { api: 60, plan: 60 },
    coverage: null, cost: { apiUsd: null, planUsdPerRun: null, planUsdPerPoint: null, fallback: null, route: null },
  }),
  base({
    slug: 'eps', name: 'Eps', shortName: 'Eps', developer: 'Delta Labs', grade: 'missing',
    rank: { api: null, plan: null }, overall: { api: null, plan: null }, quality: null, qualityRank: null,
    dims: { a: null, b: null }, costDims: { api: null, plan: null },
    coverage: { pct: 0, availablePriority: 0, totalPriority: 100, missing: ['all'] },
    cost: { apiUsd: null, planUsdPerRun: null, planUsdPerPoint: null, fallback: null, route: null },
  }),
];

export const data = {
  version: 'v9.9.9', publishDate: 'October 8, 2026', defaultBasis: 'plan', costWeightPct: 20,
  bases: {
    api: { label: 'API ranking', costLabel: 'API cost', costUnit: 'USD per Index run', description: 'api' },
    plan: { label: 'Plan ranking', costLabel: 'Plan cost', costUnit: 'USD per Index point', description: 'plan' },
  },
  dimensions,
  categories: { cost: 'Cost', code: 'Code', rely: 'Reliability' },
  models,
  picks: {
    plan: { value: { slug: 'alpha', reason: 'committed value' }, quality: { slug: 'beta', reason: 'committed quality' }, budget: { slug: 'gamma', reason: 'committed budget' } },
    api: { value: { slug: 'beta', reason: 'committed api value' }, quality: { slug: 'beta', reason: 'q' }, budget: { slug: 'gamma', reason: 'b' } },
  },
};
