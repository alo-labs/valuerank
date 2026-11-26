import test from 'node:test';
import assert from 'node:assert/strict';
import { applyFilters, sortModels, columnCatalog, columnValue, DEFAULT_COLUMNS } from '../../../valuerank/site/assets/js/filters.js';
import { dimensions, models } from './fixture.mjs';

const none = { provider: [], grade: [], route: 'all', cov: 0, q: '' };
const slugs = (rows) => rows.map((m) => m.slug);

test('no filters keeps every model in order', () => {
  assert.deepEqual(slugs(applyFilters(models, none)), ['alpha', 'beta', 'gamma', 'delta', 'eps']);
});

test('provider and grade filter by membership', () => {
  assert.deepEqual(slugs(applyFilters(models, { ...none, provider: ['Acme'] })), ['alpha', 'gamma']);
  assert.deepEqual(slugs(applyFilters(models, { ...none, grade: ['estimate', 'claim'] })), ['beta', 'delta']);
});

test('route filter separates models with an admitted subscription route from API-fallback models', () => {
  assert.deepEqual(slugs(applyFilters(models, { ...none, route: 'eligible' })), ['alpha', 'gamma']);
  assert.deepEqual(slugs(applyFilters(models, { ...none, route: 'fallback' })), ['beta']);
});

test('minimum coverage excludes lower and unknown coverage', () => {
  assert.deepEqual(slugs(applyFilters(models, { ...none, cov: 70 })), ['alpha', 'gamma']);
  assert.deepEqual(slugs(applyFilters(models, { ...none, cov: 0 })).includes('delta'), true);
  assert.deepEqual(slugs(applyFilters(models, { ...none, cov: 1 })).includes('delta'), false);
});

test('free text matches name or developer case-insensitively', () => {
  assert.deepEqual(slugs(applyFilters(models, { ...none, q: 'BOLT' })), ['beta']);
  assert.deepEqual(slugs(applyFilters(models, { ...none, q: 'alp' })), ['alpha']);
  assert.deepEqual(slugs(applyFilters(models, { ...none, q: 'delta' })), ['delta', 'eps']);
});

test('facets combine with AND', () => {
  const state = { ...none, provider: ['Acme'], grade: ['assumption'], q: 'gam', cov: 50 };
  assert.deepEqual(slugs(applyFilters(models, state)), ['gamma']);
  assert.deepEqual(slugs(applyFilters(models, { ...state, grade: ['measured'] })), []);
});

test('columnValue reads basis-specific and nested fields', () => {
  const b = models[1];
  assert.equal(columnValue(b, 'rank', 'api'), 1);
  assert.equal(columnValue(b, 'overall', 'plan'), 69.4);
  assert.equal(columnValue(b, 'quality', 'plan'), 84);
  assert.equal(columnValue(b, 'qualityRank', 'plan'), 1);
  assert.equal(columnValue(b, 'cost', 'api'), 2500);
  assert.equal(columnValue(b, 'cost', 'plan'), 2500);
  assert.equal(columnValue(b, 'grade', 'plan'), 'estimate');
  assert.equal(columnValue(b, 'coverage', 'plan'), 68);
  assert.equal(columnValue(models[3], 'coverage', 'plan'), null);
  assert.equal(columnValue(b, 'speed', 'plan'), 80);
  assert.equal(columnValue(b, 'ii', 'plan'), 50);
  assert.equal(columnValue(b, 'name', 'plan'), 'Beta');
  assert.equal(columnValue(b, 'developer', 'plan'), 'Bolt AI');
  assert.equal(columnValue(b, 'a', 'plan'), 84);
  assert.equal(columnValue(b, 'b', 'plan'), null);
  assert.equal(columnValue(b, 'nonexistent', 'plan'), null);
});

test('sortModels sorts numerically in both directions with nulls last', () => {
  assert.deepEqual(slugs(sortModels(models, 'overall', 'desc', 'api')), ['beta', 'alpha', 'gamma', 'delta', 'eps']);
  assert.deepEqual(slugs(sortModels(models, 'overall', 'asc', 'api')), ['gamma', 'alpha', 'beta', 'delta', 'eps']);
  assert.deepEqual(slugs(sortModels(models, 'rank', 'asc', 'plan')), ['alpha', 'beta', 'gamma', 'delta', 'eps']);
});

test('sortModels sorts text columns and grade by evidence strength', () => {
  assert.deepEqual(slugs(sortModels(models, 'name', 'desc', 'api')), ['gamma', 'eps', 'delta', 'beta', 'alpha']);
  assert.deepEqual(slugs(sortModels(models, 'grade', 'asc', 'api')), ['alpha', 'delta', 'beta', 'gamma', 'eps']);
});

test('sortModels breaks ties by name and does not mutate its input', () => {
  const before = slugs(models);
  const out = sortModels(models, 'developer', 'asc', 'api');
  assert.deepEqual(slugs(models), before);
  assert.deepEqual(slugs(out), ['alpha', 'gamma', 'beta', 'delta', 'eps']);
});

test('sortModels puts nulls last for a dimension column in either direction', () => {
  assert.deepEqual(slugs(sortModels(models, 'b', 'asc', 'api')), ['gamma', 'alpha', 'beta', 'delta', 'eps']);
  assert.deepEqual(slugs(sortModels(models, 'b', 'desc', 'api')), ['alpha', 'gamma', 'beta', 'delta', 'eps']);
});

test('columnCatalog lists core columns, then one column per non-cost dimension; defaults are marked', () => {
  const cols = columnCatalog(dimensions);
  const keys = cols.map((c) => c.key);
  assert.deepEqual(keys.slice(0, 7), ['rank', 'name', 'overall', 'quality', 'cost', 'grade', 'coverage']);
  assert.ok(keys.includes('a') && keys.includes('b') && !keys.includes('costComposite'));
  assert.equal(new Set(keys).size, keys.length);
  assert.deepEqual(cols.filter((c) => c.default).map((c) => c.key), DEFAULT_COLUMNS);
  assert.equal(cols.find((c) => c.key === 'a').label, 'Alpha bench');
  assert.equal(cols.find((c) => c.key === 'a').defaultDir, 'desc');
  assert.equal(cols.find((c) => c.key === 'cost').defaultDir, 'asc');
});
