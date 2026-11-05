# Internal review I35 — Claude Sonnet 5.5 (effort medium) on draft r94

## 0. Read check

- First line of the draft: "# ValueRank methodology — draft r94".
- Last line of the folded copy (line 924): "Surge's Complex Constraints is excluded (O53). On the Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Last 12 words of the last paragraph: "Plan basis the MiMo multiples are provider-derived quota ceilings, not measurements (O46)."
- Also read: the whole folded draft (924 lines, in chunks), `reviewer-prompt.md`, `ledger-brief.md`, `ledger.md` from "## Internal review I28" to the end (through I34), and the root `AGENTS.md`.
- Checked against data: `data/scores.json` (`v3` and `v3Tracks.aicd`) for the separability medians, grids, tolerances, bands, plan-row counts, cost-influence allocations, bars, bar currency, noise-margin companions, anchors and exchange rates, family-primary diagnostics, FrontierCode cross-check and the admission object. `data/plan_cost_routes.json` for the Claude route records. Every number I tested matches the draft (3.01 / 4.45 / 4.54 medians, 2.35 / 5.28 tolerances, 65% and 2% and −90% and −26% allocations, 49.76 / 60.72 / 62.12 and 38.00 / 49.24 / 57.16 bars, 64.7 / 53.8 / 66.1 and 55.1 / 43.9 / 63.0 margins, 14 and 48 transfer rows, 27 and 50 plan rows, anchor values and exchange rates). I found no wrong stated figure.

## 1. Findings by severity

**Critical**

None.

**High**

None.

**Medium**

**M1. The Plan rule for Claude Opus 5.5 at an effort other than max is not stated, and the AI Coding Daily Plan figures depend on it.**
- Issue. The draft states Plan routes for four groups.
  - Opus 5.5 (the exact measured SemiAnalysis routes).
  - "Other Claude models" (the owner-named transfer, line 357 and the Fable paragraph).
  - GPT rows (O45 and E246, including the effort binding).
  - MiMo (O46).
- Opus 5.5 at medium and high is none of these. It is not "another Claude model", and the only effort-binding sentence (E246) sits inside the GPT bullet and speaks of "a SemiAnalysis figure that names a model without an effort".
- The ranked AI Coding Daily rows Claude Opus 5.5 (high) and (medium) exist, and Claude Opus 5.5 (medium) on Claude Pro is the draft's own displayed cheapest Plan row at the headline, lower and upper-companion bars (the noise-margin sentence).
- The build resolves it by giving them the "common Claude assumption" copy of the Opus (max) figure (`plan_cost_routes.json`, `modelIds` of the measured routes is `claude-opus-5-5` only).
- Why that hurts. Two faithful implementers diverge.
  - (a) Read as built: Opus (high or medium) takes Opus (max)'s multiple as an owner-named transfer, labelled †.
  - (b) Read from AGENTS.md ("keep Opus 5.5 on its exact measured routes") and the "names a model without an effort" wording: treat SemiAnalysis's "Opus 5.5" as covering the model's efforts and score them as measured.
  - (c) Apply the "other Claude models" transfer only to other models, so Opus (high or medium) has no route and falls to API cost.
  - (a) and (b) give the same score but change the published transfer count ("48 of 50"), the † marks, the Plan evidence grade (and so route comparison) and whether the AI Coding Daily measured-evidence calibration (E164) is "unavailable" or computable (today "unavailable because no row has a measured route").
  - (c) changes the AI Coding Daily Plan ranking for six plan rows and its anchors.
  - The GPT case needed an owner decision (O45) for exactly this question; the Claude case has no equivalent text.
- Change. Add one sentence to the Plan-assumptions bullet, for example: "A SemiAnalysis figure that names a model without an effort binds to the model's unsuffixed AA row (E246, all providers); every other effort of Opus 5.5 takes that figure as the owner-named Claude transfer (donor: the Opus 5.5 (max) route on the same plan), labelled †." Generalise E246's first sentence out of the GPT bullet. If the owner prefers (b) or (c), that is a decision (Question 1).

**Low**

**L1. Known limitations says the AI Coding Daily basket "holds no agentic-coding component".**
- That basket admits Terminal-Bench 4.0 (AA's terminal-agent run) and SciCode, and the draft's own coding share (E200, 19% there) counts "coding and terminal tasks".
- Change: "holds no Coding Agent Index component, so its coding share is far lower".

**L2. AGENTS.md says "two-thirds of the cohort"; O57's per-ranking reading is in the draft and ledger but not in AGENTS.md.**
- The draft is right to cite O57. But a reader checking against the root instructions finds a literal whole-cohort wording, and the Cohort bullet says AGENTS.md was amended for O36/O38 but is silent for O57.
- Change: one clause in the draft ("AGENTS.md's 'the cohort' is read per ranking by O57; the owner may wish to amend it"), or have the owner amend AGENTS.md. No score changes.

**L3. The FrontierCode gap-fill offset used to lower fills in the AI Coding Daily ranking rests on two rows, while the draft says scale equivalence is not tested there.**
- The AI Coding Daily ranking lowers each Cognition fill by a mean offset of 1.45 from a 2-row panel (Gemini 4 Argon, GPT-6 Luna). The max-effort ranking measures 1.71 on six rows, and the Cognition-versus-AA relation is a property of the configuration, not of the ranking.
- Change: compute the E234 agreement and offset once over every cohort configuration that has both AA and Cognition results, and show each ranking's panel as a subset. The two-row figure would then no longer be the only basis for the "lowered" bar test.

**L4. The O46 quota-ceiling clock has no renewal rule.**
- "Ages from its authorisation date" is stated, but not whether a dated re-confirmation of Xiaomi's price and quota pages or a re-authorisation restarts it (E144 says a check or edit date never does).
- Without a rule, the four MiMo plan rows lapse to API cost about four months after 2026-10-23. Change: say that a dated re-verification of Xiaomi's pages by the build, with no change detected, is a new authorisation date, or that it is not.

**L5. Indicative values beyond a frozen anchor.**
- Listed rows can lie beyond an anchor (AI Coding Daily: Claude Opus 5.5 (max) at $6,039 and Claude Sonnet 5.5 (max) at $5,074 against c_H $4,764; their cost score is 0).
- The draft says the indicative cost is "on that ranking's frozen anchors" but not whether it clips, nor that the clip gate (which counts scored rows) ignores them.
- Change: one sentence: "indicative cost scores clip like any score, the unclipped dollars are shown, and listed rows do not count in the clip gate".

**L6. A configuration's plan rows can straddle a noise-band boundary, and the E248 wording does not say so.**
- E248 says a band that starts at one of a configuration's plan rows "extends over its other plan rows". Today GPT-6.1 Sol (medium) on ChatGPT Pro 500 is in AI Coding Daily Plan band 1–11 while its other three plan rows are in 12–24, and GPT-6 Luna (max) on Plus is alone in band 21 while its other rows are in 11–20.
- That is the forward-only reading, and it is consistent with the invariant, but a reader meets the sentence and the table together.
- Change: add "forward in value order only; a configuration's plan rows may therefore straddle a boundary (today two do)".

## 2. Methodology design recommendations

Prioritised. All use data already in the bundle.

1. State the provider-general effort-binding rule once, before the provider-specific bullets, and use it for Claude as well as GPT. Proposed text: "A SemiAnalysis figure binds to the AA row it names; if it names no effort it binds to the unsuffixed row (max) and to no other effort. Another effort of the same model takes the figure as a labelled owner-named assumption naming that donor route." It closes M1 and makes the GPT and Claude cases one rule.
2. Make the gap-fill cross-check configuration-level, not ranking-level (L3). Compute τ_b and the offset on the union of configurations with both sources, once, and print each ranking's subset. Lowering fills by an offset measured on six or more rows is a stronger sensitivity than a two-row mean.
3. Give every lapse clock a renewal sentence (L4). The lifecycle table is complete for measurements and transfers. The O46 ceilings are the one evidence class with no donor and a rule that says only "authorisation date".
4. Keep the AGENTS.md text and the draft in step on O57 (L2). The draft's own convention (the Cohort bullet) is to say when the repository instructions agree; do the same for per-ranking admission.
5. Small presentation fixes: L1, L5 and L6 wording.

## 3. Questions for the owner

1. For Claude Opus 5.5 at efforts other than max (today the AI Coding Daily ranking's Opus 5.5 (high) and (medium)): should SemiAnalysis's unsuffixed "Opus 5.5" figure be (a) a labelled transfer to those efforts (what is built), (b) measured evidence for every Opus 5.5 effort, or (c) not applied, so those rows take API cost? The answer decides the evidence grade, the † marks, whether the AI Coding Daily measured-evidence calibration exists, and (under (c)) the six Opus plan rows' scores. A default of (a) is my recommendation, matching O45's treatment of GPT.

## 4. Verdict

VERDICT: HAS FEEDBACK
