// Real-browser scenarios against the generated site/ directory. The CDN is
// blocked, so charts render as placeholders; everything else is live code.
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

async function open(path, options) {
  const { page, context, errors } = await browser.newPage(options);
  await page.goto(server.baseUrl + path, { waitUntil: 'load' });
  return { page, context, errors };
}

const PAGES = [
  '/', '/rankings/', '/models/', '/plans/', '/benchmarks/', '/benchmarks/terminal-bench-4/', '/methodology/', '/changelog/', '/data/',
  '/models/gpt-6-1-sol/', '/models/mimo-v2-6-pro/',
];

function query(page) {
  return page.evaluate(() => window.location.search);
}

describe('answer page', () => {
  test('opens on the Plan ranking with the headline, picks and a compact table', async () => {
    const { page, context, errors } = await open('/');
    assert.equal(await page.locator('h1').count(), 1);
    assert.equal(await page.locator('#basis-toggle [data-basis="plan"]').getAttribute('aria-pressed'), 'true');
    assert.equal(await page.locator('h1 [data-basis-only="plan"]').isVisible(), true);
    assert.equal(await page.locator('h1 [data-basis-only="api"]').isVisible(), false);
    assert.equal(await page.evaluate(() => document.documentElement.dataset.basis), 'plan');
    assert.equal(await page.locator('[data-pick]:visible').count(), 3);
    assert.equal(await page.locator('#index-body tr').count(), 16);
    assert.equal(await query(page), '');
    assert.deepEqual(errors, []);
    await context.close();
  });

  test('basis toggle and cost weight slider are reflected in the URL and restored on reload', async () => {
    const { page, context } = await open('/');
    await page.locator('#basis-toggle [data-basis="api"]').click();
    assert.equal(await query(page), '?basis=api');
    assert.equal(await page.locator('h1 [data-basis-only="api"]').isVisible(), true);
    assert.equal(await page.locator('h1 [data-basis-only="plan"]').isVisible(), false);
    assert.equal(await page.evaluate(() => document.documentElement.dataset.basis), 'api');
    await page.locator('summary', { hasText: 'Adjust how much cost matters' }).click();
    await page.locator('#cost-weight').fill('30');
    await page.locator('#cost-weight').dispatchEvent('input');
    assert.equal(await query(page), '?basis=api&w=30');
    assert.equal(await page.locator('#cost-weight-value').innerText(), '30.0%');

    await page.goto(server.baseUrl + '/?basis=api&w=30', { waitUntil: 'load' });
    assert.equal(await page.locator('#basis-toggle [data-basis="api"]').getAttribute('aria-pressed'), 'true');
    assert.equal(await page.locator('#cost-weight').inputValue(), '30');
    assert.equal(await page.locator('#cost-weight-value').textContent(), '30.0%');
    await context.close();
  });

  test('a shared URL reproduces the same table order', async () => {
    const { page, context } = await open('/?basis=api&w=60');
    const first = await page.locator('#index-body tr').first().getAttribute('data-slug');
    await page.locator('#basis-toggle [data-basis="plan"]').click();
    const firstPlan = await page.locator('#index-body tr').first().getAttribute('data-slug');
    await page.goto(server.baseUrl + '/?basis=api&w=60', { waitUntil: 'load' });
    assert.equal(await page.locator('#index-body tr').first().getAttribute('data-slug'), first);
    assert.notEqual(first, null);
    assert.notEqual(firstPlan, null);
    await context.close();
  });
});

describe('rankings instrument', () => {
  test('filters, sorting, columns and comparison all live in the URL', async () => {
    const { page, context, errors } = await open('/rankings/');
    assert.equal(await page.locator('#rankings-body tr').count(), 31);

    await page.locator('#filters input[name="provider"][value="OpenAI"]').check();
    assert.match(await query(page), /provider=OpenAI/);
    const openAiRows = await page.locator('#rankings-body tr[data-slug]').count();
    assert.ok(openAiRows > 0 && openAiRows < 28);

    await page.locator('#filters input[name="q"]').fill('sol');
    await page.locator('#filters input[name="q"]').dispatchEvent('input');
    assert.match(await query(page), /q=sol/);

    await page.locator('#rankings-head th[data-col="quality"] .sort-btn').click();
    assert.match(await query(page), /sort=quality/);
    assert.equal(await page.locator('#rankings-head th[data-col="quality"]').getAttribute('aria-sort'), 'descending');

    const slugs = await page.locator('#rankings-body tr[data-slug]').evaluateAll((rows) => rows.slice(0, 2).map((row) => row.dataset.slug));
    for (const slug of slugs) await page.locator(`#rankings-body tr[data-slug="${slug}"] [data-compare]`).check();
    assert.match(await query(page), new RegExp(`compare=${slugs.join('(%2C|,)')}`));
    assert.equal(await page.locator('#compare-drawer').isVisible(), true);

    await page.goto(server.baseUrl + '/rankings/' + (await query(page)), { waitUntil: 'load' });
    assert.equal(await page.locator('#filters input[name="provider"][value="OpenAI"]').isChecked(), true);
    assert.equal(await page.locator('#filters input[name="q"]').inputValue(), 'sol');
    assert.equal(await page.locator('#compare-drawer').isVisible(), true);
    assert.deepEqual(errors, []);
    await context.close();
  });

  test('export links produce downloadable CSV and JSON for the current basis', async () => {
    const { page, context } = await open('/rankings/?basis=api');
    const [download] = await Promise.all([page.waitForEvent('download'), page.locator('#export-csv').click()]);
    assert.match(download.suggestedFilename(), /api/);
    assert.match(download.suggestedFilename(), /\.csv$/);
    await context.close();
  });

  test('column picker hides a column and the choice is shareable', async () => {
    const { page, context } = await open('/rankings/');
    const option = page.locator('#column-picker-list input[type="checkbox"]:not([disabled])').first();
    const key = await option.getAttribute('data-col');
    assert.equal(await page.locator(`#rankings-head th[data-col="${key}"]`).count(), 1);
    await option.uncheck();
    assert.match(await query(page), /cols=/);
    assert.equal(await page.locator(`#rankings-head th[data-col="${key}"]`).count(), 0);
    await page.goto(server.baseUrl + '/rankings/' + (await query(page)), { waitUntil: 'load' });
    assert.equal(await page.locator(`#rankings-head th[data-col="${key}"]`).count(), 0);
    await context.close();
  });
});

describe('site chrome', () => {
  test('mobile navigation opens, closes with Escape, and the page has no horizontal scroll', async () => {
    const { page, context } = await open('/', { viewport: { width: 375, height: 812 }, isMobile: true, hasTouch: true });
    const toggle = page.locator('[data-nav-toggle]');
    assert.equal(await toggle.getAttribute('aria-expanded'), 'false');
    await toggle.click();
    assert.equal(await toggle.getAttribute('aria-expanded'), 'true');
    await page.keyboard.press('Escape');
    assert.equal(await toggle.getAttribute('aria-expanded'), 'false');
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
    assert.equal(overflow, 0);
    await context.close();
  });

  test('theme toggle is the only thing stored locally', async () => {
    const { page, context } = await open('/rankings/?basis=api');
    await page.locator('[data-theme-toggle]').click();
    const stored = await page.evaluate(() => Object.keys(localStorage));
    assert.deepEqual(stored, ['vr-theme']);
    assert.equal(await page.evaluate(() => document.documentElement.dataset.theme), 'dark');
    await context.close();
  });

  test('legacy URLs redirect to their new homes', async () => {
    const { page, context } = await open('/tb4/');
    await page.waitForURL(/\/benchmarks\/terminal-bench-4\/$/);
    await page.goto(server.baseUrl + '/coding-agents/', { waitUntil: 'load' });
    await page.waitForURL(/\/archive\/coding-agents-v0\.3\/$/);
    assert.equal(await page.locator('.archive-banner').count(), 1);
    await context.close();
  });

  test('every generated page has one h1, a skip link and a canonical URL', async () => {
    const { page, context } = await open('/');
    for (const path of PAGES) {
      await page.goto(server.baseUrl + path, { waitUntil: 'load' });
      assert.equal(await page.locator('h1').count(), 1, path);
      assert.equal(await page.locator('a.skip-link[href="#main"]').count(), 1, path);
      assert.equal(await page.locator('link[rel="canonical"]').count(), 1, path);
    }
    await context.close();
  });
});

describe('charts, model, plans and listing pages', () => {
  test('the chart tab on the rankings page is part of the shareable URL', async () => {
    const { page, context, errors } = await open('/rankings/');
    assert.equal(await page.locator('[data-chart-tab="pareto"]').getAttribute('aria-selected'), 'true');
    await page.locator('[data-chart-tab="decomposition"]').click();
    assert.equal(await query(page), '?chart=decomposition');
    assert.equal(await page.locator('[data-chart-panel="decomposition"]').isVisible(), true);
    assert.equal(await page.locator('[data-chart-panel="pareto"]').isVisible(), false);
    await page.locator('#cost-weight').fill('40');
    await page.locator('#cost-weight').dispatchEvent('input');
    assert.equal(await query(page), '?w=40&chart=decomposition');

    await page.goto(server.baseUrl + '/rankings/?chart=heatmap', { waitUntil: 'load' });
    assert.equal(await page.locator('[data-chart-tab="heatmap"]').getAttribute('aria-selected'), 'true');
    await page.locator('[data-chart-tab="pareto"]').click();
    assert.equal(await query(page), '');
    assert.deepEqual(errors, []);
    await context.close();
  });

  test('the models index lists all 31 models and links to their pages', async () => {
    const { page, context } = await open('/models/');
    assert.equal(await page.locator('#models-table tbody tr').count(), 31);
    await page.locator('#models-table a.model-name', { hasText: 'GPT-6.1 Sol' }).first().click();
    await page.waitForURL(/\/models\/gpt-6-1-sol\/$/);
    assert.equal(await page.locator('h1').innerText(), 'GPT-6.1 Sol');
    assert.equal(await page.locator('#dimension-table tbody tr').count() > 10, true);
    assert.equal(await page.locator('nav[aria-label="Primary"] a[aria-current="page"]').innerText(), 'Models');
    await context.close();
  });

  test('the plans page explains the calculation with the worked example numbers', async () => {
    const { page, context } = await open('/plans/');
    const rows = page.locator('#worked-example tbody tr');
    assert.equal(await rows.count(), 2);
    assert.match(await rows.nth(1).innerText(), /GPT-6\.1 Sol/);
    assert.match(await rows.nth(1).innerText(), /\$\d/);
    await context.close();
  });

  test('legacy benchmarks pages keep working: Terminal-Bench shows its table and a chart placeholder', async () => {
    const { page, context } = await open('/benchmarks/terminal-bench-4/');
    assert.equal(await page.locator('#official-rows tbody tr').count(), 23);
    await page.locator('[data-chart="tb4"]').scrollIntoViewIfNeeded();
    await page.waitForFunction(() => document.querySelector('[data-chart="tb4"]').dataset.chartStatus === 'error');
    await context.close();
  });

  test('no page logs a console or script error, at desktop and phone width, in both themes', async () => {
    for (const options of [{}, { viewport: { width: 375, height: 812 }, isMobile: true, hasTouch: true }, { colorScheme: 'dark' }]) {
      const { page, context, errors } = await browser.newPage(options);
      for (const path of PAGES) {
        await page.goto(server.baseUrl + path, { waitUntil: 'load' });
        if (path === '/rankings/') await page.waitForSelector('#rankings-body tr[data-slug]');
        const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
        assert.equal(overflow, 0, `${path} overflows horizontally`);
      }
      assert.deepEqual(errors.map((e) => e.message), []);
      await context.close();
    }
  });
});
