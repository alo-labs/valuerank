# Internal review I2 — Claude Sonnet 5.5, effort low, on draft r61

(Saved from the subagent's report; the reviewer read all 760 folded lines.)

## 0. Read check
- First line: `# ValueRank methodology — draft r61`
- Last 12 words of the last paragraph: "covers two-thirds of ranked rows jointly with the admitted components (E95, E101)." The folded file's physical line 760 is only "(E95, E101)." I read lines 1–760 in three chunks and the ledger brief. I also checked the full ledger by grep and read its Internal review I1 section.
- I ran no web search. The draft's AA, tbench and SemiAnalysis facts are dated 2026-10 and I could not check them against a public source, so I do not rule on them.
- I did check the arithmetic by hand and with a small Monte Carlo:
  - The arcsine fixture gives 86.66% (the draft says about 86.7%).
  - The uniform fixture gives 91.5%.
  - The E150/E77 confidence level and closed forms are right.
  - The weights sum to 100.
  - The 86.7% retained weight in the basket-scope branch is right.
  - The Omniscience vectors are right.
  - The admission fixtures are right.
  - The exchange-rate algebra is consistent with V = 0.25·S_C + 0.75·Q.

## 1. Findings by severity

**Critical**
None.

**High**

H1. The "cheapest above a bar" output is degenerate at freeze on the API basis.
- Passages: the E156 policy ("median-definite-frontier", v1), Confirmed cheapest (E38), K_r (E45), and the scenario-supported label.
- The bar reference r is a non-provisional member of the API main-workload definite frontier, and r always qualifies against itself and competes (r ∈ R_W).
- Suppose some i ≠ r were confirmed cheapest. Then Q_i ≥ Q_r and c_i < c_r in every θ ∈ Θ, so i dominates r everywhere. That contradicts r being definite-frontier.
- So at the freeze release, API confirmed-cheapest can only be r itself (or nothing, if a blocker is unresolved), and K_r contains only r plus exact duplicates.
- The scenario-supported label has the same problem. S1 draws come from Θ, so a ≥90% share of scenarios in which i beats r contradicts r being definite.
- The Plan basis is not degenerate in principle, but today it is empty (see M4).
- Why it hurts: one of the four headline outputs, "which model is cheapest above a quality bar", reports the bar-setter on the API basis. A reader takes this as a finding, but it follows from how the bar is built.
- Later releases can drift (a new entrant dominates r), but the output is uninformative at every freeze.
- Not in the ledger. I searched for median, tautology, trivial and "reference itself" and found nothing on this.
- Recommended change:
  1. Make the bar a quality level, not a frontier configuration. For example, Q_bar is the lower median of observed quality over all non-provisional ranked rows. Keep the existing reference-quality object (E52) and its interval and scenario treatment.
  2. If the owner wants a configuration as the bar, require the reference to be off the cost-quality frontier it is meant to test, such as a quality-percentile configuration chosen among non-frontier rows.
  3. In either case, add a release assertion "bar output is non-tautological": at freeze, the candidate set that can qualify must contain at least one row other than r.
  4. Do not change any published label wording until the bar is redefined.

**Medium**

M1. One configuration per family drops cheaper rendered-frontier points that AGENTS says to include.
- Passages: E188 and the Cohort bullet.
- AGENTS.md requires "every model represented on the frontier".
- E188 ranks only the highest-Index rendered-frontier point of a frontier family and publishes the rest as "alternatives".
- The highest-Index point is typically the most expensive effort, so for a ranking about lowest cost per value the rule systematically picks the worse-value point of a family.
- The term "family" is never defined.
  - Is it model name without effort, base model plus version, or provider line?
  - "Two MiMo rows" appear in the capture status although the retained list does not include MiMo and the rule gives one row per family.
  - Two implementations will disagree on cohort size.
- Recommended change, in two parts:
  - Add a normative family key, for example the AA model slug stripped of effort and fallback tokens, with fixtures including MiMo.
  - Either rank every rendered-frontier point, since the frontier is by definition efficient in Index-cost, or at least score each family's other frontier points on the frozen anchors in a published "alternatives" table.
  - Frozen anchors mean alternatives move nobody else's score. Rank rows stay as they are, so this alone is not an owner decision challenge. If "one row per family" is owner policy, it becomes an Owner decision challenge to that rule.

M2. The report-eligibility window is undefined.
- Passages: E107 ("report date within the window"), the Governance expiry rules, and AGENTS.md ("Use reports from the preceding month").
- The draft never states the window length or its anchor (the release cutoff, the discovery date, or the measurement-window end).
- The 30/90/+30-day expiry clocks (O13) are a separate thing and cannot stand in for the window.
- Why it hurts: whether a 60-day-old report is in E_r,t, and so whether concordance and ≥2-report admission pass, is implementation-dependent. This decides which Plan routes are official.
- Recommended change: add a rule such as "a report enters E_r,t if its measurement-window end (else its report date) lies in the 30 days before the release cutoff. Older reports stay as expired diagnostics under O13." Alternatively, state that O13's 90 days supersedes AGENTS' "preceding month" for already-admitted routes, and flag that as an owner decision.

M3. The way "AA's rendered Pareto line as observed" is captured is unspecified.
- Passages: the Source contract registry fields and the Cohort rule.
- Frontier membership is declared never recomputed. But the draft only records the chart identity and filters, not how a point's membership is read.
- Candidates are an AA data flag, the chart's SVG or path vertices, or a rendered-image trace.
- The difference matters for ties, for filter toggles that change the line (reasoning vs non-reasoning, open weights), and for the 3-point near rule, which uses F(c) over rendered-frontier points.
- Recommended change: add registry fields frontier_membership_source (data field or path vertex), the extractor version, a point-to-line tolerance, and a fixture that fails the build if the extracted line is not monotone non-dominated in (cost, Index). Add a reconciliation count (rendered vs extracted) per refresh.

M4. No Plan interval output exists today, and the draft does not give the Plan buyer a conditional alternative.
- Per the ledger brief, no Plan route has an identified M_W today. So R_W on the Plan basis is empty. The Plan frontier, bar and label outputs are all unevaluable.
- Disclosed ("exploratory" is structural), and withholding unidentified Plan scores was rejected. But the draft has no conditional output at all for the buyer type that ValueRank exists to serve separately.
- See recommendation 3 in section 2.

**Low**

L1. The "25% cost weight" label can mislead.
- The Outputs section does disclose the exchange rate and the SD ratio, and E189 adds the variance allocation.
- The brief's I1 numbers say cost carries about 80% of API value variance, the SD ratio is 55%, and the quality-only ordering has τ = 0.03 against the value ordering.
- The headline therefore reads "cost 25%" while cost decides most of the ordering. The 10%/90% flag does not fire in this case.
- Owner decision challenge: see section 2, item 4, and question Q1.

L2. The clip-gate "any row beyond an anchor by more than 2×" clause holds the release when a single cheaper entrant is more than 4× below the cheapest reference.
- The ledger (I1 M3) rejected removing it, and a re-freeze resolves it within the same cycle. I only note that it fires on exactly the entrant AGENTS wants reconciled promptly, so the re-freeze should be a pre-built path with a dual-run, not an ad hoc step.

## 2. Methodology design recommendations (prioritised)

1. Fix the bar (H1).
   - Define the bar as a quality level, publish the non-tautology assertion, and report r separately.
   - Implementable now: Q_bar comes from observed quality over non-provisional rows, with the E52 interval and scenario machinery unchanged.
2. Define "family" and score all rendered-frontier points (M1).
   - Add a normative family key.
   - Publish an alternatives table scoring every plotted configuration of a ranked family on frozen anchors, flagged "not ranked".
3. Add a conditional Plan output (M4).
   - A named "conditional on observed-workload multiple" frontier and bar view, using M_observed over the route set used for display and labelled "target-workload transport assumed, not identified".
   - It stays outside Θ-certified labels, so E32 and E49 are untouched.
   - It gives Plan buyers something decision-usable until an identified M_W exists.
   - It conflicts with E32 as written, so it needs an owner or editor decision.
4. Report nominal weight and effective influence together in the headline (L1).
   - Print "cost: 25% nominal; X% of value variance" in the headline line itself.
   - Optionally add an anchor-calibration sensitivity in which anchors are set so that SD(0.25·S_C) = SD(0.75·Q) on the common panel, as a sensitivity only.
5. Pin the report window and frontier extraction (M2, M3) as registry fields so they are testable.

## 3. Questions for the owner
- Q1. Does "cost = 25% of the value score" mean the nominal weight on anchored 0–100 scales, or the intended influence on the ordering? If influence, the anchors (not β) need calibrating. If nominal, should the headline carry the variance share?
- Q2. Is "one ranked row per family" owner policy, or may every rendered-frontier point be ranked? This changes M1.
- Q3. Which bar semantics do you intend: a frontier configuration (as now) or a quality level? This changes H1.
- Q4. Is the report window the preceding 30 days (AGENTS) or O13's 90 days plus grace? This changes M2.

## 4. Verdict
VERDICT: HAS FEEDBACK
