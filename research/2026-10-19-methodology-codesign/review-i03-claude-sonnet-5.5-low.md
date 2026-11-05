# Internal review I3 — Claude Sonnet 5.5, effort low, on draft r62

(Saved from the subagent's report; the reviewer read all 788 folded lines.)

## 0. Read check
First line: `# ValueRank methodology — draft r62`

Last 12 words of the final text: "covers two-thirds of ranked rows jointly with the admitted components (E95, E101)." The folded copy's last physical line, 788, holds only "(E95, E101).".

I read all 788 lines and ledger-brief.md. I also grepped ledger.md for E187/E188/E192/E193/E194 and the I1/I2 sections. I did not use web search. The checkable claims are internal arithmetic and statistics, and I verified them directly:
- The quality weights sum to 100, and the 86.7% basket-scope retention is right.
- The Omniscience test vectors are correct: 82 and 66 under the old formula, and I = 50 and z = 75 under the new one.
- The Bug Hunt vector 52/105 gives 49.52.
- The Clopper–Pearson endpoints and δ = 0.05/16 are correct.
- The exchange-rate formula is correct.
- Lower-median-of-n always leaves at least 2 configurations at or above Q̄.

## 1. Findings by severity

**Critical**
None.

**High**

H1. Retention (E163/E187) and the one-configuration-per-family rule (E188/E193) are not reconciled.
- Passages: Cohort bullet 1 says any tracked-catalog configuration with exact DeepSWE and a matched Bug Hunt result "is also ranked". The configuration rule then says "the build fails when the tracked catalog ranks any other configuration of a frontier or near family".
- The gap: two cases are unspecified.
  1. A frontier family's non-highest effort has both exact results. Retention says rank it; the family rule says fail the build.
  2. A near family has two or more efforts with both exact results. "Ranks the configuration that retention already ranks when there is one" does not say which.
- Why it matters: two faithful implementations produce different cohorts and different anchors. Retained rows already set anchor extremes (Grok 4.7 sets the Plan upper anchor). The ledger shows E187 and E188 were adopted separately, and neither addresses this case. Today's nine retained rows avoid it only because none shares an AA model identity with a frontier or near family.
- Change: add a precedence sentence. Retention applies only to configurations whose family (E193) has no frontier or near point. For a family with a frontier or near point, the single ranked configuration is the E188 pick, or, for a near family with several retained efforts, a stated deterministic pick (for example smallest gap, then lower cost, then name). Add a fixture for each case and have the build reject any other outcome with a named reason.

**Medium**

M1. The bar's "always compares alternatives" guarantee is overstated (Outputs item 3, the bar-policy bullets, and the release test "never returns its own setter by construction").
- The non-tautology proof (at least two population configurations at or above Q̄) holds on displayed quality, over non-provisional ranked rows.
- Qualification is evaluated only over R_W: rows with FullCost on W and, on Plan, an identified M_W.
  - Nothing requires the two at-or-above rows to lie in R_W. On the main workload, the 3 rows without Coding Agent Index cost are outside R_W.
  - On Plan, the ledger says no route has an identified M_W today, so R_W is empty and the Plan bar and frontier outputs are vacuous.
- The release test wording "never returns its own setter" also conflicts with the text that the setter "competes like any row". The test is really "is not forced to return it".
- Change:
  - Publish per basis and workload the count of R_W rows with possible qualification, and the status "comparison vacuous" when that is below 2.
  - Restate the guarantee as "at freeze, at least two population configurations reach Q̄ on displayed quality", not as a property of the output.
  - Reword the release test.

M2. The bar level and the candidates' qualification use different quality equations.
- Q̄ is an observed-only renormalised statistic, the lower-median displayed quality. Candidates are tested with the full composite, with missing leaves anywhere in [0,100].
- A row at exactly Q̄ on the displayed measure (the setter, GLM-5.3) can fail confirmed qualification at coverage below 100%, because Q^L sets its missing leaves to 0. The draft concedes this for the setter at line ~605.
- So the published "bar 52.1" reads as a displayed-quality threshold, while the labels apply a stricter, coverage-dependent test.
- Change: label the bar "displayed-quality level; labels test the full composite". Publish a column giving each row's observed-only margin to Q̄ beside the interval status. A reader can then tell "below the bar" from "not provably above it because of missing leaves".

M3. The report window has an unstated rule for sole reports (E194 with E151).
- The window is the 30 days ending at the search cutoff. "A report admitted at an earlier release … thereafter ages under E151/O13." The build fails if a newly admitted report is dated outside the window.
- The rules do not say whether a single in-window report, which is single-source and diagnostic under O11, counts as "admitted". If it does, it can pair at the next release with a new in-window report from up to ~90 days earlier. That is wider than AGENTS.md's "preceding month". If it does not, two reports 45 days apart can never form a pair.
- Two faithful implementations will disagree on whether such routes become official.
- Change: state it explicitly. Either "admitted" means passing inclusion rules regardless of the source count, or concordance pairs must both fall inside one window. Add the 45-day-apart fixture.

M4. E170 says the join "returns exactly one outcome" but lists three; the text defines a fourth.
- The three outcomes are (1) compatible, (2) revalued, (3) not in force.
- The text also defines "valuation basis unverified": never interval-eligible, excluded from anchors (the E184 reading, "outcome 1 or 2"), and not in B_W (E183, which holds outcome 3 only).
- The consequence: an unverified-basis row neither competes in U_W nor blocks other rows' labels. Outcome-3 rows do block. The E38 scope text covers this, but only as a disclosure.
- Change: make "unverified" an explicit outcome 4, with its treatment stated (anchor-ineligible, interval-ineligible, and either a blocker with a full-domain cost or a listed omitted competitor, whichever the owner intends).

**Low**

L1. Garbled normative sentence, "Reference object (E52, amended by E192)", ~line 570: "…Q_r ≡ Q̄: i ∈ R_WOver R_W and a pinned reference r: i ∈ R_W, competitors j ∈ U_W (E183):". It is a doubled fragment from an edit. The definitions of confirmed, possible and scenario qualification that follow depend on it. The same paragraph, K_r and the Q_r(θ) notation keep v1's reference r although the v2 bar has no reference row. Fix the sentence and rename the notation to Q̄.

L2. Plan interval outputs are empty today. The text says Plan interval outputs use only an identified M_W, and the ledger says none exists. The draft says this only indirectly, through the "exploratory" label and the manifest's "vacuous" status. The Outputs list (items 2 and 3) presents frontier and bar views per basis without saying the Plan ones are currently empty. Add one line to Outputs, and let the headline print "Plan frontier/bar: 0 evaluable rows" until that changes.

L3. Sequential-rule scope. The guarantee is stated per event, not per family. The label needs every kernel assignment (up to 2^G, small in v1) to pass for each of up to 19 candidate rows. The false-label rate across rows is therefore larger than 0.05/16 per event. Say so beside the label ("per-event guarantee; not corrected across candidate rows"), or apply a Bonferroni factor to the candidate count.

## 2. Methodology design recommendations

1. **Claims-actually-supported table on the headline (highest priority).** One table per basis and output (frontier, bar, scenario shares) with the evaluable count, the evidence class behind it (measured, transfer, API fallback), and the status vacuous / partial / full. The draft's many conditional gates (R_W, B_W, identified M_W, FullCost) mean a reader cannot tell from the headline how much of the Plan side is substantive. This is presentation only, built from existing manifest fields, and changes no score.
2. **Within-family sibling check.** The ledger rejected ranking or scoring alternatives, so this is a different request: an unranked diagnostic. For each frontier family with several rendered frontier points (18 vertices over 7 frontier families), list the sibling points that also have exact DeepSWE and Bug Hunt results, with their displayed quality and cost. E188 ranks only the dearest point, and the ranked point's value rank can differ from a sibling's. This shows readers whether the family's best-value effort is the one ranked, without adding rows. Where a sibling lacks exact results, mark it "not evidenced".
3. **Observed-only margin column** for the bar (see M2). It uses only existing quantities.

## 3. Questions for the owner
1. When a near-frontier family has several efforts with both exact results, should the ranked configuration be the smallest-gap near point, the highest-quality retained effort, or the cheapest (H1)?
2. Should "admitted report" for the report window (M3) include a sole in-window report awaiting a partner, or must concordant pairs lie within one 30-day window?
3. Should an "unverified valuation basis" row block other rows' labels the way a superseded-price row does (M4)?

## 4. Verdict
VERDICT: HAS FEEDBACK
