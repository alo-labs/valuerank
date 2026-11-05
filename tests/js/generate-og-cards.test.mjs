import { describe, test } from 'node:test';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import { cpSync, existsSync, readFileSync, rmSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import * as og from '../../scripts/generate-og-cards.mjs';
import { REPO_ROOT, makeTempDir, runScriptWithFakePlaywright } from './helpers/run-script.mjs';

const require = createRequire(import.meta.url);
const { createFakeChromium } = require('./helpers/fake-playwright.cjs');

const SCRIPT = join(REPO_ROOT, 'scripts', 'generate-og-cards.mjs');
const SCRIPT_URL = new URL('../../scripts/generate-og-cards.mjs', import.meta.url);
const FIXTURES = new URL('./fixtures/og-cards/', import.meta.url);
const FIXTURE_ROOT = fileURLToPath(FIXTURES);

const CARD_IDS = [
  'index', 'rankings', 'models', 'plans', 'benchmarks', 'tb4', 'methodology', 'changelog', 'data',
  'model-alpha-one', 'model-beta-two', 'model-gamma-three', 'archive',
];

function fixture(name) {
  return readFileSync(new URL(name, FIXTURES), 'utf8');
}

function goldenCalls() {
  return fixture('run-calls.jsonl').split('\n').filter(Boolean).map((line) => JSON.parse(line));
}

function withRootPlaceholder(calls, root) {
  return calls.map((entry) => JSON.parse(JSON.stringify(entry).replaceAll(root, '<ROOT>')));
}

function fixturePublication() {
  return og.readPublication(FIXTURE_ROOT);
}

function fixtureModels() {
  return fixturePublication().rankings.models;
}

describe('card set', () => {
  test('buildCards makes one card per core page, roster model and the archive, all under site/og', () => {
    const root = join(REPO_ROOT, 'fixture-root');
    const cards = og.buildCards(root, fixturePublication());

    assert.deepEqual(cards.map((card) => card.id), CARD_IDS);
    assert.deepEqual(cards.map((card) => card.out), [
      join(root, 'site', 'og', 'index.png'),
      join(root, 'site', 'og', 'rankings.png'),
      join(root, 'site', 'og', 'models.png'),
      join(root, 'site', 'og', 'plans.png'),
      join(root, 'site', 'og', 'benchmarks.png'),
      join(root, 'site', 'og', 'tb4.png'),
      join(root, 'site', 'og', 'methodology.png'),
      join(root, 'site', 'og', 'changelog.png'),
      join(root, 'site', 'og', 'data.png'),
      join(root, 'site', 'og', 'models', 'alpha-one.png'),
      join(root, 'site', 'og', 'models', 'beta-two.png'),
      join(root, 'site', 'og', 'models', 'gamma-three.png'),
      join(root, 'site', 'og', 'archive.png'),
    ]);
    for (const card of cards) {
      assert.match(card.html, /^<!DOCTYPE html>/, card.id);
      assert.match(card.html, /v1\.9\.6/, card.id);
      assert.match(card.html, /fonts\.googleapis\.com\/css2\?family=IBM\+Plex/, card.id);
    }
  });
});

describe('core cards', () => {
  test('coreFacts gives each core page its path, copy and three numbers from the publication', () => {
    const publication = fixturePublication();
    const expected = {
      index: { path: '/', labels: ['Top Plan pick', 'Plan overall', 'Models ranked'], values: ['Beta <Two> & Co', '80.2', '2'] },
      rankings: { path: '/rankings/', labels: ['Models ranked', 'Dimensions', 'Default cost weight'], values: ['2 of 3', '3', '18.9%'] },
      models: { path: '/models/', labels: ['Roster models', 'Ranked', 'Developers'], values: ['3', '2', '2'] },
      plans: { path: '/plans/', labels: ['Best plan cost per basket run', 'Plan routes', 'Models priced on a plan'], values: ['$98.80', '2', '2'] },
      benchmarks: { path: '/benchmarks/', labels: ['Benchmark sources', 'Basket components', 'Cohort models'], values: ['2', '3', '3'] },
      tb4: { path: '/benchmarks/terminal-bench-4/', labels: ['Official rows', 'On the frontier', 'Cohort models matched'], values: ['2', '1', '1 of 3'] },
      methodology: { path: '/methodology/', labels: ['Dimensions', 'Cost weight'], values: ['3', '18.9%'] },
      changelog: { path: '/changelog/', labels: ['Latest release', 'Released', 'Releases recorded'], values: ['v1.9.6', 'October 8, 2026', '2'] },
      data: { path: '/data/', labels: ['JSON files', 'Model documents'], values: ['8', '3'] },
    };
    for (const [key, want] of Object.entries(expected)) {
      const facts = og.coreFacts(key, publication);
      assert.equal(facts.path, want.path, key);
      assert.deepEqual(facts.stats.map((stat) => stat.value), want.values, key);
      assert.deepEqual(facts.stats.map((stat) => stat.label), want.labels, key);
      assert.ok(facts.kicker && facts.headline && facts.description, key);
    }
  });

  test('coreFacts refuses a key that is not a core page', () => {
    assert.throws(() => og.coreFacts('pricing', fixturePublication()), /no core card for pricing/);
  });

  test('renderCoreCard escapes publication text and shows the headline, the page path and the numbers', () => {
    const facts = og.coreFacts('index', fixturePublication());
    const html = og.renderCoreCard(facts, 'v1.9.6');

    assert.ok(html.includes(og.escapeHtml(facts.headline)));
    assert.match(html, /stat-value long">Beta &lt;Two&gt; &amp; Co</);
    assert.doesNotMatch(html, /<Two>/);
    assert.match(html, /class="stat-value">80\.2</);
    assert.match(html, /valuerank\.alolabs\.dev\//);
    assert.match(html, /class="frame"/);
  });

  test('renderCoreCard marks long stat values so they fit the card and leaves short ones at full size', () => {
    const html = og.renderCoreCard(og.coreFacts('changelog', fixturePublication()), 'v1.9.6');

    assert.match(html, /class="stat-value long">October 8, 2026</);
    assert.match(html, /class="stat-value">v1\.9\.6</);
    assert.match(html, /class="stat-value">2</);
  });
});

describe('model cards', () => {
  test('modelFacts gives a ranked model its rank pills, numbers and evidence grade', () => {
    const [alpha] = fixtureModels();

    assert.deepEqual(og.modelFacts(alpha), {
      slug: 'alpha-one',
      name: 'Alpha One',
      developer: 'Acme AI',
      path: '/models/alpha-one/',
      grade: 'measured',
      pills: ['Plan #2', 'API #1'],
      stats: [
        { value: '75.7', label: 'Plan overall' },
        { value: '74.3', label: 'API overall' },
        { value: '74.6', label: 'Quality' },
      ],
    });
  });

  test('modelFacts shows unranked pills and dashes for a model outside the ranking', () => {
    const facts = og.modelFacts(fixtureModels()[2]);

    assert.deepEqual(facts.pills, ['Plan unranked', 'API unranked']);
    assert.deepEqual(facts.stats.map((stat) => stat.value), ['—', '—', '—']);
    assert.equal(facts.grade, 'missing');
  });

  test('renderModelCard shows name, developer, both ranks, overall, quality and the evidence grade', () => {
    const html = og.renderModelCard(og.modelFacts(fixtureModels()[0]), 'v1.9.6');

    for (const text of ['Acme AI', 'Alpha One', 'Plan #2', 'API #1', '75.7', '74.3', '74.6', 'Evidence: measured', '/models/alpha-one/']) {
      assert.ok(html.includes(text), text);
    }
    assert.match(html, /class="pill grade g-measured">Evidence: measured</);
  });

  test('renderModelCard shows unranked pills for a model outside the ranking', () => {
    const html = og.renderModelCard(og.modelFacts(fixtureModels()[2]), 'v1.9.6');

    assert.ok(html.includes('Plan unranked') && html.includes('API unranked'));
    assert.match(html, /class="pill grade g-missing">Evidence: missing</);
  });

  test('renderModelCard escapes the model name and only emits known evidence classes', () => {
    const beta = fixtureModels()[1];
    const html = og.renderModelCard(og.modelFacts(beta), 'v1.9.6');
    assert.ok(html.includes('Beta &lt;Two&gt; &amp; Co'));
    assert.doesNotMatch(html, /<Two>/);
    assert.match(html, /class="pill grade g-estimate">Evidence: estimate</);

    const forged = og.renderModelCard(og.modelFacts({ ...beta, grade: 'estimate" onload="alert(1)' }), 'v1.9.6');
    assert.doesNotMatch(forged, /onload="alert/);
    assert.match(forged, /class="pill grade g-missing"/);
  });
});

describe('archive card and escaping', () => {
  test('renderArchiveCard names the archived v0.3 snapshot and its path', () => {
    const html = og.renderArchiveCard('v1.9.6');

    assert.match(html, /Coding Agent ValueRank/);
    assert.match(html, />Archived</);
    assert.match(html, /valuerank\.alolabs\.dev\/archive\/coding-agents-v0\.3\//);
  });

  test('escapeHtml escapes the markup characters in text and leaves plain text alone', () => {
    assert.equal(og.escapeHtml(`<a href='x'>Tom & "Jerry"</a>`), '&lt;a href=&#39;x&#39;&gt;Tom &amp; &quot;Jerry&quot;&lt;/a&gt;');
    assert.equal(og.escapeHtml('plain 80.2'), 'plain 80.2');
  });
});

describe('publication reading', () => {
  test('readPublication loads the public documents and counts the JSON files under site/data', () => {
    const publication = og.readPublication(FIXTURE_ROOT);

    assert.deepEqual(Object.keys(publication).sort(), ['benchmarks', 'changelog', 'dataFileCount', 'plans', 'rankings', 'tb4']);
    assert.equal(publication.rankings.version, 'v1.9.6');
    assert.equal(publication.tb4.frontierCount, 1);
    assert.equal(publication.dataFileCount, 8);
  });

  test('readPublication fails when a public document is missing', () => {
    const root = makeTempDir('og-read-missing-');
    try {
      assert.throws(() => og.readPublication(root), /ENOENT/);
    } finally {
      rmSync(root, { recursive: true, force: true });
    }
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
        publication: fixturePublication(),
        chromium: createFakeChromium({ record: (entry) => calls.push(entry) }),
        log: (line) => lines.push(line),
      });

      const cards = og.buildCards(root, fixturePublication());
      assert.deepEqual(withRootPlaceholder(calls, root), goldenCalls());
      assert.deepEqual(lines, cards.map((card) => `wrote ${card.out}`));
      for (const card of cards) {
        assert.equal(readFileSync(join(root, '.tmp', 'og', `${card.id}.html`), 'utf8'), card.html, card.id);
        assert.equal(existsSync(card.out), true, `missing screenshot ${card.out}`);
      }
    } finally {
      rmSync(root, { recursive: true, force: true });
    }
  });

  test('reads the publication from the root when none is passed in', async () => {
    const root = makeTempDir('og-run-read-');
    try {
      cpSync(join(FIXTURE_ROOT, 'site'), join(root, 'site'), { recursive: true });
      const lines = [];
      await og.run({ root, chromium: createFakeChromium(), log: (line) => lines.push(line) });

      assert.equal(lines.length, CARD_IDS.length);
      assert.equal(existsSync(join(root, 'site', 'og', 'models', 'beta-two.png')), true);
    } finally {
      rmSync(root, { recursive: true, force: true });
    }
  });

  test('reads the publication before launching a browser, so missing data never starts Chromium', async () => {
    const root = makeTempDir('og-run-nodata-');
    try {
      const calls = [];
      await assert.rejects(
        og.run({
          root,
          chromium: createFakeChromium({ record: (entry) => calls.push(entry) }),
          log: () => {},
        }),
        /ENOENT/,
      );
      assert.deepEqual(calls, []);
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
          publication: fixturePublication(),
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
          publication: fixturePublication(),
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
      publication: fixturePublication(),
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
        publication: fixturePublication(),
        chromium: createFakeChromium(),
        log: () => {},
        exit: (code) => exits.push(code),
      });
      assert.deepEqual(exits, []);
      assert.equal(existsSync(join(root, 'site', 'og', 'archive.png')), true);
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
