import { test } from 'node:test';
import assert from 'node:assert/strict';
import { loadPlotly, PLOTLY_URL } from '../../../valuerank/site/assets/js/charts/plotly-loader.js';
import { createFakeDocument } from './_fake-dom.mjs';

test('reuses an existing global without injecting a script', async () => {
  const plotly = {};
  const doc = createFakeDocument({ plotly });
  assert.equal(await loadPlotly(doc), plotly);
  assert.equal(doc.appended.length, 0);
});

test('injects one pinned script and dedupes concurrent calls', async () => {
  const doc = createFakeDocument();
  const first = loadPlotly(doc);
  const second = loadPlotly(doc);
  assert.equal(first, second);
  assert.equal(doc.appended.length, 1);
  assert.equal(doc.appended[0].src, PLOTLY_URL);
  assert.match(PLOTLY_URL, /plotly-2\.27\.0\.min\.js$/);
  doc.defaultView.Plotly = { loaded: true };
  doc.appended[0].onload();
  assert.deepEqual(await first, { loaded: true });
});

test('rejects on script error and allows a retry', async () => {
  const doc = createFakeDocument();
  const failed = loadPlotly(doc);
  doc.appended[0].onerror();
  await assert.rejects(failed, /Could not load https:\/\/cdn\.plot\.ly/);
  loadPlotly(doc);
  assert.equal(doc.appended.length, 2);
});
