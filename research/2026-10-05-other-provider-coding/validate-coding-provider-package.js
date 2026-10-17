#!/usr/bin/env node
'use strict';

const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');

const root = __dirname;
const errors = [];
const readJson = (name) => JSON.parse(fs.readFileSync(path.join(root, name), 'utf8'));
const readJsonl = (name) => {
  const file = path.join(root, name);
  if (!fs.existsSync(file)) return [];
  const rows = [];
  for (const [index, line] of fs.readFileSync(file, 'utf8').split(/\r?\n/).entries()) {
    if (!line.trim()) continue;
    try {
      rows.push(JSON.parse(line));
    } catch (error) {
      errors.push(`${name}:${index + 1}: invalid JSON: ${error.message}`);
    }
  }
  return rows;
};
const uniqueIds = (rows, key, label) => {
  const seen = new Set();
  for (const row of rows) {
    const id = row[key];
    if (!id) errors.push(`${label}: missing ${key}`);
    else if (seen.has(id)) errors.push(`${label}: duplicate ${key} ${id}`);
    seen.add(id);
  }
  return seen;
};
const assertCount = (actual, expected, label) => {
  if (actual !== expected) errors.push(`${label}: expected ${expected}, got ${actual}`);
};

const manifest = readJson('run_manifest.json');
const oldSources = readJsonl('community-sources-addendum.jsonl');
const oldEvidence = readJsonl('community-evidence-addendum.jsonl');
const oldClaims = readJsonl('community-claims-addendum.jsonl');
const coreSources = readJsonl('sources.jsonl');
const sourceIds = uniqueIds(oldSources, 'source_id', 'prior community sources');
const evidenceIds = uniqueIds(oldEvidence, 'evidence_id', 'prior community evidence');
uniqueIds(oldClaims, 'claim_id', 'prior community claims');

for (const row of oldEvidence) {
  if (!sourceIds.has(row.source_id)) errors.push(`prior evidence ${row.evidence_id}: unknown source ${row.source_id}`);
}
for (const row of oldClaims) {
  for (const id of row.evidence_ids || []) {
    if (!evidenceIds.has(id)) errors.push(`prior claim ${row.claim_id}: unknown evidence ${id}`);
  }
}

const oldQueryLog = fs.readFileSync(path.join(root, 'community-query-log-addendum.md'), 'utf8');
const oldQueryIds = [...oldQueryLog.matchAll(/^\|\s*(Q\d+)\s*\|/gm)].map((match) => match[1]);
const directSourceCount = oldSources.filter((row) => /^A\d+$/.test(row.source_id)).length;
const searchOutcomeCount = oldSources.filter((row) => row.source_type === 'search_outcome_bounded_not_found').length;
const urls = new Set([...coreSources, ...oldSources].map((row) => row.url));
const coreUrls = new Set(coreSources.map((row) => row.url));
const overlappingUrls = oldSources.filter((row) => coreUrls.has(row.url)).map((row) => row.url);

assertCount(oldSources.length, 21, 'prior community source rows');
assertCount(directSourceCount, 19, 'prior direct-source rows');
assertCount(searchOutcomeCount, 2, 'prior bounded search-outcome rows');
assertCount(oldEvidence.length, 13, 'prior evidence rows');
assertCount(oldClaims.length, 9, 'prior claim rows');
assertCount(new Set(oldQueryIds).size, 22, 'prior unique query rows');
assertCount(oldQueryIds.length, 22, 'prior query rows');
assertCount(overlappingUrls.length, 2, 'prior/core overlapping source URLs');
assertCount(urls.size, 58, 'prior/core unique source URLs');
assertCount(manifest.supplemental_community_search?.source_records, 21, 'manifest prior source rows');
assertCount(manifest.supplemental_community_search?.evidence_records, 13, 'manifest prior evidence rows');
assertCount(manifest.supplemental_community_search?.claim_records, 9, 'manifest prior claim rows');

const newSources = readJsonl('coding-provider-sources-addendum.jsonl');
const newEvidence = [...readJsonl('coding-provider-evidence-addendum.jsonl'), ...readJsonl('coding-provider-policy-addendum.jsonl')];
const newClaims = readJsonl('coding-provider-claims-addendum.jsonl');
if (newSources.length || newEvidence.length || newClaims.length) {
  const newSourceIds = uniqueIds(newSources, 'id', 'coding-provider sources');
  const newEvidenceIds = uniqueIds(newEvidence, 'id', 'coding-provider evidence');
  uniqueIds(newClaims, 'id', 'coding-provider claims');
  const allowedClasses = new Set([
    'provider_account_meter',
    'published_provider_quota',
    'local_usage_log_estimate',
    'user_extrapolation',
    'api_cost_equivalent',
    'synthetic_example',
  ]);
  for (const row of newEvidence) {
    if (!newSourceIds.has(row.source_id)) errors.push(`coding evidence ${row.id}: unknown source ${row.source_id}`);
    if (!allowedClasses.has(row.measurement_class)) errors.push(`coding evidence ${row.id}: invalid measurement_class ${row.measurement_class}`);
    if (row.is_user_report === true && !row.plan_tier_as_reported) errors.push(`coding evidence ${row.id}: missing exact plan or 'not stated'`);
    if (row.is_user_report === true && row.eligibility === 'eligible' && !/^2026-09-05$|^2026-09-0[6-9]$|^2026-09-[12]\d$|^2026-09-3[0]$|^2026-10-0[1-5]$/.test(row.publication_date || '')) {
      errors.push(`coding evidence ${row.id}: eligible publication_date outside research window`);
    }
    if (row.is_user_report === true && row.eligibility === 'eligible' && !row.reported_observation) errors.push(`coding evidence ${row.id}: eligible datapoint has no observation`);
  }
  for (const row of newClaims) {
    for (const id of row.evidence_ids || []) {
      if (!newEvidenceIds.has(id)) errors.push(`coding claim ${row.id}: unknown evidence ${id}`);
    }
  }
}

const packageDir = path.join(root, 'coding-provider-ultradeep');
const readPackageJsonl = (name) => fs.readFileSync(path.join(packageDir, name), 'utf8').split(/\r?\n/).filter(Boolean).map((line, i) => {
  try { return JSON.parse(line); }
  catch (error) { errors.push(`coding-provider-ultradeep/${name}:${i + 1}: invalid JSON ${error.message}`); return null; }
}).filter(Boolean);
const pSources = readPackageJsonl('sources.jsonl');
const pEvidence = readPackageJsonl('evidence.jsonl');
const pClaims = readPackageJsonl('claims.jsonl');
const pQueries = readPackageJsonl('query_log.jsonl');
const pManifest = readJson('coding-provider-ultradeep/run_manifest.json');
const rootManifest = readJson('run_manifest.json');
const hash16 = (value) => crypto.createHash('sha256').update(value).digest('hex').slice(0, 16);
assertCount(pSources.length, 22, 'canonical package source records');
assertCount(pEvidence.length, 20, 'canonical package evidence records');
assertCount(pClaims.length, 8, 'canonical package claims');
assertCount(pQueries.length, 47, 'exact retained coding-provider query strings');
assertCount(new Set(pQueries.map(q => q.query)).size, 47, 'unique retained coding-provider query strings');
const pSourceIds = new Set(pSources.map(row => row.source_id));
const pEvidenceIds = new Set(pEvidence.map(row => row.evidence_id));
const pQueryIds = new Set(pQueries.map(row => row.query_id));
const packageEvidenceByReportId = new Map();
if (pSourceIds.size !== pSources.length) errors.push('canonical package has duplicate source_id values');
if (pEvidenceIds.size !== pEvidence.length) errors.push('canonical package has duplicate evidence_id values');
for (const row of pSources) {
  if (!/^[0-9a-f]{16}$/.test(row.source_id || '')) errors.push(`canonical source ${row.title}: invalid source_id`);
  if (hash16(row.canonical_locator) !== row.source_id) errors.push(`canonical source ${row.title}: source_id hash mismatch`);
  if (!['web','documentation','code','news','academic','government','book'].includes(row.source_type)) errors.push(`canonical source ${row.title}: invalid source_type`);
}
for (const row of pEvidence) {
  if (!pSourceIds.has(row.source_id)) errors.push(`canonical evidence ${row.evidence_id}: unknown source_id`);
  if (!row.report_evidence_id) errors.push(`canonical evidence ${row.evidence_id}: missing report_evidence_id crosswalk`);
  else if (packageEvidenceByReportId.has(row.report_evidence_id)) errors.push(`canonical evidence: duplicate report_evidence_id ${row.report_evidence_id}`);
  else packageEvidenceByReportId.set(row.report_evidence_id, row);
  if (row.observation_class === 'user_observation') {
    const original = newEvidence.find(item => item.id === row.report_evidence_id);
    if (!original || original.is_user_report !== true) errors.push(`canonical evidence ${row.evidence_id}: report_evidence_id does not map to a user observation`);
    else {
      if (!row.plan_tier_as_reported || row.plan_tier_as_reported !== original.plan_tier_as_reported) errors.push(`canonical evidence ${row.evidence_id}: missing or mismatched exact plan tier`);
      if (row.reporter_label !== original.reporter_label) errors.push(`canonical evidence ${row.evidence_id}: reporter identity mismatch`);
      const source = newSources.find(item => item.id === original.source_id);
      if (!source) errors.push(`canonical evidence ${row.evidence_id}: custom source crosswalk is missing`);
      else {
        const locator = new URL(source.url);
        locator.hash = '';
        const canonical = locator.toString().replace(/\/$/, '');
        if (row.source_id !== hash16(canonical)) errors.push(`canonical evidence ${row.evidence_id}: source/comment crosswalk mismatch`);
      }
    }
  } else if (row.observation_class !== 'provider_policy') {
    errors.push(`canonical evidence ${row.evidence_id}: invalid observation_class`);
  }
  const normQuote = row.quote.replace(/\s+/g,' ').trim();
  if (hash16(`${row.source_id}${normQuote}${row.locator}`) !== row.evidence_id) errors.push(`canonical evidence ${row.evidence_id}: evidence_id hash mismatch`);
}
for (const row of newEvidence) {
  if (!packageEvidenceByReportId.has(row.id)) errors.push(`canonical evidence is missing report evidence ${row.id}`);
}
for (const row of pClaims) {
  if (hash16(`${row.section_id}${row.text}`) !== row.claim_id) errors.push(`canonical claim ${row.claim_id}: claim_id hash mismatch`);
  for (const id of row.cited_source_ids || []) if (!pSourceIds.has(id)) errors.push(`canonical claim ${row.claim_id}: unknown source ${id}`);
  for (const id of row.evidence_ids || []) if (!pEvidenceIds.has(id)) errors.push(`canonical claim ${row.claim_id}: unknown evidence ${id}`);
}
for (const row of newEvidence.filter(row => row.is_user_report === true)) {
  for (const queryId of row.search_query_ids || []) if (!pQueryIds.has(queryId)) errors.push(`coding evidence ${row.id}: unknown search query ${queryId}`);
}
if (pManifest.mode !== 'ultradeep' || pManifest.version !== '3.0.0') errors.push('canonical run manifest mode/version mismatch');
if (rootManifest.coding_provider_ultradeep?.source_records !== 22 || rootManifest.coding_provider_ultradeep?.eligible_user_observations !== 13) errors.push('top-level manifest coding-provider counts are stale');
if (!/manual/i.test(rootManifest.silver_bullet_degradation || '') || /invocation unavailable/i.test(rootManifest.silver_bullet_degradation || '')) errors.push('top-level manifest misstates Silver Bullet workflow access/invocation');
if (rootManifest.coding_provider_validation?.sb_phase_gate?.slice(0,4) !== 'pass' || rootManifest.coding_provider_validation?.sb_verify_citations?.slice(0,4) !== 'pass') errors.push('top-level manifest Silver Bullet validation statuses are stale');
const eligibleCodingEvidence = newEvidence.filter(row => row.is_user_report === true && row.eligibility === 'eligible');
const userClassCounts = Object.fromEntries([...new Set(eligibleCodingEvidence.map(row => row.measurement_class))].sort().map(k => [k, eligibleCodingEvidence.filter(row => row.measurement_class === k).length]));
if (eligibleCodingEvidence.some(row => row.plan_tier_as_reported !== 'not stated' && !row.plan_tier_as_reported.trim())) errors.push('eligible user evidence contains a blank plan tier instead of "not stated"');
if (userClassCounts.provider_account_meter !== 9 || userClassCounts.user_extrapolation !== 1 || userClassCounts.local_usage_log_estimate !== 1 || userClassCounts.api_cost_equivalent !== 2) errors.push(`unexpected eligible measurement-class counts ${JSON.stringify(userClassCounts)}`);
const validationDir = path.join(packageDir, 'validation');
const validationChecks = [
  ['validate_report.log', text => /ALL CHECKS PASSED|VALIDATION PASSED/.test(text) && text.includes('VALIDATING REPORT')],
  ['verify_citations.log', text => text.includes('URL Verified: 19/19') && text.includes('CITATION VERIFICATION PASSED')],
  ['verify_claim_support.log', text => text.includes('"status": "pass"') && text.includes('"factual_unsupported": 0')],
  ['phase_gate.log', text => /"status":\s*"pass"/.test(text) && /"mode":\s*"ultradeep"/.test(text)],
];
const validationLogStates = {};
for (const [name, test] of validationChecks) {
  const file = path.join(validationDir, name);
  const text = fs.existsSync(file) ? fs.readFileSync(file, 'utf8') : '';
  const pass = !!text && test(text);
  validationLogStates[name] = pass ? 'pass' : 'missing_or_failed';
  if (!pass) errors.push(`validation log ${name}: missing or does not show required pass evidence`);
}

const summary = {
  prior_addendum: {
    source_records: oldSources.length,
    direct_sources: directSourceCount,
    bounded_search_outcomes: searchOutcomeCount,
    evidence_records: oldEvidence.length,
    claim_records: oldClaims.length,
    query_rows: oldQueryIds.length,
    unique_queries: new Set(oldQueryIds).size,
    core_addendum_url_overlaps: overlappingUrls.length,
    unique_urls_core_plus_addendum: urls.size,
  },
  coding_provider_supplement: {
    source_records: newSources.length,
    evidence_records: newEvidence.length,
    claim_records: newClaims.length,
    eligible_user_observations: eligibleCodingEvidence.length,
    excluded_user_context_observations: newEvidence.filter(row => row.is_user_report === true && row.eligibility !== 'eligible').length,
    policy_observations: newEvidence.filter(row => row.is_user_report !== true && row.measurement_class === 'published_provider_quota').length,
    measurement_class_counts: userClassCounts,
  },
  coding_provider_ultradeep_package: {
    source_records: pSources.length,
    evidence_records: pEvidence.length,
    claims: pClaims.length,
    exact_query_strings: pQueries.length,
    unique_query_strings: new Set(pQueries.map(q => q.query)).size,
    mode: pManifest.mode,
    orchestration_command_invoked: false,
  },
  validation_logs: validationLogStates,
  errors,
};
console.log(JSON.stringify(summary, null, 2));
if (errors.length) process.exitCode = 1;
