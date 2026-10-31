0. Read check

Part 12 — research/2026-10-19-methodology-codesign/perplexity/parts-r153/draft-r153-part-12-of-13.md

First line: ## Governance

Last 12 words: "article changes nothing until the owner selects it (AGENTS.md; Plan cost, E238)."

Part 13 — research/2026-10-19-methodology-codesign/perplexity/parts-r153/draft-r153-part-13-of-13.md

First line: **Plan evidence lifecycle (E212)** — one table for the stages above (E18, E36, E142, E144, E151, O13).

Last 12 words: "(not normative); it is in draft-r153.md in the same folder of the repository."

Both parts were opened through the GitHub connector at commit 0ab322c… and read to their ends as returned. I spent the remaining tool budget on the mandated file reads and did not use web search; the findings below therefore rest on the parts' own text plus internal consistency and arithmetic checks. Part 12 covers Governance (E18 change detection, E142 route order, E177 swing attribution, E168 amount lineage, E216 freshness, E265 figure rendering, O59/O60 source clocks, O69 row dates, E217/E211 capture gates, E141 tariffs, E170/E185/E202/E222 valuation gate, E87 dispersion, release gates, E62/E66 independent checks, E63 manifest, O56 convergence, SemiAnalysis watch). Part 13 covers the E212 Plan lifecycle table, fault-window handling, Known limitations, and the revision-history note.

1. Findings by severity

Critical

None.

High

Plan measured evidence is structurally transient (Owner decision challenge: O32, O112). Part 13's lifecycle table rebuilds report partitions strictly from the window 
[
𝑉
−
30
d
,
𝑉
]
[V−30d,V] with no grace ("a counting report leaves through the O32 row (at day 31, with no grace)"), while OpenAI's ~2-day global meter resets (O112) exclude almost every user reading, so OpenAI's flagged routes "are unlikely to be replaced by a report pair before they are demoted at 121 days." Combined with the monthly cadence, a route admitted on two concordant reports has roughly one release of tenure before its partition breaks — even when nothing in the world changed — and Plan rows oscillate between measured multiples and API fallback, while OpenAI routes march irreversibly toward demotion. This hurts the objective directly: the Plan ranking's measured share decays by construction, and release-to-release comparability degrades for reasons unrelated to provider behaviour. The parts already disclose the symptom (21 of 27 and 44 of 51 plan rows on flagged or expired routes) but offer no stabiliser. Concrete change: (a) grant an admitted concordant report pair a measurement-like tenure — stage clocks from the older supporting report's date under the E151/O13 clocks (90 days + grace), with only in-window reports allowed to change the figure, and expiry/demotion rather than partition-loss as the exit path; (b) for reset-prone meters, admit paired readings (two observations inside one inter-reset interval, end minus start) as a report observation, since such a pair's span lies wholly between resets and therefore satisfies O112 as written. Both are implementable from routine public evidence.

Medium

E265's stale-figure lint provably misses figure classes present in these very parts. The lint's triggers are datedness heuristics plus "N of M" counts, cohort-thing counts, and dollar amounts. Percentage and ratio figures tied to the current release — e.g., part 12's "34% independent weight in the max-effort ranking and 22% in the AI Coding Daily ranking," "factor of 1.10" comparability trigger context, quota/weight shares — fall outside every enumerated pattern, so a hand-typed or stale value there cannot fail the check even though E265 intends "every current-release figure" to be a placeholder. Concrete change: extend the lint grammar to percent signs, ratio/weight shares, and "$\times$" multiples occurring in current-release sentences, and require that any such sentence resolve its numbers from scores.json/figures.json or carry an explicit at O<n>/date anchor.

The two rankings share rows with no published agreement diagnostic between them. Known limitations states that a configuration ranked in both rankings "has two values" and that values, ranks, bands and bar results "are not comparable," then stops at disclosure. With 9 and 16 ranked rows and a nonempty overlap, a reader cannot tell whether the two rankings substantively agree or the value signal is set-dependent. Concrete change: publish, beside the rankings, a descriptive overlap agreement statistic — Kendall τ_b between the two value rankings on rows ranked in both, plus the count of shared-row rank inversions — in the same spirit as the E62/E66 matched-panel checks (descriptive only, no scenario share). If this already lives in another part, disregard; I found no reference to it in parts 12–13.

E177's naming rule leaves attributable-but-unexplained swings. Attribution succeeds when the replay residual is within 10⁻⁶ and "every step carrying more than 5 points names the changed bundle fields." A swing of −7 composed of three steps of −2.4, −2.4, −2.2 has residual ≈ 0 and no step over 5, so it is "attributed" with no named cause at all — passing its own gate while failing the audit purpose E177 exists for. Concrete change: when a row's total |Δ| exceeds the 5-point gate, additionally require that the named steps account for at least 80% of |Δ| (largest-first), with the remainder reported as an aggregate named "small-step remainder."

Low

The Plan-side hull in E170 appears looser than necessary. If Plan cost 
𝑃
=
𝐹
gross
/
𝑀
P=F
gross
	​

/M with the cash fee unchanged by a tariff change, then 
𝑀
′
/
𝑀
∈
[
min
⁡
𝑟
,
max
⁡
𝑟
]
M
′
/M∈[minr,maxr] implies 
𝑃
′
∈
[
𝑃
/
max
⁡
𝑟
,
  
𝑃
/
min
⁡
𝑟
]
P
′
∈[P/maxr,P/minr], but the part publishes 
𝑃
′
∈
[
𝑃
⋅
min
⁡
𝑟
÷
max
⁡
𝑟
,
  
𝑃
⋅
max
⁡
𝑟
÷
min
⁡
𝑟
]
P
′
∈[P⋅minr÷maxr,P⋅maxr÷minr] — wider by up to 
(
max
⁡
𝑟
/
min
⁡
𝑟
)
2
(maxr/minr)
2
. It is diagnostic-only and valid as an enclosure, but the derivation should be printed and, if 
𝑃
P truly has no further 
𝑟
r-dependence, tightened to the sharp interval (with E185's domain conditions unchanged).

E62/E66 panel statistics lack a floor. "A panel with insufficient rank variation returns 'undefined'" is unquantified; on a 9-row ranking the matched panel could be small enough that a bootstrap τ_b interval is all width and no content. Concrete change: fix a minimum panel size (or equivalently a maximum published CI width) before printing (a)–(c), and say "panel too small" rather than printing an uninformative interval.

The 1.10 different-metering-basis comparability trigger is an unmotivated constant. Tokenizer and provider-count differences vary by task mix; a fixed 1.10 can both over-warn and miss genuine mis-rankings. Concrete change: derive the trigger from measured cross-tokenizer cost dispersion over the basket's own demand mix and publish the derivation alongside it.

Plan freshness metrics belong beside the table, not only in Known limitations. The fallback/flagged fault-window counts (2/27, 3/51, 21/27, 44/51) already exist as rendered figures; printing "share of Plan rows on measured routes" as a standing per-release metric next to the Plan table would make the High finding's drift visible to readers without reading the limitations section.

2. Methodology design recommendations

Stabilise Plan evidential tenure (highest priority). Adopt measurement-like clocks for admitted concordant report pairs (E151/O13 clocks keyed to the older report's date; in-window reports may revise, not merely continue, the figure) and add the intra-reset paired-reading report type for meter-resetting providers. Add a release-level guardrail metric: fraction of Plan rows on currently measured routes, printed every release.

Close the E265 lint classes. Extend pattern coverage to percentages, ratios, weight shares and multipliers; add a cross-reference lint that resolves every O-, E- and I- citation in the rendered draft against the decision ledger, failing the build on a dangling or contradicted reference. This also hardens the sectional review process against cross-part drift that no single sectional reviewer can see.

Publish a between-rankings agreement block. On shared rows: τ_b of the two value rankings, inversion count, and a compact side-by-side of rows whose rank moves by more than a stated threshold — labelled descriptive, matching the E62/E66 treatment.

Strengthen E177 as an audit artifact. Residual ≤ 10⁻⁶ plus the ≥80%-named-steps rule from Finding 3; print per row the top named steps in the release notes so swing causes are readable without replaying bundles.

Tighten and derive the valuation hulls. Print the derivation of both the API and Plan hull bounds in the spec (one short paragraph), replace the Plan bound with the sharp 
[
𝑃
/
max
⁡
𝑟
,
𝑃
/
min
⁡
𝑟
]
[P/maxr,P/minr] form if the fee is tariff-independent, and keep E185's domain conditions as the only failure modes.

Ground small-sample diagnostics. Minimum panel size / CI-width publication rule for E62/E66 and the proposed cross-ranking τ_b; derive the metering-base comparability trigger from measured tokenizer dispersion.

3. Questions for the owner

Once two concordant in-window reports admit a Plan route under O11, does the route's figure persist beyond the 30-day window (aging under E151/O13) with partitions newly built only to update it — or is it strictly rebuilt from in-window reports each release as E212's table implies? The answer determines whether the High finding requires O32 to change or only E212's operationalisation.

Is the Plan cost 
𝑃
P in the E170 hull exactly 
𝐹
gross
÷
𝑀
F
gross
	​

÷M with the cash fee fixed across tariff changes (in which case the Low bound-tightening applies), or does 
𝑃
P contain further 
𝑟
r-dependent terms (in which case only the derivation needs printing)?

Is there a whole-draft consistency pass at release time — beyond the per-part review rounds and E265 — that resolves cross-part rule citations? The answer determines whether recommendation 2's lint is new work or already covered elsewhere in the build.

4. Verdict

VERDICT: HAS FEEDBACK