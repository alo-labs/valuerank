# Internal review I4 — Claude Sonnet 5.5, effort low, on draft r63

(Saved from the subagent's report; the reviewer read all 801 folded lines.)

## 0. Read check
First line: "# ValueRank methodology — draft r63"
Last 12 words of the last line: "ranked rows jointly with the admitted components (E95, E101)."
Those are the last 11 words of the line, where the last word is "(E95, E101)." The line ends: "...until complete exact-variant cost evidence covers two-thirds of ranked rows jointly with the admitted components (E95, E101)."
I read all 801 lines in three chunks (1–300, 301–600, 601–801).

Checks I ran:
- I recomputed the arithmetic against the draft. The following all hold:
  - the quality weights sum (60/20/10/10, and the 80/20 source split);
  - 86.7% retained under E178;
  - 113+124+66 = 303;
  - the Omniscience vectors and the retired (2A+N)/3 examples;
  - the Bug Hunt vector 52/105 → 49.52;
  - the exchange-rate and E164 formulas;
  - the Clopper–Pearson endpoints.
- I Monte-Carlo checked the E-kernel fixture: 91.46% under uniform draws and 86.75% under arcsine draws. These match the draft's 91.5% and 86.7%.
- The facts about AA, SemiAnalysis, LiveBench and tbench.ai are dated 2026-10 and sit after my knowledge cutoff. I did not check them against the web.

## 1. Findings by severity

**Critical**
None.

**High**

H1. The "tracked catalog" that decides retention is not defined in the draft, so two faithful implementations can rank different cohorts.
- Where: Cohort section, "a configuration in the release's tracked catalog is also ranked when it has both…". The ledger (E187, line 765) calls the catalog part of the build.
- The draft never says how a non-frontier model enters the catalog, who adds it, or from what public list. It also never says whether non-frontier AA models without Bug Hunt results are in it.
- The 9 retained rows (Grok 4.7, Qwen3.8 Max and others) are therefore only reproducible from a maintained roster.
  - They set the Plan upper anchor (Grok 4.7).
  - They make up 9 of the 17 rows behind the median bar.
- AGENTS.md says "capture the complete selected catalog" and that a manually maintained roster must not silently exclude a frontier model. Here the roster silently includes non-policy rows that move anchors and the bar.
- Fix:
  - Define the catalog as the registry's "AA selected catalog capture" (every model on the AA chart or leaderboard filter, with a stated rule and capture date).
  - Add it to the evidence bundle.
  - State that retention is evaluated over that whole capture, not over an ad hoc list.
  - Add a build check that fails if a catalog entry has both exact results but is not ranked.
- This is not the same as the narrowing question already recorded (E163 and E187). It is about reproducibility of the retained set.

H2. The median bar is set by the non-policy rows, and the only guard (the frontier-families diagnostic) covers anchors but not the bar.
- Where: the bar policy "lower-median displayed quality of the 17 non-provisional ranked configurations" (Q̄ = 56.70, set by Grok 4.7, a retained row). The diagnostic in the Cohort section rebuilds "anchors and exchange rate" only.
- Why it hurts: the claim scope is "AA Pareto and near-Pareto families", yet the output "cheapest above the bar" is defined by a quality level derived from the mix of policy and retained rows. When the retained set changes (H1), Q̄ changes, and the answer to "cheapest above the bar" changes with it. Nothing published shows that dependence.
- Fix: in the frontier-families diagnostic, also recompute Q̄ (lower-median over the policy cohort alone) and publish the confirmed and possible cheapest results at that alternative level, as a sensitivity beside the primary bar. The bar stays frozen.
- New relative to E192 and E198: those fix the bar-setter tautology, not the cohort dependence of the level.

**Medium**

M1. The "SDLC cost basket" label overstates what is priced today.
- Where: Outputs 1, the headline wording "SDLC basket v1", and Cost, "tasks typically part of an end-to-end SDLC and DevOps/IT workflow".
- The admitted basket is mostly general professional work: GDPval, GDP.pdf, AutomationBench, Briefcase and LCR, plus SciCode.
  - GDPval, GDP.pdf and Briefcase are non-coding professional-document tasks.
  - FrontierCode and ITBench-AA, the benchmarks closest to the stated objective of software engineering and DevOps, are pending.
- Quality is 60% software engineering, so the quality side and the cost side measure different work. A model cheap on office tasks but dear on code gets a good cost score.
- This is an Owner decision challenge to O15's composition and name, not to its mechanics. O14 and E22 already publish c_SWE and per-component shares.
- Fix: the headline should print the share of basket cost from coding components (Coding Agent Index and Terminal-Bench) next to the basket label. Suggested wording: "coding components = x% of median basket cost". Also publish the c_SWE-based rank shift as a standing column. Today it is flagged only when c_SWE deviates by more than 50% from the cohort median.

M2. The report window and the pooling fixture conflict with AGENTS.md as written.
- Where: E194 (30-day window = "the preceding month") against the fixture "two concordant reports 45 days apart… pool at the second release", and the 90-day expiry.
- AGENTS.md says to use reports from the preceding month and to exclude measurements outside the window when the report isolates them. At the second release the first report is 45 days old, outside that window, yet it still counts toward O11's two-report minimum.
- The ledger (line 796) records the window decision but I found no decision that lets an out-of-window report count toward the source count.
- Fix: either require both pooled reports to be in the current window (the strict reading of AGENTS.md), or record an explicit dated owner decision that out-of-window but unexpired reports count toward source count. The draft currently resolves the conflict silently in favour of the second reading.

M3. The score swing gate (the rule that holds the release on a swing of more than 5 points) lacks a stated treatment for a held release's entrant.
- Where: Governance. A clip hold keeps the previous release live. The ledger answers this with "versioned re-freeze in the same release cycle, so no entrant is excluded" (M3, O12 stands). The draft only says the remedy is "pre-built".
- Gap: the draft does not say what the public sees for the entrant while the release is held. AGENTS.md requires frontier entrants to be reconciled on each routine refresh.
- Fix: state that the held release still publishes the entrant in the reconciliation inventory with its unclipped score and an "off-anchor scale, release held" flag. This is a disclosure only and does not change the hold.

**Low**

L1. The explicit nominal-versus-influence disclosure is good, but the headline example hard-codes "80% of API and 63% of Plan value variance".
- Where: Outputs 1, E196. These are one date's numbers inside normative-looking wording, and they will go stale.
- Fix: generate the sentence from the release data and mark the example as illustrative.

L2. A frontier family whose top rendered point lacks DeepSWE or Bug Hunt results is ranked there and becomes provisional. O30's evidence-first choice applies only to near families.
- This is consistent with AGENTS.md ("every model on the frontier") and I raise no change.
- The draft should say plainly that the asymmetry is intentional, so that a reader does not take it for an omission.

## 2. Methodology design recommendations
In priority order:
1. Make the cohort catalog a captured artifact (H1). Define it, hash it in the evidence bundle and have the build compare it with the ranked set.
2. Extend the frontier-families diagnostic to the bar (H2). Publish Q̄ and the bar results on the policy cohort alone, beside the primary result.
3. Print the coding-component share of basket cost next to the basket label (M1). The data already exists in E22.
4. Resolve the pooling-window conflict with AGENTS.md in writing (M2), before the first Plan route becomes identified.
5. Publish held-release entrants as flagged reconciliation rows (M3).

## 3. Questions for the owner
1. Is a report that falls outside the 30-day window at the second release allowed to count toward the two-source requirement of O11 (M2)? The answer changes whether the 45-day pooling fixture stays.
2. Should the "cheapest above the bar" level be computed on the policy cohort alone, with retained rows shown as unranked context? That would change H2 from a sensitivity to the primary rule. (This is an Owner decision challenge to E163.)

## 4. Verdict
VERDICT: HAS FEEDBACK
