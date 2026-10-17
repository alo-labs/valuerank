// Read-only local evidence inspection; no HTTP or filesystem mutations.
const fs=require('fs');
try {
  if(process.argv[2]==='skills') {
    for(const p of ['/Users/shafqat/.agents/skills/graphify/SKILL.md','/Users/shafqat/projects/silver-bullet/repo/skills/silver-deep-research/SKILL.md']) {
      console.log('SKILL '+p+'\n'+fs.readFileSync(p,'utf8'));
    }
  }
  if(process.argv[2]==='sb') console.log(fs.readFileSync('/Users/shafqat/projects/silver-bullet/repo/skills/silver-deep-research/SKILL.md','utf8'));
  if(process.argv[2]==='search-probe') {
    const cp=require('child_process'); const r=cp.spawnSync('which',['search'],{encoding:'utf8'});console.log(JSON.stringify({available:r.status===0,path:(r.stdout||'').trim(),exit:r.status}));
  }
  if(process.argv[2]==='retrieval') console.log(fs.readFileSync('/Users/shafqat/valuerank/research/2026-10-07-mimo-investigation/retrieval/user-measurements.md','utf8').split('\n').filter(l=>/https|query|Query|fee|plan tier/i.test(l)).join('\n'));
  if(process.argv[2]==='csv') console.log(fs.readFileSync('/Users/shafqat/valuerank/subagent-model-scores.csv','utf8').split('\n').slice(-7).join('\n'));
  if(process.argv[2]==='arithmetic') {
    const parts={cache:67848448*.0036/1e6,input:4479135*.435/1e6,output:1388760*.87/1e6};
    const total=Object.values(parts).reduce((a,b)=>a+b,0); console.log(JSON.stringify({parts,total,partialRegularFeeRatio:total/6,usedCreditFraction:2190625116/4100000000,excludedProjection:total/(2190625116/4100000000)/6,tokenSum:67848448+4479135+1388760}));
  }
  if(process.argv[2]==='package') {
    const root='/Users/shafqat/valuerank/research/2026-10-07-mimo-investigation/allowance-ultradeep/';
    console.log(fs.existsSync(root)?fs.readdirSync(root).join(', '):'not present');
    for(const name of ['run_manifest.json','vloop-rollup.json','claims.jsonl','research_report.md','critique.md']) {
      if(!fs.existsSync(root+name)) continue;
      const s=fs.readFileSync(root+name,'utf8');console.log(name+'\n'+s.slice(0,process.argv[3]==='full'?16000:2500));
    }
  }
  if(process.argv[2]==='consistency') {
    const root='/Users/shafqat/valuerank/research/2026-10-07-mimo-investigation/allowance-ultradeep/';
    const parse=n=>fs.readFileSync(root+n+'.jsonl','utf8').trim().split('\n').filter(Boolean).map(JSON.parse);
    const sources=parse('sources'),evidence=parse('evidence'),claims=parse('claims');
    const sid=new Set(sources.map(x=>x.source_id)),eid=new Set(evidence.map(x=>x.evidence_id));
    console.log(JSON.stringify({sources:sources.length,evidence:evidence.length,claims:claims.length,sourceIds:[...sid],duplicateSourceIds:sources.length-sid.size,duplicateEvidenceIds:evidence.length-eid.size,missingClaimSourceRefs:claims.flatMap(c=>(c.cited_source_ids||[]).filter(s=>!sid.has(s))),missingClaimEvidenceRefs:claims.flatMap(c=>(c.evidence_ids||[]).filter(e=>!eid.has(e))),partialClaims:claims.filter(c=>c.support_status!=='supported').map(c=>({id:c.claim_id,text:c.text,status:c.support_status})),reportWords:fs.readFileSync(root+'research_report.md','utf8').split(/\s+/).length,phases:JSON.parse(fs.readFileSync(root+'vloop-rollup.json','utf8')).phases.map(p=>({phase:p.phase,status:p.status,missing:['input_contract','work_product','evidence_refs','verification','validation','repair','status'].filter(k=>!(k in p))}))}));
  }
  if(process.argv[2]==='audit') {
    for(const p of ['omission-audit.md','retrieval/chinese-user-measurements.md']) console.log(p+'\n'+fs.readFileSync('/Users/shafqat/valuerank/research/2026-10-07-mimo-investigation/'+p,'utf8'));
  }
  if(process.argv[2]==='verify-code') {
    const base='/Users/shafqat/valuerank/';
    for(const [p,a,b] of [['package.json',9,17],['.refresh/v1.4/capture_aa_v432.py',45,54],['.refresh/v1.4/build_aa_metrics.py',165,184],['.refresh/v1.4/build_scores.py',267,278],['.refresh/v1.4/build_scores.py',337,345],['.refresh/v1.4/build_scores.py',452,484]]) console.log(p+'\n'+fs.readFileSync(base+p,'utf8').split('\n').slice(a-1,b).map((l,i)=>(a+i)+': '+l).join('\n'));
    for(const p of ['.refresh/v1.4/aa_mapping.json','.refresh/v1.4/aa/aa_extract.json','.refresh/v1.4/aa_metrics.json']) {
      const d=JSON.parse(fs.readFileSync(base+p,'utf8')); console.log(p+' '+JSON.stringify({keys:Object.keys(d),mimoMatches:JSON.stringify(d).match(/mimo|xiaomi/gi)}));
    }
  }
}catch(e){console.error(e.message);process.exitCode=1;}
