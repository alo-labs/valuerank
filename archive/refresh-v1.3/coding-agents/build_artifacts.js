const fs = require('fs');
const path = require('path');
const dir = __dirname;
const root = path.join(dir, '../..', '..');
const scored = JSON.parse(fs.readFileSync(path.join(dir, 'valuerank_scores.json'), 'utf8'));
const tb21 = JSON.parse(fs.readFileSync(path.join(dir, 'tb21_snapshot.json'), 'utf8'));
const DATE = 'July 28, 2026';
const SHORT = 'Jul 28, 2026';

function fmt(n, d=1) { return Number(n).toFixed(d); }
function money(n) { return '$' + Number(n).toFixed(3); }

// --- scores.md ---
let scores = `# Coding Agent ValueRank - Scores

Last updated: ${DATE}

Formula:

\`\`\`text
Overall = 0.25 * CostNorm + 0.60 * AAIndexNorm + 0.15 * TB2.1Norm
\`\`\`

Rows without official Terminal Bench 2.1 coverage receive neutral TB2.1 normalization (50).

| Rank | Agent Variant | Overall | Quality | CostNorm | AAIndexNorm | TB2.1Norm | TB2.1 Coverage |
|---:|---|---:|---:|---:|---:|---:|---|
`;
for (const r of scored) {
  scores += `| ${r.rank} | ${r.label} | ${fmt(r.Overall)} | ${fmt(r.Quality)} | ${fmt(r.CostNorm)} | ${fmt(r.AAIndexNorm)} | ${fmt(r.TB21Norm)} | ${r.tb21Coverage} |\n`;
}
fs.writeFileSync(path.join(root, 'coding-agents-valuerank/scores.md'), scores);

// --- raw-data.md ---
let raw = `# Coding Agent ValueRank - Raw Data

Last updated: ${DATE}

Sources:

- Artificial Analysis Coding Agents: https://artificialanalysis.ai/agents/coding-agents
- Terminal Bench 2.1: https://www.tbench.ai/leaderboard/terminal-bench/2.1

## Artificial Analysis Cohort

AA Coding Agent Index v1.3 components: DeepSWE, Terminal-Bench v2, SWE-Atlas-QnA (equal weight). Index shown as 0–100.

| Agent | Model / Setting | AA Index | Cost / Task | Time / Task | DeepSWE | TB v2 | SWE-Atlas-QnA | TB2.1 |
|---|---|---:|---:|---:|---:|---:|---:|---:|
`;
const byLabel = [...scored].sort((a,b) => a.agent.localeCompare(b.agent) || a.model.localeCompare(b.model));
for (const r of byLabel) {
  raw += `| ${r.agent} | ${r.model} | ${fmt(r.indexScore)} | ${money(r.costUsd)} | ${fmt(r.wallTimeSec,1)}s | ${r.deepSWE!=null?fmt(r.deepSWE):'-'} | ${r.tbv2!=null?fmt(r.tbv2):'-'} | ${r.sweAtlas!=null?fmt(r.sweAtlas):'-'} | ${r.tb21Accuracy!=null?fmt(r.tb21Accuracy):'-'} |\n`;
}

raw += `
## Terminal Bench 2.1 Source Rows

The official Terminal Bench 2.1 page listed ${tb21.count} entries at verification time (${DATE}). These rows are used only where they match the Artificial Analysis cohort (family-level alias).

| Rank | Agent | Model | Effort | Accuracy | Cost |
|---:|---|---|---|---:|---:|
`;
for (const r of tb21.entries) {
  raw += `| ${r.rank} | ${r.agent} | ${r.model} | ${r.effort} | ${fmt(r.accuracy)}% | $${r.cost.toFixed(2)} |\n`;
}

raw += `
## TB2.1 Family Mapping Used

| AA Rows (family) | TB2.1 Match | Accuracy |
|---|---|---:|
`;
const maps = new Map();
for (const r of scored.filter(x => x.tb21Accuracy != null)) {
  const fam = `${r.agent} + ${r.model.replace(/\s*\([^)]*\)\s*$/, '').trim()}`;
  if (!maps.has(fam)) maps.set(fam, r);
}
for (const [fam, r] of maps) {
  raw += `| ${fam} (*effort variants) | ${r.tb21Match} | ${fmt(r.tb21Accuracy)}% |\n`;
}
fs.writeFileSync(path.join(root, 'coding-agents-valuerank/raw-data.md'), raw);

// meta for site
const top5 = scored.slice(0,5);
const siteData = {
  updated: DATE,
  shortDate: SHORT,
  version: 'v1.3',
  formula: '0.25*Cost + 0.60*AA + 0.15*TB21',
  cohortSize: scored.length,
  tb21Size: tb21.count,
  tb21Covered: scored.filter(r => r.tb21Coverage === 'Covered').length,
  top5: top5.map(r => ({ rank: r.rank, label: r.label, overall: r.Overall, quality: r.Quality, costNorm: r.CostNorm, aa: r.AAIndexNorm, tb: r.TB21Norm, coverage: r.tb21Coverage, indexScore: +r.indexScore.toFixed(1), costUsd: +r.costUsd.toFixed(3) })),
  agents: scored.map(r => ({
    rank: r.rank,
    agent: r.agent,
    model: r.model,
    label: r.label,
    overall: r.Overall,
    quality: r.Quality,
    costNorm: r.CostNorm,
    aaNorm: r.AAIndexNorm,
    tbNorm: r.TB21Norm,
    tbCoverage: r.tb21Coverage,
    tb21: r.tb21Accuracy,
    indexScore: +r.indexScore.toFixed(1),
    costUsd: +r.costUsd.toFixed(3),
    wallTimeSec: r.wallTimeSec != null ? +r.wallTimeSec.toFixed(1) : null,
    deepSWE: r.deepSWE != null ? +r.deepSWE.toFixed(1) : null,
    tbv2: r.tbv2 != null ? +r.tbv2.toFixed(1) : null,
    sweAtlas: r.sweAtlas != null ? +r.sweAtlas.toFixed(1) : null,
  })),
};
fs.writeFileSync(path.join(dir, 'site_embed.json'), JSON.stringify(siteData, null, 2));
console.log('Wrote scores/raw-data; cohort', scored.length, 'top5', top5.map(r=>r.label).join(' | '));
