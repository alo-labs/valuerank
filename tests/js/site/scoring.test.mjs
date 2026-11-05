import test from 'node:test';
import assert from 'node:assert/strict';
import {
  compositeScore, competitionRanks, recompute, paretoFront, costTier, costValue, picks, COST_KEY,
} from '../../../valuerank/site/assets/js/scoring.js';
import { models } from './fixture.mjs';

const byName = (n) => models.find((m) => m.slug === n);
const near = (a, b) => assert.ok(Math.abs(a - b) < 1e-9, `${a} !== ${b}`);

test('compositeScore is the fixed cost share plus the quality share, unrounded', () => {
  near(compositeScore(byName('alpha'), 'api', 20), 67.6);
  near(compositeScore(byName('alpha'), 'plan', 20), 71.6);
  near(compositeScore(byName('beta'), 'api', 20), 75.3);
  near(compositeScore(byName('alpha'), 'api', 50), 61);
  near(compositeScore(byName('alpha'), 'api', 0), 72);
  near(compositeScore(byName('alpha'), 'api', 100), 50);
  assert.equal(COST_KEY, 'costComposite');
});

test('compositeScore uses the build arithmetic, so the default weight reproduces committed values bit for bit', () => {
  const model = { quality: 61.32724120424232, costDims: { api: 57.32402943766114 } };
  assert.equal(compositeScore(model, 'api', 25), 0.25 * 57.32402943766114 + (1 - 0.25) * 61.32724120424232);
});

test('a requested weight outside 0-100 is clamped', () => {
  near(compositeScore(byName('alpha'), 'api', 500), 50);
  near(compositeScore(byName('alpha'), 'api', -3), 72);
});

test('no cost score or no quality score means no value score', () => {
  assert.equal(compositeScore({ quality: 80, costDims: { api: null } }, 'api', 25), null);
  assert.equal(compositeScore({ quality: null, costDims: { api: 60 } }, 'api', 25), null);
  assert.equal(compositeScore(byName('eps'), 'api', 20), null);
});

test('competitionRanks share the better rank and skip missing values', () => {
  assert.deepEqual(competitionRanks([10, 50, 10, null, undefined]), [2, 1, 2, null, null]);
  assert.deepEqual(competitionRanks([]), []);
});

test('recompute reproduces the committed overall and rank for both bases at the default weight', () => {
  for (const basis of ['api', 'plan']) {
    const out = recompute(models, basis, 20);
    for (const m of out) {
      const orig = byName(m.slug);
      if (orig.overall[basis] === null) assert.equal(m.overall[basis], null);
      else near(m.overall[basis], orig.overall[basis]);
      assert.equal(m.rank[basis], orig.rank[basis], `${m.slug} rank ${basis}`);
    }
  }
});

test('recompute does not mutate input and leaves the other basis untouched', () => {
  const before = JSON.stringify(models);
  const out = recompute(models, 'api', 90);
  assert.equal(JSON.stringify(models), before);
  assert.equal(out.find((m) => m.slug === 'alpha').overall.plan, 71.6);
  assert.equal(out.find((m) => m.slug === 'alpha').rank.plan, 1);
});

test('moving the cost weight changes ranks; equal values share a rank; ineligible models stay unranked', () => {
  // At 100% cost: gamma (90) > alpha (50) > beta (40.5) on api.
  const out = recompute(models, 'api', 100);
  const r = Object.fromEntries(out.map((m) => [m.slug, m.rank.api]));
  assert.deepEqual(r, { gamma: 1, alpha: 2, beta: 3, delta: null, eps: null });
  assert.equal(out.find((m) => m.slug === 'delta').overall.api, null);
  const tie = (slug, name) => ({ slug, name, rankingEligible: true, quality: 50, costDims: { api: 50 }, overall: {}, rank: {} });
  const t = recompute([tie('z', 'Zed'), tie('y', 'Yak'), { ...tie('x', 'Xi'), quality: 10 }], 'api', 20);
  assert.deepEqual(t.map((m) => [m.slug, m.rank.api]), [['z', 1], ['y', 1], ['x', 3]]);
});

test('costValue reads the basis-specific USD per basket run', () => {
  assert.equal(costValue(byName('alpha'), 'api'), 100);
  assert.equal(costValue(byName('alpha'), 'plan'), 0.5);
  assert.equal(costValue(byName('beta'), 'plan'), 2500);
});

test('paretoFront keeps ranked models no cheaper-and-better model dominates, cheapest first', () => {
  const rows = [
    { slug: 'a', overall: { api: 60 }, cost: { apiUsd: 100 } },
    { slug: 'b', overall: { api: 70 }, cost: { apiUsd: 200 } },
    { slug: 'c', overall: { api: 65 }, cost: { apiUsd: 300 } },
    { slug: 'd', overall: { api: 80 }, cost: { apiUsd: 200 } },
    { slug: 'e', overall: { api: null }, cost: { apiUsd: 1 } },
    { slug: 'f', overall: { api: 90 }, cost: { apiUsd: null } },
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

test('a subset-cost pick says its cross-workload ordering is not identified', () => {
  const subset = { ...rival('s', 'Sub', 90, 90, 50, 10, 10), cost: { subset: true } };
  const p = picks([subset, rival('t', 'Tee', 80, 80, 60, 20, 20)], 'api', BASES);
  assert.ok(p.value.reason.endsWith('Subset cost: cross-workload ordering not identified.'));
  assert.ok(!p.other.reason.includes('Subset cost'));
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
