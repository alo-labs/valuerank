# Internal review I17 — Claude Sonnet 5.5, effort low, on draft r76

(Saved from the subagent's report; the reviewer read all 956 folded lines.)

## 0. Read check
First line: "# ValueRank methodology — draft r76".
The last line of the folded copy is only "(E95, E101)." The last 12 words of the final sentence are: "covers two-thirds of cohort rows jointly with the admitted components (E95, E101)."
I read all 956 lines, in three chunks, and the ledger-brief before them.

I did not use web search. The draft's sources are dated 2026-10 and I could not verify them externally. I checked internal arithmetic and the ledger instead. These all hold:
- Ladder positions for n = 35, and the 18 / 27 / 10 reach counts.
- The cohort population counts (37, 36, 35, 33, 34).
- The ⌈n/2⌉ identity for the headline bar.
- The per-look error δ = 0.05/16 and the closed-form Clopper–Pearson endpoints.
- The anchor exchange rates, 2.74 and 1.73 per cost doubling, from the stated anchors.
- The 91.5% uniform / 86.7% arcsine fixture (I re-simulated the arcsine case: 0.868).
- The token identity 13,409,872 + 24,491,270 = 37,901,142.
- Fable 5.1's 1.0% cost discrepancy.
- The 3.4-day and 37-minute capture gaps.

## 1. Findings by severity

**Critical**
None.

**High**
None.

**Medium**

M1. Independence is defined with an unexplained and under-specified time gap (Plan evidence section, "Independence = distinct observers, measurement periods at least 7 days apart and no shared upstream source").
- Defect: independence is about observers and sources, not calendar spacing. Two different users measuring in the same week are independent. The draft gives no rationale for the 7-day gap, and AGENTS.md does not ask for it.
- Ambiguity: "measurement periods" is not tied to E194's observation date. Two implementations can disagree on whether overlapping windows, or a window start against a window end, count as "apart".
- Why it hurts: together with E102's comparability requirements and O32's 30-day window, this shrinks the set of report pairs that can ever reach O11's two-source minimum. That quietly makes the report route harder than O11's wording ("≥2 independent concordant reports") requires.
- The ledger records "Report independence definition" as adopted early. I found no argument for the 7 days. That absence is what is new here.
- Change: define independence as distinct observers and no shared upstream post, thread or derivation. Either drop the day gap or define it on the two E194 observation dates (|d₁ − d₂| ≥ 7, calendar days, UTC). Add a fixture: two reports on the same day by different users are independent.

M2. Bug Hunt harness selection has no same-harness diagnostic, unlike Terminal-Bench (quality table and E206 against E125).
- Defect: E206 selects the largest-N mean over every harness and route. How many runs the maintainer happened to do has nothing to do with model quality, so different models end up scored on different CLIs. The draft calls Bug Hunt "model plus harness" (E29). The Terminal-Bench leaf gets a same-harness variant and τ_b (E125), but the Bug Hunt leaf gets only an S2 band borrowed from tbench.ai spreads (E19).
- Why it hurts: Bug Hunt is 10% of quality and carries retention for 27 of 37 rows. A vendor-CLI advantage, such as a model run in its own vendor CLI against one run in a third-party CLI, can move ranks without any diagnostic showing it.
- Change: publish, beside the leaf, a restricted Bug Hunt variant on one declared harness policy. For example, use each family's vendor-native CLI, or the CLI that covers the most roster models, with other rows missing in the variant. Add τ_b against the primary leaf on the common panel and a "harness-mixed" mark per row, as E125 does. It is diagnostic only and changes no score. It needs only the owner's public scoreboard.

**Low**

L1. Weight units are inconsistent (Normative definitions, "Coverage and scores", against E221 and the SWE rule).
- The full-composite Q_i(θ) = Σ w z + Σ w u gives a 0–100 score only if the w sum to 1. E221 writes u* = (100·H − Σ w z) / Σ_missing w, which only works if the w are percent points summing to 100. The code (`valuerank/value_v3.py`, `required_missing_score`) uses the percent convention. The provisional rule ("≥ 40 of the 100 quality points") and E178 ("retained 86.7%") also use percent.
- Change: state once that w_b are percent points summing to 100 and that Q = Σ w z / 100. Or move everything to fractions. Add a unit fixture.

L2. Report-window boundary mixes a timestamp and a date (E194 / E213).
- The text says "[V − 30 days, V]" with V = 2026-10-21T05:24:16Z, but also calls it a "closed day interval". Observation dates are often date-only, and no time zone is stated.
- A report dated 2026-09-21 is in or out depending on whether it is compared as a date or as 00:00. A timestamped window end at 2026-09-21T03:00Z is out on a timestamp comparison but in on a date comparison.
- Change: state the comparison as UTC calendar dates, date(V) − 30 ≤ d ≤ date(V). Truncate any timestamped E194 date to its UTC date. Add boundary fixtures for both forms.

L3. Panels for leaf-level SD are not declared (quality section, "non-discriminating").
- E180 requires a declared panel for every cohort SD. But "a leaf with cohort SD(z) < 3 points" does not say whether the panel is each leaf's observed rows or the common complete panel I used by the drift flag. The set B* depends on the choice, so drift flags can differ between implementations.
- Separately, "S_Q" in Outputs item 1 is never defined. The text uses Q̄_i, Q and S_Q interchangeably.
- Change: name the panel for the non-discriminating test, and define S_Q ≡ Q̄_i on the common-workload panel, or replace it with the defined symbol.

## 2. Methodology design recommendations
1. (From M2.) Add the Bug Hunt same-harness diagnostic. This is the only recommendation that adds information. It is cheap, public and routinely refreshable.
2. (From M1, L1–L3.) Make a spec-hygiene pass in r77. Apply the independence definition, the unit statement, the UTC-date window and the leaf-SD panel as release-test fixtures. These are small edits that remove real disagreement between implementations.

## 3. Questions for the owner
None.

## 4. Verdict
VERDICT: HAS FEEDBACK
