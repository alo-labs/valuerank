# DR-SCOPE — O71 stage 3 (Silver Bullet Deep Research, deep mode)

Date: 2026-10-25 (confirmed with `date -u`: Sun Oct 25 14:34 UTC 2026).

## Bounded question

For each first-party subscription plan tier of the frontier and near-frontier providers in the ValueRank plan cohort,
find **new** actual end-user reports (not already listed in stages 1–2) of how much API-list-price-equivalent usage the
plan delivers per period, and evidence that resolves the stage-2 discordances. Then judge each model × tier against
O11: at least two independent reports whose API-priced allowance per period agree within 20% (largest ≤ 1.20 ×
smallest), over every eligible report of a comparability partition together; split a partition only on public
evidence of a quota-schema change.

## Cells (all failing after stage 2)

1. Anthropic Claude Pro / Max 5x / Max 20x × Opus 5.5, Sonnet 5.5, Haiku 5.5. Discordances: Pro #124 ($1,266/week;
   possible reuse of Team Premium data); Max 20x leaflavaplanetmoss $1,140 vs $2.0–2.9k cluster; post-10-14/17 lower
   group (claude-code #102667). Dated public quota-schema change?
2. OpenAI ChatGPT Plus / Pro $100 / Pro $200 (new 10×, grandfathered 20×) / Pro $500 in Codex × GPT-6.1 Sol, GPT-6
   Astra, GPT-6 Luna, GPT-5.6 Luna (standard vs Fast; "28 days of shipping" accounting changes).
3. Google AI Pro / Ultra (Antigravity) × Gemini 4 Argon.
4. Xiaomi MiMo Token Plan Lite / Standard / Pro / Max × MiMo-V2.6-Pro, V2.6-Flash.
5. Kimi membership Plus $19 / Pro $39 / Max $99 / Ultra $199 × Kimi K3.1 Pro.
6. MiniMax M Plan Go / Explore / Build × MiniMax-M3.1-Flash.
DeepSeek: no first-party plan (out of scope).

## In scope
- End-user reports dated 2026-09-25..2026-10-25 (older labelled), stating model (+effort/mode), tier, date and numbers
  from which API-priced consumption per plan period (or per window with documented window structure and fraction used)
  can be computed.
- Provider statements or corroborated public measurements dating quota-schema changes.
- Evidence on the provenance of discordant reports (#124 reuse question; leaflavaplanetmoss method).
- Under-used source classes: YouTube, X mirrors/snippets, Bluesky, Mastodon, Discord/Telegram logs, Chinese platforms,
  Japanese/Korean blogs, Substack/Medium/dev.to, code search, Wayback/archive.today, HN Algolia, Reddit mirrors.

## Out of scope
- Re-reporting stage-1/2 items (listed in `raw/known_sources.txt`), except where new evidence changes their eligibility.
- Third-party resellers' plans; DeepSeek; enterprise/Team plans (except as evidence about #124).
- Editing any repository file other than this output directory; committing.

## Assumptions (to validate)
- A1 (high): API list prices as given in the stage files (Opus 5.5 $4/$20/$0.20 read/$5 5-min/$8 1-h; Sonnet 5.5 $2/$10,
  cache read $0.10 from ≈10-08; Haiku 5.5 $0.10/$0.50/$0.01; GPT-6.1 Sol $2/$0.10/$10; GPT-6 Astra $10/$1/$50; GPT-6
  Luna $0.10/$0.01/$0.50; GPT-5.6 Luna $0.20/$0.02/$1.20; Gemini 4 Argon $2/$0.10/$10 introductory; K3.1 Pro
  $2/$0.20/$10; MiMo-V2.6-Pro $0.0036/$0.435/$0.87; M3.1-Flash $0.15/$0.015/$0.60).
- A2 (high): stage-2 eligibility rules (seven conditions, Fast → ×2.5 standard-equivalent, monthly = weekly × 4.33,
  one user = one independent source, ranges must pass over the whole range) remain the operative reading of O11.
- A3 (medium): reports from a reporter's tooling (ccusage, OTel, LiteLLM) price tokens correctly at list unless shown
  otherwise.
- A4 (medium): a provider statement, changelog or support e-mail is "public evidence" of a schema change; a single
  user's impression is not.

## Success criteria
- Every cell gets a verdict with every eligible report across all three stages tabulated.
- Each new report quoted verbatim with URL, author, date, and graded (admiralty).
- Each discordance addressed with whatever new evidence exists, or recorded as unresolved.
