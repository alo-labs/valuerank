import { test } from 'node:test';
import assert from 'node:assert/strict';
import * as theme from '../../../valuerank/site/assets/js/charts/theme.js';

test('colour tokens: developer, tier and fallbacks', () => {
  assert.equal(theme.developerColor('OpenAI'), '#10a37f');
  assert.equal(theme.developerColor('Nobody'), theme.FALLBACK_COLOR);
  assert.equal(theme.tierColor('Budget'), '#22c55e');
  assert.equal(theme.tierColor('?'), theme.FALLBACK_COLOR);
});

test('rankColor and scoreColor thresholds', () => {
  assert.deepEqual([1, 2, 3, 4].map(theme.rankColor), ['var(--gold)', 'var(--silver)', 'var(--bronze)', 'var(--muted)']);
  assert.deepEqual([70, 55, 40, 10].map(theme.scoreColor), ['#22c55e', '#3b82f6', '#f59e0b', '#ef4444']);
});

test('themeTokens picks palette by theme and reads CSS variables when given', () => {
  assert.equal(theme.themeTokens().dark, false);
  assert.equal(theme.themeTokens({ dark: true }).bg, '#111827');
  const read = theme.themeTokens({ getVar: (name) => (name === '--bg-card' ? ' #fafafa ' : ''), dark: false });
  assert.equal(read.bg, '#fafafa');
  assert.equal(read.text, '#475569');
  const nullish = theme.themeTokens({ getVar: () => undefined });
  assert.equal(nullish.grid, '#e2e8f0');
});

test('layout, title, axis helper, ring and theme update use the tokens', () => {
  const tokens = theme.themeTokens({ dark: true });
  const layout = theme.plotlyLayout(tokens);
  assert.equal(layout.paper_bgcolor, tokens.bg);
  assert.equal(layout.xaxis.gridcolor, tokens.grid);
  assert.notEqual(layout.xaxis.title, layout.yaxis.title);
  assert.deepEqual(theme.plotlyTitle(tokens), { color: tokens.title, size: 14 });
  assert.equal(theme.plotlyTitle(tokens, 13).size, 13);
  assert.equal(theme.axisWith(layout.xaxis, 'Cost', { type: 'log' }).title.text, 'Cost');
  assert.equal(theme.axisWith(layout.xaxis, 'Cost').type, undefined);
  assert.equal(theme.frontierRing(tokens), '#064e3b');
  assert.equal(theme.frontierRing(theme.themeTokens()), '#ecfdf5');
  const update = theme.plotlyThemeUpdate(tokens);
  assert.equal(update['yaxis.gridcolor'], tokens.grid);
  assert.equal(update['font.color'], tokens.text);
  assert.equal(theme.PLOTLY_CONFIG.displaylogo, false);
});
