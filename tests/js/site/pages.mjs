// Builds the DOM structure the templates must provide (see the report's DOM contract).
import { add, createWindow } from '../helpers/fake-dom.mjs';
import { data } from './fixture.mjs';

export function basisToggle(body, id = 'basis-toggle') {
  const box = add(body, 'div', { id });
  return { box, api: add(box, 'button', { 'data-basis': 'api' }), plan: add(box, 'button', { 'data-basis': 'plan' }) };
}

export function shared(win, payload = data) {
  const { body } = win.document;
  add(body, 'script', { id: 'rankings-data', type: 'application/json' }, JSON.stringify(payload));
  const toggle = basisToggle(body);
  const slider = add(body, 'input', { id: 'cost-weight', type: 'range' });
  const sliderOut = add(body, 'output', { id: 'cost-weight-value' });
  const basisLabel = add(body, 'span', { 'data-basis-label': '' });
  const costUnit = add(body, 'span', { 'data-cost-unit': '' });
  return { toggle, slider, sliderOut, basisLabel, costUnit };
}

export function rankingsPage(opts = {}) {
  const win = createWindow({ pathname: '/rankings/', ...opts });
  const { body } = win.document;
  const parts = shared(win);
  const form = add(body, 'form', { id: 'filters' });
  parts.q = add(form, 'input', { name: 'q', type: 'search' });
  parts.cov = add(form, 'input', { name: 'cov', type: 'number' });
  parts.routes = ['all', 'eligible', 'fallback'].map((v) => add(form, 'input', { name: 'route', type: 'radio', value: v }));
  parts.routes[0].checked = true;
  parts.covOut = add(form, 'output', { id: 'filter-cov-value' });
  parts.providers = ['Acme', 'Bolt AI', 'Delta Labs'].map((v) => add(form, 'input', { name: 'provider', type: 'checkbox', value: v }));
  parts.grades = ['measured', 'estimate', 'claim'].map((v) => add(form, 'input', { name: 'grade', type: 'checkbox', value: v }));
  parts.reset = add(form, 'button', { 'data-action': 'reset-filters', type: 'button' });
  parts.resetBox = add(body, 'button', { 'data-action': 'reset-filters', type: 'button' });
  parts.form = form;
  parts.columns = add(body, 'div', { id: 'column-picker-list' });
  const table = add(body, 'table', { id: 'rankings-table', 'data-model-base': '/models/' });
  parts.head = add(table, 'thead', { id: 'rankings-head' });
  parts.body = add(table, 'tbody', { id: 'rankings-body' });
  parts.count = add(body, 'p', { id: 'rankings-count' });
  parts.loading = add(parts.body, 'tr', { 'data-state': 'loading' });
  parts.empty = add(body, 'p', { id: 'rankings-empty', hidden: '' });
  parts.error = add(body, 'p', { id: 'rankings-error', hidden: '' });
  parts.share = add(body, 'button', { 'data-share': '' });
  parts.drawer = add(body, 'section', { id: 'compare-drawer', hidden: '' });
  parts.compareBody = add(parts.drawer, 'div', { id: 'compare-body' });
  parts.clear = add(parts.drawer, 'button', { id: 'compare-clear' });
  parts.notes = add(body, 'ol', { id: 'rankings-evidence' });
  parts.csv = add(body, 'a', { id: 'export-csv', href: '#' });
  parts.json = add(body, 'a', { id: 'export-json', href: '#' });
  return { win, ...parts };
}

export function indexPage(opts = {}) {
  const win = createWindow({ pathname: '/', ...opts });
  const { body } = win.document;
  const parts = shared(win);
  parts.body = add(add(body, 'table'), 'tbody', { id: 'index-body' });
  parts.notes = add(body, 'ol', { id: 'index-evidence' });
  parts.picks = {};
  for (const kind of ['value', 'other', 'budget']) {
    const box = add(body, 'article', { 'data-pick': kind });
    parts.picks[kind] = { box, label: add(box, 'h3', { 'data-pick-label': '' }), name: add(box, 'a', { 'data-pick-name': '', href: '#' }), score: add(box, 'p', { 'data-pick-score': '' }), reason: add(box, 'p', { 'data-pick-reason': '' }) };
  }
  return { win, ...parts };
}

export const rows = (parts) => [...parts.body.children];
export const slugsInOrder = (parts) => rows(parts).map((r) => r.getAttribute('data-slug')).filter(Boolean);
export const cell = (row, col) => row.querySelector(`[data-col="${col}"]`);
export const header = (parts, col) => parts.head.querySelector(`th[data-col="${col}"]`);
