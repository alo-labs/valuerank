# Research plan — Ultradeep

## Phase sequence and execution record

| Phase | Planned work | Artifact / result |
|---|---|---|
| 1. SCOPE | Lock question, providers, cutoff, tier rule, and measurement classes. | `scope.md`; separates user reports from policy context. |
| 2. PLAN | Search communities, provider docs, and allowance apps; record exclusions and source-quality limits. | `research-plan.md`; query log has 47 exact retained search strings. |
| 3. RETRIEVE | Search Reddit, HN, GitHub discussions/repos and open qualifying sources. | `sources.jsonl`, `evidence.jsonl`, and `query_log.jsonl`; 22 source records (19 direct pages plus 3 bounded search-outcome records). |
| 4. TRIANGULATE | Compare user meter readings with provider policy and local trackers without treating them as interchangeable. | `triangulation.md`; 14 user-source rows (13 eligible, one excluded) and six provider-policy observations. |
| 5. OUTLINE | Organize by measurement class and provider, then summarize app coverage and gaps. | `outline.md`. |
| 6. SYNTHESIZE | Draft claims with source/evidence links and explicit plan tiers. | `research_report.md`, `claims.jsonl`. |
| 7. CRITIQUE | Run three documented adversarial review cycles for tier transfer, class conflation, date leakage, and evidence strength. | `critique.md`; revisions made after each cycle. |
| 8. REFINE | Resolve issues and update ledgers, report, and exclusion decisions. | Latest report and ledgers; one vague Ollama estimate stays excluded. |
| 9. PACKAGE | Preserve manifest, query log, ledgers, decisions, handoff, validation outputs, and rollup. | Package directory; validation claims are limited to logs actually captured. |

## Search strategy

1. Search Reddit and HN with provider plus `quota`, `limit`, `usage`, `credits`, or `plan` terms and September/2026 date filters.
2. Search repositories for account-meter or local-log tools, not only public usage aggregators.
3. Search/open official provider documentation to clarify meter types and plan/reset rules.
4. Check each candidate's publication or comment date, named tier, observation interval, measurement surface, and whether the data is user-authored, official policy, synthetic, or tool-maintainer text.
5. Keep source and measurement uncertainty in the evidence row; exclude out-of-window and non-user synthetic data.

## Search record caveat

`query_log.jsonl` records all 47 exact query strings preserved in the captured handoff history. Earlier official-document searches are mentioned in that history but their exact text is unavailable. No query is fabricated to fill that gap, and the recorded number is not presented as the total number of web tool invocations.
