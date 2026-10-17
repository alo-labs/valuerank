# Decision record — Claude allowance research

## Decision

Do not publish a universal Pro/Max token allowance, API-dollar entitlement, or average from current public reports. Preserve three qualifying partial-period user estimates only as exploratory API-price multiples (44.1x and 50.9x for Max20x; 20.3x for Max5x); label them estimates from actual logs, not raw full-week measurements, and state that logs were not independently reproduced. Exclude any measurement starting before 2026-09-06, regardless of post date. Provider allowance/quota statements are context only, never numerator. Keep the shared Claude Opus 5.5 40x route unvalidated for exact-model current use.

## Alternatives considered

- **Average the Reddit account observations:** rejected because the rows differ in tier, model, workload, account count, observation period, meter, log capture, and price assumptions.
- **Convert provider per-session multipliers to absolute tokens or API dollars:** rejected because the current policy pages publish relative limits and workload factors, not a fixed absolute entitlement.
- **Treat incident reports or the Artifacts promotion as allowance readings:** rejected because the incidents concern account/meter anomalies or Console API billing, while the 1–15 October Artifacts promotion is unrelated to Claude Code allowance.
- **Claim ValueRank's 40x route matches the reports:** rejected because there is no controlled current Opus 5.5 40x shared-route measurement in this research.

## Evidence summary

The package retains 11 Reddit user reports (posts through Oct 5), 2 official policy pages, 2 GitHub anomaly reports, 1 Reddit Console-credit incident, and 4 selected tracker/product pages; an Oct 6 Reddit-first indexed search surfaced no qualifying new candidate. The audited measurement window is Sep 6–Oct 6. S-C03/S-C04 pre-window segments are excluded and later partial segments remain. S-C05's Sep10–17 two-account aggregate and Sep17-reset one-account $2,350/week extrapolation are ledgered separately; the $12,751 aggregate is not isolatable to one plan because it combines two accounts and includes a 30% top-up. S12's 22 Sep ratio is context only; its Aug23 point and S11's August readings are excluded.

## Tradeoffs and risks

The report prioritizes measurement-start eligibility, exact plan wording, and strict numerator provenance. It preserves heterogeneity and cannot estimate a population distribution. Public posts are self-selected; raw logs and workload details are not independently available. Report, citation, claim-support, and phase-gate outcomes are stated only from refreshed validation logs.

## Confidence and remaining gaps

- **High** that the two cited Anthropic pages describe their published policy as summarized.
- **High** that the public posts/pages contain the recorded wording and publication dates checked.
- **Low to medium** for whether individual account-meter or API-price calculations generalize beyond the reporting account; methods are author-controlled.
- **Unverified** for ValueRank's exact shared Opus 5.5 40x route and for any hidden absolute provider quota.

## Downstream handoff

Keep `research_report.md`, source/evidence/claim ledgers, and validation logs together. For route validation, capture plan tier, exact model and route, shared-account scope, workload, start/end meter snapshots, tool/feature use, and any local token logs; analyze that as a separate controlled study. Refresh Reddit-first sources after the next cutoff without importing older readings into the current window.
