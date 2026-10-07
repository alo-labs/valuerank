const fs=require('fs'),path=require('path');const root='/Users/shafqat/valuerank';
try {
 const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
 const scores=read('.refresh/v1.4/scores.json'), ranked=scores.models.filter(x=>x.rankingEligible);
 console.log(JSON.stringify({version:scores.version,rankedN:ranked.length,sourceN:scores.models.length,required:scores.frontierSelection?.selectedFamilyModelIds?.map(x=>x.modelId),weights:scores.weights.map(x=>({key:x.key,priority:x.priority})),models:ranked.filter(x=>['gpt-6.1-sol','gpt-6-luna','claude-opus-5-5','mimo-v2-6-pro','mimo-v2-6-flash'].includes(x.id)).map(x=>({id:x.id,rank:x.rank,score:x.overallScore,quality:x.qualityScore,coverage:x.metricCoverage,cost:x.aaEvalCost}))}));
 const doc=fs.readFileSync(path.join(root,'site/index.html'),'utf8');const m=doc.match(/const MODELS = ([\s\S]*?);\n/);
 if(m){const rows=JSON.parse(m[1]);console.log('site',JSON.stringify({n:rows.length,required:rows.filter(x=>/MiMo|6\.1 Sol|6 Luna|Opus 5\.5/.test(x.name)).map(x=>({name:x.name,rank:x.rank,cost:x.apiCost,planCost:x.planCost,multiple:x.planRoute?.valueMultiple,coverage:x.metricCoverage})),nullMetricRows:rows.filter(x=>x.dims.some(v=>v===null)).length}));}
 for(const name of ['README.md','scores.md','methodology.md','raw-data.md']){const lines=fs.readFileSync(path.join(root,name),'utf8').split('\n');let cols=null,bad=[];for(let i=0;i<lines.length;i++){if(lines[i].startsWith('|')){const n=lines[i].split('|').length;if(cols===null)cols=n;else if(n!==cols)bad.push(i+1);}else cols=null;}console.log(name,'tableColumnMismatches',bad);}
 const rec=read('.refresh/v1.4/aa_reconciliation_report.json');console.log('reconciliation',JSON.stringify({status:rec.status,issues:rec.issues,required:rec.requiredFamilies,metricGaps:rec.metricGaps}));
}catch(e){console.log(e.stack);process.exitCode=1;}
