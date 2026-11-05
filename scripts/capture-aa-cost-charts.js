#!/usr/bin/env node
/**
 * Capture the "Total Cost to Run" bar charts of AA evaluation pages whose
 * per-model costs are not in the static page payload (FrontierCode, ITBench-AA).
 *
 * The charts render client-side, so the totals are read from the rendered SVG:
 * each bar has a model tick (an <svg><title>) at its x position, stacked-segment
 * value labels, and a total label above the bar. The total is the topmost label
 * at the bar's x. Labels are rounded to USD 1 and AA marks a total with "*" when
 * "the model or provider declined some tasks on safety grounds".
 *
 * Usage: node capture-aa-cost-charts.js [outJson]
 */
const fs = require('fs');
const path = require('path');

const EVALUATIONS = [
  { slug: 'frontiercode', url: 'https://artificialanalysis.ai/evaluations/frontiercode' },
  { slug: 'itbench-aa', url: 'https://artificialanalysis.ai/evaluations/itbench-aa' },
];
const DEFAULT_OUT = path.join(__dirname, '..', 'data', 'aa', 'cost_charts_capture.json');
const PAGE_OPTIONS = {
  viewport: { width: 1600, height: 1200 },
  userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
};
const NAVIGATION_TIMEOUT_MS = 120000;
const RENDER_WAIT_MS = 8000;
const TAB_WAIT_MS = 4000;
const MAX_ATTEMPTS = 4;
const TAB_TEXT = 'Total Cost to Run';
const TITLE_SUFFIX = ': Total Cost to Run';
const BAR_TOLERANCE_PX = 8;
const DECLINED_NOTE = 'The model or provider declined some tasks on safety grounds';
const ENTITIES = { '&amp;': '&', '&lt;': '<', '&gt;': '>', '&quot;': '"', '&#39;': "'", '&#x27;': "'" };

/** The output path: the first CLI argument, or data/aa/cost_charts_capture.json. */
function resolveOutputPath(argv) {
  return argv[2] || DEFAULT_OUT;
}

/** Decodes the HTML entities that appear in model names and labels. */
function decodeEntities(text) {
  return text.replace(/&(?:amp|lt|gt|quot|#39|#x27);/g, (entity) => ENTITIES[entity]);
}

/** Parses a chart label such as "$1,015" or "$16*" into USD; anything else is null. */
function parseUsd(label) {
  const match = /^\$([0-9][0-9,]*(?:\.[0-9]+)?)(k?)\*?$/.exec(label.trim());
  if (!match) {
    return null;
  }
  const value = Number(match[1].replace(/,/g, ''));
  return match[2] ? value * 1000 : value;
}

/** Model ticks (x position and name) in chart order. */
function parseTicks(html) {
  const pattern = /<g transform="translate\(([0-9.]+),[0-9.]+\)"[^>]*>(?:<g[^>]*>)?<svg><title>([^<]+)<\/title>/g;
  return Array.from(html.matchAll(pattern), (match) => ({ x: Number(match[1]), model: decodeEntities(match[2]) }));
}

/** Every SVG text label with its position. */
function parseLabels(html) {
  const pattern = /<text x="([0-9.]+)" y="([0-9.]+)"[^>]*>([^<]*)<\/text>/g;
  return Array.from(html.matchAll(pattern), (match) => ({ x: Number(match[1]), y: Number(match[2]), text: decodeEntities(match[3]) }));
}

/** One row per tick: the topmost label at the tick's x is the bar total. */
function parseChartRows(html) {
  const labels = parseLabels(html);
  return parseTicks(html).map(({ x, model }) => {
    const atBar = labels.filter((label) => Math.abs(label.x - x) < BAR_TOLERANCE_PX && parseUsd(label.text) !== null);
    if (!atBar.length) {
      return { model, totalUsdLabel: null, totalUsd: null, declinedTasks: false };
    }
    const total = atBar.reduce((top, label) => (label.y < top.y ? label : top));
    return { model, totalUsdLabel: total.text, totalUsd: parseUsd(total.text), declinedTasks: total.text.endsWith('*') };
  });
}

/**
 * Runs inside the page: scrolls the leaf element whose text is exactly the tab
 * label into view (the charts render lazily) and clicks it; the click bubbles
 * to the tab control. Returns whether one was found.
 */
function clickTotalCostTab(tabText) {
  const leaves = Array.from(document.querySelectorAll('*')).filter(
    (element) => element.children.length === 0 && (element.textContent || '').trim() === tabText,
  );
  if (!leaves.length) {
    return false;
  }
  const leaf = leaves[0];
  leaf.scrollIntoView({ block: 'center' });
  // Tab controls may switch on mouse-down rather than click, so send the full sequence.
  for (const type of ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click']) {
    leaf.dispatchEvent(new MouseEvent(type, { bubbles: true, cancelable: true, button: 0 }));
  }
  return true;
}

/**
 * Runs inside the page: finds the smallest element whose text ends with the
 * chart-title suffix and returns its nearest ancestor holding SVG text labels.
 */
function readTotalCostChart(titleSuffix) {
  const titles = Array.from(document.querySelectorAll('*'))
    .filter((element) => (element.textContent || '').trim().endsWith(titleSuffix))
    .sort((a, b) => a.textContent.length - b.textContent.length);
  let node = titles[0] || null;
  while (node && node.querySelectorAll('svg text').length === 0) {
    node = node.parentElement;
  }
  return node ? { title: titles[0].textContent.trim(), html: node.outerHTML, finalUrl: location.href } : null;
}

/** O103: the notes AA prints on a page ("* <text>" strings in its payload), verbatim and once each. */
function printedNotes(html) {
  return [...new Set(Array.from(html.matchAll(/"\* ([A-Z][^"\\]{15,400})/g), (match) => match[1].trim()))];
}

/** Loads one evaluation page and returns its parsed chart, retrying transient failures. */
async function captureEvaluation(page, evaluation, { attempts = MAX_ATTEMPTS, log = () => {} } = {}) {
  let lastError = 'no attempt made';
  for (let attempt = 1; attempt <= attempts; attempt += 1) {
    try {
      await page.goto(evaluation.url, { waitUntil: 'domcontentloaded' });
      await page.waitForTimeout(RENDER_WAIT_MS);
      if (!(await page.evaluate(clickTotalCostTab, TAB_TEXT))) {
        throw new Error(`no "${TAB_TEXT}" tab on ${evaluation.url}`);
      }
      await page.waitForTimeout(TAB_WAIT_MS);
      const chart = await page.evaluate(readTotalCostChart, TITLE_SUFFIX);
      if (!chart) {
        throw new Error(`no "${TITLE_SUFFIX}" chart on ${evaluation.url}`);
      }
      const rows = parseChartRows(chart.html);
      if (!rows.length) {
        throw new Error(`no bars in the cost chart on ${evaluation.url}`);
      }
      // O103: the page's printed notes on the chart; a bar carries no note of its own (its "*" marker is parsed apart).
      const notes = printedNotes(await page.content());
      return { slug: evaluation.slug, url: evaluation.url, finalUrl: chart.finalUrl, chartTitle: chart.title, notes, rows: rows.map((row) => ({ ...row, notes: [] })) };
    } catch (failure) {
      lastError = failure.message;
      log(`attempt ${attempt} for ${evaluation.slug} failed: ${lastError}`);
    }
  }
  throw new Error(`could not capture ${evaluation.slug}: ${lastError}`);
}

/** Assembles the capture document; key order is part of the published format. */
function buildCaptureDocument({ capturedAt, evaluations }) {
  return {
    schemaVersion: 'valuerank-aa-cost-charts/v1',
    capturedAt,
    precision: 'chart labels rounded to USD 1',
    declinedTasksMarker: { marker: '*', meaning: DECLINED_NOTE },
    evaluations,
  };
}

function serializeCapture(capture) {
  return `${JSON.stringify(capture, null, 2)}\n`;
}

function summarizeCapture(out, capture) {
  return {
    out,
    evaluations: capture.evaluations.map(({ slug, rows }) => ({ slug, bars: rows.length })),
  };
}

/** Captures every evaluation chart and writes the JSON snapshot; the browser is always closed. */
async function run({ argv = process.argv, chromium, filesystem = fs, now = () => new Date(), log = console.log, evaluations = EVALUATIONS }) {
  const out = resolveOutputPath(argv);
  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage(PAGE_OPTIONS);
    page.setDefaultTimeout(NAVIGATION_TIMEOUT_MS);
    const captured = [];
    for (const evaluation of evaluations) {
      captured.push(await captureEvaluation(page, evaluation, { log }));
    }
    const capture = buildCaptureDocument({ capturedAt: now().toISOString(), evaluations: captured });
    filesystem.mkdirSync(path.dirname(out), { recursive: true });
    filesystem.writeFileSync(out, serializeCapture(capture));
    log(JSON.stringify(summarizeCapture(out, capture), null, 2));
    return capture;
  } finally {
    await browser.close();
  }
}

/** CLI entry: resolves the real Playwright browser lazily and reports failures. */
async function main({ exit = process.exit, error = console.error, chromium, ...options } = {}) {
  try {
    return await run({ ...options, chromium: chromium ?? require('playwright').chromium });
  } catch (failure) {
    error(failure);
    exit(1);
  }
}

if (require.main === module) {
  main();
}

module.exports = {
  EVALUATIONS,
  printedNotes,
  resolveOutputPath,
  decodeEntities,
  parseUsd,
  parseTicks,
  parseLabels,
  parseChartRows,
  clickTotalCostTab,
  readTotalCostChart,
  captureEvaluation,
  buildCaptureDocument,
  serializeCapture,
  summarizeCapture,
  run,
  main,
};
