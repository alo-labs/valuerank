0. Read check
Part 13

First line: ## Governance

Last 12 words: cost (within 1%) and its displayed Index (the page's unrounded Index

Part 14

First line: a point without a captured page is captured within the window, its common revision unverified. **Cohort capture age (E211)**: the AA chart and catalog capture that defines the cohort is at most 7 days old at the release cutoff.

Last 12 words: (not normative); it is in draft-r175.md in the same folder of the repository.

Both parts were read completely to their ends.

1. Findings by severity
Critical

None

High

None

Medium
1. Inconsistent handling of zero-priced API categories in bound domain (E185 vs E109)

Issue: Under Bound domain (E185) in Part 14, the text specifies:

"a zero price in force at V makes $\min r = 0$, so the API bound starts at 0 (an exactly repriced zero cost is "cost not scoreable (zero)", E109) and the Plan bound has no finite upper end."

However, in E170 outcome 3, a superseded-price blocker competes over its current-tariff hull $[C \cdot \min r, C \cdot \max r]$. If a provider drops an API category rate to zero (e.g., promotional or permanent free input caching / free input tokens), setting $\min r = 0$ collapses the lower bound to 0. An API cost of 0 would produce an undefined or infinite value score ($V_i = \beta \cdot S_{C,i} + \dots$ where $S_{C,i}$ uses logarithmic or ratio scaling against anchors). Even if treated as a blocker interval boundary, a blocker cost spanning down to 0 trivially blocks every candidate from receiving a confirmed cheaper-above-bar or frontier label across the entire cohort.

Why it hurts the objective: Allows a single category price dropping to zero to make all competitor interval labels in the ranking "unresolved" or permanently denied, paralyzing ValueRank's interval and label engine.

Concrete change: Clarify under E185 that when a price in force at $V$ falls to zero for a category, the ratio $r$ for that category is evaluated either against a non-zero floor or that $\min r$ is taken strictly over categories with positive prices in force at $V$ (while bounding total category expenditure), or explicitly declare that a zero price in force at $V$ triggers "current-tariff bound unavailable" rather than an unconstrained lower bound of 0.

2. Ambiguity in "Report out of window" handling vs admitted report aging (O32 vs O127 / E212)

Issue: In the Plan evidence lifecycle table (Part 14) and Part 13, the trigger for "Report out of window (O32)" states:

"a counting report's E194 date leaves its cell's admission window (the envelope $[V - 30\text{ days}, V]$ cut at the cell's latest staged search, O161) before it is admitted"

Under Action, it notes: "with fewer than two concordant in-window reports the route is diagnostic and the row takes the next eligible candidate or API cost (E142); a report already admitted at an earlier release (admittedOn) instead keeps counting and ages on its own clock through the rows above, like a measurement (owner decision O127, 2026-10-30)..." However, O11 / O86 requires concordance between $\ge 2$ independent reports. If one report in an admitted pair ages past 30 days while the other was admitted later (or if a cell had exactly two reports and one reaches 91 days / expired), the text does not explicitly define whether the surviving single report continues to provide a valid measured route or whether the pair as an ensemble ages based on the oldest contributor (most advanced contributor's stage).

Why it hurts the objective: If an admitted route's partition stage follows its "most advanced contributor" (the older report), the route could be demoted or put into grace even if refreshed reports are arriving asynchronously, or conversely, a single unexpired report could be left standing without a concordant partner.

Concrete change: In the Plan evidence lifecycle section (E212), state explicitly: "A report partition requires $\ge 2$ non-expired admitted reports to remain an official route. The partition's lifecycle stage is governed by the oldest report required to maintain concordance ($\ge 2$ reports); if aging reduces the pool of unexpired concordant reports below two, the route demotes to diagnostic/API fallback unless replenished."

Low
1. Inconsistent terminology between E329 and E222 regarding cluster bootstrap vs single-run panel

Issue: Under Independent-source checks (E62, split by E66) in Part 14, the text references scores.json fields and states that panel bootstrap uses model-identity clustering (E329). It mentions:

"with a model-identity cluster-bootstrap companion that resamples an identity with all its matched efforts when one repeats (it coincides otherwise; E329, on reviewer 89)"

However, earlier in the same paragraph it states: "two named statistics with configuration-row bootstrap intervals", which creates a slight contradiction between row-level IID bootstrap and cluster-level bootstrap.

Why it hurts the objective: Minor documentation inconsistency that could lead to ambiguity in the verification script or test suite.

Concrete change: Harmonize the wording to: "two named statistics with configuration-row bootstrap intervals and their model-identity cluster-bootstrap companions (E329)..."

2. Methodology design recommendations

Explicit Zero-Price Floor / Exclusion for Current-Tariff Blockers (E185 refinement)

Design: In E185, define $r = \frac{p_{V}}{p_{\text{applied}}}$ strictly for categories where both $p_{\text{applied}} > 0$ and $p_{V} > 0$. If a category has $p_{\text{applied}} > 0$ and $p_{V} = 0$, instead of setting $\min r = 0$ (which collapses the API cost lower bound to 0 and breaks interval labeling), bound the maximum expenditure share of that category using the basket's structural bounds or mark the current-tariff bound as one-sided ($C' \le C \cdot \max r$), leaving the lower bound at $C \cdot \min_{p_V > 0} r \cdot (1 - s_{\max})$ where $s_{\max}$ is the known maximum expenditure share of the zeroed category.

Priority: High.

Clarify Minimum Concordant Multi-Report Survival under O127

Design: Explicitly specify in E212 that the lifecycle stage of an admitted report-based route is determined by the $k$-th newest report where $k=2$ (the minimum concordance threshold). When the second-newest report in a cell hits 91 days (entering grace) or 121 days (demoted), the entire route transitions to that stage, preventing an orphaned single report from sustaining an official measurement route.

Priority: Medium.

3. Questions for the owner

None

4. Verdict

VERDICT: HAS FEEDBACK