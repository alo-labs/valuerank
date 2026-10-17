import test from 'node:test';
import assert from 'node:assert/strict';
import {
  effectiveWeights, compositeScore, recompute, paretoFront, costTier, costValue, picks, COST_KEY,
} from '../../../valuerank/site/assets/js/scoring.js';
import { dimensions, models } from './fixture.mjs';

const byName = (n) => models.find((m) => m.slug === n);
const near = (a, b) => assert.ok(Math.abs(a - b) < 1e-9, `${a} !== ${b}`);

test('weights renormalise to 1 over the available dimensions at the default cost weight', () => {
  const w = effectiveWeights(byName('alpha'), dimensions, 20, 'api');
  near(w.costComposite, 0.2); near(w.a, 0.48); near(w.b, 0.32);
  const w2 = effectiveWeights(byName('beta'), dimensions, 20, 'api');
  near(w2.costComposite, 20 / 68); near(w2.a, 48 / 68); assert.equal(w2.b, 0);
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

test('default basis is plan and a 100% default cost weight yields zero quality scale', () => {
  const w = effectiveWeights(byName('alpha'), dimensions, 20);
  near(w.costComposite, 0.2);
  const all = [{ key: COST_KEY, weightPct: 100 }, { key: 'a', weightPct: 0 }];
  const w100 = effectiveWeights({ dims: { a: 5 }, costDims: { plan: 5 } }, all, 100);
  near(w100.costComposite, 1); assert.equal(w100.a, 0);
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
  const only = { dims: { a: 80, b: null }, costDims: { api: null } };
  assert.equal(compositeScore(only, dimensions, 'api', 100), null);
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

test('moving the cost weight changes ranks; ties break by name; ineligible models stay unranked', () => {
  // At 100% cost: gamma (90) > alpha (50) > beta (40) on api.
  const out = recompute(models, dimensions, 'api', 100);
  const r = Object.fromEntries(out.map((m) => [m.slug, m.rank.api]));
  assert.deepEqual(r, { gamma: 1, alpha: 2, beta: 3, delta: null, eps: null });
  assert.equal(out.find((m) => m.slug === 'delta').overall.api, null);
  const tied = [
    { slug: 'z', name: 'Zed', rankingEligible: true, dims: { a: 50, b: 50 }, costDims: { api: 50 }, overall: {}, rank: {} },
    { slug: 'y', name: 'Yak', rankingEligible: true, dims: { a: 50, b: 50 }, costDims: { api: 50 }, overall: {}, rank: {} },
  ];
  const t = recompute(tied, dimensions, 'api', 20);
  assert.deepEqual(t.map((m) => [m.slug, m.rank.api]), [['z', 2], ['y', 1]]);
});

test('costValue reads the basis-specific USD figure', () => {
  assert.equal(costValue(byName('beta'), 'api'), 2500);
  assert.equal(costValue(byName('beta'), 'plan'), 2.25);
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

test('picks selects value, quality and budget leaders with reasons from the data', () => {
  const p = picks(models, 'api');
  assert.equal(p.value.slug, 'beta');
  assert.match(p.value.reason, /Beta .*75\.3/);
  assert.equal(p.quality.slug, 'beta');
  assert.match(p.quality.reason, /90\.0/);
  // eligible: alpha(cost 50), beta(40), gamma(90): cheapest third = gamma
  assert.equal(p.budget.slug, 'gamma');
  assert.match(p.budget.reason, /Gamma .*58\.0/);
});

test('picks returns nulls when nothing is rankable', () => {
  const p = picks([byName('eps')], 'api');
  assert.deepEqual(p, { value: null, quality: null, budget: null });
});

test('picks tolerates ranked models without a cost score or quality', () => {
  const m = [{ slug: 'x', name: 'X', overall: { api: 50 }, quality: null, costDims: { api: null } }];
  const p = picks(m, 'api');
  assert.equal(p.value.slug, 'x');
  assert.equal(p.quality, null);
  assert.equal(p.budget, null);
});

test('picks breaks exact score ties by name', () => {
  const m = [
    { slug: 'z', name: 'Zed', overall: { api: 50 }, quality: 50, costDims: { api: 10 } },
    { slug: 'a', name: 'Aye', overall: { api: 50 }, quality: 50, costDims: { api: 10 } },
    { slug: 'q', name: 'Qux', overall: { api: 40 }, quality: 50, costDims: { api: 10 } },
  ];
  const p = picks(m, 'api');
  assert.deepEqual([p.value.slug, p.quality.slug], ['a', 'a']);
  const rev = picks([...m].reverse(), 'api');
  assert.deepEqual([rev.value.slug, rev.quality.slug], ['a', 'a']);
});
