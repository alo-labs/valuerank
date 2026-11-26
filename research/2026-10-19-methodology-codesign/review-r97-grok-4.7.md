I'll read the draft from the GitHub connector, part by part, starting with the file-read schema so each part can be opened in full.
The fifteen parts are in. I’m checking a few public measurement rules that the draft relies on before writing the review.
0. Read check

First line: # ValueRank methodology — draft r179

Today 10 configurations are retained (Claude Haiku 5.5 (max), Claude Haiku 5.5 (xhigh), Claude Opus 5.5 (medium), Claude Sonnet 5.5 (xhigh), DeepSeek V4.1 Flash 1017, GPT-5.6 Luna (low), Gemini 4 Argon, Kimi K3.1 Pro, MiMo-V2.6-Pro and MiniMax-M3.1-Flash), the 2026-10-25 release's cohort members that left at the v5 re-capture, so the cohort holds 37 configurations; applying O145 moved the release cutoff (O65) and re-captured every source.

Missing stays missing, and a configuration missing a leaf after the search is listed, not ranked (O36).

Release assertion: the scored field is the basket sum, not cost per task, not AA's 7:2:1 blended price, not total Index cost.

Priced-mix coverage (share of quality weight whose leaves are priced in the basket) is published each release.

and a report route must name the same observers as a passing cell for its plan and model (the build compares observers, not report values);

Evidence rules unchanged except for two owner exceptions, the O46 MiMo quota ceilings and the O76 speed-mode conversion of a user report (no provider marketing quotas otherwise; end-user API-priced reports or SemiAnalysis controlled measurements).

Domain validity is separate from evidence completeness.

| | Code Migration v1.1 (Vals AI; code porting graded by hidden tests, 130 tasks; Pi agent harness for every model) | 6% | — | — | hidden-test pass rate (%), anchors 0–100; Vals' standard error recorded |

The manifest records separately, per leaf: independent evaluation repetitions (e.g. Bug Hunt's mean over N published runs — affects precision only) and deployment attempt policy (attempts permitted per task, retry/best-of-k/selection/verifier policy) with the cost coverage of those attempts. Only a genuine deployment-policy mismatch between the quality figure and the priced attempts is reconciled (as a bias bound in the identification layer); repetitions are not a bias.

Where public evidence cannot separate them the route is labelled "measurement and transport not separable" and its S0 result is not described as target-workload support.

The current ladders are in Output 3 and scores.json barCurrency.

the summary says these outputs compare ranked configurations only and names the listed configurations.

every cost check reads C_W, never the Index diagnostic.

a mismatch stops the build for a re-capture of both (scores.json aaStateReconciliation, E322, on reviewer 87);

Revision history: omitted from this review copy (not normative); it is in draft-r179.md in the same folder of the repository.

1. Findings by severity

Critical

None.

High

O175 and the Opus cost-status sentences contradict each other. O175 keeps a row complete when the nine-evaluation residual is at most 0.1%. The same section then says the Claude Opus 5.5 rows (0.03–0.04% high) carry "partial component" and are E209-unresolved, and also that no ranked row in either leading ranking is unresolved. Owner text governs, but an implementer who follows the stale sentences drops those rows from FullCost, R_W and anchors for a residual the owner called immaterial. Change: one status sentence: residual ≤ 0.1% is confirmed complete with residualDisclosed; unresolved starts only above 0.1%. Delete the "partial component" / "unresolved" claims for these rows.

The 2026-11-01 release does not show a post-change allowance search. The last all-provider three-stage search named in the draft is 2026-10-25. Anthropic's 2026-10-30 announcement renamed Max 20x to Ultra and removed the five-hour cap for verified accounts, weekly cap unchanged. O164/O167 open a provider's cells on a registered limit change and fail the build unless a three-stage search follows. The draft records the change and still describes a built release, with Claude plan rows on the 2026-10-06 measurement. Change: the release record must name the three-stage search that followed each limit or price change before V. If none exists for Anthropic after 2026-10-30, the O167 clock has not passed; run it before the Plan order is treated as current.
notebookcheck
+1

Owner decision challenge (O2, display only). On AI Coding Daily API, cost's value-variance allocation is −55%. Because S_C is a cheapness score, a negative allocation means the headline value order rewards higher cost. That is the opposite of "lowest cost for the value delivered," and it is the published order for that ranking and basis. β stays 25% (O2). Change: when Cov(0.25·S_C, V)/Var(V) < 0, the first line of that basis is "headline rewards higher cost; cheapest-above-bar is the cost answer," and the default sort for that basis is the already computed bar table. Do not recalibrate anchors or β.

Medium

The Ultra flag does not use the binding window the scored estimand needs. O3 scores full-period utilisation. Public copy says Ultra's weekly allowance stays 10× Pro and Max stays 5× Pro, at twice the fee, so fee-normalised weekly allowance is about 1:1; the removed cap is the five-hour window, and only for verified accounts. A measurement that already saturated the weekly cap is not superseded for O3; one that saturated the five-hour cap is a lower bound on the new regime. The draft flags the whole route and does not record the verification split. Change: each controlled Claude route stores the binding window from its own record (E139). If that window is weekly, the 2026-10-30 event is an availability/label flag (O105/O107), not an E228 blocker. If it is five-hour, or unrecorded, the Max-versus-Ultra order is marked "weekly-allowance ordering not identified" and the published 5×/10× card is printed beside the measured ratio.
developersdigest
+1

Low

None.

2. Methodology design recommendations

Binding-window annotation on every plan multiple. From the measurement record plus the provider's current plan card, store binding_window ∈ {5h, weekly, monthly, unrecorded} and fee_normalised_published_ratio versus the donor plan. Displayed M stays the measured figure (O16, O72). The Plan table adds a column: rank range under the constraint that fee-normalised weekly multiples of Max and Ultra differ by at most the O86 band (1.20). If that range exceeds the between-configuration separability threshold, the pair is not an identified Plan order.

Negative-allocation banner, no weight change. Each release already computes Cov(0.25·S_C, V)/Var(V). If it is negative, prepend the banner in recommendation form above and sort that basis by the headline bar's displayed-record cheapest row, then by value score. Interval labels stay on the published record (O25).

Post-change search artifact. planResearchClocks gains postChangeSearches[]: change id, provider, search instant, stages, reports found. The build fails when a limit, price or credit record dated in (last all-provider search, V] has no later three-stage search for that provider. This uses only the registry the draft already keeps.

3. Questions for the owner

Did any three-stage Anthropic search run after 2026-10-30 and before 2026-11-01T06:10:00Z? If it did, the draft should name it; if it did not, should O164 treat that announcement as opening cells?

Does the selected SemiAnalysis transcription record which window bound each Claude plan (five-hour versus weekly)? That answer chooses between an availability flag and "weekly-allowance ordering not identified."

4. Verdict

VERDICT: HAS FEEDBACK