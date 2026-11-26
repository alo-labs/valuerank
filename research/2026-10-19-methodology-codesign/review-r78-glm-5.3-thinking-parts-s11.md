Part 11 read to its end. Now reading part 12.
Both parts read to their end. Before writing the review, I'll verify two numerical fixture claims in the parts (the kernel-check fixture's uniform/arcsine qualification rates) and ground one external premise (tbench.ai's agent-keyed leaderboard, which the E19 harness-stress band depends on).
The kernel-check fixture's numbers verify exactly (uniform 91.47%, arcsine 86.75% vs the draft's "about 91.5%" and "about 86.7%"). Now a quick web check on the tbench.ai premise behind the E19 harness-stress band.
0. Read check

Both listed parts were opened through the GitHub connector at commit fb080b5db88dfb22a45792636fb340ff404ceddc and read to their ends (blob SHAs 30429b08… and 58d40567… respectively).

Part 11 — first line (opening): " - Noise-margin companion (owner decision O44, kept over a per-candidate margin as O128, 2026-10-30): because each bar is a configuration's own displayed quality (O34), the cheapest row at a bar can be its setter, an answer a 0.01-point move could change. …" — last 12 words: "maximum (with consumption-dependent payments the multiple ratio is not assumed ≤ 1)."

Part 12 — first line (opening): "- Harness stress branch (E19, premise corrected by E227). Bug Hunt runs on vendor CLIs, AI Coding Daily on a harness chosen per model, and tbench.ai's matched rows mostly on vendor agents; Vals and LiveBench run one harness for every model; since O37 the Terminal-Bench leaf is AA's own run on one harness (mini-SWE-agent), so only a tbench.ai gap fill carries an agent. …" — last 12 words: "or definite result; every cost check reads C_W, never the Index diagnostic."

1. Findings by severity

Verification note first: I numerically verified the part 11 kernel-check fixture (uniform draws 91.47%, arcsine 86.75% vs the draft's "about 91.5% / about 86.7%") and hand-checked the E89 dominated-corner fixture, the E43/E50 interior-witness regressions, the E221 u* algebra, and all O28 Omniscience vectors — all correct. The findings below are the residual issues.

Critical

None.

High

None.

Medium

Bug Hunt record: harness-specific mean vs cross-harness pooling is ambiguous. Part 12's E29 states "The measurement is the mean of the published runs for the exact model, effort and harness (pooled fixed/105 per complete run…)", while the in-force E206/E222 rule keys the record on (roster name, effort), "harness by largest N", as the "largest-sample owner mean … over every harness and route". Two readings are possible: (a) select the largest-N harness, then pool runs within it — compatible with E29; (b) pool runs across every harness and route at the name/effort. These give different published values exactly where it matters: E224's own cross-harness example shows a 7.7-point spread (Gemini 4 Argon 40.7 vs 33.0), and external evidence shows same-model cross-harness swings of 8–18 points on terminal benchmarks. Why it hurts: Bug Hunt carries 8 quality points in the max-effort ranking (O61) and 12 in AI Coding Daily (O55); an estimand stated two ways threatens reproducibility of the published record and the defensibility of the exact-variant rule. Concrete change: add one sentence to the E29 paragraph fixing the selection rule (e.g., "the record is the mean of runs at the exact roster name and effort on the harness with the largest N (E222/E206); per-harness means and cross-harness differences are diagnostics (E224)") and publish each record's harness/run composition beside the leaf.
artificialanalysis
+1

The noise-margin companion's 1.96·√2 calibration does not match its own comparison. Part 11 defines the margin as 1.96 × √2 × the median analytic quality SD, explicitly "about 1/0.75 times the separability threshold". But the same part (E52) states the frozen bar level "has no uncertainty of its own" (Q_r ≡ H). A √2 factor calibrates the difference of two independent uncertain quantities — correct for adjacent-rank separability, wrong for one uncertain quantity (a row's displayed quality under reporting precision) against a constant. Using 2.77·SD instead of 1.96·SD overstates the margin by ~41%, so the companion reports "none clears the bar by the margin" more often than a 95%-style intent implies; today's 3.5-point margin would be ~2.5 points at 1.96, which can flip the named configuration. This is not a challenge to O128 (the single margin stays); only the constant is at issue. Concrete change: recalibrate the companion to 1.96 × median SD (keeping 1.96√2 for the pairwise separability threshold), or add one sentence recording that the companion deliberately reuses the pairwise calibration as a conservative choice, and record the basis (a margin_basis field beside the existing displayedCheapest…bars[].margin).
snorkel

The Omniscience reconstruction formula's inputs are undefined. Part 12: "The reconstruction I = 100 [A − h (1 − A)] from AA's accuracy A and conditional hallucination rate h is tested against AA's published index each release". The identity I = 100(c−i)/T holds only for specific denominators — A = c/T (correct over all questions, abstentions counted against) and h = i/(T−c) (incorrect share of non-correct). Under the natural readings (accuracy over attempted, hallucination over answered) the formula fails: with the part's own vector c=60, p=0, i=10, a=30 it yields ≈54.3, not 50. Why it hurts: a per-release reconciliation test whose inputs are not pinned cannot be reproduced by a reader and can pass or fail for the wrong reason. Concrete change: state A's and h's exact denominators (and where partials p enter — nowhere but T), and add the c=60/i=10 vector as a worked test beside the existing O28 vectors.
artificialanalysis

Low

E276's "a candidate never shares it" is asserted, not checked. The claim that a candidate never shares a shared cost factor holds only if every row covered by a model's price list or a registered pricing omission is itself blocker-classified (O29, E222, O94). Part 11 already asserts separability per release (E89); extend the same per-release build assertion here: fail the build if a non-blocker candidate shares a registered shared factor.
snorkel

E19's harness-mismatch band rests on two unregistered assumptions. The band is estimated from same-model cross-agent spreads on the tbench.ai leaderboard and applied to Bug Hunt, AI Coding Daily and Terminal-Bench gap fills. External evidence shows harness effects are pair- and direction-specific — Codex CLI beat Terminus 2 in 10 of 10 same-model pairs (median +9.65) while Gemini 3 Pro reversed (65.8 vs 73.9) — so a pooled spread is only a rough magnitude, and a terminal-benchmark spread need not transfer to Bug Hunt or AI Coding Daily. It is stress-only and never in Θ, which is acceptable; but the registry entry should record both assumptions (cross-benchmark transfer; pooling across agent pairs regardless of sign), and the stress output should print the band's derivation. (The premise itself checks out: the tbench.ai leaderboard is agent-keyed with several models under two agents, and AA's Terminal-Bench run is on mini-SWE-agent, as E227 states.)
artificialanalysis
+4

The cohort-rule paragraph still says "family" where the rule is per configuration. "A family is near-frontier when a plotted configuration's rounded Index ≥ F(c) − 3" and "a near-frontier family is deferred…" predate O33/O51, under which every evidenced effort is its own row and the cohort is configurations. The operational Membership sentence is correct; the surrounding family wording could mislead an implementer into family-level aggregation. Change "family" to "configuration" in those two sentences.
artificialanalysis

2. Methodology design recommendations

Prioritized, all implementable from refreshable public data:

Pin the Bug Bug Hunt selection rule and publish record composition (fixes Medium 1). One sentence in E29 plus a per-record disclosure: harness name, run count per harness, and N — the run count is already recorded, so this is a rendering change to the leaf's provenance output (E57 already publishes harness per leaf).

Dual-calibrate or document the O44 margin (fixes Medium 2). Either publish both margin (1.96·√2·median SD, pairwise, as today) and margin_row_vs_bar (1.96·median SD) in displayedCheapest, or keep one value with an explicit margin_basis field; the separability threshold is untouched.

Pin the Omniscience reconstruction (fixes Medium 3). Add "A = c/T, h = i/(T−c), partials counted in T only" to the E28 paragraph and one worked vector to the release tests.

Per-release shared-factor assertion (fixes Low 1): a build check, modelled on the existing per-release separability assertion, that every row covered by a registered shared factor is blocker-classified.

Register the E19 band's derivation (fixes Low 2): the registry entry names the tbench.ai capture, the agent pairs used, the pooling rule, and the cross-benchmark transfer assumption; the S2 output prints the band value and its source capture date.

Terminology fix in the cohort rule (fixes Low 3): two word substitutions, no behavioural change.

3. Questions for the owner

For the Bug Hunt record, does E206 mean pooling runs across every harness and route at the exact name/effort, or selecting the largest-N harness and pooling within it? The answer decides whether finding Medium 1 is a wording fix or an estimand change — given 7.7-point cross-harness spreads, pooling mixes measurement conditions in the point estimate while E19 only stresses them in S2.

Is the √2 in the O44 companion a deliberate conservative reuse of the pairwise separability calibration, or unintended? The answer decides between recalibrating to 1.96·SD and documenting the conservative choice.

4. Verdict

VERDICT: HAS FEEDBACK