// Read-only local processing; no network or writes.
const fs=require('fs'),path=require('path');
try {
 const root='/Users/shafqat/valuerank';
 if(process.argv[2]==='final') {
  const lock=JSON.parse(fs.readFileSync(path.join(root,'package-lock.json'),'utf8'));console.log('lock versions '+JSON.stringify({version:lock.version,root:lock.packages?.['']?.version}));
  for(const p of ['package-lock.json','research/2026-10-08-mimo-correction']) console.log(p+': '+(fs.existsSync(path.join(root,p))?(fs.statSync(path.join(root,p)).isDirectory()?fs.readdirSync(path.join(root,p)).join(', '):'exists'):'absent'));
  const ls=fs.readFileSync(path.join(root,'subagent-model-scores.csv'),'utf8').trim().split('\n');console.log('CSV last rows\n'+ls.slice(-8).join('\n'));
  for(const p of ['.refresh/v1.4/aa_reconciliation.py','.refresh/v1.4/capture_aa_v432.py','.refresh/v1.4/build_scores.py']) {const ls=fs.readFileSync(path.join(root,p),'utf8').split('\n');const hits=new Set();ls.forEach((s,i)=>{if(/def variant|def .*match|def preserved_public|reasoning_variant_unverified|availableOwnerConfigurations/.test(s))for(let j=Math.max(0,i-3);j<Math.min(ls.length,i+50);j++)hits.add(j)});console.log(p+'\n'+[...hits].map(i=>(i+1)+': '+ls[i]).join('\n'));}
 }
 if(process.argv[2]==='files') {
  for(const d of ['.github/workflows','scripts','.vercel']) if(fs.existsSync(path.join(root,d))) console.log(d+': '+fs.readdirSync(path.join(root,d)).join(', '));
 }
 if(process.argv[2]==='memory') {
  const p='/Users/shafqat/.codex/memories/MEMORY.md'; const ls=fs.readFileSync(p,'utf8').split('\n');console.log(ls.map((s,i)=>({s,i})).filter(x=>/valuerank|publication|deploy/i.test(x.s)).map(x=>(x.i+1)+': '+x.s).slice(0,20).join('\n'));
 }
 if(process.argv[2]==='read') for(const p of process.argv.slice(3)) console.log(p+'\n'+fs.readFileSync(path.join(root,p),'utf8').slice(0,9000));
 if(process.argv[2]==='tail') for(const p of process.argv.slice(3)) console.log(p+'\n'+fs.readFileSync(path.join(root,p),'utf8').slice(-6500));
 if(process.argv[2]==='outputs') {
  for(const p of ['aa_metrics.json','livebench.json','ranking_summary.json','coverage_matrix.json','aa_reconciliation_report.json']) {
   const f=path.join(root,'.refresh/v1.4',p);if(!fs.existsSync(f)){console.log(p+':missing');continue;}
   const j=JSON.parse(fs.readFileSync(f,'utf8'));const m=j.models;console.log(p+' '+JSON.stringify({keys:Object.keys(j),modelN:m?Object.keys(m).length:null,mimo:m?Object.entries(m).filter(([k,v])=>/mimo/.test(k)||/mimo/.test(v.modelId||'')).map(([k,v])=>({id:k,record:v})):null,cohort:j.cohortN,sourceN:j.sourceCohortN,missing:j.missingFrontierIds,unresolved:j.unresolvedFrontierIds,errors:j.errors}));
  }
 }
 if(process.argv[2]==='identities') {
  const j=JSON.parse(fs.readFileSync(path.join(root,'.refresh/v1.4/aa_metrics.json'),'utf8'));
  console.log(Object.entries(j.models).filter(([k,v])=>/gpt-6|opus-5|mimo/.test(k)).map(([id,v])=>({id,name:v.aaName,short:v.aaShortName,slug:v.aaSlug,variant:v.aaVariant,reasoning:v.isReasoning})));
 }
 if(process.argv[2]==='review') {
  const load=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
  const scores=load('.refresh/v1.4/scores.json');const old=JSON.parse(require('child_process').execFileSync('git',['show','HEAD:.refresh/v1.4/scores.json'],{cwd:root,encoding:'utf8'}));
  const ranked=scores.models.filter(m=>m.rankingEligible);const changed=ranked.filter(m=>{let before=old.models.find(x=>x.id===m.id);return !before||before.rank!==m.rank||before.overallScore!==m.overallScore});
  const rec=load('.refresh/v1.4/aa_reconciliation_report.json');
  console.log(JSON.stringify({version:scores.version,sourceN:scores.models.length,rankedN:ranked.length,changedExistingRanks:changed.map(x=>x.id),mimo:scores.models.filter(m=>m.id.startsWith('mimo')).map(m=>({id:m.id,rank:m.rank,eligible:m.rankingEligible,cost:m.aaEvalCost,briefcase:m.briefcaseElo,gdp:m.gdpvalV21,deepSWE:m.deepswePassAt1Pct,reasons:m.rankingExclusionReasons})),reconciliation:{status:rec.status,issues:rec.issues,missing:rec.missingFrontierIds,deferred:rec.deferredFrontierIds,unresolved:rec.unresolvedFrontierIds},siteMarkers:['v1.9.4','MiMo-V2.6-Pro','MiMo-V2.6-Flash','23.3','AA frontier'].map(v=>({v,present:fs.readFileSync(path.join(root,'site/index.html'),'utf8').includes(v)}))},null,2));
 }
} catch(e) {console.error(e.message);process.exitCode=1;}
