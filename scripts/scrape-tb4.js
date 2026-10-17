#!/usr/bin/env node
/**
 * Capture the current Terminal-Bench 4.0 leaderboard through its rendered
 * public page.  The site is client-rendered, so a browser capture is the
 * reproducible source snapshot used by the v1.4 builder.
 *
 * Usage: node scrape-tb4.js [outJson]
 */
const fs = require('fs');
const path = require('path');

const TB4_URL = 'https://www.tbench.ai/leaderboard/terminal-bench/4.0';
const DEFAULT_OUT = path.join(__dirname, '..', 'data', 'tb4-scrape.json');
const PAGE_OPTIONS = {
  viewport: { width: 1440, height: 1200 },
  userAgent: 'ValueRank research snapshot; contact via repository metadata',
};
const NAVIGATION_TIMEOUT_MS = 120000;
const RENDER_WAIT_MS = 7000;
const SCRIPT_CHAR_LIMIT = 250000;
const LEADERBOARD_MARKERS = /GPT-6 Astra|Claude Opus 5|leaderboard|terminal-bench/i;

/** The output path: the first CLI argument, or data/tb4-scrape.json. */
function resolveOutputPath(argv) {
  return argv[2] || DEFAULT_OUT;
}

/** Collapses whitespace and trims; missing text becomes an empty string. */
function cleanText(value) {
  return (value || '').replace(/\s+/g, ' ').trim();
}

/** Keeps rows with at least three cells and cleans every cell. */
function cleanRows(rows) {
  return rows
    .map((cells) => cells.map(cleanText))
    .filter((cells) => cells.length >= 3);
}

/** Keeps anchors that have visible text or point at the leaderboard. */
function cleanLinks(links) {
  return links
    .map(({ text, href }) => ({ text: cleanText(text), href }))
    .filter((link) => link.text || link.href.includes('leaderboard'));
}

/** Keeps leaderboard-related script bodies, each capped in length. */
function selectScripts(texts) {
  return texts
    .map((text) => text || '')
    .filter((text) => LEADERBOARD_MARKERS.test(text))
    .map((text) => text.slice(0, SCRIPT_CHAR_LIMIT));
}

/** Assembles the capture document; key order is part of the published format. */
function buildCaptureDocument({ scrapedAt, source, page }) {
  return {
    scrapedAt,
    source,
    finalUrl: page.finalUrl,
    title: page.title,
    text: cleanText(page.bodyText),
    rows: cleanRows(page.rows),
    links: cleanLinks(page.links),
    scripts: selectScripts(page.scripts),
  };
}

function serializeCapture(capture) {
  return `${JSON.stringify(capture, null, 2)}\n`;
}

function summarizeCapture(out, capture) {
  return {
    out,
    finalUrl: capture.finalUrl,
    title: capture.title,
    tableRows: capture.rows.length,
    bodyChars: capture.text.length,
  };
}

/**
 * Runs inside the page through page.evaluate, so it must stay self-contained.
 * It reads raw DOM values only; cleaning and filtering happen in Node.
 */
function readTb4Page() {
  return {
    finalUrl: location.href,
    title: document.title,
    bodyText: document.body.innerText,
    rows: Array.from(document.querySelectorAll('table tr, [role="row"]')).map((row) =>
      Array.from(row.querySelectorAll('th, td, [role="cell"]')).map((cell) => cell.innerText)),
    links: Array.from(document.querySelectorAll('a[href]')).map((a) => ({ text: a.innerText, href: a.href })),
    scripts: Array.from(document.querySelectorAll('script')).map((script) => script.textContent),
  };
}

/**
 * Captures the leaderboard and writes the JSON snapshot. Every dependency is
 * injectable; the browser is closed even when navigation or extraction fails.
 */
async function run({ argv = process.argv, chromium, filesystem = fs, now = () => new Date(), log = console.log }) {
  const out = resolveOutputPath(argv);
  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage(PAGE_OPTIONS);
    page.setDefaultTimeout(NAVIGATION_TIMEOUT_MS);
    await page.goto(TB4_URL, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(RENDER_WAIT_MS);
    const rawPage = await page.evaluate(readTb4Page);
    const capture = buildCaptureDocument({ scrapedAt: now().toISOString(), source: TB4_URL, page: rawPage });
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
  resolveOutputPath,
  cleanText,
  cleanRows,
  cleanLinks,
  selectScripts,
  buildCaptureDocument,
  serializeCapture,
  summarizeCapture,
  readTb4Page,
  run,
  main,
};
