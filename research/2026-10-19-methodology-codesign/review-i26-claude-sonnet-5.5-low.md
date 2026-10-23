# Internal review I26 — Claude Sonnet 5.5 (effort low) on draft r85

## 0. Read check
First line: `# ValueRank methodology — draft r85`. Last 12 words of the last line: "covers two-thirds of cohort rows jointly with the admitted components (E95, E101)."
(All 1056 lines read in four chunks, plus the condensed ledger and the current AGENTS.md; the full ledger grepped. No web search. Re-derived and consistent: ladder positions and the 17 / 25 / 9 of 32 reach counts; Plan ln(13,400/0.61) ≈ 10.0 → 1.73 points per doubling; Omniscience fixtures (82 / 66, 98.5 / 99) and the Bug Hunt vector (52/105 → 49.52); Clopper–Pearson endpoints at k = n and k = 0; the Plan evidence-clock dates.)

## 1. Findings by severity

**Critical**
None.

**High**
None.

**Medium**

M1. The rank-separability statement (O39) is biased in one direction and the draft does not say which. The threshold 1.96 × root-sum of the two value SDs assumes independent errors, but every configuration is scored on the same tasks, so shared task difficulty correlates the errors (Var(difference) = v₁ + v₂ − 2·cov), and averaging three attempts per task lowers per-task variance below p(1−p); the binomial SE also ignores near-always or near-never solved tasks. "0 of 30 adjacent ranks separable" is therefore the conservative direction, but a reader will take it as neutral. Print the bias direction ("upper bound on the separation threshold; true paired noise is smaller"); where task-level outcomes are public use a paired bootstrap; otherwise report "separable at ρ = 0 / 0.3 / 0.6".

M2. GDPval in S1T is inconsistent with E174: E174 keeps GDPval-AA's unstated-level interval out of S1M, yet S1T draws GDPval from Opus 5.5's ±26 Elo read as a 95% interval, SD 13.3 Elo for every row — an analyst parameter where E145/E134 route analyst ranges to S2, and one row's width standing in for 30 although rating CIs depend on each model's comparisons. Capture the per-row intervals; until then run GDPval as a two-width sensitivity (SD 13.3 and 26.5) or exclude it; state in the lint that the kernel is analyst-derived and the separability count is sensitive to it.

M3. Tension between AGENTS.md (2026-10-18: "replace a shared route with an exact measurement for the listed model as soon as one exists") and E238's treatment of a revised article, where a newly added exact measurement stays diagnostic until re-selection; line 364 states the replacement rule without that qualification. Option A (preferred): a new per-(plan, model) measurement replaces the matching transfer immediately, labelled "added after selection", everything else diagnostic; Option B: amend line 364. Ask the owner.

M4. **Owner decision challenge (O36/O38 with O31/O33)**: a single-maintainer benchmark (Bug Hunt: 2 TypeScript repos, 10% weight, one person on vendor CLIs) gates both retention (23 of 32 rows) and whether a frontier family is ranked (MiMo-V2.6-Flash); a 10%-weight leaf acts as a 100% gate, with selection-bias risk for open-weight and smaller-lab models. Publish beside the ranking a reduced-leaf indicative value for each listed frontier family ("not ranked, not comparable", no imputation), or ask the owner to restore a labelled provisional row for frontier families only.

**Low**

L1. E238 says "Anthropic and OpenAI"; AGENTS.md says "Anthropic and Codex". Scope the rule by surface or state that no non-Codex OpenAI route exists in v1.

L2. The report window is closed [V − 30 d, V] "compared as UTC calendar dates", while V is a timestamp; a report dated on V's date but published after V counts, contradicting "one release cutoff governs everything" (E213). Add "and not published after V", or define the end bound as V itself for timestamped dates.

L3. The bar setter is structurally never "confirmed" at any n (H equals an element of the order); freeze H at the midpoint of the two central order statistics for even n, or count the setter as confirmed when its displayed margin is 0 and no leaf is missing. Low priority.

## 2. Methodology design recommendations (prioritised)
1. Rank bands beside ordinal ranks: group rows into bands where every pair is within the separability threshold by a rule fixed before the data, e.g. "ranks 4–9 (indistinguishable under S1T)", keeping the ordinal rank.
2. Fix M1 before M2: quantify the correlation bias with a paired variant wherever task-level data are public.
3. Split the spec into a short active v3 spec and a normative registry of dormant rules with fixtures, activated by named triggers.
4. Replace the single GDPval kernel width with captured per-row intervals.

## 3. Questions for the owner
Q1. When the selected SemiAnalysis article adds an exact per-(plan, model) measurement, replace the transfer immediately or only after re-selection?
Q2. Would you accept a separated, non-ranked reduced-leaf indicative value for frontier families listed under O38?

## 4. Verdict
VERDICT: HAS FEEDBACK
