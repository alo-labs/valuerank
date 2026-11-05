# Internal review I43 — Claude Sonnet 5.5 (effort high) on draft r101

## 0. Read check

- First line of the draft: "# ValueRank methodology — draft r101"
- Last line of the draft (folded line 950): "noise, renders every current figure from the build and checks it, moves this history below the body and splits Output 1. Every change is recorded with its rationale in the ledger."
- Last 12 words of the last paragraph: "Output 1. Every change is recorded with its rationale in the ledger."
- Also read: the whole folded draft (lines 1–950, in chunks); `reviewer-prompt.md`; `ledger-brief.md`; `ledger.md` from "## Internal review I28" (line 1170) to the end (O45–O62, E247–E265, I28–I42); `AGENTS.md` (project rules); and the source `draft-r101.src.md` for the placeholders.
- Checked against repository data and code: `data/scores.json` (both rankings' leaf tables and `track.leaves`, `barPolicy.bars`, `gates`, `diagnostics.rankSeparability`, `sourceClocks`, `measuredOnlyPlanView`, per-row leaf z values), `data/aa_frontier_capture.json` (cohort and near-gap recomputation: 18 frontier, 11 near, first vertex GPT-6 Luna (low) at 10.63 equal to the cheapest of 189 points), `valuerank/quality.py`, `valuerank/draft_figures.py` (the lint), and `python3 -m valuerank.draft_figures check` (passes, rc 0).
- Verified as correct and not raised: the ladder positions and fixtures (n = 9, 15, 32), the exchange rate and its offset (3.04 / 4.06 = 0.75), the transfer tolerance arithmetic (2^(2.87 / 2.44) = 2.26), leaf weights sum to 100 in both rankings (max-effort 60 + 40; Coding Daily 60 + 40), the 66% / 34% and 78% / 22% source splits, the 86.7% basket-scope retention, the admission fixtures, 4 against 5 and 7 against 8 qualifier counts, the cohort counts 29 / 18 / 11 / 12 / 7 / 5, and the source-clock arithmetic (O59, O60).

## 1. Findings by severity

**Critical**

None.

**High**

None.

**Medium**

**M1. "The max-effort ranking has 14 leaves" is wrong; it has 13 (location: "Leaf sets per ranking" paragraph, folded line 429; source line 69).**
Issue: O61 replaced LiveBench's two categories (Long Agentic, Coding) with one leaf, LiveBench 2.0 Overall, so the max-effort leaf table has six software-engineering leaves (FrontierCode, Terminal-Bench, Bug Hunt, Vibe Code, Code Migration, LiveBench Overall) plus seven common leaves = 13. `data/scores.json` `v3.track.leaves` has 13 entries; the leaf table in the draft itself lists 13 rows' worth of leaves (the HLE / SciCode / CritPt row is three). 14 is the pre-O61 count, and the sentence is a leftover from r100. The Coding Daily count of 11 is right.
Why it hurts: it is a stated figure that is wrong, in the paragraph that defines what each ranking is scored on, and two implementers counting leaves would disagree with the text.
Defect type: the figure is hard-coded in the source (not a placeholder), and the check missed it because the sentence neither says "today" nor carries an "N of M" count (`draft_figures.lint` only reads sentences with "today" and undated "N of M" counts). So it is a defect in the source and in the check.
Change: replace it with placeholders resolved from `len(quality.TRACKS[...])` for both rankings (for example `{{fig:max.leafN}}` and `{{fig:aicd.leafN}}`), and see Recommendation 1 for the lint extension.

**M2. The max-effort bar ladder in the re-freeze history (49.76 / 60.72 / 62.12) is stale and contradicts Output 3 (location: Quality / Cheapest-above-a-bar bullet "Ladder positions", folded lines 645–647; source line 119).**
Issue: the sentence "the max-effort ladder over 9 configurations is 49.76 (MiMo-V2.6-Pro), 60.72 (Gemini 4 Argon (high), headline) and 62.12 (GPT-6 Astra (max))" gives the pre-O61 levels. Output 3 (folded line 58), `data/scores.json` `v3.barPolicy.bars` and the ledger's own E265 sweep note give 54.23 (MiMo-V2.6-Pro, lower quartile), 64.26 (Gemini 4 Argon (high), headline) and 65.00 (GPT-6 Astra (max), upper quartile). The setters are the same configurations; only the levels moved, because O61 changed the quality weights. E265 names exactly this change ("the bar ladder 49.8/60.7/62.1 → 54.2/64.3/65.0 … all are placeholders now"), so it was meant to be swept, but this sentence was missed. The Coding Daily ladder in the same sentence (38.00 / 49.24 / 57.16) is right.
Second part of the same defect: the sentence says E247's ladder "was replaced before any release" by the max-effort and Coding Daily ladders (E253), but the max-effort ladder was then replaced a second time by O61's reweighting, before any release and under the same anchor-version string. The draft never says that O61 re-froze the max-effort bars. A reader following the history from E247 to now cannot reproduce the sequence, and the frozen bar levels a reader would try to verify against `v3_frozen.json` do not match the quoted ones.
Why it hurts: the bars are a headline output, and the draft shows two different headline-bar ladders for the same ranking (64.3 in Output 3, 60.72 here).
Defect type: hard-coded in the source; the check skipped it because the sentence is dated ("At the 2026-10-23 re-freezes"), and the lint treats dated sentences as history, but this one describes the frozen state of the current anchor version, not a past draft.
Change: render the three levels and setters with placeholders (`{{max:barPolicy.bars…}}`), and add "O61 then reweighted the max-effort leaves and re-froze its bars on the same anchor version, before any release; the cost anchors were unchanged." Alternatively delete the digits and point to scores.json `barPolicy`.

**M3. LiveBench 2.0 Overall and FrontierCode are both 15%, but the recorded O61 rule is that LiveBench outweighs every single AA leaf (location: leaf table, folded lines 435 and 446; no statement of the rule in the draft).**
Issue: the owner's reasoning for O61 is recorded as "LiveBench needs to get more % than AA Intelligence Score's % since LB is a non-contaminated benchmark whereas AA's benchmarks are mostly contaminated", and the option the owner chose is "LB above each AA leaf" (ledger O61: "above every single AA leaf"). AGENTS.md (binding) says LiveBench "outweighs every single AA leaf"; `quality.py` and `emit_docs.py` repeat "weighted above every single AA leaf" / "more weight than any single AA leaf". The weights recorded under O61 give FrontierCode 15 and LiveBench Overall 15. FrontierCode 1.1 is an AA-run leaf (the draft's own 66% AA-run split lists it, and the leaf table says "AA's run, then Cognition's"). So LiveBench ties the largest AA leaf instead of exceeding it. The draft itself states no inequality, so it is internally consistent, but it carries weights that do not satisfy the rule AGENTS.md and the ledger attach to those weights.
Why it hurts: two faithful implementers reading AGENTS.md and the draft would resolve it differently (change a weight, or read "outweighs" as "at least as much as"). The effect on results is small: recomputing the max-effort API value from `scores.json` with FrontierCode 14 and LiveBench 16 (cost scores, anchors and every other weight fixed) leaves all nine ranks unchanged, but values and the three frozen bars would move slightly, so the choice is not cosmetic for a frozen release.
Change: this needs an owner answer (Question 1). Until then, state the tie in the leaf table note ("LiveBench equals FrontierCode, the largest AA leaf; owner decision O61 asked for more than any AA leaf — pending") so a reader is not misled, and do not change weights unilaterally.

**Low**

**L1. The "every current-release figure is a placeholder" claim is broader than the check (location: Governance, "Figures in this specification (E265)", folded lines 825–829; ledger E265).** The sentence says every current-release figure the document quotes is a placeholder, and then describes the check accurately as covering "today" sentences and undated "N of M" counts. Several current-state statements remain hard-coded and outside the lint: M1 and M2 above; the Plan calibration sentence for the Coding Daily ranking (Claude Haiku 5.5 (medium) on Claude Pro, Gemini 4 Argon (high) on API fallback, folded lines 373–374; correct today); the confirmed / possible qualifier counts 4 against 5 and 7 against 8 and the bar setters (folded line 674; correct today); the cohort counts 29, 18, 11, 12, 7, 5 (folded lines 84–85; correct today); and "189 plotted points … $10.63" (folded line 759; correct today). Change: weaken the sentence to what the check enforces, and extend the lint (Recommendation 1).

**L2. Output 1's split put a Cost-weight sentence inside the Noise-band bullet (location: folded lines 38–41).** After "The ordinal ranks stay … labelled with the independent-task approximation …", the same bullet continues "Two named quantities are printed per basis: (a) the anchor exchange rate … (b) the within-cohort influence …". That text is about cost-weight disclosure and is repeated in the Cost-weight disclosure (E60) bullet (folded line 55) and the Dispersion bullet. It reads as if the two quantities belong to the band rule. Change: move it to the E60 bullet.

**L3. E256's wording of LiveBench Overall's noise is ambiguous (location: Added leaves, folded line 470).** "takes the mean of its seven categories' binomial noise" can be read as the mean of seven SDs. The S1T paragraph (folded lines 515–517) and E264 mean the SD of the mean of seven binomial shares, (100/7) × √Σ p̃_c(1 − p̃_c)/n_c. Change: write the formula once in the draft (the ledger has it; the draft does not).

**L4. O55 is still cited as setting the max-effort weights (location: folded line 97 "owner-set weights (O55)"; line 427 heading "owner decisions O49, O52–O55"; line 428 "O55 sets each ranking's software-engineering weights").** For the max-effort ranking O61 replaced O55's weights (FrontierCode 18, Terminal-Bench 14, Bug Hunt 10, LiveBench Long Agentic 5 and Coding 2). Only the table row mentions O61. Change: cite "O55, as amended for the max-effort ranking by O61" in these three places and add O61 to the heading.

**L5. A hard-coded characterisation of Vibe Code Bench does not match the data (location: Known limitations, folded line 902).** "Vibe Code Bench v1.1 is saturated near its top, so it separates the max-effort rows little" — the nine z values run 81.6 to 92.4 with population SD 3.22, the same spread as FrontierCode (3.23) and above the 3-point non-discriminating line the draft defines (so it is not flagged). "Saturated" is too strong and "little" is untested. Change: say "ranges 81.6–92.4 (SD 3.2) on the leaf's anchors" via placeholders, or drop the sentence.

## 2. Methodology design recommendations

1. (Highest priority, removes M1, M2 and L1 as a class.) Close the lint gap with two cheap rules, not another editorial sweep: (a) in every sentence before the revision history, flag a bare integer or decimal within about 80 characters after "max-effort", "AI Coding Daily", "ranking", "leaves", "ladder" or "bar" unless it is a placeholder, an anchor-rule constant or a dated-as-history sentence; (b) treat a sentence dated 2026-10-23 or later that describes the current frozen state (re-freeze, capture, cutoff) as current, and allow history only for sentences that name a superseded version (for example "E247's" or "before O53"). Add the two counts (`len(TRACKS[k])` per ranking) and the three bar levels with setters to `data/figures.json` so the sentences can be placeholders. A fixture test should reproduce M1 and M2 as failing lines.
2. Resolve the LiveBench / FrontierCode tie with the owner (Question 1). If the owner wants a strict inequality, the smallest change is FrontierCode 14 and LiveBench 16 with software engineering still 60; my recomputation shows no rank change on the max-effort API basis. If the owner accepts the tie, change AGENTS.md's "outweighs" to "at least as much as any single AA leaf" and put the same wording in `quality.py` and `emit_docs.py`.
3. Add one sentence to the O61 history in the draft: O61 re-froze the max-effort bars on the unchanged anchor version, no release having been published, and the old and new ladders are kept in the research record. This is the same practice the draft already uses for the 2026-10-21 re-freezes.
4. State the S1T formula for LiveBench Overall in the draft once (L3), so the stream is reproducible from the draft alone.

## 3. Questions for the owner

1. O61 asked that LiveBench 2.0 Overall carry "more % than AA Intelligence Score's %" and the chosen option was "LB above each AA leaf", but the recorded weights give LiveBench 15% and FrontierCode (an AA-run leaf) 15%. Do you want LiveBench strictly above FrontierCode (for example LiveBench 16 and FrontierCode 14, software engineering still 60), or is the tie intended and the wording in AGENTS.md ("outweighs every single AA leaf") to be relaxed? The answer changes the max-effort quality weights, so it changes values and the three frozen bars.

## 4. Verdict

VERDICT: HAS FEEDBACK
