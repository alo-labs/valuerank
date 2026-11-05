import test from 'node:test';
import assert from 'node:assert/strict';
import { toCsv, toJson, exportFilename } from '../../../valuerank/site/assets/js/export.js';
import { columnCatalog } from '../../../valuerank/site/assets/js/filters.js';
import { dimensions, models } from './fixture.mjs';

const catalog = columnCatalog(dimensions);
const cols = ['name', 'developer', 'overall', 'cost', 'grade', 'b'].map((k) => catalog.find((c) => c.key === k));

test('toCsv writes a header of labels and one CRLF-terminated row per model', () => {
  const csv = toCsv(models.slice(0, 2), cols, 'api');
  const lines = csv.split('\r\n');
  assert.equal(lines.length, 3);
  assert.equal(lines[0], 'Model,Developer,Overall,Cost,Evidence,Beta bench');
  assert.equal(lines[1], 'Alpha,Acme,67.6,100,measured,60');
  assert.equal(lines[2], 'Beta,Bolt AI,75.3,2500,estimate,');
});

test('toCsv quotes commas, quotes and newlines and doubles embedded quotes', () => {
  const m = [{ ...models[0], name: 'He said "hi", ok\nbye', developer: 'plain' }];
  const csv = toCsv(m, cols.slice(0, 2), 'api').split('\r\n');
  assert.equal(csv[1], '"He said ""hi"", ok\nbye",plain');
});

test('toCsv uses the plan cost under the plan basis', () => {
  assert.match(toCsv([models[1]], cols, 'plan'), /Beta,Bolt AI,69\.4,2500,estimate,/);
});

test('toJson emits an array of objects keyed by column key, with nulls preserved', () => {
  const out = JSON.parse(toJson(models.slice(1, 2), cols, 'api'));
  assert.deepEqual(out, [{ name: 'Beta', developer: 'Bolt AI', overall: 75.3, cost: 2500, grade: 'estimate', b: null }]);
  assert.match(toJson(models.slice(1, 2), cols, 'api'), /\n  /);
});

test('exportFilename contains the basis and the version', () => {
  assert.equal(exportFilename('plan', 'v1.9.6', 'csv'), 'valuerank-v1.9.6-plan.csv');
});
