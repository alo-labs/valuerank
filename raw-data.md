# ValueRank v3.0.0 Raw Data

**Updated:** October 19, 2026 · methodology 3.0.0

Every input behind the published scores, with the artifact and locator that holds it. Generated from the committed snapshots in [data/](data/); nothing here is edited by hand.

## Quality leaf inputs

| Configuration | Leaf | Raw value | Unit | Score z | Evaluated configuration / agent | Evidence |
|---|---|---:|---|---:|---|---|
| GPT-6.1 Sol (xhigh) | DeepSWE v1.1 | 73.2 | percent | 73.20 | Codex - GPT-6.1 Sol (xhigh) ({'reasoning_effort': 'xhigh'}) / Codex | `data/aa_deepswe.json` `configurations[valueRankModelId=gpt-6.1-sol-xhigh].scorePct` |
| GPT-6.1 Sol (xhigh) | Bug Hunt Bench | 42.7 | bugs fixed of 105 | 40.67 | GPT-6.1 Sol (xhigh effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6.1-sol-xhigh].fixedOf105` |
| GPT-6.1 Sol (xhigh) | GDPval-AA v2.1 | 1538.05 | Elo | 51.90 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.gdpval` |
| GPT-6.1 Sol (xhigh) | AutomationBench-AA | 0.6657372141364344 | fraction | 66.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.automationBenchPartialScore` |
| GPT-6.1 Sol (xhigh) | AA-Omniscience | 40.86666666666667 | AA Omniscience Index | 70.43 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.omniscience` |
| GPT-6.1 Sol (xhigh) | AA-LCR v1.1 | 0.796666666666667 | fraction | 79.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.lcr` |
| GPT-6.1 Sol (xhigh) | Humanity's Last Exam | 0.526413345690454 | fraction | 52.64 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.hle` |
| GPT-6.1 Sol (xhigh) | SciCode | 0.556712962962963 | fraction | 55.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.scicode` |
| GPT-6.1 Sol (xhigh) | CritPt | 0.317142857142857 | fraction | 31.71 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-xhigh].model.critpt` |
| GPT-6.1 Sol (high) | DeepSWE v1.1 | 70.5 | percent | 70.50 | Codex - GPT-6.1 Sol (high) ({'reasoning_effort': 'high'}) / Codex | `data/aa_deepswe.json` `configurations[valueRankModelId=gpt-6.1-sol-high].scorePct` |
| GPT-6.1 Sol (high) | Bug Hunt Bench | 36.5 | bugs fixed of 105 | 34.76 | GPT-6.1 Sol (high effort) - mean of 2 | `data/bug_hunt.json` `models[modelId=gpt-6.1-sol-high].fixedOf105` |
| GPT-6.1 Sol (high) | GDPval-AA v2.1 | 1511.35 | Elo | 50.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.gdpval` |
| GPT-6.1 Sol (high) | AutomationBench-AA | 0.6449523732184466 | fraction | 64.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.automationBenchPartialScore` |
| GPT-6.1 Sol (high) | AA-Omniscience | 41.45 | AA Omniscience Index | 70.72 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.omniscience` |
| GPT-6.1 Sol (high) | AA-LCR v1.1 | 0.823333333333333 | fraction | 82.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.lcr` |
| GPT-6.1 Sol (high) | Humanity's Last Exam | 0.513901760889713 | fraction | 51.39 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.hle` |
| GPT-6.1 Sol (high) | SciCode | 0.55787037037037 | fraction | 55.79 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.scicode` |
| GPT-6.1 Sol (high) | CritPt | 0.3 | fraction | 30.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.critpt` |
| GPT-6.1 Sol (medium) | DeepSWE v1.1 | 72.0 | percent | 72.00 | Codex - GPT-6.1 Sol (medium) ({'reasoning_effort': 'medium'}) / Codex | `data/aa_deepswe.json` `configurations[valueRankModelId=gpt-6.1-sol-medium].scorePct` |
| GPT-6.1 Sol (medium) | Bug Hunt Bench | 29.0 | bugs fixed of 105 | 27.62 | GPT-6.1 Sol (medium effort) - mean of 2 | `data/bug_hunt.json` `models[modelId=gpt-6.1-sol-medium].fixedOf105` |
| GPT-6.1 Sol (medium) | GDPval-AA v2.1 | 1450.1 | Elo | 47.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.gdpval` |
| GPT-6.1 Sol (medium) | AutomationBench-AA | 0.6257350970435687 | fraction | 62.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.automationBenchPartialScore` |
| GPT-6.1 Sol (medium) | AA-Omniscience | 39.95 | AA Omniscience Index | 69.97 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.omniscience` |
| GPT-6.1 Sol (medium) | AA-LCR v1.1 | 0.833333333333333 | fraction | 83.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.lcr` |
| GPT-6.1 Sol (medium) | Humanity's Last Exam | 0.498609823911029 | fraction | 49.86 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.hle` |
| GPT-6.1 Sol (medium) | SciCode | 0.532407407407407 | fraction | 53.24 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.scicode` |
| GPT-6.1 Sol (medium) | CritPt | 0.277142857142857 | fraction | 27.71 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.critpt` |
| Claude Sonnet 5.5 (max) | DeepSWE v1.1 | 72.0 | percent | 72.00 | Claude Code - Sonnet 5.5 (max) / Claude Code | `data/aa_deepswe.json` `configurations[valueRankModelId=claude-sonnet-5-5].scorePct` |
| Claude Sonnet 5.5 (max) | Bug Hunt Bench | 51.3 | bugs fixed of 105 | 48.86 | Sonnet 5.5 (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-sonnet-5-5].fixedOf105` |
| Claude Sonnet 5.5 (max) | AA FrontierCode 1.1 | 0.458291333333333 | fraction | 45.83 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.frontierCode` |
| Claude Sonnet 5.5 (max) | Terminal-Bench 4.0 (tbench.ai) | 61.8 | percent | 61.80 | Sonnet 5.5 (max) / Claude Code | `data/tb4.json` `rows[model=Sonnet 5.5 (max), agent=Claude Code].resolutionRatePct` |
| Claude Sonnet 5.5 (max) | GDPval-AA v2.1 | 1837.82 | Elo | 66.89 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.gdpval` |
| Claude Sonnet 5.5 (max) | AutomationBench-AA | 0.7176882128193995 | fraction | 71.77 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.automationBenchPartialScore` |
| Claude Sonnet 5.5 (max) | AA-Omniscience | 32.3 | AA Omniscience Index | 66.15 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.omniscience` |
| Claude Sonnet 5.5 (max) | AA-LCR v1.1 | 0.826666666666667 | fraction | 82.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.lcr` |
| Claude Sonnet 5.5 (max) | Humanity's Last Exam | 0.549582947173309 | fraction | 54.96 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.hle` |
| Claude Sonnet 5.5 (max) | SciCode | 0.609953703703704 | fraction | 61.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.scicode` |
| Claude Sonnet 5.5 (max) | CritPt | 0.314285714285714 | fraction | 31.43 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.critpt` |
| Claude Opus 5.5 (max) | DeepSWE v1.1 | 68.4 | percent | 68.40 | Claude Code - Opus 5.5 (max) / Claude Code | `data/aa_deepswe.json` `configurations[valueRankModelId=claude-opus-5-5].scorePct` |
| Claude Opus 5.5 (max) | Bug Hunt Bench | 41.7 | bugs fixed of 105 | 39.71 | Opus 5.5 (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-opus-5-5].fixedOf105` |
| Claude Opus 5.5 (max) | AA FrontierCode 1.1 | 0.521731 | fraction | 52.17 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.frontierCode` |
| Claude Opus 5.5 (max) | Terminal-Bench 4.0 (tbench.ai) | 64.8 | percent | 64.80 | Opus 5.5 (max) / Claude Code | `data/tb4.json` `rows[model=Opus 5.5 (max), agent=Claude Code].resolutionRatePct` |
| Claude Opus 5.5 (max) | GDPval-AA v2.1 | 1866.27 | Elo | 68.31 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.gdpval` |
| Claude Opus 5.5 (max) | AutomationBench-AA | 0.6953868128636069 | fraction | 69.54 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.automationBenchPartialScore` |
| Claude Opus 5.5 (max) | AA-Omniscience | 46.416666666666664 | AA Omniscience Index | 73.21 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.omniscience` |
| Claude Opus 5.5 (max) | AA-LCR v1.1 | 0.846666666666667 | fraction | 84.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.lcr` |
| Claude Opus 5.5 (max) | Humanity's Last Exam | 0.613531047265987 | fraction | 61.35 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.hle` |
| Claude Opus 5.5 (max) | SciCode | 0.668981481481482 | fraction | 66.90 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.scicode` |
| Claude Opus 5.5 (max) | CritPt | 0.317142857142857 | fraction | 31.71 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.critpt` |
| Claude Sonnet 5.5 (xhigh) | DeepSWE v1.1 | 68.4 | percent | 68.40 | Claude Code - Sonnet 5.5 (xhigh) / Claude Code | `data/aa_deepswe.json` `configurations[valueRankModelId=claude-sonnet-5-5-xhigh].scorePct` |
| Claude Sonnet 5.5 (xhigh) | Bug Hunt Bench | 36.0 | bugs fixed of 105 | 34.29 | Sonnet 5.5 (xhigh effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-sonnet-5-5-xhigh].fixedOf105` |
| Claude Sonnet 5.5 (xhigh) | AA FrontierCode 1.1 | 0.461498666666667 | fraction | 46.15 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-xhigh].model.frontierCode` |
| Claude Sonnet 5.5 (xhigh) | GDPval-AA v2.1 | 1728.44 | Elo | 61.42 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-xhigh].model.gdpval` |
| Claude Sonnet 5.5 (xhigh) | AutomationBench-AA | 0.6552026949665557 | fraction | 65.52 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-xhigh].model.automationBenchPartialScore` |
| Claude Sonnet 5.5 (xhigh) | AA-Omniscience | 23.5 | AA Omniscience Index | 61.75 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-xhigh].model.omniscience` |
| Claude Sonnet 5.5 (xhigh) | AA-LCR v1.1 | 0.796666666666667 | fraction | 79.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-xhigh].model.lcr` |
| Claude Sonnet 5.5 (xhigh) | Humanity's Last Exam | 0.5 | fraction | 50.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-xhigh].model.hle` |
| Claude Sonnet 5.5 (xhigh) | SciCode | 0.572916666666667 | fraction | 57.29 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-xhigh].model.scicode` |
| Claude Sonnet 5.5 (xhigh) | CritPt | 0.311428571428571 | fraction | 31.14 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-xhigh].model.critpt` |
| Claude Sonnet 5.5 (high) | DeepSWE v1.1 | 66.7 | percent | 66.70 | Claude Code - Sonnet 5.5 (high) / Claude Code | `data/aa_deepswe.json` `configurations[valueRankModelId=claude-sonnet-5-5-high].scorePct` |
| Claude Sonnet 5.5 (high) | Bug Hunt Bench | 34.3 | bugs fixed of 105 | 32.67 | Sonnet 5.5 (high effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-sonnet-5-5-high].fixedOf105` |
| Claude Sonnet 5.5 (high) | AA FrontierCode 1.1 | 0.442987666666667 | fraction | 44.30 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-high].model.frontierCode` |
| Claude Sonnet 5.5 (high) | GDPval-AA v2.1 | 1549.39 | Elo | 52.47 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-high].model.gdpval` |
| Claude Sonnet 5.5 (high) | AutomationBench-AA | 0.5942923026067375 | fraction | 59.43 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-high].model.automationBenchPartialScore` |
| Claude Sonnet 5.5 (high) | AA-Omniscience | 20.95 | AA Omniscience Index | 60.48 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-high].model.omniscience` |
| Claude Sonnet 5.5 (high) | AA-LCR v1.1 | 0.78 | fraction | 78.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-high].model.lcr` |
| Claude Sonnet 5.5 (high) | Humanity's Last Exam | 0.458294717330862 | fraction | 45.83 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-high].model.hle` |
| Claude Sonnet 5.5 (high) | SciCode | 0.537037037037037 | fraction | 53.70 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-high].model.scicode` |
| Claude Sonnet 5.5 (high) | CritPt | 0.245714285714286 | fraction | 24.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-high].model.critpt` |
| GPT-6.1 Sol (max) | DeepSWE v1.1 | 69.6 | percent | 69.60 | Codex - GPT-6.1 Sol (max) / Codex | `data/aa_deepswe.json` `configurations[valueRankModelId=gpt-6.1-sol].scorePct` |
| GPT-6.1 Sol (max) | Bug Hunt Bench | 44.3 | bugs fixed of 105 | 42.19 | GPT-6.1 Sol (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6.1-sol].fixedOf105` |
| GPT-6.1 Sol (max) | AA FrontierCode 1.1 | 0.491209333333333 | fraction | 49.12 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.frontierCode` |
| GPT-6.1 Sol (max) | Terminal-Bench 4.0 (tbench.ai) | 58.2 | percent | 58.20 | GPT-6.1 Sol (max) / Codex | `data/tb4.json` `rows[model=GPT-6.1 Sol (max), agent=Codex].resolutionRatePct` |
| GPT-6.1 Sol (max) | GDPval-AA v2.1 | 1593.85 | Elo | 54.69 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.gdpval` |
| GPT-6.1 Sol (max) | AutomationBench-AA | 0.6486844882398171 | fraction | 64.87 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.automationBenchPartialScore` |
| GPT-6.1 Sol (max) | AA-Omniscience | 41.53333333333333 | AA Omniscience Index | 70.77 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.omniscience` |
| GPT-6.1 Sol (max) | AA-LCR v1.1 | 0.83 | fraction | 83.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.lcr` |
| GPT-6.1 Sol (max) | Humanity's Last Exam | 0.529193697868397 | fraction | 52.92 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.hle` |
| GPT-6.1 Sol (max) | SciCode | 0.541666666666667 | fraction | 54.17 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.scicode` |
| GPT-6.1 Sol (max) | CritPt | 0.317142857142857 | fraction | 31.71 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.critpt` |
| GPT-6.1 Sol (low) | DeepSWE v1.1 | 67.6 | percent | 67.60 | Codex - GPT-6.1 Sol (low) ({'reasoning_effort': 'low'}) / Codex | `data/aa_deepswe.json` `configurations[valueRankModelId=gpt-6.1-sol-low].scorePct` |
| GPT-6.1 Sol (low) | Bug Hunt Bench | 22.5 | bugs fixed of 105 | 21.43 | GPT-6.1 Sol (low effort) - mean of 2 | `data/bug_hunt.json` `models[modelId=gpt-6.1-sol-low].fixedOf105` |
| GPT-6.1 Sol (low) | GDPval-AA v2.1 | 1314.67 | Elo | 40.73 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.gdpval` |
| GPT-6.1 Sol (low) | AutomationBench-AA | 0.5257088964747538 | fraction | 52.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.automationBenchPartialScore` |
| GPT-6.1 Sol (low) | AA-Omniscience | 37.63333333333333 | AA Omniscience Index | 68.82 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.omniscience` |
| GPT-6.1 Sol (low) | AA-LCR v1.1 | 0.84 | fraction | 84.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.lcr` |
| GPT-6.1 Sol (low) | Humanity's Last Exam | 0.473586654309546 | fraction | 47.36 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.hle` |
| GPT-6.1 Sol (low) | SciCode | 0.532407407407407 | fraction | 53.24 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.scicode` |
| GPT-6.1 Sol (low) | CritPt | 0.248571428571429 | fraction | 24.86 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-low].model.critpt` |
| Claude Sonnet 5.5 (medium) | DeepSWE v1.1 | 65.5 | percent | 65.50 | Claude Code - Sonnet 5.5 (medium) / Claude Code | `data/aa_deepswe.json` `configurations[valueRankModelId=claude-sonnet-5-5-medium].scorePct` |
| Claude Sonnet 5.5 (medium) | Bug Hunt Bench | 23.3 | bugs fixed of 105 | 22.19 | Sonnet 5.5 (medium effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-sonnet-5-5-medium].fixedOf105` |
| Claude Sonnet 5.5 (medium) | AA FrontierCode 1.1 | 0.293075666666667 | fraction | 29.31 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-medium].model.frontierCode` |
| Claude Sonnet 5.5 (medium) | GDPval-AA v2.1 | 1323.27 | Elo | 41.16 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-medium].model.gdpval` |
| Claude Sonnet 5.5 (medium) | AutomationBench-AA | 0.5490962996121462 | fraction | 54.91 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-medium].model.automationBenchPartialScore` |
| Claude Sonnet 5.5 (medium) | AA-Omniscience | 20.1 | AA Omniscience Index | 60.05 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-medium].model.omniscience` |
| Claude Sonnet 5.5 (medium) | AA-LCR v1.1 | 0.763333333333333 | fraction | 76.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-medium].model.lcr` |
| Claude Sonnet 5.5 (medium) | Humanity's Last Exam | 0.39805375347544 | fraction | 39.81 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-medium].model.hle` |
| Claude Sonnet 5.5 (medium) | SciCode | 0.528935185185185 | fraction | 52.89 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-medium].model.scicode` |
| Claude Sonnet 5.5 (medium) | CritPt | 0.168571428571429 | fraction | 16.86 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-medium].model.critpt` |
| Claude Opus 5 (max) | DeepSWE v1.1 | 62.5 | percent | 62.50 | Claude Code - Opus 5 (max) / Claude Code | `data/aa_deepswe.json` `configurations[valueRankModelId=claude-opus-5].scorePct` |
| Claude Opus 5 (max) | Bug Hunt Bench | 27.0 | bugs fixed of 105 | 25.71 | Opus 5 (max effort) | `data/bug_hunt.json` `models[modelId=claude-opus-5].fixedOf105` |
| Claude Opus 5 (max) | GDPval-AA v2.1 | 1721.15 | Elo | 61.06 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5].model.gdpval` |
| Claude Opus 5 (max) | AutomationBench-AA | 0.565735557649325 | fraction | 56.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5].model.automationBenchPartialScore` |
| Claude Opus 5 (max) | AA-Omniscience | 37.06666666666667 | AA Omniscience Index | 68.53 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5].model.omniscience` |
| Claude Opus 5 (max) | AA-LCR v1.1 | 0.793333333333333 | fraction | 79.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5].model.lcr` |
| Claude Opus 5 (max) | Humanity's Last Exam | 0.548656163113994 | fraction | 54.87 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5].model.hle` |
| Claude Opus 5 (max) | SciCode | 0.563657407407407 | fraction | 56.37 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5].model.scicode` |
| Claude Opus 5 (max) | CritPt | 0.291428571428571 | fraction | 29.14 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5].model.critpt` |
| GPT-6 Sol (max) | DeepSWE v1.1 | 69.0 | percent | 69.00 | Codex - GPT-6 Sol (max) / Codex | `data/aa_deepswe.json` `configurations[valueRankModelId=gpt-6-sol].scorePct` |
| GPT-6 Sol (max) | Bug Hunt Bench | 29.3 | bugs fixed of 105 | 27.90 | GPT-6 Sol MAX - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6-sol].fixedOf105` |
| GPT-6 Sol (max) | Terminal-Bench 4.0 (tbench.ai) | 49.4 | percent | 49.40 | GPT-6 Sol (max) / Codex | `data/tb4.json` `rows[model=GPT-6 Sol (max), agent=Codex].resolutionRatePct` |
| GPT-6 Sol (max) | GDPval-AA v2.1 | 1508.23 | Elo | 50.41 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-sol].model.gdpval` |
| GPT-6 Sol (max) | AutomationBench-AA | 0.6163369295959864 | fraction | 61.63 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-sol].model.automationBenchPartialScore` |
| GPT-6 Sol (max) | AA-Omniscience | 27.116666666666667 | AA Omniscience Index | 63.56 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-sol].model.omniscience` |
| GPT-6 Sol (max) | AA-LCR v1.1 | 0.836666666666667 | fraction | 83.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-sol].model.lcr` |
| GPT-6 Sol (max) | Humanity's Last Exam | 0.479147358665431 | fraction | 47.91 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-sol].model.hle` |
| GPT-6 Sol (max) | SciCode | 0.576388888888889 | fraction | 57.64 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-sol].model.scicode` |
| GPT-6 Sol (max) | CritPt | 0.308571428571429 | fraction | 30.86 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-sol].model.critpt` |
| Claude Haiku 5.5 (xhigh) | DeepSWE v1.1 | 49.0 | percent | 49.00 | Claude Code - Haiku 5.5 (xhigh) / Claude Code | `data/aa_deepswe.json` `configurations[valueRankModelId=claude-haiku-5-5].scorePct` |
| Claude Haiku 5.5 (xhigh) | Bug Hunt Bench | 18.3 | bugs fixed of 105 | 17.43 | Haiku 5.5 (xhigh effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-haiku-5-5].fixedOf105` |
| Claude Haiku 5.5 (xhigh) | AA FrontierCode 1.1 | 0.45471 | fraction | 45.47 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-xhigh].model.frontierCode` |
| Claude Haiku 5.5 (xhigh) | GDPval-AA v2.1 | 1513.05 | Elo | 50.65 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-xhigh].model.gdpval` |
| Claude Haiku 5.5 (xhigh) | AutomationBench-AA | 0.35953889773428194 | fraction | 35.95 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-xhigh].model.automationBenchPartialScore` |
| Claude Haiku 5.5 (xhigh) | AA-Omniscience | 6.05 | AA Omniscience Index | 53.02 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-xhigh].model.omniscience` |
| Claude Haiku 5.5 (xhigh) | AA-LCR v1.1 | 0.783333333333333 | fraction | 78.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-xhigh].model.lcr` |
| Claude Haiku 5.5 (xhigh) | Humanity's Last Exam | 0.42678405931418 | fraction | 42.68 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-xhigh].model.hle` |
| Claude Haiku 5.5 (xhigh) | SciCode | 0.517361111111111 | fraction | 51.74 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-xhigh].model.scicode` |
| Claude Haiku 5.5 (xhigh) | CritPt | 0.225714285714286 | fraction | 22.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-xhigh].model.critpt` |
| Claude Sonnet 5.5 (low) | DeepSWE v1.1 | 61.9 | percent | 61.90 | Claude Code - Sonnet 5.5 (low) / Claude Code | `data/aa_deepswe.json` `configurations[valueRankModelId=claude-sonnet-5-5-low].scorePct` |
| Claude Sonnet 5.5 (low) | Bug Hunt Bench | 19.0 | bugs fixed of 105 | 18.10 | Sonnet 5.5 (low effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-sonnet-5-5-low].fixedOf105` |
| Claude Sonnet 5.5 (low) | AA FrontierCode 1.1 | 0.264162666666667 | fraction | 26.42 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-low].model.frontierCode` |
| Claude Sonnet 5.5 (low) | GDPval-AA v2.1 | 1175.34 | Elo | 33.77 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-low].model.gdpval` |
| Claude Sonnet 5.5 (low) | AutomationBench-AA | 0.4942092641344955 | fraction | 49.42 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-low].model.automationBenchPartialScore` |
| Claude Sonnet 5.5 (low) | AA-Omniscience | 19.366666666666667 | AA Omniscience Index | 59.68 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-low].model.omniscience` |
| Claude Sonnet 5.5 (low) | AA-LCR v1.1 | 0.76 | fraction | 76.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-low].model.lcr` |
| Claude Sonnet 5.5 (low) | Humanity's Last Exam | 0.362372567191844 | fraction | 36.24 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-low].model.hle` |
| Claude Sonnet 5.5 (low) | SciCode | 0.490740740740741 | fraction | 49.07 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-low].model.scicode` |
| Claude Sonnet 5.5 (low) | CritPt | 0.114285714285714 | fraction | 11.43 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5-low].model.critpt` |
| GPT-5.6 Sol (max) | DeepSWE v1.1 | 72.3 | percent | 72.30 | Codex - GPT-5.6 Sol (max) ({'reasoning_effort': 'max'}) / Codex | `data/aa_deepswe.json` `configurations[valueRankModelId=gpt-5.6-sol].scorePct` |
| GPT-5.6 Sol (max) | Bug Hunt Bench | 43.5 | bugs fixed of 105 | 41.43 | GPT-5.6 Sol (max effort) - mean of 2 | `data/bug_hunt.json` `models[modelId=gpt-5.6-sol].fixedOf105` |
| GPT-5.6 Sol (max) | Terminal-Bench 4.0 (tbench.ai) | 37.3 | percent | 37.30 | GPT-5.6 Sol (max) / Codex | `data/tb4.json` `rows[model=GPT-5.6 Sol (max), agent=Codex].resolutionRatePct` |
| GPT-5.6 Sol (max) | GDPval-AA v2.1 | 1608.63 | Elo | 55.43 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-sol].model.gdpval` |
| GPT-5.6 Sol (max) | AutomationBench-AA | 0.6008114996276329 | fraction | 60.08 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-sol].model.automationBenchPartialScore` |
| GPT-5.6 Sol (max) | AA-Omniscience | 21.966666666666665 | AA Omniscience Index | 60.98 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-sol].model.omniscience` |
| GPT-5.6 Sol (max) | AA-LCR v1.1 | 0.84 | fraction | 84.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-sol].model.lcr` |
| GPT-5.6 Sol (max) | Humanity's Last Exam | 0.494902687673772 | fraction | 49.49 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-sol].model.hle` |
| GPT-5.6 Sol (max) | SciCode | 0.570601851851852 | fraction | 57.06 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-sol].model.scicode` |
| GPT-5.6 Sol (max) | CritPt | 0.322857142857143 | fraction | 32.29 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-sol].model.critpt` |
| GPT-6 Luna (max) | DeepSWE v1.1 | 63.7 | percent | 63.70 | Codex - GPT-6 Luna (max) ({'reasoning_effort': 'max'}) / Codex | `data/aa_deepswe.json` `configurations[valueRankModelId=gpt-6-luna].scorePct` |
| GPT-6 Luna (max) | Bug Hunt Bench | 18.3 | bugs fixed of 105 | 17.43 | GPT-6 Luna MAX - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6-luna].fixedOf105` |
| GPT-6 Luna (max) | AA FrontierCode 1.1 | 0.419269666666667 | fraction | 41.93 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.frontierCode` |
| GPT-6 Luna (max) | Terminal-Bench 4.0 (tbench.ai) | 16.4 | percent | 16.40 | GPT-6 Luna (max) / Codex | `data/tb4.json` `rows[model=GPT-6 Luna (max), agent=Codex].resolutionRatePct` |
| GPT-6 Luna (max) | GDPval-AA v2.1 | 1431.86 | Elo | 46.59 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.gdpval` |
| GPT-6 Luna (max) | AutomationBench-AA | 0.5316814034483175 | fraction | 53.17 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.automationBenchPartialScore` |
| GPT-6 Luna (max) | AA-Omniscience | 0.65 | AA Omniscience Index | 50.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.omniscience` |
| GPT-6 Luna (max) | AA-LCR v1.1 | 0.833333333333333 | fraction | 83.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.lcr` |
| GPT-6 Luna (max) | Humanity's Last Exam | 0.385078776645042 | fraction | 38.51 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.hle` |
| GPT-6 Luna (max) | SciCode | 0.546296296296296 | fraction | 54.63 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.scicode` |
| GPT-6 Luna (max) | CritPt | 0.194285714285714 | fraction | 19.43 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.critpt` |
| Claude Haiku 5.5 (high) | DeepSWE v1.1 | 46.3 | percent | 46.30 | Claude Code - Haiku 5.5 (high) / Claude Code | `data/aa_deepswe.json` `configurations[valueRankModelId=claude-haiku-5-5-high].scorePct` |
| Claude Haiku 5.5 (high) | Bug Hunt Bench | 16.0 | bugs fixed of 105 | 15.24 | Haiku 5.5 (high effort) - mean of 2 | `data/bug_hunt.json` `models[modelId=claude-haiku-5-5-high].fixedOf105` |
| Claude Haiku 5.5 (high) | AA FrontierCode 1.1 | 0.436422666666667 | fraction | 43.64 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.frontierCode` |
| Claude Haiku 5.5 (high) | GDPval-AA v2.1 | 1417.55 | Elo | 45.88 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.gdpval` |
| Claude Haiku 5.5 (high) | AutomationBench-AA | 0.3372685311767238 | fraction | 33.73 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.automationBenchPartialScore` |
| Claude Haiku 5.5 (high) | AA-Omniscience | 5.75 | AA Omniscience Index | 52.88 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.omniscience` |
| Claude Haiku 5.5 (high) | AA-LCR v1.1 | 0.773333333333333 | fraction | 77.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.lcr` |
| Claude Haiku 5.5 (high) | Humanity's Last Exam | 0.3725671918443 | fraction | 37.26 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.hle` |
| Claude Haiku 5.5 (high) | SciCode | 0.487268518518519 | fraction | 48.73 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.scicode` |
| Claude Haiku 5.5 (high) | CritPt | 0.185714285714286 | fraction | 18.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.critpt` |
| GPT-6 Astra (max) | DeepSWE v1.1 | 67.6 | percent | 67.60 | Codex - GPT-6 Astra (max) / Codex | `data/aa_deepswe.json` `configurations[valueRankModelId=gpt-6-astra].scorePct` |
| GPT-6 Astra (max) | Bug Hunt Bench | 45.0 | bugs fixed of 105 | 42.86 | GPT-6 Astra (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6-astra].fixedOf105` |
| GPT-6 Astra (max) | AA FrontierCode 1.1 | 0.469827666666667 | fraction | 46.98 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.frontierCode` |
| GPT-6 Astra (max) | Terminal-Bench 4.0 (tbench.ai) | 58.2 | percent | 58.20 | GPT-6 Astra (max) / Codex | `data/tb4.json` `rows[model=GPT-6 Astra (max), agent=Codex].resolutionRatePct` |
| GPT-6 Astra (max) | GDPval-AA v2.1 | 1572.84 | Elo | 53.64 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.gdpval` |
| GPT-6 Astra (max) | AutomationBench-AA | 0.6849174806688876 | fraction | 68.49 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.automationBenchPartialScore` |
| GPT-6 Astra (max) | AA-Omniscience | 43.4 | AA Omniscience Index | 71.70 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.omniscience` |
| GPT-6 Astra (max) | AA-LCR v1.1 | 0.806666666666667 | fraction | 80.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.lcr` |
| GPT-6 Astra (max) | Humanity's Last Exam | 0.546802594995366 | fraction | 54.68 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.hle` |
| GPT-6 Astra (max) | SciCode | 0.564814814814815 | fraction | 56.48 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.scicode` |
| GPT-6 Astra (max) | CritPt | 0.317142857142857 | fraction | 31.71 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.critpt` |
| Claude Haiku 5.5 (medium) | DeepSWE v1.1 | 47.5 | percent | 47.50 | Claude Code - Haiku 5.5 (medium) / Claude Code | `data/aa_deepswe.json` `configurations[valueRankModelId=claude-haiku-5-5-medium].scorePct` |
| Claude Haiku 5.5 (medium) | Bug Hunt Bench | 12.0 | bugs fixed of 105 | 11.43 | Haiku 5.5 (medium effort) | `data/bug_hunt.json` `models[modelId=claude-haiku-5-5-medium].fixedOf105` |
| Claude Haiku 5.5 (medium) | AA FrontierCode 1.1 | 0.404265666666667 | fraction | 40.43 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.frontierCode` |
| Claude Haiku 5.5 (medium) | GDPval-AA v2.1 | 1274.5 | Elo | 38.73 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.gdpval` |
| Claude Haiku 5.5 (medium) | AutomationBench-AA | 0.2858961481429316 | fraction | 28.59 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.automationBenchPartialScore` |
| Claude Haiku 5.5 (medium) | AA-Omniscience | 4.466666666666667 | AA Omniscience Index | 52.23 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.omniscience` |
| Claude Haiku 5.5 (medium) | AA-LCR v1.1 | 0.773333333333333 | fraction | 77.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.lcr` |
| Claude Haiku 5.5 (medium) | Humanity's Last Exam | 0.337812789620019 | fraction | 33.78 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.hle` |
| Claude Haiku 5.5 (medium) | SciCode | 0.489583333333333 | fraction | 48.96 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.scicode` |
| Claude Haiku 5.5 (medium) | CritPt | 0.128571428571429 | fraction | 12.86 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.critpt` |
| GPT-5.6 Luna (max) | DeepSWE v1.1 | 66.4 | percent | 66.40 | Codex - GPT-5.6 Luna (max) / Codex | `data/aa_deepswe.json` `configurations[valueRankModelId=gpt-5.6-luna].scorePct` |
| GPT-5.6 Luna (max) | Bug Hunt Bench | 31.3 | bugs fixed of 105 | 29.81 | GPT-5.6 Luna (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-5.6-luna].fixedOf105` |
| GPT-5.6 Luna (max) | Terminal-Bench 4.0 (tbench.ai) | 17.3 | percent | 17.30 | GPT-5.6 Luna (max) / Codex | `data/tb4.json` `rows[model=GPT-5.6 Luna (max), agent=Codex].resolutionRatePct` |
| GPT-5.6 Luna (max) | GDPval-AA v2.1 | 1459.2 | Elo | 47.96 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-luna].model.gdpval` |
| GPT-5.6 Luna (max) | AutomationBench-AA | 0.5020861763756194 | fraction | 50.21 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-luna].model.automationBenchPartialScore` |
| GPT-5.6 Luna (max) | AA-Omniscience | -10.283333333333333 | AA Omniscience Index | 44.86 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-luna].model.omniscience` |
| GPT-5.6 Luna (max) | AA-LCR v1.1 | 0.836666666666667 | fraction | 83.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-luna].model.lcr` |
| GPT-5.6 Luna (max) | Humanity's Last Exam | 0.394810009267841 | fraction | 39.48 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-luna].model.hle` |
| GPT-5.6 Luna (max) | SciCode | 0.53587962962963 | fraction | 53.59 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-luna].model.scicode` |
| GPT-5.6 Luna (max) | CritPt | 0.205714285714286 | fraction | 20.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-luna].model.critpt` |
| Gemini 4 Argon (high) | DeepSWE v1.1 | 78.8 | percent | 78.80 | Antigravity CLI - Gemini 4 Argon (high) / Antigravity CLI | `data/aa_deepswe.json` `configurations[valueRankModelId=gemini-4-argon].scorePct` |
| Gemini 4 Argon (high) | Bug Hunt Bench | 40.7 | bugs fixed of 105 | 38.76 | Gemini 4 Argon (high effort, Antigravity CLI) - mean of 3 | `data/bug_hunt.json` `models[modelId=gemini-4-argon].fixedOf105` |
| Gemini 4 Argon (high) | AA FrontierCode 1.1 | 0.434532 | fraction | 43.45 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-4-argon].model.frontierCode` |
| Gemini 4 Argon (high) | GDPval-AA v2.1 | 1623.99 | Elo | 56.20 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-4-argon].model.gdpval` |
| Gemini 4 Argon (high) | AutomationBench-AA | 0.7751346945899195 | fraction | 77.51 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-4-argon].model.automationBenchPartialScore` |
| Gemini 4 Argon (high) | AA-Omniscience | 42.35 | AA Omniscience Index | 71.17 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-4-argon].model.omniscience` |
| Gemini 4 Argon (high) | AA-LCR v1.1 | 0.796666666666667 | fraction | 79.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-4-argon].model.lcr` |
| Gemini 4 Argon (high) | Humanity's Last Exam | 0.570898980537535 | fraction | 57.09 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-4-argon].model.hle` |
| Gemini 4 Argon (high) | SciCode | 0.618055555555556 | fraction | 61.81 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-4-argon].model.scicode` |
| Gemini 4 Argon (high) | CritPt | 0.271428571428571 | fraction | 27.14 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-4-argon].model.critpt` |
| Claude Fable 5.1 (max) | DeepSWE v1.1 | 64.3 | percent | 64.30 | Claude Code - Fable 5.1 (max) (with fallback) / Claude Code | `data/aa_deepswe.json` `configurations[valueRankModelId=claude-fable-5-1].scorePct` |
| Claude Fable 5.1 (max) | Bug Hunt Bench | 43.0 | bugs fixed of 105 | 40.95 | Fable 5.1 (max effort) | `data/bug_hunt.json` `models[modelId=claude-fable-5-1].fixedOf105` |
| Claude Fable 5.1 (max) | AA FrontierCode 1.1 | 0.489732333333333 | fraction | 48.97 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-1].model.frontierCode` |
| Claude Fable 5.1 (max) | Terminal-Bench 4.0 (tbench.ai) | 57.9 | percent | 57.90 | Fable 5.1 (max) / Claude Code | `data/tb4.json` `rows[model=Fable 5.1 (max), agent=Claude Code].resolutionRatePct` |
| Claude Fable 5.1 (max) | GDPval-AA v2.1 | 1754.07 | Elo | 62.70 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-1].model.gdpval` |
| Claude Fable 5.1 (max) | AutomationBench-AA | 0.5937591715646424 | fraction | 59.38 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-1].model.automationBenchPartialScore` |
| Claude Fable 5.1 (max) | AA-Omniscience | 43.45 | AA Omniscience Index | 71.72 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-1].model.omniscience` |
| Claude Fable 5.1 (max) | AA-LCR v1.1 | 0.853333333333333 | fraction | 85.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-1].model.lcr` |
| Claude Fable 5.1 (max) | Humanity's Last Exam | 0.591288229842447 | fraction | 59.13 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-1].model.hle` |
| Claude Fable 5.1 (max) | SciCode | 0.630787037037037 | fraction | 63.08 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-1].model.scicode` |
| Claude Fable 5.1 (max) | CritPt | 0.297142857142857 | fraction | 29.71 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-fable-5-1].model.critpt` |
| MiMo-V2.6-Flash | AA FrontierCode 1.1 | 0.420675333333333 | fraction | 42.07 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-flash].model.frontierCode` |
| MiMo-V2.6-Flash | GDPval-AA v2.1 | 1607.51 | Elo | 55.38 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-flash].model.gdpval` |
| MiMo-V2.6-Flash | AutomationBench-AA | 0.6405168250285657 | fraction | 64.05 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-flash].model.automationBenchPartialScore` |
| MiMo-V2.6-Flash | AA-Omniscience | -12.683333333333334 | AA Omniscience Index | 43.66 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-flash].model.omniscience` |
| MiMo-V2.6-Flash | AA-LCR v1.1 | 0.743333333333333 | fraction | 74.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-flash].model.lcr` |
| MiMo-V2.6-Flash | Humanity's Last Exam | 0.350787766450417 | fraction | 35.08 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-flash].model.hle` |
| MiMo-V2.6-Flash | SciCode | 0.512731481481482 | fraction | 51.27 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-flash].model.scicode` |
| MiMo-V2.6-Flash | CritPt | 0.12 | fraction | 12.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-flash].model.critpt` |
| Claude Haiku 5.5 (low) | DeepSWE v1.1 | 45.4 | percent | 45.40 | Claude Code - Haiku 5.5 (low) / Claude Code | `data/aa_deepswe.json` `configurations[valueRankModelId=claude-haiku-5-5-low].scorePct` |
| Claude Haiku 5.5 (low) | Bug Hunt Bench | 11.0 | bugs fixed of 105 | 10.48 | Haiku 5.5 (low effort) | `data/bug_hunt.json` `models[modelId=claude-haiku-5-5-low].fixedOf105` |
| Claude Haiku 5.5 (low) | AA FrontierCode 1.1 | 0.293338 | fraction | 29.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.frontierCode` |
| Claude Haiku 5.5 (low) | GDPval-AA v2.1 | 1122.82 | Elo | 31.14 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.gdpval` |
| Claude Haiku 5.5 (low) | AutomationBench-AA | 0.22910812181110643 | fraction | 22.91 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.automationBenchPartialScore` |
| Claude Haiku 5.5 (low) | AA-Omniscience | 3.25 | AA Omniscience Index | 51.62 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.omniscience` |
| Claude Haiku 5.5 (low) | AA-LCR v1.1 | 0.72 | fraction | 72.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.lcr` |
| Claude Haiku 5.5 (low) | Humanity's Last Exam | 0.270157553290083 | fraction | 27.02 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.hle` |
| Claude Haiku 5.5 (low) | SciCode | 0.491898148148148 | fraction | 49.19 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.scicode` |
| Claude Haiku 5.5 (low) | CritPt | 0.0914285714285714 | fraction | 9.14 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-low].model.critpt` |
| Claude Haiku 5.5 (max) | DeepSWE v1.1 | 46.0 | percent | 46.00 | Claude Code - Haiku 5.5 (max) / Claude Code | `data/aa_deepswe.json` `configurations[valueRankModelId=claude-haiku-5-5-max].scorePct` |
| Claude Haiku 5.5 (max) | Bug Hunt Bench | 21.5 | bugs fixed of 105 | 20.48 | Haiku 5.5 (max effort) - mean of 2 | `data/bug_hunt.json` `models[modelId=claude-haiku-5-5-max].fixedOf105` |
| Claude Haiku 5.5 (max) | AA FrontierCode 1.1 | 0.418067 | fraction | 41.81 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5].model.frontierCode` |
| Claude Haiku 5.5 (max) | GDPval-AA v2.1 | 1618.33 | Elo | 55.92 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5].model.gdpval` |
| Claude Haiku 5.5 (max) | AutomationBench-AA | 0.35411015132783624 | fraction | 35.41 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5].model.automationBenchPartialScore` |
| Claude Haiku 5.5 (max) | AA-Omniscience | 10.666666666666666 | AA Omniscience Index | 55.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5].model.omniscience` |
| Claude Haiku 5.5 (max) | AA-LCR v1.1 | 0.826666666666667 | fraction | 82.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5].model.lcr` |
| Claude Haiku 5.5 (max) | Humanity's Last Exam | 0.443929564411492 | fraction | 44.39 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5].model.hle` |
| Claude Haiku 5.5 (max) | SciCode | 0.549768518518518 | fraction | 54.98 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5].model.scicode` |
| Claude Haiku 5.5 (max) | CritPt | 0.188571428571429 | fraction | 18.86 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5].model.critpt` |
| Muse Wonder (max) | DeepSWE v1.1 | 75.8 | percent | 75.80 | Muse Code - Muse Wonder (max) / Muse Code | `data/aa_deepswe.json` `configurations[valueRankModelId=muse-wonder].scorePct` |
| Muse Wonder (max) | Bug Hunt Bench | 31.7 | bugs fixed of 105 | 30.19 | Muse Wonder 1.0 (max effort, Muse Code, Meta API) - mean of 3 | `data/bug_hunt.json` `models[modelId=muse-wonder].fixedOf105` |
| Muse Wonder (max) | GDPval-AA v2.1 | 1770.34 | Elo | 63.52 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-wonder].model.gdpval` |
| Muse Wonder (max) | AutomationBench-AA | 0.6809455131207758 | fraction | 68.09 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-wonder].model.automationBenchPartialScore` |
| Muse Wonder (max) | AA-Omniscience | 25.483333333333334 | AA Omniscience Index | 62.74 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-wonder].model.omniscience` |
| Muse Wonder (max) | AA-LCR v1.1 | 0.806666666666667 | fraction | 80.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-wonder].model.lcr` |
| Muse Wonder (max) | Humanity's Last Exam | 0.500926784059314 | fraction | 50.09 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-wonder].model.hle` |
| Muse Wonder (max) | SciCode | 0.603009259259259 | fraction | 60.30 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-wonder].model.scicode` |
| Muse Wonder (max) | CritPt | 0.282857142857143 | fraction | 28.29 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-wonder].model.critpt` |
| MiMo-V2.6-Pro | Bug Hunt Bench | 18 | bugs fixed of 105 | 17.14 | MiMo-V2.6-Pro (first-party, thinking enabled) | `data/bug_hunt.json` `models[modelId=mimo-v2-6-pro].fixedOf105` |
| MiMo-V2.6-Pro | AA FrontierCode 1.1 | 0.454153333333333 | fraction | 45.42 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-pro].model.frontierCode` |
| MiMo-V2.6-Pro | GDPval-AA v2.1 | 1684.34 | Elo | 59.22 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-pro].model.gdpval` |
| MiMo-V2.6-Pro | AutomationBench-AA | 0.5862340943419085 | fraction | 58.62 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-pro].model.automationBenchPartialScore` |
| MiMo-V2.6-Pro | AA-Omniscience | 8.383333333333333 | AA Omniscience Index | 54.19 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-pro].model.omniscience` |
| MiMo-V2.6-Pro | AA-LCR v1.1 | 0.863333333333333 | fraction | 86.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-pro].model.lcr` |
| MiMo-V2.6-Pro | Humanity's Last Exam | 0.493512511584801 | fraction | 49.35 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-pro].model.hle` |
| MiMo-V2.6-Pro | SciCode | 0.608796296296296 | fraction | 60.88 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-pro].model.scicode` |
| MiMo-V2.6-Pro | CritPt | 0.265714285714286 | fraction | 26.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-pro].model.critpt` |
| Muse Spark 1.3 (max) | DeepSWE v1.1 | 71.7 | percent | 71.70 | Muse Code - Muse Spark 1.3 (max) / Muse Code | `data/aa_deepswe.json` `configurations[valueRankModelId=muse-spark-1-3].scorePct` |
| Muse Spark 1.3 (max) | Bug Hunt Bench | 32.2 | bugs fixed of 105 | 30.67 | Muse Spark 1.3 (max effort, Muse Code, Meta API) - mean of 5 | `data/bug_hunt.json` `models[modelId=muse-spark-1-3].fixedOf105` |
| Muse Spark 1.3 (max) | AA FrontierCode 1.1 | 0.406458333333333 | fraction | 40.65 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-spark-1-3].model.frontierCode` |
| Muse Spark 1.3 (max) | GDPval-AA v2.1 | 1680.99 | Elo | 59.05 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-spark-1-3].model.gdpval` |
| Muse Spark 1.3 (max) | AutomationBench-AA | 0.5785343786538614 | fraction | 57.85 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-spark-1-3].model.automationBenchPartialScore` |
| Muse Spark 1.3 (max) | AA-Omniscience | 25 | AA Omniscience Index | 62.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-spark-1-3].model.omniscience` |
| Muse Spark 1.3 (max) | AA-LCR v1.1 | 0.83 | fraction | 83.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-spark-1-3].model.lcr` |
| Muse Spark 1.3 (max) | Humanity's Last Exam | 0.487025023169602 | fraction | 48.70 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-spark-1-3].model.hle` |
| Muse Spark 1.3 (max) | SciCode | 0.587962962962963 | fraction | 58.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-spark-1-3].model.scicode` |
| Muse Spark 1.3 (max) | CritPt | 0.248571428571429 | fraction | 24.86 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-spark-1-3].model.critpt` |
| Grok 4.6 (xhigh) | DeepSWE v1.1 | 64.9 | percent | 64.90 | Grok Build - Grok 4.6 (xhigh) / Grok Build | `data/aa_deepswe.json` `configurations[valueRankModelId=grok-4.6-xhigh].scorePct` |
| Grok 4.6 (xhigh) | Bug Hunt Bench | 28.7 | bugs fixed of 105 | 27.33 | Grok 4.6 (xhigh) seq - mean of 3 | `data/bug_hunt.json` `models[modelId=grok-4.6-xhigh].fixedOf105` |
| Grok 4.6 (xhigh) | GDPval-AA v2.1 | 1645.38 | Elo | 57.27 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=grok-4-6-xhigh].model.gdpval` |
| Grok 4.6 (xhigh) | AutomationBench-AA | 0.6699736836183247 | fraction | 67.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=grok-4-6-xhigh].model.automationBenchPartialScore` |
| Grok 4.6 (xhigh) | AA-Omniscience | 29.316666666666666 | AA Omniscience Index | 64.66 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=grok-4-6-xhigh].model.omniscience` |
| Grok 4.6 (xhigh) | AA-LCR v1.1 | 0.81 | fraction | 81.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=grok-4-6-xhigh].model.lcr` |
| Grok 4.6 (xhigh) | Humanity's Last Exam | 0.440685820203893 | fraction | 44.07 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=grok-4-6-xhigh].model.hle` |
| Grok 4.6 (xhigh) | SciCode | 0.530092592592593 | fraction | 53.01 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=grok-4-6-xhigh].model.scicode` |
| Grok 4.6 (xhigh) | CritPt | 0.197142857142857 | fraction | 19.71 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=grok-4-6-xhigh].model.critpt` |
| DeepSeek V4 Flash (max) | DeepSWE v1.1 | 54.3 | percent | 54.30 | Codex - DeepSeek V4 Flash 0731 (max) / Codex | `data/aa_deepswe.json` `configurations[valueRankModelId=deepseek-v4-flash].scorePct` |
| DeepSeek V4 Flash (max) | Bug Hunt Bench | 21.7 | bugs fixed of 105 | 20.67 | DeepSeek V4.1 Flash (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=deepseek-v4-flash].fixedOf105` |
| DeepSeek V4 Flash (max) | GDPval-AA v2.1 | 1433.74 | Elo | 46.69 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-flash].model.gdpval` |
| DeepSeek V4 Flash (max) | AutomationBench-AA | 0.5396771855133674 | fraction | 53.97 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-flash].model.automationBenchPartialScore` |
| DeepSeek V4 Flash (max) | AA-Omniscience | -14.283333333333333 | AA Omniscience Index | 42.86 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-flash].model.omniscience` |
| DeepSeek V4 Flash (max) | AA-LCR v1.1 | 0.796666666666667 | fraction | 79.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-flash].model.lcr` |
| DeepSeek V4 Flash (max) | Humanity's Last Exam | 0.385542168674699 | fraction | 38.55 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-flash].model.hle` |
| DeepSeek V4 Flash (max) | SciCode | 0.503472222222222 | fraction | 50.35 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-flash].model.scicode` |
| DeepSeek V4 Flash (max) | CritPt | 0.165714285714286 | fraction | 16.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-flash].model.critpt` |
| Muse Spark 1.3 (xhigh) | DeepSWE v1.1 | 73.2 | percent | 73.20 | Muse Code - Muse Spark 1.3 (xhigh) / Muse Code | `data/aa_deepswe.json` `configurations[valueRankModelId=muse-spark-1-3-xhigh].scorePct` |
| Muse Spark 1.3 (xhigh) | Bug Hunt Bench | 20.3 | bugs fixed of 105 | 19.33 | Muse Spark 1.3 (xhigh effort, Muse Code, Meta API) - mean of 3 | `data/bug_hunt.json` `models[modelId=muse-spark-1-3-xhigh].fixedOf105` |
| Muse Spark 1.3 (xhigh) | Terminal-Bench 4.0 (tbench.ai) | 14.5 | percent | 14.50 | Muse Spark 1.3 (xhigh) / Muse Code | `data/tb4.json` `rows[model=Muse Spark 1.3 (xhigh), agent=Muse Code].resolutionRatePct` |
| Muse Spark 1.3 (xhigh) | GDPval-AA v2.1 | 1626.61 | Elo | 56.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-spark-1-3-xhigh].model.gdpval` |
| Muse Spark 1.3 (xhigh) | AutomationBench-AA | 0.5683609003249621 | fraction | 56.84 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-spark-1-3-xhigh].model.automationBenchPartialScore` |
| Muse Spark 1.3 (xhigh) | AA-Omniscience | 23.116666666666667 | AA Omniscience Index | 61.56 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-spark-1-3-xhigh].model.omniscience` |
| Muse Spark 1.3 (xhigh) | AA-LCR v1.1 | 0.83 | fraction | 83.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-spark-1-3-xhigh].model.lcr` |
| Muse Spark 1.3 (xhigh) | Humanity's Last Exam | 0.47451343836886 | fraction | 47.45 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-spark-1-3-xhigh].model.hle` |
| Muse Spark 1.3 (xhigh) | SciCode | 0.597222222222222 | fraction | 59.72 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-spark-1-3-xhigh].model.scicode` |
| Muse Spark 1.3 (xhigh) | CritPt | 0.26 | fraction | 26.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-spark-1-3-xhigh].model.critpt` |
| DeepSeek V4 Pro (max) | DeepSWE v1.1 | 57.2 | percent | 57.20 | Codex - DeepSeek V4 Pro 0813 (max) / Codex | `data/aa_deepswe.json` `configurations[valueRankModelId=deepseek-v4-pro].scorePct` |
| DeepSeek V4 Pro (max) | Bug Hunt Bench | 16.0 | bugs fixed of 105 | 15.24 | DeepSeek V4-Pro (max effort, DeepSeek API) | `data/bug_hunt.json` `models[modelId=deepseek-v4-pro].fixedOf105` |
| DeepSeek V4 Pro (max) | GDPval-AA v2.1 | 1450.47 | Elo | 47.52 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-pro].model.gdpval` |
| DeepSeek V4 Pro (max) | AutomationBench-AA | 0.5671165546344002 | fraction | 56.71 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-pro].model.automationBenchPartialScore` |
| DeepSeek V4 Pro (max) | AA-Omniscience | 0.8333333333333334 | AA Omniscience Index | 50.42 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-pro].model.omniscience` |
| DeepSeek V4 Pro (max) | AA-LCR v1.1 | 0.803333333333333 | fraction | 80.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-pro].model.lcr` |
| DeepSeek V4 Pro (max) | Humanity's Last Exam | 0.410101946246525 | fraction | 41.01 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-pro].model.hle` |
| DeepSeek V4 Pro (max) | SciCode | 0.510416666666667 | fraction | 51.04 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-pro].model.scicode` |
| DeepSeek V4 Pro (max) | CritPt | 0.18 | fraction | 18.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-pro].model.critpt` |
| Grok 4.7 (xhigh) | DeepSWE v1.1 | 72.6 | percent | 72.60 | Grok Build - Grok 4.7 (xhigh) / Grok Build | `data/aa_deepswe.json` `configurations[valueRankModelId=grok-4.7].scorePct` |
| Grok 4.7 (xhigh) | Bug Hunt Bench | 29.0 | bugs fixed of 105 | 27.62 | Grok 4.7 (xhigh) - mean of 5 | `data/bug_hunt.json` `models[modelId=grok-4.7].fixedOf105` |
| Grok 4.7 (xhigh) | AA FrontierCode 1.1 | 0.338342 | fraction | 33.83 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=grok-4-7].model.frontierCode` |
| Grok 4.7 (xhigh) | Terminal-Bench 4.0 (tbench.ai) | 37.6 | percent | 37.60 | Grok 4.7 (xhigh) / Grok Build | `data/tb4.json` `rows[model=Grok 4.7 (xhigh), agent=Grok Build].resolutionRatePct` |
| Grok 4.7 (xhigh) | GDPval-AA v2.1 | 1711.07 | Elo | 60.55 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=grok-4-7].model.gdpval` |
| Grok 4.7 (xhigh) | AutomationBench-AA | 0.6555835148969458 | fraction | 65.56 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=grok-4-7].model.automationBenchPartialScore` |
| Grok 4.7 (xhigh) | AA-Omniscience | 32.03333333333333 | AA Omniscience Index | 66.02 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=grok-4-7].model.omniscience` |
| Grok 4.7 (xhigh) | AA-LCR v1.1 | 0.766666666666667 | fraction | 76.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=grok-4-7].model.lcr` |
| Grok 4.7 (xhigh) | Humanity's Last Exam | 0.431417979610751 | fraction | 43.14 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=grok-4-7].model.hle` |
| Grok 4.7 (xhigh) | SciCode | 0.574074074074074 | fraction | 57.41 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=grok-4-7].model.scicode` |
| Grok 4.7 (xhigh) | CritPt | 0.177142857142857 | fraction | 17.71 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=grok-4-7].model.critpt` |
| GLM-5.3 (max) | DeepSWE v1.1 | 61.4 | percent | 61.40 | Opencode - GLM-5.3 ({'reasoning_effort': 'max'}) / Opencode | `data/aa_deepswe.json` `configurations[valueRankModelId=glm-5.3].scorePct` |
| GLM-5.3 (max) | Bug Hunt Bench | 19.0 | bugs fixed of 105 | 18.10 | GLM-5.3 (max effort, Z.ai API) | `data/bug_hunt.json` `models[modelId=glm-5.3].fixedOf105` |
| GLM-5.3 (max) | AA FrontierCode 1.1 | 0.400752 | fraction | 40.08 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=glm-5-3].model.frontierCode` |
| GLM-5.3 (max) | Terminal-Bench 4.0 (tbench.ai) | 41.8 | percent | 41.80 | GLM-5.3 (max) / Claude Code | `data/tb4.json` `rows[model=GLM-5.3 (max), agent=Claude Code].resolutionRatePct` |
| GLM-5.3 (max) | GDPval-AA v2.1 | 1650.31 | Elo | 57.52 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=glm-5-3].model.gdpval` |
| GLM-5.3 (max) | AutomationBench-AA | 0.622028649962642 | fraction | 62.20 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=glm-5-3].model.automationBenchPartialScore` |
| GLM-5.3 (max) | AA-Omniscience | 14.3 | AA Omniscience Index | 57.15 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=glm-5-3].model.omniscience` |
| GLM-5.3 (max) | AA-LCR v1.1 | 0.796666666666667 | fraction | 79.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=glm-5-3].model.lcr` |
| GLM-5.3 (max) | Humanity's Last Exam | 0.422613531047266 | fraction | 42.26 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=glm-5-3].model.hle` |
| GLM-5.3 (max) | SciCode | 0.590277777777778 | fraction | 59.03 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=glm-5-3].model.scicode` |
| GLM-5.3 (max) | CritPt | 0.191428571428571 | fraction | 19.14 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=glm-5-3].model.critpt` |
| Gemini 3.8 Flash (high) | DeepSWE v1.1 | 65.8 | percent | 65.80 | Antigravity SDK - Gemini 3.8 Flash (high) / Antigravity SDK | `data/aa_deepswe.json` `configurations[valueRankModelId=gemini-3.8-flash].scorePct` |
| Gemini 3.8 Flash (high) | Bug Hunt Bench | 18.0 | bugs fixed of 105 | 17.14 | Gemini 3.8 Flash - mean of 3 | `data/bug_hunt.json` `models[modelId=gemini-3.8-flash].fixedOf105` |
| Gemini 3.8 Flash (high) | AA FrontierCode 1.1 | 0.363585 | fraction | 36.36 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-3-8-flash].model.frontierCode` |
| Gemini 3.8 Flash (high) | Terminal-Bench 4.0 (tbench.ai) | 19.1 | percent | 19.10 | Gemini 3.8 Flash (high) / mini-SWE-agent | `data/tb4.json` `rows[model=Gemini 3.8 Flash (high), agent=mini-SWE-agent].resolutionRatePct` |
| Gemini 3.8 Flash (high) | GDPval-AA v2.1 | 1436.3 | Elo | 46.81 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-3-8-flash].model.gdpval` |
| Gemini 3.8 Flash (high) | AutomationBench-AA | 0.5993009432118243 | fraction | 59.93 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-3-8-flash].model.automationBenchPartialScore` |
| Gemini 3.8 Flash (high) | AA-Omniscience | 29.55 | AA Omniscience Index | 64.78 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-3-8-flash].model.omniscience` |
| Gemini 3.8 Flash (high) | AA-LCR v1.1 | 0.813333333333333 | fraction | 81.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-3-8-flash].model.lcr` |
| Gemini 3.8 Flash (high) | Humanity's Last Exam | 0.478220574606117 | fraction | 47.82 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-3-8-flash].model.hle` |
| Gemini 3.8 Flash (high) | SciCode | 0.565972222222222 | fraction | 56.60 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-3-8-flash].model.scicode` |
| Gemini 3.8 Flash (high) | CritPt | 0.182857142857143 | fraction | 18.29 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-3-8-flash].model.critpt` |
| Qwen3.8 Max | DeepSWE v1.1 | 51.0 | percent | 51.00 | Claude Code - Qwen3.8 Max / Claude Code | `data/aa_deepswe.json` `configurations[valueRankModelId=qwen3.8-max].scorePct` |
| Qwen3.8 Max | Bug Hunt Bench | 25.7 | bugs fixed of 105 | 24.48 | Qwen3.8-Max (max effort, Alibaba API) - mean of 3 | `data/bug_hunt.json` `models[modelId=qwen3.8-max].fixedOf105` |
| Qwen3.8 Max | AA FrontierCode 1.1 | 0.431563 | fraction | 43.16 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=qwen3-8-max].model.frontierCode` |
| Qwen3.8 Max | Terminal-Bench 4.0 (tbench.ai) | 27.0 | percent | 27.00 | Qwen3.8-Max-0902 (max) / Claude Code | `data/tb4.json` `rows[model=Qwen3.8-Max-0902 (max), agent=Claude Code].resolutionRatePct` |
| Qwen3.8 Max | GDPval-AA v2.1 | 1665.58 | Elo | 58.28 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=qwen3-8-max].model.gdpval` |
| Qwen3.8 Max | AutomationBench-AA | 0.561905381087678 | fraction | 56.19 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=qwen3-8-max].model.automationBenchPartialScore` |
| Qwen3.8 Max | AA-Omniscience | 11.983333333333333 | AA Omniscience Index | 55.99 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=qwen3-8-max].model.omniscience` |
| Qwen3.8 Max | AA-LCR v1.1 | 0.803333333333333 | fraction | 80.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=qwen3-8-max].model.lcr` |
| Qwen3.8 Max | Humanity's Last Exam | 0.430954587581094 | fraction | 43.10 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=qwen3-8-max].model.hle` |
| Qwen3.8 Max | SciCode | 0.520833333333333 | fraction | 52.08 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=qwen3-8-max].model.scicode` |
| Qwen3.8 Max | CritPt | 0.177142857142857 | fraction | 17.71 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=qwen3-8-max].model.critpt` |
| Muse Wonder Full (max) | DeepSWE v1.1 | 77.0 | percent | 77.00 | Muse Code - Muse Wonder Full (max) / Muse Code | `data/aa_deepswe.json` `configurations[valueRankModelId=muse-wonder-full].scorePct` |
| Muse Wonder Full (max) | Bug Hunt Bench | 42.0 | bugs fixed of 105 | 40.00 | Muse Wonder Full 1.0 (max effort, Muse Code, Meta API) - mean of 2 | `data/bug_hunt.json` `models[modelId=muse-wonder-full].fixedOf105` |
| Muse Wonder Full (max) | GDPval-AA v2.1 | 1857.09 | Elo | 67.85 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-wonder-full].model.gdpval` |
| Muse Wonder Full (max) | AutomationBench-AA | 0.7133074973223975 | fraction | 71.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-wonder-full].model.automationBenchPartialScore` |
| Muse Wonder Full (max) | AA-Omniscience | 30.15 | AA Omniscience Index | 65.08 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-wonder-full].model.omniscience` |
| Muse Wonder Full (max) | AA-LCR v1.1 | 0.836666666666667 | fraction | 83.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-wonder-full].model.lcr` |
| Muse Wonder Full (max) | Humanity's Last Exam | 0.536144578313253 | fraction | 53.61 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-wonder-full].model.hle` |
| Muse Wonder Full (max) | SciCode | 0.626157407407407 | fraction | 62.62 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-wonder-full].model.scicode` |
| Muse Wonder Full (max) | CritPt | 0.328571428571429 | fraction | 32.86 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=muse-wonder-full].model.critpt` |

## Basket cost components

| Configuration | Component | Cost (USD) | Completeness | Tasks | USD per task | Source |
|---|---|---:|---|---:|---:|---|
| GPT-6.1 Sol (xhigh) | AA-Briefcase | $94.51 | confirmed-complete | 91 | $1.0386 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (xhigh) | GDPval-AA | $122.86 | confirmed-complete | 220 | $0.5585 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (xhigh) | GDP.pdf | $36.81 | confirmed-complete | 100 | $0.3681 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (xhigh) | AutomationBench-AA | $164.62 | confirmed-complete | 657 | $0.2506 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (xhigh) | Terminal-Bench 4.0 (AA Index run) | $67.71 | confirmed-complete | 66 | $1.0259 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (xhigh) | SciCode | $6.35 | confirmed-complete | 288 | $0.0220 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (xhigh) | AA-LCR | $19.35 | confirmed-complete | 100 | $0.1935 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (xhigh) | Coding Agent Index | $315.03 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| GPT-6.1 Sol (high) | AA-Briefcase | $76.16 | confirmed-complete | 91 | $0.8369 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (high) | GDPval-AA | $94.10 | confirmed-complete | 220 | $0.4277 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (high) | GDP.pdf | $34.94 | confirmed-complete | 100 | $0.3494 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (high) | AutomationBench-AA | $148.34 | confirmed-complete | 657 | $0.2258 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (high) | Terminal-Bench 4.0 (AA Index run) | $54.66 | confirmed-complete | 66 | $0.8282 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (high) | SciCode | $3.73 | confirmed-complete | 288 | $0.0130 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (high) | AA-LCR | $19.14 | confirmed-complete | 100 | $0.1914 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (high) | Coding Agent Index | $269.44 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| GPT-6.1 Sol (medium) | AA-Briefcase | $42.26 | confirmed-complete | 91 | $0.4644 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (medium) | GDPval-AA | $50.86 | confirmed-complete | 220 | $0.2312 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (medium) | GDP.pdf | $33.75 | confirmed-complete | 100 | $0.3375 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (medium) | AutomationBench-AA | $128.97 | confirmed-complete | 657 | $0.1963 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (medium) | Terminal-Bench 4.0 (AA Index run) | $40.51 | confirmed-complete | 66 | $0.6138 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (medium) | SciCode | $2.68 | confirmed-complete | 288 | $0.0093 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (medium) | AA-LCR | $19.02 | confirmed-complete | 100 | $0.1902 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (medium) | Coding Agent Index | $213.52 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| Claude Sonnet 5.5 (max) | AA-Briefcase | $1,863.13 | confirmed-complete | 91 | $20.4739 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | GDPval-AA | $1,504.30 | confirmed-complete | 220 | $6.8377 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | GDP.pdf | $79.43 | confirmed-complete | 100 | $0.7943 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | AutomationBench-AA | $678.32 | confirmed-complete | 657 | $1.0324 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | Terminal-Bench 4.0 (AA Index run) | $834.67 | confirmed-complete | 66 | $12.6464 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | SciCode | $80.07 | confirmed-complete | 288 | $0.2780 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | AA-LCR | $33.93 | confirmed-complete | 100 | $0.3393 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | Coding Agent Index | $4,299.81 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| Claude Sonnet 5.5 (max) | FrontierCode | $826.00 | confirmed-complete | — | — | AA FrontierCode total cost chart (labels rounded to USD 1) |
| Claude Opus 5.5 (max) | AA-Briefcase | $1,915.18 | confirmed-complete | 91 | $21.0460 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | GDPval-AA | $1,962.05 | confirmed-complete | 220 | $8.9184 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | GDP.pdf | $155.23 | confirmed-complete | 100 | $1.5523 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | AutomationBench-AA | $938.69 | confirmed-complete | 657 | $1.4288 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | Terminal-Bench 4.0 (AA Index run) | $865.21 | confirmed-complete | 66 | $13.1093 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | SciCode | $135.11 | confirmed-complete | 288 | $0.4691 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | AA-LCR | $67.66 | confirmed-complete | 100 | $0.6766 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | Coding Agent Index | $3,950.02 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| Claude Opus 5.5 (max) | FrontierCode | $1,015.00 | confirmed-complete | — | — | AA FrontierCode total cost chart (labels rounded to USD 1) |
| Claude Opus 5.5 (max) | ITBench-AA | $146.00 | confirmed-complete | — | — | AA ITBench-AA total cost chart (labels rounded to USD 1) |
| Claude Sonnet 5.5 (xhigh) | AA-Briefcase | $634.80 | confirmed-complete | 91 | $6.9758 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (xhigh) | GDPval-AA | $430.06 | confirmed-complete | 220 | $1.9548 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (xhigh) | GDP.pdf | $46.01 | confirmed-complete | 100 | $0.4601 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (xhigh) | AutomationBench-AA | $277.51 | confirmed-complete | 657 | $0.4224 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (xhigh) | Terminal-Bench 4.0 (AA Index run) | $401.18 | confirmed-complete | 66 | $6.0784 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (xhigh) | SciCode | $6.81 | confirmed-complete | 288 | $0.0237 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (xhigh) | AA-LCR | $29.66 | confirmed-complete | 100 | $0.2966 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (xhigh) | Coding Agent Index | $1,010.02 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| Claude Sonnet 5.5 (xhigh) | FrontierCode | $120.00 | confirmed-complete | — | — | AA FrontierCode total cost chart (labels rounded to USD 1) |
| Claude Sonnet 5.5 (high) | AA-Briefcase | $297.64 | confirmed-complete | 91 | $3.2707 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (high) | GDPval-AA | $151.47 | confirmed-complete | 220 | $0.6885 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (high) | GDP.pdf | $40.86 | confirmed-complete | 100 | $0.4086 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (high) | AutomationBench-AA | $205.39 | confirmed-complete | 657 | $0.3126 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (high) | Terminal-Bench 4.0 (AA Index run) | $144.29 | confirmed-complete | 66 | $2.1862 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (high) | SciCode | $4.61 | confirmed-complete | 288 | $0.0160 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (high) | AA-LCR | $29.39 | confirmed-complete | 100 | $0.2939 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (high) | Coding Agent Index | $374.36 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| GPT-6.1 Sol (max) | AA-Briefcase | $210.45 | confirmed-complete | 91 | $2.3126 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | GDPval-AA | $196.57 | confirmed-complete | 220 | $0.8935 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | GDP.pdf | $41.99 | confirmed-complete | 100 | $0.4199 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | AutomationBench-AA | $195.01 | confirmed-complete | 657 | $0.2968 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | Terminal-Bench 4.0 (AA Index run) | $120.30 | confirmed-complete | 66 | $1.8228 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | SciCode | $12.50 | confirmed-complete | 288 | $0.0434 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | AA-LCR | $19.94 | confirmed-complete | 100 | $0.1994 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | Coding Agent Index | $470.90 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| GPT-6.1 Sol (max) | FrontierCode | $81.00 | confirmed-complete | — | — | AA FrontierCode total cost chart (labels rounded to USD 1) |
| GPT-6.1 Sol (low) | AA-Briefcase | $16.12 | confirmed-complete | 91 | $0.1771 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (low) | GDPval-AA | $23.10 | confirmed-complete | 220 | $0.1050 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (low) | GDP.pdf | $33.41 | confirmed-complete | 100 | $0.3341 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (low) | AutomationBench-AA | $104.75 | confirmed-complete | 657 | $0.1594 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (low) | Terminal-Bench 4.0 (AA Index run) | $25.27 | confirmed-complete | 66 | $0.3829 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (low) | SciCode | $2.43 | confirmed-complete | 288 | $0.0084 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (low) | AA-LCR | $18.99 | confirmed-complete | 100 | $0.1899 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (low) | Coding Agent Index | $151.14 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| Claude Sonnet 5.5 (medium) | AA-Briefcase | $126.68 | confirmed-complete | 91 | $1.3921 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (medium) | GDPval-AA | $69.91 | confirmed-complete | 220 | $0.3178 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (medium) | GDP.pdf | $38.14 | confirmed-complete | 100 | $0.3814 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (medium) | AutomationBench-AA | $172.20 | confirmed-complete | 657 | $0.2621 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (medium) | Terminal-Bench 4.0 (AA Index run) | $104.16 | confirmed-complete | 66 | $1.5782 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (medium) | SciCode | $3.90 | confirmed-complete | 288 | $0.0135 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (medium) | AA-LCR | $29.16 | confirmed-complete | 100 | $0.2916 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (medium) | Coding Agent Index | $187.48 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| Claude Opus 5 (max) | AA-Briefcase | $1,619.19 | confirmed-complete | 91 | $17.7933 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5 (max) | GDPval-AA | $1,488.52 | confirmed-complete | 220 | $6.7660 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5 (max) | GDP.pdf | $108.57 | confirmed-complete | 100 | $1.0857 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5 (max) | AutomationBench-AA | $864.64 | confirmed-complete | 657 | $1.3160 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5 (max) | Terminal-Bench 4.0 (AA Index run) | $1,273.08 | confirmed-complete | 66 | $19.2891 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5 (max) | SciCode | $33.90 | confirmed-complete | 288 | $0.1177 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5 (max) | AA-LCR | $76.11 | confirmed-complete | 100 | $0.7611 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5 (max) | Coding Agent Index | $3,269.11 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| GPT-6 Sol (max) | AA-Briefcase | $238.81 | confirmed-complete | 91 | $2.6243 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Sol (max) | GDPval-AA | $280.84 | confirmed-complete | 220 | $1.2765 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Sol (max) | GDP.pdf | $42.54 | confirmed-complete | 100 | $0.4254 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Sol (max) | AutomationBench-AA | $235.06 | confirmed-complete | 657 | $0.3578 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Sol (max) | Terminal-Bench 4.0 (AA Index run) | $264.22 | confirmed-complete | 66 | $4.0034 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Sol (max) | SciCode | $12.24 | confirmed-complete | 288 | $0.0425 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Sol (max) | AA-LCR | $19.82 | confirmed-complete | 100 | $0.1982 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Sol (max) | Coding Agent Index | $905.89 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| GPT-6 Sol (max) | ITBench-AA | $38.00 | confirmed-complete | — | — | AA ITBench-AA total cost chart (labels rounded to USD 1) |
| Claude Haiku 5.5 (xhigh) | AA-Briefcase | $33.29 | confirmed-complete | 91 | $0.3658 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (xhigh) | GDPval-AA | $20.26 | confirmed-complete | 220 | $0.0921 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (xhigh) | GDP.pdf | $2.73 | confirmed-complete | 100 | $0.0273 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (xhigh) | AutomationBench-AA | $18.14 | confirmed-complete | 657 | $0.0276 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (xhigh) | Terminal-Bench 4.0 (AA Index run) | $30.38 | confirmed-complete | 66 | $0.4603 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (xhigh) | SciCode | $0.77 | confirmed-complete | 288 | $0.0027 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (xhigh) | AA-LCR | $1.53 | confirmed-complete | 100 | $0.0153 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (xhigh) | Coding Agent Index | $184.98 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| Claude Haiku 5.5 (xhigh) | FrontierCode | $16.00 | confirmed-incomplete | — | — | AA FrontierCode total cost chart (labels rounded to USD 1) |
| Claude Sonnet 5.5 (low) | AA-Briefcase | $73.03 | confirmed-complete | 91 | $0.8025 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (low) | GDPval-AA | $45.90 | confirmed-complete | 220 | $0.2086 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (low) | GDP.pdf | $37.23 | confirmed-complete | 100 | $0.3723 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (low) | AutomationBench-AA | $158.19 | confirmed-complete | 657 | $0.2408 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (low) | Terminal-Bench 4.0 (AA Index run) | $84.80 | confirmed-complete | 66 | $1.2848 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (low) | SciCode | $3.73 | confirmed-complete | 288 | $0.0129 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (low) | AA-LCR | $29.14 | confirmed-complete | 100 | $0.2914 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (low) | Coding Agent Index | $146.38 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| GPT-5.6 Sol (max) | AA-Briefcase | $365.84 | confirmed-complete | 91 | $4.0203 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-5.6 Sol (max) | GDPval-AA | $618.22 | confirmed-complete | 220 | $2.8101 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-5.6 Sol (max) | GDP.pdf | $92.85 | confirmed-complete | 100 | $0.9285 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-5.6 Sol (max) | AutomationBench-AA | $638.90 | confirmed-complete | 657 | $0.9725 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-5.6 Sol (max) | Terminal-Bench 4.0 (AA Index run) | $534.15 | confirmed-complete | 66 | $8.0932 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-5.6 Sol (max) | SciCode | $22.95 | confirmed-complete | 288 | $0.0797 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-5.6 Sol (max) | AA-LCR | $40.16 | confirmed-complete | 100 | $0.4016 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-5.6 Sol (max) | Coding Agent Index | $1,925.06 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| GPT-5.6 Sol (max) | ITBench-AA | $106.00 | confirmed-complete | — | — | AA ITBench-AA total cost chart (labels rounded to USD 1) |
| GPT-6 Luna (max) | AA-Briefcase | $15.47 | confirmed-complete | 91 | $0.1700 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | GDPval-AA | $19.66 | confirmed-complete | 220 | $0.0894 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | GDP.pdf | $2.85 | confirmed-complete | 100 | $0.0285 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | AutomationBench-AA | $23.91 | confirmed-complete | 657 | $0.0364 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | Terminal-Bench 4.0 (AA Index run) | $15.59 | confirmed-complete | 66 | $0.2362 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | SciCode | $1.06 | confirmed-complete | 288 | $0.0037 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | AA-LCR | $1.02 | confirmed-complete | 100 | $0.0102 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | Coding Agent Index | $53.30 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| GPT-6 Luna (max) | FrontierCode | $9.00 | confirmed-complete | — | — | AA FrontierCode total cost chart (labels rounded to USD 1) |
| Claude Haiku 5.5 (high) | AA-Briefcase | $20.29 | confirmed-complete | 91 | $0.2229 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (high) | GDPval-AA | $9.59 | confirmed-complete | 220 | $0.0436 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (high) | GDP.pdf | $2.26 | confirmed-complete | 100 | $0.0226 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (high) | AutomationBench-AA | $14.91 | confirmed-complete | 657 | $0.0227 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (high) | Terminal-Bench 4.0 (AA Index run) | $21.88 | confirmed-complete | 66 | $0.3315 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (high) | SciCode | $0.43 | confirmed-complete | 288 | $0.0015 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (high) | AA-LCR | $1.50 | confirmed-complete | 100 | $0.0150 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (high) | Coding Agent Index | $110.50 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| GPT-6 Astra (max) | AA-Briefcase | $864.69 | confirmed-complete | 91 | $9.5021 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | GDPval-AA | $996.49 | confirmed-complete | 220 | $4.5295 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | GDP.pdf | $207.58 | confirmed-complete | 100 | $2.0758 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | AutomationBench-AA | $1,048.30 | confirmed-complete | 657 | $1.5956 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | Terminal-Bench 4.0 (AA Index run) | $560.88 | confirmed-complete | 66 | $8.4981 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | SciCode | $66.89 | confirmed-complete | 288 | $0.2323 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | AA-LCR | $99.73 | confirmed-complete | 100 | $0.9973 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | Coding Agent Index | $2,262.53 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| GPT-6 Astra (max) | FrontierCode | $422.00 | confirmed-complete | — | — | AA FrontierCode total cost chart (labels rounded to USD 1) |
| GPT-6 Astra (max) | ITBench-AA | $133.00 | confirmed-complete | — | — | AA ITBench-AA total cost chart (labels rounded to USD 1) |
| Claude Haiku 5.5 (medium) | AA-Briefcase | $12.10 | confirmed-complete | 91 | $0.1330 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (medium) | GDPval-AA | $4.56 | confirmed-complete | 220 | $0.0207 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (medium) | GDP.pdf | $2.06 | confirmed-complete | 100 | $0.0206 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (medium) | AutomationBench-AA | $12.57 | confirmed-complete | 657 | $0.0191 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (medium) | Terminal-Bench 4.0 (AA Index run) | $12.79 | confirmed-complete | 66 | $0.1938 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (medium) | SciCode | $0.34 | confirmed-complete | 288 | $0.0012 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (medium) | AA-LCR | $1.49 | confirmed-complete | 100 | $0.0149 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (medium) | Coding Agent Index | $68.60 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| GPT-5.6 Luna (max) | AA-Briefcase | $35.95 | confirmed-complete | 91 | $0.3951 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-5.6 Luna (max) | GDPval-AA | $24.18 | confirmed-complete | 220 | $0.1099 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-5.6 Luna (max) | GDP.pdf | $5.68 | confirmed-complete | 100 | $0.0568 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-5.6 Luna (max) | AutomationBench-AA | $59.91 | confirmed-complete | 657 | $0.0912 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-5.6 Luna (max) | Terminal-Bench 4.0 (AA Index run) | $56.06 | confirmed-complete | 66 | $0.8493 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-5.6 Luna (max) | SciCode | $2.67 | confirmed-complete | 288 | $0.0093 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-5.6 Luna (max) | AA-LCR | $2.09 | confirmed-complete | 100 | $0.0209 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-5.6 Luna (max) | Coding Agent Index | $132.72 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| Gemini 4 Argon (high) | AA-Briefcase | $530.33 | confirmed-complete | 91 | $5.8277 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 4 Argon (high) | GDPval-AA | $400.23 | confirmed-complete | 220 | $1.8192 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 4 Argon (high) | GDP.pdf | $25.93 | confirmed-complete | 100 | $0.2593 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 4 Argon (high) | AutomationBench-AA | $399.89 | confirmed-complete | 657 | $0.6087 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 4 Argon (high) | Terminal-Bench 4.0 (AA Index run) | $447.49 | confirmed-complete | 66 | $6.7801 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 4 Argon (high) | SciCode | $30.44 | confirmed-complete | 288 | $0.1057 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 4 Argon (high) | AA-LCR | $23.64 | confirmed-complete | 100 | $0.2364 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 4 Argon (high) | Coding Agent Index | $1,770.70 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| Gemini 4 Argon (high) | FrontierCode | $670.00 | confirmed-complete | — | — | AA FrontierCode total cost chart (labels rounded to USD 1) |
| Claude Fable 5.1 (max) | AA-Briefcase | $2,066.92 | unresolved | 91 | $22.7135 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Fable 5.1 (max) | GDPval-AA | $2,150.47 | unresolved | 220 | $9.7749 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Fable 5.1 (max) | GDP.pdf | $277.49 | unresolved | 100 | $2.7749 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Fable 5.1 (max) | AutomationBench-AA | $1,715.62 | unresolved | 657 | $2.6113 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Fable 5.1 (max) | Terminal-Bench 4.0 (AA Index run) | $1,268.42 | unresolved | 66 | $19.2185 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Fable 5.1 (max) | SciCode | $189.65 | unresolved | 288 | $0.6585 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Fable 5.1 (max) | AA-LCR | $158.45 | unresolved | 100 | $1.5845 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Fable 5.1 (max) | Coding Agent Index | $3,753.59 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| Claude Fable 5.1 (max) | FrontierCode | $1,200.00 | confirmed-complete | — | — | AA FrontierCode total cost chart (labels rounded to USD 1) |
| Claude Fable 5.1 (max) | ITBench-AA | $237.00 | confirmed-complete | — | — | AA ITBench-AA total cost chart (labels rounded to USD 1) |
| MiMo-V2.6-Flash | AA-Briefcase | $13.81 | confirmed-complete | 91 | $0.1517 | AA Intelligence Index evaluation cost (cost per task x task count) |
| MiMo-V2.6-Flash | GDPval-AA | $16.10 | confirmed-complete | 220 | $0.0732 | AA Intelligence Index evaluation cost (cost per task x task count) |
| MiMo-V2.6-Flash | GDP.pdf | $2.01 | confirmed-complete | 100 | $0.0201 | AA Intelligence Index evaluation cost (cost per task x task count) |
| MiMo-V2.6-Flash | AutomationBench-AA | $10.94 | confirmed-complete | 657 | $0.0167 | AA Intelligence Index evaluation cost (cost per task x task count) |
| MiMo-V2.6-Flash | Terminal-Bench 4.0 (AA Index run) | $15.19 | confirmed-complete | 66 | $0.2302 | AA Intelligence Index evaluation cost (cost per task x task count) |
| MiMo-V2.6-Flash | SciCode | $0.81 | confirmed-complete | 288 | $0.0028 | AA Intelligence Index evaluation cost (cost per task x task count) |
| MiMo-V2.6-Flash | AA-LCR | $1.51 | confirmed-complete | 100 | $0.0151 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (low) | AA-Briefcase | $4.30 | confirmed-complete | 91 | $0.0472 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (low) | GDPval-AA | $2.28 | confirmed-complete | 220 | $0.0104 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (low) | GDP.pdf | $1.93 | confirmed-complete | 100 | $0.0193 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (low) | AutomationBench-AA | $10.04 | confirmed-complete | 657 | $0.0153 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (low) | Terminal-Bench 4.0 (AA Index run) | $7.82 | confirmed-complete | 66 | $0.1186 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (low) | SciCode | $0.27 | confirmed-complete | 288 | $0.0009 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (low) | AA-LCR | $1.48 | confirmed-complete | 100 | $0.0148 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (low) | Coding Agent Index | $43.40 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| Claude Haiku 5.5 (max) | AA-Briefcase | $61.41 | confirmed-complete | 91 | $0.6749 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (max) | GDPval-AA | $48.90 | confirmed-complete | 220 | $0.2223 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (max) | GDP.pdf | $5.27 | confirmed-complete | 100 | $0.0527 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (max) | AutomationBench-AA | $27.80 | confirmed-complete | 657 | $0.0423 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (max) | Terminal-Bench 4.0 (AA Index run) | $43.02 | confirmed-complete | 66 | $0.6519 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (max) | SciCode | $3.15 | confirmed-complete | 288 | $0.0109 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (max) | AA-LCR | $1.93 | confirmed-complete | 100 | $0.0193 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (max) | Coding Agent Index | $781.84 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| Claude Haiku 5.5 (max) | FrontierCode | $33.00 | confirmed-incomplete | — | — | AA FrontierCode total cost chart (labels rounded to USD 1) |
| Muse Wonder (max) | AA-Briefcase | $1,133.00 | confirmed-complete | 91 | $12.4506 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Muse Wonder (max) | GDPval-AA | $1,075.46 | confirmed-complete | 220 | $4.8885 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Muse Wonder (max) | GDP.pdf | $72.26 | confirmed-complete | 100 | $0.7226 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Muse Wonder (max) | AutomationBench-AA | $545.12 | confirmed-complete | 657 | $0.8297 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Muse Wonder (max) | Terminal-Bench 4.0 (AA Index run) | $1,185.90 | confirmed-complete | 66 | $17.9681 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Muse Wonder (max) | SciCode | $38.88 | confirmed-complete | 288 | $0.1350 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Muse Wonder (max) | AA-LCR | $43.70 | confirmed-complete | 100 | $0.4370 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Muse Wonder (max) | Coding Agent Index | $2,439.83 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| MiMo-V2.6-Pro | AA-Briefcase | $34.60 | confirmed-complete | 91 | $0.3802 | AA Intelligence Index evaluation cost (cost per task x task count) |
| MiMo-V2.6-Pro | GDPval-AA | $35.47 | confirmed-complete | 220 | $0.1612 | AA Intelligence Index evaluation cost (cost per task x task count) |
| MiMo-V2.6-Pro | GDP.pdf | $2.40 | confirmed-complete | 100 | $0.0240 | AA Intelligence Index evaluation cost (cost per task x task count) |
| MiMo-V2.6-Pro | AutomationBench-AA | $27.77 | confirmed-complete | 657 | $0.0423 | AA Intelligence Index evaluation cost (cost per task x task count) |
| MiMo-V2.6-Pro | Terminal-Bench 4.0 (AA Index run) | $28.91 | confirmed-complete | 66 | $0.4381 | AA Intelligence Index evaluation cost (cost per task x task count) |
| MiMo-V2.6-Pro | SciCode | $2.25 | confirmed-complete | 288 | $0.0078 | AA Intelligence Index evaluation cost (cost per task x task count) |
| MiMo-V2.6-Pro | AA-LCR | $4.74 | confirmed-complete | 100 | $0.0474 | AA Intelligence Index evaluation cost (cost per task x task count) |
| MiMo-V2.6-Pro | FrontierCode | $18.00 | confirmed-complete | — | — | AA FrontierCode total cost chart (labels rounded to USD 1) |
| Muse Spark 1.3 (max) | AA-Briefcase | $369.37 | confirmed-complete | 91 | $4.0590 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Muse Spark 1.3 (max) | GDPval-AA | $448.59 | confirmed-complete | 220 | $2.0390 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Muse Spark 1.3 (max) | GDP.pdf | $20.51 | confirmed-complete | 100 | $0.2051 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Muse Spark 1.3 (max) | AutomationBench-AA | $238.77 | confirmed-complete | 657 | $0.3634 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Muse Spark 1.3 (max) | Terminal-Bench 4.0 (AA Index run) | $457.96 | confirmed-complete | 66 | $6.9388 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Muse Spark 1.3 (max) | SciCode | $11.31 | confirmed-complete | 288 | $0.0393 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Muse Spark 1.3 (max) | AA-LCR | $13.29 | confirmed-complete | 100 | $0.1329 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Muse Spark 1.3 (max) | Coding Agent Index | $1,205.18 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| Grok 4.6 (xhigh) | AA-Briefcase | $444.04 | confirmed-complete | 91 | $4.8795 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Grok 4.6 (xhigh) | GDPval-AA | $536.69 | confirmed-complete | 220 | $2.4395 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Grok 4.6 (xhigh) | GDP.pdf | $26.17 | confirmed-complete | 100 | $0.2617 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Grok 4.6 (xhigh) | AutomationBench-AA | $430.84 | confirmed-complete | 657 | $0.6558 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Grok 4.6 (xhigh) | Terminal-Bench 4.0 (AA Index run) | $435.30 | confirmed-complete | 66 | $6.5955 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Grok 4.6 (xhigh) | SciCode | $8.52 | confirmed-complete | 288 | $0.0296 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Grok 4.6 (xhigh) | AA-LCR | $20.36 | confirmed-complete | 100 | $0.2036 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Grok 4.6 (xhigh) | Coding Agent Index | $1,081.75 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| DeepSeek V4 Flash (max) | AA-Briefcase | $38.53 | confirmed-complete | 91 | $0.4234 | AA Intelligence Index evaluation cost (cost per task x task count) |
| DeepSeek V4 Flash (max) | GDPval-AA | $63.77 | confirmed-complete | 220 | $0.2899 | AA Intelligence Index evaluation cost (cost per task x task count) |
| DeepSeek V4 Flash (max) | GDP.pdf | $4.66 | confirmed-complete | 100 | $0.0466 | AA Intelligence Index evaluation cost (cost per task x task count) |
| DeepSeek V4 Flash (max) | AutomationBench-AA | $69.22 | confirmed-complete | 657 | $0.1054 | AA Intelligence Index evaluation cost (cost per task x task count) |
| DeepSeek V4 Flash (max) | Terminal-Bench 4.0 (AA Index run) | $60.65 | confirmed-complete | 66 | $0.9189 | AA Intelligence Index evaluation cost (cost per task x task count) |
| DeepSeek V4 Flash (max) | SciCode | $12.16 | confirmed-complete | 288 | $0.0422 | AA Intelligence Index evaluation cost (cost per task x task count) |
| DeepSeek V4 Flash (max) | AA-LCR | $4.76 | confirmed-complete | 100 | $0.0476 | AA Intelligence Index evaluation cost (cost per task x task count) |
| DeepSeek V4 Flash (max) | Coding Agent Index | $25.77 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| Muse Spark 1.3 (xhigh) | AA-Briefcase | $311.27 | confirmed-complete | 91 | $3.4206 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Muse Spark 1.3 (xhigh) | GDPval-AA | $307.10 | confirmed-complete | 220 | $1.3959 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Muse Spark 1.3 (xhigh) | GDP.pdf | $19.64 | confirmed-complete | 100 | $0.1964 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Muse Spark 1.3 (xhigh) | AutomationBench-AA | $242.26 | confirmed-complete | 657 | $0.3687 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Muse Spark 1.3 (xhigh) | Terminal-Bench 4.0 (AA Index run) | $411.31 | confirmed-complete | 66 | $6.2319 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Muse Spark 1.3 (xhigh) | SciCode | $10.70 | confirmed-complete | 288 | $0.0372 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Muse Spark 1.3 (xhigh) | AA-LCR | $13.15 | confirmed-complete | 100 | $0.1315 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Muse Spark 1.3 (xhigh) | Coding Agent Index | $1,050.73 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| DeepSeek V4 Pro (max) | AA-Briefcase | $90.59 | confirmed-complete | 91 | $0.9955 | AA Intelligence Index evaluation cost (cost per task x task count) |
| DeepSeek V4 Pro (max) | GDPval-AA | $127.70 | confirmed-complete | 220 | $0.5805 | AA Intelligence Index evaluation cost (cost per task x task count) |
| DeepSeek V4 Pro (max) | GDP.pdf | $11.00 | confirmed-complete | 100 | $0.1100 | AA Intelligence Index evaluation cost (cost per task x task count) |
| DeepSeek V4 Pro (max) | AutomationBench-AA | $223.87 | confirmed-complete | 657 | $0.3408 | AA Intelligence Index evaluation cost (cost per task x task count) |
| DeepSeek V4 Pro (max) | Terminal-Bench 4.0 (AA Index run) | $247.85 | confirmed-complete | 66 | $3.7552 | AA Intelligence Index evaluation cost (cost per task x task count) |
| DeepSeek V4 Pro (max) | SciCode | $14.47 | confirmed-complete | 288 | $0.0503 | AA Intelligence Index evaluation cost (cost per task x task count) |
| DeepSeek V4 Pro (max) | AA-LCR | $13.89 | confirmed-complete | 100 | $0.1389 | AA Intelligence Index evaluation cost (cost per task x task count) |
| DeepSeek V4 Pro (max) | Coding Agent Index | $72.13 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| Grok 4.7 (xhigh) | AA-Briefcase | $846.62 | confirmed-complete | 91 | $9.3035 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Grok 4.7 (xhigh) | GDPval-AA | $1,415.17 | confirmed-complete | 220 | $6.4326 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Grok 4.7 (xhigh) | GDP.pdf | $32.43 | confirmed-complete | 100 | $0.3243 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Grok 4.7 (xhigh) | AutomationBench-AA | $707.44 | confirmed-complete | 657 | $1.0768 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Grok 4.7 (xhigh) | Terminal-Bench 4.0 (AA Index run) | $963.85 | confirmed-complete | 66 | $14.6038 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Grok 4.7 (xhigh) | SciCode | $38.30 | confirmed-complete | 288 | $0.1330 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Grok 4.7 (xhigh) | AA-LCR | $24.51 | confirmed-complete | 100 | $0.2451 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Grok 4.7 (xhigh) | Coding Agent Index | $2,671.69 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| Grok 4.7 (xhigh) | FrontierCode | $1,131.00 | confirmed-complete | — | — | AA FrontierCode total cost chart (labels rounded to USD 1) |
| Grok 4.7 (xhigh) | ITBench-AA | $203.00 | confirmed-complete | — | — | AA ITBench-AA total cost chart (labels rounded to USD 1) |
| GLM-5.3 (max) | AA-Briefcase | $514.04 | confirmed-complete | 91 | $5.6488 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GLM-5.3 (max) | GDPval-AA | $496.54 | confirmed-complete | 220 | $2.2570 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GLM-5.3 (max) | GDP.pdf | $17.34 | confirmed-complete | 100 | $0.1734 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GLM-5.3 (max) | AutomationBench-AA | $302.51 | confirmed-complete | 657 | $0.4604 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GLM-5.3 (max) | Terminal-Bench 4.0 (AA Index run) | $532.24 | confirmed-complete | 66 | $8.0642 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GLM-5.3 (max) | SciCode | $23.62 | confirmed-complete | 288 | $0.0820 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GLM-5.3 (max) | AA-LCR | $14.86 | confirmed-complete | 100 | $0.1486 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GLM-5.3 (max) | Coding Agent Index | $1,285.14 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| GLM-5.3 (max) | FrontierCode | $432.00 | confirmed-complete | — | — | AA FrontierCode total cost chart (labels rounded to USD 1) |
| GLM-5.3 (max) | ITBench-AA | $91.00 | confirmed-complete | — | — | AA ITBench-AA total cost chart (labels rounded to USD 1) |
| Gemini 3.8 Flash (high) | AA-Briefcase | $245.87 | confirmed-complete | 91 | $2.7019 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 3.8 Flash (high) | GDPval-AA | $372.82 | confirmed-complete | 220 | $1.6946 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 3.8 Flash (high) | GDP.pdf | $10.90 | confirmed-complete | 100 | $0.1090 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 3.8 Flash (high) | AutomationBench-AA | $278.70 | confirmed-complete | 657 | $0.4242 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 3.8 Flash (high) | Terminal-Bench 4.0 (AA Index run) | $385.54 | confirmed-complete | 66 | $5.8415 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 3.8 Flash (high) | SciCode | $22.12 | confirmed-complete | 288 | $0.0768 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 3.8 Flash (high) | AA-LCR | $9.88 | confirmed-complete | 100 | $0.0988 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 3.8 Flash (high) | Coding Agent Index | $747.62 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| Gemini 3.8 Flash (high) | FrontierCode | $372.00 | confirmed-complete | — | — | AA FrontierCode total cost chart (labels rounded to USD 1) |
| Gemini 3.8 Flash (high) | ITBench-AA | $86.00 | confirmed-complete | — | — | AA ITBench-AA total cost chart (labels rounded to USD 1) |
| Qwen3.8 Max | AA-Briefcase | $1,781.49 | confirmed-complete | 91 | $19.5769 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Qwen3.8 Max | GDPval-AA | $998.39 | confirmed-complete | 220 | $4.5381 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Qwen3.8 Max | GDP.pdf | $33.31 | confirmed-complete | 100 | $0.3331 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Qwen3.8 Max | AutomationBench-AA | $261.64 | confirmed-complete | 657 | $0.3982 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Qwen3.8 Max | Terminal-Bench 4.0 (AA Index run) | $1,232.62 | confirmed-complete | 66 | $18.6761 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Qwen3.8 Max | SciCode | $32.57 | confirmed-complete | 288 | $0.1131 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Qwen3.8 Max | AA-LCR | $22.88 | confirmed-complete | 100 | $0.2288 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Qwen3.8 Max | Coding Agent Index | $1,054.13 | confirmed-complete | — | — | AA Coding Agent Index cost to run (mean API cost per task) x 303 tasks |
| Qwen3.8 Max | FrontierCode | $675.00 | confirmed-complete | — | — | AA FrontierCode total cost chart (labels rounded to USD 1) |
| Qwen3.8 Max | ITBench-AA | $327.00 | confirmed-complete | — | — | AA ITBench-AA total cost chart (labels rounded to USD 1) |

### AA Index total reconciliation

The seven Index components plus AA's residual reproduce AA's published Intelligence Index total cost.

| Configuration | Index SDLC components | Residual | Reconstructed total | Published total | Reconciled |
|---|---:|---:|---:|---:|---|
| GPT-6.1 Sol (xhigh) | $512.20 | $150.08 | $662.28 | $662.28 | yes |
| GPT-6.1 Sol (high) | $431.07 | $90.24 | $521.32 | $521.32 | yes |
| GPT-6.1 Sol (medium) | $318.05 | $43.32 | $361.37 | $361.37 | yes |
| Claude Sonnet 5.5 (max) | $5,073.84 | $2,185.66 | $7,259.50 | $7,259.50 | yes |
| Claude Opus 5.5 (max) | $6,039.13 | $2,669.07 | $8,708.20 | $8,708.20 | yes |
| Claude Sonnet 5.5 (xhigh) | $1,826.03 | $350.78 | $2,176.82 | $2,176.82 | yes |
| Claude Sonnet 5.5 (high) | $873.64 | $153.76 | $1,027.40 | $1,027.40 | yes |
| GPT-6.1 Sol (max) | $796.76 | $284.79 | $1,081.55 | $1,081.55 | yes |
| GPT-6.1 Sol (low) | $224.07 | $26.40 | $250.48 | $250.48 | yes |
| Claude Sonnet 5.5 (medium) | $544.15 | $78.13 | $622.28 | $622.28 | yes |
| Claude Opus 5 (max) | $5,464.01 | $1,810.73 | $7,274.74 | $7,274.74 | yes |
| GPT-6 Sol (max) | $1,093.52 | $442.27 | $1,535.80 | $1,535.80 | yes |
| Claude Haiku 5.5 (xhigh) | $107.10 | $50.48 | $157.58 | $157.58 | yes |
| Claude Sonnet 5.5 (low) | $432.01 | $50.12 | $482.13 | $482.13 | yes |
| GPT-5.6 Sol (max) | $2,313.08 | $1,151.76 | $3,464.84 | $3,464.84 | yes |
| GPT-6 Luna (max) | $79.56 | $42.49 | $122.05 | $122.05 | yes |
| Claude Haiku 5.5 (high) | $70.85 | $23.22 | $94.07 | $94.07 | yes |
| GPT-6 Astra (max) | $3,844.56 | $1,479.54 | $5,324.10 | $5,324.10 | yes |
| Claude Haiku 5.5 (medium) | $45.91 | $10.45 | $56.36 | $56.36 | yes |
| GPT-5.6 Luna (max) | $186.53 | $133.40 | $319.93 | $319.93 | yes |
| Gemini 4 Argon (high) | $1,857.94 | $549.30 | $2,407.24 | $2,407.24 | yes |
| Claude Fable 5.1 (max) | $7,827.03 | $5,432.49 | $13,259.52 | $13,128.86 | no |
| MiMo-V2.6-Flash | $60.37 | $49.18 | $109.55 | $109.55 | yes |
| Claude Haiku 5.5 (low) | $28.12 | $6.19 | $34.31 | $34.31 | yes |
| Claude Haiku 5.5 (max) | $191.49 | $138.76 | $330.25 | $330.25 | yes |
| Muse Wonder (max) | $4,094.33 | $1,638.86 | $5,733.19 | $5,733.19 | yes |
| MiMo-V2.6-Pro | $136.13 | $70.53 | $206.66 | $206.66 | yes |
| Muse Spark 1.3 (max) | $1,559.80 | $440.55 | $2,000.35 | $2,000.35 | yes |
| Grok 4.6 (xhigh) | $1,901.91 | $340.00 | $2,241.91 | $2,241.91 | yes |
| DeepSeek V4 Flash (max) | $253.74 | $220.45 | $474.19 | $474.19 | yes |
| Muse Spark 1.3 (xhigh) | $1,315.43 | $339.83 | $1,655.27 | $1,655.27 | yes |
| DeepSeek V4 Pro (max) | $729.37 | $392.90 | $1,122.27 | $1,122.27 | yes |
| Grok 4.7 (xhigh) | $4,028.33 | $939.03 | $4,967.35 | $4,967.35 | yes |
| GLM-5.3 (max) | $1,901.15 | $602.33 | $2,503.48 | $2,503.48 | yes |
| Gemini 3.8 Flash (high) | $1,325.82 | $296.90 | $1,622.73 | $1,622.73 | yes |
| Qwen3.8 Max | $4,362.91 | $571.88 | $4,934.79 | $4,934.79 | yes |
| Muse Wonder Full (max) | $0.00 | $0.00 | $0.00 | — | no |

## DeepSWE v1.1 AA chart configurations

The AA chart publishes 42 DeepSWE v1.1 configurations across 113 tasks, observed 2026-10-17T19:26:26Z. Each keeps its displayed agent, model and effort; only exact matches enter a score.

| # | Agent | Evaluated model variant | Effort | pass@1 | ValueRank match | Note |
|---:|---|---|---|---:|---|---|
| 1 | Antigravity CLI | Gemini 4 Argon | high | 78.8% | Exact: gemini-4-argon | Exact variant: chart model Gemini 4 Argon (high) matches the roster display name 'Gemini 4 Argon' at effort high. |
| 2 | Muse Code | Muse Wonder Full | max | 77.0% | Exact: muse-wonder-full | Exact variant: chart model Muse Wonder Full (max) matches the roster display name 'Muse Wonder Full' at effort max. |
| 3 | Muse Code | Muse Wonder | max | 75.8% | Exact: muse-wonder | Exact variant: chart model Muse Wonder (max) matches the roster display name 'Muse Wonder' at effort max. |
| 4 | Codex | GPT-6.1 Sol | xhigh | 73.2% | Exact: gpt-6.1-sol-xhigh | Exact variant: chart model GPT-6.1 Sol (xhigh) matches the roster AA short name 'GPT-6.1 Sol' at effort xhigh. |
| 5 | Muse Code | Muse Spark 1.3 | xhigh | 73.2% | Exact: muse-spark-1-3-xhigh | Exact variant: chart model Muse Spark 1.3 (xhigh) matches the roster AA short name 'Muse Spark 1.3' at effort xhigh. |
| 6 | Devin Fusion CLI | Claude Opus 5.5 Max + GPT-6 Luna High | not shown | 72.6% | not in roster | No ValueRank roster model has this chart model name. It is a composite agent configuration. |
| 7 | Grok Build | Grok 4.7 | xhigh | 72.6% | Exact: grok-4.7 | Exact variant: chart model Grok 4.7 (xhigh) matches the roster display name 'Grok 4.7' at effort xhigh. |
| 8 | Codex | GPT-5.6 Sol | max | 72.3% | Exact: gpt-5.6-sol | Exact variant: chart model GPT-5.6 Sol (max) matches the roster display name 'GPT-5.6 Sol' at effort max. |
| 9 | Claude Code | Sonnet 5.5 | max | 72.0% | Exact: claude-sonnet-5-5 | Exact variant: chart model Sonnet 5.5 (max) matches the roster display name 'Claude Sonnet 5.5' at effort max. |
| 10 | Codex | GPT-6.1 Sol | medium | 72.0% | Exact: gpt-6.1-sol-medium | Exact variant: chart model GPT-6.1 Sol (medium) matches the roster AA short name 'GPT-6.1 Sol' at effort medium. |
| 11 | Muse Code | Muse Spark 1.3 | max | 71.7% | Exact: muse-spark-1-3 | Exact variant: chart model Muse Spark 1.3 (max) matches the roster display name 'Muse Spark 1.3' at effort max. |
| 12 | Codex | GPT-6.1 Sol | high | 70.5% | Exact: gpt-6.1-sol-high | Exact variant: chart model GPT-6.1 Sol (high) matches the roster AA short name 'GPT-6.1 Sol' at effort high. |
| 13 | Codex | GPT-6.1 Sol | max | 69.6% | Exact: gpt-6.1-sol | Exact variant: chart model GPT-6.1 Sol (max) matches the roster display name 'GPT-6.1 Sol' at effort max. |
| 14 | Codex | GPT-6 Sol | max | 69.0% | Exact: gpt-6-sol | Exact variant: chart model GPT-6 Sol (max) matches the roster display name 'GPT-6 Sol' at effort max. |
| 15 | Claude Code | Opus 5.5 | max | 68.4% | Exact: claude-opus-5-5 | Exact variant: chart model Opus 5.5 (max) matches the roster display name 'Claude Opus 5.5' at effort max. |
| 16 | Claude Code | Sonnet 5.5 | xhigh | 68.4% | Exact: claude-sonnet-5-5-xhigh | Exact variant: chart model Sonnet 5.5 (xhigh) matches the roster AA short name 'Claude Sonnet 5.5' at effort xhigh. |
| 17 | Kimi Code CLI | Kimi K3 | not shown | 68.4% | effort unconfirmed | The chart row shows no effort; the roster's selected configuration is max, so the variant cannot be confirmed and no result is transferred. |
| 18 | Codex | GPT-6 Astra | max | 67.6% | Exact: gpt-6-astra | Exact variant: chart model GPT-6 Astra (max) matches the roster display name 'GPT-6 Astra' at effort max. |
| 19 | Codex | GPT-6.1 Sol | low | 67.6% | Exact: gpt-6.1-sol-low | Exact variant: chart model GPT-6.1 Sol (low) matches the roster AA short name 'GPT-6.1 Sol' at effort low. |
| 20 | Devin Fusion CLI | GPT-6 Astra XHigh + SWE-2 Medium | not shown | 67.3% | not in roster | No ValueRank roster model has this chart model name. It is a composite agent configuration. |
| 21 | Claude Code | Sonnet 5.5 | high | 66.7% | Exact: claude-sonnet-5-5-high | Exact variant: chart model Sonnet 5.5 (high) matches the roster AA short name 'Claude Sonnet 5.5' at effort high. |
| 22 | Codex | GPT-5.6 Luna | max | 66.4% | Exact: gpt-5.6-luna | Exact variant: chart model GPT-5.6 Luna (max) matches the roster display name 'GPT-5.6 Luna' at effort max. |
| 23 | Antigravity SDK | Gemini 3.8 Flash | high | 65.8% | Exact: gemini-3.8-flash | Exact variant: chart model Gemini 3.8 Flash (high) matches the roster display name 'Gemini 3.8 Flash' at effort high. |
| 24 | Claude Code | Sonnet 5.5 | medium | 65.5% | Exact: claude-sonnet-5-5-medium | Exact variant: chart model Sonnet 5.5 (medium) matches the roster AA short name 'Claude Sonnet 5.5' at effort medium. |
| 25 | Grok Build | Grok 4.6 | xhigh | 64.9% | Exact: grok-4.6-xhigh | Exact variant: chart model Grok 4.6 (xhigh) matches the roster AA short name 'Grok 4.6' at effort xhigh. |
| 26 | Claude Code | Fable 5.1 | max | 64.3% | Exact: claude-fable-5-1 | Exact variant: chart model Fable 5.1 (max) matches the roster display name 'Claude Fable 5.1' at effort max. AA labels this configuration 'with fallback'; the marker is recorded but does not affect matching. |
| 27 | Codex | GPT-6 Luna | max | 63.7% | Exact: gpt-6-luna | Exact variant: chart model GPT-6 Luna (max) matches the roster display name 'GPT-6 Luna' at effort max. |
| 28 | Devin Fusion CLI | Claude Fable 5.1 XHigh + SWE-2 Medium | not shown | 63.1% | not in roster | No ValueRank roster model has this chart model name. It is a composite agent configuration. |
| 29 | Claude Code | Opus 5 | max | 62.5% | Exact: claude-opus-5 | Exact variant: chart model Opus 5 (max) matches the roster display name 'Claude Opus 5' at effort max. |
| 30 | Claude Code | Sonnet 5.5 | low | 61.9% | Exact: claude-sonnet-5-5-low | Exact variant: chart model Sonnet 5.5 (low) matches the roster AA short name 'Claude Sonnet 5.5' at effort low. |
| 31 | Claude Code | Step 5 Preview | not shown | 61.9% | not in roster | No ValueRank roster model has this chart model name. |
| 32 | Opencode | GLM-5.3 | max | 61.4% | Exact: glm-5.3 | Exact variant: chart model GLM-5.3 (max) matches the roster display name 'GLM-5.3' at effort max. |
| 33 | Muse Code | Muse Spark Open | xhigh | 60.2% | not in roster | No ValueRank roster model has this chart model name. |
| 34 | Codex | DeepSeek V4 Pro 0813 | max | 57.2% | Exact: deepseek-v4-pro | Exact variant: chart model DeepSeek V4 Pro 0813 (max) matches the roster AA short name 'DeepSeek V4 Pro 0813' at effort max. |
| 35 | Codex | DeepSeek V4 Flash 0731 | max | 54.3% | Exact: deepseek-v4-flash | Exact variant: chart model DeepSeek V4 Flash 0731 (max) matches the roster AA short name 'DeepSeek V4 Flash 0731' at effort max. |
| 36 | Claude Code | Qwen3.8 Max | not shown | 51.0% | Exact: qwen3.8-max | Exact variant: chart model Qwen3.8 Max (no effort) matches the roster display name 'Qwen3.8 Max' at effort no effort. |
| 37 | Claude Code | Haiku 5.5 | xhigh | 49.0% | Exact: claude-haiku-5-5 | Exact variant: chart model Haiku 5.5 (xhigh) matches the roster display name 'Claude Haiku 5.5' at effort xhigh. |
| 38 | Claude Code | Haiku 5.5 | medium | 47.5% | Exact: claude-haiku-5-5-medium | Exact variant: chart model Haiku 5.5 (medium) matches the roster AA short name 'Claude Haiku 5.5' at effort medium. |
| 39 | Claude Code | Haiku 5.5 | high | 46.3% | Exact: claude-haiku-5-5-high | Exact variant: chart model Haiku 5.5 (high) matches the roster AA short name 'Claude Haiku 5.5' at effort high. |
| 40 | Claude Code | Haiku 5.5 | max | 46.0% | Exact: claude-haiku-5-5-max | Exact variant: chart model Haiku 5.5 (max) matches the roster AA short name 'Claude Haiku 5.5' at effort max. |
| 41 | Claude Code | Haiku 5.5 | low | 45.4% | Exact: claude-haiku-5-5-low | Exact variant: chart model Haiku 5.5 (low) matches the roster AA short name 'Claude Haiku 5.5' at effort low. |
| 42 | Mirror | Beam 1.0 | not shown | 39.8% | not in roster | No ValueRank roster model has this chart model name. |

## Terminal-Bench 4.0 official rows

23 official rows (13 of 49 cohort matches), observed 2026-10-17T19:25:15Z. The published ± is the source's 95% confidence interval (used by stream S1M).

| Rank | Base model | Agent | Resolution rate | Tokens | Cost |
|---|---|---|---:|---|---:|
| 1 | Opus 5.5 | Claude Code | 64.8% ± 3.1% | 8.0B | $4,700 |
| 2 | Sonnet 5.5 | Claude Code | 61.8% ± 2.9% | 19.4B | $7,300 |
| 3 | GPT-6 Astra | Codex | 58.2% ± 2.8% | 1.5B | $3,300 |
| 3 | GPT-6.1 Sol | Codex | 58.2% ± 3.1% | 1.5B | $600 |
| 5 | Fable 5.1 | Claude Code | 57.9% ± 3.8% | 2.7B | $6,200 |
| 6 | Opus 5 | Claude Code | 53.9% ± 3.2% | 6.9B | $6,100 |
| 7 | GPT-6 Sol | Codex | 49.4% ± 3.2% | 5.0B | $1,500 |
| 8 | Fable 5 | Claude Code | 44.5% ± 3.8% | 3.8B | $7,300 |
| 9 | GLM-5.3 | Claude Code | 41.8% ± 3.2% | 8.7B | $2,700 |
| 10 | Grok 4.7 | Grok Build | 37.6% ± 3.5% | 5.5B | $3,700 |
| 11 | GPT-5.6 Sol | Codex | 37.3% ± 3.8% | 4.4B | $2,500 |
| 12 | GLM-5.3-Flash | Claude Code | 35.8% ± 3.5% | 2.9B | $2,900 |
| 13 | Qwen3.8-Max-0902 | Claude Code | 27.0% ± 3.8% | 3.0B | $4,600 |
| 14 | Opus 4.8 | Claude Code | 23.6% ± 3.6% | 6.4B | $6,500 |
| 15 | GPT-5.6 Terra | Codex | 21.5% ± 3.3% | 5.7B | $1,700 |
| 16 | Grok 4.6 | Grok Build | 20.3% ± 3.1% | 4.0B | $3,600 |
| 17 | Gemini 3.8 Flash | mini-SWE-agent | 19.1% ± 3.4% | 17.2B | $1,800 |
| 18 | GPT-5.6 Luna | Codex | 17.3% ± 2.8% | 11.6B | $300 |
| 19 | GPT-6 Luna | Codex | 16.4% ± 2.7% | 3.9B | $100 |
| 20 | Muse Spark 1.3 | Muse Code | 14.5% ± 2.9% | 9.0B | — |
| 21 | Grok 4.5 | Grok Build | 12.4% ± 2.6% | 3.4B | $2,100 |
| 21 | Sonnet 5 | Claude Code | 12.4% ± 3.1% | 21.6B | $9,600 |
| 23 | Gemini 3.7 Flash | mini-SWE-agent | 11.2% ± 2.4% | 11.1B | $1,300 |

## Bug Hunt Bench matched runs

Owner-published runs at commit `aec976170df89a371384174ca87646a9a8c82415`; the score is the owner's largest-sample mean of bugs fixed of 105 for the exact model and effort, with the harness that result was run on (E206). Cross-harness results at the same effort (E224, diagnostic): Gemini 4 Argon: Antigravity CLI 40.7 (3 runs), Gemini CLI 33.0 (1 run).

| Model | Evaluated model | Bugs fixed of 105 | Runs | Effort | Harness |
|---|---|---:|---:|---|---|
| GPT-6 Astra | GPT-6 Astra (max effort) - mean of 3 | 45.0 | 3 | max | Codex CLI |
| Gemini 3.8 Flash | Gemini 3.8 Flash - mean of 3 | 18.0 | 3 | high | Antigravity CLI |
| Claude Opus 5 | Opus 5 (max effort) | 27.0 | 1 | max | Claude Code |
| Claude Opus 5.5 | Opus 5.5 (max effort) - mean of 3 | 41.7 | 3 | max | Claude Code |
| GPT-5.6 Sol | GPT-5.6 Sol (max effort) - mean of 2 | 43.5 | 2 | max | Codex CLI |
| Claude Fable 5 | Fable 5 (max effort) | 29.0 | 1 | max | Claude Code |
| GLM-5.3 | GLM-5.3 (max effort, Z.ai API) | 19.0 | 1 | max | Claude Code / Z.ai API |
| Kimi K3 | Kimi K3 | 21.0 | 1 | default | Claude Code / OpenRouter |
| GPT-5.6 Luna | GPT-5.6 Luna (max effort) - mean of 3 | 31.3 | 3 | max | Codex CLI |
| GLM-5.3 Flash | GLM-5.3 Flash (max effort, Z.ai API) - mean of 3 | 17.7 | 3 | max | Claude Code / Z.ai API |
| DeepSeek V4 Pro | DeepSeek V4-Pro (max effort, DeepSeek API) | 16.0 | 1 | max | Claude Code / DeepSeek API |
| Claude Opus 4.8 | Opus 4.8 (max effort) | 15.0 | 1 | max | Claude Code |
| Qwen3.8 Max | Qwen3.8-Max (max effort, Alibaba API) - mean of 3 | 25.7 | 3 | max | Claude Code / Alibaba API |
| Muse Spark 1.2 | Muse Spark 1.2 (default effort, OpenRouter) | 14.0 | 1 | default | Claude Code / OpenRouter |
| Claude Sonnet 5 | Sonnet 5 (max effort) | 9.0 | 1 | max | Claude Code |
| DeepSeek V4 Flash | DeepSeek V4.1 Flash (max effort) - mean of 3 | 21.7 | 3 | max | Claude Code / DeepSeek API |
| GPT-6 Sol | GPT-6 Sol MAX - mean of 3 | 29.3 | 3 | max | Codex CLI |
| GPT-6.1 Sol | GPT-6.1 Sol (max effort) - mean of 3 | 44.3 | 3 | max | Codex CLI |
| GPT-6 Luna | GPT-6 Luna MAX - mean of 3 | 18.3 | 3 | max | Codex CLI |
| Grok 4.7 | Grok 4.7 (xhigh) - mean of 5 | 29.0 | 5 | xhigh | Grok Build CLI (ACP) |
| MiMo-V2.6-Pro | MiMo-V2.6-Pro (first-party, thinking enabled) | 18.0 | 1 | enabled | Claude Code / Anthropic-compatible shim |
| Claude Haiku 5.5 | Haiku 5.5 (xhigh effort) - mean of 3 | 18.3 | 3 | xhigh | Claude Code |
| Claude Sonnet 5.5 | Sonnet 5.5 (max effort) - mean of 3 | 51.3 | 3 | max | Claude Code |
| Gemini 4 Argon | Gemini 4 Argon (high effort, Antigravity CLI) - mean of 3 | 40.7 | 3 | high | Antigravity CLI |
| Claude Fable 5.1 | Fable 5.1 (max effort) | 43.0 | 1 | max | Claude Code |
| Muse Spark 1.3 | Muse Spark 1.3 (max effort, Muse Code, Meta API) - mean of 5 | 32.2 | 5 | max | Muse Code / Meta API |
| Muse Wonder | Muse Wonder 1.0 (max effort, Muse Code, Meta API) - mean of 3 | 31.7 | 3 | max | Muse Code / Meta API |
| Muse Wonder Full | Muse Wonder Full 1.0 (max effort, Muse Code, Meta API) - mean of 2 | 42.0 | 2 | max | Muse Code / Meta API |
| GPT-6.1 Sol (xhigh) | GPT-6.1 Sol (xhigh effort) - mean of 3 | 42.7 | 3 | xhigh | Codex CLI |
| GPT-6.1 Sol (high) | GPT-6.1 Sol (high effort) - mean of 2 | 36.5 | 2 | high | Codex CLI |
| GPT-6.1 Sol (medium) | GPT-6.1 Sol (medium effort) - mean of 2 | 29.0 | 2 | medium | Codex CLI |
| GPT-6.1 Sol (low) | GPT-6.1 Sol (low effort) - mean of 2 | 22.5 | 2 | low | Codex CLI |
| Claude Haiku 5.5 (max) | Haiku 5.5 (max effort) - mean of 2 | 21.5 | 2 | max | Claude Code |
| Claude Haiku 5.5 (high) | Haiku 5.5 (high effort) - mean of 2 | 16.0 | 2 | high | Claude Code |
| Claude Haiku 5.5 (medium) | Haiku 5.5 (medium effort) | 12.0 | 1 | medium | Claude Code |
| Claude Haiku 5.5 (low) | Haiku 5.5 (low effort) | 11.0 | 1 | low | Claude Code |
| Claude Sonnet 5.5 (xhigh) | Sonnet 5.5 (xhigh effort) - mean of 3 | 36.0 | 3 | xhigh | Claude Code |
| Claude Sonnet 5.5 (high) | Sonnet 5.5 (high effort) - mean of 3 | 34.3 | 3 | high | Claude Code |
| Claude Sonnet 5.5 (medium) | Sonnet 5.5 (medium effort) - mean of 3 | 23.3 | 3 | medium | Claude Code |
| Claude Sonnet 5.5 (low) | Sonnet 5.5 (low effort) - mean of 3 | 19.0 | 3 | low | Claude Code |
| Muse Spark 1.3 (xhigh) | Muse Spark 1.3 (xhigh effort, Muse Code, Meta API) - mean of 3 | 20.3 | 3 | xhigh | Muse Code / Meta API |
| Grok 4.6 (xhigh) | Grok 4.6 (xhigh) seq - mean of 3 | 28.7 | 3 | xhigh | Grok Build CLI (ACP) |

## Plan routes

Route evidence as of 2026-10-08. Full allocation regimes, workloads and notes are in [data/plan_cost_routes.json](data/plan_cost_routes.json).

| Plan | Eligible configurations | Monthly fee | Value Multiple | Evidence | Source model | Source date | Source |
|---|---|---:|---:|---|---|---|---|
| ChatGPT Plus $20 · common GPT assumption | GPT-6 Astra, GPT-5.6 Sol, GPT-5.6 Luna, GPT-5.5, GPT-6 Sol, GPT-6.1 Sol, GPT-6 Luna, GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro $100 · common GPT assumption | GPT-6 Astra, GPT-5.6 Sol, GPT-5.6 Luna, GPT-5.5, GPT-6 Sol, GPT-6.1 Sol, GPT-6 Luna, GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro $200 · common GPT assumption | GPT-6 Astra, GPT-5.6 Sol, GPT-5.6 Luna, GPT-5.5, GPT-6 Sol, GPT-6.1 Sol, GPT-6 Luna, GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro $500 · common GPT assumption | GPT-6 Astra, GPT-5.6 Sol, GPT-5.6 Luna, GPT-5.5, GPT-6 Sol, GPT-6.1 Sol, GPT-6 Luna, GPT-6.1 Sol (xhigh), GPT-6.1 Sol (high), GPT-6.1 Sol (medium), GPT-6.1 Sol (low) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · Opus 5.5 | Claude Opus 5.5 | $20.00 | 58.9× | Controlled account measurement / workload projection | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max $100 · Opus 5.5 | Claude Opus 5.5 | $100.00 | 57.25× | Controlled account measurement / workload projection | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max $200 · Opus 5.5 | Claude Opus 5.5 | $200.00 | 58.63× | Controlled account measurement / workload projection | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max $100 · Fable 5.1 | Claude Fable 5.1 | $100.00 | 12.73× | Controlled account measurement / workload projection | Fable 5.1 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max $200 · Fable 5.1 | Claude Fable 5.1 | $200.00 | 12.425× | Controlled account measurement / workload projection | Fable 5.1 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| SuperGrok Heavy $300 · Grok 4.7 XHigh | Grok 4.7 | $300.00 | 5.785× | user reported projection | Grok 4.7 XHigh | 2026-09-25 | [Source](https://www.remakebench.com/capacity/plans/supergrok-heavy) |
| MiMo · provisional 1.5x assumption | MiMo-V2.6-Pro, MiMo-V2.6-Flash | — | 1.5× | Provisional assumption | — | — | User assumption |
| Claude Pro $20 · common Claude assumption | Claude Opus 5, Claude Fable 5, Claude Opus 4.8, Claude Sonnet 5, Claude Haiku 5.5, Claude Sonnet 5.5, Claude Haiku 5.5 (max), Claude Haiku 5.5 (high), Claude Haiku 5.5 (medium), Claude Haiku 5.5 (low), Claude Sonnet 5.5 (xhigh), Claude Sonnet 5.5 (high), Claude Sonnet 5.5 (medium), Claude Sonnet 5.5 (low) | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Opus 5, Claude Fable 5, Claude Opus 4.8, Claude Sonnet 5, Claude Haiku 5.5, Claude Sonnet 5.5, Claude Haiku 5.5 (max), Claude Haiku 5.5 (high), Claude Haiku 5.5 (medium), Claude Haiku 5.5 (low), Claude Sonnet 5.5 (xhigh), Claude Sonnet 5.5 (high), Claude Sonnet 5.5 (medium), Claude Sonnet 5.5 (low) | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Opus 5, Claude Fable 5, Claude Opus 4.8, Claude Sonnet 5, Claude Haiku 5.5, Claude Sonnet 5.5, Claude Haiku 5.5 (max), Claude Haiku 5.5 (high), Claude Haiku 5.5 (medium), Claude Haiku 5.5 (low), Claude Sonnet 5.5 (xhigh), Claude Sonnet 5.5 (high), Claude Sonnet 5.5 (medium), Claude Sonnet 5.5 (low) | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |

### Plan amounts and their lineage

Each routed row's amount with what it measures, how it was derived and which objects it comes from (E166, E168); API-fallback rows have none.

| Configuration | Amount (USD per fee period) | Measures | Derivation | Workload | Cash object | Measurement object |
|---|---:|---|---|---|---|---|
| GPT-6.1 Sol (xhigh) | $5,386 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | chatgpt-pro500-common-semianalysis-assumption:month cash | chatgpt-pro500-common-semianalysis-assumption |
| Claude Sonnet 5.5 (max) | $1,178 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | claude-pro-common-opus55-assumption:month cash | claude-pro-common-opus55-assumption |
| GPT-6.1 Sol (max) | $5,386 | measured-workload capacity | measurement record: its recorded numerator U_obs = M_obs x F_obs (applied estimate) | the route's measurement workload | chatgpt-pro500-common-semianalysis-assumption:month cash | chatgpt-pro500-common-semianalysis-assumption |
| GPT-6.1 Sol (high) | $5,386 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | chatgpt-pro500-common-semianalysis-assumption:month cash | chatgpt-pro500-common-semianalysis-assumption |
| GPT-6.1 Sol (medium) | $5,386 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | chatgpt-pro500-common-semianalysis-assumption:month cash | chatgpt-pro500-common-semianalysis-assumption |
| Claude Opus 5.5 (max) | $1,178 | measured-workload capacity | measurement record: its recorded numerator U_obs = M_obs x F_obs (workload capacity projection) | the route's measurement workload | claude-pro-opus55-semianalysis:month cash | claude-pro-opus55-semianalysis |
| GPT-6 Astra (max) | $162 | measured-workload capacity | measurement record: its recorded numerator U_obs = M_obs x F_obs (applied estimate) | the route's measurement workload | chatgpt-plus-common-semianalysis-assumption:month cash | chatgpt-plus-common-semianalysis-assumption |
| GPT-5.6 Sol (max) | $5,386 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | chatgpt-pro500-common-semianalysis-assumption:month cash | chatgpt-pro500-common-semianalysis-assumption |
| Claude Sonnet 5.5 (xhigh) | $1,178 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | claude-pro-common-opus55-assumption:month cash | claude-pro-common-opus55-assumption |
| GPT-6 Sol (max) | $5,386 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | chatgpt-pro500-common-semianalysis-assumption:month cash | chatgpt-pro500-common-semianalysis-assumption |
| MiMo-V2.6-Pro | — | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | mimo-provisional-user-assumption:month cash | mimo-provisional-user-assumption |
| Claude Fable 5.1 (max) | $1,273 | measured-workload capacity | measurement record: its recorded numerator U_obs = M_obs x F_obs (workload capacity projection) | the route's measurement workload | claude-max5x-fable51-semianalysis:month cash | claude-max5x-fable51-semianalysis |
| Claude Sonnet 5.5 (high) | $1,178 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | claude-pro-common-opus55-assumption:month cash | claude-pro-common-opus55-assumption |
| GPT-6.1 Sol (low) | $5,386 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | chatgpt-pro500-common-semianalysis-assumption:month cash | chatgpt-pro500-common-semianalysis-assumption |
| GPT-5.6 Luna (max) | $5,386 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | chatgpt-pro500-common-semianalysis-assumption:month cash | chatgpt-pro500-common-semianalysis-assumption |
| GPT-6 Luna (max) | $5,386 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | chatgpt-pro500-common-semianalysis-assumption:month cash | chatgpt-pro500-common-semianalysis-assumption |
| Claude Haiku 5.5 (max) | $1,178 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | claude-pro-common-opus55-assumption:month cash | claude-pro-common-opus55-assumption |
| Claude Haiku 5.5 (xhigh) | $1,178 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | claude-pro-common-opus55-assumption:month cash | claude-pro-common-opus55-assumption |
| MiMo-V2.6-Flash | — | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | mimo-provisional-user-assumption:month cash | mimo-provisional-user-assumption |
| Claude Sonnet 5.5 (medium) | $1,178 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | claude-pro-common-opus55-assumption:month cash | claude-pro-common-opus55-assumption |
| Claude Opus 5 (max) | $1,178 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | claude-pro-common-opus55-assumption:month cash | claude-pro-common-opus55-assumption |
| Claude Haiku 5.5 (high) | $1,178 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | claude-pro-common-opus55-assumption:month cash | claude-pro-common-opus55-assumption |
| Claude Haiku 5.5 (medium) | $1,178 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | claude-pro-common-opus55-assumption:month cash | claude-pro-common-opus55-assumption |
| Claude Haiku 5.5 (low) | $1,178 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | claude-pro-common-opus55-assumption:month cash | claude-pro-common-opus55-assumption |
| Claude Sonnet 5.5 (low) | $1,178 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | claude-pro-common-opus55-assumption:month cash | claude-pro-common-opus55-assumption |

## Evidence bundle

Bundle hash `15dd4ea9c6287ccd873a7d565f8fb13edb281b4bca574e90445a9a2b7557b750`: every published output is rebuilt from these artifacts at the pinned publication clock (npm run verify:docs), never from live pages.

| Key | Artifact | SHA-256 | Captured | Extractor |
|---|---|---|---|---|
| snapshot | `data/aa/aa_v432_snapshot.json` | `177373c89a4a9cf5c35de64ad92652584693a5b1fc3d520a448432417a494780` | 2026-10-17T19:25:14Z | valuerank.capture_aa |
| deepswe | `data/aa_deepswe.json` | `e659a61582c7846ce6902da084336dcca39d447ff8f5915b370f6f3987ea0fdc` | 2026-10-17T19:26:26Z | valuerank.fetch_deepswe |
| bugHunt | `data/bug_hunt.json` | `c57cbb62851f571a9708f0599cf12265e25324118d15681837dcdb3d432b896d` | 2026-10-17 | editorial capture of the owner's published results (source commit recorded) |
| tb4 | `data/tb4.json` | `756505046b59b2436498acab8979225d88d4e726889c5fedf56c6520de4091e2` | 2026-10-17T19:25:15Z | scripts/scrape-tb4.js, then valuerank.build_tb4 |
| codingAgents | `data/aa/coding_agents_capture.json` | `944b4082d89e451c9383b662a8b3c4b3c32423d31dca2316a8ff9dc6eca6ca7c` | 2026-10-19T19:31:46Z | valuerank.capture_coding_agents |
| costCharts | `data/aa/cost_charts_capture.json` | `2e2cd3653c5f2add06595161e3839062e0ce1e989f8f3ba781cdc00814c3b5d3` | 2026-10-19T19:39:55.048Z | scripts/capture-aa-cost-charts.js |
| configurationMap | `data/v3_configuration_map.json` | `f7b36b5b186c4e9873c525d4580b46869d012713de3b95425b010bfd3ae0db62` | 2026-10-19 | editorial pinning from the research capture |
| frontierCapture | `data/aa_frontier_capture.json` | `8426c98260619827f4b1fa8182f7a2aa1c83d003f5d92b6431a35e9ef0e89b30` | — | browser capture of AA's Intelligence Index vs cost chart from public tooltips (frontier membership, E195; unevaluated cheaper siblings, E201) |
| roster | `data/aa_mapping.json` | `cf8eaf85e125fa675e3b6928ceb924794ba6d1a2920152c5263474d1190e87a7` | — | editorial roster: AA frontier and near-frontier families plus every configuration with exact DeepSWE and Bug Hunt results (O31) |
| bugHuntScoreboard | `data/bug_hunt_scoreboard.json` | `d11b49c46c60f43909e2c8e02067a9bbfd17dd3b56d5210ff047316449ef1ebb` | 2026-10-21T06:30:00Z | the owner's combined scoreboard at the pinned commit (O31 roster check) |
| planRoutes | `data/plan_cost_routes.json` | `6e72d796297481210442eeff95c15586d37b0b3c546c3e81cdd81313f139d1cf` | 2026-10-08 | editorial Plan evidence registry |
| priceRecords | `data/price_records.json` | `41e71ffea3a13f0cec1573493a8baf24b274d2de5290224d1107ee818c05cd95` | 2026-10-17T19:25:14Z | editorial E141 price-record registry (superseded and promotional tariffs) |
| anchors | `data/v3_frozen.json` | `c0738b154e26564b8629f3e923a83dce9091ebf16ddc78ffae4f206044c65dfc` | 2026-10-21 | valuerank.value_v3 freeze |


## AA intelligence and total-cost comparison

Observed 2026-10-17T18:48:27Z; Artificial Analysis Intelligence Index v4.3.2. Scope: Complete displayed intelligence versus total evaluation cost Pareto line with all 694 catalog models selected; 189 eligible plotted points, every one read from its public tooltip. This is not ValueRank's composite-quality frontier.. Reconciliation: reconciled. This view compares AA intelligence index with AA total evaluation cost in USD. Primary composite-rank eligibility is shown separately. Membership is AA's directly observed displayed frontier; no frontier is recomputed from these rows. Source selected 694 models, plotted 189 eligible points, and displayed 18 frontier points. Public metric/export gaps are shown explicitly. All 7 distinct frontier model families are required in the main ranking using exact selected configurations; 7 are included. Other effort configurations remain separate comparison entries. 9 plotted configurations from 6 families lie within 3 Index points of the rendered frontier; 6 of those families are in the main ranking, 0 are deferred.

| Exact AA model | AA ID | Intelligence index | Total evaluation cost (USD) | Observed comparison | Primary rank status | Primary evidence gaps |
|---|---|---|---|---|---|---|
| [GPT-6 Luna (low)](https://artificialanalysis.ai/models/gpt-6-luna-low) | gpt-6-luna-low | 22 (rounded) | $10.63 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the GPT-6 Luna family is represented in the primary ranking by its selected configuration (gpt-6-luna). No result is transferred between efforts. |
| [GPT-6 Luna (medium)](https://artificialanalysis.ai/models/gpt-6-luna-medium) | gpt-6-luna-medium | 30 (rounded) | $31.17 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the GPT-6 Luna family is represented in the primary ranking by its selected configuration (gpt-6-luna). No result is transferred between efforts. |
| [GPT-6 Luna (high)](https://artificialanalysis.ai/models/gpt-6-luna-high) | gpt-6-luna-high | 33 (rounded) | $47.85 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the GPT-6 Luna family is represented in the primary ranking by its selected configuration (gpt-6-luna). No result is transferred between efforts. |
| [Claude Haiku 5.5 (medium)](https://artificialanalysis.ai/models/claude-haiku-5-5-medium) | claude-haiku-5-5-medium | 34 (rounded) | $56.36 | Observed AA frontier | Primary ranked | None |
| [GPT-6 Luna (xhigh)](https://artificialanalysis.ai/models/gpt-6-luna-xhigh) | gpt-6-luna-xhigh | 35 (rounded) | $66.81 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the GPT-6 Luna family is represented in the primary ranking by its selected configuration (gpt-6-luna). No result is transferred between efforts. |
| [Claude Haiku 5.5 (high)](https://artificialanalysis.ai/models/claude-haiku-5-5-high) | claude-haiku-5-5-high | 38 (rounded) | $94.07 | Observed AA frontier | Primary ranked | None |
| [MiMo-V2.6-Flash](https://artificialanalysis.ai/models/mimo-v2-6-flash) | mimo-v2-6-flash | 38 (rounded) | $109.55 | Observed AA frontier | Primary ranked | None |
| [GPT-6 Luna (max)](https://artificialanalysis.ai/models/gpt-6-luna) | gpt-6-luna | 38 (rounded) | $122.05 | Observed AA frontier | Primary ranked | None |
| [Claude Haiku 5.5 (xhigh)](https://artificialanalysis.ai/models/claude-haiku-5-5-xhigh) | claude-haiku-5-5-xhigh | 41 (rounded) | $157.58 | Observed AA frontier | Primary ranked | None |
| [MiMo-V2.6-Pro](https://artificialanalysis.ai/models/mimo-v2-6-pro) | mimo-v2-6-pro | 46 (rounded) | $206.66 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (medium)](https://artificialanalysis.ai/models/gpt-6-1-sol-medium) | gpt-6-1-sol-medium | 48 (rounded) | $361.37 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (high)](https://artificialanalysis.ai/models/gpt-6-1-sol-high) | gpt-6-1-sol-high | 50 (rounded) | $521.32 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (xhigh)](https://artificialanalysis.ai/models/gpt-6-1-sol-xhigh) | gpt-6-1-sol-xhigh | 51 (rounded) | $662.28 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (max)](https://artificialanalysis.ai/models/gpt-6-1-sol) | gpt-6-1-sol | 52 (rounded) | $1,081.55 | Observed AA frontier | Primary ranked | None |
| [Claude Opus 5.5 (high with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-high) | claude-opus-5-5-high | 54 (rounded) | $2,172.43 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the Claude Opus 5.5 family is represented in the primary ranking by its selected configuration (claude-opus-5-5). No result is transferred between efforts. |
| [Claude Opus 5.5 (xhigh with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-xhigh) | claude-opus-5-5-xhigh | 56 (rounded) | $4,056.65 | Observed AA frontier | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA frontier comparison; the Claude Opus 5.5 family is represented in the primary ranking by its selected configuration (claude-opus-5-5). No result is transferred between efforts. |
| [Claude Sonnet 5.5 (max with fallback)](https://artificialanalysis.ai/models/claude-sonnet-5-5) | claude-sonnet-5-5 | 56 (rounded) | $7,259.50 | Observed AA frontier | Primary ranked | None |
| [Claude Opus 5.5 (max with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5) | claude-opus-5-5 | 58 (rounded) | $8,708.20 | Observed AA frontier | Primary ranked | None |
| [GPT-5.6 Luna (low)](https://artificialanalysis.ai/models/gpt-5-6-luna-low) | gpt-5-6-luna-low | 21 (rounded) | $27.02 | Near AA frontier (within 3 Index points) | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA near-frontier comparison; the GPT-5.6 Luna family is represented in the primary ranking by its selected configuration (gpt-5-6-luna). No result is transferred between efforts. |
| [Claude Haiku 5.5 (low)](https://artificialanalysis.ai/models/claude-haiku-5-5-low) | claude-haiku-5-5-low | 29 (rounded) | $34.31 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Claude Haiku 5.5 (max)](https://artificialanalysis.ai/models/claude-haiku-5-5) | claude-haiku-5-5 | 43 (rounded) | $330.25 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Claude Opus 5.5 (medium with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-medium) | claude-opus-5-5-medium | 51 (rounded) | $1,626.81 | Near AA frontier (within 3 Index points) | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA near-frontier comparison; the Claude Opus 5.5 family is represented in the primary ranking by its selected configuration (claude-opus-5-5). No result is transferred between efforts. |
| [Claude Sonnet 5.5 (xhigh with fallback)](https://artificialanalysis.ai/models/claude-sonnet-5-5-xhigh) | claude-sonnet-5-5-xhigh | 52 (rounded) | $2,176.82 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Gemini 4 Argon (high)](https://artificialanalysis.ai/models/gemini-4-argon) | gemini-4-argon | 53 (rounded) | $2,407.24 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [GPT-6 Astra (high)](https://artificialanalysis.ai/models/gpt-6-astra-high) | gpt-6-astra-high | 51 (rounded) | $2,925.01 | Near AA frontier (within 3 Index points) | Deferred comparison candidate | Exact evaluated variant absent from source roster; Reviewed 2026-10-17T19:16:08Z: Alternate configuration retained in the AA near-frontier comparison; the GPT-6 Astra family is represented in the primary ranking by its selected configuration (gpt-6-astra-xhigh). No result is transferred between efforts. |
| [GPT-6 Astra (xhigh)](https://artificialanalysis.ai/models/gpt-6-astra-xhigh) | gpt-6-astra-xhigh | 52 (rounded) | $3,802.98 | Near AA frontier (within 3 Index points) | Missing from source roster | Exact evaluated variant absent from source roster |
| [GPT-6 Astra (max)](https://artificialanalysis.ai/models/gpt-6-astra) | gpt-6-astra | 53 (rounded) | $5,324.10 | Near AA frontier (within 3 Index points) | Primary ranked | None |
