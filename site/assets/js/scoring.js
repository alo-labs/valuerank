// Pure scoring: client-side port of the cost-weight renormalisation rule.
import { fmtScore } from './format.js';

export const COST_KEY = 'costComposite';

const clamp = (n, lo, hi) => Math.min(hi, Math.max(lo, n));
const has = (v) => v !== null && v !== undefined;
const round1 = (n) => Math.round(n * 10) / 10;
const byName = (a, b) => a.name.localeCompare(b.name);

function dimValue(model, dim, basis) {
  return dim.key === COST_KEY ? model.costDims[basis] : model.dims[dim.key];
}

/** Weight fractions per dimension key: available priorities only, summing to 1 (or all zero). */
export function effectiveWeights(model, dimensions, costWeightPct, basis = 'plan') {
  const defaultCost = dimensions.find((d) => d.key === COST_KEY).weightPct / 100;
  const requested = clamp(costWeightPct, 0, 100) / 100;
  const scale = defaultCost < 1 ? (1 - requested) / (1 - defaultCost) : 0;
  const raw = dimensions.map((d) => {
    if (!has(dimValue(model, d, basis))) return 0;
    return d.key === COST_KEY ? requested : (d.weightPct / 100) * scale;
  });
  const total = raw.reduce((sum, w) => sum + w, 0);
  return Object.fromEntries(dimensions.map((d, i) => [d.key, total > 0 ? raw[i] / total : 0]));
}

/** Weighted score rounded to one decimal, or null when no weighted dimension is available. */
export function compositeScore(model, dimensions, basis, costWeightPct) {
  const weights = effectiveWeights(model, dimensions, costWeightPct, basis);
  let sum = 0;
  let total = 0;
  for (const d of dimensions) {
    const w = weights[d.key];
    if (w <= 0) continue;
    sum += dimValue(model, d, basis) * w;
    total += w;
  }
  return total > 0 ? round1(sum / total) : null;
}

/** Copies of the models with overall[basis] and rank[basis] recomputed; ranking is score desc then name. */
export function recompute(models, dimensions, basis, costWeightPct) {
  const scored = models.map((m) => ({
    ...m,
    overall: { ...m.overall, [basis]: m.rankingEligible ? compositeScore(m, dimensions, basis, costWeightPct) : null },
    rank: { ...m.rank, [basis]: null },
  }));
  scored
    .filter((m) => m.overall[basis] !== null)
    .sort((a, b) => b.overall[basis] - a.overall[basis] || byName(a, b))
    .forEach((m, i) => { m.rank[basis] = i + 1; });
  return scored;
}

/** Cost in the unit of the basis; a model without a plan route shows its API-derived comparable plan cost. */
export function costValue(model, basis) {
  if (basis === 'api') return model.cost.apiUsd;
  return model.cost.planUsdPerPoint ?? model.cost.planComparableUsdPerPoint ?? null;
}

/** Ranked models not dominated on (cost USD, overall), cheapest first. */
export function paretoFront(models, basis) {
  const rows = models
    .filter((m) => has(m.overall[basis]) && has(costValue(m, basis)))
    .sort((a, b) => costValue(a, basis) - costValue(b, basis) || b.overall[basis] - a.overall[basis]);
  const front = [];
  let best = -Infinity;
  for (const m of rows) {
    if (m.overall[basis] > best) {
      front.push(m);
      best = m.overall[basis];
    }
  }
  return front;
}

export function costTier(costScore) {
  if (!has(costScore)) return null;
  const penalty = 100 - costScore;
  if (penalty <= 15) return 'Budget';
  if (penalty <= 22) return 'Near-Budget';
  if (penalty <= 35) return 'Mid-Range';
  if (penalty <= 55) return 'Premium';
  return 'Expensive';
}

const leader = (models, score) => models.reduce(
  (best, m) => (best === null || score(m) > score(best) || (score(m) === score(best) && byName(m, best) < 0) ? m : best),
  null,
);
const pick = (m, reason) => (m ? { slug: m.slug, reason } : null);

/** The three picks for a basis, computed from the (possibly recomputed) models. */
export function picks(models, basis) {
  const ranked = models.filter((m) => has(m.overall[basis]));
  const overall = (m) => m.overall[basis];
  const best = leader(ranked, overall);
  const withQuality = ranked.filter((m) => has(m.quality));
  const topQuality = leader(withQuality, (m) => m.quality);
  const cheap = ranked
    .filter((m) => has(m.costDims[basis]))
    .sort((a, b) => b.costDims[basis] - a.costDims[basis])
    .slice(0, Math.ceil(ranked.filter((m) => has(m.costDims[basis])).length / 3));
  const budget = leader(cheap, overall);
  return {
    value: pick(best, best && `${best.name} has the highest overall score on this basis (${fmtScore(overall(best))}).`),
    quality: pick(topQuality, topQuality && `${topQuality.name} has the highest quality score (${fmtScore(topQuality.quality)}), before cost is considered.`),
    budget: pick(budget, budget && `${budget.name} has the best overall score (${fmtScore(overall(budget))}) among the cheapest third of models.`),
  };
}
