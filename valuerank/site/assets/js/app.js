// Shared page behaviour: theme, mobile nav, basis toggle, URL state sync, FAQ expanders.
// Every function takes the window (or a container) so nothing touches globals at import time.
import { parseState, serializeState } from './urlstate.js';
import { DEFAULT_COLUMNS } from './filters.js';

const THEME_KEY = 'vr-theme';
const THEMES = ['light', 'dark'];

export function initTheme(win, onChange) {
  const html = win.document.documentElement;
  const button = win.document.querySelector('[data-theme-toggle]');
  const read = () => {
    try { return win.localStorage.getItem(THEME_KEY); } catch { return null; }
  };
  const write = (theme) => {
    try { win.localStorage.setItem(THEME_KEY, theme); } catch { /* storage blocked: theme still applies */ }
  };
  const stored = read();
  const system = win.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  let current = THEMES.includes(stored) ? stored : system;

  const apply = () => {
    html.setAttribute('data-theme', current);
    if (button) {
      button.setAttribute('aria-pressed', String(current === 'dark'));
      button.setAttribute('aria-label', current === 'dark' ? 'Switch to light theme' : 'Switch to dark theme');
    }
    if (onChange) onChange(current === 'dark');
  };
  const toggle = () => {
    current = current === 'dark' ? 'light' : 'dark';
    write(current);
    apply();
  };
  apply();
  if (button) button.addEventListener('click', toggle);
  return { current: () => current, toggle };
}

export function initNav(win) {
  const doc = win.document;
  const button = doc.querySelector('[data-nav-toggle]');
  if (!button) return;
  const menu = doc.getElementById(button.getAttribute('aria-controls'));
  const isOpen = () => button.getAttribute('aria-expanded') === 'true';
  const setOpen = (open) => {
    button.setAttribute('aria-expanded', String(open));
    menu.classList.toggle('is-open', open);
  };
  button.addEventListener('click', () => {
    setOpen(!isOpen());
    const first = menu.querySelector('a');
    if (isOpen() && first) first.focus();
  });
  doc.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape' || !isOpen()) return;
    setOpen(false);
    button.focus();
  });
}

export function initBasisToggle(container, active, onChange) {
  const buttons = container.querySelectorAll('[data-basis]');
  const root = container.ownerDocument.documentElement;
  const set = (basis) => {
    buttons.forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.basis === basis)));
    root.setAttribute('data-basis', basis);
  };
  buttons.forEach((b) => b.addEventListener('click', () => {
    set(b.dataset.basis);
    onChange(b.dataset.basis);
  }));
  set(active);
  return { set };
}

/** Text that names the active basis: [data-basis-label] and [data-cost-unit] come from rankings.bases. */
export function syncBasisText(doc, bases, basis) {
  doc.querySelectorAll('[data-basis-label]').forEach((el) => { el.textContent = bases[basis].label; });
  doc.querySelectorAll('[data-cost-unit]').forEach((el) => { el.textContent = bases[basis].costUnit; });
}

/** Default view state for a rankings.json payload (what the URL omits). */
export function defaultState(data) {
  return {
    basis: data.defaultBasis, w: data.costWeightPct, sort: 'rank', dir: 'asc', cols: [...DEFAULT_COLUMNS],
    provider: [], grade: [], route: 'all', cov: 0, q: '', compare: [], chart: '',
  };
}

export function createUrlSync(win, defaults) {
  return {
    read: () => parseState(win.location.search, defaults),
    write: (state) => win.history.replaceState(null, '', win.location.pathname + serializeState(state, defaults)),
  };
}

export function initFaq(root) {
  root.querySelectorAll('[data-faq-toggle]').forEach((button) => {
    button.addEventListener('click', () => {
      const open = button.getAttribute('aria-expanded') !== 'true';
      button.setAttribute('aria-expanded', String(open));
      root.querySelector(`#${button.getAttribute('aria-controls')}`).hidden = !open;
    });
  });
}

export function initApp(win, onTheme) {
  const theme = initTheme(win, onTheme);
  initNav(win);
  initFaq(win.document);
  return theme;
}
