# Internal review I33 — Claude Sonnet 5.5 (effort medium) on draft r92

## 0. Read check

- First line of the draft: "# ValueRank methodology — draft r92".
- Last line of the draft (line 917 of the folded copy): "Surge's Complex Constraints is excluded (O53). On the Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Last 12 words of its last paragraph: "Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Also read: `reviewer-prompt.md`; the whole folded draft (917 lines, in chunks); `ledger-brief.md`; `ledger.md` from "## Internal review I28" (line 1170) to the end (line 1248, through I32 and "Draft r92"); the owner's binding instructions in `AGENTS.md` (as supplied with the task).
- Checked against `data/scores.json` (the generated `v3` and `v3Tracks.aicd` objects): cohort tiers and gaps, ranked/excluded status of all 29 cohort configurations, bar ladders and bar reach, displayed-cheapest results and noise-margin companions, rank-separability medians, counts, grids, bands and transfer tolerances, cost-influence allocations, admission matrices, plan-row counts, listed-indicative rows, frontier-families and one-row-per-family diagnostics, FrontierCode and Terminal-Bench cross-source figures. I also recomputed by hand the weight sums (60 + 20 + 10 + 10 in both rankings), the ladder positions and fixtures, the admission counts (2^8 − 1 = 255 and 2^7 − 1 = 127 feasible sets), the exchange rates and tolerances, the MiMo quota-ceiling table (credits × rate ÷ fee), the kernel-check fixture (91.5%) and the evidence-lifecycle dates. All of these agree with the draft except the points raised below.

## 1. Findings by severity

**Critical**

None.

**High**

None.

**Medium**

- **M1. The scope of the O41 indicative value is ambiguous, and the "today" example is incomplete.**
  - Issue. The draft says "a listed frontier or near-frontier configuration shows, apart from the ranking table, an indicative value on the leaves it has" and gives, as today's example, only MiMo-V2.6-Flash (max-effort quality 45.0 over 72% of the weight, API 56.9, Plan 47.5; AI Coding Daily 44.1 over 78%, 50.9, 44.7). The draft uses "listed" in two ways. The Cohort bullet says a configuration is "excluded from ValueRank, listed under O38 with its searches, only when it lacks every ranking's set" (today 9). The next sentence says "each ranking also lists the cohort configurations without its own set" (today 20 beside the max-effort ranking and 14 beside the AI Coding Daily ranking). The generated data follow the second reading: `listedIndicative` holds 20 rows in the max-effort object and 14 in the AI Coding Daily object. Those include rows that are ranked, with a real value, in the other ranking (for example GPT-6.1 Sol (high), 82% coverage, API 54.9, in the max-effort listing; Claude Sonnet 5.5, 90% coverage, in the AI Coding Daily listing). They also include MiniMax-M3.1-Flash (47.8 over 72%, API 53.1, Plan 44.8), which is listed under O38 and so falls under O41 on any reading, yet the "today" example omits it.
  - Why it hurts. Two faithful implementers read different row sets: the 9 O38-excluded configurations, or the 20 and 14 per-ranking listed rows. The second reading shows one configuration with a real value in one ranking and an indicative value at 82% or 90% coverage in the other. That sits uneasily with "values compare within one ranking only" and with O41's "apart from the ranking, not ranked, not comparable". No score changes, but the published table differs.
  - Recommendation. State in the O41 paragraph which set shows indicative values (the O38-excluded configurations only, or every configuration listed beside a ranking). Say whether a configuration ranked in the other ranking is shown. Make the "today" example complete (add MiniMax-M3.1-Flash, 47.8 over 72%, API 53.1, Plan 44.8; AI Coding Daily 46.6 over 78%, 47.2, 42.5) or replace it with counts.

**Low**

- **L1. The scale of SD_i in the separability formula is not stated where the formula is given.** Output 1 writes 1.96 × √(SD_i² + SD_j² − 2ρ·SD_i·SD_j) as "the median value gap", "from analytic quality-leaf SDs". The generated `valueSd` values (about 1.08 to 1.76) show SD_i is the row's value-score SD, which is 0.75 times its quality SD. The 0.75 appears only in the noise-margin paragraph ("about 1/0.75 times the separability threshold"). Add "SD_i = 0.75 × the row's quality SD" to the formula sentence.
- **L2. An undated figure is stale.** The Quality section says "AA's IFBench covers 1 of 19". The 19 is the cohort size at O26 (2026-10-19). Today the cohort is 29 and the rankings have 9 and 15 rows. Date it ("1 of 19 cohort rows at O26") or restate it for the current cohort.
- **L3. The end-user report search list omits MiniMax.** The 2026-10-21 search covered "xAI, Google, Z.AI, Kimi, MiMo, DeepSeek, Qwen, Meta Muse", yet MiniMax-M3.1-Flash has been a cohort configuration since O51. It is only listed, so no ranked Plan row is affected, but the sentence implies the non-Anthropic/OpenAI providers were covered. Either add MiniMax to the next search or say that listed-only providers were not searched.
- **L4. Bar triples are printed in two orders.** Output 3 and the Bar-policy bullet give lower, headline, upper (49.8, 60.7, 62.1). E205 and E207 give headline, lower, upper (60.7 / 49.8 / 61.1; "5, 7 and 3"). Each is labelled, but one fixed order, or the label repeated in each place, would remove a way to misread them.
- **L5. The Cost section's per-ranking admission sentence cites E254 under O53 but not O57.** The Cohort bullet cites O57. The ledger (I30 L4, I31) made O57 the owner's decision, so the Cost section should name it too.

## 2. Methodology design recommendations

1. (Priority 1, answers M1.) Add one definition, "listed row", with two named subsets: "excluded from both rankings (O38 list)" and "not in this ranking (per-ranking list)". Attach the O41 indicative value to exactly one of them, and put the choice and the displayed fields (quality, coverage, API and Plan value) in the E255 paragraph.
2. If the owner wants indicative values for the per-ranking list, suppress the indicative value for a configuration that has a real value in the other ranking and print a pointer to that row instead. This avoids two values for one configuration.
3. Print the value-scale SD definition (0.75 × quality SD, Plan rows taking the configuration's SD) once, in the separability definition. Then the formula, the noise-margin ratio and the E242 tolerance share one stated scale.
4. Date the stale counts (IFBench coverage) at refresh. A short lint that flags any bare "x of N" in the Quality prose whose N differs from the current cohort or ranking size would catch these.

## 3. Questions for the owner

1. Should O41's indicative value be shown only for the configurations excluded from both rankings (today MiMo-V2.6-Flash and MiniMax-M3.1-Flash), or for every configuration listed beside a ranking (today 20 and 14), including those ranked in the other ranking? The answer changes which rows the published tables show, not any score.

## 4. Verdict

VERDICT: HAS FEEDBACK
