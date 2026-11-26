// Capture AA's Intelligence Index v5 "Intelligence Index vs. Cost to Run" chart (owner decision O132).
//
//   node capture_chart.mjs <out.json>
//
// Method as in the 2026-10-25 capture (O65): headless Chromium at 1600 x 1200, no sign-in, the cookie banner declined;
// the chart's model selector set to Select all; every circle centre and the dotted Pareto path read from the chart SVG;
// each circle hovered from a neutral position and its public tooltip recorded verbatim. No embedded payload is read.
import fs from 'fs';
import { chromium } from 'playwright';

const URL = 'https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index?eval-cost=intelligence-vs-total-cost';
const HEADING = 'Intelligence Index vs. Cost to Run Artificial Analysis Intelligence Index';
const out = process.argv[2];

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1600, height: 1200 } });
await page.goto(URL, { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(12000);
const cookies = page.getByRole('button', { name: /Decline optional/i });
if (await cookies.count()) await cookies.first().click().catch(() => {});

// The chart's own selector and surface: the first model-selector combobox and the first chart surface after its heading.
const order = await page.evaluate((title) => {
  const heading = [...document.querySelectorAll('h1,h2,h3,h4')].find((element) => element.innerText.trim() === title);
  const follows = (element) => !!(heading.compareDocumentPosition(element) & Node.DOCUMENT_POSITION_FOLLOWING);
  const boxes = [...document.querySelectorAll('button[role=combobox]')].filter((element) => /of \d+ models/.test(element.textContent));
  return { selector: boxes.findIndex(follows) };
}, HEADING);
const selector = page.locator('button[role=combobox]').filter({ hasText: /of \d+ models/ }).nth(order.selector);
await selector.scrollIntoViewIfNeeded();
const before = (await selector.innerText()).trim();
await selector.click();
await page.waitForTimeout(1500);
await page.getByRole('option', { name: /^Select all$/ }).or(page.getByRole('button', { name: /^Select all$/ })).or(page.getByText(/^Select all$/)).first().click();
await page.waitForTimeout(3000);
await page.keyboard.press('Escape');
await page.waitForTimeout(3000);
const after = (await selector.innerText()).trim();

// Charts render lazily, so the surface is found after the selection, once the chart is in view.
await page.getByRole('heading', { name: HEADING }).first().scrollIntoViewIfNeeded();
await page.waitForTimeout(2500);
const surfaceIndex = await page.evaluate((title) => {
  const heading = [...document.querySelectorAll('h1,h2,h3,h4')].find((element) => element.innerText.trim() === title);
  return [...document.querySelectorAll('svg.recharts-surface')].findIndex((element) => !!(heading.compareDocumentPosition(element) & Node.DOCUMENT_POSITION_FOLLOWING));
}, HEADING);
if (surfaceIndex < 0) throw new Error('the chart surface did not render');
const surface = page.locator('svg.recharts-surface').nth(surfaceIndex);
await surface.scrollIntoViewIfNeeded();
await page.waitForTimeout(2000);
const svg = await surface.evaluate((element) => {
  const circles = [...element.querySelectorAll('circle')].map((circle) => ({
    id: circle.getAttribute('data-chart-item-id') || circle.closest('[data-chart-item-id]')?.getAttribute('data-chart-item-id') || null,
    cx: Number(circle.getAttribute('cx')), cy: Number(circle.getAttribute('cy')), fill: circle.getAttribute('fill'),
    // The circles sit in a translated group, so hovers use each circle's on-screen centre, relative to the surface.
    screenX: circle.getBoundingClientRect().left + circle.getBoundingClientRect().width / 2 - element.getBoundingClientRect().left,
    screenY: circle.getBoundingClientRect().top + circle.getBoundingClientRect().height / 2 - element.getBoundingClientRect().top,
  }));
  const dotted = [...element.querySelectorAll('path')].filter((path) => (path.getAttribute('stroke-dasharray') || '').startsWith('0.1'));
  return { width: element.getAttribute('width'), height: element.getAttribute('height'), circles, paths: dotted.map((path) => ({ d: path.getAttribute('d'), dash: path.getAttribute('stroke-dasharray') })) };
});
const box = await surface.boundingBox();

// Hover each circle centre from a neutral point and record the tooltip text.
const hovers = [];
for (const circle of svg.circles) {
  await page.mouse.move(box.x + 2, box.y + 2);
  await page.waitForTimeout(150);
  await page.mouse.move(box.x + circle.screenX, box.y + circle.screenY);
  await page.waitForTimeout(450);
  // v5's tooltip is a custom panel ending "Click for more info": read the smallest visible element holding it.
  const tooltip = await page.evaluate(() => {
    const panels = [...document.querySelectorAll('body *')].filter((element) => element.offsetParent !== null && (element.innerText || '').includes('Click for more info')
      && (element.innerText || '').includes('Cost to Run'));
    panels.sort((a, b) => a.innerText.length - b.innerText.length);
    return panels.length ? panels[0].innerText : '';
  });
  hovers.push({ ...circle, tooltip: tooltip.trim() });
}
const document = {
  capturedAt: new Date().toISOString().replace(/\.\d+Z$/, 'Z'), sourceUrl: URL, chartTitle: HEADING,
  title: await page.title(), selectorBefore: before, selectorAfter: after, svgWidth: svg.width, svgHeight: svg.height,
  circleCount: svg.circles.length, paretoPaths: svg.paths, hovers,
};
fs.writeFileSync(out, JSON.stringify(document, null, 1) + '\n');
console.log(JSON.stringify({ selectorBefore: before, selectorAfter: after, circles: svg.circles.length, paths: svg.paths.length,
  distinctTooltips: new Set(hovers.map((item) => item.tooltip)).size, emptyTooltips: hovers.filter((item) => !item.tooltip).length }));
await browser.close();
