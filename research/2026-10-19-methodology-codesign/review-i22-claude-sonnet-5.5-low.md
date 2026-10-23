# Internal review I22 — Claude Sonnet 5.5 (effort low) on draft r81

## 0. Read check
- First line: `# ValueRank methodology — draft r81`
- Last 12 words of last line: "covers two-thirds of cohort rows jointly with the admitted components (E95, E101)."

(All 1006 lines read in four chunks; ledger-brief.md read first; ledger.md grepped for E98/±20% (decided), the Fable route (decided) and Cognition (long lines omitted, not read). No web search: the relevant facts are internal captures dated 2026-10-17..21 that cannot be externally verified. Arithmetic checked — anchor exchange rates, ladder positions, panel counts, capture-age gaps — consistent except the numeric slip in L1.)

## 1. Findings by severity

### Critical
None

### High
**H1. "No quality floor" vs O36/O38's 100% coverage floor, and AGENTS.md still states the older rule.** Output 1 says "No quality floor (O8); every ranked row has every quality leaf (O36)"; Cohort and Quality say a configuration missing any of the eleven leaves "is listed, not ranked" and "gets no score" — including a required frontier family (MiMo-V2.6-Flash, no Bug Hunt). Yet the checked-in AGENTS.md says "Include every model represented on … the frontier", "Missing leaves stay missing, low coverage marks a row provisional, and there is no quality floor (O8)", and "a missing supplementary benchmark must not silently exclude a frontier model". The exclusion is logged (not silent), but "no quality floor" is false as written and the draft never says which text governs; two faithful implementers could disagree on whether a frontier model with partial coverage is ranked. A single third-party benchmark (Bug Hunt: one maintainer, two repos) can remove a frontier model from the ranking, while the provisional/bound/renormalisation machinery stays specified but "vacuous" (E235). Change: (a) reword to "no floor except full benchmark coverage for ranking (O36, O38; supersedes O8's partial-coverage ranking)"; (b) state in Governance that O36/O38 supersede AGENTS.md's partial-coverage clause and ask the owner to amend AGENTS.md; (c) **Owner decision challenge (O36/O38)**: show each listed required frontier family in the ranking table as an unranked row with its displayed observed-leaf quality ("partial coverage, not ranked, no label, no bar membership") and cost score where one exists.

### Medium
**M1. Third-party gap fills with a measured offset keep full label eligibility; provider-claimed fills lose it (E233 vs E234).** E234 shows Cognition above AA by 2.5 points on average and 11.8 at most (τ_b 0.73, 10 rows); eight configurations use Cognition's number at 10% quality weight; gap-fill removal moves 11 API ranks (largest 6) and 15 Plan (largest 8). Only a provider claim denies a label, and the draft does not say why a different-harness, different-publisher leaf with a documented upward offset is safer. Change: pre-register an E222-style denial for rows whose filled leaf comes from a pair with mean offset above a fixed threshold (e.g. 2 points) or with scale equivalence not tested — or, if the owner prefers parity, state the reason in the draft. (Ledger Cognition lines not read; discard if already decided.)

**M2. The only controlled Plan evidence has no stated clock or route mapping in the methodology.** The draft never prints the SemiAnalysis publication/measurement date, the resulting 90-day expiry and 30-day grace dates, or each measured route's allocation regime (Opus 5.5 all-Opus; Fable 50% shared pool), so the lifecycle table cannot be applied by a reader. It also never says Fable 5.1 uses its exact measured routes rather than the Opus transfer (the ledger does). Change: add a short "Plan evidence today" table: route, source, date, regime, stage, expiry.

### Low
**L1.** The harness-stress paragraph says "13 of 14 matched tbench.ai Terminal-Bench rows" use vendor agents, but the cross-check row's per-agent counts are mini-SWE-agent 1, Claude Code 5, Codex 6, Grok Build 1 (13 total, 12 vendor). Reconcile.

**L2.** The ladder population includes Muse Wonder Full (no AA cost) and MiMo-V2.6-Pro (provider-claimed DeepSWE); both help set H, which is used to rank cost. Exclude rows with no value score from the bar population or state the reason (borderline given the ledger's earlier rejection of the policy-cohort bar as primary).

**L3.** A "window-straddling" report (measurement started before the window) still counts toward two-source concordance by its end date; consider denying it a counting role unless its in-window portion is isolated.

## 2. Methodology design recommendations (prioritised)
1. Keep listed frontier families visible: an "unranked frontier families" block in the ranking table (observed-leaf quality, cost score, gap list, search-log date).
2. Label eligibility conditioned on gap-fill agreement: a per-source-pair verdict each release ("label-eligible" or "competes, never earns") within pre-registered offset and rank-agreement tolerances, via the E222 mechanism.
3. A noise-context diagnostic for bar results: for each bar's cheapest and marginal qualifier, the margin to H in units of a conventional standard error from published sample sizes (e.g. binomial √(p(1−p)/113) for DeepSWE's 113 tasks; Bug Hunt's run count N), as a named stream under E145/E155/E165 that never authorises a label.
4. Dormant-stream registry: mark S1M "dormant (equals S1)" in the active-rules manifest.
5. Plan evidence-today table (M2).

## 3. Questions for the owner
1. Should AGENTS.md be amended so "no quality floor" and "include every frontier model" read as "listed but unranked when a leaf is missing", and should a listed frontier model still show partial-coverage figures?
2. Should a Cognition FrontierCode number that measurably exceeds AA's be able to earn labels, or only compete?
3. What are the SemiAnalysis publication and measurement dates and each route's allocation regime?

## 4. Verdict
VERDICT: HAS FEEDBACK
