Part 13 read completely. Now reading part 14.
Both parts are read to their end. Before writing the review, I'll run one web search to verify a few factual claims these parts make (Python RNG reproducibility guarantees, the Artificial Analysis Coding Agent Index cost metric, and Terminal-Bench's harness).
0. Read check

Part 13 (draft-r178-part-13-of-15.md, read to its end):

First line: "- Interval decision procedure (E40, amended by E43). Interval labels are decided by deterministic, decision-specific feasibility problems over Θ, never from scenario draws."

Final sentence: "widening Θ cannot create a confirmed or definite result; every cost check reads C_W, never the Index diagnostic."

Part 14 (draft-r178-part-14-of-15.md, read to its end):

First line: "## Governance"

Final sentence: "…each chart point linked to a captured page must carry that page's total Index cost (within 1%) and its displayed Index (the page's unrounded Index within half a display unit), and a mismatch stops the build for a re-capture of both (scores.json aaStateReconciliation, E322, on reviewer 87);" — the part terminates on this clause, which continues in part 15 as expected of the 15-way split; this is not a read failure.

Both parts were read in full. Before the findings: I independently re-derived the numerical fixtures these parts state, and they check out — the Omniscience identity I = 100[A − h(1−A)] (vector (60, 0, 10, 30) → I = 50), the E335 repricing multiplier (p′·u/p·u)(p·x/p′·x) including the asymmetric two-category fixture, the E43 interior-witness and E89 dominated-corner fixtures, the E117 workday regression caveat, and the O69 "N hours ago" bound of read-instant minus (N−1) hours (correct for round/truncate/ceil conventions). External checks also corroborate the draft's factual premises: Python documents that only random() with a compatible seeder is stable across versions, with other algorithms subject to change; AA's Coding Agent Index v2.0 does combine FrontierCode v1.1, Terminal-Bench 4.0 and SWE-Atlas-QnA-AA; AA publishes per-evaluation cost-per-task split by input, cache-hit, cache-write, reasoning and answer tokens, which underwrites both O27's per-task cost metric and E176's cache-rate decomposition class; and mini-SWE-agent is a real, runnable harness.
python
+5

1. Findings by severity

Critical

None.

High

None.

Medium

Scoped change detection has no stated failure mode for a disappearing monitored scope. The governance section defines scoped change detection over "pricing tables, rate-limit documentation sections and model-availability matrices, not full-page diffs," with typed records, date discipline ("the build stops on a missing, extra or wrong date") and classification rules — but nothing covers a provider redesigning its documentation so that a monitored section moves, is renamed, or vanishes. If the locator yields nothing, the scoped diff has no content to compare and can silently return "no change," leaving every route that scope covers running on stale evidence until the 30-day "possibly superseded" flag or the 90-day expiry fires — while the remaining backstops (O77 announcements, ≥2 user reports) depend on the change being publicly visible. This weakens the freshness guarantee that Plan labels rest on. Recommendation: add a scope registry (per provider and record type: URL, section anchor or selector, last-verified capture hash) and a rule that a scope whose locator yields no content at a refresh — or whose captured section heading changes beyond a registered similarity threshold — stops the build with a named "scope missing" state, with every route the scope covers treated as change-detection-unresolved (blocking, like an unclassified change) until classified. This mirrors the existing missing-date build stop and O100's classification register, and is implementable from public data refreshed routinely.

Low

Imprecise and redundant rationale in the cohort rule. The sentence "A point cheaper than every rendered-frontier point has no F(c) and is not near-frontier; at that cost it would be on the frontier itself" is wrong as a justification — such a point need not be on the frontier (it may be dominated by an even cheaper plotted point, and if it were non-dominated the rendered frontier itself would be wrong), and the case is anyway unreachable in a passing release: the first rendered vertex is the cheapest frontier point, so any plotted point cheaper than every frontier point lies left of the first vertex and already stops the build under E204. Recommendation: restate the branch as an explicitly defensive default that cannot occur while E204 holds, or fold it into E204. No output changes; this removes a misleading rationale from a rule the build enforces.

Scenario reproducibility depends on the toolchain version. The draft is right that Python guarantees only random() across versions, not the Beta and normal samplers, and it handles this by recording the Python version and treating a version change like a change of draw order. The cost is that a routine toolchain upgrade re-draws every scenario output, and those redraws then flow into bridge and swing attribution as an artificial cause class. Recommendation: vendor the samplers — an explicit inverse-CDF Beta and a Box–Muller (or Ziggurat) normal implemented only over random() — so draws are version-invariant by construction; keep the recorded Python version as a fallback check and demote the redraw bridge class.
python
+1

No standing check for the harness-band precondition. E19's harness-mismatch band and O123's S2 harness-cost stress are both unevaluable on the same unmet condition (no tbench.ai configuration listed under two agents), and both rest on disclosed registered assumptions. The tbench.ai leaderboard is already captured each release, but nothing states that the co-listing condition is re-checked and its status printed. Recommendation: add a build-printed band status (evaluable / unevaluable, with the capture date of the co-listing check) so the transition from unevaluable to evaluable is observed at a release rather than remembered.

E276 wording invites a misreading. "Two rows can still share a cost factor, through one model's price list (two efforts of one model, including a superseded tariff's hull, E183)" reads as if any shared tariff creates a shared uncertain factor that turns rows into blockers ("A row carrying one is a blocker"). As the surrounding clauses make clear, only superseded-tariff hulls (E183) and registered pricing omissions (O94, O98) create uncertain shared primitives; tariffs in force are published constants, not Θ primitives. Recommendation: one clarifying sentence stating that shared Θ primitives arise only from superseded-tariff hulls and registered omissions, both of which are blocker-creating, so no label-eligible candidate can carry one.

2. Methodology design recommendations

Prioritised, all implementable from routinely refreshable public data:

Scope registry with missing-scope build stop (from Medium 1). Concrete shape: data/change_scopes.json with entries {provider, record_type, url, anchor, capture_hash}; at refresh, a locator miss or heading change beyond a registered threshold emits "scope missing: provider/type", stops the build, and marks every covered route change-detection-unresolved until a dated classification. Highest priority: it closes the only silent gap I found in the change-detection stage, which is the main protection between the 30-day flag and expiry.

Vendor the scenario samplers (from Low 3). Implement Beta via inverse CDF and normal via Box–Muller over random.random() only; record algorithm id, seed and Python version in scenarios.generator. This makes published scenario-rank sensitivity (E13) reproducible across environments without treating an upgrade as a redraw, and removes one recurring bridge cause.

Band-status field for the harness stress (from Low 4). A one-line scores.json diagnostic (harnessBand.status, lastCoListedCheck) printed beside E19 and O123's stress; zero cost, converts a latent precondition into an observed one.

E276 clarification sentence (from Low 5). Textual only; it protects future reviewers from misreading blocker scope in the separability argument, which is otherwise sound — I verified the shared-factor logic (factors move blocker rows together, never against a candidate; candidates never carry them because the factor covers every effort of its model) and the E273 donor-multiple unresolved rule covers the one cross-row factor the Plan basis can create.

Worst-case elapsed-age companion. E314 already discloses that calendar-day counting admits up to ~24 hours of slack past a boundary; a one-line companion in the freshness section ("30 days = 30 whole UTC calendar days ⇒ up to 30d 23h59m elapsed") would let readers of the published outputs see the effective bound without reading the spec. Lowest priority.

3. Questions for the owner

Should a missing change-detection scope (provider docs redesign) stop the build, or only flag the routes it covers? My Medium 1 assumes stop-or-block; a softer flag would change the recommendation's severity and mechanics.

Is vendoring the scenario samplers acceptable, or do you prefer keeping Python's own samplers with the version-recorded redraw rule as the standing design? My Low 3 assumes vendoring is acceptable.

4. Verdict

VERDICT: HAS FEEDBACK