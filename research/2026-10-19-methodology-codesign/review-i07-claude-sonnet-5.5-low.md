# Internal review I7 — Claude Sonnet 5.5, effort low, on draft r66

(Saved from the subagent's report; the reviewer read all 841 folded lines.)

## 0. Read check
First line: `# ValueRank methodology — draft r66`
Last 12 words of the last line: "covers two-thirds of ranked rows jointly with the admitted components (E95, E101)."
(The folded file ends on the fragment "(E95, E101)."; the 12 words are counted from the unfolded last paragraph. I read lines 1–841 in three chunks.)

## 1. Findings by severity

**Critical**
None.

**High**

H1. **The O34 bar ladder is not defined in the draft, and the draft contradicts itself about how many bars exist.**
- Output 3 (line 59) says "v2 pins one bar", then describes a ladder of three levels (lower quartile, lower median, upper quartile).
- The bar-selection policy bullets (lines 591–599) define only Q̄ as "the ⌈n/2⌉-th value".
- The quartile rule is nowhere in the draft. The only statement of it is in the ledger as "zero-based position floor((n−1)k/4)". I grepped the draft for it and found no match.
- "Lower quartile" and "upper quartile" could be read as interpolated percentiles, as lower or upper elements, or as Tukey hinges. Two faithful implementations would freeze different levels, for example 48.06 against some other value.
- The policy object's fields ("position", "order") are listed but never given values for the quartiles.
- Recommendation:
  - Write the three positions into the policy bullets as k = 1, 2, 3 with zero-based index floor((n−1)k/4). This reproduces the ⌈n/2⌉-th rule at k = 2 for both odd and even n; I checked n = 35 and n = 36.
  - State that all three bars are frozen together.
  - Say what "unavailable" means for each bar when n < 2.
  - Delete "v2 pins one bar" or rename the policy version.
  - Add a fixture: n = 35 gives the 9th, 18th and 26th ascending values.

**Medium**

M1. **A stale count contradicts the defined cohort.**
- Line 173 says the subset workload W_S "covers 21 of the 23 cohort rows". The draft defines the cohort as 37 rows.
- By the draft's own counts, W_S (the seven AA Index evaluations) is complete for 35 of 37 rows. Line 138 gives 36 of 37 with costs, and only Claude Fable 5.1 is unresolved.
- A reader cannot tell whether "21 of 23" refers to an older cohort or to a different population.
- Recommendation: regenerate the sentence from the manifest, or state "35 of 37". Add a release lint that every "x of N cohort rows" figure uses the current N.

M2. **Rule IDs are reused for different rules, which undermines E191.**
- Line 3 makes tagged rules normative everywhere and lets "a rule that amends another govern it".
- E198 is used for two unrelated rules: the bar counts and the displayed-level test (lines 61, 601–603, 757), and the valuation-gate outcome (4) "Valuation basis unverified" (line 812).
- The brief shows the same reuse for E177 (swing attribution versus the swing gate's cohort transitions), E182 (the asymmetric kernel versus zero-length sides) and E184 (several different freeze rules).
- A citation such as "E198 governs" is ambiguous, and the "amendment governs" precedence rule cannot be applied mechanically.
- Recommendation: give each rule a unique ID, for example E198a and E198b or fresh numbers. Add a build lint that each tag maps to one registry entry.

M3. **The headline "cheapest above the bar" has no deterministic displayed-record counterpart.**
- The bar is a displayed-quality level (renormalised over observed leaves). The only defined outputs are interval and scenario labels, which test full-composite bounds with missing leaves at 0.
- At coverage p, a confirmed label needs displayed quality of at least about Q̄/p. The draft itself reports 5 confirmed qualifiers against 21 possible (line 605), so confirmed labels go almost only to full-coverage rows. This is disclosed and follows O25.
- However, the headline ranking is on displayed quality. The one view the owner asked for (O2, "cheapest above a bar") is therefore never stated on that same scale.
- Recommendation: define one plain output, "lowest-cost row with displayed quality ≥ Q̄ among non-provisional scored rows", with ties listed. Publish it beside the label columns and state that it is the displayed record, not a claim. This adds no new evidence, only an output on the headline scale.

**Low**

L1. **The coding-share figure may be stale.** Line 136 prints a median of 53% (range 35–85%) over 33 rows. The ledger brief records "median 56%". If the 53% is the post-O33 figure, the brief and its rejection note for I4 M1 ("coding share median 56%") need updating, so the owner is not shown an outdated number.

L2. **Quality credits fewer priced components than the cost basket pays for.**
- ITBench-AA, AA-Briefcase and GDP.pdf are priced in the basket (line 121), but none is a quality leaf. DevOps and IT operations, which the objective names, are credited in quality only through Terminal-Bench.
- The priced-mix coverage statistic already exists (line 230).
- Recommendation: state next to the headline how much of the quality weight sits on leaves whose benchmark is priced, and the basket cost share on benchmarks with no quality leaf. Priced-mix coverage may already cover the first number; I did not verify that. No score change is proposed (O6 and O15 stand).

## 2. Methodology design recommendations
1. Fix H1, M1 and M2 first. They are mechanical, they can be checked by a lint, and they are the only defects I found that would let two implementations disagree.
2. Add the displayed-scale "cheapest above Q̄" output (M3) as a named headline view. Keep the interval and scenario labels as the stricter claim beside it.
3. Add a release lint: every count quoted in prose must be generated from the manifest, since this draft has already shown a stale count (21 of 23).
4. Add the priced-versus-rewarded disclosure (L2) to the readiness table.

I checked the arithmetic for the Omniscience vectors and the reconstruction identity, the Bug Hunt vector (52/105 → 49.52), the exchange-rate formulas, the quality weights (they sum to 100), the 1,024 admission subsets, and the cohort counts (27 retained plus 10 primary = 37; 37 − 2 MiMo − Muse Wonder Full − Fable = 33 panel rows). All are consistent. I did not use web search. The facts about benchmarks, AA pages and SemiAnalysis come from the draft and ledger, and I did not verify them against outside sources.

## 3. Questions for the owner
1. For the three ladder bars (O34): should the quartiles be zero-based floor((n−1)k/4) elements as in the ledger, or interpolated percentiles? If you want interpolation, the "level is never a configuration" property is lost unless a frozen interpolated value is allowed. Your answer changes the H1 wording.

## 4. Verdict
VERDICT: HAS FEEDBACK
