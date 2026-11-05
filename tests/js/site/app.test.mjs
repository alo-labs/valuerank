import test from 'node:test';
import assert from 'node:assert/strict';
import {
  initTheme, initNav, initBasisToggle, createUrlSync, initFaq, initApp,
} from '../../../valuerank/site/assets/js/app.js';
import { createWindow, add } from '../helpers/fake-dom.mjs';

const KEY = 'vr-theme';

function themeWin(opts) {
  const win = createWindow(opts);
  const btn = add(win.document.body, 'button', { 'data-theme-toggle': '' });
  return { win, btn, html: win.document.documentElement };
}

test('theme defaults to the system preference when nothing is stored', () => {
  const dark = themeWin({ dark: true });
  initTheme(dark.win);
  assert.equal(dark.html.getAttribute('data-theme'), 'dark');
  const light = themeWin({ dark: false });
  initTheme(light.win);
  assert.equal(light.html.getAttribute('data-theme'), 'light');
});

test('a stored theme wins over the system preference; garbage is ignored', () => {
  const a = themeWin({ dark: true, stored: { [KEY]: 'light' } });
  initTheme(a.win);
  assert.equal(a.html.getAttribute('data-theme'), 'light');
  const b = themeWin({ dark: true, stored: { [KEY]: 'neon' } });
  initTheme(b.win);
  assert.equal(b.html.getAttribute('data-theme'), 'dark');
});

test('toggling flips the theme, updates the button and writes exactly one localStorage key', () => {
  const { win, btn, html } = themeWin({ dark: false });
  const theme = initTheme(win);
  assert.equal(btn.getAttribute('aria-pressed'), 'false');
  btn.click();
  assert.equal(html.getAttribute('data-theme'), 'dark');
  assert.equal(btn.getAttribute('aria-pressed'), 'true');
  assert.match(btn.getAttribute('aria-label'), /light/i);
  assert.equal(theme.current(), 'dark');
  btn.click();
  assert.equal(html.getAttribute('data-theme'), 'light');
  assert.deepEqual([...new Set(win.localStorage.writes)], [KEY]);
  assert.equal(win.localStorage.getItem(KEY), 'light');
});

test('theme still works when storage is blocked and when there is no toggle button', () => {
  const { win, btn, html } = themeWin({ storageThrows: true, dark: true });
  initTheme(win);
  assert.equal(html.getAttribute('data-theme'), 'dark');
  btn.click();
  assert.equal(html.getAttribute('data-theme'), 'light');
  const bare = createWindow();
  const t = initTheme(bare);
  t.toggle();
  assert.equal(bare.document.documentElement.getAttribute('data-theme'), 'dark');
});

function navWin() {
  const win = createWindow();
  const btn = add(win.document.body, 'button', { 'data-nav-toggle': '', 'aria-controls': 'site-nav', 'aria-expanded': 'false' });
  const menu = add(win.document.body, 'nav', { id: 'site-nav' });
  const link = add(menu, 'a', { href: '/rankings/' });
  return { win, btn, menu, link };
}

test('menu button toggles aria-expanded, the open class, and moves focus to the first link', () => {
  const { win, btn, menu, link } = navWin();
  initNav(win);
  btn.click();
  assert.equal(btn.getAttribute('aria-expanded'), 'true');
  assert.equal(menu.classList.contains('is-open'), true);
  assert.equal(win.document.activeElement, link);
  btn.click();
  assert.equal(btn.getAttribute('aria-expanded'), 'false');
  assert.equal(menu.classList.contains('is-open'), false);
});

test('Escape closes an open menu and returns focus to the button; other keys and closed menus do nothing', () => {
  const { win, btn, menu } = navWin();
  initNav(win);
  win.document.fire('keydown', { key: 'Escape' });
  assert.equal(win.document.activeElement, null);
  btn.click();
  win.document.fire('keydown', { key: 'Tab' });
  assert.equal(btn.getAttribute('aria-expanded'), 'true');
  win.document.fire('keydown', { key: 'Escape' });
  assert.equal(btn.getAttribute('aria-expanded'), 'false');
  assert.equal(menu.classList.contains('is-open'), false);
  assert.equal(win.document.activeElement, btn);
});

test('menu without links still opens; initNav without a button is a no-op', () => {
  const win = createWindow();
  const btn = add(win.document.body, 'button', { 'data-nav-toggle': '', 'aria-controls': 'm' });
  add(win.document.body, 'nav', { id: 'm' });
  initNav(win);
  btn.click();
  assert.equal(btn.getAttribute('aria-expanded'), 'true');
  assert.doesNotThrow(() => initNav(createWindow()));
});

test('basis toggle marks the active button, reports clicks, and can be set programmatically', () => {
  const win = createWindow();
  const box = add(win.document.body, 'div');
  const api = add(box, 'button', { 'data-basis': 'api' });
  const plan = add(box, 'button', { 'data-basis': 'plan' });
  const seen = [];
  const toggle = initBasisToggle(box, 'plan', (b) => seen.push(b));
  assert.equal(plan.getAttribute('aria-pressed'), 'true');
  assert.equal(api.getAttribute('aria-pressed'), 'false');
  api.click();
  assert.deepEqual(seen, ['api']);
  assert.equal(api.getAttribute('aria-pressed'), 'true');
  assert.equal(plan.getAttribute('aria-pressed'), 'false');
  toggle.set('plan');
  assert.equal(plan.getAttribute('aria-pressed'), 'true');
  assert.deepEqual(seen, ['api']);
});

test('URL sync reads the query on load and replaceStates the serialized query on write', () => {
  const defaults = { basis: 'plan', w: 20, sort: 'rank', dir: 'asc', cols: ['rank'], provider: [], grade: [], route: 'all', cov: 0, q: '', compare: [], chart: '' };
  const win = createWindow({ search: '?basis=api&w=40', pathname: '/rankings/' });
  const sync = createUrlSync(win, defaults);
  const s = sync.read();
  assert.equal(s.basis, 'api');
  assert.equal(s.w, 40);
  sync.write({ ...s, basis: 'plan', w: 20 });
  assert.deepEqual(win.history.calls, ['/rankings/']);
  sync.write({ ...s, q: 'x y' });
  assert.deepEqual(win.history.calls.at(-1), '/rankings/?basis=api&w=40&q=x%20y');
});

test('FAQ expanders toggle aria-expanded and the hidden state of their panel', () => {
  const win = createWindow();
  const root = add(win.document.body, 'section');
  const b1 = add(root, 'button', { 'data-faq-toggle': '', 'aria-controls': 'p1', 'aria-expanded': 'false' });
  const p1 = add(root, 'div', { id: 'p1', hidden: '' });
  initFaq(root);
  b1.click();
  assert.equal(b1.getAttribute('aria-expanded'), 'true');
  assert.equal(p1.hidden, false);
  b1.click();
  assert.equal(b1.getAttribute('aria-expanded'), 'false');
  assert.equal(p1.hidden, true);
});

test('initApp wires theme, nav and FAQ together', () => {
  const win = createWindow({ dark: true });
  const nav = add(win.document.body, 'button', { 'data-nav-toggle': '', 'aria-controls': 'n' });
  add(win.document.body, 'nav', { id: 'n' });
  const faq = add(win.document.body, 'button', { 'data-faq-toggle': '', 'aria-controls': 'f', 'aria-expanded': 'false' });
  add(win.document.body, 'div', { id: 'f', hidden: '' });
  initApp(win);
  assert.equal(win.document.documentElement.getAttribute('data-theme'), 'dark');
  nav.click(); faq.click();
  assert.equal(nav.getAttribute('aria-expanded'), 'true');
  assert.equal(faq.getAttribute('aria-expanded'), 'true');
});

test('defaultState derives the URL defaults from the rankings payload', async () => {
  const { defaultState } = await import('../../../valuerank/site/assets/js/app.js');
  const d = defaultState({ defaultBasis: 'plan', costWeightPct: 18.9394 });
  assert.equal(d.basis, 'plan');
  assert.equal(d.w, 18.9394);
  assert.deepEqual(d.cols, ['rank', 'name', 'overall', 'quality', 'cost', 'grade', 'coverage']);
  assert.deepEqual([d.provider, d.grade, d.compare], [[], [], []]);
});

test('the theme callback hears the initial theme and every toggle as a dark flag', () => {
  const { win, btn } = themeWin({ dark: false });
  const seen = [];
  initTheme(win, (dark) => seen.push(dark));
  btn.click();
  btn.click();
  assert.deepEqual(seen, [false, true, false]);
  const withApp = themeWin({ dark: true });
  const heard = [];
  const theme = initApp(withApp.win, (dark) => heard.push(dark));
  assert.deepEqual(heard, [true]);
  assert.equal(theme.current(), 'dark');
});

test('the basis toggle mirrors the active basis on <html> so CSS can show the matching copy', () => {
  const win = createWindow();
  const box = add(win.document.body, 'div');
  const api = add(box, 'button', { 'data-basis': 'api' });
  add(box, 'button', { 'data-basis': 'plan' });
  const toggle = initBasisToggle(box, 'plan', () => {});
  assert.equal(win.document.documentElement.getAttribute('data-basis'), 'plan');
  api.click();
  assert.equal(win.document.documentElement.getAttribute('data-basis'), 'api');
  toggle.set('plan');
  assert.equal(win.document.documentElement.getAttribute('data-basis'), 'plan');
});

test('syncBasisText names the active basis and cost unit wherever the page asks for them', async () => {
  const { syncBasisText } = await import('../../../valuerank/site/assets/js/app.js');
  const win = createWindow();
  const label = add(win.document.body, 'span', { 'data-basis-label': '' });
  const unit = add(win.document.body, 'span', { 'data-cost-unit': '' });
  const bases = { api: { label: 'API ranking', costUnit: 'USD per basket run' }, plan: { label: 'Plan ranking', costUnit: 'USD per basket run' } };
  syncBasisText(win.document, bases, 'api');
  assert.equal(label.textContent, 'API ranking');
  assert.equal(unit.textContent, 'USD per basket run');
  syncBasisText(win.document, bases, 'plan');
  assert.equal(label.textContent, 'Plan ranking');
});
