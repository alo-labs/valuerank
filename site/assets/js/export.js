// Pure CSV/JSON serialisation of the visible table.
import { columnValue } from './filters.js';

const cell = (v) => {
  if (v === null || v === undefined) return '';
  const s = String(v);
  return /[",\r\n]/.test(s) ? `"${s.replaceAll('"', '""')}"` : s;
};

export function toCsv(models, columns, basis) {
  const header = columns.map((c) => cell(c.label)).join(',');
  const rows = models.map((m) => columns.map((c) => cell(columnValue(m, c.key, basis))).join(','));
  return [header, ...rows].join('\r\n');
}

export function toJson(models, columns, basis) {
  const rows = models.map((m) => Object.fromEntries(columns.map((c) => [c.key, columnValue(m, c.key, basis) ?? null])));
  return JSON.stringify(rows, null, 2);
}

export function exportFilename(basis, version, ext) {
  return `valuerank-${version}-${basis}.${ext}`;
}
