#!/usr/bin/env node
/**
 * Capture the current Terminal-Bench 4.0 leaderboard through its rendered
 * public page.  The site is client-rendered, so a browser capture is the
 * reproducible source snapshot used by the v1.4 builder.
 *
 * Usage: node scrape_tb4.js [outJson]
 */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const OUT = process.argv[2] || path.join(__dirname, 'tb4-scrape.json');
const URL = 'https://www.tbench.ai/leaderboard/terminal-bench/4.0';

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({
    viewport: { width: 1440, height: 1200 },
    userAgent: 'ValueRank research snapshot; contact via repository metadata',
  });
  page.setDefaultTimeout(120000);
  await page.goto(URL, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(7000);

  const captured = await page.evaluate(() => {
    const clean = (value) => (value || '').replace(/\s+/g, ' ').trim();
    const rows = Array.from(document.querySelectorAll('table tr, [role="row"]'))
      .map((row) => Array.from(row.querySelectorAll('th, td, [role="cell"]')).map((cell) => clean(cell.innerText)))
      .filter((row) => row.length >= 3);
    const links = Array.from(document.querySelectorAll('a[href]'))
      .map((a) => ({ text: clean(a.innerText), href: a.href }))
      .filter((item) => item.text || item.href.includes('leaderboard'));
    const scripts = Array.from(document.querySelectorAll('script'))
      .map((script) => script.textContent || '')
      .filter((text) => /GPT-6 Astra|Claude Opus 5|leaderboard|terminal-bench/i.test(text))
      .map((text) => text.slice(0, 250000));
    return {
      finalUrl: location.href,
      title: document.title,
      text: clean(document.body.innerText),
      rows,
      links,
      scripts,
    };
  });

  const result = {
    scrapedAt: new Date().toISOString(),
    source: URL,
    ...captured,
  };
  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  fs.writeFileSync(OUT, JSON.stringify(result, null, 2) + '\n');
  console.log(JSON.stringify({
    out: OUT,
    finalUrl: result.finalUrl,
    title: result.title,
    tableRows: result.rows.length,
    bodyChars: result.text.length,
  }, null, 2));
  await browser.close();
})().catch((error) => {
  console.error(error);
  process.exit(1);
});
