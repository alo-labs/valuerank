#!/usr/bin/env node
/**
 * Rendered capture of the tbench.ai Terminal-Bench leaderboard, laid out like
 * research/2026-10-30-v5-recapture/third-party/tbench/tb4-scrape-2026-10-30.json:
 * headless Chromium, 1600x1200, no sign-in, no interaction beyond loading the page;
 * saves rendered text, table rows, links, button texts ("tabs"), every inline script
 * (the page's embedded leaderboard payload is among them) and a full-page screenshot.
 *
 * 2026-11-26 changes (the capture logic is otherwise the 2026-11-01 script): the board URL is an optional third
 * argument (default: the 4.1 leaderboard path, which, like the 4.0 path, redirects to the home page), and playwright
 * resolves from <cwd>/node_modules, else from PLAYWRIGHT_DIR, else normally.
 *
 * Usage (from the repository root):
 *   node research/2026-11-26-recapture/third-party/tools/capture_tbench.js <out.json> <out.png> [url]
 */
const fs = require('fs');
const path = require('path');
function loadPlaywright() {
  for (const dir of [path.join(process.cwd(), 'node_modules'), process.env.PLAYWRIGHT_DIR].filter(Boolean)) {
    try { return require(path.join(dir, 'playwright')); } catch (e) { /* try the next location */ }
  }
  return require('playwright');
}
const { chromium } = loadPlaywright();

const URL = process.argv[4] || 'https://www.tbench.ai/leaderboard/terminal-bench/4.1';
const clean = (s) => (s || '').replace(/\s+/g, ' ').trim();

(async () => {
  const [outJson, outPng] = process.argv.slice(2);
  const launch = { headless: true };
  if (process.env.CHROMIUM_PATH) launch.executablePath = process.env.CHROMIUM_PATH;
  const browser = await chromium.launch(launch);
  try {
    const page = await browser.newPage({ viewport: { width: 1600, height: 1200 } });
    page.setDefaultTimeout(120000);
    await page.goto(URL, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(8000);
    const scrapedAt = new Date().toISOString();
    const raw = await page.evaluate(() => ({
      finalUrl: location.href,
      title: document.title,
      text: document.body.innerText,
      rows: Array.from(document.querySelectorAll('table tr, [role="row"]')).map((r) =>
        Array.from(r.querySelectorAll('th, td, [role="cell"]')).map((c) => c.innerText)),
      links: Array.from(document.querySelectorAll('a[href]')).map((a) => ({ text: a.innerText, href: a.href })),
      tabs: Array.from(document.querySelectorAll('button, [role="tab"]')).map((b) => b.innerText),
      scripts: Array.from(document.querySelectorAll('script')).map((s) => s.textContent).filter((t) => t),
    }));
    const capture = {
      scrapedAt,
      source: URL,
      finalUrl: raw.finalUrl,
      title: raw.title,
      text: clean(raw.text),
      rows: raw.rows.map((r) => r.map(clean)).filter((r) => r.length >= 3),
      links: raw.links.map((l) => ({ text: clean(l.text), href: l.href })).filter((l) => l.text || l.href.includes('leaderboard')),
      tabs: raw.tabs.map(clean).filter((t) => t),
      scripts: raw.scripts,
    };
    await page.screenshot({ path: outPng, fullPage: true });
    fs.writeFileSync(outJson, `${JSON.stringify(capture, null, 2)}\n`);
    console.log(JSON.stringify({ scrapedAt, finalUrl: capture.finalUrl, rows: capture.rows.length, scripts: capture.scripts.length }));
  } finally {
    await browser.close();
  }
})().catch((e) => { console.error(e); process.exit(1); });
