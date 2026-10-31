// Print styles: navigation and interactive controls are hidden, the data tables stay visible and the
// page prints dark ink on white even when the reader's theme is dark.
import assert from 'node:assert/strict';
import { after, before, describe, test } from 'node:test';

import { launchBrowser, startServer } from './helpers/site-server.mjs';

let server;
let browser;

before(async () => {
  server = await startServer();
  browser = await launchBrowser();
});

after(async () => {
  await browser?.close();
  await server?.close();
});

async function openForPrint(path, theme) {
  const { page, context, errors } = await browser.newPage({ colorScheme: theme });
  await context.addInitScript((value) => localStorage.setItem('vr-theme', value), theme);
  await page.goto(server.baseUrl + path, { waitUntil: 'load' });
  await page.emulateMedia({ media: 'print' });
  return { page, context, errors };
}

const visible = (page, selector) => page.locator(selector).evaluateAll(
  (nodes) => nodes.filter((node) => node.getClientRects().length > 0 && getComputedStyle(node).visibility !== 'hidden').length,
);

describe('print', () => {
  for (const theme of ['light', 'dark']) {
    test(`the answer page prints its table without navigation or controls (${theme} theme)`, async () => {
      const { page, context, errors } = await openForPrint('/', theme);
      for (const hidden of ['.site-header', '.skip-link', '.nav-links', '[data-theme-toggle]', '#basis-toggle', '.slider-panel', '.chart-tabs', '.footer-links']) {
        assert.equal(await visible(page, hidden), 0, `${hidden} should not print`);
      }
      assert.equal(await visible(page, '#answer-table'), 1);
      assert.equal(await visible(page, '#answer-table tbody tr'), 16);
      assert.equal(await visible(page, '#answer-table thead th'), 6); // no Evidence column: evidence is footnoted
      assert.equal(await visible(page, '#index-evidence li'), 16);
      assert.equal(await visible(page, '.fn-back'), 0); // back-links are screen-only
      assert.equal(await page.locator('.table-wrap').first().evaluate((node) => getComputedStyle(node).overflowX), 'visible');
      const ink = await page.evaluate(() => ({ background: getComputedStyle(document.body).backgroundColor, color: getComputedStyle(document.body).color }));
      assert.deepEqual(ink, { background: 'rgb(255, 255, 255)', color: 'rgb(0, 0, 0)' });
      assert.deepEqual(errors, []);
      await context.close();
    });

    test(`a model page prints its breakdown tables on white (${theme} theme)`, async () => {
      const { page, context } = await openForPrint('/models/gpt-6-1-sol/', theme);
      for (const hidden of ['.site-header', '.nav-links', '[data-theme-toggle]', '.footer-links']) {
        assert.equal(await visible(page, hidden), 0, `${hidden} should not print`);
      }
      assert.equal(await visible(page, '#dimension-table tbody tr'), 13); // the max-effort ranking's thirteen leaves (O55, O61)
      assert.equal(await visible(page, 'h1'), 1);
      assert.equal(await page.evaluate(() => getComputedStyle(document.body).backgroundColor), 'rgb(255, 255, 255)');
      await context.close();
    });
  }
});
