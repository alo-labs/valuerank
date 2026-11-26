0. Read check

Read both listed parts to their ends at commit 5917e61757433bf61ca45bbb5cb030200bb8f863, in order.

Part 7

First line:

MiMo quota ceiling (owner decision O46): Xiaomi prices MiMo Token Plan credits at parity with its pay-as-you-go API (100M credits = ¥1), and the owner-requested research (Claude's deep-research skill with three researchers, and Perplexity Search with GPT-6.1 Sol, Grok 4.7 and Gemini 3.8 Flash; Silver Bullet's multi-model workflow could not run without provider credentials; record research/2026-10-23-mimo-token-plans/) found no end-user measurement of a MiMo-V2.6 billing period. Each MiMo-V2.6 model therefore takes, per Token Plan tier, the tier's monthly credits valued at Xiaomi's overseas API rate for that model (for Pro its cache-hit rate and the lower of its two published rates; each rate is recorded on the route with its capture, E261) divided by the list fee (O46): today Pro 0.984 / 0.99 / 1.0944 / 1.1808 and Flash 0.9567 / 0.9625 / 1.064 / 1.148 on Lite / Standard / Pro / Max, read from the route registry. The build recomputes each ceiling from the route's recorded credits, rate and fee and fails when the stored multiple differs by more than 5 × 10⁻⁵, half a unit of its fourth stored decimal. Each ceiling is labelled provider-derived and not a measurement, and flagged as full use of the quota, the optimistic end on use, while its credits are valued at the recorded rate, not the highest (the formula: M = quota credits × the API dollars one credit buys for that model, at the lowest of the model's recorded per-token rates, ÷ the tier's fee; credits are spent per token at model-specific rates, so a tier's ceiling differs by model; the stored multiple must recompute within 5 × 10⁻⁵, half a unit of its fourth decimal, reviewer 76) (reviewer 72 separates use from rate; unlike E74's lower-bound scoring of a set-identified multiple; owner decision O125, 2026-10-30, keeps O46's ceiling and names the direction); it is an explicit AGENTS.md exception to the end-user numerator rule, replaces the earlier 1.5× owner assumption, never identifies M_W, and is replaced by end-user measurements for the exact model and tier once they meet the admission rule of any other provider's route (O11); one report alone does not replace it (owner decision O62). The build counts its rows among the Plan rows resting on an owner assumption, by kind (marked †, E242).

Last 12 words:

drift-flag counting). AA Intelligence Index and output speed are diagnostics, not quality.

Part 8

First line: empty.

Last 12 words:

a bias bound in the identification layer); repetitions are not a bias.

1. Findings by severity
Critical

None.

High

None.

Medium

The Bug Hunt record selector can also change the AI Coding Daily leaf, creating a coupled score change that the stated harness diagnostics do not isolate.

Issue: E206 selects Bug Hunt’s largest-sample result across harnesses. E268 then preferentially selects the AI Coding Daily row whose harness matches that selected Bug Hunt harness. Consequently, a newly published Bug Hunt result with a larger run count can change both leaves—even when neither AI Coding Daily result has changed. Part 8 explicitly supplies the first half of this transition as a fixture: a larger-N Bug Hunt result switches the selected harness. It also explicitly makes that harness an input to AI Coding Daily selection. Part 8

Why it hurts the objective: one benchmark’s evidence-refresh rule can move 22% of AI Coding Daily quality weight—the 12% Bug Hunt leaf and 10% AI Coding Daily leaf—rather than only the benchmark whose evidence changed. Publishing alternate rows exposes the inputs, but does not distinguish a better-measured Bug Hunt result from the induced change in the other benchmark’s selected deployment harness.

Concrete change: retain the selectors, but add a coupled-selection diagnostic whenever the selected Bug Hunt harness changes. Replay the old and new Bug Hunt and AI Coding Daily selections independently, holding other evidence and anchors fixed; publish each contribution to quality, value, ranks and bar answers.

What is new relative to the ledger: E224/E268 publish alternatives, O162 addresses label changes under Bug Hunt’s harness span, and E177 attributes release changes. This finding concerns the cross-benchmark selection dependency itself: a Bug Hunt refresh changing an otherwise unchanged AI Coding Daily leaf. It is not another request for the already-adopted single-leaf harness sensitivity.

Low

None.

2. Methodology design recommendations

Prioritise a four-state replay of the coupled harness selection. For an affected configuration, let 
𝑏
0
,
𝑏
1
b
0
	​

,b
1
	​

 be the old and new normalised Bug Hunt values, and 
𝑎
0
,
𝑎
1
a
0
	​

,a
1
	​

 the AI Coding Daily values selected before and after the harness switch. Calculate:

𝑄
𝑢
𝑣
=
𝑄
other
+
0.12
𝑏
𝑢
+
0.10
𝑎
𝑣
,
𝑢
,
𝑣
∈
{
0
,
1
}
.
Q
uv
	​

=Q
other
	​

+0.12b
u
	​

+0.10a
v
	​

,u,v∈{0,1}.

The coefficients are the AI Coding Daily ranking’s published leaf weights. Use the existing exact-configuration alternatives and provenance records; no new external measurements, evidence transfer or imputation are needed. The published official result remains 
𝑄
11
Q
11
	​

. The other three states are selection diagnostics, not additional ranked configurations. Part 8 Publish:

Direct Bug Hunt contribution: 
0.12
(
𝑏
1
−
𝑏
0
)
0.12(b
1
	​

−b
0
	​

) quality points.

Induced AI Coding Daily contribution: 
0.10
(
𝑎
1
−
𝑎
0
)
0.10(a
1
	​

−a
0
	​

) quality points.

Value contributions: each quality contribution multiplied by 
0.75
0.75, with costs unchanged.

Rank and bar-answer outcomes for all four states, because those outcomes need not change additively.

Whether the transition came solely from a larger published Bug Hunt run count, rather than a changed AI Coding Daily observation.

Add a build fixture in which a larger-N Bug Hunt result changes the preferred harness, both AI Coding Daily alternatives remain unchanged, and the diagnostic correctly identifies the induced leaf switch. If the previously selected exact record is unavailable, report the replay as unevaluable rather than filling it. Keep this separate from sampling uncertainty: it measures the consequence of the deterministic evidence-selection rules, not run-to-run noise. That distinction is consistent with these sections’ separation of evaluation repetitions, deployment policy and harness provenance. Part 8

3. Questions for the owner

None.

4. Verdict

VERDICT: HAS FEEDBACK