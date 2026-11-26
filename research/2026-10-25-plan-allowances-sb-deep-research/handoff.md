# Handoff — O71 stage 3 (FS-SILVER_DEEP_RESEARCH → AF-DOCUMENT → AF-VALIDATE)

## For the coordinator
- Output directory: `research/2026-10-25-plan-allowances-sb-deep-research/` (no other repository file was edited;
  nothing committed). Raw retrieval outputs are in `raw/` (search dumps; `known_sources.txt` = stage-1/2 identifiers
  used for de-duplication).
- Verdict to record: **no model × tier passes O11** after stages 1–3. No O11 value or multiple to adopt.
- Rulings that change stage-2 tables: K45SLE added to Claude Pro (provisional) [T2]. #124 reuse ruled out [T1].
  leaflavaplanetmoss challenged [T3]. The Claude 10-17 split is extended to Max 5x [T4]. DhAdaptive's Pro $500 is
  excluded because of OpenAI's upgrade-entitlement error, corrected 2026-10-16 [T8].

## Owner-actionable next steps (ranked by expected effect on O11)
1. Ask Anthropic, or watch for, a dated statement on weekly-meter or cache-read accounting around 2026-10-17 (claude-code
   #102667 is an open `bug`). A provider statement would make the Max split provider-grade.
2. Recruit deliberately: two or more model-pure, full-week (0→100%) measurements per cell in fresh partitions: Claude
   after 2026-10-25, OpenAI after Day 19 and after the 2026-10-29 end of grandfathering, Argon AI Pro at Low and at
   Medium/High effort.
3. Read the YouTube leads manually (blocked here by a bot check): Binh Dad of 3 Monkeys, "I tested the $200 Claude Max
   plan so you don't have to" (video 7TVIaQ7IoQA) and "$100 Claude Max … $987 at API prices" (OCM5XxIL47I); Iris Ludd,
   "Is the $200 Codex plan still worth it?" (gUA_6WWyuRI, the only lead for Pro $200 new 10×); Receipts, Please
   (iF9pddgeWcE); TreeCityWes (QQAPGv-zGYY).
4. An owner ruling on outlier handling would flip at least Claude Pro (#124 is 4× every other measurer). One example:
   an eligible report whose tokens cannot be verified and that sits >3× from all independent peers may be set aside.
5. For Kimi USD tiers, MiMo-V2.6-Flash and MiniMax M Plan tiers: request named-tier measurements directly; organic
   reporting has produced none.

## Tooling notes (deep mode degradation)
search-cli was unavailable, and the host fallback was used (run_manifest.json `fallback_reason`). For future deep runs on
this topic, a web-breadth provider (Brave or Serper) and an extraction provider (Jina or Firecrawl) would help reach
X and YouTube transcripts through supported APIs. No Task/Agent tool was available, so helper agents were not spawned.

## Downstream SB route
`silver-ensure-docs` (record the verdict in the ValueRank decision log) → `silver-validate`.
