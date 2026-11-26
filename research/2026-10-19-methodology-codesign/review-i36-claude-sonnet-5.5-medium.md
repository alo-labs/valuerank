# Internal review I36 — Claude Sonnet 5.5 (effort medium) on draft r95

## 0. Read check

- First line of the draft: "# ValueRank methodology — draft r95".
- Last line of the draft: "Instruction following has no weight while Surge's Complex Constraints is excluded (O53). On the Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Last 12 words of the last paragraph: "Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Also read: the whole folded draft (lines 1–929, in chunks); `reviewer-prompt.md`; `ledger-brief.md`; `ledger.md` from "## Internal review I28" (line 1170) to the end (line 1276); the root `AGENTS.md` (as supplied in the task context); and the review brief.
- Checked against data and code: `data/scores.json` (v3 and v3Tracks.aicd: bars, bar currency, displayed-cheapest and margin results, exchange rates, anchors, cost influence, listed indicative values, clip gates), `data/aa_frontier_capture.json` (18 frontier and 11 near points, gaps, 189 plotted points, first vertex GPT-6 Luna (low) at $10.63) and `valuerank/anchors.py` (`clip_gate`). Every figure I recomputed matched the draft: ladder positions and fixtures, 7/5/3 and 12/8/5 bar reach, margins 4.0 and 5.9 and the margin-adjusted bars, exchange rates 3.04/2.44 and 2.83/1.89 with their quality offsets, tolerances 2.35 and 5.28, plan-row counts 27 and 50, transfer counts 14 and 48, the cost-variance allocations (65%, 2%, about −90%, −26%), the indicative values for MiMo-V2.6-Flash and MiniMax-M3.1-Flash, the age arithmetic of the SemiAnalysis evidence, and the admission counts (255 and 127 alternatives, thresholds 6 and 10). No stated figure is wrong.

## 1. Findings by severity

**Critical**

None.

**High**

None.

**Medium**

M1. The clip gate's population is stated in a way that reads onto the listed (indicative) configurations, and under that reading both rankings would be held today.

- Issue. Cost, "Clip gate (single governing gate)", says the release is held when more than max(1, 10% of n) rows clip, or any such row lies beyond an anchor by more than a factor of 2, "where n is the number of rows scored on that anchor object (rows on its workload with a positive cost on that basis…)". Cohort says a listed configuration shows an indicative value with "its cost on that ranking's frozen anchors for its own workload (the cost score clipped to 0–100 like any other…)" (E259, I35 L5). A listed configuration is a row on the workload with a positive cost on that basis, so the parenthetical covers it. The defined term "scored row" (Counts: a cohort row with a value score and a rank) points the other way, and the code (`valuerank/anchors.py` `clip_gate`, `data/scores.json` gates) counts ranked rows only (15 rows, no clips in the AI Coding Daily ranking; 7 and 2 rows in the max-effort ranking). The draft never says which reading governs.
- Why it matters. The two readings give different outcomes on today's data. Listed rows already sit outside the frozen anchors: in the AI Coding Daily ranking Claude Opus 5.5 (max) and Claude Sonnet 5.5 (max) have API cost score 0 (allowance 1.5 on 15 ranked rows, 1.7 on 17 rows with them, so two clipped rows exceed it) and GPT-6 Luna (low) scores 100 at $8.4 against c_L of $10.35. In the max-effort ranking, GPT-6 Luna (low) lies about 7.5 times below c_L ($8.4 against $62.86), beyond the factor-2 limit, and four other listed rows clip. A faithful implementer taking the parenthetical literally holds both rankings. One taking "scored row" holds neither. The gate's stated purpose also points to the broad reading: E197 and E200 describe it as the catch for a cheaper frontier entrant beyond the low anchor. GPT-6 Luna (low) is the first vertex of AA's rendered frontier, and O51/O36 now keep it out of the ranked population.
- Recommendation. State the population explicitly. The simplest choice is the engine's: n and the clip test range over ranked rows (rows with a value score and a rank on that anchor object), and remove "rows on its workload with a positive cost" from the parenthetical. Add an informational line to the gate output, "listed rows beyond the anchors", with the count, the identities and the factor, and mark a listed row that is on the rendered frontier. That row would be the E197 entrant case, and it would never hold a release but would be visible. Add a fixture in which a listed frontier row lies beyond the low anchor by more than a factor of 2 and the release is not held. If the owner wants the gate to see listed frontier points, the rule should say so (see the question in section 3).

**Low**

L1. Release-gate scope across two rankings is not stated. O12 and the Governance section say a failed gate "holds the release". Since O53 a release carries two rankings with separate anchor objects, and the draft says gates are per basis and anchor object. It does not say whether a hold in the AI Coding Daily ranking also blocks publication of the max-effort ranking, or whether the swing gate runs per ranking. Nothing fires today, so no ranking is affected. Add one sentence: gates are evaluated per ranking and a hold applies to that ranking alone, or to the whole release if the owner prefers.

L2. The near-point census in Cohort does not add up on its face. The draft says 11 near points and then names the near families' primaries (5) and the frontier families' near points (4), which gives 9. The missing two are GPT-6 Astra (max) (gap 3) and GPT-6 Astra (high) (gap 3), the Astra points that are ranked, which the text only mentions as "other efforts ranked". Name them once, for example in the near-family sentence: "GPT-6 Astra also has near points (high) and (max), both at gap 3".

L3. "Listed" is used in two senses again in one place. After E259, "listed beside a ranking" means a cohort configuration without that ranking's set, and "excluded" (O38) means lacking both. The frontier-and-near-families paragraph ("Today the primaries of two frontier families… are listed… Claude Haiku 5.5 (low) and Claude Sonnet 5.5 (xhigh), also listed…") means "excluded". Replace "listed" with "excluded (O38)" there.

L4. The bar-currency sentence on the interval outputs' counts is hard to parse ("the headline and upper counts are the same there and the lower one is 5"). Say: "over the main-workload rows the headline and upper counts equal the bar-population counts (5 and 3), and the lower count is 5 against 7".

## 2. Methodology design recommendations

1. (Priority 1, implements M1.) Fix the clip-gate population as ranked rows, publish a "listed rows beyond the anchors" disclosure with a rendered-frontier marker, and add the matching fixture. Cost: one sentence and one output field. It changes no score and no rank.
2. (L1.) Add a gate-scope sentence: each gate runs per ranking, and the release record states which rankings were held.
3. (Presentation, L2–L4.) Name the Astra near points, separate "listed" from "excluded" in the primary paragraph, and rewrite the bar-currency count sentence.
4. No other design change is warranted. The remaining open choices (the unestablished net direction of the separability threshold, S1T's GDPval assumption, the dormant S1M stream) are disclosed in the draft and are decisions the ledger records as already handled.

## 3. Questions for the owner

Q1. Should a listed configuration that lies on AA's rendered frontier and falls beyond a ranking's anchors by more than a factor of 2 (today GPT-6 Luna (low), the first vertex, about 7.5 times below the max-effort low anchor) be able to hold the release, as E197's "cheaper entrant beyond the low anchor" wording implies? If yes, the gate population must include listed frontier rows and the anchors would have to be re-frozen or widened every time such a row is listed. If no, the ranked-rows-only rule in M1 stands and the disclosure line is enough. My recommendation is "no": a listed row has no rank and no label, so it cannot distort a score, but the owner should confirm because the answer changes whether both rankings are held today.

## 4. Verdict

VERDICT: HAS FEEDBACK
