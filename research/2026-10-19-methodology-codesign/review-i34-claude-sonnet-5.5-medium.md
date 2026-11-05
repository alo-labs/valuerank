# Internal review I34 — Claude Sonnet 5.5 (effort medium) on draft r93

## 0. Read check

- First line of the draft: "# ValueRank methodology — draft r93".
- Last line of the folded draft (line 922): "Surge's Complex Constraints is excluded (O53). On the Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Last 12 words of the last paragraph: "Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Also read: the whole folded draft (lines 1–922, in chunks); `reviewer-prompt.md`; `ledger-brief.md`; `ledger.md` from "## Internal review I28" (line 1170) to the end (line 1257, through the I33 entry); the brief; and the root `AGENTS.md` rules supplied in the task context.
- Checked against repository data (`data/scores.json`, keys `v3` and `v3Tracks.aicd`, and the generated `methodology.md` and `README.md`): bar ladders, one-row-per-family diagnostic, anchors and exchange rates, rank separability (medians, counts, grids, tolerances, bands), noise margin, displayed-cheapest and bar-currency counts, gap-fill offsets, listed-indicative values and counts (20 and 14), cost influence and variance allocation, clip gates, plan-row counts, weight sums per ranking, admission counts (255 and 127 alternatives, thresholds 6 and 10) and the Plan evidence date arithmetic. Everything matched except the item in finding M1.

## 1. Findings by severity

**Critical**

None.

**High**

None.

**Medium**

M1. The AI Coding Daily one-row-per-family ladder is printed in the wrong order, against the draft's own stated order and Outputs item 3 (Cohort bullet "One row per family (E205)", draft line 168).
- Issue: the sentence for the max-effort ranking says "ladder (lower, headline, upper, the order used everywhere else) 49.8 / 60.7 / 61.1 against the frozen 49.8 / 60.7 / 62.1", which is correct. The AI Coding Daily sentence then says "ladder 49.2 / 42.8 / 52.8 against the frozen 49.2 / 38.0 / 57.2". Read in the declared order, that gives a lower bar (49.2) above the headline bar (42.8), which is impossible. It also contradicts Outputs item 3, which says E205 "gives the same headline bars, 60.7 and 49.2". The data confirm the triple is in headline / lower / upper order: `v3Tracks.aicd.diagnostics.familyPrimary.ladder` is median 49.24, lower 42.75, upper 52.82, and the frozen ladder is 37.997 / 49.240 / 57.156. The correct lower / headline / upper statement is 42.8 / 49.2 / 52.8 against the frozen 38.0 / 49.2 / 57.2.
- Why it matters: I33 L4 recorded "bar triples are given as lower, headline, upper throughout" as adopted, but this sentence was missed. The ladder is a published figure, and a reader or a generator test that follows the stated order gets a wrong headline bar for the one-row diagnostic (42.8 instead of 49.2) and a wrong lower bar. A stated figure that is wrong under its declared labels is a Medium.
- Change: reorder the AI Coding Daily triple to "42.8 / 49.2 / 52.8 against the frozen 38.0 / 49.2 / 57.2". Add a release lint that asserts lower ≤ headline ≤ upper in every printed bar triple, and that the draft's triples are emitted from `scores.json` rather than transcribed.

**Low**

L1. "Along the strictly rising rendered line that point is also the family's dearest" (the Cohort configuration rule, E193/E251 text, draft line 176) is true only among the family's rendered-frontier points. Claude Haiku 5.5 (max), a plotted near point of the same family, costs more than the family primary, Haiku 5.5 (xhigh): the data show Haiku (max) at an AA eval cost of about 330 against about 158 for the primary. Change: say "the family's dearest rendered-frontier point". The same sentence appears in the generated `methodology.md` frontier rule.

L2. The separability threshold uses "the row's analytic quality SD from its leaves" (Outputs item 1), while the O44 noise margin uses "the median row's S1T quality SD" (draft line 683). They are the same quantity today: the data's `qualityMargin` 4.0239 equals 1.96·√2 times the median of the printed value SDs divided by 0.75. Two names for one quantity invite an implementer to build two calculators. Change: name it once (for example "the analytic quality SD, which S1T draws from") and use that name in both places.

L3. Plan indicative values for a configuration with no Plan route. The report-search paragraph (draft line 327) says MiniMax-M3.1-Flash "has no Plan row", while the indicative-value paragraph prints Plan values 44.8 and 42.5 for it. The data show these are its API cost on the Plan anchors (an API-cost fallback, flagged under O13), which is why they differ from its API values (53.1 and 47.2). The draft never says so. Change: add "a listed configuration with no eligible route shows its API-cost fallback on the Plan anchors, flagged (O13)" to the E259 sentence, and reword line 327 to "has no route-based Plan row".

L4. The basket label "SDLC basket v1" is used for two different admitted sets: 8 of 9 target components in the max-effort ranking and 7 of 9 in the AI Coding Daily ranking (draft lines 85–86 and 207). The workload hashes differ (the data show `9a0d376cc6080f3c` for the max-effort main workload and `1453a9a0576b02ea` for the AI Coding Daily main workload), so scoring is unambiguous, but a reader comparing the two headlines sees the same version name over different baskets. Change: print the workload ID beside the basket version in each headline, or name the versions per ranking.

L5. "Listed" has two senses left in text that E259 did not touch. E240 ("every logged search for a listed frontier or near-frontier family") and the full-benchmark-set paragraph ("the configuration is then listed with its missing leaves and the search ... and gets no score in that ranking") use the older O38 sense, while E259 defines "listed beside a ranking" and then shows indicative values there. The practical effect is small because every missing (configuration, leaf) pair is already searched (Cohort bullet 3), but "gets no score" reads against the indicative value shown beside the ranking. Change: "gets no ranked value score in that ranking (an indicative value may be shown beside it, E259)", and tie E240 to "every configuration listed beside a ranking".

## 2. Methodology design recommendations

1. Generate every "today" figure in the prose from `scores.json` at build time, with a lint over the draft or README text. Every figure I checked other than the M1 triple matched the data, which shows the hand-maintained text is close. M1 shows the remaining risk is transcription order. Priority: highest, cheap, and it would have prevented M1 and I33 L4.
2. Add the ordering assertion from M1 to the active-rules manifest as a fixture: "printed bar triples are lower ≤ headline ≤ upper".
3. Keep the E259 indicative-value rows in a machine-readable table with columns (configuration, ranking, leaves present, coverage, workload ID, anchors, API value, Plan value, Plan route kind). The Plan route kind column (measured / transfer / O46 ceiling / API fallback) answers L3 without prose.
4. When the one-row-per-family diagnostic is next extended, publish the rebuilt ladder with its setter configurations (the data already carry `levelConfiguration`), so a reader can see that the AI Coding Daily lower bar moves from GPT-6 Luna (xhigh) to GPT-6 Luna (max).

## 3. Questions for the owner

None.

## 4. Verdict

VERDICT: HAS FEEDBACK
