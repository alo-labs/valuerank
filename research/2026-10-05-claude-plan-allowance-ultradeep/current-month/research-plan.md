# Research plan

## Research question

What public user-reported Claude subscription allowance measurements fall within 2026-09-06 through 2026-10-06, and do API-priced end-user logs justify any exploratory plan-value multiple or validate ValueRank's provisional shared Claude Opus 5.5 40x route?

## Mode rationale

Selected `ultradeep` because the request requires a comprehensive date-filtered source review with conflicting, low-control account reports and an exact-model applicability decision. Three adversarial critique cycles are documented; remaining route-specific uncertainty is an explicit blocker.

## Scope and order

1. Search Reddit first for dated account observations and current plan-specific allowance claims.
2. Open candidate Reddit permalinks/metadata; record publication and observation dates separately.
3. Apply the 2026-09-06–2026-10-06 window to the measurement start date, not merely the post date. Record publication dates as provenance; exclude measurements that start before the window and retain only separable segments that start within it.
4. Record each user's plan wording verbatim; use `not stated` when absent. Do not infer a tier from price, a reply, or subreddit.
5. Check GitHub reports for anomalies, provider documentation for policy, and selected project pages for tracker-tool types.
6. Build a claim/evidence ledger that maps every evidence row to at least one claim. Keep account readings, incidents, policy, tool discovery, and historical exclusions separate.
7. Red-team date eligibility, method, denominator, task comparability, estimates vs entitlements, and exact-model route applicability.

## Evidence standards

- Prefer primary post bodies and platform metadata over search snippets.
- Preserve source identity, UTC post time when available, observed window, stated tier, model/workload, method, and caveats.
- Only actual end-user reported measured usage valued at API prices can be a numerator. Label user-derived calculations from actual logs as estimates/extrapolations, not raw measured totals, and state whether the underlying data can be independently reproduced.
- Provider allowance/quota claims and meter-only reports are context only, never numerator; provider plan prices may be used as a supported fee denominator.
- Meter percentages are individual observations, not universal token units.
- No combined estimate or average unless a common denominator and comparable design are available; none were found in this window.
- Record inaccessible routes and validators as not run; never present intended commands as executed.

## Deliverables

`report.md`, `scope.md`, `query_log.md`, `sources.jsonl`, `evidence.jsonl`, `claims.jsonl`, this plan, `outline.md`, `triangulation.md`, `critique.md`, `decision-record.md`, `handoff.md`, `run_manifest.json`, `vloop-rollup.json`, and validation logs under `validation/`.
