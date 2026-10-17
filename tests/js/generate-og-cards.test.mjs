import { describe, test } from 'node:test';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import { existsSync, readFileSync, rmSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import * as og from '../../scripts/generate-og-cards.mjs';
import { REPO_ROOT, makeTempDir, runScriptWithFakePlaywright } from './helpers/run-script.mjs';

const require = createRequire(import.meta.url);
const { createFakeChromium } = require('./helpers/fake-playwright.cjs');

const SCRIPT = join(REPO_ROOT, 'scripts', 'generate-og-cards.mjs');
const SCRIPT_URL = new URL('../../scripts/generate-og-cards.mjs', import.meta.url);
const FIXTURES = new URL('./fixtures/og-cards/', import.meta.url);

function fixture(name) {
  return readFileSync(new URL(name, FIXTURES), 'utf8');
}

function goldenCalls() {
  return fixture('run-calls.jsonl').split('\n').filter(Boolean).map((line) => JSON.parse(line));
}

function withRootPlaceholder(calls, root) {
  return calls.map((entry) => JSON.parse(JSON.stringify(entry).replaceAll(root, '<ROOT>')));
}

describe('share card definitions', () => {
  test('buildCards lists the home, coding-agents and tb4 cards with their site output paths', () => {
    const root = join(REPO_ROOT, 'fixture-root');
    const cards = og.buildCards(root);

    assert.deepEqual(cards.map((card) => card.id), ['home', 'coding-agents', 'tb4']);
    assert.deepEqual(cards.map((card) => card.out), [
      join(root, 'site', 'og.png'),
      join(root, 'site', 'coding-agents', 'og.png'),
      join(root, 'site', 'tb4', 'og.png'),
    ]);
  });

  test('each card html is byte-identical to the markup the script has always produced', () => {
    assert.equal(og.renderHomeCard(), fixture('home.html'));
    assert.equal(og.renderCodingAgentsCard(), fixture('coding-agents.html'));
    assert.equal(og.renderTb4Card(), fixture('tb4.html'));
  });

  test('each card shows its brand, title, subtitle and pill labels', () => {
    const home = og.renderHomeCard();
    assert.match(home, /<div class="brand">ValueRank<\/div>/);
    assert.match(home, /<h1 class="title">ValueRank<\/h1>/);
    assert.match(home, /Frontier models ranked on real-world value/);
    assert.match(home, /<\/span> v1\.4\.0<\/div>/);
    assert.match(home, /<\/span> 21 models<\/div>/);

    const coding = og.renderCodingAgentsCard();
    assert.match(coding, /<h1 class="title compact">Coding Agent ValueRank<\/h1>/);
    assert.match(coding, /<div class="subtitle">value per dollar<\/div>/);
    assert.match(coding, /<\/span> Historical<\/div>/);
    assert.match(coding, /<\/span> 42 agents<\/div>/);

    const tb4 = og.renderTb4Card();
    assert.match(tb4, /<h1 class="title">Terminal-Bench 4\.0<\/h1>/);
    assert.match(tb4, /<div class="subtitle">Score vs Cost<\/div>/);
    assert.match(tb4, /<\/span> Dominated<\/div>/);
    assert.match(tb4, /<\/span> Pareto frontier<\/div>/);
  });
});

describe('run (browser orchestration)', () => {
  test('renders each card HTML under .tmp/og, screenshots it at 1200x630 and logs each output', async () => {
    const root = makeTempDir('og-run-');
    try {
      const calls = [];
      const lines = [];
      await og.run({
        root,
        chromium: createFakeChromium({ record: (entry) => calls.push(entry) }),
        log: (line) => lines.push(line),
      });

      assert.deepEqual(withRootPlaceholder(calls, root), goldenCalls());
      assert.deepEqual(lines, [
        `wrote ${join(root, 'site', 'og.png')}`,
        `wrote ${join(root, 'site', 'coding-agents', 'og.png')}`,
        `wrote ${join(root, 'site', 'tb4', 'og.png')}`,
      ]);
      assert.equal(readFileSync(join(root, '.tmp', 'og', 'home.html'), 'utf8'), og.renderHomeCard());
      assert.equal(readFileSync(join(root, '.tmp', 'og', 'coding-agents.html'), 'utf8'), og.renderCodingAgentsCard());
      assert.equal(readFileSync(join(root, '.tmp', 'og', 'tb4.html'), 'utf8'), og.renderTb4Card());
      for (const card of og.buildCards(root)) {
        assert.equal(existsSync(card.out), true, `missing screenshot ${card.out}`);
      }
    } finally {
      rmSync(root, { recursive: true, force: true });
    }
  });

  test('does not create the working directory when the browser cannot be launched', async () => {
    const root = makeTempDir('og-run-launch-');
    try {
      await assert.rejects(
        og.run({
          root,
          chromium: createFakeChromium({ scenario: { launchError: 'no browser' } }),
          log: () => {},
        }),
        /no browser/,
      );
      assert.equal(existsSync(join(root, '.tmp')), false);
      assert.equal(existsSync(join(root, 'site')), false);
    } finally {
      rmSync(root, { recursive: true, force: true });
    }
  });

  test('closes the browser and rejects when a screenshot fails', async () => {
    const root = makeTempDir('og-run-fail-');
    try {
      const calls = [];
      await assert.rejects(
        og.run({
          root,
          chromium: createFakeChromium({
            scenario: { screenshotError: 'disk full' },
            record: (entry) => calls.push(entry),
          }),
          log: () => {},
        }),
        /disk full/,
      );
      assert.equal(calls.at(-1).call, 'browser.close');
    } finally {
      rmSync(root, { recursive: true, force: true });
    }
  });
});

describe('entry points', () => {
  test('main logs a launch failure through the error sink and exits with status 1', async () => {
    const errors = [];
    const exits = [];
    await og.main({
      root: makeTempDir('og-main-fail-'),
      chromium: createFakeChromium({ scenario: { launchError: 'no browser installed' } }),
      error: (failure) => errors.push(failure),
      exit: (code) => exits.push(code),
    });

    assert.deepEqual(exits, [1]);
    assert.equal(errors.length, 1);
    assert.equal(errors[0].message, 'no browser installed');
  });

  test('main completes the run without exiting when every screenshot succeeds', async () => {
    const root = makeTempDir('og-main-ok-');
    try {
      const exits = [];
      await og.main({
        root,
        chromium: createFakeChromium(),
        log: () => {},
        exit: (code) => exits.push(code),
      });
      assert.deepEqual(exits, []);
      assert.equal(existsSync(join(root, 'site', 'tb4', 'og.png')), true);
    } finally {
      rmSync(root, { recursive: true, force: true });
    }
  });

  test('isEntryPoint is true only for the module file that is being executed', () => {
    assert.equal(og.isEntryPoint(fileURLToPath(SCRIPT_URL), SCRIPT_URL.href), true);
    assert.equal(og.isEntryPoint(undefined, SCRIPT_URL.href), false);
    assert.equal(og.isEntryPoint(fileURLToPath(import.meta.url), SCRIPT_URL.href), false);
    assert.equal(og.isEntryPoint('/no/such/file.mjs', SCRIPT_URL.href), false);
  });

  test('the CLI runs the browser through the fake, then exits 1 when the launch fails', () => {
    const run = runScriptWithFakePlaywright({
      script: SCRIPT,
      scenario: { launchError: 'fake launch failed' },
    });

    assert.equal(run.status, 1);
    assert.match(run.stderr, /fake launch failed/);
    assert.deepEqual(run.calls.map((entry) => entry.call), ['chromium.launch']);
  });
});
