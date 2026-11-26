# Internal review I24 — Claude Sonnet 5.5 (effort low) on draft r83

## 0. Read check
First line: "# ValueRank methodology — draft r83". Last 12 words of last line: "covers two-thirds of cohort rows jointly with the admitted components (E95, E101)."
(All 1025 lines read in four chunks, plus ledger-brief.md, ledger sections I20–I23 and O36–O38, and the amended AGENTS.md. No web search; checks were derived arithmetic and local files: the quality ladder 47.36 / 55.31 / 59.56 and reach counts 17 / 25 / 9, all 32 quality values from leaf weights, the E203 cheapest row ($531.56), the coding share median 53%, and the Omniscience and Clopper–Pearson fixtures.)

## 1. Findings by severity

**Critical**
None.

**High**
H1. "Use the latest SemiAnalysis analysis" (AGENTS.md) has no operative rule, so a stale higher multiple can beat the newest measurement (comparator E85/E111 keys 1–6; lifecycle E212: "the stage is not a comparator key"). Recency is not a key: between two controlled measurements of one route the comparator decides by key 3, the larger multiple. With regimes changing within weeks (legacy Pro $200 allocation "until October 29"; all-Opus vs Fable shared pool), a SemiAnalysis revision would lose to an older still-current object with a larger multiple, contradicting AGENTS.md; E144 also says a newer donor replaces the old one "only by being named". Recommendation: a pre-comparator supersession step — within one publisher series and route key the newest controlled analysis supersedes older ones (which become diagnostics with an eligibility-transition reason); a changed limit schema or allocation regime supersedes rather than competes; fixtures for a lower newer multiple, a dropped model and automatic transfer to the new donor.

**Medium**
M1. A near-frontier family whose evidence-first configuration lacks a leaf is undefined (O30 vs O36/O38; "Frontier and near families differ on purpose"; E188/E193). The draft covers the frontier case but not whether a near family falls back to another evidenced complete effort, to the smallest-gap near point, or is listed; E211 also fails the gate on a near family neither rostered nor deferred. Recommendation: (1) choose among configurations with exact DeepSWE and Bug Hunt and all eleven leaves; (2) else the smallest-gap near point if complete; (3) else list the family with the logged search and a dated roster decision; add a fixture.

M2. "Exhaustive search" is not reproducible, so cohort membership depends on search diligence (Full benchmark set; O37 "other sources if needed"). Every leaf except Terminal-Bench (closed agent list, E225) has an open source list; e.g. a third-party post next week would admit Grok 4.6 (xhigh), changing the cohort count, quartile positions at the next re-freeze, anchors and the clip gate. (I23 Design 3 rejected a recall audit; this asks for a closed registry.) Recommendation: a versioned, closed per-leaf source registry (AA, the named other party, the leaf owner, the provider's primary document class) so "missing" is a deterministic function of the registry at the capture date; a new source requires a registry update.

M3. The headline rank column puts incomparable rows in one integer sequence, and the provider-claim row is not marked there: MiMo-V2.6-Pro is API rank 3 (Plan 17) on the seven-evaluation subset basket against different anchors, with Xiaomi's DeepSWE claim (attempts unstated) on the 30% leaf; gap-fill removal moves it six places. **Owner decision challenge (O17, O37)**: publish a structural best-case rank bound beside it (full-basket cost ≥ subset cost) and print a "provider-claimed leaf" flag in the rank table.

M4. The category-mix bound (E210) is unsound when u_k = 0 and x_k > 0: with p = (1,1), x = (1,1), u = (1,0), a = (1, a_B), M_W/M_obs = (1 + a_B)/2 is unbounded, while the draft's bound gives 1. Range over categories with x_k > 0 or u_k > 0, set ρ_k = ∞ where u_k = 0 < x_k (and 0 where x_k = 0 < u_k), identify only when none is 0 or ∞; add a two-category fixture.

M5. "One eligibility predicate (E92)" is no longer one predicate: E222, E233 and E228 add denials without citing E92 as amended. Rewrite E92 in place as the full conjunction and cite it from E222, E228 and E233.

**Low**
L1. E201b's "14 against 15, since every ranked row now has full coverage" — the gap is the bar setter, Claude Sonnet 5.5 (high), whose displayed quality equals H exactly, so its rounding interval can never clear H. Correct the sentence; optionally freeze H at a midpoint, or document the artifact.

L2. E234's "the measured offset bounds its effect" is overstated: a 10-row sample maximum is not a bound and the mean is directional. Call it an estimate; consider a bias-adjusted sensitivity.

L3. Bug Hunt runs open-weight models (GLM, Qwen, DeepSeek, MiMo) through Claude Code via API or Anthropic-compatible shims, while Claude and GPT models run in native harnesses; publish a vendor-native / shimmed / third-party class per Bug Hunt row with its own flag.

## 2. Methodology design recommendations (prioritised)
1. The newest-same-publisher supersession step (H1) with the near-family order (M1).
2. The closed per-leaf source registry (M2).
3. A best-case rank bound for subset rows and an evidence-flag column in the rank table (M3).
4. One UniqueLabelEligible definition (M5) and the corrected E210 domain (M4).
5. An "executed in v1" index of the normative blocks (Plan identification machinery, interval branch-and-bound and E105/E80/E39 programs are dormant today).

## 3. Questions for the owner
1. May a near-frontier family whose evidence-first configuration lacks a leaf be ranked at another evidenced complete effort, or should it be listed (with a dated roster decision)?
2. When SemiAnalysis publishes a newer analysis for a route, should it always supersede the older one, even when the old multiple is larger?
3. Under O17, may a subset-scored row be shown with a best-case rank bound instead of a bare integer rank?

## 4. Verdict
VERDICT: HAS FEEDBACK
