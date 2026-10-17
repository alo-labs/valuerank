// Automated accessibility audit: axe-core runs on every page type in both colour schemes and the
// build fails on any serious or critical violation (colour contrast included).
import assert from 'node:assert/strict';
import { after, before, describe, test } from 'node:test';
import { AxeBuilder } from '@axe-core/playwright';

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

const AUDITED = [
  '/', '/rankings/', '/rankings/?chart=heatmap', '/models/', '/models/gpt-6-1-sol/', '/plans/', '/benchmarks/',
  '/benchmarks/terminal-bench-4/', '/methodology/', '/changelog/', '/data/', '/archive/coding-agents-v0.3/',
];
const VIEWPORTS = { desktop: { width: 1280, height: 900 }, phone: { width: 375, height: 812 } };
const BLOCKING = new Set(['serious', 'critical']);

async function audit(page, path) {
  await page.goto(server.baseUrl + path, { waitUntil: 'load' });
  if (path.startsWith('/rankings/')) await page.waitForSelector('#rankings-body tr[data-slug]');
  const { violations } = await new AxeBuilder({ page }).analyze();
  return violations
    .filter((violation) => BLOCKING.has(violation.impact))
    .map((violation) => `${violation.impact} ${violation.id}: ${violation.nodes.map((node) => node.target.join(' ')).slice(0, 6).join(' | ')}`);
}

describe('accessibility audit', () => {
  for (const colorScheme of ['light', 'dark']) {
    for (const [name, viewport] of Object.entries(VIEWPORTS)) {
      test(`no serious or critical axe violations in the ${colorScheme} theme at ${name} width`, async () => {
        const { page, context } = await browser.newPage({ colorScheme, viewport });
        // The shared theme toggle and the archived page both read this key, so the stored theme wins over the system one.
        await context.addInitScript((theme) => localStorage.setItem('vr-theme', theme), colorScheme);
        const found = {};
        for (const path of AUDITED) found[path] = await audit(page, path);
        await context.close();
        const failing = Object.fromEntries(Object.entries(found).filter(([, issues]) => issues.length));
        assert.deepEqual(failing, {});
      });
    }
  }
});
