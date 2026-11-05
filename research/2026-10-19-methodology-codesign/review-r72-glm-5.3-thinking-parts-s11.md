0. Read check

Part 11 (draft-r154-part-11-of-13.md, read to its end):

First line: "- Interval decision procedure (E40, amended by E43). Interval labels are decided by deterministic, decision-specific feasibility problems over Θ, never from scenario draws."

Last 12 words: "or definite result; every cost check reads C_W, never the Index diagnostic."

Part 12 (draft-r154-part-12-of-13.md, read to its end):

First line: "## Governance"

Last 12 words: "the standard tariff is publicly documented and the consumption ledger supports repricing;"

Both parts were read to their ends (part 12 ends mid-sentence at the split point, continuing into part 13). The material reviewed below is limited to what these two parts state.

1. Findings by severity

Critical

None.

High

The v1 separability assertion (E89) is in tension with declared shared cost factors, and the joint-tariff case is unspecified. Part 11 opens by declaring "a box of declared shared factors, e.g. a common price list or a donor multiple shared by several rows," then asserts "In v1 every row's C and Q come from distinct published records, so the condition holds and is asserted per release," naming the donor multiple as "the one cross-row factor the Plan basis can create." Record provenance does not establish constraint disjointness. Under E183, B_W rows (priced on a tariff not in force at V) enter interval outputs "over their current-tariff hull," and under O94/O98 rows with an AA-documented pricing omission range over [C, factor × C] or [C, ∞). If two or more rows derive their cost range from the same tariff vector or the same shared pricing-term omission, their feasible variation is jointly constrained; treating each row's hull as an independent per-row box is exactly the "enclosing box containing a favourable state the original constraints exclude" case that part 11's own release fixture says must never return a certified possible membership. Why it hurts the objective: a certified-possible (or denied) frontier/cheapest-above-bar label decided on per-row boxes could pair two tariff-linked rows at mutually incompatible price points, producing a wrong label that the certification machinery then vouches for. Recommended change: state explicitly whether B_W hulls and O94/O98 ranges are implemented as per-row intervals or as shared primitives in Θ; make the rule that a shared tariff lineage or shared omission factor among a decision's candidate rows is a shared factor (→ branch-and-bound, or unresolved like E273, never corners); and add a release fixture with two rows sharing one price-vector primitive in which a corner state pairs incompatible tariff points and must not certify possible membership.

Medium

The E19 harness-mismatch band transfers an agent-effect estimate across benchmarks without a within-benchmark check. The band is estimated from same-model cross-agent spreads on the tbench.ai leaderboard and applied to Bug Hunt (vendor CLIs), AI Coding Daily and a Terminal-Bench gap fill. Two problems. First, tbench.ai's board ranks agent–model pairs, not models, and cross-agent spread there is measured on Terminal-Bench task distributions with its agent roster — not on Bug Hunt's vendor CLI runs. Second, harness effects are demonstrably benchmark- and pair-specific: the same Claude Opus 4.6 scored 58.0% under Claude Code and 76.4% under Meta-Harness on the same Terminal-Bench 2.0 tasks, and the direction of the vendor-agent advantage flips by model (Gemini 3 Pro scored higher under the generic harness than under Gemini CLI); even frozen-model work shows harness ranking is itself unstable across setups. Since the branch is S2-only and never enters Θ, this cannot corrupt labels, but a miscalibrated published "stress" understates or overstates the real exposure and misleads readers about robustness. Recommended change: derive a second, Bug Hunt-internal cross-harness band from the E224-style data already published (Gemini 4 Argon 40.7 vs 33.0), publish both bands per leaf (tbench-derived and within-benchmark), and state which band each agent-run leaf uses.
tbench
+2

The O69 age-rounding assumption is asserted, not evidenced, and is unsound if a board ceils. Part 12 tests a row shown "N hours ago" as "no later than the read instant minus (N − ½) hours (the board rounds the age)." If a board rounds or truncates, this bound is valid or conservative; but if any board displays a ceiling (age ∈ (N−1, N]), the (N−½)-hour lower bound on age is too large, and a row timestamped after the cutoff could pass the pre-cutoff test and contaminate a leaf at release. Why it hurts: the whole O60/O69 machinery exists to guarantee that post-cutoff rows never enter a release, and this is the one bound resting on an unrecorded behavioural assumption about a third-party UI. Recommended change: pin each board's age-display semantics (round / truncate / ceil) in the registry with captured evidence, as E175 does for dates; where semantics are unverified, fall back to the conservative N−1 bound or a date-only test.

Low

The O77 announcement-monitoring surface is not specified. Part 12's scoped change detection covers "pricing tables, rate-limit documentation sections and model-availability matrices, not full-page diffs," and separately triggers on "the provider announces a change" — but the part does not say where announcements are monitored (provider blogs, changelogs, status pages). A limit change announced only in a blog post and reflected in a moved or renamed page section could be missed between captures. Recommend enumerating the monitored announcement surfaces in the registry, so the O77 trigger is auditable.

The E29 pooling notation is ambiguous. "Pooled fixed/105 per complete run" does not state whether pooling across runs is run-equal (mean of per-run means) or task-weighted; with unequal run counts or unequal per-run task coverage the two differ. E206 governs record selection, not pooling weights. Recommend one sentence defining the pooling estimator precisely.

The E15 workday diagnostic publishes a single calendar point. M_workday/M_full is computed on one pre-registered 40-hour week and one versioned calendar; the ratio will move with timezone and weekday pattern, so a single point understates the range for the light users the diagnostic serves. Recommend publishing the ratio under two or three pre-registered calendars (e.g., a 5×8h aligned week and a weekend-heavy pattern). Diagnostic-only, consistent with O3, so low.

2. Methodology design recommendations

(Priority 1) Shared cost-factor rule with a tariff-lineage fixture. Amend the E89/E73 text with: "whenever ≥2 rows in a decision's candidate set derive cost variation from one tariff vector, one registered pricing omission (O100-classified) or one shared donor multiple, that vector is a shared primitive in Θ with its joint constraint; the per-release separability assertion fails and the decision runs certified branch-and-bound or returns unresolved." Add the two-rows-one-tariff fixture from High-1. This is implementable now: the build already knows each row's valuation basis (E170) and the O100 note register identifies shared omission texts, so the shared-lineage detection is a join on (tariff id, note id).

(Priority 2) Dual-source harness band. Compute the E19 band twice: (a) the existing tbench.ai cross-agent spread, and (b) a Bug Hunt-internal cross-harness spread from same model/effort rows across harnesses (E224 data; the Bug Hunt scoreboard is a public bundle artifact). Publish per leaf: band value, source, and the n of same-model pairs behind it; where the two bands differ by more than a pre-registered threshold (e.g., 2 points), print both rather than a maximum, so readers see the disagreement rather than a hidden choice.

(Priority 3) Per-board display-semantics registry entry. Extend the E175-style pinning to age displays: registry field age_display_semantics ∈ {round, truncate, ceil, unknown} with a captured evidence artifact per board; the O69 bound becomes read − (N − δ) with δ = ½ for round, 0 for truncate (conservative), 1 for unknown/ceil. A one-line change to the O69 test.

(Priority 4) Workday calendar grid as in Low-3: two or three pre-registered calendars, each with its own versioned IANA timezone entry, published side by side with the existing single-calendar ratio.

(Priority 5) Announcement-surface enumeration in the registry (blogs, changelogs, status pages per provider), each with capture cadence, so O77 triggers are reproducible.

3. Questions for the owner

Are current-tariff hulls (E183 B_W rows) and O94/O98 cost ranges currently implemented in the build as per-row input boxes or as shared primitives in Θ? The answer determines whether High-1 is a specification change or only a documentation fix plus a fixture.

Has the AI Coding Daily "N hours ago" display behaviour been empirically verified (round vs truncate vs ceil), and can that verification be captured as registry evidence — or should the conservative N−1 bound be used until it is?

Would you accept publishing a Bug Hunt-internal cross-harness band alongside the tbench.ai-derived band for E19, given the branch is S2-only and never enters Θ?

4. Verdict

VERDICT: HAS FEEDBACK