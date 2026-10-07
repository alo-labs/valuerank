// Read-only bounded schema and consistency inspection for the MiMo correction.
const fs = require('fs');
const path = require('path');
const root = '/Users/shafqat/valuerank';
try {
  const load = p => JSON.parse(fs.readFileSync(path.join(root, p), 'utf8'));
  if (process.argv[2] === 'schemas') {
    const bug = load('.refresh/v1.4/bug_hunt.json');
    const tb = load('.refresh/v1.4/tb4.json');
    console.log('SCHEMAS ' + JSON.stringify({
      refreshFiles: fs.readdirSync(path.join(root, '.refresh/v1.4')).filter(n => /external|bug|tb4|livebench|capture/.test(n)),
      unmatchedBugSample: bug.models.find(x => x.matched !== true),
      tbKeys: Object.keys(tb),
      snapshotCapture: load('.refresh/v1.4/aa/aa_v432_snapshot.json').pages[0].capture,
    }));
  } else if (process.argv[2] === 'roster') {
    const mapping = load('.refresh/v1.4/aa_mapping.json');
    const extract = load('.refresh/v1.4/aa/aa_extract.json');
    const snapshots = load('.refresh/v1.4/aa/aa_v432_snapshot.json').pages;
    const bug = load('.refresh/v1.4/bug_hunt.json');
    const tb = load('.refresh/v1.4/tb4.json');
    const ids = new Set(mapping.map(x => x.id));
    console.log('ROSTER ' + JSON.stringify({
      rosterN: mapping.length,
      extractN: extract.length,
      duplicateMappingIds: mapping.length - ids.size,
      extractMissingIds: mapping.filter(x => !extract.some(e => e.id === x.id)).map(x => x.id),
      mimo: mapping.filter(x => x.id.startsWith('mimo-')).map(x => {
        const source = snapshots.find(e => e.id === x.id);
        const bugHunt = bug.models.find(e => e.modelId === x.id);
        return {
          ...x, extract: extract.find(e => e.id === x.id),
          source: source ? {url: source.url, capture: source.capture, intelligenceIndex: source.model?.intelligenceIndex, aaEvalCost: source.model?.aaEvalCost ?? source.model?.intelligenceIndexCost?.total} : null,
          bugHunt: bugHunt ? {matched: bugHunt.matched, status: bugHunt.matchStatus, score: bugHunt.fixedOf105, sampleN: bugHunt.sampleN, effort: bugHunt.effort, configurationsN: bugHunt.availableOwnerConfigurations?.length} : null,
          terminalBench4: tb.cohortRows[x.id] ?? null,
        };
      }),
    }));
  } else if (process.argv[2] === 'emitter') {
    const lines = fs.readFileSync(path.join(root, '.refresh/v1.4/emit_v14_docs.py'), 'utf8').split('\n');
    const indexes = new Set();
    lines.forEach((line, i) => {
      if (/availableOwnerConfigurations|owner result|matched Bug Hunt|reasoning_variant_unverified|No official result|owner missing/i.test(line)) {
        for (let j = Math.max(0, i - 2); j <= Math.min(lines.length - 1, i + 2); j++) indexes.add(j);
      }
    });
    console.log([...indexes].sort((a,b) => a-b).map(i => `${i+1}: ${lines[i]}`).join('\n'));
  } else if (process.argv[2] === 'livebench-delta') {
    const models = load('.refresh/v1.4/aa_metrics.json').models;
    const source = fs.readFileSync(path.join(root, '.refresh/v1.4/fetch_livebench.py'), 'utf8');
    const block = source.match(/COHORT_MAP = \{([\s\S]*?)\n\}/)?.[1] ?? '';
    const mappingIds = [...block.matchAll(/^\s*"([^"]+)":/gm)].map(m => m[1]);
    const snapshot = load('.refresh/v1.4/livebench.json');
    console.log('LIVEBENCH_DELTA ' + JSON.stringify({
      aaN: Object.keys(models).length, mappingN: mappingIds.length,
      missingMappingIds: Object.keys(models).filter(id => !mappingIds.includes(id)),
      extraMappingIds: mappingIds.filter(id => !(id in models)),
      retainedSnapshotMatchesForMissing: Object.keys(models).filter(id => !mappingIds.includes(id)).map(id => ({id, row:snapshot.models?.[id]})),
    }));
  }
} catch (error) {
  console.error(error.message);
  process.exitCode = 1;
}
