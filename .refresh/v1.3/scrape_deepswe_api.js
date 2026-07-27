#!/usr/bin/env node
/** Capture DeepSWE API responses + DOM text after hydration */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const OUT_DIR = path.join(__dirname, 'snapshots');
fs.mkdirSync(OUT_DIR, { recursive: true });

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  const apiHits = [];

  page.on('response', async (resp) => {
    try {
      const url = resp.url();
      const ct = (resp.headers()['content-type'] || '').toLowerCase();
      if (
        url.includes('datacurve') ||
        url.includes('deepswe') ||
        url.includes('supabase') ||
        url.includes('api') ||
        ct.includes('json')
      ) {
        let body = null;
        try {
          if (ct.includes('json') || url.includes('api')) {
            body = await resp.text();
          }
        } catch (_) {}
        if (body && body.length < 5_000_000) {
          apiHits.push({ url, status: resp.status(), ct, len: body.length, bodyPreview: body.slice(0, 500) });
          const safe = url.replace(/[^a-zA-Z0-9._-]/g, '_').slice(0, 120);
          if (body.includes('passRate') || body.includes('pass_rate') || body.includes('averageCost') || body.includes('models')) {
            fs.writeFileSync(path.join(OUT_DIR, `api_${safe}.json`), body);
          }
        } else {
          apiHits.push({ url, status: resp.status(), ct, len: body ? body.length : 0 });
        }
      }
    } catch (_) {}
  });

  await page.goto('https://deepswe.datacurve.ai/', { waitUntil: 'networkidle', timeout: 120000 });
  await page.waitForTimeout(5000);

  // Click filters
  for (const label of ['Best', 'Max', 'All', 'Pass']) {
    try {
      const btn = page.getByRole('button', { name: new RegExp(label, 'i') }).first();
      if (await btn.count()) {
        await btn.click({ timeout: 2000 });
        await page.waitForTimeout(1000);
      }
    } catch (_) {}
  }

  const dump = await page.evaluate(() => {
    return {
      title: document.title,
      bodyLen: document.body.innerText.length,
      body: document.body.innerText,
      htmlLen: document.documentElement.outerHTML.length,
    };
  });
  fs.writeFileSync(path.join(OUT_DIR, 'deepswe-body.txt'), dump.body);
  fs.writeFileSync(path.join(__dirname, 'api_hits.json'), JSON.stringify(apiHits, null, 2));
  console.log(JSON.stringify({
    title: dump.title,
    bodyLen: dump.bodyLen,
    apiHits: apiHits.length,
    interesting: apiHits.filter(h => (h.bodyPreview||'').includes('pass') || (h.url||'').includes('model')).slice(0,10),
    bodyHead: dump.body.slice(0, 2000),
  }, null, 2));
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
