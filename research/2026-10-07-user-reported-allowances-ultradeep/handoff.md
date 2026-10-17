# Handoff — validation and next allowance refresh

## Current deliverable

Status is `completed_with_disclosed_limitations`. The provider table/index include ten rows: Anthropic 3 carried forward, OpenAI 3, xAI Standard 1 and Heavy 1, Z.AI 1, Kimi 1, with provider groups sorted by their highest multiple. The evidence package contains 21 sources, 18 evidence records and 14 claims. Read the [report](research_report.md), [manifest](run_manifest.json), [critique](critique.md), [decision](decision-record.md) and [rollup](vloop-rollup.json) together.

## Actual final validation

The actual report-format, citation, strict claim-support and phase-gate validators passed; all nine phase artifacts exist. The ten-row table has exactly the four requested columns, valid arithmetic, and no missing or duplicate references. Report format retains a warning for two recommended headings. Citation validation checked 14 references: 10 HTTP-accessible, four HTTP-unverified ([2]/[3] 403, [10] 405, [14] 403); primary fee pages were separately browser-verified. Strict support reports 14 claims, 12 factual, zero unsupported, eight partial, one needs-review and five supported. The Z.AI review label is resolved in the decision record as an eligible recent reported whole-period estimate with disclosed cutoff and raw-reproduction limits. See [final checks](validation/2026-10-07-final-checks.md), [completion audit](completion-audit.md) and [tracker apps](tracker-apps.md).

## Refresh rules

- Move the publication window forward; keep measurement intervals separately visible.
- Use end-user API-priced measured usage or labeled estimates tied to measured usage. Provider allowances, quota multipliers, and marketing claims remain excluded numerators.
- For OpenAI crowd numerical evidence, use only the TiboTattle homepage. Explicitly permitted raw By-plan aggregates may qualify without individual permalinks; identify installation/account tracks and historical dates. Never substitute normalized overall comparisons for raw plan values.
- Recheck allocation changes, particularly the September 29 new Pro $200 change, before claiming current capacity.
- Keep mixed/unidentified models at provider/plan level. Preserve K3-256, Standard local Grok 4.7 with unspecified effort, and Heavy Grok 4.7 XHigh exact variants.
- Preserve Z.AI's cross-cutoff whole-period interval and partial/projected measurement labels. Recalculate with weekly × 52 ÷ 12 ÷ monthly fee.
- Read the actual Silver Bullet skill and execute its documented host fallback when needed; absence of native invocation is not a blocker.

## Known gaps

No new qualifying Google DeepMind or Alibaba/Qwen row was found in bounded retrieval. xAI Plus/X displayed cost has unresolved API pricing basis. Standard's September 23 local Grok 4.7 account report projects $45.25/week from 30% usage at $30/month, yielding 6.536111×; identity, effort and raw ledger are unavailable. Heavy remains a low-confidence 5.785× projection: its primary plan page was verified, but browser access to supporting `report.md` was client-blocked. Tibo aggregates lack individual datapoint permalinks and independent-person counts. Z.AI's whole August 29–September 29 estimate crosses cutoff. Public sources lack complete token ledgers for independent re-pricing; search coverage remains bounded. Validator passage does not establish exhaustive Internet coverage or complete raw-ledger reproduction.
