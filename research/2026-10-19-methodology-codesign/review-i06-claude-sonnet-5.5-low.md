# Internal review I6 — Claude Sonnet 5.5, effort low, on draft r65

(Saved from the subagent's report; the reviewer read all 834 folded lines.)

## 0. Read check
First line: "# ValueRank methodology — draft r65".
Last 12 words of the last line: "covers two-thirds of ranked rows jointly with the admitted components (E95, E101)."
I read all 834 lines in three chunks (1–300, 301–600, 601–834) after reading ledger-brief.md.

## 1. Findings by severity

**Critical**
None.

**High**

H1. The draft says cheaper same-family configurations lack exact evidence. For at least one family, GPT-6.1 Sol, that is false. (Cohort section, "The family's other plotted configurations ... unscored because their exact-configuration SDLC evidence is not captured"; E201 "Unevaluated cheaper siblings"; the same section's own sentence that Bug Hunt reports several efforts.)
- The draft itself says GPT-6.1 Sol, Claude Haiku 5.5 and Claude Sonnet 5.5 have both results at five efforts.
- `data/bug_hunt_scoreboard.json` holds exact Codex CLI rows for GPT-6.1 Sol at max, xhigh, high, medium and low (fixedOf105 44, 41, 38, 28, 31, plus per-effort means of 3 or 2 runs).
- `data/aa_deepswe.json` has GPT-6.1 Sol rows at the same five efforts.
- The ledger's I5 rejection of the "sibling diagnostic" gives the reason "Bug Hunt publishes one configuration per model". The draft contradicts that, and so do the data. This is the new argument.
- Why it hurts the objective: ValueRank answers "which frontier model is lowest cost for the value delivered". GPT-6.1 Sol (max) is the confirmed cheapest in the E199 frontier-families bar, and its cheaper efforts may also clear the bar. The draft lists the siblings, but only by AA Index and cost. It never tests them with evidence that exists, and it states a false reason for not doing so.
- Recommendation:
  - (a) Correct the sentence to say which siblings have exact DeepSWE and Bug Hunt results but are not ranked, with the reason "one configuration per family (E193)". Do not say the evidence is missing.
  - (b) Add a sibling-evidence diagnostic table. For each sibling with exact evidence, show its own exact leaves, coverage, displayed quality, cost on the same workload and the value score on the frozen anchors. It must be unranked, outside the anchor and bar populations, and use no transfer or imputation.
  - (c) In each bar result, mark any sibling as "displayed quality ≥ Q̄ at lower cost: not evaluated for labels".
  - This partly challenges the one-configuration-per-family part of O30/E193 (Owner decision challenge). Parts (a) and (c) do not.

**Medium**

M1. The word "ranked" has three meanings (cohort rule, Output 3, Admission rule, Known limitations).
- The draft says "23 ranked rows" in the Capture status. It defines 22 as scored, "ranked" in the sense of having a rank. It says "21 non-provisional ranked configurations" for the bar. Admission says "two-thirds of the ranked rows" and the ledger says "23 ranked".
- E201 defines N as every cohort row, but the body still says "ranked".
- Two implementers could compute ⌈2N/3⌉ as 16 or 15 (N = 23 or 22). They could also disagree on whether Muse Wonder Full, which has no cost, is in the 21 behind Q̄ = 58.28.
- Fix: define "cohort row", "scored row" and "bar population row" once, then replace "ranked" everywhere. State the bar population as a count and name any cohort row it excludes.

M2. The draft omits two AGENTS.md cohort obligations.
- AGENTS.md says to "report the cost ratio to the frontier for information only" and to defer a near-frontier family "only by a dated, reasoned roster decision". The draft's Cohort section and normative rule contain neither. The code (`valuerank/frontier.py`, `publication.py`) does report the ratio, so the draft understates what is built.
- Fix: add one normative line each. Every near point publishes `cost_ratio` as information only and it never gates inclusion. A deferred near family needs a dated reasoned roster decision and stays listed in the reconciliation inventory.

**Low**

L1. A stale figure. E184 says "the 2026-10-19 outcome is unchanged (eight components, 16-row panel)". Capture status implies about 19 full-basket rows today, and the cohort is now 23. State today's reference-panel size and the earlier release's separately.

L2. The statement "at least two population configurations are at or above Q̄ at freeze (non-tautology)" is true for every n ≥ 2 under a lower-median rule. It guards nothing. The real guard is `possibleQualifierN` ≥ 2 (E198). Reword it so readers do not take it as a safeguard.

## 2. Methodology design recommendations

1. **Sibling-evidence diagnostic** (H1). Highest priority. It is implementable today from data already in the repository, and it fixes the only place where the draft's stated reason is contradicted by its own data.
2. **Publish a small registered set of bars rather than one.** For example, quartile levels plus the E199 frontier-families level, with cheapest-above-bar at each. The single lower-median bar depends on cohort composition: retained rows that Bug Hunt happens to cover set it, and the bar moves from 58.3 to 60.9 under E199. It also has no buyer meaning. The policy object already supports a versioned level, so this is a registry change. It is cheap to compute from the frontier table and makes the "cheapest for the value" answer a curve. Keep the single frozen bar as the primary pin, which the ledger decided.
3. **Counts glossary** (M1). Generate every count (cohort, scored, bar population, admission denominator) from one object and print it beside the headline.

## 3. Questions for the owner
1. May exact-evidence same-family siblings appear as unranked diagnostic rows with their own value score (H1), given that the ledger's stated reason for excluding them, one Bug Hunt configuration per model, is contradicted by the scoreboard? If yes, I would also want the bar result to flag a sibling that clears Q̄ at lower cost.

## 4. Verdict
VERDICT: HAS FEEDBACK
