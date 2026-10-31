// The "Total Cost to Run" charts with every model selected (as the 2026-10-23 refresh did; O132 re-capture).
//
//   node research/2026-10-30-v5-recapture/capture_cost_charts_all.js data/aa/cost_charts_capture.json
//
// Uses scripts/capture-aa-cost-charts.js's own tab click, chart read and parser, and adds one step: the chart's model
// selector set to Select all (optional cookies declined first, since the banner can intercept clicks).
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const charts = require(path.join(__dirname, '..', '..', 'scripts', 'capture-aa-cost-charts.js'));

const EVALUATIONS = [
  { slug: 'frontiercode', url: 'https://artificialanalysis.ai/evaluations/frontiercode' },
  { slug: 'itbench-aa', url: 'https://artificialanalysis.ai/evaluations/itbench-aa' },
];

async function selectAll(page) {
  const cookies = page.getByRole('button', { name: /Decline optional/i });
  if (await cookies.count()) await cookies.first().click().catch(() => {});
  // The cost chart's selector is the model-selector combobox nearest after the chart title.
  const index = await page.evaluate(() => {
    const title = [...document.querySelectorAll('*')].filter((element) => (element.textContent || '').trim().endsWith(': Total Cost to Run'))
      .sort((a, b) => a.textContent.length - b.textContent.length)[0];
    const boxes = [...document.querySelectorAll('button[role=combobox]')].filter((element) => /of \d+ models/.test(element.textContent));
    return boxes.findIndex((element) => !!(title.compareDocumentPosition(element) & Node.DOCUMENT_POSITION_FOLLOWING));
  });
  if (index < 0) throw new Error('no model selector after the cost chart title');
  const selector = page.locator('button[role=combobox]').filter({ hasText: /of \d+ models/ }).nth(index);
  const before = (await selector.innerText()).trim();
  await selector.click();
  await page.waitForTimeout(1500);
  await page.getByRole('option', { name: /^Select all$/ }).or(page.getByText(/^Select all$/)).first().click();
  await page.waitForTimeout(3000);
  await page.keyboard.press('Escape');
  await page.waitForTimeout(4000);
  return { before, after: (await selector.innerText()).trim() };
}

(async () => {
  const out = process.argv[2];
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1600, height: 1200 } });
  page.setDefaultTimeout(120000);
  const captured = [];
  for (const evaluation of EVALUATIONS) {
    await page.goto(evaluation.url, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(8000);
    if (!(await page.evaluate(charts.clickTotalCostTab, 'Total Cost to Run'))) throw new Error(`no tab on ${evaluation.url}`);
    await page.waitForTimeout(4000);
    const selection = await selectAll(page);
    const chart = await page.evaluate(charts.readTotalCostChart, ': Total Cost to Run');
    const rows = charts.parseChartRows(chart.html);
    captured.push({ slug: evaluation.slug, url: evaluation.url, finalUrl: chart.finalUrl, chartTitle: chart.title, selection, rows });
  }
  const capture = charts.buildCaptureDocument({ capturedAt: new Date().toISOString(), evaluations: captured });
  fs.writeFileSync(out, charts.serializeCapture(capture));
  console.log(JSON.stringify(captured.map(({ slug, selection, rows }) => ({ slug, selection, bars: rows.length }))));
  await browser.close();
})();
