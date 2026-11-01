0. Read check

Part 6 (draft-r158-part-6-of-14.md) was read to its end in one connector call at the pinned commit.

First line: "- Assumptions: only the owner-named model-to-model transfers (Opus 5.5's measured Claude multiples to other Claude models; the GPT rule of O45) and the owner's MiMo quota ceilings (O46) stay in the official Plan ranking, labelled, …". The first line is one very long paragraph, so I quote only its opening.

Last 12 words: "value; no epsilon is introduced. Domain validity is separate from evidence completeness."

I did no web search. The tool budget was one file read, so the review rests on the part alone.

1. Findings by severity

Critical

None.

High

None.

Medium

Effort-invariance is stated in tokens but applied in API dollars (O87, O88, O126, E246).

Issue: The part justifies the effort-invariant allowance with "the plan's meter counts tokens". A token-count meter makes the allowance constant in tokens, not in API-priced dollars. The multiple M is dollar-denominated. A higher effort has a larger share of (5×-priced) reasoning and output tokens and a different cache mix. So one measured max-effort figure gives a different dollar-equivalent value for the same quota at another effort. The same problem applies to the Opus 5.5 → other-Claude transfers, which differ in token mix by model.

Why it hurts: A cross-effort route labelled "measured" can be biased in a systematic direction, and the bias can reorder rows. High-effort rows would look cheaper on the plan than they are.

Change:

Store the donor measurement in meter units (tokens per period, with the category weights the provider documents).

Compute the target row's M as allowance × the target configuration's own price per metered token. Use AA's per-row output/reasoning token counts and the Index-wide category totals for the mix.

Where the meter's category weighting is not documented, apply the E210 category-mix bound to cross-effort and transfer routes. The result is a set-identified [L, U] flagged "mix-bounded", instead of a point.

The admission table (E106) has no stated evaluation order.

Issue: A route can satisfy several cases at once. For example, an exact-route measurement with an unreconciled valuation basis (case 4) can also fail expiry (case 5). A case-(3) route can also hit case 4. Case 3a is listed before case 3 and also overlaps case 1 through O88. The text says "classified once" but gives no precedence.

Why it hurts: Case 4 means "unmatched, excluded". Case 5 means "diagnostic only". Case 3 means "scored, flagged". These are different published statuses, so an implementer's ordering decides whether a row is scored.

Change: Publish a strict precedence, for example 1 → 5 → 4 → 2 → 3a → 3. Add a fixture per ordered pair. Return the failing predicates as a set, with the first match used for status.

The O46 MiMo ceiling's direction label and derivation are internally unclear (O125).

Issue: Xiaomi prices credits at parity (100M credits = ¥1), so credits-over-fee looks rate-independent. Yet the draft says the multiple depends on a per-model "overseas API rate", with Pro's cache-hit rate or the lower of two rates. Choosing the lowest rate lowers the ceiling, while the row is labelled the "optimistic end". The phrase "optimistic on use, not on rate" mixes two directions in one flag. The 0.0005 recompute tolerance is also ten times the 4-decimal storage resolution (5e-5).

Why it hurts: A reader cannot tell whether the published multiple is an upper or a lower bound on API-equivalent value, which is the question the Plan score answers.

Change:

Publish the formula explicitly: M = credits × (API-equivalent value per credit) ÷ fee, with the per-credit definition spelled out.

Publish the multiple at both the lowest and highest recorded rate as a set [L, U]. This is within the scope of E74's set-identified scoring.

Tighten the stored-multiple tolerance to 5e-5.

Low

Plan-row multiplicity inflates row-based statistics.

Issue: There are 18 plan rows for 5 configurations and 57 for 15, about 3.8 per configuration. The "fewer than half of Plan rows identified" threshold, the bar ladder and the identification yield all count rows.

Why it hurts: A configuration with many plans (for example the GPT rows) dominates these counts.

Change: Also publish configuration-level counts, with the label threshold taken on the stricter of the two.

Naming collision on "unmatched".

Issue: "Unmatched" means price-basis mismatch (O7, case 4) but also sits beside "workload-unmatched" (case 3, O16). The first is excluded and the second is scored.

Why it hurts: Readers of the site will confuse an excluded row with a scored, flagged one.

Change: Rename case 4 to "price-basis-unreconciled".

Zero-cost handling hides legitimately free options.

Issue: A published zero cost gets no score and is "never treated as best value".

Why it hurts: A free-tier or open-weights row at zero cost is a real cheapest-above-bar answer for some readers.

Change: Keep the score exclusion, but add a separate "zero published cost" list beside the cheapest-above-bar view, with the quality bar test applied.

The part is hard to audit.

Issue: The "Assumptions" bullet and the others are single paragraphs of several thousand characters. They mix definitions, fixture lists and historical decision numbers, such as "reviewer 72 separates use from rate".

Why it hurts: A reviewer cannot confirm that every fixture is a testable rule, and cross-references are brittle.

Change: Move the fixtures to a machine-readable table keyed by rule ID. Leave a one-sentence normative rule in the prose.

2. Methodology design recommendations

Meter-unit allowances. This is the highest priority.

Store each plan allowance as a metered quantity: tokens or credits per period, with documented category weights.

Derive M_i(config) = allowance × p_i(mix_i) ÷ fee, where p_i(mix_i) is the config's API price per metered unit given its mix from AA's output and reasoning tokens.

Where category totals are unavailable, publish the bounded interval from the structural category-mix bound (E210).

Keep the point score at the lower bound, as E74 does.

This removes the effort-invariance bias without any new data source.

Precedence-ordered admission. Publish the case order and a failedPredicates[] field per route. The plan-evidence lifecycle table (E212) then reads from a single source of truth.

Dual-rate MiMo ceilings. Carry [L, U] from the recorded low and high rates. Score at L. Show U as the sensitivity, so the "optimistic" flag has a defined meaning.

Configuration-level yield. Report N_config and N_rows for identification yield, the exploratory label and the bar ladder. The label fires on the stricter measure.

Free-cost list. Publish it separately, outside value-score ranking.

3. Questions for the owner

For Xiaomi MiMo tiers, with credits at parity to currency (100M credits = ¥1), is the ceiling's API rate used to convert credits into tokens, with each model priced at AA's valuation rate? Or is the multiple simply credit value ÷ fee? If the latter, the rate-dependence in O46 and O125 is spurious, and the ceiling would be the same for Pro and Flash at each tier. Today they differ, e.g. Lite 0.984 vs 0.9567.

Are SemiAnalysis's Claude and ChatGPT figures stated in plan-meter units (tokens or credits) or only in API-equivalent dollars? If only in dollars, the meter-unit design in recommendation 1 needs the provider's category weights, and I would recommend bounds instead of points for cross-effort routes.

4. Verdict

VERDICT: HAS FEEDBACK