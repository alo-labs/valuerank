I've now read all five parts in full. Before drafting the review, let me verify a few real-world benchmark anchors the draft relies on (Public-data constraint: these added quality leaves drive ~30–44 points of quality weight).
0. Read check

All five parts were opened through the GitHub connector and read to their end.

Part 1 — first line: # ValueRank methodology — draft r153. Last 12 words: "carries a logged search whose open-web step is the coverage research (research/2026-10-23-swe-benchmarks/add_track_searches.py)".

Part 2 — first line: - **Full benchmark set (owner decisions O36, O38)**: a cohort configuration is ranked in a ranking only when it has every leaf of that ranking.... Last 12 words: "or provider declined some tasks on safety grounds") also flags "partial component".

Part 3 — first line: - **Capture status (per ranking, E254).** Coding share (E200): the published summary prints.... Last 12 words: "on the Plan basis the workload question is the M_W identification status."

Part 4 — first line: - **Plan cost input (full-utilisation effective cost, labelled)** = API cost input ÷ Value Multiple of the selected route. Last 12 words: "for other Claude models; the transfers keep their assumption label and caution."

Part 5 — first line is blank; first non-empty line: **Report window (E194, O32, E201a)**: the report window is the closed day interval.... Last 12 words: "(no provider marketing quotas otherwise; end-user API-priced reports or SemiAnalysis controlled measurements)".

Scope note: parts 1–5 cover the objective, outputs, source contract, cohort/configuration rules, API cost (basket, admission, completeness, matched-cost diagnostic) and Plan cost (Value Multiple, comparator, report evidence lifecycle). Rules cited from later parts (anchors, scenario streams, Normative definitions) are treated as defined there.

1. Findings by severity

Critical

None.

High

H1. No flag state exists for the realised-influence failure mode that is live in today's numbers. E196 prints cost's value-variance allocation beside the nominal 25% — currently 106% API / 21% Plan in the max-effort ranking and −96% API / −25% Plan in the AI Coding Daily ranking — with an explanatory sentence, but no named release flag. The only flag in this family (E126, "cost not discriminating" / "quality not discriminating") tests the SD ratio 0.25·SD(S_C)/(0.25·SD(S_C)+0.75·SD(S_Q)), which lives strictly in (0, 1) and can sit comfortably mid-range while the covariance allocation Cov(0.25·S_C, V)/Var(V) is negative — the allocation goes negative exactly when Cov(S_C, Q) < −Var(S_C)/3, i.e. when the cost term is net subtractive from value. So in the AI Coding Daily ranking today, the flagship output of a ranking whose objective is "actually lowest cost for the value it delivers" is one where the cost term's realised contribution is to offset quality differences, and nothing in the flag layer says so; a reader sees a printed statistic plus a sentence, while an SD-ratio extreme would earn a named flag. Why it hurts the objective: the two rankings' headline credibility rests on the 25/75 weight meaning something; when its realised direction inverts, the disclosure should be at least as salient as the "not discriminating" states. Concrete change: add an E126-family flag ("cost term offsetting" / "quality term offsetting") per basis when the allocation is outside [0, 100%], and publish the allocation in the existing exchange-rate series. New argument relative to the ledger: this does not recalibrate anchors, change β, or shrink weights (the rejected proposals); the new element is that the SD-ratio flag and the covariance allocation diverge in sign of failure — demonstrated by today's live values — so the existing flag structurally cannot catch this case.

Medium

M1. The E242 transfer tolerance is derived from a slope that only holds in the unclipped cost region. The exchange-rate disclosure (E60) carefully scopes its formula "in the unclipped region", but the tolerance — 2^(threshold ÷ value points per cost doubling) — applies that same slope to every Plan row resting on an assumption. For a row whose Plan cost sits beyond an anchor, the cost score is clipped to 0 or 100, the local slope of value in ln(cost) is exactly 0, and the true tolerance is unbounded until the row re-enters the unclipped region; the printed finite factor then materially understates how wrong the transferred multiple can be. Change: compute the tolerance per row from the row's actual position — piecewise slope, with rows in a clipped region printing "unbounded within clip region; k× to re-enter" — or at minimum scope the printed figure to unclipped rows, as E60 already does for its own formula.

M2. The O116 FrontierCode stand-in inherits USD-1 chart-label rounding with no precision gate. The stand-in unit's values come from a chart whose labels are "rounded to USD 1", treated as rounding intervals — the convention the draft applies to ITBench-AA chart totals. For a low-cost configuration a ±$0.5 interval on a single-digit total is a large relative error, and the stand-in exists precisely in the ranking where cost evidence is thinnest (today the AI Coding Daily ranking has the Coding Agent Index priced for only 3 of 16 rows), so rounded chart values could decide both admission and scores there. Change: admit the stand-in only where its rounding interval is within a published fraction of the panel's median component cost, and check at capture whether the underlying FrontierCode payload carries unrounded totals (the Index evaluation fields are captured unrounded; if FrontierCode's are too, the rounding treatment and this concern disappear).

M3. The report intake route (E244) has no anti-gaming resistance. Admission under O11 needs two independent concordant reports; E223 defines independence as distinct observers with no shared upstream source. The GitHub issue form collects self-asserted fields (exact model, tier, API-priced usage) with no evidence artifact, so two coordinated submissions — the obvious attack on a public ranking with commercial stakes — pass every build check the draft defines. Change: (a) require an attached artifact (meter screenshot or provider usage-ledger excerpt) hashed into the evidence bundle; (b) admit a route only if at least one of the two counting reports was discovered organically in the staged O71 search rather than submitted through the form; (c) keep an observer registry so a repeat observer with a track record is distinguishable from two fresh accounts. All three are implementable on public artifacts.

M4. Owner decision challenge (O24): the Terminal-Bench double pricing is row-specific, so disclosure does not neutralise it. Terminal-Bench 4.0 is costed twice in C_W — the AA Index run and again inside the Coding Agent Index's pooled total — while its quality leaf enters once. The ledger records "overlap disclosed"; the new argument is that the second count is executed under vendor agents (O123), so the duplicated share carries agent token overhead that the quality side never measures, and the distortion varies by row (a configuration efficient at terminal tasks but run under a token-heavy agent is penalised twice on the same task family). A fixed double weight would be a disclosure matter; a row-correlated double weight silently reshapes cost ordering. Change if the owner reconsiders: when the Coding Agent Index is admitted, price its Terminal-Bench portion at the AA Index-run cost (both are public) instead of counting both; if both stay, publish a per-row "terminal-task double share" beside the E200 coding share, as E203 already does for unrewarded share.

M5. Discovery blind spots are provider-correlated, so "no concordant pair found" is partly a coverage artifact. The build environment recorded reddit (mirrors only), X, Zhihu, LINUX DO search, GitHub search and YouTube as unreachable. End-user allowance reports for the Chinese-provider plans (Kimi, Xiaomi/MiMo, MiniMax — exactly the rows sitting on O46 quota ceilings or API fallback) live disproportionately on Zhihu and LINUX DO, so those providers face a structurally lower probability of ever graduating from ceiling/fallback status than Anthropic or OpenAI. Change: publish a per-provider discovery-coverage field (sources reached/unreachable, mirrors used) beside each cell's outcome in planAllowanceCells, so the reader can tell "searched well, nothing found" from "searched where the evidence is not".

Low

L1. E248's justification sentence is stronger than the construction. "A row between them cannot be told apart from either" is not true in general: for two plan rows of one configuration separated by a certain value gap D, a third-configuration row between them faces the same pairwise threshold T = 1.96√(SD_X² + SD_c²) against both, and if D > T with the row within T of the nearer plan row, it is separable from the farther one. The band invariant holds anyway because bands are built forward and the span clause handles large gaps, so this is a wording fix: delete the causal sentence and state the extension as a convention that keeps a configuration's plan rows contiguous in the band order.

L2. The added leaves' structural pins are thinner than the AA pins. The draft pins LiveBench 2.0 by release (2026-10-23) and relies on its seven categories — including "Long Agentic" for the O122 coding share — and on LiveBench's "own weighted Overall"; public trackers I checked describe LiveBench's design as about 1,000 questions across 6 categories and 18 tasks and list current category names (Coding, Agents, Reasoning, Math, Knowledge) without a "Long Agentic" entry. And Vals ships two confusable products: the pinned "Vibe Code Bench v1.1" board and "Vibe Code Bench 1-100", released 2026-09-17, which measures multi-turn app evolution and is scored very differently. The E237 comparability record pins version strings; change: extend it to pin category names and the Overall's published weights for LiveBench, and the board identity (v1.1 vs 1-100) for Vals, so a silent taxonomy change trips the O68/O59 machinery instead of silently recomputing.
tomrochette
+3

L3. Influence diagnostics will flicker at current panel sizes without a series view. With 8–16-row panels, the E126 SD ratio, the E189 allocation and the cost/quality ordering τ_b will move materially release to release from single-row changes. The exchange rate is already published as a series; add the influence ratio, allocation and flag states to it so drift is visible rather than appearing as silent flag toggling.

2. Methodology design recommendations

Realised-influence flag family (implements H1). Per ranking and basis: flag "cost term offsetting" when allocation_C ∉; publish allocation and the E126 ratio in the existing exchange-rate time series. No score, anchor or weight changes — disclosure only, so it clears the rejected-proposals boundary.
0

Clip-aware tolerance and exchange-rate localisation (implements M1). Define tolerance_i = 2^(threshold / s_i) where s_i = |dV/d ln C| at row i (0 in clipped regions → print "unbounded within clip region; re-entry factor f"), replacing the single fleet-wide figure; reuse E60's existing unclipped-region scoping language for consistency.

Rounding-precision gate for chart-label stand-ins (implements M2). Admission condition: stand-in inadmissible for any panel row whose rounding half-width exceeds x% of the panel median component cost (publish x, e.g. 10%); capture-side check for unrounded payload fields first.

Intake hardening (implements M3). Artifact-backed reports hashed into the bundle; admission requires ≥1 organically discovered report per O11 pair; observer registry with history. This preserves the current comparator and pooling unchanged.

Agent-overhead bridge diagnostic (new, extends O123's S2 stress). Since FrontierCode's own chart total and the Index-run Terminal-Bench cost are both captured and agent-free, publish per row b_i = CAI cost − (agent-free FrontierCode total + Index-run TB 4.0 cost), with the SWE-Atlas QnA remainder noted as non-separable, as an upper-bound estimate of vendor-agent token overhead inside C_W. Unevaluable pieces stay labelled as such; rows are never re-scored. This gives API buyers (who supply their own agent) the decomposition the objective implies, from data already captured.

Task-family multiplicity disclosure (implements M4's fallback). If O24 stands, extend E200's coding-share block with the share of C_W carried by the twice-costed Terminal-Bench executions, per row, beside the median/range.

Discovery-coverage output (implements M5). Per provider: sources reached, unreachable, mirrors used; printed beside each no-pair outcome so assumption/fallback persistence is interpretable.

Structural pins for added leaves (implements L2). Registry-pinned category list and weights for LiveBench 2.0 Overall; board-identity assertion for Vals v1.1 vs 1-100; build stops on mismatch, migration by O68.

3. Questions for the owner

On H1: Is a negative or >100% realised cost allocation an acceptable steady state for the headline, or should it trigger a named release state as E126's SD-ratio extremes do? If the owner views the allocation as purely informational, I would re-grade H1 as Low.

On M4 (O24): Is the Terminal-Bench double pricing a deliberate up-weighting of terminal-task cost efficiency, or an artifact kept pending separability? If deliberate, my recommendation collapses to the multiplicity disclosure (recommendation 6) only.

On M2: Does AA's FrontierCode data payload carry unrounded cost fields like the Index evaluation fields do? If yes, the stand-in should be captured unrounded and M2 closes.

On recommendation 5: Is an agent-overhead bridge (agent-free component costs vs pooled CAI cost) within the intended meaning of "recommendations implementable from public data refreshed routinely", given the remainder is non-separable? If bridges of this kind are out of scope, recommendation 5 reduces to the existing O123 stress.

4. Verdict

VERDICT: HAS FEEDBACK