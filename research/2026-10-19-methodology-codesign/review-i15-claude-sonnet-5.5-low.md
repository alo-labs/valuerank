# Internal review I15 — Claude Sonnet 5.5, effort low, on draft r74

(Saved from the subagent's report; the reviewer read all 935 folded lines.)

## 0. Read check
First line: `# ValueRank methodology — draft r74`
Last line of the folded file (935): `(E95, E101).` The last 12 words of the final paragraph are: "covers two-thirds of ranked rows jointly with the admitted components (E95, E101)."

I read the ledger brief and all 935 lines. I did not use web search or read the code. The factual claims I checked are internal: the ladder positions for n=35, the Omniscience and Bug Hunt test vectors, the admission-enumeration fixtures, the exchange-rate algebra, the Clopper–Pearson endpoints, and the capture-age arithmetic (37 minutes, 3.4 days). All of these are correct. I also cross-checked the draft against AGENTS.md. I found no point where the draft contradicts a binding owner decision.

## 1. Findings by severity

**Critical**
None.

**High**
None.

**Medium**

M1. The report-date and report-age rules contradict each other, and one clock path cannot be reached.
- Passages: the E151 parenthesis ("a report partition reaches the 90-day expiry only through a report whose own measurement window ended long before its report date and could not be split") and the Report window paragraph ("A report's date is its measurement window's end, else its report date, else its publication date").
- Other formulations of the same date:
  - E151: "its measurement window's end, else its report date; an undated report ages with the route".
  - E144: "measurement window's end, else the source publication date".
- Problems:
  1. Under the window paragraph, an in-window report has a date (its window end) no more than 30 days before V. Its age is therefore never "more than 30 days", so the "possibly superseded" stage can only be reached by change detection. The expiry path described in E151 cannot be reached by any report. A straddling report counts "by its end date", so the "window ended long before its report date" case is out of window by construction.
  2. An undated report "ages with the route" (E151), but the build must fail on a "newly admitted report dated outside the window". An undated report has no date to test. Two implementations will disagree on whether it counts toward O11.
- Why it matters: this is the O32 gate that decides whether a report route reaches two concordant sources. Different readings change which Plan routes are scored.
- Change:
  1. Define one observation date: window end, else report date, else publication date.
  2. Say that a report with none of these is diagnostic-only and never counts toward O11.
  3. Delete the E151 parenthesis about reports reaching expiry, or say that report partitions use only the change-detection stage.
  4. State that "more than 30 days old" is strict, and that the closed window spans 31 calendar days.

M2. The Index-reconstruction gate (E209) has an ambiguous tolerance, and the failure mode is large.
- Passage: "AA's ten evaluation costs reproduce its published Index total at source precision (relative error at most 10⁻⁶)".
- Problem: "At source precision" and a fixed 10⁻⁶ are two different tests. If AA's page ever rounds, say to cents, a sum of ten rounded costs on a $13,000 total can miss by more than 10⁻⁶ relative (about 0.013) with no real inconsistency. Every row would then become "unresolved" at once. The seven Index components would fail K, the admission panel would collapse below ⌈2N/3⌉, and the basket would be re-enumerated. The draft does not say whether this holds the release.
- Change: define the tolerance as the sum of the half-units of the published digits of the eleven numbers, plus a floating-point epsilon. State that a gate failing for more than 10% of rows is reported as "source precision changed" and treated as a versioned AA field change, not as eleven or more per-row inconsistencies. Today's Fable 5.1 failure (1.0%) would still fail under this definition.

M3. Owner decision challenge (O4/O7/O35). The Claude transfers ignore the model-price asymmetry that makes them least reliable for the cheapest models.
- Argument: a Value Multiple is API-priced usage divided by the fee. If a plan's allowance is token- or compute-weighted, as the draft treats pool and burn coefficients, the API-priced multiple scales with the model's price per token. If the allowance is instead cost-weighted, the multiple does not scale. Applying Opus 5.5's 57–59x to Haiku 5.5 or Sonnet 5.5 therefore has a systematic direction of error, and it favours exactly the cheap configurations that win the value ranking.
- What the draft has: O35 rules out the Fable gauge. The draft also mentions a "directional bias bound" for different burn coefficients but supplies none.
- Change: keep the label, and add a named S2 stress branch for the Claude transfers. It scales the transferred multiple by the ratio of the configuration's price to the donor's price, taken on the basket's demand region. Publish it as sensitivity only (O19: never in Θ). This is implementable from public rate cards and does not use Fable. The Plan headline then shows how much of a cheap Claude model's Plan lead depends on a cost-weighted-allowance assumption.

M4. The bar level and the qualification test live on different quality scales (E198b, E201b, E207).
- Facts: H is a quantile of displayed quality, which is observed-only and renormalised. Qualification tests the full composite, with missing leaves anywhere in 0–100 and at 0 in the lower bound. The draft reports 18 rows reach the headline bar (E207), 21 can possibly qualify and 5 are confirmed. No bar has a confirmed cheapest.
- Effect: the headline "cheapest above a bar" output is structurally unable to return a confirmed answer today. The bar is a level on a scale (partial-coverage rows renormalised upward) that the test then judges on a stricter scale.
- This is partly acknowledged by E198b and E201b. The new argument is that the scale mismatch is the cause of the vacuity, not just an effect of missing evidence. A frozen level only means something if the thing it is compared with is on the same scale.
- Change: see Recommendation 1.

**Low**

L1. The tie-break "the later-numbered record governs an unamended conflict" is arbitrary. Numbers record authoring order, not scope. A later narrow editor record such as E220 could override an earlier broader rule without anyone noticing. E191 also does not say what happens when an editor record amends an owner decision.
- Change: say that an editor record never amends or overrides an owner decision. Replace the numeric tie-break with a conflict register, so a conflict is a build-checked defect that holds the release until the owner or editor records a resolution.

L2. The mixed-model report rule in AGENTS.md ("Keep mixed-model or unidentified use at provider/plan level; do not transfer it to a specific ValueRank model") is only implicit, under Plan admission case 1. Add one sentence to E107's inclusion rules: a report that does not name the exact model and effort is excluded from every model route and kept only as a provider- and plan-level diagnostic.

L3. The AGENTS.md reconciliation inventory must retain "direct owner links" and "observation dates" for every catalog model. The draft states them for Bug Hunt records and for evidence-bundle artifacts. It does not say that unscored rows in the inventory carry the owner link and observation date. Add that statement to the cohort capture paragraph.

L4. The E37 "Cost completeness" sentence (lines 173–177) is garbled. It has a dangling "(e.g. the '*' declined-tasks marker…)" and refers twice to "the four of E209 below". This is editorial, but the passage is normative for completeness. Rewrite it as a single pointer to the E209 status scale.

## 2. Methodology design recommendations (prioritised)

1. Put the bar on the scale it is tested on, and publish what would settle each candidate.
   - Freeze H as the lower-median of full-composite quality at the observed-leaf point value, over the non-provisional rows with full coverage, where displayed and full-composite quality coincide. Alternatively keep the current H and add a second, full-coverage bar.
   - For each row that possibly but not confirmedly qualifies, publish the required mean score on its missing leaves: u* = (H − Σ_obs w z) / Σ_missing w. Also publish the observed cohort range and median for those leaves.
   - Effect: "cheapest above the bar" gets an answer even when it cannot be confirmed. A reader sees which cheaper rows need only a modest score on one missing leaf. This uses only published data, never enters Θ or a label, and is a parameter-free alternative to the E219 observed-range sensitivity. It respects O25, O19 and exact-variant evidence.
2. Fix the report-date lifecycle (M1) and the reconstruction tolerance (M2). These change which routes and rows are scored.
3. Add the price-ratio stress for transferred Claude multiples (M3).
4. Publish a cohort-composition note beside the headline bar and ladder. O33 means effort multiplicity drives the median: the one-row-per-family diagnostic moves the headline from 56.7 to 58.3 and the cost exchange rate from 2.74 to 3.04. The draft already publishes the numbers (E205). Add the one-line reading "the headline bar is a median over configurations, not families".

## 3. Questions for the owner
1. Is the cost-weighted-allowance assumption behind the Claude transfers intended? If allowance burn is proportional to API price, the transfers are about right for cheaper Claude models. If it is token-weighted, they are inflated for the cheap ones (M3).
2. Should a "required missing-leaf score" table (Recommendation 1) appear in the public summary as a non-claim diagnostic, beside the displayed-record cheapest?
3. Should an undated end-user report be diagnostic-only (M1)? Or should it count by its publication date, which is what the window paragraph says?

## 4. Verdict
VERDICT: HAS FEEDBACK
