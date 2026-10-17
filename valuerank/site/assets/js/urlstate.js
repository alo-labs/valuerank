// URL view state: parse and serialize the query parameters listed in docs/site-data-contract.md.
import { GRADES } from './format.js';

const BASES = ['api', 'plan'];
const DIRS = ['asc', 'desc'];
const ROUTES = ['all', 'eligible', 'fallback'];
const TOKEN = /^[A-Za-z0-9_-]+$/;
const KEYS = ['basis', 'w', 'sort', 'dir', 'cols', 'provider', 'grade', 'route', 'cov', 'q', 'compare', 'chart'];

const round1 = (n) => Math.round(n * 10) / 10;
const clamp = (n, lo, hi) => Math.min(hi, Math.max(lo, n));
const number = (raw) => (raw === '' || !Number.isFinite(Number(raw)) ? null : Number(raw));
const list = (raw) => raw.split(',').map((s) => s.trim()).filter(Boolean);
const oneOf = (allowed) => (raw) => (allowed.includes(raw) ? raw : null);
const token = (raw) => (TOKEN.test(raw) ? raw : null);
const nonEmpty = (items) => (items.length ? items : null);

const PARSERS = {
  basis: oneOf(BASES),
  dir: oneOf(DIRS),
  route: oneOf(ROUTES),
  sort: token,
  chart: token,
  w: (raw, def) => {
    const n = number(raw);
    if (n === null) return null;
    const v = round1(clamp(n, 0, 100));
    return v === round1(def) ? def : v;
  },
  cov: (raw) => {
    const n = number(raw);
    return n === null ? null : clamp(n, 0, 100);
  },
  q: (raw) => raw.trim().slice(0, 100),
  cols: (raw) => nonEmpty(list(raw).filter((s) => TOKEN.test(s))),
  grade: (raw) => nonEmpty(list(raw).filter((s) => GRADES.includes(s))),
  provider: (raw) => nonEmpty(list(raw)),
  compare: (raw) => {
    const slugs = [...new Set(list(raw))];
    if (slugs.some((s) => !TOKEN.test(s))) return null;
    return slugs.length >= 2 ? slugs.slice(0, 4) : null;
  },
};

export function parseState(search, defaults) {
  const state = structuredClone(defaults);
  const params = new URLSearchParams(search);
  for (const key of KEYS) {
    if (!params.has(key)) continue;
    const parsed = PARSERS[key](params.get(key), defaults[key]);
    if (parsed !== null) state[key] = parsed;
  }
  return state;
}

function isDefault(key, value, def) {
  if (key === 'w') return round1(value) === round1(def);
  return JSON.stringify(value) === JSON.stringify(def);
}

export function serializeState(state, defaults) {
  const parts = [];
  for (const key of KEYS) {
    const value = state[key];
    if (value === undefined || isDefault(key, value, defaults[key])) continue;
    if (key === 'compare' && value.length < 2) continue;
    if (Array.isArray(value)) {
      const items = value.map((s) => String(s).replaceAll(',', '')).filter(Boolean);
      if (items.length) parts.push(`${key}=${items.map(encodeURIComponent).join(',')}`);
    } else {
      parts.push(`${key}=${encodeURIComponent(key === 'w' ? round1(value) : value)}`);
    }
  }
  return parts.length ? `?${parts.join('&')}` : '';
}
