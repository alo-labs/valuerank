0. Read check

Both listed parts were opened through the GitHub connector at commit fb080b5db88dfb22a45792636fb340ff404ceddc and read to their end.

Part 1 (draft-r160-part-1-of-14.md) — first line: # ValueRank methodology — draft r160. Last 12 words: "re-capture; applying O145 moved the release cutoff (O65) and re-captured every source."

Part 2 (draft-r160-part-2-of-14.md) — first line: - **Two rankings (owner decisions O52, O53, O54)**: ValueRank picks the benchmarks and ranks the configurations that have all of them, balancing the number of benchmarks against the number of configurations ranked; the cohort does not set the spread of benchmarks (O52). Last 12 words: "is published without a synthetic total. The basket itself is unchanged (O15)."

1. Findings by severity

Critical

None.

High

O145 retention was not propagated to population statements that assume every cohort row is plotted on or near AA's frontier. Two symptoms in these parts:

Part 2's excluded-set partition claims "five classes that partition the excluded set; the build checks it," but the five classes enumerate only 8 of the 12 excluded configurations (4 frontier-family primaries + 4 non-primary rendered-frontier points). The four unnamed rows — Claude Haiku 5.5 (xhigh), Claude Sonnet 5.5 (xhigh), GPT-5.6 Luna (low), MiniMax-M3.1-Flash (max) — are exactly the O145-retained rows that lack both rankings' sets; they carry the "left cohort" inclusion reason and fit none of the five plotted-position classes. Either the "partition" claim or the build check behind it is wrong; if E282's O145-implementation record was meant to cover this, the rendered text has not caught up.

Part 2's frontier-families diagnostic states "Under O51 every cohort row carries such a reason, so both diagnostics equal the primary outputs today." With O145, 10 cohort rows carry a "left cohort" reason instead of a frontier/near reason, so the E187/E199 populations now cover 27 of 37 cohort rows and the equality claim no longer follows. The same section's "each row publishes its inclusion route (on the rendered frontier, or near it)" also now names only two of three routes.

Why it hurts the objective: these are current-figure claims in a draft whose own standard (E265) is that every current figure is build-rendered and checked; a false "diagnostics equal primary" statement misleads readers about the headline bar's robustness, and a partition missing a third of the excluded set misstates the ranked population's composition. Concrete change: make inclusion route a machine-checked enum {frontier, near, retained-left-cohort}; extend the excluded-set partition to a sixth "retained, left cohort" class (or fold retained rows into the plotted classes with a retention flag); re-render the E187/E199 equality claim from the build.

Medium

The separability prose contradicts its own count and part 2. Part 1 prints "today 2 and 0 API pairs, because no ranking has a subset row" for crossWorkloadAdjacentPairs, but part 2 states MiMo-V2.6-Pro is on the subset workload in the max-effort ranking (8 of 9 rows on the main workload), and the reported figures — 2 cross-workload pairs, and "1 of 6 adjacent API ranks separate" (8 adjacent pairs minus the 2 cross-workload ones) — only reconcile if a subset row exists. The reason clause is stale. Why it hurts: the published explanation of a headline uncertainty diagnostic is wrong, so readers cannot tell which figure to trust. Change: render the clause from the build (e.g. "the AI Coding Daily ranking has no subset row; the max-effort ranking has one, MiMo-V2.6-Pro") or remove hand-written explanatory prose the build does not generate.

Plan-row evidence categories are reported only marginally, never jointly. Part 1 gives 14 of 27 / 42 of 67 rows on an owner assumption, 21 and 60 on a possibly-superseded/expired route, 3 and 12 in an accounting-fault window, 21 and 60 without a recorded valuation basis, and 2 and 3 on API fallback. These overlap heavily (an owner-named transfer shares its donor's flag under O89, for instance), so a reader cannot compute how many plan rows rest on no assumption, no flag and a recorded basis — possibly zero, which the text never says. Why it hurts: the Plan basis is the only output plan buyers get, and its "exploratory, no claim supported" status is justified by exactly these counts; without a joint decomposition that justification is unauditable. Change: publish a per-plan-row status bitmask (owner transfer / O46 ceiling / measured-unidentified-M / API fallback / superseded-or-expired / accounting-fault / basis-unrecorded) with counts by combination in scores.json, and print the number of fully clean rows even when it is zero.

E158's cost-boundary verification predates the AA v5 migration and the O137 basket change. The boundary record was "verified 2026-10-19 on AA's methodology page"; AA Intelligence Index v5.0 published around 2026-10-27 (O132), and O137 swapped basket components (GDPval-AA, SciCode, AA-LCR out; FrontierCode 2.0, Terminal-Bench-Science in) precisely because v5 pages changed what they publish. The only component with a verified boundary (GDP.pdf) was verified pre-v5, and the v5-era components have never had their boundaries checked — even though AA's current pages publish detailed per-task cost breakdowns by token class, so the information may now exist where it did not before. Why it hurts: the objective's core claim is "lowest cost for value in practice," and the boundary record is what tells the reader which dollars (judges, tools, environment) the basket figure excludes; a stale record quietly weakens it. Change: make boundary verification a per-component, per-source-version record; build-check that each admitted component's verification date is not older than its captured source version, and re-verify on every basket migration.
artificialanalysis

The O123 agent confound is unquantified in the release. The Coding Agent Index is a vendor-agent run whose pooled cost includes the agent's token use, while the matching quality leaves (FrontierCode 2.0, Terminal-Bench) come from AA's own model runs — the draft states this — and the S2 stress that would isolate the agent effect h_a is "unevaluable while no model is listed under two agents (today: unevaluable)." With the Coding Agent Index v2.0 aggregating FrontierCode v1.1, Terminal-Bench 4.0 and SWE-Atlas-QnA-AA across agent harnesses, it is a dominant basket component whose agent overhead differs across rows with no published magnitude. Why it hurts: cost comparability across rows run under different agents directly biases the value score's 25% cost term in an unmeasured direction. Change (implementable now from public data): publish each row's Coding Agent Index share of its total basket cost beside its agent name (complementing E285's cross-workload comparison), plus a one-sentence panel statement of the confound's direction; the h_a stress then fires automatically once any model appears under two agents.
artificialanalysis
+1

Low

The common-leaf diagnostic's weights are cited "at the O55 weights" but printed as FrontierCode 25, Terminal-Bench 20, Bug Hunt 15; O55 as amended by O61 gives 15/11/8 (max-effort) and 21/17/12 (AI Coding Daily), and 25/20/15 is O49's ten-leaf split. Name the governing decision and print the exact ten-leaf vector in scores.json so the citation is machine-checkable.

The claim scope (part 1) describes the ranked population as "configurations AA plots on, or within the near gap of, its rendered frontier"; with O145 the population also includes one-release retained rows, which the claim-scope sentence never mentions. Add "plus one-release retained configurations (O145)" to the parenthetical.

The noise-band fixed rule is stated as "every row is inseparable from its band's first row," but E248's forward-extension convention can break exactly that for a configuration's own plan rows when they span the threshold (the invariant is later guaranteed only "for every row of another configuration"). State the same-configuration caveat where the fixed rule is first stated; no live violation exists today.

In the Cost section, FrontierCode's potential double pricing is explicitly defused ("the two components never price the same tasks"), but Terminal-Bench's is not: Terminal-Bench 4.0 is priced both as its own basket component (AA Index run) and inside the Coding Agent Index v2.0's pooled cost (66 tasks), and O24 keeps both executions. If the O24 overlap disclosure lives in a later part, surface it also at the target-basket listing where both executions are named side by side.

The near-gap edge diagnostic says "today one point inside the edge" and then lists three configurations (and two outside); "one point" means rounded-Index distance 1, not a single configuration. Reword to "at one rounded Index point inside/outside the edge."

Two external checks came back consistent with the draft and are worth recording: the pinned LiveBench 2.0 release of 2026-10-25 with seven categories and LiveBench's own weighted Overall matches public documentation of the 25 October release and its weight scheme (Long Agentic 2×, Coding and Design 1.5×, others 1×), and the Coding Agent Index v2.0's three-benchmark composition matches AA's public index page.
artificialanalysis
+2

2. Methodology design recommendations

Prioritized, all implementable from public data refreshable routinely:

Inclusion-route enum with build-rendered population claims (fixes the High finding and generalizes). Model inclusion reason as a checked enum {frontier, near, retained-left-cohort}; every "today" population sentence — the excluded-set partition, the E187/E199 frontier-families equality, the "each row publishes its inclusion route" sentence, panel counts — is rendered from the build, and the build fails when an enumerated list's length differs from the computed class count. This is the cheap, deterministic fix for the exact staleness class O145 introduced, and it protects the next cohort-widening decision the same way.

Plan evidence joint decomposition (Medium 2). Per-plan-row status bitmask plus a combination-count table in scores.json, with the count of rows carrying no assumption, no flag and a recorded basis printed even when zero. Derived entirely from flags the build already computes, so it adds no new capture burden.

Boundary-verification freshness gate (Medium 3). Per-component verification dates keyed to the captured source version; re-verification required at every basket or source migration (O137-class events); build fails when a component's boundary record is older than its source version. Given AA's current pages publish per-task cost splits by token class, the re-verification is likely to upgrade several "unknown" cells to documented inclusions/exclusions.
artificialanalysis

Coding Agent Index cost-share column and agent-confound disclosure (Medium 4). Per-row share of basket cost coming from the Coding Agent Index, published beside the agent name already required by O123, plus a fixed panel sentence on the confound's direction; the registered h_a stress remains the estimator once a model is listed under two agents.

Weight-vector registry for the O121 diagnostic (Low 1). Print the exact ten-leaf weight vector with its governing decision number and add a build check that cited decision numbers match the printed weights, preventing citation drift like the O55/O49 mismatch.

Prose-from-build for explanatory clauses (Medium 1). Any clause of the form "today X, because Y" must be generated from the same build output as X, or dropped; the "because no ranking has a subset row" clause shows why hand-written explanations rot faster than the figures they explain.

3. Questions for the owner

Do retained (O145) rows keep their original frontier/near inclusion reason alongside the "left cohort" flag, or does the reason become "left cohort" only? The answer decides whether the E187/E199 "equal the primary outputs" claim needs re-rendering (my High finding) or only a clarifying sentence, and how the excluded-set partition should be extended.

Was GPT-6 Astra (medium) a member of the 2026-10-25 release's cohort? It now sits one rounded Index point outside the near gap but is not among the 10 retained rows; if it was in the previous cohort, the O145 retention list appears incomplete and the cohort count is off by one.

4. Verdict

VERDICT: HAS FEEDBACK