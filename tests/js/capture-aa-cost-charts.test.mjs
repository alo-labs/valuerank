import { describe, test } from 'node:test';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import { join } from 'node:path';
import { REPO_ROOT, runScriptWithFakePlaywright } from './helpers/run-script.mjs';

const require = createRequire(import.meta.url);
const { withGlobals } = require('./helpers/fake-dom.cjs');
const charts = require('../../scripts/capture-aa-cost-charts.js');

const SCRIPT = join(REPO_ROOT, 'scripts', 'capture-aa-cost-charts.js');
const CAPTURED_AT = '2026-10-19T19:00:00.000Z';
const FIXED_NOW = () => new Date(CAPTURED_AT);

// A rendered chart: two bars with stacked-segment labels below their totals, one
// declined-tasks total, one tick without any label, and an axis label far from every bar.
const CHART_HTML = [
  '<div class="chart"><svg>',
  '<text x="45.0" y="231.0" fill="white">$5</text>',
  '<text x="45.2" y="205.5" fill="black">$9</text>',
  '<text x="95.1" y="204.5" fill="black">$1,015*</text>',
  '<text x="95.0" y="230.0" fill="white">$600</text>',
  '<text x="44.9" y="230.0" fill="white">Input</text>',
  '<text x="600.0" y="10.0" fill="black">$1.2k</text>',
  '<g transform="translate(45.18,223)" style="overflow: visible;"><g style="x"><svg><title>GPT-6 Luna (max)</title></svg></g></g>',
  '<g transform="translate(95.15,223)"><svg><title>Claude &amp; Co (xhigh)</title></svg></g>',
  '<g transform="translate(300.0,223)"><svg><title>No label model</title></svg></g>',
  '</svg></div>',
].join('');

describe('pure helpers', () => {
  test('resolveOutputPath prefers the CLI argument', () => {
    assert.equal(charts.resolveOutputPath(['node', 'script', 'out.json']), 'out.json');
    assert.match(charts.resolveOutputPath(['node', 'script']), /data[\\/]aa[\\/]cost_charts_capture\.json$/);
  });

  test('decodeEntities handles the entities that appear in labels', () => {
    assert.equal(charts.decodeEntities('A &amp; B &lt;c&gt; &quot;d&quot; &#39;e&#x27;'), 'A & B <c> "d" \'e\'');
  });

  test('parseUsd reads dollars, thousands separators, k suffix and the declined marker', () => {
    assert.equal(charts.parseUsd('$9'), 9);
    assert.equal(charts.parseUsd(' $1,015* '), 1015);
    assert.equal(charts.parseUsd('$12.5'), 12.5);
    assert.equal(charts.parseUsd('$1.2k'), 1200);
    assert.equal(charts.parseUsd('Input'), null);
  });

  test('parseTicks and parseLabels read positions and decoded text', () => {
    assert.deepEqual(charts.parseTicks(CHART_HTML), [
      { x: 45.18, model: 'GPT-6 Luna (max)' },
      { x: 95.15, model: 'Claude & Co (xhigh)' },
      { x: 300, model: 'No label model' },
    ]);
    assert.equal(charts.parseLabels(CHART_HTML).length, 6);
  });

  test('parseChartRows takes the topmost dollar label at each bar as its total', () => {
    assert.deepEqual(charts.parseChartRows(CHART_HTML), [
      { model: 'GPT-6 Luna (max)', totalUsdLabel: '$9', totalUsd: 9, declinedTasks: false },
      { model: 'Claude & Co (xhigh)', totalUsdLabel: '$1,015*', totalUsd: 1015, declinedTasks: true },
      { model: 'No label model', totalUsdLabel: null, totalUsd: null, declinedTasks: false },
    ]);
  });

  test('buildCaptureDocument, serializeCapture and summarizeCapture', () => {
    const capture = charts.buildCaptureDocument({ capturedAt: CAPTURED_AT, evaluations: [{ slug: 's', rows: [1, 2] }] });
    assert.deepEqual(Object.keys(capture), ['schemaVersion', 'capturedAt', 'precision', 'declinedTasksMarker', 'evaluations']);
    assert.equal(capture.declinedTasksMarker.marker, '*');
    assert.ok(charts.serializeCapture(capture).endsWith('}\n'));
    assert.deepEqual(charts.summarizeCapture('o.json', capture), { out: 'o.json', evaluations: [{ slug: 's', bars: 2 }] });
  });
});

// A tiny DOM for the in-page functions: elements with text, children, parents and events.
function element({ text = '', svgTexts = 0, outerHTML = '<div/>', children = [] } = {}) {
  const node = {
    textContent: text,
    children,
    parentElement: null,
    outerHTML,
    events: [],
    scrolled: null,
    querySelectorAll: (selector) => (selector === 'svg text' ? Array.from({ length: svgTexts }) : []),
    scrollIntoView(options) {
      node.scrolled = options;
    },
    dispatchEvent(event) {
      node.events.push(event.type);
      return true;
    },
  };
  return node;
}

class FakeMouseEvent {
  constructor(type, init) {
    this.type = type;
    this.init = init;
  }
}

function inPage(elements, action) {
  const documentStub = { querySelectorAll: (selector) => (selector === '*' ? elements : []) };
  return withGlobals(
    { document: documentStub, location: { href: 'https://example.test/page' }, MouseEvent: FakeMouseEvent },
    action,
  );
}

describe('in-page functions', () => {
  test('clickTotalCostTab scrolls the exact-text leaf into view and sends the full mouse sequence', () => {
    const parent = element({ text: 'Total Cost to Run', children: [{}] });
    const leaf = element({ text: '  Total Cost to Run ' });
    const other = element({ text: 'Cost per Task' });
    const empty = element({ text: undefined });
    assert.equal(inPage([parent, other, empty, leaf], () => charts.clickTotalCostTab('Total Cost to Run')), true);
    assert.deepEqual(leaf.scrolled, { block: 'center' });
    assert.deepEqual(leaf.events, ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click']);
    assert.deepEqual(parent.events, []);
  });

  test('clickTotalCostTab reports a missing tab', () => {
    assert.equal(inPage([element({ text: 'Other' })], () => charts.clickTotalCostTab('Total Cost to Run')), false);
  });

  test('readTotalCostChart climbs from the smallest title to the chart container', () => {
    const container = element({ text: 'Model X: Total Cost to Run  chart', svgTexts: 3, outerHTML: '<div>chart</div>' });
    const wrapper = element({ text: 'Section Model X: Total Cost to Run' });
    const title = element({ text: 'Model X: Total Cost to Run' });
    title.parentElement = wrapper;
    wrapper.parentElement = container;
    const unrelated = element({ text: undefined });
    const result = inPage([unrelated, wrapper, title], () => charts.readTotalCostChart(': Total Cost to Run'));
    assert.deepEqual(result, { title: 'Model X: Total Cost to Run', html: '<div>chart</div>', finalUrl: 'https://example.test/page' });
  });

  test('readTotalCostChart returns null without a title or without a chart ancestor', () => {
    assert.equal(inPage([element({ text: 'nothing' })], () => charts.readTotalCostChart(': Total Cost to Run')), null);
    const orphan = element({ text: 'A: Total Cost to Run' });
    assert.equal(inPage([orphan], () => charts.readTotalCostChart(': Total Cost to Run')), null);
  });
});

// A scripted page: each goto consumes the next outcome for the in-page calls.
function scriptedPage(outcomes, calls) {
  let current = null;
  return {
    setDefaultTimeout(ms) {
      calls.push(['setDefaultTimeout', ms]);
    },
    async goto(url) {
      calls.push(['goto', url]);
      current = outcomes.shift();
      if (current.gotoError) {
        throw new Error(current.gotoError);
      }
    },
    async waitForTimeout(ms) {
      calls.push(['wait', ms]);
    },
    async evaluate(fn) {
      calls.push(['evaluate', fn.name]);
      return fn.name === 'clickTotalCostTab' ? current.tab : current.chart;
    },
    async content() {
      calls.push(['content']);
      return current.content || '';
    },
  };
}

function fakeChromium(page, calls) {
  return {
    async launch(options) {
      calls.push(['launch', options]);
      return {
        async newPage() {
          return page;
        },
        async close() {
          calls.push(['close']);
        },
      };
    },
  };
}

const NOTE = 'The model or provider declined some tasks on safety grounds';
const GOOD = { tab: true, chart: { title: 'X: Total Cost to Run', html: CHART_HTML, finalUrl: 'https://final' }, content: `x "* ${NOTE}" y "* ${NOTE}"` };

describe('printedNotes', () => {
  test('reads each "* <text>" note AA prints once, in page order, and nothing else', () => {
    assert.deepEqual(charts.printedNotes(`a "* ${NOTE}" b "* Second note on the page here" "* ${NOTE}" "* short" "* lower case is not a note"`),
      [NOTE, 'Second note on the page here']);
    assert.deepEqual(charts.printedNotes('<html>no notes</html>'), []);
  });
});

describe('captureEvaluation and run', () => {
  test('captureEvaluation retries transient failures and reports each one', async () => {
    const calls = [];
    const logs = [];
    const page = scriptedPage(
      [{ gotoError: 'upstream request failed' }, { tab: false }, { tab: true, chart: null }, { tab: true, chart: { title: 't', html: '<svg></svg>', finalUrl: 'f' } }, GOOD],
      calls,
    );
    const result = await charts.captureEvaluation(page, { slug: 'fc', url: 'https://fc' }, { attempts: 5, log: (line) => logs.push(line) });
    assert.equal(result.slug, 'fc');
    assert.equal(result.chartTitle, 'X: Total Cost to Run');
    assert.equal(result.rows.length, 3);
    // O103: the page's printed notes on the chart, and none on a bar.
    assert.deepEqual(result.notes, [NOTE]);
    assert.ok(result.rows.every((row) => Array.isArray(row.notes) && row.notes.length === 0));
    assert.deepEqual(logs, [
      'attempt 1 for fc failed: upstream request failed',
      'attempt 2 for fc failed: no "Total Cost to Run" tab on https://fc',
      'attempt 3 for fc failed: no ": Total Cost to Run" chart on https://fc',
      'attempt 4 for fc failed: no bars in the cost chart on https://fc',
    ]);
  });

  test('captureEvaluation gives up after the attempt budget with the last error', async () => {
    const page = scriptedPage([{ tab: false }], []);
    await assert.rejects(charts.captureEvaluation(page, { slug: 'it', url: 'https://it' }, { attempts: 1 }), /could not capture it: no "Total Cost to Run" tab/);
  });

  test('captureEvaluation uses the default attempt budget and a silent log', async () => {
    const page = scriptedPage([{ tab: false }, { tab: false }, { tab: false }, { tab: false }], []);
    await assert.rejects(charts.captureEvaluation(page, { slug: 'd', url: 'https://d' }), /could not capture d/);
  });

  test('captureEvaluation with no attempts reports that none was made', async () => {
    await assert.rejects(charts.captureEvaluation(scriptedPage([], []), { slug: 'z', url: 'u' }, { attempts: 0 }), /no attempt made/);
  });

  test('run captures every evaluation, writes the document and closes the browser', async () => {
    const calls = [];
    const written = {};
    const filesystem = {
      mkdirSync(dir, options) {
        written.dir = [dir, options];
      },
      writeFileSync(file, text) {
        written.file = [file, text];
      },
    };
    const logs = [];
    const page = scriptedPage([GOOD, GOOD], calls);
    const capture = await charts.run({
      argv: ['node', 'script', '/tmp/out/costs.json'],
      chromium: fakeChromium(page, calls),
      filesystem,
      now: FIXED_NOW,
      log: (line) => logs.push(line),
    });
    assert.equal(capture.capturedAt, CAPTURED_AT);
    assert.deepEqual(capture.evaluations.map((evaluation) => evaluation.slug), ['frontiercode', 'itbench-aa']);
    assert.deepEqual(written.dir, ['/tmp/out', { recursive: true }]);
    assert.equal(written.file[0], '/tmp/out/costs.json');
    assert.deepEqual(JSON.parse(logs.at(-1)).evaluations, [{ slug: 'frontiercode', bars: 3 }, { slug: 'itbench-aa', bars: 3 }]);
    assert.deepEqual(calls.at(-1), ['close']);
    assert.deepEqual(calls[0], ['launch', { headless: true }]);
  });

  test('run closes the browser when a capture fails', async () => {
    const calls = [];
    const page = scriptedPage([{ tab: false }], calls);
    await assert.rejects(
      charts.run({ argv: ['n', 's'], chromium: fakeChromium(page, calls), evaluations: [{ slug: 'x', url: 'u' }], log: () => {}, filesystem: {} }),
      /could not capture x/,
    );
    assert.deepEqual(calls.at(-1), ['close']);
  });
});

describe('main', () => {
  test('main returns the capture on success', async () => {
    const page = scriptedPage([GOOD], []);
    const capture = await charts.main({
      chromium: fakeChromium(page, []),
      evaluations: [{ slug: 'only', url: 'u' }],
      argv: ['n', 's', '/tmp/x.json'],
      filesystem: { mkdirSync() {}, writeFileSync() {} },
      log: () => {},
    });
    assert.equal(capture.evaluations[0].slug, 'only');
    assert.match(capture.capturedAt, /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$/);
  });

  test('main reports a failure and exits 1', async () => {
    const errors = [];
    let code = null;
    await charts.main({
      chromium: { launch: async () => { throw new Error('launch failed'); } },
      error: (failure) => errors.push(failure.message),
      exit: (value) => {
        code = value;
      },
    });
    assert.deepEqual(errors, ['launch failed']);
    assert.equal(code, 1);
  });

  test('the CLI resolves the real playwright module and exits 1 when the page has no chart', () => {
    const result = runScriptWithFakePlaywright({ script: SCRIPT, args: ['/tmp/never-written.json'] });
    assert.equal(result.status, 1);
    assert.match(result.stderr, /could not capture frontiercode/);
    assert.ok(result.calls.some((entry) => entry.call === 'browser.close'));
  });
});
