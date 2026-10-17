// Read-only arithmetic and artifact-consistency inspection.
const fs=require('fs');
try {
  const root='/Users/shafqat/valuerank/research';
  const note=fs.readFileSync(root+'/2026-10-07-semianalysis-subscription-update.md','utf8');
  const measured=note.split(/\r?\n/).filter(l=>/^\| (Anthropic|OpenAI) \|/.test(l)).map(l=>{
    const c=l.split('|').slice(1,-1).map(v=>v.trim());
    const fee=Number(c[1].match(/\$([\d,]+)/)?.[1]?.replaceAll(',',''));
    const value=Number(c[3].replace(/[^\d.]/g,''));
    const multiple=Number(c[4].replace(/[^\d.]/g,''));
    return {provider:c[0],plan:c[1],model:c[2],value,fee,derived:value/fee,printed:multiple,matches:Math.abs(value/fee-multiple)<0.00001};
  });
  const table=fs.readFileSync(root+'/2026-10-07-provider-wise-user-reported-value-multiples.md','utf8');
  const rows=table.split(/\r?\n/).filter(l=>l.startsWith('| ')&&!l.startsWith('| Provider'));
  const index=fs.readFileSync(root+'/2026-10-07-allowance-research-index.md','utf8');
  console.log(JSON.stringify({observations:measured.length,allArithmeticMatches:measured.every(r=>r.matches),values:measured,tableRows:rows.length,columns:rows.map(l=>l.split('|').length-2),providers:rows.map(l=>l.split('|')[1].trim()),semiRows:rows.filter(l=>/SemiAnalysis|semianalysis/.test(l)).length,policyMentionsSemi:index.includes('SemiAnalysis'),newReportLinked:index.includes('2026-10-07-semianalysis-subscription-update.md')}));
}catch(e){console.error(e.message);process.exitCode=1;}
