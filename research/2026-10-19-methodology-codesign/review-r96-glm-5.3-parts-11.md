0. Read check

Both listed parts were opened through the GitHub connector at commit ce7c11f064d17d1f947ebf5e0389c366df0b335d and read to their ends.

Part 11 (draft-r178-part-11-of-15.md) — first line: "- Specification: alternative leaf weights, leave-one-benchmark-out, leave-one-source-out (leave-AA-out is registered but "not identifiable under the coverage rule" while independent leaves hold under 40% of nominal weight, today 34% in the max-effort ranking and 22% in the AI Coding Daily ranking; independent-source robustness is reported by the matched-panel statistics of E62), cost-weight slider, owner assumptions on/off, cache-rate stress, Bug Hunt harness stress." — final sentence: "The current ladders are in Output 3 and scores.json barCurrency."

Part 12 (draft-r178-part-12-of-15.md) — first line: "- Fewer than two population configurations pin no bar: all three bars, and every output that reads them, are published as unavailable." — final sentence: "Ranked configurations only (owner decision O43): a family listed under O38 with an indicative value (O41) is not a competitor in any frontier or bar output; each ranking's outputs compare that ranking's rows only, so a configuration ranked only in the other ranking is outside them too; the summary says these outputs compare ranked configurations only and names the listed configurations."

Both parts read fully; proceeding to the review. I also re-computed the parts' numerical fixtures: the E137 kernel fixture (uniform ≈ 91.5%, arcsine ≈ 86.8% — matches "about 91.5% / about 86.7%"), the E221 u* fixtures (102 at H = 93, −2 at H = 67), the E74/E152 basis-typing fixture (P = 25, P^(−TB) = 20), the O34 ladder positions for n = 2, 3, 4, 9, 15, 27, 32, and the E92/E192 dominance logic — all check out.

1. Findings by severity

Critical

None.

High

The bar-population rule admits partial-leaf rows, whose displayed quality the draft itself calls "not comparable." Part 11's normative text says: "The population is the non-provisional cohort rows with a displayed quality." A listed row (O38: a required frontier family missing a leaf after the logged search is "listed, not ranked") still has a renormalised displayed quality Q̄_i over its remaining leaves — and O41 labels exactly that value "not ranked, not comparable." Per the letter of the population rule, such a row can enter the population and set the headline bar H. E243's phrasing ("the bar population keeps full-benchmark rows without a cost") presupposes a complete-leaf population, but the primary rule never states the requirement, and O43 excludes listed rows from bar *claims*, not from *setting* the bar. This hurts the objective directly: H is the level the headline cheapest-above-bar view is built on; a renormalised quality from a row missing its weakest or strongest leaf could shift H by points and corrupt every bar output and label. The 2026-10-21 population (32 = the ranked set, while the cohort was 37) suggests the build already restricts, so this is a spec–build divergence risk in an "executable specification." Concrete change: amend the population rule to "the non-provisional cohort rows with the ranking's complete leaf set (p_i = 1) and a displayed quality," and add a build check that fails when a bar-population row lacks a leaf of the ranking.

Medium

The E203 displayed-record answer and the O171 noise screen never define their comparison panel. E203 names "the lowest-cost scored, non-provisional main-workload row whose displayed quality reaches the bar" — an O94 row satisfies every word of that (it is ranked, non-provisional, main-workload), yet blockers "compete and can deny a label but never earn one." Worse, the O171 screen requires "every cheaper row has Δ ≤ −1.96" and prints "the number of cheaper rows compared" without saying which rows count: a subset-workload row (E190; E173 says the direction of the subset cost effect is not known) cannot be cost-ordered against main-workload rows at all, and an O94 row's published cost sits at the bottom of a [C, factor·C] domain. Why it hurts: whether an answer reads "passes the screen," "contested," or "rounding-stable only" — a published headline companion — turns entirely on this unstated panel, and two implementations of the same spec can print opposite readings. Concrete change: state the panel explicitly (main-workload, scored, non-provisional rows on the answer's basis; blockers either excluded with a printed line or compared on their published cost with a blocker marker; subset-workload rows named as uncomparable beside the count), mirroring how E201c and E203 already label their comparison objects.

S1M's level attribution for Terminal-Bench's interval is unpinned, and the ledger records this exact error class before. Part 11 hard-codes the stream description "conventional range sensitivity inside Terminal-Bench's published 95% confidence interval." Public TB 4.0 results appear with ± bands of unstated level (e.g., "Opus 5.5 (max), 64.8% ±3.1"), and third-party write-ups explicitly warn that some Terminal-Bench error bars are standard errors across runs, not 95% confidence intervals. The ledger's rejected-claims list already contains a misattributed 95% level ("AA states a 95% level for GDPval-AA intervals": rejected — the sentence belonged to AA-Briefcase). Why it hurts: the stream description is normative published output; if tbench documents a standard error, "published 95% confidence interval" attributes a level the source does not state. The impact is low today (S1M is dormant, E236), but the fix is cheap. Concrete change: pin the captured tbench sentence that states the level in the evidence registry; if it states a standard error, describe S1M as "Terminal-Bench's published interval (level as documented)" with the 1.96 widening as a named conventional alternative under E165, and update the part-11 stream-description template accordingly.
gravity
+2

Low

E221's "observed-score rounding decides this row" status fires only when u* falls outside (E338). A row whose in-domain u* is nevertheless already decided by the observed leaves' rounding interval gets no such flag on the u* output itself; the reader must cross-read the interval statuses published beside it (E198b). Concrete change: attach the same status whenever the observed rounding interval alone determines the row's qualification, not only on out-of-domain u*.
0

Three overlapping disclosure surfaces for unevaluable cheaper configurations now coexist — E201c's uncheckedCheaperSiblings (compares AA total Index cost), the O143 headline note, and the O172 common-leaf answer — with different comparison objects and different fields. Nothing requires them to agree or cross-reference, so the lists can diverge across releases and confuse exactly the reader they exist to warn. Concrete change: consolidate into one named per-bar table (configuration, why unevaluated, comparison object) referenced from all three surfaces.

2. Methodology design recommendations

Prioritised, all implementable from public data already captured:

Complete-leaf clause in the bar population (fixes the High finding). Population = non-provisional cohort rows with p_i = 1 and a displayed quality; build check fails on a population row missing any leaf of the ranking; the release prints how many cohort rows were excluded from the population for coverage. This aligns the primary text with E243's "full-benchmark rows" and with O41's own "not comparable" label, at zero data cost.

Panel contract for E203/O171 (fixes the first Medium finding). One sentence in the E203 definition: the answer and the noise screen range over main-workload, scored, non-provisional rows on the same basis; blockers compared separately at published cost with a marker; subset-workload rows listed as uncomparable. Print the panel size beside noise.comparedN, which already exists.

Pin the Terminal-Bench interval level (fixes the second Medium finding). One registry entry holding the captured sentence that states the level, plus the E165 fallback wording if it is a standard error. Precedent: the GDPval 95% misattribution already rejected in the ledger.

Correlation-grid companion for the O171 screen. The screen fixes ρ = 0 between σ_i and σ_H. That is the conservative choice in both directions, but candidate and bar setter are measured over shared task universes, so positive correlation is plausible; O42 already publishes a 0 / 0.3 / 0.6 grid for the separability threshold. Compute the same screen at 0.3 and 0.6 from the same analytic SDs — no new data, no label change, and it shows whether the pointwise pass/contested readings survive shared-task correlation (still explicitly not simultaneous, per E337).

Extend the E338 rounding-decides status to any u* whose row is decided by observed rounding, per the Low finding above — a one-line change in the same scores.json field.

3. Questions for the owner

Is the bar population intended to be restricted to complete-leaf rows (as E243's "full-benchmark rows" phrasing and the 2026-10-21 population of 32 suggest), i.e., should a listed, partial-coverage row be barred from setting H? The answer determines whether the High finding is a text fix or a policy change.

In the E203 displayed-record answer and the O171 noise screen, are O94/blocker rows and subset-workload rows intended as candidates or comparators, or excluded with a printed exclusion list? The answer determines the panel contract in recommendation 2.

4. Verdict

VERDICT: HAS FEEDBACK