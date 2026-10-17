# Handoff

## Package use

- Read `research_report.md` for the coding-provider supplement.
- Read `scope.md` before merging it into the larger ValueRank allowance synthesis.
- Preserve `plan_tier_as_reported` exactly when aggregating user reports; do not merge the Copilot thread author with the commenter or the two Ollama commenters.
- Use `measurement_class` to filter results. `user_extrapolation` and local log figures are not account meters; API-cost equivalents are not subscription usage; provider-published quota records are not subscriber observations.
- Keep CP-E14 excluded. It is retained to show why a weak source was rejected.
- Treat the tracker repositories as evidence of tools that claim to read personal meters/logs, not as an aggregate user dataset.
- For any `CP-E##` observation cited in the report, find the same value in `report_evidence_id` in [canonical evidence](evidence.jsonl). The matching row contains the exact `plan_tier_as_reported`, reporter/comment label, and `source_id`; use [canonical sources](sources.jsonl) to resolve that source ID. `CP-P##` rows are provider policy and have no subscriber tier.

## Validation status

After the evidence-tier traceability update, the nine-phase Silver Bullet gate, report contract, citation verification, claim-support verifier, and custom package/tier crosswalk validator were rerun; the latest results are recorded in `validation/evidence-tier-revalidation.md`. All passed: 19/19 cited URLs accessible, 7 claims supported, 1 partial, 0 unsupported factual claims, and zero package-validator errors. These checks ran through the supported local LeanCTX command route. The Silver Bullet skill/workflow was accessible from its registered LeanCTX root, but the per-run `/sb ultradeep` orchestration command was not invoked. The older raw logs remain in `validation/` as the first full package-validation outputs.

An MCP `ctx_execute` probe separately failed because the shared sandbox was at 15/15 live workers. This is an execution-capacity limit for that route, not evidence that the Silver Bullet workflow was unavailable. The successful local validation logs above are the completion evidence.

## Remaining limitations

- The exact literals for a small earlier official-document search set are absent from the retained transcript; 47 exact search strings are available in `query_log.jsonl`.
- Reddit evidence is self-reported; raw account exports and screenshot pixels were not independently inspected.
- Hacker News, Windsurf-only, and Z.ai/GLM no-hit findings are bounded to the returned searches.
- No typical-use estimate or provider plan ranking can be supported.
- The older parent addendum's E01 row aggregates distinct Cursor commenters; this supplement does not repair that historical row and the audit calls out the limitation.
