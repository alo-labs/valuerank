# Authorized Ultradeep contract audit

Assessment date: 2026-10-07. Scope: existing allowance research package against the actual Silver deep research workflow contract. This rework uses contract text, package counts, and validator outcomes independently inspected by the parent agent and supplied in the task message. I did not independently reread the skill, package, or external evidence: LeanCTX registration was blocked at 15/15 live workers, and the routed CLI fallback was rejected by the hook. This is a bounded contract analysis, not independent source qualification.

## Finding

The package does not yet satisfy the report and citation contracts. The phase gate passed, but the report and citation validators failed. A phase-gate pass alone cannot establish successful Ultradeep completion or substantiate numerical eligibility.

The earlier assertion that the native skill was unavailable because no named MCP invocation existed is incorrect. The skill is a workflow of instructions and explicitly supports host search/fetch fallback. Document the actual fallback execution and its limitations; do not characterize lack of a named tool as a workflow blocker.

## Required repairs

| Contract | Verified input supplied by parent | Concrete repair |
|---|---|---|
| Nine phases | All nine required; phase gate passed | Preserve each phase rollup and inspect it for `input_contract`, `work_product`, `evidence_refs`, `verification`, `validation`, `repair`, and `status`. Ensure references resolve to actual artifacts and statuses distinguish completed work from blockers. |
| Ultradeep critique | Skeptic, reviewer, and red-team angles required | Record each angle's substantive deltas under `contradiction`, `missing_source_class`, `unsupported_inference`, and `decision_risk`. Link each material delta to a loopback and resulting repair, or a documented unresolved blocker. Empty labels or repeated summaries do not demonstrate critique. |
| Run manifest | Required identity and fallback fields | Set `workflow_id`, `atomic_flow: AF-DECIDE`, `flow_step: FS-SILVER_DEEP_RESEARCH`, `question`, `mode`, `research_type`, `started_at`, `search_cli.status`, `search_cli.providers_available`, and `fallback_reason` to observed execution facts. Explain host fallback without claiming an unavailable MCP was mandatory. |
| Report structure | `validate_report` failed | Add the exact required sections: Introduction, Main Analysis, Synthesis, Recommendations, Bibliography, Methodology, and Report Metadata. Use numbered citations in the report and a matching bibliography. Retain eligibility distinctions and gaps when reorganizing. |
| Citation contract | `verify_citations` failed: no bibliography | Convert the 16-source registry into or connect it to a numbered bibliography, and resolve every numbered report citation to its source. Retain direct links and retrieval/report dates; a source count does not prove citation support. |
| Claim support | Nine claim records; strict command not yet correctly run | Run claim verification with `verify --dir DIR --strict` on the final package. Inspect claim-to-source alignment and eligibility, not just successful parsing. |
| Completion evidence | Phase gate pass; report/citation failures | Store final logs for `validate_report`, `verify_citations`, `verify_claim_support`, and `phase_gate`. Repair failures, rerun affected validators after final edits, and state any remaining blockers explicitly. |

## Numerical evidence risks requiring resolution

**ZAI approximately 5.68×:** the supplied measurement period is August 29–September 29, crossing the September 7 cutoff of the stated preceding-month window. A report date inside the window does not make the whole isolated measurement period eligible. Establish an in-window API-priced subtotal from the source, or exclude this row from the eligible numerator. Do not prorate a total across days without evidence that usage was uniform. The whole-period estimate can remain as explicitly excluded context with its exact period and reason.

**Kimi approximately 4×:** establish whether this is a weekly observation, a subscription-cycle observation, or a projection. A monthly multiple produced by scaling one week is an extrapolation and must not be presented as measured monthly allowance. Verify the reported plan, applicable denominator and cycle, and exact K3-256 variant from the underlying end-user report. If variant identity cannot be supported, retain it only at provider/plan level; do not transfer it to a ValueRank model.

**TiboTattle:** homepage plan aggregates are expressly permitted by the user and must not be automatically rejected for being aggregates. They represent installation/account tracks rather than individual users. Before calculating a multiple, verify that the numerator and denominator cover the same population, plan tier, measurement period, and currency; identify what the homepage's API-priced usage figure actually measures. Preserve the homepage as the permitted OpenAI numerical source and disclose the lack of individual datapoint permalinks. An average or aggregate requires semantic normalization supported by the homepage; do not invent it.

**Three carried Anthropic observations:** recheck report dates, isolated measurement windows, plan tiers, and whether each numerator is actual end-user API-priced usage. Carry-forward provenance alone does not establish current-window eligibility. Label reported API-priced estimates when raw token ledgers are unavailable, and keep mixed or unidentified model usage at provider/plan level.

**Four providers with no data:** preserve the absence of qualifying observations as a research gap, not a zero allowance or inferred multiple. Critique should inspect missing source classes and search coverage before asserting that no eligible evidence exists.

## Validation sequence

1. Repair eligibility decisions and claim records before changing report conclusions. Keep excluded observations discoverable with explicit reasons.
2. Complete the manifest, phase rollups, and three critique records; link any unresolved evidence risks to a documented blocker.
3. Add the required report sections and matching numbered bibliography; align report numbers with the nine claim records and 16 source records.
4. Rerun the existing `validate_report` and `verify_citations` entry points with their inspected CLI arguments. This audit has no verified script path or flags for those commands and deliberately does not invent them.
5. Run the actual claim-support verifier using its inspected entry point and `verify --dir /Users/shafqat/valuerank/research/2026-10-07-user-reported-allowances-ultradeep --strict`.
6. Rerun the existing `phase_gate` entry point against the final artifacts. Save all four validator outputs in package logs, including exit status and final invocation.
7. Independently inspect resolved citations, temporal eligibility, exact model attribution, denominator mapping, and aggregate semantics. Passing structural validators cannot replace these checks.

## Acceptance boundary

Current status: contract repairs required; external numerical evidence remains unverified by this audit. The parent-supplied phase-gate pass is retained as an observed validator outcome, while report/citation failures remain completion blockers. Completion requires successful final validation logs plus source-grounded resolution or explicit exclusion of the material numerical risks above.
