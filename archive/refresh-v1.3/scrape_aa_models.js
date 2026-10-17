#!/usr/bin/env node
/**
 * Scrape Artificial Analysis model pages for ValueRank dimensions.
 * Usage: node scrape_aa_models.js mapping.json outDir
 */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const mappingPath = process.argv[2];
const outDir = process.argv[3] || path.join(__dirname, 'aa');
fs.mkdirSync(outDir, { recursive: true });

const mapping = JSON.parse(fs.readFileSync(mappingPath, 'utf8'));

const METRIC_PATTERNS = [
  { key: 'intelligenceIndex', re: /Intelligence Index[^\n]{0,40}?([\d.]+)/i },
  { key: 'speed', re: /(?:Output Speed|Speed)[^\n]{0,40}?([\d.]+)\s*(?:t\/s|tok)/i },
  { key: 'evalCost', re: /(?:Evaluations? Cost|Eval(?:uation)? Cost|Price)[^\n]{0,60}?\$?\s*([\d,]+(?:\.\d+)?)/i },
  { key: 'ifbench', re: /IFBench[^\n]{0,40}?([\d.]+)/i },
  { key: 'omniAcc', re: /Omniscience[^\n]{0,80}?Accuracy[^\n]{0,40}?([\d.]+)/i },
  { key: 'omniHalluc', re: /Hallucination[^\n]{0,40}?([\d.]+)/i },
  { key: 'terminalBenchHard', re: /Terminal-?Bench(?:\s*v?2\.1)?[^\n]{0,60}?([\d.]+)/i },
  { key: 'gdpval', re: /GDPval[^\n]{0,40}?([\d.]+)/i },
  { key: 'tau2', re: /τ²-?Bench|Tau[- ]?2[^\n]{0,40}?([\d.]+)/i },
  { key: 'lcr', re: /AA-?LCR|Long Context[^\n]{0,40}?([\d.]+)/i },
  { key: 'hle', re: /Humanity'?s Last Exam|HLE[^\n]{0,40}?([\d.]+)/i },
  { key: 'gpqa', re: /GPQA[^\n]{0,40}?([\d.]+)/i },
  { key: 'scicode', re: /SciCode[^\n]{0,40}?([\d.]+)/i },
  { key: 'critpt', re: /CritPt[^\n]{0,40}?([\d.]+)/i },
];

function parseMetrics(text) {
  const m = {};
  for (const { key, re } of METRIC_PATTERNS) {
    const hit = text.match(re);
    if (hit) m[key] = parseFloat(String(hit[1]).replace(/,/g, ''));
  }
  return m;
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const results = [];

  for (const entry of mapping) {
    const page = await browser.newPage();
    const urls = entry.urls || [entry.url];
    let best = null;
    for (const url of urls) {
      try {
        await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
        await page.waitForTimeout(2500);
        const text = await page.evaluate(() => document.body.innerText);
        const html = await page.content();
        const slug = url.split('/').pop();
        const safe = `${entry.id}__${slug}`.replace(/[^a-zA-Z0-9._-]/g, '_');
        fs.writeFileSync(path.join(outDir, `${safe}.txt`), text);
        fs.writeFileSync(path.join(outDir, `${safe}.html`), html);
        const metrics = parseMetrics(text);
        // Also try structured extraction from common AA labels
        const structured = await page.evaluate(() => {
          const out = {};
          const walk = (root) => {
            const nodes = Array.from(root.querySelectorAll('div, span, li, p, td, dt, dd'));
            for (const n of nodes) {
              const t = (n.innerText || '').trim();
              if (!t || t.length > 120) continue;
              const labels = [
                'Intelligence Index',
                'IFBench',
                'GPQA',
                'SciCode',
                'CritPt',
                'AA-LCR',
                'Terminal-Bench',
                'GDPval',
                'Omniscience',
                'Hallucination',
                'Humanity',
                'τ²',
                'Tau',
                'Speed',
                'Eval',
              ];
              if (labels.some((l) => t.includes(l))) {
                const sib = n.parentElement ? n.parentElement.innerText : t;
                out[t.slice(0, 80)] = sib.slice(0, 200);
              }
            }
          };
          walk(document.body);
          return out;
        });
        const coverage = Object.keys(metrics).length;
        const row = {
          id: entry.id,
          displayName: entry.displayName,
          url,
          variant: slug,
          metrics,
          coverage,
          structuredSample: Object.fromEntries(Object.entries(structured).slice(0, 40)),
          textLen: text.length,
        };
        if (!best || coverage > best.coverage) best = row;
        console.error(`OK ${entry.id} ${slug} coverage=${coverage}`);
      } catch (e) {
        console.error(`FAIL ${entry.id} ${url}: ${e.message}`);
      }
    }
    if (best) results.push(best);
    await page.close();
  }

  await browser.close();
  const outPath = path.join(outDir, 'aa_extract.json');
  fs.writeFileSync(outPath, JSON.stringify(results, null, 2));
  console.log(JSON.stringify({ n: results.length, outPath, coverages: results.map((r) => [r.id, r.variant, r.coverage]) }, null, 2));
})().catch((e) => {
  console.error(e);
  process.exit(1);
});
