# Internal review I21 — Claude Sonnet 5.5 (effort low) on draft r80

## 0. Read check
First line: "# ValueRank methodology — draft r80"
Last 12 words of last line: "covers two-thirds of cohort rows jointly with the admitted components (E95, E101)."
(Read all 997 lines in four chunks: 1–300, 301–600, 601–800, 801–997; read the condensed ledger brief. I did not open ledger.md or the code and ran no web search; cited sources — AA pages dated 2026-10, SemiAnalysis, Bug Hunt, Cognition — are not independently checkable from here, so no factual-error findings are raised. I recomputed the draft's arithmetic: anchor exchange-rate formulas, ladder positions and bar-currency counts (17/25/9 of 32), the Omniscience vectors, the Clopper–Pearson endpoints, the 91.5% uniform kernel fixture, and the lifecycle age boundaries; all are correct.)

## 1. Findings by severity

**Critical**
None

**High**

1. **Gap-filled and provider-claimed leaves carry full weight with no gap-fill sensitivity or label restriction** (Cohort "Full benchmark set (O36, O38)", with E222/E100 for labels). The draft admits 11 filled leaves — FrontierCode for 8 configurations from Cognition, FrontierCode for 2 from a newer AA capture, and DeepSWE (the 30% leaf) for MiMo-V2.6-Pro from Xiaomi's own result — roughly a third of cohort rows. A source-type flag is published per row and the leaf is "labelled a provider claim", but nothing then treats them differently: they can earn "confirmed cheapest" and scenario-supported labels (UniqueLabelEligible checks only non-provisional and not label-denied), and they enter anchors and the bar population as if AA-run. Governance says "provider claims never overwrite independent measurements", yet a claim that is the sole evidence on the heaviest leaf functions as one. Cognition's FrontierCode is asserted to be "on the same 0–1 scale" as AA's with no specified agreement check; E229's τ_b cross-check covers Terminal-Bench only.
   Recommendation: (a) add "provider-claim leaf" to the E222 label-denial conditions (the row can block a label but never earn one); (b) for third-party gap fills, publish each release an overlap check — on rows where AA and Cognition both report FrontierCode, Kendall τ_b and mean/max offset, as E229 does for Terminal-Bench, with "scale equivalence not tested" below n overlapping rows; (c) add a standing "gap-fill removal" column that rescores affected rows with the filled leaf treated as missing (E221 u* / E146 renormalisation machinery) and reports rank changes — E146's leave-one-benchmark-out removes the leaf for all rows and cannot isolate this; (d) state the harness/agent of every gap fill beside the leaf (as E227 does for DeepSWE).

**Medium**

2. **Stale, contradictory population counts in the normative text** (Cost "Admission and persistence (E26)"). It says the 2026-10-21 outcome is "eight components on a 33-row panel (cohort of 37)", "the admission panel and the anchor references are the same 33 rows", and that Claude Fable 5.1 is "the 34th row of the common-workload panel". The Counts paragraph gives cohort 32, admission/anchor panels 29, R_W 29, common-workload panel 30 (which I reproduced from the exclusions: Muse Wonder Full no cost, Fable fails FullCost, MiMo-V2.6-Pro lacks Coding Agent Index cost). Two faithful implementations testing the stated counts cannot both pass; these are pre-O36/O38 leftovers. Replace 33→29 and 34th→31st (or drop numbers from rule text and keep them only in the generated "Today" counts), and add a release lint that all "Today N rows" statements equal generated counts. Ledger-brief also disagrees with the draft on coding share (56% vs 53%), unrewarded share (15% vs 14%) and the frontier-families bar (60.9 vs 61.0); flagged so the ledger is refreshed.

3. **With no missing leaves and no identified Plan multiples, S0, S1 and S1M collapse, and the "confirmed"/"scenario-supported" labels certify a nearly deterministic event** (Uncertainty, E100, E77, E145). Every ranked row has all eleven leaves, the Terminal-Bench CI is unused (the leaf is AA's own run, so S1M = S1), and no Plan multiple is identified; Θ reduces to rounding intervals and S0 = S1 for every row except a rounding-level tie. A "≥ 90% scenario share" at S1 core is then ~0% or ~100% for every row, while the only perturbation with real spread (the Dirichlet weight stress in S2) is barred from authorising labels by E100. A reader sees "confirmed" beside a cost-per-bar answer whose quality margin may be below Bug Hunt run-to-run noise or DeepSWE's 3-attempt average. **Owner decision challenge (O25/O22 — the published-record target itself is not questioned)**: drop the word "confirmed" from labels in favour of "cheapest on the published record, rounding-robust", and print "no benchmark run-to-run or fitted-rating uncertainty is included" in the same sentence as the label, not only in the stream manifest.

4. **Dead machinery and live rules are interleaved with no marker.** O36 makes every missing-leaf rule vacuous today (provisional status, Q̄ renormalisation, E198b, E201b, E219, E221, E226, S1 missing-leaf draws, label reach). The draft says they stay "defined so that the formal definitions remain total" but scatters them with "today none fires" remarks. Add a standing "Rules inactive in v3 (O36)" index of rule IDs with their activation trigger, add the inactive list to the E63 active-rules manifest as status "vacuous", and keep one fixture per inactive rule.

**Low**

5. **Owner decision challenge (O36/O38 against AGENTS.md bullet 1).** MiMo-V2.6-Flash is on AA's rendered frontier (tied with GPT-6 Luna (max) at displayed 38) and is "listed, not ranked". The exclusion is logged, so not silent, but the headline table no longer shows one of the cheapest frontier models. Suggestion: a non-ranked "frontier families not scored" band directly under the ranking showing cost, leaves present and the missing leaf (optionally its E221 u* per bar); no rank changes.

6. **The ±20% concordance in E98/E33 (max/min ≤ 1.20) is narrower than one reading of O11's "±20%"** (each report within 20% of the pooled value allows a ratio up to 1.5). The draft chose the stricter reading; ask the owner to confirm.

## 2. Methodology design recommendations
1. Deterministic weight-flip margin per bar and frontier result: the smallest L1 shift of the 60/20/10/10 group weights (or box [0.5×, 1.5×] of nominal weights) that flips qualification or cheapest status, an exact LP using E108 rational arithmetic; a diagnostic under O25.
2. Rule-tier the document: a 1–2 page public summary; the normative spec with a generated "rules in force today" table from the E63 manifest; an inactive-rules appendix.
3. Generate every "Today N" figure from the build with a lint, as E155 does for uncertainty text.
4. Gap-fill provenance as a first-class column, with an AA-only quality sensitivity for rows with fills.
5. Bar population disclosure in the headline: "bar set by retained rows; frontier-only bar: 61.0".

## 3. Questions for the owner
1. May a row whose heaviest leaf (DeepSWE 30%) is a provider's own published result earn a unique-cheapest label, or should it be label-denied like E222 rows?
2. Does O11's "±20%" mean max/min ≤ 1.20, or each report within ±20% of the pooled value?
3. Would the owner accept dropping "confirmed" from interval labels in favour of "cheapest on the published record"?

## 4. Verdict
VERDICT: HAS FEEDBACK
