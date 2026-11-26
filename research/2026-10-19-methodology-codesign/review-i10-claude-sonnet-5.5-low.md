# Internal review I10 — Claude Sonnet 5.5, effort low, on draft r69

(Saved from the subagent's report; the reviewer read all 877 folded lines.)

## 0. Read check
First line: `# ValueRank methodology — draft r69`

The last line of the file (line 877) is only `(E95, E101).` The last 12 words of the final sentence are: "covers two-thirds of ranked rows jointly with the admitted components (E95, E101)."

I read all 877 lines and the brief. I also read the ledger sections that bear on each point below, plus `valuerank/basket.py`. I ran no web searches. The sources the draft rests on (AA pages, SemiAnalysis, tbench.ai, Bug Hunt) are dated October 2026 and I could not check them against public indexes. I checked the arithmetic and statistics myself and found them sound. That covers the Clopper–Pearson endpoints, ladder positions and bar-reach counts (18/27/10 of 35), Omniscience vectors, rank-difference formula, exchange-rate formula, Fable's 1.0%, the 33-row panel arithmetic and the interval-solver fixtures.

## 1. Findings by severity

**Critical**

None

**High**

**H1. Nothing bounds the age of the chart capture that defines the cohort.**
- Where: the Source contract says the AA chart was "captured 2026-10-17". Governance says "Freshness: AA cost snapshot and price list max age 45 days … monthly cadence".
- The ledger shows 45-day freshness decided for cost only (line 101). The build checks in E195, E204 and the roster check test a capture's internal consistency, not whether it is current.
- Why it hurts: AGENTS.md's first rule is that every Pareto and near-Pareto model is included and that frontier entrants are reconciled on each routine refresh. A release built on a chart up to 45 days old can silently omit a new entrant, and every check in the draft would still pass.
- Today's practice (a 4-day gap between capture and release) hides this.
- Change:
  - Register a maximum age for the chart and catalog capture relative to the release cutoff, for example 7 days. The build should fail if the capture is older.
  - Publish an entrant and exit diff against the previous release: plotted points, rendered-frontier vertices and the near set.
  - Require a dated roster decision for any near-frontier family that is deferred.

**Medium**

**M1. The evidence lifecycle is spread over four places and its middle stage has no stated effect.**
- Where: Governance ("30-day soft expiry with change detection … 90-day hard expiry … further 30-day grace"), the capacity section ("A schema change triggers the 30-day soft expiry"), E151/E142/E144, and O13.
- Problems:
  - "Soft expiry" is defined as event-triggered change detection (flag "possibly superseded"), but the wording reads as an age rule. "Triggers the 30-day soft expiry" has no defined meaning.
  - The draft never says what the "possibly superseded" stage does to selection. It could be a flag only, a comparator penalty, or a loss of interval eligibility.
  - The partition stage, "most advanced contributor stage", is used without a stage-to-effect map. The ledger (line 946) confirms that for reports only this stage is reachable under O32.
  - Two faithful builds can therefore rank a flagged route differently.
- Change: add one lifecycle table with these columns: stage (current, possibly superseded, expired within grace, demoted), trigger, effect on the official displayed score, effect on route comparison, effect on interval eligibility, and the published label. Replace "30-day soft expiry" with "change-detection stage".

**M2. The Index reconciliation tolerance is hard-coded and contradicts nearby text.**
- Where: E37/E209 ("at source precision (relative error at most 10⁻⁶)"); the Accounting identities passage ("decomposes exactly … verified to < 0.002% for every row").
- Code check: `basket.py:92` uses a fixed `<= 1e-6`, although the docstring says "source precision".
- Problems:
  - 0.002% is 2×10⁻⁵, twenty times the gate. "Exactly" and "<0.002%" are stale next to the gate.
  - A fixed 10⁻⁶ is tighter than rounding allows for any cheap model with rounded published fields. A $10.63 total rounded to the cent already carries about 5×10⁻⁴ relative uncertainty. Such a row would flip to "unresolved" on rounding alone, which silently removes it from P_K, the anchors and the interval outputs.
  - The E37 sentence lists two statuses, but E209 defines four.
- Change: define the test as |Σ(cost per task × tasks) − published total| ≤ the propagated half-unit-in-last-place of every published field involved, floored at 10⁻⁶ of the total. Delete "exactly" and "<0.002%", or restate them as "within rounding". List all four statuses in E37.

**M3. Normative rules sit inside nested parentheticals.**
- Where: the Report set (E107) passage. The E194 window, O32, E201a and their fixtures are inside "inclusion rules (…)", which is inside "a pre-registered discovery procedure (…) … inclusion rules (… report window (E194) … Fixtures: …) and exclusion reason codes". The E151 clock note is also a long parenthetical.
- Why it hurts: the preface says tagged rules are normative wherever they appear. Parsing the parentheses still lets an implementer attach the window, the date rule or the straddling rule to the wrong object. The build-failure sentence ("The build fails when a newly admitted report is dated outside the window") sits in the middle of a clause.
- Change: lift the report window, report date, straddling, O32 count rule and fixtures into their own bullet, with one rule per sentence.

**Low**

**L1. The quality normalisation rule and the leaf table disagree.**
- The text says "a_low = chance/baseline level; a_high = documented ceiling … else 100%". The table sets 0–100 for most leaves and 0–105 for Bug Hunt.
- The table sits outside "Normative definitions", so the preface's precedence does not settle it.
- Change: say the table's anchors are the frozen ones and drop the chance-level wording, or add a per-leaf a_low and a_high column.

**L2. Notation clash.** Q̄_i is a row's displayed quality, and Q̄ is the frozen bar level. Both appear in the same formulas (for example "Q̄ = 58.28" and "Q̄_i, observed leaves renormalised"). Rename the bar level, for example B_k.

## 2. Methodology design recommendations

**R1 (priority 1). Add a distribution-free two-sided bound on M_W from category mixes alone.**

Problem: every Plan route is "unidentified" today, so Plan frontier and bar outputs are unevaluable. The ledger records the claim that "M_W needs category-specific burn evidence … which no public source provides". But the draft's own additive-capacity model supports a bound with no burn data.

Derivation:
- Let x be the measured category-token vector at saturation and u the basket's per-pass category vector. Let the burn rates a_k ≥ 0 be unknown.
- Let ρ_k = x_k/u_k, taken over categories with u_k > 0.
- For the binding pool at measurement, λ_W = (a·x)/(a·u) ∈ [ρ_min, ρ_max].
- The valuation factor (p·u)/(p·x) ∈ [1/ρ_max, 1/ρ_min].
- Therefore M_W ∈ M_obs × [ρ_min/ρ_max, ρ_max/ρ_min].
- With several pools, λ_W ≥ ρ_min × λ_x holds for every pool, because the measured capacity is the minimum over pools. The upper bound holds through the pool that bound at measurement.

What it needs:
- Public inputs only. SemiAnalysis already reports a cache-heavy mix.
- AA's set-identified region D_iW. Take the worst case over D_iW, which is a small linear-fractional problem.
- A controlled saturation measurement, so that capacity is established.
- Additive token meters. The draft already assumes these for its capacity formula.
- x_k > 0 wherever u_k > 0. Otherwise the lower bound is zero-inclusive and the route stays unidentified under E67.

Why it is allowed: it uses no analyst assumption, so it is consistent with O19. It is a strictly positive, finite interval, so under E67 it is "set-identified, mechanism: category-mix bound".

Expected effect:
- The interval will probably be wide (my rough estimate is a factor of several each way, not computed from the data).
- It would still turn "unevaluable" into honest possible-frontier and possible-qualifier sets.
- It would let the Plan interval outputs say something while the "exploratory" label stays until half the rows qualify.
- It does not apply to owner-named transfers (still "never identifies M_W").

I could not confirm that the ledger considered and rejected this. I searched for related terms and found nothing.

**R2. Publish a frontier entrant and exit diff each release** (see H1). Include a "chart capture age" line in the active-rules manifest.

**R3. Add a one-page evidence-lifecycle table** (see M1). Reuse it in the Plan headline footnote so readers can see which stage each route is in.

## 3. Questions for the owner
1. Is a wide, positive two-sided category-mix bound (R1) acceptable as "set-identified" under E67, given that it carries no burn evidence? If not, should it be published only as a diagnostic?
2. What maximum age do you want for the chart and catalog capture at release cutoff (H1)? I suggested 7 days.

## 4. Verdict
VERDICT: HAS FEEDBACK
