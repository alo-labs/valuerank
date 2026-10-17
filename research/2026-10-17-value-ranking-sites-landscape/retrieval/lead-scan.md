# Lead broad scan (DR-RETRIEVE, 2026-10-17)

Eight parallel host web searches (search-cli unavailable). These are discovery notes from search-result summaries, not evidence: every claim below must be confirmed from the page itself before it enters `evidence.jsonl`.

## Discovered candidates by cluster

**Aggregators with an explicit value or price-performance view**
- benchlm.ai — "best value overall" and "price vs performance" pages; score ÷ output-token price; 954 models, 639 benchmarks; ranked table dated 2026-10-17.
- modelpricewatch.com/rankings — performance per dollar on blended price; 55+ models.
- whatllm.org/explore — intelligence, agentic capability, cost per task, price, speed; daily refresh.
- llm-stats.com — composite of intelligence, speed, latency, per-token price; 300+ models.
- lmmarketcap.com — 350+ models with source-freshness tags.
- aimodelcomparison.org — "most intelligence per dollar" table (index points ÷ price per million tokens).
- dervity.com/tools/benchmark-dashboard — cost of one benchmark task including thinking tokens.
- discretestack.com — cost per Intelligence Index task (e.g. GLM-5.3-Flash $0.09 per task).
- neura.market/tools/ai-benchmarks — "Best Value" section (intelligence per dollar).
- klu.ai/llm-leaderboard — Klu Index vs price per million tokens; updated 2026-10-13.
- swfte.com/ai/leaderboard, aiven.io/tools/llm-leaderboard, yourgpt.ai, llmleaderboard.in (India focus, dated 2026-07-12), analyticalinsider.ai top-50 with value scores, fast.io, felloai.com.

**Coding-agent cost per task**
- morphllm.com best-ai-coding-agents-2026 (Terminal-Bench 4.0 figures with $/task), tembo.io best-llm-for-coding (SWE-bench Verified $/task), manishprakash2.substack.com (cost per finished task, FrontierCode 1.1), arXiv 2605.08366 SWE Atlas (cost-vs-pass Pareto frontier).

**Subscription plans and allowance trackers**
- Comparison pages: blog.memoryplugin.com, tech-insider.org, altaitools.com, fuelgauge.pro, vortenza.com, aizolo.com, userightai.com/ai-plan-limits, docs.bswen.com, aionx.co.
- Trackers computing API-equivalent value: github.com/efekoca/ai-usage-tracker ("4.7×" over 30 days), github.com/jimdawdy-hub/claude-usage-tracker (savings vs Pro, Max 5×, Max 20×), sessionwatcher.com, custats.info, lpm.cx, claude-monitor.com.

**Critiques and research**
- arXiv 2511.23455 "The Price of Progress: Price Performance and the Future of AI"; arXiv 2510.26136 "Beyond Benchmarks: The Economics of AI Inference"; arXiv 2601.21448 ChipBench (cost per successful pass); cloudchipr.com (hidden reasoning tokens, output vs input pricing); i10x.ai; permutable.ai.

**Non-US**
- SuperCLUE and OpenCompass: scan found no described price dimension; a Jamestown note claims "cost-efficiency" without method. To be confirmed from the live pages.

## Observations to test in triangulation
- Value leaders differ by site because the formulas differ (score ÷ output price, blended price, cost per task including thinking tokens, cost per Index task).
- Several aggregators show stale snapshots (210 days old in one case) and unverifiable model names.
- No scanned site combines benchmark quality with subscription-plan cost at the model level (assumption A1 so far unchallenged).
- Trackers derive allowance value from vendor interface percentages and list prices, not controlled measurements.
