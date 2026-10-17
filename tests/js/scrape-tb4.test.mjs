import { describe, test } from 'node:test';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import { readFileSync, rmSync } from 'node:fs';
import { join } from 'node:path';
import { REPO_ROOT, makeTempDir, runScriptWithFakePlaywright } from './helpers/run-script.mjs';

const require = createRequire(import.meta.url);
const { createFakeChromium } = require('./helpers/fake-playwright.cjs');
const { buildFakeDocument, buildFakeLocation, withGlobals } = require('./helpers/fake-dom.cjs');
const tb4 = require('../../scripts/scrape-tb4.js');

const SCRIPT = join(REPO_ROOT, 'scripts', 'scrape-tb4.js');
const TB4_URL = 'https://www.tbench.ai/leaderboard/terminal-bench/4.0';
const LEADERBOARD_HREF = 'https://www.tbench.ai/leaderboard/terminal-bench/4.0';
const SCRAPED_AT_PATTERN = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$/;
const SCRAPED_AT = '2026-10-17T12:00:00.000Z';
const FIXED_NOW = () => new Date(SCRAPED_AT);
const LONG_SCRIPT_CHARS = 250000;
const NO_OP_FS = { mkdirSync() {}, writeFileSync() {} };
const DEFAULT_OUT = join(REPO_ROOT, 'data', 'tb4-scrape.json');

// A rendered-page fixture covering every cleaning, filtering and truncation rule.
const PAGE = {
  finalUrl: 'https://www.tbench.ai/leaderboard/terminal-bench/4.0?view=full',
  title: '  Terminal-Bench   4.0 \n Leaderboard ',
  bodyText: 'Intro \n\t text   here ',
  rows: [
    { cells: [{ innerText: '  Rank ' }, { innerText: 'Agent' }, { innerText: '  Score\n' }] },
    { cells: [{ innerText: '1' }, { innerText: 'GPT-6   Astra' }, { innerText: '70.5' }, { innerText: '' }] },
    { cells: [{ innerText: 'only' }, { innerText: 'two' }] },
    { cells: [] },
    { cells: [{ innerText: ' a ' }, { innerText: ' b ' }, { innerText: ' c ' }] },
    { cells: [{}, { innerText: 'x' }, { innerText: 'y' }] },
  ],
  anchors: [
    { innerText: '  Home  ', href: 'https://www.tbench.ai/' },
    { innerText: '', href: LEADERBOARD_HREF },
    { innerText: '', href: 'https://www.tbench.ai/about' },
    { innerText: ' ', href: 'https://www.tbench.ai/careers' },
  ],
  scripts: [
    { textContent: 'window.__DATA__ = {"Claude Opus 5": 1}' },
    { textContent: 'console.log(1)' },
    { textContent: null },
    { textContent: `terminal-bench ${'x'.repeat(LONG_SCRIPT_CHARS)}` },
  ],
};

// What page.evaluate returns for PAGE: raw DOM values, before any cleaning.
const RAW_PAGE = {
  finalUrl: PAGE.finalUrl,
  title: PAGE.title,
  bodyText: PAGE.bodyText,
  rows: [
    ['  Rank ', 'Agent', '  Score\n'],
    ['1', 'GPT-6   Astra', '70.5', ''],
    ['only', 'two'],
    [],
    [' a ', ' b ', ' c '],
    [undefined, 'x', 'y'],
  ],
  links: [
    { text: '  Home  ', href: 'https://www.tbench.ai/' },
    { text: '', href: LEADERBOARD_HREF },
    { text: '', href: 'https://www.tbench.ai/about' },
    { text: ' ', href: 'https://www.tbench.ai/careers' },
  ],
  scripts: [
    'window.__DATA__ = {"Claude Opus 5": 1}',
    'console.log(1)',
    null,
    `terminal-bench ${'x'.repeat(LONG_SCRIPT_CHARS)}`,
  ],
};

// The published capture after cleaning, without scrapedAt.
const EXPECTED_CAPTURE = {
  source: TB4_URL,
  finalUrl: PAGE.finalUrl,
  title: PAGE.title,
  text: 'Intro text here',
  rows: [
    ['Rank', 'Agent', 'Score'],
    ['1', 'GPT-6 Astra', '70.5', ''],
    ['a', 'b', 'c'],
    ['', 'x', 'y'],
  ],
  links: [
    { text: 'Home', href: 'https://www.tbench.ai/' },
    { text: '', href: LEADERBOARD_HREF },
  ],
  scripts: [
    'window.__DATA__ = {"Claude Opus 5": 1}',
    `terminal-bench ${'x'.repeat(LONG_SCRIPT_CHARS)}`.slice(0, LONG_SCRIPT_CHARS),
  ],
};

const BROWSER_CALLS = [
  'chromium.launch',
  'browser.newPage',
  'page.setDefaultTimeout',
  'page.goto',
  'page.waitForTimeout',
  'page.evaluate',
  'browser.close',
];

describe('scrape-tb4 CLI (characterization of the current behaviour)', () => {
  test('writes the capture JSON to the argv path and prints a summary', () => {
    const dir = makeTempDir('tb4-cli-out-');
    try {
      const out = join(dir, 'capture.json');
      const run = runScriptWithFakePlaywright({ script: SCRIPT, args: [out], scenario: { page: PAGE } });

      assert.equal(run.status, 0, run.stderr);
      const raw = readFileSync(out, 'utf8');
      const capture = JSON.parse(raw);
      const { scrapedAt, ...document } = capture;
      assert.match(scrapedAt, SCRAPED_AT_PATTERN);
      assert.deepEqual(Object.keys(capture), ['scrapedAt', 'source', 'finalUrl', 'title', 'text', 'rows', 'links', 'scripts']);
      assert.deepEqual(document, EXPECTED_CAPTURE);
      assert.equal(raw, `${JSON.stringify(capture, null, 2)}\n`);

      assert.deepEqual(JSON.parse(run.stdout), {
        out,
        finalUrl: PAGE.finalUrl,
        title: PAGE.title,
        tableRows: 4,
        bodyChars: 'Intro text here'.length,
      });
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });

  test('drives the browser with the 1440x1200 viewport, timeouts and wait settings', () => {
    const dir = makeTempDir('tb4-cli-calls-');
    try {
      const run = runScriptWithFakePlaywright({
        script: SCRIPT,
        args: [join(dir, 'capture.json')],
        scenario: { page: PAGE },
      });

      assert.equal(run.status, 0, run.stderr);
      assert.deepEqual(run.calls.map((entry) => entry.call), BROWSER_CALLS);
      assert.deepEqual(run.calls[0].options, { headless: true });
      assert.deepEqual(run.calls[1].options, {
        viewport: { width: 1440, height: 1200 },
        userAgent: 'ValueRank research snapshot; contact via repository metadata',
      });
      assert.equal(run.calls[2].timeout, 120000);
      assert.deepEqual(run.calls[3], { call: 'page.goto', url: TB4_URL, options: { waitUntil: 'domcontentloaded' } });
      assert.equal(run.calls[4].ms, 7000);
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });

  test('reports navigation failures on stderr and exits with status 1', () => {
    const dir = makeTempDir('tb4-cli-fail-');
    try {
      const out = join(dir, 'capture.json');
      const run = runScriptWithFakePlaywright({
        script: SCRIPT,
        args: [out],
        scenario: { page: PAGE, gotoError: 'net::ERR_NAME_NOT_RESOLVED' },
      });

      assert.equal(run.status, 1);
      assert.match(run.stderr, /net::ERR_NAME_NOT_RESOLVED/);
      assert.equal(run.stdout, '');
      assert.throws(() => readFileSync(out, 'utf8'), { code: 'ENOENT' });
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });
});

describe('output path', () => {
  test('uses the first command-line argument when one is given', () => {
    assert.equal(tb4.resolveOutputPath(['node', 'scrape-tb4.js', '/work/capture.json']), '/work/capture.json');
  });

  test('defaults to data/tb4-scrape.json under the repository root when no argument or an empty one is given', () => {
    assert.equal(tb4.resolveOutputPath(['node', 'scrape-tb4.js']), DEFAULT_OUT);
    assert.equal(tb4.resolveOutputPath(['node', 'scrape-tb4.js', '']), DEFAULT_OUT);
  });
});

describe('cleaning and filtering', () => {
  test('cleanText collapses whitespace runs, trims, and treats missing text as empty', () => {
    assert.equal(tb4.cleanText('  Intro \n\t text   here '), 'Intro text here');
    assert.equal(tb4.cleanText(undefined), '');
    assert.equal(tb4.cleanText(null), '');
  });

  test('cleanRows drops rows with fewer than three cells and cleans the cells that remain', () => {
    assert.deepEqual(tb4.cleanRows(RAW_PAGE.rows), EXPECTED_CAPTURE.rows);
  });

  test('cleanLinks keeps anchors with visible text or a leaderboard href and cleans their text', () => {
    assert.deepEqual(tb4.cleanLinks(RAW_PAGE.links), EXPECTED_CAPTURE.links);
  });

  test('selectScripts keeps leaderboard scripts case-insensitively and caps each at 250000 characters', () => {
    const long = `GPT-6 Astra ${'y'.repeat(LONG_SCRIPT_CHARS)}`;
    const scripts = tb4.selectScripts([
      'window.__DATA__ = {"Claude Opus 5": 1}',
      'console.log(1)',
      null,
      'TERMINAL-BENCH',
      long,
    ]);
    assert.deepEqual(scripts, [
      'window.__DATA__ = {"Claude Opus 5": 1}',
      'TERMINAL-BENCH',
      long.slice(0, LONG_SCRIPT_CHARS),
    ]);
    assert.equal(scripts[2].length, LONG_SCRIPT_CHARS);
  });
});

describe('capture document', () => {
  test('buildCaptureDocument assembles the published fields in their published key order', () => {
    const document = tb4.buildCaptureDocument({ scrapedAt: SCRAPED_AT, source: TB4_URL, page: RAW_PAGE });
    assert.deepEqual(Object.keys(document), ['scrapedAt', 'source', 'finalUrl', 'title', 'text', 'rows', 'links', 'scripts']);
    assert.deepEqual(document, { scrapedAt: SCRAPED_AT, ...EXPECTED_CAPTURE });
  });

  test('serializeCapture writes two-space JSON with a trailing newline', () => {
    const document = tb4.buildCaptureDocument({ scrapedAt: SCRAPED_AT, source: TB4_URL, page: RAW_PAGE });
    assert.equal(tb4.serializeCapture(document), `${JSON.stringify(document, null, 2)}\n`);
  });

  test('summarizeCapture reports the output path, page identity and table and text sizes', () => {
    const document = tb4.buildCaptureDocument({ scrapedAt: SCRAPED_AT, source: TB4_URL, page: RAW_PAGE });
    assert.deepEqual(tb4.summarizeCapture('/work/capture.json', document), {
      out: '/work/capture.json',
      finalUrl: PAGE.finalUrl,
      title: PAGE.title,
      tableRows: 4,
      bodyChars: 'Intro text here'.length,
    });
  });
});

describe('page-side reader', () => {
  test('readTb4Page returns the raw text, table cells, anchors and scripts of the rendered page', () => {
    const raw = withGlobals(
      { document: buildFakeDocument(PAGE), location: buildFakeLocation(PAGE) },
      () => tb4.readTb4Page(),
    );
    assert.deepEqual(raw, RAW_PAGE);
  });
});

describe('run (browser orchestration)', () => {
  test('drives the browser like the CLI and writes the capture, creating the output directory', async () => {
    const dir = makeTempDir('tb4-run-');
    try {
      const out = join(dir, 'nested', 'capture.json');
      const calls = [];
      const logs = [];
      const capture = await tb4.run({
        argv: ['node', 'scrape-tb4.js', out],
        chromium: createFakeChromium({ scenario: { page: PAGE }, record: (entry) => calls.push(entry) }),
        now: FIXED_NOW,
        log: (line) => logs.push(line),
      });

      assert.deepEqual(calls.map((entry) => entry.call), BROWSER_CALLS);
      assert.deepEqual(calls[0].options, { headless: true });
      assert.deepEqual(calls[1].options, {
        viewport: { width: 1440, height: 1200 },
        userAgent: 'ValueRank research snapshot; contact via repository metadata',
      });
      assert.equal(calls[2].timeout, 120000);
      assert.deepEqual(calls[3], { call: 'page.goto', url: TB4_URL, options: { waitUntil: 'domcontentloaded' } });
      assert.equal(calls[4].ms, 7000);
      assert.deepEqual(capture, { scrapedAt: SCRAPED_AT, ...EXPECTED_CAPTURE });
      assert.equal(readFileSync(out, 'utf8'), tb4.serializeCapture(capture));
      assert.deepEqual(logs.map((line) => JSON.parse(line)), [tb4.summarizeCapture(out, capture)]);
    } finally {
      rmSync(dir, { recursive: true, force: true });
    }
  });

  test('writes to data/tb4-scrape.json under the repository root when no output path is given', async () => {
    const mkdirs = [];
    const writes = [];
    await tb4.run({
      argv: ['node', 'scrape-tb4.js'],
      chromium: createFakeChromium({ scenario: { page: PAGE } }),
      filesystem: {
        mkdirSync: (dir, options) => mkdirs.push([dir, options]),
        writeFileSync: (file) => writes.push(file),
      },
      now: FIXED_NOW,
      log: () => {},
    });
    assert.deepEqual(mkdirs, [[join(REPO_ROOT, 'data'), { recursive: true }]]);
    assert.deepEqual(writes, [DEFAULT_OUT]);
  });

  test('closes the browser and rejects with the original error when navigation fails', async () => {
    const calls = [];
    await assert.rejects(
      tb4.run({
        argv: ['node', 'scrape-tb4.js'],
        chromium: createFakeChromium({
          scenario: { page: PAGE, gotoError: 'net::ERR_NAME_NOT_RESOLVED' },
          record: (entry) => calls.push(entry),
        }),
        filesystem: NO_OP_FS,
        now: FIXED_NOW,
        log: () => {},
      }),
      /net::ERR_NAME_NOT_RESOLVED/,
    );
    assert.equal(calls.at(-1).call, 'browser.close');
    assert.equal(calls.filter((entry) => entry.call === 'browser.close').length, 1);
  });
});

describe('main and entry point', () => {
  test('main sends failures to the error sink and exits with status 1', async () => {
    const errors = [];
    const exits = [];
    await tb4.main({
      argv: ['node', 'scrape-tb4.js'],
      chromium: createFakeChromium({ scenario: { launchError: 'no chromium' } }),
      filesystem: NO_OP_FS,
      now: FIXED_NOW,
      log: () => {},
      error: (failure) => errors.push(failure),
      exit: (code) => exits.push(code),
    });
    assert.equal(errors.length, 1);
    assert.equal(errors[0].message, 'no chromium');
    assert.deepEqual(exits, [1]);
  });

  test('main resolves with the capture and does not exit when the run succeeds', async () => {
    const errors = [];
    const exits = [];
    const capture = await tb4.main({
      argv: ['node', 'scrape-tb4.js'],
      chromium: createFakeChromium({ scenario: { page: PAGE } }),
      filesystem: NO_OP_FS,
      now: FIXED_NOW,
      log: () => {},
      error: (failure) => errors.push(failure),
      exit: (code) => exits.push(code),
    });
    assert.deepEqual(capture, { scrapedAt: SCRAPED_AT, ...EXPECTED_CAPTURE });
    assert.deepEqual(exits, []);
    assert.deepEqual(errors, []);
  });
});
