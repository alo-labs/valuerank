// Theme tokens, colour maps and Plotly layout defaults shared by every chart.
export const PLOTLY_CONFIG = Object.freeze({
  responsive: true,
  displayModeBar: true,
  modeBarButtonsToRemove: ['select2d', 'lasso2d'],
  displaylogo: false,
});

export const TIER_COLORS = Object.freeze({
  'Budget': '#22c55e', 'Near-Budget': '#a3e635', 'Mid-Range': '#fbbf24',
  'Premium': '#fb923c', 'Expensive': '#f87171', 'Very Expensive': '#fca5a5', 'Ultra-Premium': '#fca5a5',
});

export const DEV_COLORS = Object.freeze({
  'Google DeepMind': '#4285F4', 'OpenAI': '#10a37f', 'Kay (alo-exp)': '#6366f1',
  'Moonshot AI': '#8b5cf6', 'Zhipu AI': '#06b6d4', 'Z AI': '#06b6d4', 'MiniMax': '#f59e0b',
  'Alibaba': '#ff6900', 'DeepSeek': '#64748b', 'Anthropic': '#d4a574',
  'Mistral AI': '#ff7043', 'Amazon': '#ff9900', 'xAI': '#1a1a2e', 'SpaceXAI': '#736cd3', 'Meta': '#0066ff',
  'Microsoft': '#0078d4', 'Xiaomi': '#ff6700', 'Z-AI': '#06b6d4',
});

export const CATEGORY_COLORS = Object.freeze({
  cost: '#22c55e', rely: '#a78bfa', code: '#3b82f6', intel: '#eab308', prod: '#f97316', language: '#ec4899',
});

export const FALLBACK_COLOR = '#64748b';
export const FRONTIER_COLOR = '#10b981';
export const DOMINATED_COLOR = '#a78bfa';
export const FONT_FAMILY = 'IBM Plex Sans,system-ui,sans-serif';

export const developerColor = (developer) => DEV_COLORS[developer] ?? FALLBACK_COLOR;
export const tierColor = (tier) => TIER_COLORS[tier] ?? FALLBACK_COLOR;

export function rankColor(rank) {
  if (rank === 1) return 'var(--gold)';
  if (rank === 2) return 'var(--silver)';
  if (rank === 3) return 'var(--bronze)';
  return 'var(--muted)';
}

export function scoreColor(score) {
  if (score >= 65) return '#22c55e';
  if (score >= 50) return '#3b82f6';
  if (score >= 35) return '#f59e0b';
  return '#ef4444';
}

const PALETTE = {
  light: { bg: '#ffffff', text: '#475569', grid: '#e2e8f0', title: '#0f172a', dim: '#cbd5e1', missing: '#e5e7eb' },
  dark: { bg: '#111827', text: '#cbd5e1', grid: '#1e293b', title: '#f1f5f9', dim: '#475569', missing: '#334155' },
};
const CSS_VARS = { bg: '--bg-card', text: '--text-secondary', grid: '--border', title: '--text-primary', dim: '--border-hover' };

/**
 * Colour tokens for the active theme. `getVar(name)` may read a CSS custom
 * property; an empty answer falls back to the built-in palette.
 */
export function themeTokens({ dark = false, getVar } = {}) {
  const base = PALETTE[dark ? 'dark' : 'light'];
  const tokens = { ...base, dark: Boolean(dark) };
  if (getVar) {
    for (const [key, name] of Object.entries(CSS_VARS)) tokens[key] = String(getVar(name) ?? '').trim() || base[key];
  }
  return tokens;
}

export const frontierRing = (tokens) => (tokens.dark ? '#064e3b' : '#ecfdf5');

export function plotlyLayout(tokens) {
  const axis = { gridcolor: tokens.grid, zerolinecolor: tokens.grid, tickfont: { color: tokens.text }, title: { font: { color: tokens.text } } };
  return {
    paper_bgcolor: tokens.bg,
    plot_bgcolor: tokens.bg,
    font: { family: FONT_FAMILY, color: tokens.text, size: 12 },
    margin: { t: 40, r: 20, b: 60, l: 60 },
    xaxis: { ...axis, tickfont: { ...axis.tickfont }, title: { font: { ...axis.title.font } } },
    yaxis: { ...axis, tickfont: { ...axis.tickfont }, title: { font: { ...axis.title.font } } },
  };
}

export const plotlyTitle = (tokens, size = 14) => ({ color: tokens.title, size });

/** Axis with a title string plus the themed defaults (Plotly 2 title object). */
export function axisWith(base, title, extra = {}) {
  return { ...base, ...extra, title: { ...base.title, text: title } };
}

/** relayout payload that re-themes an existing plot without rebuilding it. */
export function plotlyThemeUpdate(tokens) {
  return {
    paper_bgcolor: tokens.bg,
    plot_bgcolor: tokens.bg,
    'font.color': tokens.text,
    'title.font.color': tokens.title,
    'xaxis.gridcolor': tokens.grid,
    'xaxis.zerolinecolor': tokens.grid,
    'xaxis.tickfont.color': tokens.text,
    'xaxis.title.font.color': tokens.text,
    'yaxis.gridcolor': tokens.grid,
    'yaxis.zerolinecolor': tokens.grid,
    'yaxis.tickfont.color': tokens.text,
    'yaxis.title.font.color': tokens.text,
  };
}
