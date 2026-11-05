// Pure scoring: client-side port of the methodology v3 value rule (valuerank.anchors.value_score).
import { fmtScore } from './format.js';

export const COST_KEY = 'costComposite';

const clamp = (n, lo, hi) => Math.min(hi, Math.max(lo, n));
const has = (v) => v !== null && v !== undefined;
const byName = (a, b) => a.name.localeCompare(b.name);

/**
 * Value on a basis at a cost weight (percent): w x cost score + (1 - w) x quality, unrounded, with the
 * same arithmetic as the build. A model without a cost score or a quality score has no value score.
 */
export function compositeScore(model, basis, costWeightPct) {
  const cost = model.costDims[basis];
  if (!has(cost) || !has(model.quality)) return null;
  const w = clamp(costWeightPct, 0, 100) / 100;
  return w * cost + (1 - w) * model.quality;
}

/** Competition ranks (1 = best): equal values share the better rank. */
export function competitionRanks(values) {
  const scored = values.filter(has);
  return values.map((v) => (has(v) ? 1 + scored.filter((o) => o > v).length : null));
}

/** Copies of the models with overall[basis] and rank[basis] recomputed; unranked models keep null. */
export function recompute(models, basis, costWeightPct) {
  const scored = models.map((m) => ({
    ...m,
    overall: { ...m.overall, [basis]: m.rankingEligible ? compositeScore(m, basis, costWeightPct) : null },
    rank: { ...m.rank },
  }));
  const ranks = competitionRanks(scored.map((m) => m.overall[basis]));
  scored.forEach((m, i) => { m.rank[basis] = ranks[i]; });
  return scored;
}

/** USD per basket run on the basis (the Plan cost is the API cost when no route is admitted). */
export function costValue(model, basis) {
  return basis === 'api' ? model.cost.apiUsd : model.cost.planUsd;
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
const rankOn = (models, basis, m) => 1 + models.filter((o) => o.overall[basis] > m.overall[basis]).length;
// O17: a subset-cost model is scored on its own workload; its ordering against full-basket models is not identified.
const pick = (m, label, reason, score, unit) => ({
  slug: m.slug, label, reason: m.cost?.subset ? `${reason} Subset cost: cross-workload ordering not identified.` : reason, score, unit,
});

// Second card: rank 1 on the other basis, else the quality leader, else the runner-up (never the first card's model).
function otherPick(ranked, value, basis, bases) {
  const otherKey = Object.keys(bases).find((k) => k !== basis);
  const label = bases[basis].label;
  const lead = leader(ranked.filter((m) => has(m.overall[otherKey])), (m) => m.overall[otherKey]);
  if (lead && lead !== value) {
    const phrase = bases[otherKey].pickPhrase;
    return pick(lead, bases[otherKey].pickLabel, `${lead.name} ranks #1 ${phrase} and #${rankOn(ranked, basis, lead)} in the ${label}.`, lead.overall[otherKey], `overall ${phrase}`);
  }
  const topQuality = leader(ranked.filter((m) => has(m.quality)), (m) => m.quality);
  if (topQuality && topQuality !== value) {
    return pick(topQuality, 'Best quality, any cost', `${topQuality.name} has the best quality score (${fmtScore(topQuality.quality)}) before cost; it ranks #${rankOn(ranked, basis, topQuality)} in the ${label}.`, topQuality.quality, 'quality');
  }
  const runnerUp = leader(ranked.filter((m) => m !== value), (m) => m.overall[basis]);
  return runnerUp && pick(runnerUp, 'Runner-up overall', `${runnerUp.name} is the runner-up in the ${label} at ${fmtScore(runnerUp.overall[basis])}.`, runnerUp.overall[basis], 'overall');
}

/**
 * The three picks for a basis, computed from the (possibly recomputed) models, which must carry
 * overall scores for both bases: best overall value, best on the other basis, best on a budget.
 * Same rule as valuerank/site/picks.py.
 */
export function picks(models, basis, bases) {
  const ranked = models.filter((m) => has(m.overall[basis]));
  const overall = (m) => m.overall[basis];
  const best = leader(ranked, overall);
  if (!best) return { value: null, other: null, budget: null };
  const other = otherPick(ranked, best, basis, bases);
  const priced = ranked.filter((m) => has(m.costDims[basis])).sort((a, b) => b.costDims[basis] - a.costDims[basis]);
  let cheap = priced.slice(0, Math.ceil(priced.length / 3));
  if (cheap.length > 1) {
    // Two or more priced models means two or more ranked ones, so the second pick exists.
    const unpicked = cheap.filter((m) => m !== best && m.slug !== other.slug);
    cheap = unpicked.length ? unpicked : cheap;
  }
  const budget = leader(cheap, overall);
  return {
    value: pick(best, 'Best overall value', `${best.name} has the highest overall score in the ${bases[basis].label} at ${fmtScore(overall(best))}.`, overall(best), 'overall'),
    other,
    budget: budget && pick(budget, 'Best on a budget', `${budget.name} scores best overall (${fmtScore(overall(budget))}) among the cheapest third of models.`, overall(budget), 'overall'),
  };
}
