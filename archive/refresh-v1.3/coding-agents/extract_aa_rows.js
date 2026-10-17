const fs = require('fs');
const path = require('path');
const dir = __dirname;

function extractBalancedArray(str, startIdx) {
  let depth = 0, inStr = false, esc = false;
  for (let i = startIdx; i < str.length; i++) {
    const c = str[i];
    if (inStr) {
      if (esc) { esc = false; continue; }
      if (c === '\\') { esc = true; continue; }
      if (c === '"') inStr = false;
      continue;
    }
    if (c === '"') { inStr = true; continue; }
    if (c === '[') depth++;
    else if (c === ']') {
      depth--;
      if (depth === 0) return str.slice(startIdx, i + 1);
    }
  }
  return null;
}

function tryParseRows(text) {
  const marker = 'benchmarkRows';
  let from = 0;
  let best = null;
  while (true) {
    const idx = text.indexOf(marker, from);
    if (idx < 0) break;
    const bracket = text.indexOf('[', idx);
    if (bracket < 0) break;
    const arrStr = extractBalancedArray(text, bracket);
    if (arrStr && arrStr.length > 1000) {
      const attempts = [arrStr];
      if (arrStr.includes('\\"')) {
        attempts.push(arrStr.replace(/\\"/g, '"').replace(/\\\\/g, '\\'));
      }
      for (const a of attempts) {
        try {
          const rows = JSON.parse(a);
          if (!Array.isArray(rows)) continue;
          const clean = rows.filter(r => r && typeof r === 'object' && !Array.isArray(r) && r.agentName && r.indexScore != null && r.mean);
          if (clean.length >= 10 && (!best || clean.length > best.length)) best = clean;
        } catch {}
      }
    }
    from = idx + marker.length;
  }
  return best;
}

const html = fs.readFileSync(path.join(dir, 'aa-coding-agents.html'), 'utf8');
// Also try unescaping next payloads
const variants = [html];
for (const m of html.matchAll(/self\.__next_f\.push\(\[1,"([\s\S]*?)"\]\)/g)) {
  try { variants.push(JSON.parse('"' + m[1] + '"')); } catch {}
}
let best = null;
for (const v of variants) {
  const rows = tryParseRows(v);
  if (rows && (!best || rows.length > best.length)) best = rows;
}

if (!best) { console.error('fail'); process.exit(1); }
console.log('clean rows', best.length);
fs.writeFileSync(path.join(dir, 'aa_benchmark_rows.json'), JSON.stringify(best, null, 2));

const flat = best.map(r => {
  const comps = {};
  for (const e of (r.evals || [])) {
    comps[e.evaluationDatasetSlug || e.datasetIndexName] = e.mean?.reward;
  }
  return {
    id: r.id,
    label: r.displayLabel || `${r.agentName} - ${r.display?.model}`,
    agent: r.display?.agent || r.agentName,
    model: r.display?.model,
    indexPct: +(r.indexScore * 100).toFixed(2),
    costUsd: r.mean?.costUsd,
    wallTimeSec: r.mean?.agentWallTimeSec,
    comps,
  };
}).sort((a,b) => b.indexPct - a.indexPct);

fs.writeFileSync(path.join(dir, 'aa_cohort_flat.json'), JSON.stringify(flat, null, 2));
flat.forEach((r,i) => console.log(String(i+1).padStart(2), r.indexPct.toFixed(1).padStart(5), ('$'+Number(r.costUsd).toFixed(3)).padStart(8), r.label));
console.log('agents', [...new Set(flat.map(r => r.agent))]);
