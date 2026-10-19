// The rankings instrument (/rankings/) and the answer page table (/). DOM access goes through
// the injected window; nothing runs at import time.
import { h } from './dom.js';
import { createUrlSync, defaultState, initBasisToggle, syncBasisText } from './app.js';
import { parseState, serializeState } from './urlstate.js';
import { recompute, costValue, picks } from './scoring.js';
import { applyFilters, sortModels, columnCatalog, columnValue } from './filters.js';
import { toCsv, toJson, exportFilename } from './export.js';
import { compareRows, bestIndexes } from './compare.js';
import { fmtUsd, fmtPct, fmtScore, gradeLabel } from './format.js';

const MAX_COMPARE = 4;
const LEFT_ALIGNED = ['name', 'developer', 'grade', 'coverage'];
const DEFAULT_MODEL_BASE = '/models/';

const dash = '—';
const orDash = (v, fmt = String) => (v === null || v === undefined ? dash : fmt(v));

function costHeader(data, basis) {
  const b = data.bases[basis];
  return `${b.costLabel} (${b.costUnit})`;
}

function costTitle(model, basis) {
  if (basis !== 'plan') return null;
  if (model.cost.route) return model.cost.route.planLabel;
  return model.cost.fallback ? 'API-cost fallback: no admitted Plan route' : null;
}

function coverageCell(doc, model, expanded) {
  const cov = model.coverage;
  if (!cov) return [dash];
  const summary = [
    h(doc, 'span', { class: 'cov-bar', role: 'img', 'aria-label': `Coverage ${fmtPct(cov.pct)}` },
      h(doc, 'span', { class: 'cov-fill', style: { width: `${cov.pct}%` } })),
    h(doc, 'span', { class: 'cov-pct', text: fmtPct(cov.pct) }),
  ];
  if (!cov.missing.length) return [h(doc, 'span', { class: 'cov' }, ...summary, h(doc, 'span', { class: 'cov-complete', text: 'Complete' }))];
  const id = `cov-${model.slug}`;
  const panel = h(doc, 'div', { id, class: 'cov-missing', hidden: !expanded.has(model.slug) }, `Missing: ${cov.missing.join(', ')}`);
  const button = h(doc, 'button', {
    type: 'button', class: 'cov-toggle', 'aria-controls': id, 'aria-expanded': String(expanded.has(model.slug)),
  }, `${cov.missing.length} missing`);
  button.addEventListener('click', () => {
    const open = !expanded.has(model.slug);
    if (open) expanded.add(model.slug); else expanded.delete(model.slug);
    button.setAttribute('aria-expanded', String(open));
    panel.hidden = !open;
  });
  return [h(doc, 'span', { class: 'cov' }, ...summary, button), panel];
}

const TIER_LABELS = { frontier: 'AA frontier', near: 'Near frontier' };

function tierBadge(doc, model) {
  const tier = model.aaFrontierTier;
  if (!TIER_LABELS[tier]) return null;
  const config = model.aaFrontierConfiguration;
  const title = tier === 'frontier'
    ? `${config ? `${config} is` : 'Selected configuration is'} on the rendered AA frontier.`
    : `${config ? `${config} is` : 'A plotted configuration is'} within ${Number.isFinite(model.aaFrontierIntelligenceGap) ? `${model.aaFrontierIntelligenceGap} Index point${model.aaFrontierIntelligenceGap === 1 ? '' : 's'}` : 'the policy gap'} of the rendered AA frontier at its cost.`;
  return h(doc, 'span', { class: `badge badge-tier badge-tier-${tier}`, 'data-aa-tier': tier, title, text: TIER_LABELS[tier] });
}

function cellChildren(doc, key, model, ctx) {
  switch (key) {
    case 'rank': return [orDash(model.rank[ctx.basis])];
    case 'name': return [
      h(doc, 'span', { class: 'model-id' },
        h(doc, 'a', { href: `${ctx.modelBase}${model.slug}/`, class: 'model-name', text: model.name }),
        h(doc, 'span', { class: 'model-dev', text: model.developer }),
        tierBadge(doc, model),
        model.rankingEligible ? null : h(doc, 'span', { class: 'tag', text: 'Not ranked' })),
    ];
    case 'developer': return [model.developer];
    case 'overall': return [orDash(model.overall[ctx.basis], fmtScore)];
    case 'cost': return [fmtUsd(costValue(model, ctx.basis), 2)];
    case 'grade': return [h(doc, 'span', { class: `badge badge-${model.grade}`, text: gradeLabel(model.grade) })];
    case 'coverage': return coverageCell(doc, model, ctx.expanded);
    case 'qualityRank': return [orDash(model.qualityRank, (v) => `#${v}`)];
    default: return [fmtScore(columnValue(model, key, ctx.basis))];
  }
}

function buildCell(doc, column, model, ctx) {
  const key = column.key;
  const title = key === 'cost' ? costTitle(model, ctx.basis) : null;
  const fallback = key === 'cost' && Boolean(model.cost.fallback);
  const cls = [LEFT_ALIGNED.includes(key) ? '' : 'num', key === 'name' ? 'cell-model' : '', fallback ? 'is-fallback' : ''].join(' ').trim();
  const attrs = { 'data-col': key, 'data-label': column.label, class: cls || null, title };
  if (key === 'name') return h(doc, 'th', { ...attrs, scope: 'row' }, ...cellChildren(doc, key, model, ctx));
  return h(doc, 'td', attrs, ...cellChildren(doc, key, model, ctx));
}

function fillBody(doc, tbody, models, columns, ctx, comparable) {
  const rowNodes = models.map((m) => {
    const cells = columns.map((c) => buildCell(doc, c, m, ctx));
    if (comparable) {
      const box = h(doc, 'input', {
        type: 'checkbox', 'data-compare': m.slug, 'aria-label': `Compare ${m.name}`, checked: ctx.compare.includes(m.slug),
      });
      box.addEventListener('change', () => ctx.onCompare(m.slug, box));
      cells.unshift(h(doc, 'td', { 'data-col': 'compare' }, box));
    }
    return h(doc, 'tr', { 'data-slug': m.slug, class: m.rankingEligible ? null : 'is-unranked' }, ...cells);
  });
  tbody.replaceChildren(...rowNodes);
}

export function loadData(doc) {
  return JSON.parse(doc.getElementById('rankings-data').textContent);
}

function stateStore(win, data) {
  const defaults = defaultState(data);
  const sync = createUrlSync(win, defaults);
  return {
    defaults,
    initial: () => sync.read(),
    // The chart tab belongs to the chart layer (pages/boot.js writes it), so keep whatever the URL holds now.
    write: (state) => sync.write({ ...state, chart: sync.read().chart }),
    // Round-trip through the URL grammar so every value is validated and clamped the same way.
    normalize: (candidate) => ({ ...parseState(serializeState(candidate, defaults), defaults), compare: candidate.compare }),
  };
}

function announce(win, detail) {
  win.document.dispatchEvent(new win.CustomEvent('vr:statechange', { detail }));
}

function showError(doc) {
  const loading = doc.querySelector('[data-state="loading"]');
  if (loading) loading.hidden = true;
  doc.getElementById('rankings-error').hidden = false;
}

function bindWeight(slider, output, state) {
  const shown = Number(state.w).toFixed(1);
  if (Number(slider.value) !== state.w) slider.value = String(state.w);
  output.textContent = `${shown}%`;
}

export function initRankings(win) {
  const doc = win.document;
  const $ = (id) => doc.getElementById(id);
  let data;
  try {
    data = loadData(doc);
  } catch {
    showError(doc);
    return;
  }
  const catalog = columnCatalog(data.dimensions);
  const store = stateStore(win, data);
  const expanded = new Set();
  const table = $('rankings-table');
  const modelBase = table.getAttribute('data-model-base') || DEFAULT_MODEL_BASE;
  const form = $('filters');
  const field = (name) => form.querySelector(`[name="${name}"]`);
  const checked = (name) => [...form.querySelectorAll(`input[name="${name}"]`)].filter((i) => i.checked).map((i) => i.value);
  const routes = [...form.querySelectorAll('input[name="route"]')];
  let state = store.initial();
  let scored = [];
  let visible = [];
  let shown = [];
  const exportUrls = { csv: null, json: null };

  const update = (patch) => {
    state = store.normalize({ ...state, ...patch });
    store.write(state);
    render();
  };

  const onSort = (col) => {
    if (state.sort === col.key) update({ dir: state.dir === 'asc' ? 'desc' : 'asc' });
    else update({ sort: col.key, dir: col.defaultDir });
  };

  const onCompare = (slug, box) => {
    if (!box.checked) return update({ compare: state.compare.filter((s) => s !== slug) });
    if (state.compare.length >= MAX_COMPARE) {
      box.checked = false;
      return undefined;
    }
    return update({ compare: [...state.compare, slug] });
  };

  function headerCell(col) {
    const active = state.sort === col.key;
    const sortState = state.dir === 'asc' ? 'ascending' : 'descending';
    const label = col.key === 'cost' ? costHeader(data, state.basis) : col.label;
    const button = h(doc, 'button', { type: 'button', class: 'sort-btn', text: label });
    button.addEventListener('click', () => onSort(col));
    return h(doc, 'th', {
      scope: 'col', 'data-col': col.key, 'aria-sort': active ? sortState : 'none', class: LEFT_ALIGNED.includes(col.key) ? null : 'num',
    }, button);
  }

  function renderCompare() {
    const drawer = $('compare-drawer');
    const body = $('compare-body');
    drawer.hidden = state.compare.length === 0;
    if (state.compare.length < 2) {
      body.replaceChildren(state.compare.length ? 'Select at least one more model to compare.' : '');
      return;
    }
    const { models, rows } = compareRows(scored, state.compare, data.dimensions, state.basis);
    const picked = models.map((m) => scored.find((s) => s.slug === m.slug));
    const extra = [
      { label: 'Overall', values: picked.map((m) => m.overall[state.basis]) },
      { label: 'Quality', values: picked.map((m) => m.quality) },
    ].map((r) => ({ ...r, best: bestIndexes(r.values) }));
    const line = (r) => h(doc, 'tr', {}, h(doc, 'th', { scope: 'row', text: r.label }),
      ...r.values.map((v, i) => h(doc, 'td', { class: r.best.includes(i) ? 'num is-best' : 'num', text: fmtScore(v) })));
    const removers = models.map((m) => {
      const button = h(doc, 'button', { type: 'button', 'data-remove': m.slug, 'aria-label': `Remove ${m.name} from comparison`, text: 'Remove' });
      button.addEventListener('click', () => update({ compare: state.compare.filter((s) => s !== m.slug) }));
      return h(doc, 'td', {}, button);
    });
    body.replaceChildren(h(doc, 'table', { class: 'compare-table' },
      h(doc, 'thead', {}, h(doc, 'tr', {}, h(doc, 'th', { scope: 'col', text: 'Dimension' }), ...models.map((m) => h(doc, 'th', { scope: 'col', text: m.name })))),
      h(doc, 'tbody', {}, ...[...extra, ...rows].map(line)),
      h(doc, 'tfoot', {}, h(doc, 'tr', {}, h(doc, 'td', {}), ...removers))));
  }

  function syncControls() {
    bindWeight($('cost-weight'), $('cost-weight-value'), state);
    toggle.set(state.basis);
    if (field('q').value.trim() !== state.q) field('q').value = state.q;
    field('cov').value = String(state.cov);
    $('filter-cov-value').textContent = `${state.cov}%`;
    routes.forEach((r) => { r.checked = r.value === state.route; });
    form.querySelectorAll('input[name="provider"]').forEach((i) => { i.checked = state.provider.includes(i.value); });
    form.querySelectorAll('input[name="grade"]').forEach((i) => { i.checked = state.grade.includes(i.value); });
    $('column-picker-list').querySelectorAll('input').forEach((i) => {
      i.checked = i.getAttribute('data-col') === 'name' || state.cols.includes(i.getAttribute('data-col'));
    });
  }

  function render() {
    scored = recompute(data.models, state.basis, state.w);
    visible = catalog.filter((c) => c.key === 'name' || state.cols.includes(c.key));
    shown = sortModels(applyFilters(scored, state), state.sort, state.dir, state.basis);
    const ctx = { basis: state.basis, expanded, modelBase, compare: state.compare, onCompare };
    $('rankings-head').replaceChildren(h(doc, 'tr', {},
      h(doc, 'th', { scope: 'col', 'data-col': 'compare' }, h(doc, 'span', { class: 'sr-only', text: 'Compare' })),
      ...visible.map(headerCell)));
    fillBody(doc, $('rankings-body'), shown, visible, ctx, true);
    $('rankings-empty').hidden = shown.length > 0;
    $('rankings-error').hidden = true;
    $('rankings-count').textContent = `${shown.length} of ${scored.length} models`;
    syncControls();
    syncBasisText(doc, data.bases, state.basis);
    renderCompare();
    announce(win, { state, models: scored, data });
  }

  function exporter(id, ext, mime, build) {
    const link = $(id);
    link.addEventListener('click', () => {
      const columns = visible.map((c) => (c.key === 'cost' ? { ...c, label: costHeader(data, state.basis) } : c));
      const url = win.URL.createObjectURL(new win.Blob([build(shown, columns, state.basis)], { type: mime }));
      if (exportUrls[ext]) win.URL.revokeObjectURL(exportUrls[ext]);
      exportUrls[ext] = url;
      link.setAttribute('href', url);
      link.setAttribute('download', exportFilename(state.basis, data.version, ext));
    });
  }

  const toggle = initBasisToggle($('basis-toggle'), state.basis, (basis) => update({ basis }));
  $('cost-weight').addEventListener('input', () => update({ w: Number($('cost-weight').value) }));
  form.querySelectorAll('input, select').forEach((c) => c.addEventListener('input', () => update({
    q: field('q').value, cov: Number(field('cov').value), route: routes.find((r) => r.checked).value, provider: checked('provider'), grade: checked('grade'),
  })));
  form.addEventListener('submit', (event) => event.preventDefault());
  doc.querySelectorAll('[data-action="reset-filters"]').forEach((button) => button.addEventListener('click', () => update({
    provider: [], grade: [], route: 'all', cov: 0, q: '',
  })));
  const share = doc.querySelector('[data-share]');
  share.addEventListener('click', async () => {
    try {
      await win.navigator.clipboard.writeText(win.location.href);
      share.textContent = 'Link copied';
    } catch {
      share.textContent = 'Copy the address bar link';
    }
  });
  $('compare-clear').addEventListener('click', () => update({ compare: [] }));
  $('column-picker-list').replaceChildren(...catalog.map((c) => h(doc, 'label', { class: 'col-option' },
    h(doc, 'input', { type: 'checkbox', 'data-col': c.key, disabled: c.key === 'name' }), ` ${c.label}`)));
  $('column-picker-list').querySelectorAll('input').forEach((i) => i.addEventListener('change', () => update({
    cols: [...$('column-picker-list').querySelectorAll('input')].filter((b) => b.checked).map((b) => b.getAttribute('data-col')),
  })));
  exporter('export-csv', 'csv', 'text/csv;charset=utf-8', toCsv);
  exporter('export-json', 'json', 'application/json', toJson);
  render();
}

const INDEX_COLUMNS = ['rank', 'name', 'overall', 'quality', 'cost', 'grade', 'coverage'];
const INDEX_ROWS = 16;

export function initIndex(win) {
  const doc = win.document;
  const $ = (id) => doc.getElementById(id);
  const data = loadData(doc);
  const store = stateStore(win, data);
  const catalog = columnCatalog(data.dimensions).filter((c) => INDEX_COLUMNS.includes(c.key));
  const columns = INDEX_COLUMNS.map((k) => catalog.find((c) => c.key === k));
  const tbody = $('index-body');
  const ctx = { expanded: new Set(), compare: [], modelBase: tbody.getAttribute('data-model-base') || DEFAULT_MODEL_BASE };
  let state = store.initial();

  const update = (patch) => {
    state = store.normalize({ ...state, ...patch });
    store.write(state);
    render();
  };

  // The second pick compares against the other basis, so score that one at the same cost weight.
  const withOtherBasis = (scored) => recompute(scored, Object.keys(data.bases).find((k) => k !== state.basis), state.w);

  function renderPicks(scored) {
    const chosen = state.w === data.costWeightPct ? data.picks[state.basis] : picks(withOtherBasis(scored), state.basis, data.bases);
    doc.querySelectorAll('[data-pick]').forEach((box) => {
      const pick = chosen[box.getAttribute('data-pick')];
      box.hidden = !pick;
      if (!pick) return;
      const model = scored.find((m) => m.slug === pick.slug);
      const name = box.querySelector('[data-pick-name]');
      name.textContent = model.name;
      name.setAttribute('href', `${ctx.modelBase}${model.slug}/`);
      const score = box.querySelector('[data-pick-score]');
      box.querySelector('[data-pick-label]').textContent = pick.label;
      score.replaceChildren(fmtScore(pick.score), h(doc, 'span', { class: 'unit', text: pick.unit }));
      box.querySelector('[data-pick-reason]').textContent = pick.reason;
    });
  }

  function render() {
    const scored = recompute(data.models, state.basis, state.w);
    const top = scored.filter((m) => m.rank[state.basis] !== null).sort((a, b) => a.rank[state.basis] - b.rank[state.basis]).slice(0, INDEX_ROWS);
    fillBody(doc, tbody, top, columns, { ...ctx, basis: state.basis }, false);
    renderPicks(scored);
    bindWeight($('cost-weight'), $('cost-weight-value'), state);
    toggle.set(state.basis);
    syncBasisText(doc, data.bases, state.basis);
    announce(win, { state, models: scored, data });
  }

  const toggle = initBasisToggle($('basis-toggle'), state.basis, (basis) => update({ basis }));
  $('cost-weight').addEventListener('input', () => update({ w: Number($('cost-weight').value) }));
  render();
}
