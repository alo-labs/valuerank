# Internal review I30 — Claude Sonnet 5.5 (effort low) on draft r89

## 0. Read check

- First line of the draft: "# ValueRank methodology — draft r89".
- Last line of the draft: "Surge's Complex Constraints is excluded (O53). On the Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Last 12 words of its last paragraph: "the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Also read: `reviewer-prompt.md`; the whole folded draft (908 lines, in chunks); the head of `ledger-brief.md`; `ledger.md` from "## Internal review I28" to the end (including O45–O56, E247–E258 and the I29 handling); and `AGENTS.md`. I checked figures against `data/scores.json` (v3 rows, exchange rate, workloads, anchors, `models[].aaFrontierTier`, gap and primary flags). Verified and found correct: the 29-configuration cohort (18 frontier, 11 near; 12 families, 7 frontier and 5 near-only); the 9 and 15 ranked rows; the 9 excluded configurations; 20 of 29 ranked at least once; the leaf weights and totals (60 / 20 / 10 / 10 in both rankings; 14 and 11 leaves); the 72/28 and 78/22 source shares; the ladder positions for n = 9, 15 and 5; the anchor ratio 297.5 giving 3.04 value points per doubling (the stored low and high anchors are already padded); the 255 and 127 feasible admission alternatives; the 27 and 50 plan rows and the 14 of 27 transfer or ceiling rows; the noise-margin bars (64.7 / 53.8 / 66.1; 55.1 / 43.9 / 63.0); and the transfer tolerances 2.35 and 5.28.

## 1. Findings by severity

**Critical**

None

**High**

None

**Medium**

1. **The list of near points of frontier families is wrong (a stated "today" figure).** The Cohort section (the "Configuration rule" bullet) says "A frontier family's near points (today Claude Haiku 5.5 (low), Claude Opus 5.5 (medium with fallback) and Claude Sonnet 5.5 (xhigh with fallback)) are cohort rows like any other plotted effort, never primaries". `data/scores.json` (`models[].aaFrontierTier = "near"`) shows four near points in frontier families: it also includes **Claude Haiku 5.5 (max)** (gap 3). Haiku (max) matters: it is the one Haiku row ranked in the max-effort ranking, and Haiku's frontier primary is (xhigh), which is listed. A reader who follows the sentence would conclude that Haiku (max) is neither a frontier nor a near point, or that it is a primary. The sentence is also the one r89 set out to correct (I29 L1), so the omission survives the correction. It is not a cosmetic slip, because the draft's other count statements (11 near configurations; "Claude Haiku 5.5 and GPT-6 Astra have other efforts ranked"; the one-row-per-family diagnostic that leaves Haiku and Astra out) depend on which near points belong to which family. Recommended change: list all four (Claude Haiku 5.5 (max), Claude Haiku 5.5 (low), Claude Opus 5.5 (medium with fallback), Claude Sonnet 5.5 (xhigh with fallback)), or replace "today …" with the generated list and the count. The 11 near points then reconcile as 5 near-family primaries, these 4, and GPT-6 Astra (max) and (high), which are non-primary near points of a near-only family. The draft should say so, since it states the family-primary rule for near-only families only in terms of the primary.

**Low**

1. **Basket admission is counted per ranking, but AGENTS.md says "the cohort".** AGENTS.md admits a basket component "once its exact-configuration cost is captured for at least two-thirds of the cohort jointly with the other admitted components (O15; E140)". E254 reads "cohort" as each ranking's own cohort rows (N = 9 and 15). On that reading the Coding Agent Index v2.0 (7 of 9 rows) is admitted in the max-effort ranking and DeepSeek V4.1 Flash 1017 and MiMo-V2.6-Pro become subset-cost rows. Read against the 29-configuration cohort it would stay pending (7 of 29, threshold 20). The draft states its reading consistently (the "Counts, defined once" bullet and the per-ranking admission paragraph) and O53 gives each ranking its own anchors and scenario run, so I do not call this a defect of the draft. It is an editor-level reading that changes which rows are subset-scored and that is never marked as an interpretation of AGENTS.md. Recommended change: one sentence in the per-ranking admission paragraph saying that "the cohort" in O15 and E140 is read as the ranking's cohort rows (E254), and listing it among the items the owner may confirm. This is not a new design proposal. It is the only place where an editor record fixes an ambiguity in an owner decision without saying so.

## 2. Methodology design recommendations

1. Print the near and frontier point lists of each family from the generated data (a "family table": family, frontier points, near points, primary, ranked in which ranking). That removes this class of stale or incomplete "today" enumeration, because the same table already feeds the cohort count (18 + 11) and the one-row-per-family diagnostics.
2. Add a build assertion that every "today" enumeration in the generated methodology text (near points, listed configurations, excluded configurations) equals the set derived from the data, as `check_open_web` already does for searches. The I29 M1 and L1 findings and Medium finding 1 above are all stale enumerations.

## 3. Questions for the owner

None

## 4. Verdict

VERDICT: HAS FEEDBACK
