const fs = require('fs');
const path = require('path');
const dir = __dirname;

const aa = JSON.parse(fs.readFileSync(path.join(dir, 'aa_benchmark_rows.json'), 'utf8'));
const tbRaw = JSON.parse(fs.readFileSync(path.join(dir, '../tb21/tbench_entries.json'), 'utf8'));

function comps(r) {
  const out = {};
  for (const e of (r.evals || [])) {
    const name = e.evaluationDatasetSlug || e.datasetIndexName;
    out[name] = +(e.mean?.reward || 0);
  }
  return out;
}

const cohort = aa.map(r => {
  const c = comps(r);
  return {
    id: r.id,
    agent: r.display?.agent || r.agentName,
    model: r.display?.model || '',
    label: `${r.display?.agent || r.agentName} + ${r.display?.model || ''}`,
    displayLabel: r.displayLabel,
    indexScore: +(r.indexScore || 0) * 100, // store as 0-100 for readability
    indexRaw: +r.indexScore,
    costUsd: r.mean?.costUsd != null ? +r.mean.costUsd : null,
    wallTimeSec: r.mean?.agentWallTimeSec != null ? +r.mean.agentWallTimeSec : null,
    deepSWE: (c['DeepSWE'] ?? c['deep-swe'] ?? null) != null ? +(c['DeepSWE'] ?? c['deep-swe']) * 100 : null,
    tbv2: (c['Terminal-Bench v2'] ?? c['terminal-bench-v2'] ?? null) != null ? +(c['Terminal-Bench v2'] ?? c['terminal-bench-v2']) * 100 : null,
    sweAtlas: (c['SWE-Atlas-QnA'] ?? c['swe-atlas-qna'] ?? null) != null ? +(c['SWE-Atlas-QnA'] ?? c['swe-atlas-qna']) * 100 : null,
  };
}).filter(r => r.costUsd != null && Number.isFinite(r.costUsd));

console.log('cohort with cost', cohort.length, 'dropped', aa.length - cohort.length);

// Parse TB21
const tb21 = tbRaw.map(r => ({
  rank: +r.Rank,
  agent: r.Agent,
  model: r.Model,
  effort: r.Effort,
  accuracy: parseFloat(String(r.Accuracy).replace('%', '')),
  cost: parseFloat(String(r.Cost).replace(/[$,]/g, '')),
}));

// Family-level alias mapping: AA agent+model family → best matching TB21 accuracy
// Rules from methodology: match agent harness + model family; effort settings share family score
function normalizeModelFamily(model) {
  // Strip effort suffixes in parentheses
  let m = model.replace(/\s*\([^)]*\)\s*$/, '').trim();
  // Normalize names
  m = m.replace(/^Claude\s+/i, '');
  m = m.replace(/^GPT-/i, 'GPT-');
  return m;
}

function familyKey(agent, model) {
  const a = agent.replace(/\s+CLI$/i, '').replace(/\s+Code$/i, ' Code').trim();
  // Codex CLI vs Codex
  const agentNorm = a.replace(/^Codex$/i, 'Codex').replace(/^Claude Code$/i, 'Claude Code');
  return agentNorm.toLowerCase() + '|' + normalizeModelFamily(model).toLowerCase();
}

// Build TB lookup by agent+model family (ignore effort for alias). Prefer higher accuracy if multiple.
const tbByFamily = new Map();
for (const row of tb21) {
  // Map TB agent names to AA
  let agent = row.agent;
  if (/^Codex$/i.test(agent)) agent = 'Codex';
  const key = familyKey(agent, row.model);
  const prev = tbByFamily.get(key);
  if (!prev || row.accuracy > prev.accuracy) tbByFamily.set(key, row);
}
// Also try without "CLI"
console.log('TB families:', [...tbByFamily.keys()]);

function lookupTB(agent, model) {
  const fam = normalizeModelFamily(model);
  const candidates = [
    familyKey(agent, model),
    familyKey(agent.replace(/ CLI$/i, ''), model),
    familyKey(agent, fam),
  ];
  // Fuzzy: agent contains + model family contains
  for (const [k, v] of tbByFamily) {
    const [ta, tm] = k.split('|');
    const aa = agent.toLowerCase().replace(/ cli$/, '');
    const am = fam.toLowerCase();
    if ((ta.includes(aa) || aa.includes(ta.replace(/ code$/, ''))) && (tm === am || tm.includes(am) || am.includes(tm))) {
      return v;
    }
  }
  for (const c of candidates) {
    if (tbByFamily.has(c)) return tbByFamily.get(c);
  }
  // Direct model family match on same agent class
  for (const [k, v] of tbByFamily) {
    const [ta, tm] = k.split('|');
    const agentOk =
      (agent.toLowerCase().includes('claude') && ta.includes('claude')) ||
      (agent.toLowerCase().includes('codex') && ta.includes('codex')) ||
      (agent.toLowerCase().includes('cursor') && ta.includes('cursor')) ||
      (agent.toLowerCase().includes('gemini') && ta.includes('gemini')) ||
      (agent.toLowerCase().includes('opencode') && ta.includes('opencode'));
    const modelOk = tm === fam.toLowerCase() ||
      fam.toLowerCase().startsWith(tm) ||
      tm.startsWith(fam.toLowerCase()) ||
      // Opus 4.8 matches Opus 4.8; GPT-5.6 Sol matches GPT-5.6 Sol
      fam.toLowerCase().replace(/\s+/g,'') === tm.replace(/\s+/g,'');
    if (agentOk && modelOk) return v;
  }
  return null;
}

for (const r of cohort) {
  const hit = lookupTB(r.agent, r.model);
  r.tb21Accuracy = hit ? hit.accuracy : null;
  r.tb21Coverage = hit ? 'Covered' : 'Neutralized';
  r.tb21Match = hit ? `${hit.agent} + ${hit.model} (${hit.effort})` : null;
}

const covered = cohort.filter(r => r.tb21Accuracy != null);
console.log('TB covered', covered.length, '/', cohort.length);
console.log(covered.map(r => `${r.label} -> ${r.tb21Accuracy} via ${r.tb21Match}`).join('\n'));

// Rank percentile normalization: higher better for AA and TB; lower better for cost
// norm = 100 * (n - rank) / (n - 1) with rank 1 = best; ties get average rank
function rankNorm(values, higherIsBetter) {
  const n = values.length;
  const indexed = values.map((v, i) => ({ v, i }));
  indexed.sort((a, b) => higherIsBetter ? (b.v - a.v) || (a.i - b.i) : (a.v - b.v) || (a.i - b.i));
  const ranks = new Array(n);
  let i = 0;
  while (i < n) {
    let j = i;
    while (j + 1 < n && indexed[j + 1].v === indexed[i].v) j++;
    const avgRank = (i + j) / 2 + 1; // 1-based average
    for (let k = i; k <= j; k++) ranks[indexed[k].i] = avgRank;
    i = j + 1;
  }
  if (n === 1) return values.map(() => 100);
  return ranks.map(rank => 100 * (n - rank) / (n - 1));
}

const aaNorms = rankNorm(cohort.map(r => r.indexRaw), true);
const costNorms = rankNorm(cohort.map(r => r.costUsd), false); // lower cost better

// TB: among covered only; uncovered = 50
const coveredIdx = cohort.map((r, i) => r.tb21Accuracy != null ? i : -1).filter(i => i >= 0);
const tbCoveredNorms = rankNorm(coveredIdx.map(i => cohort[i].tb21Accuracy), true);
const tbNorms = cohort.map(() => 50);
coveredIdx.forEach((ci, j) => { tbNorms[ci] = tbCoveredNorms[j]; });

const scored = cohort.map((r, i) => {
  const AAIndexNorm = aaNorms[i];
  const CostNorm = costNorms[i];
  const TB21Norm = tbNorms[i];
  const Quality = 0.80 * AAIndexNorm + 0.20 * TB21Norm;
  const Overall = 0.25 * CostNorm + 0.60 * AAIndexNorm + 0.15 * TB21Norm;
  return {
    ...r,
    AAIndexNorm: +AAIndexNorm.toFixed(1),
    CostNorm: +CostNorm.toFixed(1),
    TB21Norm: +TB21Norm.toFixed(1),
    Quality: +Quality.toFixed(1),
    Overall: +Overall.toFixed(1),
  };
}).sort((a, b) => b.Overall - a.Overall || b.Quality - a.Quality);

scored.forEach((r, i) => { r.rank = i + 1; });

fs.writeFileSync(path.join(dir, 'valuerank_scores.json'), JSON.stringify(scored, null, 2));
fs.writeFileSync(path.join(dir, 'tb21_snapshot.json'), JSON.stringify({
  scrapedAt: '2026-07-28',
  source: 'https://www.tbench.ai/leaderboard/terminal-bench/2.1',
  count: tb21.length,
  entries: tb21,
}, null, 2));

console.log('\n=== TOP 15 ===');
for (const r of scored.slice(0, 15)) {
  console.log(`${String(r.rank).padStart(2)} ${r.Overall.toFixed(1).padStart(5)} Q=${r.Quality.toFixed(1).padStart(5)} C=${String(r.CostNorm).padStart(5)} AA=${String(r.AAIndexNorm).padStart(5)} TB=${String(r.TB21Norm).padStart(5)} ${r.tb21Coverage[0]} | ${r.label} idx=${r.indexScore.toFixed(1)} cost=$${r.costUsd.toFixed(3)} tb=${r.tb21Accuracy ?? '-'}`);
}
console.log('\nTOTAL', scored.length);
console.log('Frontier cost leaders:', scored.filter(r => r.CostNorm >= 90).map(r => r.label + ' $' + r.costUsd.toFixed(3)));
