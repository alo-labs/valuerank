# Internal review I18 — Claude Sonnet 5.5, effort low, on draft r77

(Saved from the subagent's report; the reviewer read all 963 folded lines.)

## 0. Read check
First line: "# ValueRank methodology — draft r77"
Last 12 words of the last line: "covers two-thirds of cohort rows jointly with the admitted components (E95, E101)." The last line is the Known limitations text at draft lines 962–963. I read all 963 lines in three chunks.

## 1. Findings by severity

**Critical**
None.

**High**
None.

**Medium**

M1. The Terminal-Bench leaf selection rule leaves ties undefined (quality table, TB row; ledger item "Terminal-Bench agent order stated").
- The draft says: "Terminus 2, then mini-SWE-agent, then OpenHands, then any other agent by name — never best-of-agent".
- Two faithful implementations can disagree in two places.
  - "By name" does not say whether the order is lexicographic or case-sensitive, nor whether agent versions or aliases count as the same agent.
  - The draft does not say how to choose between several leaderboard submissions for the same model, effort and agent. These can differ by date, trial count or agent version. Bug Hunt has E206 for exactly this problem; Terminal-Bench has nothing.
- I checked the code, which I was not asked to review, only to see whether the rule is executable. `select_tb4_row` in `/home/user/valuerank/valuerank/exact_match.py` (around line 104) ends in `min(candidates, key=(rank, agent))`. When two rows share the same agent, that returns whichever row comes first in the input list. I did not confirm that `/home/user/valuerank/data/tb4.json` currently contains such duplicates.
- Why it matters: this leaf carries 10% of quality and is the one "independent" leaf besides Bug Hunt. A silent choice between submissions changes scores.
- Recommendation: add an E206-style record rule for Terminal-Bench.
  1. Within the chosen agent, take the submission with the most trials, then the latest submission date, then the submission ID.
  2. Define "by name" as ascending Unicode code-point order of the agent string.
  3. Make the build fail when two rows tie on all keys without a recorded selection reason.
  4. Publish the chosen row's submission ID, date and trial count in the manifest.

M2. "Provisional" has two meanings, which makes bar-population membership ambiguous (E222 against the Missing data rule and the Counts paragraph).
- Missing data defines provisional by coverage: coverage under 70%, fewer than 2 SWE leaves, observed SWE weight under 40, or DeepSWE missing.
- E222 says a valuation-basis-unverified row with FullCost "enters R_W at its published point, flagged provisional", so that it can deny a label.
- The bar population is "non-provisional cohort rows with a displayed quality", and UniqueLabelEligible uses ¬provisional.
- An implementation can therefore read E222 two ways. The row may be provisional only for label purposes, or it may leave the bar population and the ladder. The second reading would move the quantile positions.
- The draft's own counts show the exposure: "17 rows reach" the bar against bar currency's "18 of 35" (E203, E207).
- Today the row (Claude Fable 5.1) lacks FullCost, so no number changes. The ambiguity becomes live as soon as a price record is fixed.
- Recommendation: do not reuse the word. Add a separate predicate, `LabelDenied(i)`, for E222 and E170 outcome 4.
  - Define UniqueLabelEligible = ¬provisional ∧ ¬LabelDenied.
  - Keep provisional strictly coverage-defined.
  - State that the bar population ignores LabelDenied.

M3. Report-age and expiry stages do not say whether "days old" uses calendar-date or timestamp arithmetic (E151, E212, Governance).
- Only the O32 window is stated as UTC calendar dates, with "date(V) − 30 days ≤ d ≤ date(V)".
- The age stages say "more than 30 days old" and "more than 90 days old" without that convention.
- The observation date is a date. V is a timestamp, for example 05:24:16Z.
- A measurement dated exactly 30 days before V is 30 days old by calendar date but 30 days 5 hours old by timestamp, so the "possibly superseded" and grace boundaries differ by a day between implementations.
- The draft argues counting reports never reach an age stage. Controlled measurements and transfers do, and those include every current SemiAnalysis route.
- Recommendation: state that every E151/E212/O13 age is `date(V) − E194 date` in whole UTC calendar days, with the same inclusive/strict convention as the window.
  - Add boundary fixtures at ages 30, 31, 90, 91, 120 and 121.

**Low**

L1. The "closed window, both end days included" claim and the "preceding month" mapping rest on an editor reading (E194, E213).
- AGENTS.md says "the preceding month". A 31-day closed interval [V−30, V] is longer than 30 days.
- It is a defensible choice, and the draft states it exactly.
- Recommendation: say once in the summary that the window spans 31 calendar dates, so a reader does not read it as 30 days.

L2. The headline "ladder minimum" and cohort counts are repeated in four places (Outputs 3, Counts, E205, E207) with slightly different framings, for example 48.1 against 48.06.
- Not a defect today. It is a maintenance risk: any re-freeze must update four passages.
- Recommendation: generate these figures from the manifest, as E155 does for uncertainty descriptions, and lint the prose against them.

## 2. Methodology design recommendations (prioritised)

1. **Make the headline bar result honest about what it can confirm.**
   - E201b shows that a confirmed qualification at coverage p needs displayed quality of at least H/p.
   - Today 5 rows are confirmed against 21 possible, and no bar has a confirmed cheapest under either bound.
   - Publish, beside the full-cohort result, a "full-coverage subset" result: the bar tested only among rows with p = 1.
   - Under O25 this needs no new evidence, only a new declared panel.
   - It would give readers a usable cheapest-above-bar answer where one exists, while the interval labels stay unchanged.
   - Related existing material: E221 (what each open row would need) and E219 (observed-range sensitivity).

2. **Split label eligibility from provisional status.** This is the fix for M2. The same predicate should govern E92, E186, E201 and E222.

3. **Add a one-line registry rule for third-party leaderboard record selection.** It should be generic: Terminal-Bench now, any future leaf later.
   - Rule: largest sample, then latest date, then ID, with a build failure on an unrecorded tie.
   - Reuse E206's wording so the two leaves stay symmetric.

4. **Add a reader-facing generated "what the numbers do and do not support" block.** It would appear above the first table.
   - Contents: the Plan basis is exploratory, no Plan claim is supported, the nominal 25% against cost's 47% (API) / 61% (Plan) variance allocation, confirmed against possible qualifier counts, and the share of cohort rows that exist only through Bug Hunt retention (27 of 37).
   - Most of this is already computed, so it is a presentation gap.

5. **Owner decision challenge (E163 and O33).** 27 of 37 cohort rows, about 73%, exist only because a single-maintainer, two-repository benchmark (Bug Hunt) covers them. These rows also set the anchors and the quartile ladder.
   - E199 and E205 already publish diagnostics showing the effect (Plan upper anchor $13,400 against $7,257; exchange rate 2.74 against 3.04).
   - Because the cohort rule is fixed policy, I only suggest promoting one of those two diagnostics to a second, equally prominent column in the headline table. It would not be a primary ranking.

## 3. Questions for the owner
1. If a Terminal-Bench leaderboard has several submissions for the same model, effort and agent, do you prefer the latest, the largest trial count, or the best? I recommend largest trial count, then latest, which matches your Bug Hunt rule.
2. Should a valuation-basis-unverified row (E222) stay in the bar population and ladder while being denied labels? I assume yes. Please confirm.

## 4. Verdict
VERDICT: HAS FEEDBACK
