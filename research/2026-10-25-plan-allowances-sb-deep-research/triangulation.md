# DR-TRIANGULATE — cross-checks, grades and contradictions (O71 stage 3)

Prices (per 1M tokens) and normalisation as in scope.md: monthly = weekly × 4.33; OpenAI Fast × 2.5 (Ultrafast × 8)
to standard-equivalent; one user = one independent source; a range must pass over its whole range.
Source numbers refer to sources.jsonl / the report bibliography. Admiralty grades are in sources.jsonl.

## T1. Is Pro issue #124 a reuse of the Team Premium screenshot? (Anthropic Pro discordance)

| Component | #124 (ganpei777, meter week 10-09..13) [3] | Team Premium tweet (@leo114119, ≈10-05/06) [4] | Ratio |
|---|---|---|---|
| Cache read | 4,029.712M | 4,029M (panel "40.29亿", 0.01亿 = 1M resolution) | 1.000 |
| Fresh input | 0.027M | 0.026M | 1.04 |
| Output | 10.474M | 13.416M | 1.28 |
| Cache writes (5-min + 1-h) | 31.99M | 49.24M | 1.54 |
| Total at list | $1,266.15 | $1,320.38 | 1.04 |

The two ledgers agree on cache reads (at the Team panel's 1M-token resolution) and fresh input. They differ by 28% on
output and 54% on cache writes, and they cover different dates: the Team screenshot was recorded on 10-06, and #124's
meter CSV starts on 10-09 with 1,670 "pro" rows [3]. **Verdict: reuse is not supported.** A copied ledger would match
on every component. #124 therefore stays eligible. Its tokens remain unverifiable (collaborator note [3]). Grade C3.

## T2. Pro, Opus 5.5: new reports
- K45SLE [5], 2026-10-21, Pro, "Opus at xhigh effort" (version not written; Claude Code's Opus alias has been Opus 5.5
  since 09-22), controlled batch: "$10.50 at API prices … weekly from 0% to 4%". Weekly = $262.5. The meter shows whole
  percents, so the true fraction is 3.5–5.0% and the weekly value is **$210–300** ($909–1,299/month). Per 5-hour window
  the value is $42 (25%). Admitted **provisionally**: the model version is inferred. Grade D2 (controlled, small sample; the
  author is a plugin developer).
- Ok-Cauliflower-7568 [6], 2026-10-15/17, Pro, "mainly Opus 5.5": ≈$250, then "~290$ (95%CI 268-316) per weekly limit".
  **Excluded**: mixed model, as stage 2 ruled for "mostly Opus" reports. It corroborates the $250–320 level.
- #47 [7], 2026-09-26: a single snapshot ($23.58 at 21% of the week, with the week including earlier use). Lower bound
  only (≥$112/week). **Excluded.**
- Cross-check: three independent pure or near-pure measurers (K45SLE $210–300, Ok-Cauliflower $250–316, hakanavgin
  ≈$270 [51]) plus NTRYourWaifu $321 [1] and kanzakichiya $302 [2] all sit at 210–321. #124 [3] is the single 4× outlier.
  Nothing new makes #124 ineligible (T1), so the cell still fails.

## T3. Max 20x, Opus 5.5: the leaflavaplanetmoss outlier
Stage 3 recovered the comment [12]: "~70% of the 20x Max weekly usage … ~120 Opus 5.5 Max agents and ~30M output tokens.
According to CodexBar … something like $800 at API list prices." Output alone at $20/M is $600, which would leave about
$200 for all input, cache-write and cache-read traffic of ~120 agents. In every full Opus ledger available, output is
17–30% of list cost: #124 16.5% [3], #52 22.8% [1], and tomm3hshipp's Opus share 29.9% (stage 2). At a 30% output share,
30M output tokens imply ≈$2,000 for the run, or ≈$2,860/week at 70%. The reporter's own token count therefore does not
reproduce the reporter's dollar figure. A tool that omits workflow subagents would produce exactly this gap, a failure
mode another user documented for Claude Code's per-session counter [18]. **Ruling: eligibility challenged.** The figure
is indicative only, following the stage-1 precedent for figures that do not reproduce from the reporter's own numbers.
The verdict is unchanged, because P1 also holds NicoAica's $1,294–1,681 [13] against Kanttz $2,578–2,920 [10] (≥1.53×),
and Kanttz against Last_Lab_3627 ($2,045) is already 1.26×.

## T4. Max 20x / Max 5x: public evidence of a quota-schema change (dated)
- Provider statements: none. Anthropic's release notes contain no limit entry between 09-15 and 10-25 [15]. #102667
  has no staff reply and carries the labels `bug` and `area:cost` [13]. The only provider limit change near the window
  is the 09-22 Opus 5.5 launch (+20% five-hour limits, a one-time reset usable to 10-22), which falls before every
  in-window report.
- User measurements (public, timestamped): NicoAica, a 5× per-token step on 10-17 [13]. kakki-1, 10-24, transcript
  totals: the full week of 10-16..23 used 414M weighted tokens unblocked, while the 10-24 meter implies a cap of ~261M
  (≤63%), with cache reads "counted more heavily" [13]. push42, 10-20, Max 5x: a full 5-hour window costs ≈18% of the
  week, against ≤10% earlier [13]. Randomblock1, 10-17, Max 20x: "$1.2k and I'm at 86%" against a usual $2–3k week
  [14].
- Contrary: Wokey's 17-account tracker shows Max 20x unchanged in the week of 10-12..19 [16], which mostly precedes the
  split. cannonpalms (HN, 10-24): "$2k in tokens each week without consuming any credits" on Max 20x, a lower bound with
  no meter fraction [19]. A confirmed Agents SDK bug drains five-hour limits faster but "does not affect weekly limits"
  [17].
- **Ruling:** stage 2's split at ≈2026-10-17 13:00 UTC is now corroborated by four public measurers (NicoAica,
  kakki-1, push42, Randomblock1). It is kept for Max 20x and extended to Max 5x. It still rests on user measurements, not
  a provider statement. Under the split, P2 (after 10-17) has one eligible Max 20x report (NicoAica $182–212) and no
  eligible Max 5x report. kakki-1 (tier unstated) and Randomblock1 (model unstated) are excluded from the cells.

## T5. OpenAI: new items (none eligible)
- muscgab #97 [31] (Pro $100, 10-03): mixed four-model run (Astra, 6.1 Sol, 5.6 Sol, 5.6 Terra). Week = 8,020
  credits = $320.8 at $0.04 per credit. Per-model values ($234 for 6.1 Sol, $313 for Astra) are contributor-derived.
  **Excluded** (mixed). The $313 Astra figure sits within 1.02× of YiwenPang's $318 [26], but it is a derivation, not a
  measurement.
- Danikk [32] (10-21, GPT-6.1 Sol medium): $17.53 → 38% of the week = $46/week. Tier is a "legacy account" with no
  five-hour limit (unidentified), and the report describes an anomaly. **Excluded.**
- noz.am [34] (10-23, Pro $100, full week): 1.09B Sol + 602M Luna tokens, mixed, no cache split. **Excluded.**
- No new report for Pro $100 Sol, Pro $200 new 10×, Pro $500 Sol/Astra, Luna, or GPT-5.6 Luna.

## T6. Google: Argon AI Pro and Ultra
- No new priced Argon report (forum search after 10-20; r/GeminiAI and r/google_antigravity since 10-16; Bluesky; HN;
  Japanese web). Faheem_Anis1's thread [37] has no follow-up that revises the $12.3 figure.
- spin.pyokosmeme (Bluesky, 10-24) [39]: "a weekly limit at $50 of argon is about 62 M toks". Tier and basis are not
  stated. **Excluded** (F6).
- Structure: Google publishes no quota size. The intro price ends 11-30 [40]. The cell's spread (12.3 / 8.40 = 1.46) is
  between efforts (Low against Medium and High), but effort is not a partition ground under O11.

## T7. Kimi, MiMo, MiniMax
- Kimi: MoonDrinker [45] (10-25, legacy CN Allegretto ¥199) charges 6.61% / 0.0391% / 50.71% of the week per 1M
  uncached-input / cache-read / output tokens. At Astralyn's mix (97.5% cache hit, uncached input 2.5× output) that is
  **$48.6/week**, against Astralyn's $55.9 (1.15×). This is a CN legacy tier and not a cohort cell, so it is recorded as a
  reference only. No new USD-tier report was found.
- MiMo: no new report. MiniMax: no priced report on Go, Explore or Build. Ok_Bug1610 [49] confirms the 10-19 rerouting
  of M2.5/M2.7 traffic to M3.1-Flash (a metering-context change).

## Contradictions flagged
C-1 #124 against every other Pro report (4×): unresolved; reuse ruled out (T1).
C-2 leaflavaplanetmoss against the Max 20x cluster: explained by internal inconsistency (T3).
C-3 Max 20x and Max 5x before and after 10-17: corroborated user evidence, no provider statement (T4).
C-4 Argon Low (12.3) against Medium/High (8.4): unresolved.
C-5 Wokey "no change" (aggregate, to 10-19) against the post-10-17 tightening: timing explains most of it.

## Core-claim sourcing check (rule: ≥1 A/B source, or 3+ C sources)
Partition and schema claims: A2 [15] and B2 [30] for the provider-side facts. Report-level values are C/D user
evidence by nature, which O11 anticipates by requiring two concordant independent reports. Single-source items are
labelled as such in the report.
