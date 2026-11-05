# Internal review I40 — Claude Sonnet 5.5 (effort medium) on draft r99

## 0. Read check

- First line of the draft: "# ValueRank methodology — draft r99"
- Last line of the draft (the folded copy's final line, 947): "configuration (O54, E252). Instruction following has no weight while Surge's Complex Constraints is excluded (O53). On the Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Last 12 words of the last paragraph: "Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Also read in full: `reviewer-prompt.md`, `ledger-brief.md`, `ledger.md` from "## Internal review I28" (line 1170) to the end (I39 and O59/O60), the whole folded draft (947 lines), and the root `AGENTS.md`.
- Checked against repository data and code, not just prose:
  - `data/scores.json`: bar ladders; bar currency; both anchor exchange rates; the clip gate and the listed-beyond-anchor rows; separability medians, counts, correlation grids and bands; E242 tolerances; value-variance allocations; identification yield; plan-row and transfer counts; the displayed-record and noise-margin cheapest rows; the one-row-per-family diagnostic; the Cognition gap fills; drift flags; `sourceClocks`; `releaseHold`.
  - `data/aa_frontier_capture.json`: the 18 vertices, the 11 near points with gaps, and the previous-capture comparison.
  - `valuerank/value_v3.py`: `rank_separability`, `rank_bands`, `source_clocks`, `check_source_clocks`.
- Recomputed by hand and found correct:
  - the 25% / 75% exchange-rate formulas, and 3.04, 2.44, 2.83 and 1.89 from the stated anchors;
  - the Clopper–Pearson δ = 0.05/16 endpoints;
  - the Omniscience vectors and the 98/1/1 and 99/1/0 examples;
  - the quartile positions floor((n − 1)k/4) for n = 4, 9, 15, 32;
  - the 91.5% fixture;
  - the E242 tolerances 2.35 and 5.28;
  - the 27 and 50 plan-row decompositions and the 14 and 48 transfer-resting rows;
  - the 255 and 127 feasible-alternative counts;
  - the 72/28 and 78/22 source shares;
  - the quality margins 4.0 and 5.9;
  - the Plan evidence-clock dates (age 30 on 2026-11-05, expiry 2027-01-05, demotion 2027-02-04).

I found no Medium or higher finding. The r99 additions (O59 and O60 non-AA source clocks) are stated consistently with the build and with the ledger. Four Low observations follow.

## 1. Findings by severity

**Critical**

None.

**High**

None.

**Medium**

None.

I looked for the kinds of finding that made earlier rounds non-clean: a stale figure, a rule that disagrees with the build, a contradiction with AGENTS.md or an owner decision, and a rule two implementers would read differently. None of the draft's stated "today" figures I checked is wrong. Every check against `scores.json` matched. Nothing contradicts AGENTS.md. The checks included:

- cohort 29 = 18 + 11 from 12 families (7 + 5);
- 9 and 15 ranked, 20 ranked at least once, 9 excluded;
- 20 and 14 listed;
- bands, grids and tolerances;
- plan-row counts;
- the O58 listed-row disclosures (factors 4.75, 1.92, 1.57, 1.41, 1.06 and 3.41, 2.09, 2.09, 1.35; 1.27, 1.06, 1.24);
- the setter-is-cheapest counts (1 of 6 and 2 of 6);
- the variance allocations (65% and 2%; −90% and −26%).

**Low**

- **L1. The separability sentence does not say which threshold the count uses.** Output 1 gives the threshold per adjacent pair, prints the median, and then says "how many adjacent ranks it separates". The build counts a pair as separable when its own gap reaches its own pair threshold (`value_v3.rank_separability`). It does not compare every gap with the median. A reader could take "it" to mean the median threshold, and that reading gives different counts when row SDs differ. The bands rule is stated per pair and is fine. Recommendation: add "each pair against its own threshold; the median is only a summary".
- **L2. O59 and O60 leave the age arithmetic and date-only stamps to the code.**
  - The draft says a capture is rejected when "more than 30 days before the release cutoff". The build counts whole UTC calendar days between the capture date and the cutoff date (`SOURCE_MAX_AGE_DAYS`).
  - Cognition's capture is recorded as a date only ("2026-10-23"). The build treats a date-only stamp on the cutoff's day as not after the cutoff. The draft does not say this.
  - Today nothing turns on either point: Cognition's last modification (2026-10-22T22:28:12Z) predates the cutoff's day. The paragraph also calls the Bug Hunt, tbench.ai and Cognition captures "inside the clock" without separating "captured before the cutoff" from "stands under O60".
  - Recommendation: point to the whole-UTC-day, strict-threshold convention already stated under the Plan evidence lifecycle (E212), and add "a date-only capture stamp on the cutoff's day is treated as not after the cutoff". Optionally add a fixture for a source with no recorded update date captured after the cutoff, which should fail.
- **L3. "One per family" overstates the max-effort ranking's coverage.** The Cohort section says the 9 max-effort rows are "one per family at the vendor's top effort". The ranking holds 9 of the 12 families. MiMo-V2.6-Flash, MiniMax-M3.1-Flash and GPT-5.6 Luna have no row, and GPT-5.6 Luna has no top-effort point in the cohort. Recommendation: say "at most one per family, at the vendor's top effort".
- **L4. `scores.json` still carries DeepSWE labels on the cohort object.** E250 says that no DeepSWE result enters cohort membership or any diagnostic, and that withdrawn data stay in the raw data. The published `cohort` object nevertheless has `source` = "Artificial Analysis Coding Agent Index v1.5 DeepSWE v1.1 chart". It also has `sourceN` 61, `exactBenchmarkOverlapN` 17 and `sourceUpdatedOn` 2026-10-17T19:26:26Z, which is the DeepSWE chart's observation. The top-level `deepsweSource` and `deepsweConfigurationsN` are also still present. Nothing in the site or in `emit_docs.py` reads these, so no ranking is affected, but a reader of the JSON could take the cohort to be defined by that chart (it is defined by the 2026-10-23T05:27:39Z frontier capture). Recommendation: relabel them "withdrawn by AA, not scored (E250)", or point `cohort.source` at the frontier capture.

## 2. Methodology design recommendations

In priority order, all optional and none needed for a clean round:

1. **Apply the L1 clause** (pair thresholds versus the median). It is a wording change, and the figures and build stay as they are.
2. **State the date convention once** for the O59 clock (whole UTC days, strict threshold, date-only stamp rule), as E212 already does for evidence ages. Add one fixture each for a capture 31 days before the cutoff, a date-only capture on the cutoff's day, and a post-cutoff capture with a null update date.
3. **Clean up the `scores.json` cohort object** (L4) and, if cheap, add a build assertion that no field named in the cohort object reads a DeepSWE artifact.
4. **Carry forward, not for this round:** two designs from earlier rounds remain worthwhile in the final editorial pass.
   - A Bug Hunt √N sensitivity. The DeepSeek V4.1 Flash 1017 (max) tie of 7 runs each (DeepSeek's harness 42.7, Claude Code 39.1) moves its Bug Hunt z by about 3.4 points. That is about 0.34 quality points at weight 10 and about 0.41 at weight 12, so it is small, and the draft already flags the choice for owner review.
   - Splitting Output 1 into sub-bullets (I38 L4, rejected for now).

## 3. Questions for the owner

None.

## 4. Verdict

VERDICT: NO FURTHER FEEDBACK
