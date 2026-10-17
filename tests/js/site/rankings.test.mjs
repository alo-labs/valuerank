import test from 'node:test';
import assert from 'node:assert/strict';
import { initRankings } from '../../../valuerank/site/assets/js/rankings.js';
import { rankingsPage, slugsInOrder, rows, cell, header } from './pages.mjs';
import { data } from './fixture.mjs';

const mount = (opts) => {
  const page = rankingsPage(opts);
  initRankings(page.win);
  return page;
};
const lastUrl = (p) => p.win.history.calls.at(-1);
const type = (el, value) => { el.value = value; el.fire('input'); };
const check = (el, on = true) => { el.checked = on; el.fire('input'); el.fire('change'); };

test('renders one dense row per model in plan-rank order with the cost unit in the header', () => {
  const p = mount();
  assert.deepEqual(slugsInOrder(p), ['alpha', 'beta', 'gamma', 'delta', 'eps']);
  assert.equal(p.count.textContent, '5 of 5 models');
  const alpha = rows(p)[0];
  assert.equal(cell(alpha, 'rank').textContent, '1');
  assert.equal(cell(alpha, 'name').textContent, 'AlphaAcme');
  assert.equal(cell(alpha, 'name').querySelector('a').getAttribute('href'), '/models/alpha/');
  assert.equal(cell(alpha, 'overall').textContent, '71.6');
  assert.equal(cell(alpha, 'quality').textContent, '70.4');
  assert.equal(cell(alpha, 'cost').textContent, '$0.50');
  assert.equal(cell(alpha, 'grade').textContent, 'Owner-measured');
  assert.match(header(p, 'cost').textContent, /Plan cost \(USD per Index point\)/);
});

test('headers are sortable with aria-sort reflecting the active column', () => {
  const p = mount();
  assert.equal(header(p, 'rank').getAttribute('aria-sort'), 'ascending');
  assert.equal(header(p, 'overall').getAttribute('aria-sort'), 'none');
  const button = header(p, 'overall').querySelector('button');
  button.click();
  assert.equal(header(p, 'overall').getAttribute('aria-sort'), 'descending');
  assert.equal(header(p, 'rank').getAttribute('aria-sort'), 'none');
  assert.equal(lastUrl(p), '/rankings/?sort=overall&dir=desc');
  assert.deepEqual(slugsInOrder(p), ['alpha', 'beta', 'gamma', 'delta', 'eps']);
  header(p, 'overall').querySelector('button').click();
  assert.equal(header(p, 'overall').getAttribute('aria-sort'), 'ascending');
  assert.equal(lastUrl(p), '/rankings/?sort=overall');
  assert.deepEqual(slugsInOrder(p).slice(0, 3), ['gamma', 'beta', 'alpha']);
});

test('clicking a new sort column uses its default direction; cost sorts ascending first', () => {
  const p = mount();
  header(p, 'cost').querySelector('button').click();
  assert.equal(lastUrl(p), '/rankings/?sort=cost');
  assert.deepEqual(slugsInOrder(p).slice(0, 3), ['alpha', 'gamma', 'beta']);
});

test('the basis toggle switches rank order, cost header and unit, and the URL', () => {
  const p = mount();
  p.toggle.api.click();
  assert.deepEqual(slugsInOrder(p).slice(0, 3), ['beta', 'alpha', 'gamma']);
  assert.match(header(p, 'cost').textContent, /API cost \(USD per Index run\)/);
  assert.equal(cell(rows(p)[0], 'cost').textContent, '$2,500');
  assert.equal(lastUrl(p), '/rankings/?basis=api');
  assert.equal(p.toggle.api.getAttribute('aria-pressed'), 'true');
  p.toggle.plan.click();
  assert.equal(lastUrl(p), '/rankings/');
});

test('the cost-weight slider recomputes scores and ranks and writes w to the URL', () => {
  const p = mount();
  assert.equal(p.sliderOut.textContent, '20.0%');
  type(p.slider, '100');
  assert.equal(p.sliderOut.textContent, '100.0%');
  assert.deepEqual(slugsInOrder(p).slice(0, 3), ['gamma', 'alpha', 'beta']);
  assert.equal(cell(rows(p)[0], 'overall').textContent, '80.0');
  assert.equal(cell(rows(p)[0], 'rank').textContent, '1');
  assert.equal(lastUrl(p), '/rankings/?w=100');
  type(p.slider, 'garbage');
  assert.equal(p.slider.value, '20');
  assert.equal(lastUrl(p), '/rankings/');
});

test('unranked models are marked and show dashes for rank, overall and missing cost', () => {
  const p = mount();
  const delta = rows(p)[3];
  assert.equal(delta.classList.contains('is-unranked'), true);
  assert.equal(cell(delta, 'rank').textContent, '—');
  assert.equal(cell(delta, 'overall').textContent, '—');
  assert.equal(cell(delta, 'cost').textContent, '—');
  assert.match(cell(delta, 'name').textContent, /Not ranked/);
  assert.equal(rows(p)[0].classList.contains('is-unranked'), false);
});

test('fallback cost routes are flagged and plan routes expose their label', () => {
  const p = mount();
  assert.equal(cell(rows(p)[0], 'cost').getAttribute('title'), 'Plan X');
  const beta = rows(p)[1];
  assert.equal(cell(beta, 'cost').classList.contains('is-fallback'), true);
  assert.match(cell(beta, 'cost').getAttribute('title'), /fallback/i);
  p.toggle.api.click();
  assert.equal(cell(rows(p)[0], 'cost').getAttribute('title'), null);
});

test('free-text, provider, grade, coverage and route filters AND together and update count and URL', () => {
  const p = mount();
  type(p.q, 'bolt');
  assert.deepEqual(slugsInOrder(p), ['beta']);
  assert.equal(p.count.textContent, '1 of 5 models');
  assert.equal(lastUrl(p), '/rankings/?q=bolt');
  type(p.q, '');
  check(p.providers[0]);
  assert.deepEqual(slugsInOrder(p), ['alpha', 'gamma']);
  assert.equal(lastUrl(p), '/rankings/?provider=Acme');
  check(p.grades[0]);
  assert.deepEqual(slugsInOrder(p), ['alpha']);
  assert.equal(lastUrl(p), '/rankings/?provider=Acme&grade=measured');
  type(p.cov, '150');
  assert.equal(p.cov.value, '100');
  assert.equal(p.empty.hidden, true);
  p.routes.forEach((r) => { r.checked = false; });
  check(p.routes[2]);
  assert.deepEqual(slugsInOrder(p), []);
  assert.equal(rows(p).length, 0);
  assert.equal(p.empty.hidden, false);
  assert.equal(p.covOut.textContent, '100%');
  p.resetBox.click();
  assert.equal(p.empty.hidden, true);
  assert.equal(p.routes[0].checked, true);
  assert.equal(p.routes[2].checked, false);
});

test('typing a trailing space does not rewrite the search box', () => {
  const p = mount();
  type(p.q, 'bolt ');
  assert.equal(p.q.value, 'bolt ');
});

test('reset clears every filter but keeps basis, weight and sort; submit is prevented', () => {
  const p = mount({ search: '?basis=api&w=60&sort=overall&q=a&provider=Acme&grade=measured&route=eligible&cov=50' });
  assert.equal(p.q.value, 'a');
  assert.equal(p.providers[0].checked, true);
  assert.equal(p.routes[1].checked, true);
  p.reset.click();
  assert.equal(lastUrl(p), '/rankings/?basis=api&w=60&sort=overall');
  assert.equal(p.q.value, '');
  assert.equal(p.providers[0].checked, false);
  assert.equal(p.cov.value, '0');
  assert.equal(p.covOut.textContent, '0%');
  const e = p.form.fire('submit');
  assert.equal(e.defaultPrevented, true);
});

test('state in the URL wins on load: controls, headers and columns reflect it', () => {
  const p = mount({ search: '?basis=api&sort=b&dir=desc&cols=rank,b&w=45.5' });
  assert.equal(p.slider.value, '45.5');
  assert.equal(p.toggle.api.getAttribute('aria-pressed'), 'true');
  assert.equal(header(p, 'b').getAttribute('aria-sort'), 'descending');
  const cols = [...p.head.querySelectorAll('th')].map((t) => t.getAttribute('data-col'));
  assert.deepEqual(cols, ['compare', 'rank', 'name', 'b']);
  assert.equal(cell(rows(p)[0], 'b').textContent, '60.0');
  assert.equal(slugsInOrder(p)[0], 'alpha');
});

test('column picker lists every column, toggles columns, and keeps Model mandatory', () => {
  const p = mount();
  const boxes = [...p.columns.querySelectorAll('input')];
  const byKey = (k) => boxes.find((b) => b.getAttribute('data-col') === k);
  assert.ok(byKey('a') && byKey('b') && byKey('developer'));
  assert.equal(byKey('name').hasAttribute('disabled'), true);
  assert.equal(byKey('quality').checked, true);
  assert.equal(byKey('a').checked, false);
  byKey('quality').checked = false;
  byKey('quality').fire('change');
  assert.equal(header(p, 'quality'), null);
  assert.equal(lastUrl(p), '/rankings/?cols=rank,name,overall,cost,grade,coverage');
  [...p.columns.querySelectorAll('input')].find((b) => b.getAttribute('data-col') === 'a').checked = true;
  [...p.columns.querySelectorAll('input')].find((b) => b.getAttribute('data-col') === 'a').fire('change');
  assert.ok(header(p, 'a'));
  assert.match(cell(rows(p)[0], 'a').textContent, /80\.0/);
});

test('every optional column renders a value', () => {
  const keys = ['developer', 'qualityRank', 'speed', 'ii', 'a'].join(',');
  const p = mount({ search: `?cols=rank,${keys}` });
  const beta = rows(p)[1];
  assert.equal(cell(beta, 'developer').textContent, 'Bolt AI');
  assert.equal(cell(beta, 'qualityRank').textContent, '#1');
  assert.equal(cell(rows(p)[3], 'qualityRank').textContent, '—');
  assert.equal(cell(beta, 'speed').textContent, '80.0');
  assert.equal(cell(beta, 'ii').textContent, '50.0');
});

test('coverage is a bar plus an expander listing missing metrics, and stays open across re-renders', () => {
  const p = mount();
  const beta = rows(p)[1];
  const bar = beta.querySelector('.cov-fill');
  assert.equal(bar.style.width, '68%');
  const toggle = beta.querySelector('button[aria-controls]');
  const panel = p.win.document.getElementById(toggle.getAttribute('aria-controls'));
  assert.equal(toggle.getAttribute('aria-expanded'), 'false');
  assert.equal(panel.hidden, true);
  toggle.click();
  assert.equal(toggle.getAttribute('aria-expanded'), 'true');
  assert.equal(panel.hidden, false);
  assert.match(panel.textContent, /Missing: Beta bench/);
  type(p.q, 'bolt');
  const again = rows(p)[0].querySelector('button[aria-controls]');
  assert.equal(again.getAttribute('aria-expanded'), 'true');
  again.click();
  assert.equal(rows(p)[0].querySelector('button[aria-controls]').getAttribute('aria-expanded'), 'false');
  assert.equal(cell(rows(p)[0], 'coverage').textContent.includes('68.0%'), true);
});

test('full coverage shows Complete and unknown coverage a dash', () => {
  const p = mount();
  assert.match(cell(rows(p)[0], 'coverage').textContent, /100\.0%.*Complete/);
  assert.equal(rows(p)[0].querySelector('button[aria-controls]'), null);
  assert.equal(cell(rows(p)[3], 'coverage').textContent, '—');
});

const picker = (p, slug) => rows(p).find((r) => r.getAttribute('data-slug') === slug).querySelector('input[data-compare]');

test('compare drawer needs two models, then shows a side-by-side table and writes compare to the URL', () => {
  const p = mount();
  assert.equal(p.drawer.hidden, true);
  check(picker(p, 'alpha'));
  assert.equal(p.drawer.hidden, false);
  assert.match(p.compareBody.textContent, /at least one more/i);
  assert.equal(lastUrl(p), '/rankings/');
  check(picker(p, 'beta'));
  assert.equal(lastUrl(p), '/rankings/?compare=alpha,beta');
  const table = p.compareBody.querySelector('table');
  assert.deepEqual([...table.querySelectorAll('thead th')].map((t) => t.textContent).slice(1), ['Alpha', 'Beta', ]);
  const bodyRows = [...table.querySelectorAll('tbody tr')];
  const labels = bodyRows.map((r) => r.querySelector('th').textContent);
  assert.deepEqual(labels, ['Overall', 'Quality', 'Cost', 'Alpha bench', 'Beta bench']);
  const a = bodyRows[3];
  assert.deepEqual([...a.querySelectorAll('td')].map((t) => t.textContent), ['80.0', '90.0']);
  assert.equal(a.querySelectorAll('td')[1].classList.contains('is-best'), true);
  assert.equal(a.querySelectorAll('td')[0].classList.contains('is-best'), false);
  assert.deepEqual([...bodyRows[4].querySelectorAll('td')].map((t) => t.textContent), ['60.0', '—']);
});

test('compare is capped at four models; clear and per-model remove work; selection loads from the URL', () => {
  const p = mount({ search: '?compare=alpha,beta,gamma,delta' });
  assert.equal(picker(p, 'alpha').checked, true);
  assert.equal(p.compareBody.querySelectorAll('thead th').length, 5);
  check(picker(p, 'eps'));
  assert.equal(picker(p, 'eps').checked, false);
  assert.equal(lastUrl(p) ?? '', '');
  const remove = p.compareBody.querySelector('button[data-remove="beta"]');
  assert.match(remove.getAttribute('aria-label'), /Remove Beta/);
  remove.click();
  assert.equal(lastUrl(p), '/rankings/?compare=alpha,gamma,delta');
  check(picker(p, 'alpha'), false);
  check(picker(p, 'gamma'), false);
  assert.equal(p.drawer.hidden, false);
  assert.match(p.compareBody.textContent, /at least one more/i);
  p.clear.click();
  assert.equal(p.drawer.hidden, true);
  assert.equal(lastUrl(p), '/rankings/');
});

test('CSV export builds a blob URL on click with basis and version in the filename and revokes the previous one', () => {
  const p = mount();
  p.csv.click();
  const first = p.win.URL.created[0];
  assert.equal(p.csv.getAttribute('href'), first.url);
  assert.equal(p.csv.getAttribute('download'), 'valuerank-v9.9.9-plan.csv');
  assert.equal(first.blob.type, 'text/csv;charset=utf-8');
  const text = first.blob.text();
  assert.equal(text.split('\r\n')[0], 'Rank,Model,Overall,Quality,Plan cost (USD per Index point),Evidence,Coverage');
  assert.equal(text.split('\r\n')[1], '1,Alpha,71.6,70.4,0.5,measured,100');
  p.toggle.api.click();
  p.csv.click();
  assert.equal(p.csv.getAttribute('download'), 'valuerank-v9.9.9-api.csv');
  assert.deepEqual(p.win.URL.revoked, [first.url]);
});

test('JSON export respects the current filters and columns', () => {
  const p = mount({ search: '?q=bolt&cols=rank,b' });
  p.json.click();
  const created = p.win.URL.created[0];
  assert.equal(p.json.getAttribute('download'), 'valuerank-v9.9.9-plan.json');
  assert.equal(created.blob.type, 'application/json');
  assert.deepEqual(JSON.parse(created.blob.text()), [{ rank: 2, name: 'Beta', b: null }]);
});

test('a model row is a row header with a label on every cell for the phone card layout', () => {
  const p = mount();
  const alpha = rows(p)[0];
  assert.equal(cell(alpha, 'name').tagName, 'TH');
  assert.equal(cell(alpha, 'name').getAttribute('scope'), 'row');
  assert.equal(cell(alpha, 'name').querySelector('a').className, 'model-name');
  assert.equal(cell(alpha, 'cost').getAttribute('data-label'), 'Cost');
  assert.equal(cell(alpha, 'quality').getAttribute('data-label'), 'Quality');
});

test('the loading row is replaced by the table; basis labels and units follow the basis', () => {
  const p = mount();
  assert.equal(p.body.querySelector('[data-state="loading"]'), null);
  assert.equal(p.error.hidden, true);
  assert.equal(p.basisLabel.textContent, 'Plan ranking');
  assert.equal(p.costUnit.textContent, 'USD per Index point');
  p.toggle.api.click();
  assert.equal(p.basisLabel.textContent, 'API ranking');
  assert.equal(p.costUnit.textContent, 'USD per Index run');
  assert.equal(p.win.document.documentElement.getAttribute('data-basis'), 'api');
});

test('unreadable embedded data shows the error box and hides the loading row', () => {
  const page = rankingsPage();
  page.win.document.getElementById('rankings-data').replaceChildren('not json');
  initRankings(page.win);
  assert.equal(page.error.hidden, false);
  assert.equal(page.loading.hidden, true);
  assert.equal(page.body.children.length, 1);
});

test('the share button copies the current address and reports failure without clipboard access', async () => {
  const p = mount();
  const copied = [];
  p.win.location.href = 'https://example.test/rankings/?basis=api';
  p.win.navigator = { clipboard: { writeText: async (text) => { copied.push(text); } } };
  p.share.click();
  await new Promise((resolve) => setTimeout(resolve));
  assert.deepEqual(copied, ['https://example.test/rankings/?basis=api']);
  assert.equal(p.share.textContent, 'Link copied');
  p.win.navigator = { clipboard: { writeText: async () => { throw new Error('denied'); } } };
  p.share.click();
  await new Promise((resolve) => setTimeout(resolve));
  assert.match(p.share.textContent, /address bar/);
});

test('a statechange event carries the recomputed models for chart modules', () => {
  const page = rankingsPage();
  const seen = [];
  page.win.document.addEventListener('vr:statechange', (e) => seen.push(e.detail));
  initRankings(page.win);
  assert.equal(seen.length, 1);
  type(page.slider, '100');
  assert.equal(seen.length, 2);
  assert.equal(seen[1].state.w, 100);
  assert.equal(seen[1].models.find((m) => m.slug === 'gamma').rank.plan, 1);
  assert.equal(seen[1].data.version, data.version);
});

import { initIndex } from '../../../valuerank/site/assets/js/rankings.js';
import { indexPage } from './pages.mjs';

const mountIndex = (opts) => {
  const page = indexPage(opts);
  initIndex(page.win);
  return page;
};

test('answer page renders the compact table of ranked models only, in rank order, with the basis headline', () => {
  const p = mountIndex();
  assert.deepEqual(slugsInOrder(p), ['alpha', 'beta', 'gamma']);
  assert.equal(cell(rows(p)[0], 'name').querySelector('a').getAttribute('href'), '/models/alpha/');
  assert.equal(cell(rows(p)[0], 'overall').textContent, '71.6');
  assert.equal(p.sliderOut.textContent, '20.0%');
  assert.equal(cell(rows(p)[0], 'quality').textContent, '70.4');
  assert.equal(cell(rows(p)[1], 'coverage').getAttribute('data-label'), 'Coverage');
});

test('answer page lists at most 16 models', () => {
  const many = Array.from({ length: 20 }, (_, i) => ({
    ...data.models[0], slug: `m${i}`, name: `M${i}`, rank: { api: i + 1, plan: i + 1 }, overall: { api: 50, plan: 50 },
  }));
  const page = indexPage();
  page.win.document.getElementById('rankings-data').replaceChildren(JSON.stringify({ ...data, models: many, picks: { plan: { value: null, other: null, budget: null }, api: {} } }));
  initIndex(page.win);
  assert.equal(slugsInOrder(page).length, 16);
});

test('committed picks are shown at the default weight and update with the basis', () => {
  const p = mountIndex();
  assert.equal(p.picks.value.name.textContent, 'Alpha');
  assert.equal(p.picks.value.name.getAttribute('href'), '/models/alpha/');
  assert.equal(p.picks.value.reason.textContent, 'committed value');
  assert.equal(p.picks.value.label.textContent, 'Best overall value');
  assert.equal(p.picks.value.score.textContent, '71.6overall');
  assert.equal(p.picks.other.label.textContent, 'Best at API rates');
  assert.equal(p.picks.other.name.textContent, 'Beta');
  assert.equal(p.picks.other.score.textContent, '75.3overall at API rates');
  p.toggle.api.click();
  assert.equal(p.picks.value.name.textContent, 'Beta');
  assert.equal(p.picks.value.reason.textContent, 'committed api value');
  assert.equal(p.picks.other.label.textContent, 'Best on a subscription');
  assert.equal(p.win.document.documentElement.getAttribute('data-basis'), 'api');
  assert.equal(p.basisLabel.textContent, 'API ranking');
  assert.equal(p.win.history.calls.at(-1), '/?basis=api');
});

test('moving the cost weight re-renders the table and recomputes the picks from the data', () => {
  const p = mountIndex();
  p.slider.value = '100';
  p.slider.fire('input');
  assert.deepEqual(slugsInOrder(p), ['gamma', 'alpha', 'beta']);
  assert.equal(p.picks.value.name.textContent, 'Gamma');
  assert.match(p.picks.value.reason.textContent, /Gamma has the highest overall score/);
  // Gamma also leads the other basis at this weight, so the second card shows the quality leader instead.
  assert.equal(p.picks.other.label.textContent, 'Best quality, any cost');
  assert.equal(p.picks.other.name.textContent, 'Beta');
  assert.equal(p.picks.other.score.textContent, '90.0quality');
  assert.equal(p.sliderOut.textContent, '100.0%');
  assert.equal(p.win.history.calls.at(-1), '/?w=100');
});

test('picks that are null are hidden', () => {
  const none = { value: null, other: null, budget: null };
  const page = indexPage();
  const lone = { ...data, models: [data.models[3]], picks: { plan: none, api: none } };
  page.win.document.getElementById('rankings-data').replaceChildren(JSON.stringify(lone));
  initIndex(page.win);
  assert.equal(page.picks.value.box.hidden, true);
  page.slider.value = '50';
  page.slider.fire('input');
  assert.equal(page.picks.budget.box.hidden, true);
  assert.deepEqual(slugsInOrder(page), []);
});

test('answer page reads its state from the URL and honours a custom model base', () => {
  const page = indexPage({ search: '?basis=api&w=40' });
  page.body.setAttribute('data-model-base', '/m/');
  initIndex(page.win);
  assert.equal(page.slider.value, '40');
  assert.equal(page.toggle.api.getAttribute('aria-pressed'), 'true');
  assert.equal(cell(rows(page)[0], 'name').querySelector('a').getAttribute('href'), '/m/gamma/');
});

test('clicking the active ascending column flips it to descending', () => {
  const p = mount();
  header(p, 'rank').querySelector('button').click();
  assert.equal(header(p, 'rank').getAttribute('aria-sort'), 'descending');
  assert.equal(lastUrl(p), '/rankings/?dir=desc');
  assert.equal(slugsInOrder(p)[0], 'gamma');
});

test('without a data-model-base attribute rows link under /models/', () => {
  const page = rankingsPage();
  page.win.document.getElementById('rankings-table').removeAttribute('data-model-base');
  initRankings(page.win);
  assert.equal(cell(rows(page)[0], 'name').querySelector('a').getAttribute('href'), '/models/alpha/');
});

test('a chart tab chosen in the URL survives later filter and weight changes', () => {
  const p = mount({ search: '?chart=heatmap' });
  type(p.slider, '50');
  assert.equal(lastUrl(p), '/rankings/?w=50&chart=heatmap');
  p.win.location.search = '?w=50&chart=bubble';
  type(p.q, 'a');
  assert.equal(lastUrl(p), '/rankings/?w=50&q=a&chart=bubble');
});

test('frontier tier badges carry text and a tooltip with the configuration and gap', () => {
  const [alpha, beta, gamma, delta] = data.models;
  Object.assign(alpha, { aaFrontierTier: 'frontier', aaFrontierConfiguration: 'Alpha (max)', aaFrontierIntelligenceGap: 0 });
  Object.assign(beta, { aaFrontierTier: 'near', aaFrontierConfiguration: 'Beta (high)', aaFrontierIntelligenceGap: 2 });
  Object.assign(gamma, { aaFrontierTier: 'near', aaFrontierConfiguration: null, aaFrontierIntelligenceGap: null });
  Object.assign(delta, { aaFrontierTier: 'frontier' });
  try {
    const p = mount();
    const tag = (slug) => cell(rows(p).find((r) => r.dataset.slug === slug), 'name').querySelector('[data-aa-tier]');
    assert.equal(tag('alpha').textContent, 'AA frontier');
    assert.equal(tag('alpha').getAttribute('title'), 'Alpha (max) is on the rendered AA frontier.');
    assert.equal(tag('alpha').className, 'badge badge-tier badge-tier-frontier');
    assert.equal(tag('beta').textContent, 'Near frontier');
    assert.equal(tag('beta').getAttribute('title'), 'Beta (high) is within 2 Index points of the rendered AA frontier at its cost.');
    assert.equal(tag('gamma').getAttribute('title'), 'A plotted configuration is within the policy gap of the rendered AA frontier at its cost.');
    assert.equal(tag('delta').getAttribute('title'), 'Selected configuration is on the rendered AA frontier.');
    Object.assign(delta, { aaFrontierTier: 'near', aaFrontierConfiguration: 'Delta (low)', aaFrontierIntelligenceGap: 1 });
    const singular = mount();
    const deltaTag = cell(rows(singular).find((r) => r.dataset.slug === 'delta'), 'name').querySelector('[data-aa-tier]');
    assert.equal(deltaTag.getAttribute('title'), 'Delta (low) is within 1 Index point of the rendered AA frontier at its cost.');
    assert.equal(tag('eps'), null);
  } finally {
    for (const m of [alpha, beta, gamma, delta]) {
      delete m.aaFrontierTier; delete m.aaFrontierConfiguration; delete m.aaFrontierIntelligenceGap;
    }
  }
});
