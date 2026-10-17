import test from 'node:test';
import assert from 'node:assert/strict';
import {
  fmtUsd, fmtPct, fmtScore, fmtMultiple, gradeLabel, gradeBadge, GRADES, coverageNote, escapeHtml,
} from '../../../valuerank/site/assets/js/format.js';

test('fmtUsd formats with grouping and fixed digits; nulls become a dash', () => {
  assert.equal(fmtUsd(1081.5), '$1,081.50');
  assert.equal(fmtUsd(1.9312, 3), '$1.931');
  assert.equal(fmtUsd(null), '—');
  assert.equal(fmtUsd(undefined), '—');
  assert.equal(fmtUsd(Number.NaN), '—');
});

test('fmtPct, fmtScore and fmtMultiple', () => {
  assert.equal(fmtPct(88.644), '88.6%');
  assert.equal(fmtPct(88.644, 2), '88.64%');
  assert.equal(fmtPct(null), '—');
  assert.equal(fmtScore(74.25), '74.3');
  assert.equal(fmtScore(null), '—');
  assert.equal(fmtMultiple(10.7724), '10.772×');
  assert.equal(fmtMultiple(5), '5×');
  assert.equal(fmtMultiple(null), '—');
});

test('grade labels and short badge text follow the contract enum', () => {
  assert.deepEqual(GRADES, ['measured', 'claim', 'estimate', 'assumption', 'missing']);
  assert.equal(gradeLabel('measured'), 'Owner-measured');
  assert.equal(gradeLabel('claim'), 'Provider claim');
  assert.equal(gradeLabel('estimate'), 'Modelled');
  assert.equal(gradeLabel('assumption'), 'Assumption');
  assert.equal(gradeLabel('missing'), 'Missing');
  assert.equal(gradeLabel('weird'), 'Unknown');
  assert.equal(gradeBadge('measured'), 'Measured');
  assert.equal(gradeBadge('estimate'), 'Modelled');
  assert.equal(gradeBadge('weird'), '?');
});

test('coverageNote lists missing metrics or states full coverage', () => {
  assert.equal(coverageNote({ coverage: { pct: 88.64, missing: ['A', 'B'] } }), 'Coverage 88.6% · Missing: A, B');
  assert.equal(coverageNote({ coverage: { pct: 100, missing: [] } }), 'Coverage 100.0% · All retained metrics available');
  assert.equal(coverageNote({ coverage: { pct: 90, missing: [] } }), 'Coverage 90.0% · Some retained metrics unavailable');
  assert.equal(coverageNote({ coverage: null }), '');
  assert.equal(coverageNote({}), '');
});

test('escapeHtml escapes the five dangerous characters', () => {
  assert.equal(escapeHtml(`<a href="x">'&'</a>`), '&lt;a href=&quot;x&quot;&gt;&#39;&amp;&#39;&lt;/a&gt;');
});
