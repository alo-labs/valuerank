// Read-only inspection of the explicitly authorized Silver Bullet workflow.
const fs = require('fs');
const root = '/Users/shafqat/projects/silver-bullet/repo/skills/silver-deep-research';
try {
  if (process.argv[2] === 'packaging') {
    const dir='/Users/shafqat/valuerank/research/2026-10-07-user-reported-allowances-ultradeep';
    const manifest=JSON.parse(fs.readFileSync(dir+'/run_manifest.json','utf8'));
    const roll=JSON.parse(fs.readFileSync(dir+'/vloop-rollup.json','utf8'));
    const required=['input_contract','work_product','evidence_refs','verification','validation','repair','status'];
    console.log(JSON.stringify({manifestStatus:manifest.status,execution:manifest.execution,rollupStatus:roll.status,counts:roll.artifact_counts,phaseCount:roll.phases?.length,phases:roll.phases?.map(p=>({phase:p.phase,status:p.status,missing:required.filter(k=>!(k in p))})),stale: ['decision-record.md','handoff.md','critique.md','outline.md'].flatMap(f=>fs.readFileSync(dir+'/'+f,'utf8').split(/\r?\n/).filter(l=>/nine.row|9 rows|awaiting.final|not invoke|no qualifying OpenAI|two non.Anthropic/.test(l)).map(l=>({file:f,text:l})))}));process.exit(0);
  }
  if (process.argv[2] === 'quality-contract') {
    for(const file of ['SKILL.md','reference/quality-gates.md']) {
      const lines=fs.readFileSync(root+'/'+file,'utf8').split(/\r?\n/);
      console.log(JSON.stringify({file,matches:lines.map((s,i)=>({line:i+1,text:s})).filter(r=>/minimum|threshold|saturat|sources|ultradeep|critique/i.test(r.text)).slice(0,55)}));
    }process.exit(0);
  }
  if (process.argv[2] === 'roster-summary') {
    const ranking=JSON.parse(fs.readFileSync('/Users/shafqat/valuerank/.refresh/v1.4/ranking_summary.json','utf8'));
    const csv=fs.readFileSync('/Users/shafqat/valuerank/research/2026-10-06-value-multiples/roster-coverage/model-coverage.csv','utf8').trim().split(/\r?\n/);
    console.log(JSON.stringify({version:ranking.version,cohortN:ranking.cohortN,excluded:ranking.rankingExcludedModels,ranking:ranking.bugHuntEmphasisRanking?.ranking?.map(r=>({id:r.modelId,name:r.name})),coverage:csv.slice(1).map(l=>l.split(',').slice(0,4))},null,2));process.exit(0);
  }
  if (process.argv[2] === 'roster-files') {
    const path=require('path'); const found=[];
    function walk(p,d){if(d>4)return;for(const e of fs.readdirSync(p,{withFileTypes:true})){if(['.git','node_modules','.graphify'].includes(e.name))continue;const f=path.join(p,e.name);if(e.isDirectory())walk(f,d+1);else if(/ranking|coverage|models|roster/i.test(e.name)&&/json|csv|md$/.test(e.name))found.push(f);}}
    walk('/Users/shafqat/valuerank',0);console.log(found.slice(0,50));process.exit(0);
  }
  if (process.argv[2] === 'scores') {
    const rows=fs.readFileSync('/Users/shafqat/valuerank/subagent-model-scores.csv','utf8').trim().split(/\r?\n/).slice(1).map(l=>l.split(',')).filter(r=>r[1]==='gpt-6.1-sol'&&r[2]==='low');
    const first=rows.slice(0,10); console.log(JSON.stringify({runs:rows.length,firstTenMean:first.reduce((s,r)=>s+Number(r[3]),0)/first.length}));process.exit(0);
  }
  if (process.argv[2] === 'consistency') {
    const dir='/Users/shafqat/valuerank/research/2026-10-07-user-reported-allowances-ultradeep';
    const read=name=>JSON.parse(fs.readFileSync(`${dir}/${name}`,'utf8'));
    const claims=fs.readFileSync(`${dir}/claims.jsonl`,'utf8').trim().split(/\r?\n/).map(JSON.parse);
    const sources=fs.readFileSync(`${dir}/sources.jsonl`,'utf8').trim().split(/\r?\n/).map(JSON.parse);
    const evidence=fs.readFileSync(`${dir}/evidence.jsonl`,'utf8').trim().split(/\r?\n/).map(JSON.parse);
    const table=fs.readFileSync('/Users/shafqat/valuerank/research/2026-10-07-provider-wise-user-reported-value-multiples.md','utf8');
    const rows=table.split(/\r?\n/).filter(l=>l.startsWith('| ')&&!l.startsWith('| Provider'));
    const expected=[2350*52/12/200,(529.57/.26)*52/12/200,469*52/12/100,88*52/12/20,353*52/12/100,1464*52/12/200,45.25*52/12/30,400.5*52/12/300,102.17/18,(7.2/.2)*52/12/39];
    const sourceIds=new Set(sources.map(r=>r.source_id)), evIds=new Set(evidence.map(r=>r.evidence_id));
    const missing=claims.flatMap(c=>[...(c.cited_source_ids||[]).filter(id=>!sourceIds.has(id)),...(c.evidence_ids||[]).filter(id=>!evIds.has(id))]);
    const roll=read('vloop-rollup.json');
    const duplicateIds=items=>items.filter((v,i)=>items.indexOf(v)!==i);
    console.log(JSON.stringify({rows:rows.length,columns:rows.map(r=>r.split('|').length-2),claims:claims.length,sources:sources.length,evidence:evidence.length,missingRefs:missing,duplicateSourceIds:duplicateIds(sources.map(r=>r.source_id)),duplicateClaimIds:duplicateIds(claims.map(r=>r.claim_id)),arithmetic:expected,rollupKeys:Object.keys(roll),support:claims.map(c=>({id:c.claim_id,value:c.value_multiple,status:c.support_status}))}));
    process.exit(0);
  }
  if (process.argv[2] === 'claim-schema') {
    const dir = '/Users/shafqat/valuerank/research/2026-10-07-user-reported-allowances-ultradeep';
    const rows = fs.readFileSync(`${dir}/claims.jsonl`, 'utf8').trim().split(/\r?\n/).map(JSON.parse);
    console.log(JSON.stringify(rows.map(r=>({id:r.claim_id,type:r.claim_type,text:r.text,status:r.support_status}))));
    const code=fs.readFileSync(root+'/scripts/verify_claim_support.py','utf8').split(/\r?\n/);
    console.log(code.map((s,i)=>({s,i:i+1})).filter(r=>/claim_type|factual/.test(r.s)));
    process.exit(0);
  }
  if (process.argv[2] === 'ledgers') {
    const dir = '/Users/shafqat/valuerank/research/2026-10-07-user-reported-allowances-ultradeep';
    for (const name of ['sources', 'evidence', 'claims']) {
      const rows = fs.readFileSync(`${dir}/${name}.jsonl`, 'utf8').trim().split(/\r?\n/).map(JSON.parse);
      console.log(JSON.stringify({name, count:rows.length, fields:Object.keys(rows[0] || {}), rows:name === 'evidence' ? rows : undefined}));
    }
    console.log(JSON.stringify({OpenAI:{Plus:88*52/12/20,Pro5x:353*52/12/100,Pro20x:1464*52/12/200},GrokSuperGrok:45.25*52/12/30}));
    process.exit(0);
  }
  const lines = fs.readFileSync(root + '/scripts/verify_claim_support.py', 'utf8').split(/\r?\n/);
  console.log(lines.slice(430, 505).map((s, i) => `${i + 431}: ${s}`).join('\n'));
} catch (e) { console.error(e.message); process.exitCode = 1; }
