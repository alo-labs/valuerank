// Pure filtering, sorting and column catalogue for the rankings table.
import { GRADES } from './format.js';
import { costValue } from './scoring.js';

export const DEFAULT_COLUMNS = ['rank', 'name', 'overall', 'quality', 'cost', 'grade', 'coverage'];

const CORE = [
  { key: 'rank', label: 'Rank', defaultDir: 'asc' },
  { key: 'name', label: 'Model', defaultDir: 'asc' },
  { key: 'overall', label: 'Overall', defaultDir: 'desc' },
  { key: 'quality', label: 'Quality', defaultDir: 'desc' },
  { key: 'cost', label: 'Cost', defaultDir: 'asc' },
  // Data only: kept in the view state, URL, sort and export, but never drawn as a table column (evidence is footnoted).
  { key: 'grade', label: 'Evidence', defaultDir: 'asc', dataOnly: true },
  { key: 'coverage', label: 'Coverage', defaultDir: 'desc' },
  { key: 'developer', label: 'Developer', defaultDir: 'asc' },
  { key: 'qualityRank', label: 'Quality rank', defaultDir: 'asc' },
  { key: 'speed', label: 'Speed', defaultDir: 'desc' },
  { key: 'ii', label: 'Intelligence Index', defaultDir: 'desc' },
];

export function columnCatalog(dimensions) {
  const dimCols = dimensions
    .filter((d) => d.category !== 'cost')
    .map((d) => ({ key: d.key, label: d.label, defaultDir: 'desc', group: d.category }));
  return [...CORE.map((c) => ({ ...c, group: 'core' })), ...dimCols]
    .map((c) => ({ ...c, default: DEFAULT_COLUMNS.includes(c.key) }));
}

/** The raw value of a column for a model under a basis (null when missing). */
export function columnValue(model, key, basis) {
  switch (key) {
    case 'rank': return model.rank[basis];
    case 'overall': return model.overall[basis];
    case 'cost': return costValue(model, basis);
    case 'coverage': return model.coverage ? model.coverage.pct : null;
    case 'ii': return model.intelligenceIndex.value;
    case 'name': case 'developer': case 'grade': case 'quality': case 'qualityRank': case 'speed':
      return model[key];
    default: return model.dims[key] ?? null;
  }
}

export function applyFilters(models, state) {
  const q = state.q.toLowerCase();
  return models.filter((m) => {
    if (state.provider.length && !state.provider.includes(m.developer)) return false;
    if (state.grade.length && !state.grade.includes(m.grade)) return false;
    if (state.route === 'eligible' && !m.cost.route) return false;
    if (state.route === 'fallback' && !m.cost.fallback) return false;
    if (state.cov > 0 && !(m.coverage && m.coverage.pct >= state.cov)) return false;
    if (q && !`${m.name} ${m.developer}`.toLowerCase().includes(q)) return false;
    return true;
  });
}

const sortable = (model, key, basis) => {
  const v = columnValue(model, key, basis);
  return key === 'grade' ? GRADES.indexOf(v) : v;
};

export function sortModels(models, sort, dir, basis) {
  const sign = dir === 'desc' ? -1 : 1;
  const compare = (a, b) => {
    const va = sortable(a, sort, basis) ?? null;
    const vb = sortable(b, sort, basis) ?? null;
    if (va === null || vb === null) {
      if (va !== vb) return va === null ? 1 : -1;
    } else if (va !== vb) {
      return sign * (typeof va === 'string' ? va.localeCompare(vb) : va - vb);
    }
    return a.name.localeCompare(b.name);
  };
  return [...models].sort(compare);
}
