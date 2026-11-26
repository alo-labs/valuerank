# DR-PLAN — research plan (deep mode)

## Mode rationale
Deep mode (owner instruction). The decision is valuation-critical, stages 1–2 found conflicting evidence on every
near-miss cell, and evidence is user-generated (credibility C–D), so the deep budget (25–30 sources, 2 critique cycles)
applies. Ultradeep was not requested.

## Retrieval tooling (search-cli unavailable)
- Host WebSearch (standard and extended) for discovery across X, YouTube, Substack, Medium, dev.to, note.com, Zenn,
  Qiita, Korean blogs, Bilibili, Zhihu, Weibo.
- curl via the agent proxy: Hacker News Algolia API (comments/stories since 2026-10-10); arctic-shift Reddit API
  (posts/comments with keyword filters, newest index ≈10-24); Bluesky public search API
  (public.api.bsky.app app.bsky.feed.searchPosts); Mastodon (mastodon.social /api/v2/search); GitHub issue pages and
  issue JSON (api.github.com/repos/... if reachable, else WebFetch); Wayback CDX for removed posts; YouTube pages and
  transcripts (yt-dlp absent: try timedtext / youtubetranscript mirrors).
- WebFetch for single pages that curl cannot render.
- Planned 5 parallel helper agents could not be spawned (no Task/Agent tool in this session); retrieval runs
  sequentially, prioritised by which cells are closest to passing.

## Priority order (closest-to-pass first)
1. Gemini 4 Argon AI Pro (three reports at 8.40 / 8.47 / 12.3; one more concordant report does not fix the 12.3 outlier,
   so look for evidence on Low-effort reports and new reports to test the cluster; also Ultra).
2. Claude Opus 5.5 Pro (302 / 321 vs #124); Max 20x (cluster vs 1,140; post-10-17 partition); Max 5x.
3. OpenAI GPT-6 Astra Pro $100 (P2 pair 330–400 / 480); GPT-6.1 Sol Plus (mehoney vs Oleg-125 meter direction).
4. Kimi USD tiers (anything priced on Plus/Pro/Max/Ultra after the 10-24 increase).
5. MiMo and MiniMax (any priced report on a named tier).
6. Sonnet 5.5 / Haiku 5.5 model-pure reports.

## Query strategy (variants)
- English: "<model> <tier> weekly limit $ API equivalent", "ccusage <model> % weekly", "tokens per 1% weekly limit",
  "cost per 5 hour window", "API-equivalent", "usage limit test".
- Chinese: "<model> 额度 实测 美元", "5小时 额度 等效 API", "周限额 测试".
- Japanese: "<model> 週間制限 API換算 ドル", "使用量 上限 ccusage".
- Korean: "<model> 주간 한도 API 환산".
- Schema-change evidence: "<provider> usage limits change October 2026", official status/changelog/help-center pages,
  support e-mails quoted by users, Wayback snapshots of help pages before/after.

## Triangulation approach
- Recompute every dollar figure from quoted tokens at A1 prices.
- Independence: one user = one source; reposts and aggregators (wokey, codingplan.fyi, Fei2411 derived rows) are
  cross-checks only.
- Partitions by documented schema change only (provider statement or corroborated public timestamped measurement).
- O11 test: max/min ≤ 1.20 over all eligible values (ranges must pass over their whole range).

## Quality gates
- Source budget ≥25 new sources, credibility recorded per source (admiralty).
- Validation: validate_report.py, verify_citations.py, verify_claim_support.py verify --dir, phase_gate.py --dir;
  up to 3 repair loops; logs in validation/.
