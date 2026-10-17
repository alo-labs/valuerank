#!/usr/bin/env node
/**
 * Scrape DeepSWE Best roster via Playwright (Next.js hydration).
 * Usage: node scrape_deepswe.js [outJson] [htmlSnapshot]
 */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const OUT = process.argv[2] || path.join(__dirname, 'deepswe.json');
const HTML_OUT = process.argv[3] || path.join(__dirname, 'snapshots', 'deepswe-hydrated.html');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  page.setDefaultTimeout(120000);
  await page.goto('https://deepswe.datacurve.ai/', { waitUntil: 'networkidle' });
  // Wait for table / model rows
  await page.waitForTimeout(3000);
  // Try clicking "Best" filter if present
  const bestSelectors = [
    'button:has-text("Best")',
    'text=Best',
    '[role="tab"]:has-text("Best")',
    'label:has-text("Best")',
  ];
  for (const sel of bestSelectors) {
    try {
      const el = page.locator(sel).first();
      if (await el.count()) {
        await el.click({ timeout: 2000 });
        await page.waitForTimeout(1500);
        break;
      }
    } catch (_) {}
  }

  // Capture network JSON if any API returned models
  const html = await page.content();
  fs.mkdirSync(path.dirname(HTML_OUT), { recursive: true });
  fs.writeFileSync(HTML_OUT, html);

  // Extract from page via JS evaluation
  const extracted = await page.evaluate(() => {
    const out = {
      textSample: document.body.innerText.slice(0, 5000),
      rows: [],
      jsonCandidates: [],
    };
    // Look for React/Next flight data containing passRate
    const scripts = Array.from(document.querySelectorAll('script'));
    for (const s of scripts) {
      const t = s.textContent || '';
      if (t.includes('passRate') || t.includes('averageCostPerTask')) {
        out.jsonCandidates.push(t.slice(0, 200000));
      }
    }
    // Parse table rows if present
    const trs = Array.from(document.querySelectorAll('table tr, [role="row"]'));
    for (const tr of trs) {
      const cells = Array.from(tr.querySelectorAll('td, [role="cell"], th')).map(
        (c) => (c.innerText || '').trim()
      );
      if (cells.length >= 3) out.rows.push(cells);
    }
    // Also collect list-like cards
    const cards = Array.from(
      document.querySelectorAll('[class*="model"], [class*="Model"], [class*="row"]')
    )
      .slice(0, 50)
      .map((el) => (el.innerText || '').trim().slice(0, 300));
    out.cards = cards.filter(Boolean);
    return out;
  });

  // Intercept: also dump __NEXT_DATA__ if present
  const nextData = await page.evaluate(() => {
    const el = document.getElementById('__NEXT_DATA__');
    return el ? el.textContent : null;
  });

  // Try to find models in window state
  const winModels = await page.evaluate(() => {
    const found = [];
    const walk = (obj, depth = 0) => {
      if (!obj || depth > 8) return;
      if (Array.isArray(obj)) {
        if (
          obj.length &&
          typeof obj[0] === 'object' &&
          obj[0] &&
          ('passRate' in obj[0] || 'averageCostPerTask' in obj[0] || 'pass_rate' in obj[0])
        ) {
          found.push(obj);
        }
        obj.slice(0, 5).forEach((x) => walk(x, depth + 1));
        return;
      }
      if (typeof obj === 'object') {
        for (const k of Object.keys(obj)) {
          if (k === 'models' || k === 'leaderboard' || k === 'data') walk(obj[k], depth + 1);
        }
      }
    };
    try {
      walk(window.__NEXT_DATA__);
    } catch (_) {}
    return found.slice(0, 3);
  });

  await browser.close();

  const result = {
    scrapedAt: new Date().toISOString(),
    source: 'https://deepswe.datacurve.ai/',
    nextDataPresent: Boolean(nextData),
    winModelsCount: winModels.length,
    tableRows: extracted.rows.slice(0, 40),
    textSample: extracted.textSample,
    cards: extracted.cards?.slice(0, 30),
    scriptHits: extracted.jsonCandidates.length,
    winModels: winModels,
  };

  // Parse models from script candidates
  const models = [];
  const seen = new Set();
  const parseText = (text) => {
    const re =
      /"name"\s*:\s*"([^"]+)"\s*,\s*"organization"\s*:\s*"([^"]+)"[\s\S]{0,4000}?"passRate"\s*:\s*([\d.]+)[\s\S]{0,800}?"averageCostPerTask"\s*:\s*([\d.]+)/g;
    let m;
    while ((m = re.exec(text))) {
      const name = m[1];
      if (seen.has(name)) continue;
      seen.add(name);
      models.push({
        name,
        organization: m[2],
        passRate: parseFloat(m[3]),
        avgCost: parseFloat(m[4]),
      });
    }
    // alternate: passRate near shortName
    const re2 =
      /"shortName"\s*:\s*"([^"]+)"[\s\S]{0,500}?"name"\s*:\s*"([^"]+)"[\s\S]{0,2000}?"passRate"\s*:\s*([\d.]+)[\s\S]{0,500}?"averageCostPerTask"\s*:\s*([\d.]+)/g;
    while ((m = re2.exec(text))) {
      const name = m[2];
      if (seen.has(name)) continue;
      seen.add(name);
      models.push({
        shortName: m[1],
        name,
        passRate: parseFloat(m[3]),
        avgCost: parseFloat(m[4]),
      });
    }
  };
  for (const t of extracted.jsonCandidates) parseText(t);
  if (nextData) parseText(nextData);
  for (const arr of winModels) {
    for (const row of arr) {
      const name = row.name || row.shortName;
      if (!name || seen.has(name)) continue;
      if (row.passRate == null && row.pass_rate == null) continue;
      seen.add(name);
      models.push({
        name,
        organization: row.organization,
        version: row.version,
        rank: row.rank,
        passRate: row.passRate ?? row.pass_rate,
        avgCost: row.averageCostPerTask ?? row.avgCost ?? row.average_cost_per_task,
        slug: row.slug,
        shortName: row.shortName,
      });
    }
  }

  result.models = models;
  result.modelCount = models.length;
  fs.writeFileSync(OUT, JSON.stringify(result, null, 2));
  console.log(JSON.stringify({ modelCount: models.length, out: OUT, sample: models.slice(0, 5) }, null, 2));
})().catch((e) => {
  console.error(e);
  process.exit(1);
});
