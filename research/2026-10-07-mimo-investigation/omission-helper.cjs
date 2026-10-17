const fs = require('fs');
const path = require('path');
const cp = require('child_process');
const root = '/Users/shafqat/valuerank';
function lines(p, regex, before=0, after=0) {
  const rows=fs.readFileSync(path.join(root,p),'utf8').split('\n');
  let selected=new Set(); rows.forEach((s,i)=>{if(regex.test(s)){for(let j=Math.max(0,i-before);j<=Math.min(rows.length-1,i+after);j++)selected.add(j);}});
  console.log(p); [...selected].forEach(i=>console.log(`${i+1}: ${rows[i]}`));
}
const mode=process.argv[2];
if(mode==='origin'){
 const files=cp.execFileSync('rg',['--files','--hidden','-g','!node_modules','-g','!.git','-g','!graphify-out'],{cwd:root,encoding:'utf8'}).trim().split('\n').filter(p=>/^\.refresh\/.*\.(py|js|cjs)$|^scripts\/.*\.(py|js|cjs)$/.test(p));
 const matches=[];for(const p of files){const rows=fs.readFileSync(path.join(root,p),'utf8').split('\n');rows.forEach((s,i)=>{if(/aa_extract\.json|aa_mapping\.json/.test(s))matches.push(`${p}:${i+1}: ${s}`)});}console.log(matches.join('\n'));
}else if(mode==='brief'){
 for(const dir of ['.refresh/v1.4','scripts']) console.log(dir+' '+fs.readdirSync(path.join(root,dir)).filter(p=>/aa|cohort|rank|fetch|build|config|refresh/i.test(p)).join(' '));
 const p='.refresh/v1.4/ranking_summary.json'; const j=JSON.parse(fs.readFileSync(path.join(root,p),'utf8')); console.log('SUMMARY KEYS '+Object.keys(j)); for(const [k,v]of Object.entries(j))console.log(k+' '+JSON.stringify(v).slice(0,1800));
} else if(mode==='inventory'){
  const files=cp.execFileSync('rg',['--files','--hidden','-g','!node_modules','-g','!.git','-g','!graphify-out'],{cwd:root,encoding:'utf8'}).trim().split('\n');
  console.log(files.filter(p=>/\.refresh\/|scripts\//.test(p)&&/aa|cohort|rank|refresh|config|fetch|build/i.test(p)).join('\n'));
  for(const p of files.filter(p=>/\.refresh\/.*\.(py|json)$|package\.json$|methodology\.md$/.test(p))){try{lines(p,/mimo|cohort|exclude|pareto|MODEL_IDS|MODELS|aa_models/i,0,0)}catch{}}
} else if(mode==='json'){
 for(const p of process.argv.slice(3)){const j=JSON.parse(fs.readFileSync(path.join(root,p),'utf8')); console.log(p+' keys='+Object.keys(j));if(Array.isArray(j)){console.log('n='+j.length+' roster='+j.map(x=>x.displayName||x.name||x.id).join(', '));console.log('mimo='+JSON.stringify(j.filter(x=>/mimo|xiaomi/i.test(JSON.stringify(x)))));}else{console.log('metadata='+JSON.stringify(Object.fromEntries(Object.entries(j).filter(([k,v])=>!['models','pages','rows','weights','coverage'].includes(k)))).slice(0,1700)); for(const k of ['models','pages','rows'])if(j[k])console.log(k+'='+JSON.stringify(Array.isArray(j[k])?j[k].map(x=>x.displayName||x.name||x.id):Object.keys(j[k]))); console.log('mimo='+JSON.stringify(Object.entries(j).filter(([k,v])=>/mimo|xiaomi/i.test(JSON.stringify(v)))).slice(0,900));}}
} else if(mode==='window'){
 const p=process.argv[3], rows=fs.readFileSync(path.join(root,p),'utf8').split('\n'); console.log(p); console.log(rows.slice(Number(process.argv[4])-1,Number(process.argv[5])).map((s,i)=>`${i+Number(process.argv[4])}: ${s}`).join('\n'));
} else if(mode==='hits'){
 const p=process.argv[3];const rows=fs.readFileSync(path.join(root,p),'utf8').split('\n'); const re=new RegExp(process.argv[4],'i');console.log(p);console.log(rows.map((s,i)=>({s,i})).filter(x=>re.test(x.s)).map(x=>`${x.i+1}: ${x.s}`).slice(Number(process.argv[5]||0),Number(process.argv[5]||0)+18).join('\n'));
} else if(mode==='focus'){
 lines(process.argv[3],new RegExp(process.argv[4],'i'),Number(process.argv[5]||0),Number(process.argv[6]||0));
} else if(mode==='read') {
  for(const p of process.argv.slice(3)){lines(p,/./,0,0);}
} else if(mode==='search'){
  const files=cp.execFileSync('rg',['--files','--hidden','-g','!node_modules','-g','!.git','-g','!graphify-out'],{cwd:root,encoding:'utf8'}).trim().split('\n');
  for(const p of files.filter(p=>/\.refresh\/.*\.(py|json|js|md)$|scripts\/.*\.(py|js|cjs|json)$/.test(p))){try{lines(p,new RegExp(process.argv[3],'i'),2,3)}catch{}}
}
