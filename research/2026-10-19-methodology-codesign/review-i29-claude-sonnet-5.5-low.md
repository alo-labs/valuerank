# Internal review I29 — Claude Sonnet 5.5 (effort low) on draft r88

## 0. Read check

- First line of the draft: "# ValueRank methodology — draft r88".
- Last line (906) begins "Bench v1.1 is saturated near 90% at the top and LiveBench 2.0 Coding near 96%, so they separate the max-effort rows little." and ends "...On the Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Last 12 words of the last paragraph: "Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Also read: reviewer-prompt.md; the whole folded draft (lines 1–906, in chunks); ledger-brief.md; ledger.md from "## Internal review I28" to the end (including the owner decisions O45–O56 and editor decisions E247–E258); AGENTS.md (supplied in the task context). Checked against code and data: `data/scores.json` (`v3` and `v3Tracks.aicd` rankSeparability, deletionSensitivity), `valuerank/value_v3.py` (E258 symbols), `valuerank/emit_docs.py`. I also recomputed the stated arithmetic (quality weights per ranking, source shares 72/28 and 78/22, basket-scope 86.7%, ladder positions for n = 9, 15, 32, bar-reach counts, exchange rates 3.04/2.44/2.83/1.89 from the anchors, evidence-age dates 2026-11-05/2027-01-05/2027-02-04, cohort and ranking counts 20 of 29, 9 in neither); all agree.

## 1. Findings by severity

**Critical**

None

**High**

None

**Medium**

M1. The draft does not contain editor decision E258, which the ledger records as made "from the r88 drafting" and which the code already implements; the draft's Plan-basis separability statements are therefore stale and contradict the shipped data.
- Evidence. Ledger E258(a): on the Plan basis the separability threshold, its median, the separable count and the E242 transfer tolerance range over adjacent pairs of *different* configurations only; same-configuration plan-row pairs are counted apart (`sameConfigurationAdjacentPairs`). The code does this (`value_v3.py` line ~2303; `emit_docs.py` line ~1304), and `data/scores.json` now holds, for the max-effort ranking, Plan adjacentPairs 11, separable 2, median threshold 3.01, cost tolerance 2.35, same-configuration pairs 15, correlation grid 2 / 2 / 2, and for the AI Coding Daily ranking Plan adjacentPairs 19, separable 1, median 4.54, tolerance 5.28, same-configuration pairs 30, grid 1 / 1 / 1. The draft (Outputs item 1, lines 58–65) still says the Plan median threshold "is 0.00 in both rankings", "16 of 26 and 31 of 49 adjacent Plan ranks separate, 14 and 30 of them pairs of plan rows of one configuration", grid "Plan 16 / 16 / 16" and "31 / 31 / 31", and "the printed factor is 1.0 in both rankings, which says nothing about tolerance between configurations". The string "E258" occurs nowhere in the draft, and the revision history does not mention it.
- Why it matters. Two faithful implementers reading r88 build different rules (one pools same-configuration plan-row pairs into the median, as r88 states; the other excludes them, as E258 and the code do), and r88's stated Plan figures (0.00, 16 of 26, 31 of 49, factor 1.0) are wrong against the generated record. The E242 tolerance in particular is meaningless under the draft's rule, which is the reason E258 exists. The same drafting gap affects a second sentence: draft lines 585–586 say the Vals and LiveBench leave-one-source-out branches "are not yet in the published deletion table", but E258(b) registers them (`LEAF_PUBLISHERS`, `leave-source-out:*` branches in `value_v3.py`) and the data holds them.
- Change. Write E258 into the draft: (a) in Outputs item 1 define the Plan threshold, median, separable count, grid and E242 tolerance over adjacent pairs of different configurations, state that same-configuration plan-row pairs are counted apart and separable by value alone (give the counts 15 and 30), and replace the stale figures (max-effort: 3.01 points, 2 of 11, grid 2 / 2 / 2, tolerance 2.35; AI Coding Daily: 4.54, 1 of 19, grid 1 / 1 / 1, tolerance 5.28); (b) delete "not yet in the published deletion table" and state the multi-leaf source rule (a publisher with two or more independently run leaves in a ranking gets its own branch); (c) add E258 to the revision history. Re-check the band text (E248) still holds under the new pair count.

**Low**

L1. Wording: line 160–161 calls Claude Haiku 5.5 (low) the primary of a "near family" and lists it among "four near families", while line 111 counts Claude Haiku 5.5 as a family with frontier points (it is listed as a frontier family at line 160). Say "families whose primary is a near point" or restate the "5 with near points only" count against that list so a reader can reconcile 12 = 7 + 5 with the eight families named in lines 165–166.
L2. The noise-margin companion (line 668) uses 1.96 × √2 × the median row's S1T SD, which gives 4.0 and 5.9 points, while the median separation threshold is 3.01 and 4.45; both ratios are about 1.33. This is not wrong (different statistics: median of pairwise thresholds against the median row's SD), but the draft could say in one clause why the two differ, since a reader will expect them to match.
L3. The revision history paragraph (lines 7–40) is now about 33 lines of the 906 and re-narrates every review round; the page contract would be clearer with the history moved to the ledger and one line kept. Presentation only.

## 2. Methodology design recommendations

1. (Priority 1) Add a release assertion that the stated "today" figures in the draft are generated from `scores.json` (separability, grid, tolerance, counts), or move them to the generated methodology.md. M1 shows the hand-copied figures drifting from the data within one revision; a lint comparing the draft's numbers to the data would catch this class of error before review.
2. (Priority 2) State, next to the E258 rule, the minimum number of between-configuration adjacent pairs needed before the Plan median is printed (today 11 and 19), and the status when it is below 1, so the rule is total.
3. (Priority 3) No other design changes recommended. I found no new argument on points the ledger records as adopted or rejected.

## 3. Questions for the owner

None

## 4. Verdict

VERDICT: HAS FEEDBACK
