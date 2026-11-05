# Internal review I45 — Claude Sonnet 5.5 (effort high) on draft r103

## 0. Read check

- First line of the draft: "# ValueRank methodology — draft r103".
- Last line of the folded copy (line 954): "Plan anchor references as plan rows (O48), and drops internal review labels from the text. Every change is recorded with its rationale in the ledger."
- Last 12 words of the last paragraph (the "Revision history" paragraph): "the text. Every change is recorded with its rationale in the ledger."
- Also read: `reviewer-prompt.md`, `ledger-brief.md`, `ledger.md` from "## Internal review I28" (line 1170) to the end (I44 and the "Draft r103" status line), and the repository `AGENTS.md`. The copy of AGENTS.md quoted in my task context is older than the repository file: it still shows the pre-O61 LiveBench split (Long Agentic 5 and Coding 2, FrontierCode 18 / Terminal-Bench 14 / Bug Hunt 10) and "replace a ceiling as soon as one exists". The repository file carries O61 and O62, so I judged the draft against the repository file, with which it agrees.
- Checks against the build. The folded copy equals `draft-r103.md` (whitespace-normalised) and `python3 -m valuerank.draft_figures check` exits 0. I compared a sample of rendered figures with `data/scores.json`:
  - Exchange rates: 3.04 / 4.06 and 2.83 / 3.77, with the quality-point figure equal to the value-point figure divided by 0.75.
  - Bar ladders: 54.2 / 64.3 / 65.0 and 38.0 / 49.2 / 57.2. Reach counts 7 / 5 / 3 of 9 and 12 / 8 / 5 of 15 follow from positions floor((n−1)k/4).
  - Plan-row counts: 27 and 50. The 14 of 27 and 48 of 50 rows on a transfer or ceiling reproduce from the route structure.
  - Admission: thresholds 6 and 10, and 255 and 127 feasible subsets (2⁸−1 and 2⁷−1 once ITBench-AA is infeasible).
  - Source shares: 66/34 and 78/22.
  - Group drift flag, non-discriminating leaf, noise margins (3.8 and 5.9 ≈ 0.75⁻¹ × the thresholds).
  - Source clocks against O59 and O60, and the SemiAnalysis age arithmetic (day 30 = 2026-11-05, day 91 = 2027-01-05, day 121 = 2027-02-04).
  - Test vectors and fixtures: Omniscience, Bug Hunt 52/105, the admission fixtures, the three-group arcsine fixture, the Clopper–Pearson endpoints, the ladder fixtures.
  - None was wrong.
- I also checked that the plan-row spread of every configuration is below its own separation threshold, so the "none today" statement about spanning plan rows holds (GPT-6 Astra (max) is the widest at 2.04 against 2.83).

## 1. Findings by severity

**Critical**

None.

**High**

None.

**Medium**

None. I looked for a rule that two faithful implementers would resolve differently or a wrong stated figure, in the cohort and family rules, the per-ranking admission and anchors, the leaf tables and weights (13 and 11 leaves, 60 / 20 / 10 / 10 in both rankings), the O61 tie, the clip gate and O58, the source clocks, the Plan lifecycle and the separability and band rules. I found none that meets the bar. The items below are Low.

**Low**

L1. Row names: the published tables do not all follow "Rows are named 'Family (effort)'" (Cohort and configuration, Configuration rule).
- The row `claude-haiku-5-5` (the xhigh family primary) has the name "Claude Haiku 5.5" in `scores.json`. README.md (line 72, and the indicative-value table at line 89) and scores.md print it without an effort.
- AA's own bare plotted name "Claude Haiku 5.5" (slug `claude-haiku-5-5`) is the max row, which ValueRank prints as "Claude Haiku 5.5 (max)". The unqualified name therefore denotes a different configuration from AA's bare name.
- The draft qualifies every row it names ("Claude Haiku 5.5 (xhigh)"), through `draft_figures.display_names`. README.md line 151 maps the family to its xhigh row, so no ranking or claim is affected.
- Recommendation: give every emitted row `name` its effort suffix (or use the same `display_names` function in the README and scores.md emitters), and have the build's uniqueness check run on those names.

L2. E196 handles only the negative cost allocation (Outputs 1, "Nominal weight beside influence").
- The sentence "dearer configurations then score higher on quality, so cost offsets quality differences" is specified for a negative cost allocation. Today the max-effort ranking's API cost allocation is above 100%: README.md's scope line reads "103% of API and 20% of Plan value variance". Quality's allocation is then about −3%, which the headline does not print, and no sentence explains it.
- A reader of "25% nominal weight; 103% of variance" gets the number but not the meaning: on that basis the ordering is essentially a cost ordering with quality offsetting it.
- Recommendation: state the mirror case. When cost's allocation exceeds 100%, print quality's (negative) allocation beside it with "cheaper configurations then score lower on quality, so quality offsets the cost spread". The disclosure never changes a score, as E196 says.

L3. The "today" list of clipped indicative rows is API-only without saying so (Cohort, "Indicative value for a listed family", and its source placeholder `{{fig:max.indicativeClipped}}`).
- The sentence says a cost beyond an anchor "shows 0 or 100; today Claude Haiku 5.5 (low), GPT-5.6 Luna (low), GPT-6 Luna (high), (low) and (medium)" for the max-effort ranking.
- In `listedIndicative` the Plan basis also shows a clipped cost score of 100 for Claude Haiku 5.5 (high) and Claude Haiku 5.5 (medium), which are not in that list.
- The O58 sentence in the Cost section does list both bases correctly.
- Recommendation: name the basis in the sentence ("on the API basis") or list both bases, as the O58 sentence does.

L4. The headline sentence for a subset-cost leader.
- README.md opens "MiMo-V2.6-Pro leads the API ranking at 60.3 (subset cost)". The draft (Cost, E86 and E190) says orderings across W and W_S are not identified and the row is "subset cost — cross-workload ordering not identified". O17 keeps the row's table position, so the position is right.
- The sentence should carry the full label and not only "(subset cost)". The flags legend (README line 63) has it, but a headline read alone does not.
- Recommendation: add to E59's headline rule that a leader on a subset workload is named with "scored on its subset workload; ordering against main-workload rows not identified".

L5. Band layout when plan-row extension crosses another configuration's band (E248).
- The text covers the case where one configuration's plan rows span more than the threshold: another configuration's row starts a new band "as usual", and the configuration's own rows stay in the first band by extension. The extended rows can then lie inside the rank range of the band that the other row started, so the printed bands `[first rank, last rank]` overlap.
- No configuration spans that far today, so nothing is wrong.
- Recommendation: say how bands are printed in that case (a set of ranks, not a range), so the future case has one reading.

L6. Two generated header statements use terms the draft defines differently (outside the draft's own text; reported so it is not lost).
- README.md's scope line says "9 cohort configurations", while the draft defines the cohort as the 29 plotted configurations and calls the ranked ones "cohort rows". It also shows "Updated: October 19, 2026", the version date in `valuerank/release.py`, on data whose cutoff is 2026-10-23T06:26:23Z.
- Recommendation: print "9 ranked configurations of the 29 in the cohort" and the release cutoff date.

## 2. Methodology design recommendations

Priority order, all small and implementable from existing data:

1. Name hygiene (L1). Use one display-name function for every emitter (`scores.json` row `name`, README.md, scores.md, methodology.md), so a row is always "Family (effort)". Its uniqueness check should then run on those names, which also removes the collision with AA's bare names.
2. Complete the E196 disclosure (L2). Print both allocations (cost and quality) beside the nominal weights in the README scope line. Print the explanatory sentence for whichever is negative. The `allocation` object already carries both numbers.
3. State the basis in every "today" list that depends on one (L3). A cheap way to enforce it is to extend the E265 lint so a sentence quoting a clipped-row list must also contain "API basis" or "Plan basis", or a placeholder that renders both. It is a defect in the source (the placeholder `indicativeClipped` renders API only), not a check failure of the kind I43 found.
4. Headline rule for subset-cost leaders (L4), as a template line in the README emitter.
5. No new proposal on ladder bars closer than the noise margin. I44 recorded the idea for the owner report. The new fact is that the max-effort headline (64.3) and upper (65.0) bars are 0.75 points apart against a 3.8-point noise margin, so two of three rungs are effectively one rung there. That strengthens the case for the owner report but is not a defect: O34 fixes the ladder and O44 supplies the margin companion.

## 3. Questions for the owner

None.

## 4. Verdict

VERDICT: NO FURTHER FEEDBACK
