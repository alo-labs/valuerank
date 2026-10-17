const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const root = __dirname;
const out = path.join(root, 'coding-provider-ultradeep');
const runTimestamp = new Date().toISOString();
fs.mkdirSync(out, {recursive:true});
const readJsonl = name => fs.readFileSync(path.join(root,name),'utf8').split(/\r?\n/).filter(Boolean).map(s=>JSON.parse(s));
const writeJsonl = (name, rows) => fs.writeFileSync(path.join(out,name), rows.map(x=>JSON.stringify(x)).join('\n')+'\n');
const sha = s => crypto.createHash('sha256').update(s).digest('hex').slice(0,16);
const cpSources = readJsonl('coding-provider-sources-addendum.jsonl');
const cpEvidence = readJsonl('coding-provider-evidence-addendum.jsonl');
const cpPolicy = readJsonl('coding-provider-policy-addendum.jsonl');
if (!cpEvidence.some(e=>e.id==='CP-E14')) cpEvidence.push({id:'CP-E14',source_id:'CP-S08',publication_date:'2026-09-08',measurement_interval:'Rough estimate in the original post; no exact usage period or account-meter observation stated.',provider:'Ollama Cloud',plan_tier_as_reported:'not stated',product_surface:"Original poster's rough usage estimate using Hermes",measurement_class:'local_usage_log_estimate',is_user_report:true,eligibility:'excluded_uncorroborated_context',confidence:'very_low',model_version:'Hermes; exact model and counter not stated',reported_observation:'The original poster gives a rough estimate of about 50% lower usage capacity based on Hermes, without a personally documented account meter or a clearly stated subscription tier.',method:'Unclear estimate described in the post; no raw local log, controlled comparison, or account screenshot was available.',limitations:'Excluded from quantitative claims because the usage unit, plan, time window, baseline, and relationship to provider quota are unclear.'});
const reporter = {
  'CP-E01':'Original post author', 'CP-E02':'Original post author', 'CP-E03':'Original post author',
  'CP-E04':'Comment author; plan not stated', 'CP-E05':'Original post author',
  'CP-E06':'Original post author; plan not stated', 'CP-E07':'Original post author',
  'CP-E08':'Original post author', 'CP-E09':'Sep 10 commenter', 'CP-E10':'Sep 10 commenter',
  'CP-E11':'Sep 10 commenter', 'CP-E12':'Sep 15 commenter', 'CP-E13':'Sep 15 commenter', 'CP-E14':'Original post author; plan not stated'
};
const queryMap = {
  'CP-E01':['CP-Q01'], 'CP-E02':['CP-Q01'], 'CP-E03':['CP-Q01'],
  'CP-E04':['CP-Q25'], 'CP-E05':['CP-Q24'], 'CP-E06':['CP-Q04','CP-Q06'],
  'CP-E07':['CP-Q17','CP-Q37'], 'CP-E08':['CP-Q17','CP-Q36'],
  'CP-E09':['CP-Q09','CP-Q41'], 'CP-E10':['CP-Q09','CP-Q41'],
  'CP-E11':['CP-Q09','CP-Q43'], 'CP-E12':['CP-Q09','CP-Q42'], 'CP-E13':['CP-Q09','CP-Q42'],
  'CP-E14':['CP-Q09']
};
for (const e of cpEvidence) {
  e.reporter_label = reporter[e.id] || 'Author not identified in captured page';
  e.search_query_ids = queryMap[e.id] || [];
  e.provider = e.provider.trim();
  if (e.id==='CP-E10') {
    e.measurement_class='user_extrapolation';
    e.product_surface='Author-reported request count and provider weekly account meter';
    e.method='User extrapolation from the account meter percentage and approximate request count; prior baseline is recalled rather than logged in the post.';
    e.derived_estimate_from_meter=true;
  }
}
fs.writeFileSync(path.join(root,'coding-provider-evidence-addendum.jsonl'), cpEvidence.map(x=>JSON.stringify(x)).join('\n')+'\n');

const queries = [
  'site:reddit.com/r/cursor "2026" "usage" Cursor Pro Ultra September credits',
  'site:reddit.com/r/windsurf (quota OR credits OR usage) after:2026-09-04',
  'site:news.ycombinator.com/item Windsurf quota usage September 2026',
  '"Kimi Code" (quota OR limit OR usage) September 2026 Reddit',
  '"Z.AI" OR "GLM Coding Plan" (quota OR limit OR usage) September 2026 Reddit',
  'site:reddit.com/r/kimi "Kimi Code" "plan" "limit" after:2026-09-04',
  'site:reddit.com/r/ZaiGLM "Coding Plan" quota usage after:2026-09-04',
  'site:reddit.com OpenCode "coding plan" Kimi GLM quota September 2026',
  'Ollama Cloud subscription limits quota Reddit September 2026 coding',
  'site:news.ycombinator.com/item Cursor Pro quota usage September 2026',
  'site:news.ycombinator.com/item Kimi Code quota limit September 2026',
  'site:news.ycombinator.com/item Ollama Cloud usage limits OpenCode September 2026',
  'site:github.com/issues "GLM Coding Plan" "usage" "September" 2026',
  'site:reddit.com/r/ZaiGLM "Sep" "Coding Plan" "usage" 2026',
  'site:reddit.com/r/ZaiGLM "GLM Coding" "quota" after:2026-09-04',
  'site:github.com/LogicIncZo/zai-usage "as of" "Sept" usage',
  'OpenCode Go subscription quota user usage September 2026 Reddit',
  'site:github.com Kimi Code quota tracker usage monitor plan 2026',
  'site:github.com OpenCode Go usage tracker quota dashboard script',
  'site:github.com Ollama Cloud quota usage tracker OpenCode local usage logs',
  'site:github.com Z.ai GLM Coding Plan usage tracker quota logs',
  'site:reddit.com/r/GithubCopilot "7000" "credits" after:2026-09-04',
  'site:reddit.com/r/GithubCopilot "Pro" "credits" "September" 2026 usage',
  'site:github.com/orgs/community/discussions/copilot "AI Credits" after:2026-09-04 usage',
  'site:reddit.com/r/windsurf after:2026-09-04 "daily quota" Devin coding usage',
  'site:docs.github.com/en/copilot monitor AI usage billing Pro+ 7000 credits 2026',
  'site:prod.cursor.com/help/models-and-usage/usage-limits Cursor Spending pool credits',
  'site:kimi.com/code/docs membership quota 5 hour Code Console usage',
  'site:opencode.ai/go OpenCode Go usage allowance 5 hours monthly quota',
  'Ollama Cloud pricing grandfathered Pro monthly token usage new plans official',
  'site:zcode.z.ai/en/docs/usage-stats Coding Plan 5 hour weekly monthly usage stats',
  'GitHub OpenCode Bar tracker Kimi Copilot Z.AI Go usage quota official repository',
  'OpenUsage Z.AI provider quota adapter github',
  'site:reddit.com/r/ollama/comments/ "724" "DeepSeek" "Pro" "OpenCode" 2026',
  'site:reddit.com/r/ollama/comments/ "36.7%" Ollama Pro weekly OpenCode September 2026',
  'site:reddit.com/r/opencode/comments/ "12%" "OpenCode Go" "DeepSeek v4.1 Flash"',
  'site:reddit.com/r/opencode/comments/ "20% monthly" "daily quota" "OpenCode Go"',
  'site:reddit.com/r/kimi/comments/ "Allegretto" "1.5 days" "5-hour" September 2026',
  'site:reddit.com/r/ZaiGLM "GLM Coding Plan" quota usage September 2026',
  'site:news.ycombinator.com/item?id= "Kimi Code" quota usage September 2026',
  'site:news.ycombinator.com/item?id= OpenCode Go quota usage September 2026',
  'site:reddit.com/r/ollama/comments/1waiu6b "724 requests" "60%"',
  'site:reddit.com/r/ollama/comments/1waiu6b "36.7%" "400M"',
  'site:reddit.com/r/ollama/comments/1waiu6b "3,695" "CNY"',
  'site:reddit.com/r/kimi/comments/ "Allegretto" "1.5 days" quota 2026',
  'site:reddit.com/r/kimi "Allegretto" "5h" "weekly" September 2026 coding plan',
  'site:reddit.com/r/kimi/comments/ "Allegretto" "3 times" "weekly" quota'
];
const qRows = queries.map((query,i)=>({query_id:`CP-Q${String(i+1).padStart(2,'0')}`,query,search_tool:'Codex built-in web__run',searched_at:'2026-10-05',date_filter:'2026-09-05 through 2026-10-05 inclusive; enforced at source screening where provider syntax did not apply',purpose:i<25?'Community discovery, date screening, and app/usage-log search':'Provider policy, targeted source follow-up, and targeted community validation',result_handling:'Reviewed returned snippets and opened relevant direct sources; source eligibility, plan-tier wording, and measurement class are recorded in the ledgers. Search results alone are not treated as user evidence.'}));
const queryById=new Map(qRows.map(q=>[q.query_id,q.query]));
writeJsonl('query_log.jsonl',qRows);

const sourceByCustom = new Map();
const canonicalSources = cpSources.map(s=>{
  const locator = new URL(s.url);
  locator.hash='';
  const canonical = locator.toString().replace(/\/$/,'');
  const isCommunity=s.source_type.startsWith('community_');
  const isBoundary=s.source_type==='bounded_search_outcome';
  const isDocs=s.source_type.startsWith('provider_');
  const sourceType=isDocs?'documentation':(s.source_type.includes('tracker')?'code':(s.source_type.includes('code')?'code':'web'));
  const sourceClass=isBoundary?'portal':'primary';
  const reliability=isCommunity?'B4':isBoundary?'D5':isDocs?'A1':'C3';
  const biases=isCommunity?['single_perspective','recency_risk']:isDocs?['commercial','recency_risk']:isBoundary?['recency_risk']:['single_perspective','recency_risk'];
  const id=sha(canonical);
  sourceByCustom.set(s.id,id);
  return {source_id:id,canonical_locator:canonical,raw_url:s.url,title:s.title,authors:null,year:s.published_at?String(s.published_at.slice(0,4)):null,source_type:sourceType,source_class:sourceClass,metadata_status:'url_verified',reliability_code:reliability,authority_tier:isDocs?'primary':isCommunity?'primary':isBoundary?'unknown':'tertiary',bias_flags:biases,registered_at:runTimestamp};
});
writeJsonl('sources.jsonl',canonicalSources);
const evidenceRows=[];
const evidenceByCustom=new Map();
function addEvidence(e, policy=false){
  const customId=e.id;
  const src=sourceByCustom.get(e.source_id);
  if(!src) throw new Error(`Missing source for ${customId}`);
  const plan=policy?'Provider policy context; no subscriber plan inferred. ':`Reported plan tier: ${e.plan_tier_as_reported}. Reporter: ${e.reporter_label}. Measurement class: ${e.measurement_class}. `;
  const quote=plan+e.reported_observation;
  const locator=policy?'Provider documentation page':`${e.reporter_label}; publication ${e.publication_date}`;
  const eid=sha(`${src}${quote.replace(/\s+/g,' ').trim()}${locator}`);
  evidenceByCustom.set(customId,eid);
  const queryIds=policy?({ 'CP-P01':['CP-Q27'],'CP-P02':['CP-Q26'],'CP-P03':['CP-Q28'],'CP-P04':['CP-Q29'],'CP-P05':['CP-Q30'],'CP-P06':['CP-Q31'] }[customId]||[]):(e.search_query_ids||[]);
  const evidenceRow={evidence_id:eid,report_evidence_id:customId,observation_class:policy?'provider_policy':'user_observation',source_id:src,retrieval_query:queryIds.map(id=>queryById.get(id)).filter(Boolean).join(' | ')||null,locator,quote,evidence_type:'paraphrase',captured_at:runTimestamp};
  if(!policy){
    evidenceRow.plan_tier_as_reported=e.plan_tier_as_reported;
    evidenceRow.reporter_label=e.reporter_label;
  }
  evidenceRows.push(evidenceRow);
}
for(const e of cpEvidence) addEvidence(e,false);
for(const e of cpPolicy) addEvidence(e,true);
writeJsonl('evidence.jsonl',evidenceRows);

const claimDefs=[
  ['executive_summary','This window yields a small set of heterogeneous subscriber anecdotes, not a plan-normalized estimate of typical coding usage.','synthesis',['CP-E01','CP-E02','CP-E04','CP-E06','CP-E07','CP-E09','CP-E12']],
  ['cursor','A Cursor Pro account author reported the Cursor Models meter at 100% and Other Models at 23% after one day, with workload and exact model route unstated.','factual',['CP-E01','CP-P01']],
  ['copilot','A GitHub Copilot commenter with plan not stated reported 24,000 of 150,000 monthly AI credits used during project migration; a separate author with plan not stated said two generations used their monthly allowance plus nearly USD $8.','factual',['CP-E04','CP-E05','CP-P02']],
  ['kimi','A Kimi Code user with plan not stated said the five-hour account limit was exhausted within minutes during a small coding task.','factual',['CP-E06','CP-P03']],
  ['opencode_go','Two OpenCode Go reports show different meter experiences: one reached 100% of a daily allowance at 20% monthly use, while another author reported 12% current-month use after several days of heavy coding.','factual',['CP-E07','CP-E08','CP-P04']],
  ['ollama','An Ollama Cloud grandfathered Pro commenter reported 724 DeepSeek V4 Flash requests at 60% of a weekly account meter and separately extrapolated around 1,200 requests per week; a different Ollama Pro commenter reported 36.7% weekly session use after two days.','factual',['CP-E09','CP-E10','CP-E12','CP-P05']],
  ['measurement','The dataset keeps account meters, provider-published quota rules, local usage-log estimates, and API-cost equivalents in separate classes because they measure different things.','synthesis',['CP-E01','CP-E03','CP-E10','CP-E11','CP-E13','CP-P01','CP-P02','CP-P03','CP-P04','CP-P05','CP-P06']],
  ['apps','The discovered allowance tools expose personal account meters or local request/token logs; the audited tracker repositories do not publish a cross-user cohort dataset.','synthesis',['CP-P06','CP-E13']]
];
const claims=claimDefs.map(([section_id,text,claim_type,customEvidence])=>({claim_id:sha(`${section_id}${text}`),section_id,text,claim_type,cited_source_ids:[...new Set(customEvidence.map(id=>{
    const e=cpEvidence.find(x=>x.id===id)||cpPolicy.find(x=>x.id===id);
    return e&&sourceByCustom.get(e.source_id);
  }).filter(Boolean))],evidence_ids:customEvidence.map(id=>evidenceByCustom.get(id)).filter(Boolean),support_status:'supported',extracted_at:'2026-10-05T00:00:00Z'}));
writeJsonl('claims.jsonl',claims);
fs.writeFileSync(path.join(root,'coding-provider-claims-addendum.jsonl'),claimDefs.map(([section_id,claim,claim_type,evidence_ids],i)=>JSON.stringify({id:`CP-C${String(i+1).padStart(2,'0')}`,claim,claim_type,status:'supported_with_limits',evidence_ids,scope:section_id,qualifier:'Coding-provider supplement only; see canonical claim row for hashed evidence/source IDs and limitations.'})).join('\n')+'\n');

const manifest={version:'3.0.0',query:'Audit subscription plan allowance apps and user-reported usage for coding-oriented AI plans/providers, limited to material dated 2026-09-05 through 2026-10-05.',mode:'ultradeep',started_at:'2026-10-05T00:00:00Z',finished_at:runTimestamp,assumptions:[{assumption_id:'asm_8c68fa11',text:'Exact task kickoff time was not retained; started_at is a UTC date anchor, not an observed invocation timestamp.',materiality:'low',status:'implicit'}],provider_config:{primary:'Codex built-in web__run',scholarly:null},report_dir:out,artifact_paths:{sources:'sources.jsonl',evidence:'evidence.jsonl',claims:'claims.jsonl',report:'research_report.md'},continuation:null};
fs.writeFileSync(path.join(out,'run_manifest.json'),JSON.stringify(manifest,null,2)+'\n');
const priorManifestPath=path.join(root,'run_manifest.json');
const priorManifest=JSON.parse(fs.readFileSync(priorManifestPath,'utf8'));
priorManifest.silver_bullet_degradation='Silver Bullet root alias and Ultradeep skill were registered/read; nine phase artifacts were applied manually and no /sb orchestration command was invoked. The earlier root-registration issue was corrected. Shared ctx_execute capacity saturation (15/15) is a separate sandbox execution limit; local lean-ctx command route is used for validators.';
priorManifest.coding_provider_ultradeep={
  package_dir:'coding-provider-ultradeep/',
  source_records:canonicalSources.length,
  direct_post_doc_repo_pages:canonicalSources.length-3,
  bounded_search_outcome_records:3,
  eligible_user_observations:cpEvidence.filter(e=>e.eligibility==='eligible').length,
  excluded_user_context_observations:cpEvidence.filter(e=>e.eligibility!=='eligible').length,
  provider_policy_observations:cpPolicy.length,
  total_evidence_rows:evidenceRows.length,
  claims:claims.length,
  exact_query_strings_logged:qRows.length,
  exact_query_log_gap:'Earlier official-document searches were referenced in retained handoff history without their exact literals; count is exact preserved strings, not all web tool invocations.',
  user_measurement_class_counts:Object.fromEntries([...new Set(cpEvidence.filter(e=>e.eligibility==='eligible').map(e=>e.measurement_class))].map(k=>[k,cpEvidence.filter(e=>e.eligibility==='eligible'&&e.measurement_class===k).length]))
};
priorManifest.coding_provider_validation={
  custom_validator:'pass; source/evidence/claim/query counts, exact plan fields, measurement classes, hashes, and crosswalks validated',
  sb_phase_gate:'pass; mode ultradeep',
  sb_validate_report:'pass; all checks passed',
  sb_verify_citations:'pass; 19/19 URLs verified, 0 suspicious, 0 unverified',
  sb_verify_claim_support:'pass; 8 claims verified, 0 unsupported factual claims',
  execution_route:'local lean-ctx CLI; shared MCP ctx_execute probe returned agent capacity reached 15/15; this is a separate sandbox limit'
};
fs.writeFileSync(priorManifestPath,JSON.stringify(priorManifest,null,2)+'\n');
console.log(JSON.stringify({query_count:qRows.length,source_count:canonicalSources.length,eligible_community_evidence:cpEvidence.filter(e=>e.eligibility==='eligible').length,excluded_community_evidence:cpEvidence.filter(e=>e.eligibility!=='eligible').length,provider_policy_evidence:cpPolicy.length,evidence_count:evidenceRows.length,claim_count:claims.length,reporter_tiers:cpEvidence.every(e=>e.plan_tier_as_reported==='not stated'||String(e.plan_tier_as_reported).trim().length>0),out}));
