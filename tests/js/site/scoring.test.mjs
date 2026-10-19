import test from 'node:test';
import assert from 'node:assert/strict';
import {
  effectiveWeights, compositeScore, recompute, paretoFront, costTier, costValue, picks, COST_KEY,
} from '../../../valuerank/site/assets/js/scoring.js';
import { dimensions, models } from './fixture.mjs';

const byName = (n) => models.find((m) => m.slug === n);
const near = (a, b) => assert.ok(Math.abs(a - b) < 1e-9, `${a} !== ${b}`);

test('cost keeps its fixed share and quality renormalises over the available dimensions', () => {
  const w = effectiveWeights(byName('alpha'), dimensions, 20, 'api');
  near(w.costComposite, 0.2); near(w.a, 0.48); near(w.b, 0.32);
  // beta lacks b: cost stays at 20% and a takes the whole 80% quality share
  const w2 = effectiveWeights(byName('beta'), dimensions, 20, 'api');
  near(w2.costComposite, 0.2); near(w2.a, 0.8); assert.equal(w2.b, 0);
});

test('cost takes the requested weight and quality weights scale proportionally', () => {
  const w = effectiveWeights(byName('alpha'), dimensions, 50, 'api');
  near(w.costComposite, 0.5); near(w.a, 0.3); near(w.b, 0.2);
  const w0 = effectiveWeights(byName('alpha'), dimensions, 0, 'api');
  near(w0.costComposite, 0); near(w0.a, 0.6);
});

test('a requested weight outside 0-100 is clamped', () => {
  near(effectiveWeights(byName('alpha'), dimensions, 500, 'api').costComposite, 1);
  near(effectiveWeights(byName('alpha'), dimensions, -3, 'api').costComposite, 0);
});

test('default basis is plan and a 100% cost weight leaves no quality share', () => {
  const w = effectiveWeights(byName('alpha'), dimensions, 20);
  near(w.costComposite, 0.2);
  const w100 = effectiveWeights(byName('alpha'), dimensions, 100);
  near(w100.costComposite, 1); assert.equal(w100.a, 0); assert.equal(w100.b, 0);
  // Quality must carry some weight for a model to be scored at all, even at 100% cost.
  const all = [{ key: COST_KEY, weightPct: 100 }, { key: 'a', weightPct: 0 }];
  assert.deepEqual(effectiveWeights({ dims: { a: 5 }, costDims: { plan: 5 } }, all, 100), { [COST_KEY]: 0, a: 0 });
});

test('a model with no available dimension has all-zero weights', () => {
  const w = effectiveWeights(byName('eps'), dimensions, 20, 'api');
  assert.deepEqual(w, { costComposite: 0, a: 0, b: 0 });
});

test('compositeScore is the renormalised weighted mean rounded to one decimal', () => {
  assert.equal(compositeScore(byName('alpha'), dimensions, 'api', 20), 67.6);
  assert.equal(compositeScore(byName('alpha'), dimensions, 'plan', 20), 71.6);
  assert.equal(compositeScore(byName('beta'), dimensions, 'api', 20), 75.3);
  assert.equal(compositeScore(byName('alpha'), dimensions, 'api', 50), 61);
  assert.equal(compositeScore(byName('eps'), dimensions, 'api', 20), null);
});

test('a zero-weight available dimension does not make a model scoreable on its own', () => {
  const zero = [{ key: COST_KEY, weightPct: 20 }, { key: 'z', weightPct: 0 }];
  assert.equal(compositeScore({ dims: { z: 50 }, costDims: { api: 60 } }, zero, 'api', 20), null);
});

test('without a cost score a model is scored on quality alone at any cost weight', () => {
  const only = { dims: { a: 80, b: null }, costDims: { api: null } };
  assert.equal(compositeScore(only, dimensions, 'api', 100), 80);
  assert.equal(compositeScore(only, dimensions, 'api', 0), 80);
});

test('recompute reproduces the committed overall and rank for both bases at the default weight', () => {
  for (const basis of ['api', 'plan']) {
    const out = recompute(models, dimensions, basis, 20);
    for (const m of out) {
      const orig = byName(m.slug);
      assert.equal(m.overall[basis], orig.overall[basis], `${m.slug} overall ${basis}`);
      assert.equal(m.rank[basis], orig.rank[basis], `${m.slug} rank ${basis}`);
    }
  }
});

test('recompute does not mutate input and leaves the other basis untouched', () => {
  const before = JSON.stringify(models);
  const out = recompute(models, dimensions, 'api', 90);
  assert.equal(JSON.stringify(models), before);
  assert.equal(out.find((m) => m.slug === 'alpha').overall.plan, 71.6);
  assert.equal(out.find((m) => m.slug === 'alpha').rank.plan, 1);
});

test('moving the cost weight changes ranks; ties break by lower cost then name; ineligible models stay unranked', () => {
  // At 100% cost: gamma (90) > alpha (50) > beta (40) on api.
  const out = recompute(models, dimensions, 'api', 100);
  const r = Object.fromEntries(out.map((m) => [m.slug, m.rank.api]));
  assert.deepEqual(r, { gamma: 1, alpha: 2, beta: 3, delta: null, eps: null });
  assert.equal(out.find((m) => m.slug === 'delta').overall.api, null);
  const tie = (slug, name, usd) => ({
    slug, name, rankingEligible: true, dims: { a: 50, b: 50 }, costDims: { api: 50 }, cost: { apiUsdPerPoint: usd }, overall: {}, rank: {},
  });
  const t = recompute([tie('z', 'Zed', 5), tie('y', 'Yak', 5)], dimensions, 'api', 20);
  assert.deepEqual(t.map((m) => [m.slug, m.rank.api]), [['z', 2], ['y', 1]]);
  const priced = recompute([tie('y', 'Yak', null), tie('x', 'Xi', 9), tie('z', 'Zed', 3)], dimensions, 'api', 20);
  assert.deepEqual(priced.map((m) => [m.slug, m.rank.api]), [['y', 3], ['x', 2], ['z', 1]]);
});

test('costValue reads the basis-specific USD per Index point', () => {
  assert.equal(costValue(byName('beta'), 'api'), 2500);
  assert.equal(costValue(byName('beta'), 'plan'), 2.25);
});

test('paretoFront keeps ranked models no cheaper-and-better model dominates, cheapest first', () => {
  const rows = [
    { slug: 'a', overall: { api: 60 }, cost: { apiUsdPerPoint: 100 } },
    { slug: 'b', overall: { api: 70 }, cost: { apiUsdPerPoint: 200 } },
    { slug: 'c', overall: { api: 65 }, cost: { apiUsdPerPoint: 300 } },
    { slug: 'd', overall: { api: 80 }, cost: { apiUsdPerPoint: 200 } },
    { slug: 'e', overall: { api: null }, cost: { apiUsdPerPoint: 1 } },
    { slug: 'f', overall: { api: 90 }, cost: { apiUsdPerPoint: null } },
  ];
  assert.deepEqual(paretoFront(rows, 'api').map((m) => m.slug), ['a', 'd']);
});

test('costTier maps cost scores to the legacy tiers', () => {
  assert.equal(costTier(90), 'Budget');
  assert.equal(costTier(85), 'Budget');
  assert.equal(costTier(80), 'Near-Budget');
  assert.equal(costTier(70), 'Mid-Range');
  assert.equal(costTier(50), 'Premium');
  assert.equal(costTier(30), 'Expensive');
  assert.equal(costTier(null), null);
});

const BASES = {
  api: { label: 'API ranking', pickLabel: 'Best at API rates', pickPhrase: 'at API rates' },
  plan: { label: 'Plan ranking', pickLabel: 'Best on a subscription', pickPhrase: 'on a subscription' },
};
const rival = (slug, name, api, plan, quality, costApi, costPlan) => ({
  slug, name, overall: { api, plan }, quality, costDims: { api: costApi, plan: costPlan },
});
const slugsOf = (p) => [p.value?.slug, p.other?.slug, p.budget?.slug];

test('picks show the leader, the other basis leader and a budget model with data-driven labels', () => {
  const api = picks(models, 'api', BASES);
  assert.deepEqual(slugsOf(api), ['beta', 'alpha', 'gamma']);
  assert.deepEqual([api.value.label, api.other.label, api.budget.label], ['Best overall value', 'Best on a subscription', 'Best on a budget']);
  assert.match(api.value.reason, /Beta has the highest overall score in the API ranking at 75\.3/);
  assert.equal(api.other.reason, 'Alpha ranks #1 on a subscription and #2 in the API ranking.');
  assert.deepEqual([api.other.score, api.other.unit], [71.6, 'overall on a subscription']);
  assert.match(api.budget.reason, /Gamma .*58\.0/);
  assert.deepEqual([api.budget.score, api.budget.unit], [58, 'overall']);
  const plan = picks(models, 'plan', BASES);
  assert.deepEqual(slugsOf(plan), ['alpha', 'beta', 'gamma']);
  assert.equal(plan.other.label, 'Best at API rates');
  assert.equal(plan.other.reason, 'Beta ranks #1 at API rates and #2 in the Plan ranking.');
  for (const p of [...Object.values(api), ...Object.values(plan)]) assert.ok(p.reason.split(' ').length < 25);
});

test('the second pick falls back to the quality leader, then to the runner-up', () => {
  const sameLeader = [rival('a', 'Aye', 90, 90, 50, 0, 0), rival('b', 'Bee', 80, 80, 70, 50, 50), rival('c', 'Sea', 70, 70, 60, 100, 100)];
  const viaQuality = picks(sameLeader, 'api', BASES);
  assert.deepEqual(slugsOf(viaQuality), ['a', 'b', 'c']);
  assert.equal(viaQuality.other.label, 'Best quality, any cost');
  assert.match(viaQuality.other.reason, /Bee has the best quality score \(70\.0\) before cost; it ranks #2 in the API ranking/);
  assert.deepEqual([viaQuality.other.score, viaQuality.other.unit], [70, 'quality']);
  const alsoLeader = [rival('a', 'Aye', 90, 90, 90, 0, 0), rival('b', 'Bee', 80, 80, 70, 50, 50), rival('c', 'Sea', 70, 70, 60, 100, 100)];
  const runnerUp = picks(alsoLeader, 'plan', BASES);
  assert.deepEqual(slugsOf(runnerUp), ['a', 'b', 'c']);
  assert.equal(runnerUp.other.label, 'Runner-up overall');
  assert.equal(runnerUp.other.reason, 'Bee is the runner-up in the Plan ranking at 80.0.');
  assert.deepEqual([runnerUp.other.score, runnerUp.other.unit], [80, 'overall']);
  const noQuality = [rival('a', 'Aye', 90, 90, null, 0, 0), rival('b', 'Bee', 80, 80, null, 50, 50)];
  assert.equal(picks(noQuality, 'api', BASES).other.slug, 'b');
});

test('the budget pick skips models already picked, unless that would leave nothing', () => {
  const four = [rival('a', 'Aye', 90, 90, 90, 100, 100), rival('b', 'Bee', 80, 80, 70, 10, 10), rival('c', 'Sea', 70, 70, 60, 90, 90), rival('d', 'Dee', 60, 60, 50, 0, 0)];
  assert.deepEqual(slugsOf(picks(four, 'api', BASES)), ['a', 'b', 'c']);
  const crowded = [rival('a', 'Aye', 90, 80, 90, 100, 100), rival('b', 'Bee', 80, 90, 70, 90, 90), rival('c', 'Sea', 70, 70, 60, 0, 0), rival('d', 'Dee', 60, 60, 50, 5, 5)];
  assert.deepEqual(slugsOf(picks(crowded, 'api', BASES)), ['a', 'b', 'a']);
});

test('picks returns nulls when nothing is rankable and no second pick for a lone model', () => {
  assert.deepEqual(picks([byName('eps')], 'api', BASES), { value: null, other: null, budget: null });
  const lone = picks([rival('x', 'X', 50, 50, 50, 10, 10)], 'api', BASES);
  assert.deepEqual(slugsOf(lone), ['x', undefined, 'x']);
  assert.equal(lone.other, null);
});

test('picks tolerate ranked models without a cost score or quality', () => {
  const m = [{ slug: 'x', name: 'X', overall: { api: 50, plan: 50 }, quality: null, costDims: { api: null, plan: null } }];
  const p = picks(m, 'api', BASES);
  assert.equal(p.value.slug, 'x');
  assert.equal(p.other, null);
  assert.equal(p.budget, null);
});

test('picks break exact score ties by name', () => {
  const m = [
    rival('z', 'Zed', 50, 50, 50, 10, 10),
    rival('a', 'Aye', 50, 50, 50, 10, 10),
    rival('q', 'Qux', 40, 40, 50, 10, 10),
  ];
  const p = picks(m, 'api', BASES);
  assert.deepEqual([p.value.slug, p.other.slug], ['a', 'z']);
  assert.equal(p.other.reason, 'Zed is the runner-up in the API ranking at 50.0.');
  const rev = picks([...m].reverse(), 'api', BASES);
  assert.deepEqual([rev.value.slug, rev.other.slug], ['a', 'z']);
});
