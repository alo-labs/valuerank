// Pure display formatting shared by every page. No DOM access.

export const GRADES = ['measured', 'claim', 'estimate', 'assumption', 'missing'];

const LABELS = {
  measured: 'User-measured',
  claim: 'Provider claim',
  estimate: 'Modelled',
  assumption: 'Assumption',
  missing: 'Missing',
};
// The grade descriptions shown in evidence notes; the same sentences as templates/partials/badge.html.
const DESCRIPTIONS = {
  measured: 'Measured by the benchmark owner or in a controlled account measurement.',
  claim: 'Published by the model provider for the exact benchmark version and evaluated variant.',
  estimate: 'Owner estimate or projection anchored to a measurement.',
  assumption: 'Explicitly authorised assumption with no measurement.',
  missing: 'No eligible value; excluded from the score and the score is renormalised.',
};
const BADGES = {
  measured: 'Measured',
  claim: 'Claim',
  estimate: 'Modelled',
  assumption: 'Assumed',
  missing: 'Missing',
};

const isNum = (v) => v !== null && v !== undefined && Number.isFinite(Number(v));

export function fmtUsd(v, digits = 2) {
  if (!isNum(v)) return '—';
  return '$' + Number(v).toLocaleString('en-US', { minimumFractionDigits: digits, maximumFractionDigits: digits });
}

export function fmtPct(v, digits = 1) {
  return isNum(v) ? `${Number(v).toFixed(digits)}%` : '—';
}

export function fmtScore(v) {
  return isNum(v) ? Number(v).toFixed(1) : '—';
}

export function fmtMultiple(v) {
  return isNum(v) ? `${Number(v).toLocaleString('en-US', { maximumFractionDigits: 3 })}×` : '—';
}

export function gradeLabel(grade) {
  return LABELS[grade] || 'Unknown';
}

export function gradeDescription(grade) {
  return DESCRIPTIONS[grade] || DESCRIPTIONS.missing;
}

export function gradeBadge(grade) {
  return BADGES[grade] || '?';
}

export function coverageNote(model) {
  const cov = model.coverage;
  if (!cov) return '';
  const detail = cov.missing.length
    ? `Missing: ${cov.missing.join(', ')}`
    : cov.pct < 99.995 ? 'Some retained metrics unavailable' : 'All retained metrics available';
  return `Coverage ${Number(cov.pct).toFixed(1)}% · ${detail}`;
}

export function escapeHtml(text) {
  return String(text)
    .replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;').replaceAll("'", '&#39;');
}
