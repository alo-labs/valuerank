0. Read check

I read all 15 parts through the GitHub connector at commit ee35ecf, one call per part, each to its end. The one gap in the whole draft: part 15 says the revision history is omitted from the review copy, so the parts are not the entire 337,803-character file.

First line: # ValueRank methodology — draft r176

Final sentence of each part:

"Today 10 configurations are retained (Claude Haiku 5.5 (max), Claude Haiku 5.5 (xhigh), Claude Opus 5.5 (medium), Claude Sonnet 5.5 (xhigh), DeepSeek V4.1 Flash 1017, GPT-5.6 Luna (low), Gemini 4 Argon, Kimi K3.1 Pro, MiMo-V2.6-Pro and MiniMax-M3.1-Flash), the 2026-10-25 release's cohort members that left at the v5 re-capture, so the cohort holds 37 configurations; applying O145 moved the release cutoff (O65) and re-captured every source."

"Missing stays missing, and a configuration missing a leaf after the search is listed, not ranked (O36)."

"Release assertion: the scored field is the basket sum, not cost per task, not AA's 7:2:1 blended price, not total Index cost."

"Priced-mix coverage (share of quality weight whose leaves are priced in the basket) is published each release."

"…a report route must name the same observers as a passing cell for its plan and model (the build compares observers, not report values);" This sentence continues at the start of part 6.

"Evidence rules unchanged except for two owner exceptions, the O46 MiMo quota ceilings and the O76 speed-mode conversion of a user report (no provider marketing quotas otherwise; end-user API-priced reports or SemiAnalysis controlled measurements)."

"Domain validity is separate from evidence completeness."

The part ends on the AI Coding Daily table row, whose last cell is "points of 60; z = 100 × points / 60". It has no closing sentence.

"Only a genuine deployment-policy mismatch between the quality figure and the priced attempts is reconciled (as a bias bound in the identification layer); repetitions are not a bias."

"Where public evidence cannot separate them the route is labelled "measurement and transport not separable" and its S0 result is not described as target-workload support."

"The population is the non-provisional cohort rows with a displayed quality, ordered by displayed quality ascending, then configuration ID."

"…each ranking's outputs compare that ranking's rows only, so a configuration ranked only in the other ranking is outside them too; the summary says these outputs compare ranked configurations only and names the listed configurations."

"…widening Θ cannot create a confirmed or definite result; every cost check reads C_W, never the Index diagnostic."

"…and a mismatch stops the build for a re-capture of both (scores.json aaStateReconciliation, E322, on reviewer 87);" This sentence continues at the start of part 15.

"Revision history: omitted from this review copy (not normative); it is in draft-r176.md in the same folder of the repository."

I cross-checked the draft's own arithmetic and found no discrepancies:

The bar-reach counts (7/5/3 of 9; 16/11/6 of 20) match the floor((n−1)k/4) positions.

The cost-doubling offsets (3.11 → 4.14, 5.31 → 7.08, 2.71 → 3.61, 4.11 → 5.48) match the 0.75 divisor.

The leaf weights sum to 100 in all three rankings, and the 51% coding share is right.

The 25 ranked + 12 excluded = 37 cohort count holds.

1. Findings by severity

Critical

None.

High

Owner decision challenge (O25, O39, O22): interval and scenario labels certify almost nothing about noise.

Issue: O36 means every ranked row has every leaf, so S1 collapses to S0. The only remaining draws are rounding of published values. The scenario-supported label is issued from the S1 core branch only, which has no weight stress and no task sampling (S1T "never authorises a label"). Part 1 shows 0–2 adjacent ranks separable under task-sampling noise, and the median pair threshold is about 2.7–4.5 value points. A "confirmed cheapest" label therefore means "stable to the rounding of two-decimal records", not "robust to benchmark noise".

Why it hurts: the objective is to say which model is lowest cost for the value it delivers. A label that survives while the answer is inside the noise invites over-reading, even with the E51 wording.

New argument (the ledger records O25 as a scope choice, not this consequence): once O36 holds, the elaborate label machinery (E40–E186, kernel checks, 16 sequential looks) guards only against rounding.

Change: make the O44 noise-margin companion a tri-state part of the label. Use "separated" when the candidate clears H by 1.96·√(σ_i²+σ_H²) and every cheaper possible qualifier fails that test. Use "contested" when a cheaper row is within the margin. Use "rounding-stable only" otherwise. Alternatively, let S1T (with the ρ grid) authorise a separate "noise-robust" label that sits beside the existing one and replaces nothing.

Owner decision challenge (O53, O54, O121): the cost-optimal end of the frontier cannot be ranked.

Issue: the leading rankings cover only configurations with LiveBench/Vals (top effort) or AI Coding Daily. The cheap rendered-frontier points (GPT-6 Luna low, Claude Haiku 5.5 low, GPT-6.1 Terra low) are listed, not ranked. The gate section shows GPT-6 Luna (low) 7.1× below the max-effort low anchor. So "cheapest above a bar" in the max-effort ranking cannot return a low-effort row, and this is the question the objective poses against AA's Pareto frontier.

Why the current mitigation is thin: O143 gives a pointer to cheaper siblings, and the O121 common-leaf ranking carries no labels.

Change: add a pre-registered promotion test for the common-leaf ranking. For example, it becomes label-bearing when τ_b between its quality and each leading ranking's quality on shared rows is ≥ 0.8 over ≥ 8 rows. Until then, print its bar answer in the headline, not only as a diagnostic.

Plan basis: the admission design cannot produce a refreshable Plan claim from public data.

Issue:

The only controlled source is one paywalled SemiAnalysis article from 2026-10-06, which is not in the evidence bundle.

21 of 27 and 60 of 67 plan rows are flagged possibly superseded.

The staged search of 2026-10-25 found no concordant pair for any model and tier.

Strict all-report concordance (O74), 5-hour exclusion (O82) and the monthly three-stage search together make a passing cell rare.

Why it hurts: half the stated objective (subscription economics) has no route to becoming a claim, so the Plan ranking stays "exploratory" by construction.

Change: add the owner-run meter probe in §2 item 3. It is a controlled measurement under O11, repeated monthly.

Medium

Owner decision challenge (O2): the headline "value" score mostly rewards quality, and cost has little influence.

Issue: a cost doubling is worth 3.11 value points (4.14 quality points) in the max-effort API basis, while the quality noise margin is 3.6 points. The AI Coding Daily cost allocation is −56% on the API basis, so dearer configurations rank higher on "value". The exchange rate also depends on the cohort's cost range, because anchors are min/2 and max×2, so it changes whenever a re-freeze changes the range.

The draft discloses this (E196, E60) and rejected anchor recalibration. What is new: the headline name implies cost-efficiency, but it does not deliver it in one of the two leading rankings.

Change: see §2 item 2.

Owner decision challenge (O163): the Bug Hunt leaf mixes scales and is dominated by an unverified component.

Issue: z = planted + unplanted fixes with no ceiling, so z exceeds 100 while every other leaf is clipped to 0–100. In the draft's own fixture (44.3 planted + 65.3 unplanted = 109.6), unplanted fixes are 60% of the leaf. Those are judged by the maintainer's blind judge, with no answer key. The leaf is a single-maintainer, two-repository mean of N runs, with harness chosen by largest N per model. It carries 8–15% weight, which its larger spread can multiply.

Why it hurts: realised influence can exceed the nominal weight, and the model+harness confound is selected by sample size.

Change: publish Bug Hunt's realised spread share against nominal each release, and flag it when it exceeds 1.5× nominal (the E114 pattern, applied per leaf). Add a standing sensitivity with the unplanted term capped at the planted count.

Coding Agent Index cost is confounded by the vendor agent, and the stress test cannot run.

Issue: in the max-effort ranking this component is 16–74% of basket cost. The agent differs by family (Codex, Claude Code, others). The S2 harness-cost stress (O123) is unevaluable while no model is listed under two agents, so the confound is never bounded.

Change: give bar answers a fixed Index-only cost variant (E172 already has the component-removal object). Flag any bar whose cheapest row changes under it, as O162 does for the Bug Hunt harness.

Specification size and conflict rules are themselves a reliability risk.

Issue: the draft is about 338k characters. It resolves conflicts by "later-numbered record governs", and recent rounds (E311–E334, E335–E336) are still consistency fixes.

Why it hurts: the objective needs routine public refresh, and a spec this large cannot be audited by a human between releases.

Change: split into a roughly 30k-character normative core plus appendices. Make the test vectors and fixtures the arbiter of detail, with the prose as commentary.

Low

Terminal-Bench-Science is classified two ways. It is an SDLC cost component (O137) but a "science & knowledge" quality leaf at 1⅔%. The E178 basket-scope branch removes Omniscience, HLE and CritPt but keeps it. State the rationale or align the two classifications.

The SemiAnalysis article is not hashed. O130 re-reads and the transcribed figure table mitigate this, but a dated screenshot hash of the transcription file, published alongside, would let outsiders audit every Claude and OpenAI Plan figure.

Read-copy note. The review copy omits the revision history. This is harmless for review, but the 337,803-character count does not equal the sum of the parts.

2. Methodology design recommendations

Noise-aware bar decision. This is the highest priority and uses only data already published.

For row i and bar H: σ_i is the analytic quality SD (the same one the separability threshold uses), and σ_H is the SD of the configuration whose displayed quality is H.

Define Δ_i = (Q̄_i − H) / √(σ_i² + σ_H²).

Label "separated qualifier" when Δ_i ≥ 1.96, "indistinguishable" when |Δ_i| < 1.96, and "separated non-qualifier" otherwise.

A cheapest answer is "noise-separated" only if no cheaper row has Δ_j > −1.96.

Run it at ρ = 0, 0.3 and 0.6 (the O42 grid). Leave the frozen bars and the ladder unchanged.

Cohort-independent exchange rate as a sensitivity column, not a replacement for the 25/75 score.

Compute λ = median ΔIndex per cost doubling between adjacent vertices of AA's rendered frontier. This uses public data refreshed at each capture.

Publish Q* = Q̄ − λ·log₂(C/C_ref) beside the headline, with C_ref the median ranked cost.

Report λ against the implied 4.14 / 3.61 quality points per doubling.

Reading: if λ is much larger than the implied rate, the 25% weight under-prices cost relative to the frontier's own trade-off.

Owner-run meter probe for the Plan basis.

Method:

Replay a fixed, hashed coding transcript (a known token ledger by category) through each listed plan and model.

Record the provider usage meter before and after, then compute M = (API-priced ledger cost ÷ meter fraction consumed) × (window allowance fraction) ÷ fee.

Repeat for the weekly window, to avoid the O82 5-hour exclusion.

Cost and fit: this is roughly one plan fee per provider per month. It fits O11 as a controlled measurement with receipts, and each receipt can be hash-archived as O165 requires.

It would replace the O46/O40 assumption paths with fresh, dated evidence on a 30-day cycle.

Promotion rule for the common-leaf ranking (finding 2). Require τ_b ≥ 0.8 with ≥ 8 shared rows between common-leaf quality and each leading ranking's quality. The promoted ranking's bar answers would then carry the same noise-aware labels as item 1.

Bug Hunt leaf-level influence flag. Realised spread share = w·SD(z) ÷ Σ w·SD(z). Flag when it exceeds 1.5× nominal. Add an "extras capped at planted count" sensitivity column.

Normative-core refactor. Move per-release facts, fixtures and reviewer provenance out of the specification. Keep the rules, formulas and registries, and let data/figures.json carry the numbers.

3. Questions for the owner

Should "confirmed" and "scenario-supported" labels mean anything beyond rounding stability once O36 holds? If yes, item 1 changes my recommendations from a sensitivity to a label requirement.

Would you accept a label-bearing common-leaf ranking if it meets the τ_b ≥ 0.8 agreement test in §2 item 4?

Can you run your own subscription accounts for monthly meter probes (§2 item 3)? That determines whether Plan claims can ever be refreshed from public data.

For Bug Hunt, is uncapped unplanted-fix credit an intended reward for finding real defects, or a convenience of the board's own score?

4. Verdict

VERDICT: HAS FEEDBACK