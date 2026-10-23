# ValueRank v3.0.0 Raw Data

**Updated:** October 19, 2026 · methodology 3.0.0

Every input behind the published scores, with the artifact and locator that holds it. Generated from the committed snapshots in [data/](data/); nothing here is edited by hand.

## Quality leaf inputs

| Configuration | Leaf | Raw value | Unit | Score z | Evaluated configuration / agent | Evidence |
|---|---|---:|---|---:|---|---|
| Claude Opus 5.5 (max) | FrontierCode 1.1 | 0.521731 | fraction | 52.17 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.frontierCode` |
| Claude Opus 5.5 (max) | Terminal-Bench 4.0 (AA run) | 59.5959595959596 | percent | 59.60 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.terminalBench40` |
| Claude Opus 5.5 (max) | Bug Hunt Bench | 41.7 | bugs fixed of 105 | 39.71 | Opus 5.5 (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-opus-5-5].fixedOf105` |
| Claude Opus 5.5 (max) | Vibe Code Bench v1.1 (Vals) | 90.294 | percent | 90.29 | anthropic/claude-opus-5-5 | `data/swe_tracks.json` `records[modelId=claude-opus-5-5, leaf=vibeCode].value` |
| Claude Opus 5.5 (max) | Code Migration v1.1 (Vals) | 81.012 | percent | 81.01 | anthropic/claude-opus-5-5 | `data/swe_tracks.json` `records[modelId=claude-opus-5-5, leaf=codeMigration].value` |
| Claude Opus 5.5 (max) | LiveBench 2.0 Overall | 86.53 | percent | 86.53 | claude-opus-5.5 | `data/swe_tracks.json` `records[modelId=claude-opus-5-5, leaf=livebench2Overall].value` |
| Claude Opus 5.5 (max) | GDPval-AA v2.1 | 1866.27 | Elo | 68.31 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.gdpval` |
| Claude Opus 5.5 (max) | AutomationBench-AA | 0.6953868128636069 | fraction | 69.54 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.automationBenchPartialScore` |
| Claude Opus 5.5 (max) | AA-Omniscience | 46.416666666666664 | AA Omniscience Index | 73.21 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.omniscience` |
| Claude Opus 5.5 (max) | AA-LCR v1.1 | 0.846666666666667 | fraction | 84.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.lcr` |
| Claude Opus 5.5 (max) | Humanity's Last Exam | 0.613531047265987 | fraction | 61.35 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.hle` |
| Claude Opus 5.5 (max) | SciCode | 0.668981481481482 | fraction | 66.90 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.scicode` |
| Claude Opus 5.5 (max) | CritPt | 0.317142857142857 | fraction | 31.71 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5].model.critpt` |
| Claude Sonnet 5.5 (max) | FrontierCode 1.1 | 0.458291333333333 | fraction | 45.83 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.frontierCode` |
| Claude Sonnet 5.5 (max) | Terminal-Bench 4.0 (AA run) | 63.636363636363605 | percent | 63.64 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.terminalBench40` |
| Claude Sonnet 5.5 (max) | Bug Hunt Bench | 51.3 | bugs fixed of 105 | 48.86 | Sonnet 5.5 (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-sonnet-5-5].fixedOf105` |
| Claude Sonnet 5.5 (max) | Vibe Code Bench v1.1 (Vals) | 92.392 | percent | 92.39 | anthropic/claude-sonnet-5-5 | `data/swe_tracks.json` `records[modelId=claude-sonnet-5-5, leaf=vibeCode].value` |
| Claude Sonnet 5.5 (max) | Code Migration v1.1 (Vals) | 86.875 | percent | 86.88 | anthropic/claude-sonnet-5-5 | `data/swe_tracks.json` `records[modelId=claude-sonnet-5-5, leaf=codeMigration].value` |
| Claude Sonnet 5.5 (max) | LiveBench 2.0 Overall | 82.46 | percent | 82.46 | claude-sonnet-5.5 | `data/swe_tracks.json` `records[modelId=claude-sonnet-5-5, leaf=livebench2Overall].value` |
| Claude Sonnet 5.5 (max) | GDPval-AA v2.1 | 1837.82 | Elo | 66.89 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.gdpval` |
| Claude Sonnet 5.5 (max) | AutomationBench-AA | 0.7176882128193995 | fraction | 71.77 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.automationBenchPartialScore` |
| Claude Sonnet 5.5 (max) | AA-Omniscience | 32.3 | AA Omniscience Index | 66.15 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.omniscience` |
| Claude Sonnet 5.5 (max) | AA-LCR v1.1 | 0.826666666666667 | fraction | 82.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.lcr` |
| Claude Sonnet 5.5 (max) | Humanity's Last Exam | 0.549582947173309 | fraction | 54.96 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.hle` |
| Claude Sonnet 5.5 (max) | SciCode | 0.609953703703704 | fraction | 61.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.scicode` |
| Claude Sonnet 5.5 (max) | CritPt | 0.314285714285714 | fraction | 31.43 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-sonnet-5-5].model.critpt` |
| GPT-6.1 Sol (max) | FrontierCode 1.1 | 0.491209333333333 | fraction | 49.12 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.frontierCode` |
| GPT-6.1 Sol (max) | Terminal-Bench 4.0 (AA run) | 56.0606060606061 | percent | 56.06 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.terminalBench40` |
| GPT-6.1 Sol (max) | Bug Hunt Bench | 44.3 | bugs fixed of 105 | 42.19 | GPT-6.1 Sol (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6.1-sol].fixedOf105` |
| GPT-6.1 Sol (max) | Vibe Code Bench v1.1 (Vals) | 88.931 | percent | 88.93 | openai/gpt-6.1-sol | `data/swe_tracks.json` `records[modelId=gpt-6.1-sol, leaf=vibeCode].value` |
| GPT-6.1 Sol (max) | Code Migration v1.1 (Vals) | 77.324 | percent | 77.32 | openai/gpt-6.1-sol | `data/swe_tracks.json` `records[modelId=gpt-6.1-sol, leaf=codeMigration].value` |
| GPT-6.1 Sol (max) | LiveBench 2.0 Overall | 85.41 | percent | 85.41 | gpt-6.1-sol | `data/swe_tracks.json` `records[modelId=gpt-6.1-sol, leaf=livebench2Overall].value` |
| GPT-6.1 Sol (max) | GDPval-AA v2.1 | 1592.1 | Elo | 54.60 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.gdpval` |
| GPT-6.1 Sol (max) | AutomationBench-AA | 0.6486844882398171 | fraction | 64.87 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.automationBenchPartialScore` |
| GPT-6.1 Sol (max) | AA-Omniscience | 41.53333333333333 | AA Omniscience Index | 70.77 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.omniscience` |
| GPT-6.1 Sol (max) | AA-LCR v1.1 | 0.83 | fraction | 83.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.lcr` |
| GPT-6.1 Sol (max) | Humanity's Last Exam | 0.529193697868397 | fraction | 52.92 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.hle` |
| GPT-6.1 Sol (max) | SciCode | 0.541666666666667 | fraction | 54.17 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.scicode` |
| GPT-6.1 Sol (max) | CritPt | 0.317142857142857 | fraction | 31.71 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol].model.critpt` |
| Claude Haiku 5.5 (max) | FrontierCode 1.1 | 0.418067 | fraction | 41.81 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5].model.frontierCode` |
| Claude Haiku 5.5 (max) | Terminal-Bench 4.0 (AA run) | 32.8282828282828 | percent | 32.83 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5].model.terminalBench40` |
| Claude Haiku 5.5 (max) | Bug Hunt Bench | 21.5 | bugs fixed of 105 | 20.48 | Haiku 5.5 (max effort) - mean of 2 | `data/bug_hunt.json` `models[modelId=claude-haiku-5-5-max].fixedOf105` |
| Claude Haiku 5.5 (max) | Vibe Code Bench v1.1 (Vals) | 90.444 | percent | 90.44 | anthropic/claude-haiku-5-5 | `data/swe_tracks.json` `records[modelId=claude-haiku-5-5-max, leaf=vibeCode].value` |
| Claude Haiku 5.5 (max) | Code Migration v1.1 (Vals) | 52.36 | percent | 52.36 | anthropic/claude-haiku-5-5 | `data/swe_tracks.json` `records[modelId=claude-haiku-5-5-max, leaf=codeMigration].value` |
| Claude Haiku 5.5 (max) | LiveBench 2.0 Overall | 75.64 | percent | 75.64 | claude-haiku-5.5 | `data/swe_tracks.json` `records[modelId=claude-haiku-5-5-max, leaf=livebench2Overall].value` |
| Claude Haiku 5.5 (max) | GDPval-AA v2.1 | 1617.13 | Elo | 55.86 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5].model.gdpval` |
| Claude Haiku 5.5 (max) | AutomationBench-AA | 0.35411015132783624 | fraction | 35.41 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5].model.automationBenchPartialScore` |
| Claude Haiku 5.5 (max) | AA-Omniscience | 10.666666666666666 | AA Omniscience Index | 55.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5].model.omniscience` |
| Claude Haiku 5.5 (max) | AA-LCR v1.1 | 0.826666666666667 | fraction | 82.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5].model.lcr` |
| Claude Haiku 5.5 (max) | Humanity's Last Exam | 0.443929564411492 | fraction | 44.39 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5].model.hle` |
| Claude Haiku 5.5 (max) | SciCode | 0.549768518518518 | fraction | 54.98 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5].model.scicode` |
| Claude Haiku 5.5 (max) | CritPt | 0.188571428571429 | fraction | 18.86 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5].model.critpt` |
| GPT-6 Astra (max) | FrontierCode 1.1 | 0.469827666666667 | fraction | 46.98 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.frontierCode` |
| GPT-6 Astra (max) | Terminal-Bench 4.0 (AA run) | 59.09090909090911 | percent | 59.09 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.terminalBench40` |
| GPT-6 Astra (max) | Bug Hunt Bench | 45.0 | bugs fixed of 105 | 42.86 | GPT-6 Astra (max effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6-astra].fixedOf105` |
| GPT-6 Astra (max) | Vibe Code Bench v1.1 (Vals) | 89.594 | percent | 89.59 | openai/gpt-6-astra | `data/swe_tracks.json` `records[modelId=gpt-6-astra, leaf=vibeCode].value` |
| GPT-6 Astra (max) | Code Migration v1.1 (Vals) | 80.579 | percent | 80.58 | openai/gpt-6-astra | `data/swe_tracks.json` `records[modelId=gpt-6-astra, leaf=codeMigration].value` |
| GPT-6 Astra (max) | LiveBench 2.0 Overall | 86.14 | percent | 86.14 | gpt-6-astra | `data/swe_tracks.json` `records[modelId=gpt-6-astra, leaf=livebench2Overall].value` |
| GPT-6 Astra (max) | GDPval-AA v2.1 | 1571.76 | Elo | 53.59 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.gdpval` |
| GPT-6 Astra (max) | AutomationBench-AA | 0.6849174806688876 | fraction | 68.49 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.automationBenchPartialScore` |
| GPT-6 Astra (max) | AA-Omniscience | 43.4 | AA Omniscience Index | 71.70 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.omniscience` |
| GPT-6 Astra (max) | AA-LCR v1.1 | 0.806666666666667 | fraction | 80.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.lcr` |
| GPT-6 Astra (max) | Humanity's Last Exam | 0.546802594995366 | fraction | 54.68 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.hle` |
| GPT-6 Astra (max) | SciCode | 0.564814814814815 | fraction | 56.48 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.scicode` |
| GPT-6 Astra (max) | CritPt | 0.317142857142857 | fraction | 31.71 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra].model.critpt` |
| GPT-6 Luna (max) | FrontierCode 1.1 | 0.419269666666667 | fraction | 41.93 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.frontierCode` |
| GPT-6 Luna (max) | Terminal-Bench 4.0 (AA run) | 12.6262626262626 | percent | 12.63 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.terminalBench40` |
| GPT-6 Luna (max) | Bug Hunt Bench | 18.3 | bugs fixed of 105 | 17.43 | GPT-6 Luna MAX - mean of 3 | `data/bug_hunt.json` `models[modelId=gpt-6-luna].fixedOf105` |
| GPT-6 Luna (max) | Vibe Code Bench v1.1 (Vals) | 81.649 | percent | 81.65 | openai/gpt-6-luna | `data/swe_tracks.json` `records[modelId=gpt-6-luna, leaf=vibeCode].value` |
| GPT-6 Luna (max) | Code Migration v1.1 (Vals) | 46.669 | percent | 46.67 | openai/gpt-6-luna | `data/swe_tracks.json` `records[modelId=gpt-6-luna, leaf=codeMigration].value` |
| GPT-6 Luna (max) | LiveBench 2.0 Overall | 69.4 | percent | 69.40 | gpt-6-luna | `data/swe_tracks.json` `records[modelId=gpt-6-luna, leaf=livebench2Overall].value` |
| GPT-6 Luna (max) | GDPval-AA v2.1 | 1431.02 | Elo | 46.55 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.gdpval` |
| GPT-6 Luna (max) | AutomationBench-AA | 0.5316814034483175 | fraction | 53.17 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.automationBenchPartialScore` |
| GPT-6 Luna (max) | AA-Omniscience | 0.65 | AA Omniscience Index | 50.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.omniscience` |
| GPT-6 Luna (max) | AA-LCR v1.1 | 0.833333333333333 | fraction | 83.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.lcr` |
| GPT-6 Luna (max) | Humanity's Last Exam | 0.385078776645042 | fraction | 38.51 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.hle` |
| GPT-6 Luna (max) | SciCode | 0.546296296296296 | fraction | 54.63 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.scicode` |
| GPT-6 Luna (max) | CritPt | 0.194285714285714 | fraction | 19.43 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna].model.critpt` |
| MiMo-V2.6-Pro | FrontierCode 1.1 | 0.454153333333333 | fraction | 45.42 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-pro].model.frontierCode` |
| MiMo-V2.6-Pro | Terminal-Bench 4.0 (AA run) | 34.8484848484849 | percent | 34.85 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-pro].model.terminalBench40` |
| MiMo-V2.6-Pro | Bug Hunt Bench | 18 | bugs fixed of 105 | 17.14 | MiMo-V2.6-Pro (first-party, thinking enabled) | `data/bug_hunt.json` `models[modelId=mimo-v2-6-pro].fixedOf105` |
| MiMo-V2.6-Pro | Vibe Code Bench v1.1 (Vals) | 85.223 | percent | 85.22 | xiaomi/mimo-v2.6-pro | `data/swe_tracks.json` `records[modelId=mimo-v2-6-pro, leaf=vibeCode].value` |
| MiMo-V2.6-Pro | Code Migration v1.1 (Vals) | 48.786 | percent | 48.79 | xiaomi/mimo-v2.6-pro | `data/swe_tracks.json` `records[modelId=mimo-v2-6-pro, leaf=codeMigration].value` |
| MiMo-V2.6-Pro | LiveBench 2.0 Overall | 74.87 | percent | 74.87 | mimo-v2.6-pro | `data/swe_tracks.json` `records[modelId=mimo-v2-6-pro, leaf=livebench2Overall].value` |
| MiMo-V2.6-Pro | GDPval-AA v2.1 | 1683.29 | Elo | 59.16 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-pro].model.gdpval` |
| MiMo-V2.6-Pro | AutomationBench-AA | 0.5862340943419085 | fraction | 58.62 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-pro].model.automationBenchPartialScore` |
| MiMo-V2.6-Pro | AA-Omniscience | 8.383333333333333 | AA Omniscience Index | 54.19 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-pro].model.omniscience` |
| MiMo-V2.6-Pro | AA-LCR v1.1 | 0.863333333333333 | fraction | 86.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-pro].model.lcr` |
| MiMo-V2.6-Pro | Humanity's Last Exam | 0.493512511584801 | fraction | 49.35 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-pro].model.hle` |
| MiMo-V2.6-Pro | SciCode | 0.608796296296296 | fraction | 60.88 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-pro].model.scicode` |
| MiMo-V2.6-Pro | CritPt | 0.265714285714286 | fraction | 26.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=mimo-v2-6-pro].model.critpt` |
| DeepSeek V4.1 Flash 1017 (max) | FrontierCode 1.1 | 0.436605666666667 | fraction | 43.66 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-1-flash-1017].model.frontierCode` |
| DeepSeek V4.1 Flash 1017 (max) | Terminal-Bench 4.0 (AA run) | 33.8383838383838 | percent | 33.84 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-1-flash-1017].model.terminalBench40` |
| DeepSeek V4.1 Flash 1017 (max) | Bug Hunt Bench | 42.7 | bugs fixed of 105 | 40.67 | DeepSeek V4.1 Flash 1017 (max effort, DeepSeek Harness) - mean of 7 | `data/bug_hunt.json` `models[modelId=deepseek-v4-1-flash-1017].fixedOf105` |
| DeepSeek V4.1 Flash 1017 (max) | Vibe Code Bench v1.1 (Vals) | 87.73 | percent | 87.73 | deepseek/deepseek-v4.1-flash-1017 | `data/swe_tracks.json` `records[modelId=deepseek-v4-1-flash-1017, leaf=vibeCode].value` |
| DeepSeek V4.1 Flash 1017 (max) | Code Migration v1.1 (Vals) | 67.524 | percent | 67.52 | deepseek/deepseek-v4.1-flash-1017 | `data/swe_tracks.json` `records[modelId=deepseek-v4-1-flash-1017, leaf=codeMigration].value` |
| DeepSeek V4.1 Flash 1017 (max) | LiveBench 2.0 Overall | 79.2 | percent | 79.20 | deepseek-v4.1-flash-1017 | `data/swe_tracks.json` `records[modelId=deepseek-v4-1-flash-1017, leaf=livebench2Overall].value` |
| DeepSeek V4.1 Flash 1017 (max) | GDPval-AA v2.1 | 1745.77 | Elo | 62.29 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-1-flash-1017].model.gdpval` |
| DeepSeek V4.1 Flash 1017 (max) | AutomationBench-AA | 0.6664095364949257 | fraction | 66.64 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-1-flash-1017].model.automationBenchPartialScore` |
| DeepSeek V4.1 Flash 1017 (max) | AA-Omniscience | 4.7 | AA Omniscience Index | 52.35 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-1-flash-1017].model.omniscience` |
| DeepSeek V4.1 Flash 1017 (max) | AA-LCR v1.1 | 0.826666666666667 | fraction | 82.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-1-flash-1017].model.lcr` |
| DeepSeek V4.1 Flash 1017 (max) | Humanity's Last Exam | 0.433271547729379 | fraction | 43.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-1-flash-1017].model.hle` |
| DeepSeek V4.1 Flash 1017 (max) | SciCode | 0.559027777777778 | fraction | 55.90 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-1-flash-1017].model.scicode` |
| DeepSeek V4.1 Flash 1017 (max) | CritPt | 0.24 | fraction | 24.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=deepseek-v4-1-flash-1017].model.critpt` |
| Gemini 4 Argon (high) | FrontierCode 1.1 | 0.434532 | fraction | 43.45 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-4-argon].model.frontierCode` |
| Gemini 4 Argon (high) | Terminal-Bench 4.0 (AA run) | 57.07070707070711 | percent | 57.07 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-4-argon].model.terminalBench40` |
| Gemini 4 Argon (high) | Bug Hunt Bench | 40.7 | bugs fixed of 105 | 38.76 | Gemini 4 Argon (high effort, Antigravity CLI) - mean of 3 | `data/bug_hunt.json` `models[modelId=gemini-4-argon].fixedOf105` |
| Gemini 4 Argon (high) | Vibe Code Bench v1.1 (Vals) | 91.906 | percent | 91.91 | google/gemini-4-argon | `data/swe_tracks.json` `records[modelId=gemini-4-argon, leaf=vibeCode].value` |
| Gemini 4 Argon (high) | Code Migration v1.1 (Vals) | 70.796 | percent | 70.80 | google/gemini-4-argon | `data/swe_tracks.json` `records[modelId=gemini-4-argon, leaf=codeMigration].value` |
| Gemini 4 Argon (high) | LiveBench 2.0 Overall | 84.1 | percent | 84.10 | gemini-4-argon | `data/swe_tracks.json` `records[modelId=gemini-4-argon, leaf=livebench2Overall].value` |
| Gemini 4 Argon (high) | GDPval-AA v2.1 | 1623.11 | Elo | 56.16 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-4-argon].model.gdpval` |
| Gemini 4 Argon (high) | AutomationBench-AA | 0.7751346945899195 | fraction | 77.51 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-4-argon].model.automationBenchPartialScore` |
| Gemini 4 Argon (high) | AA-Omniscience | 42.35 | AA Omniscience Index | 71.17 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-4-argon].model.omniscience` |
| Gemini 4 Argon (high) | AA-LCR v1.1 | 0.796666666666667 | fraction | 79.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-4-argon].model.lcr` |
| Gemini 4 Argon (high) | Humanity's Last Exam | 0.570898980537535 | fraction | 57.09 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-4-argon].model.hle` |
| Gemini 4 Argon (high) | SciCode | 0.618055555555556 | fraction | 61.81 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-4-argon].model.scicode` |
| Gemini 4 Argon (high) | CritPt | 0.271428571428571 | fraction | 27.14 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gemini-4-argon].model.critpt` |
| Claude Opus 5.5 (high) | FrontierCode 1.1 | 0.539616333333333 | fraction | 53.96 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.frontierCode` |
| Claude Opus 5.5 (high) | Terminal-Bench 4.0 (AA run) | 56.565656565656596 | percent | 56.57 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.terminalBench40` |
| Claude Opus 5.5 (high) | Bug Hunt Bench | 31.7 | bugs fixed of 105 | 30.19 | Opus 5.5 (high effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-opus-5-5-high].fixedOf105` |
| Claude Opus 5.5 (high) | AI Coding Daily (excl. bug finding) | 57.68 | points of 60 | 96.13 | Opus 5.5 (High) | `data/swe_tracks.json` `records[modelId=claude-opus-5-5-high, leaf=aiCodingDaily].value` |
| Claude Opus 5.5 (high) | GDPval-AA v2.1 | 1703.4 | Elo | 60.17 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.gdpval` |
| Claude Opus 5.5 (high) | AutomationBench-AA | 0.6320677483186213 | fraction | 63.21 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.automationBenchPartialScore` |
| Claude Opus 5.5 (high) | AA-Omniscience | 40.63333333333333 | AA Omniscience Index | 70.32 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.omniscience` |
| Claude Opus 5.5 (high) | AA-LCR v1.1 | 0.826666666666667 | fraction | 82.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.lcr` |
| Claude Opus 5.5 (high) | Humanity's Last Exam | 0.555607043558851 | fraction | 55.56 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.hle` |
| Claude Opus 5.5 (high) | SciCode | 0.604166666666667 | fraction | 60.42 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.scicode` |
| Claude Opus 5.5 (high) | CritPt | 0.308571428571429 | fraction | 30.86 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-high].model.critpt` |
| Claude Opus 5.5 (medium) | FrontierCode 1.1 | 0.570542333333333 | fraction | 57.05 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-medium].model.frontierCode` |
| Claude Opus 5.5 (medium) | Terminal-Bench 4.0 (AA run) | 52.5252525252525 | percent | 52.53 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-medium].model.terminalBench40` |
| Claude Opus 5.5 (medium) | Bug Hunt Bench | 30.3 | bugs fixed of 105 | 28.86 | Opus 5.5 (medium effort) - mean of 3 | `data/bug_hunt.json` `models[modelId=claude-opus-5-5-medium].fixedOf105` |
| Claude Opus 5.5 (medium) | AI Coding Daily (excl. bug finding) | 56.95 | points of 60 | 94.92 | Opus 5.5 (Medium) | `data/swe_tracks.json` `records[modelId=claude-opus-5-5-medium, leaf=aiCodingDaily].value` |
| Claude Opus 5.5 (medium) | GDPval-AA v2.1 | 1582.9 | Elo | 54.15 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-medium].model.gdpval` |
| Claude Opus 5.5 (medium) | AutomationBench-AA | 0.6121742919892179 | fraction | 61.22 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-medium].model.automationBenchPartialScore` |
| Claude Opus 5.5 (medium) | AA-Omniscience | 40.31666666666667 | AA Omniscience Index | 70.16 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-medium].model.omniscience` |
| Claude Opus 5.5 (medium) | AA-LCR v1.1 | 0.843333333333333 | fraction | 84.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-medium].model.lcr` |
| Claude Opus 5.5 (medium) | Humanity's Last Exam | 0.547265987025023 | fraction | 54.73 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-medium].model.hle` |
| Claude Opus 5.5 (medium) | SciCode | 0.592592592592593 | fraction | 59.26 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-medium].model.scicode` |
| Claude Opus 5.5 (medium) | CritPt | 0.277142857142857 | fraction | 27.71 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-opus-5-5-medium].model.critpt` |
| GPT-6.1 Sol (high) | FrontierCode 1.1 | 0.466056333333333 | fraction | 46.61 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.frontierCode` |
| GPT-6.1 Sol (high) | Terminal-Bench 4.0 (AA run) | 51.5151515151515 | percent | 51.52 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.terminalBench40` |
| GPT-6.1 Sol (high) | Bug Hunt Bench | 36.5 | bugs fixed of 105 | 34.76 | GPT-6.1 Sol (high effort) - mean of 2 | `data/bug_hunt.json` `models[modelId=gpt-6.1-sol-high].fixedOf105` |
| GPT-6.1 Sol (high) | AI Coding Daily (excl. bug finding) | 56.83 | points of 60 | 94.72 | GPT-6.1-Sol (High) | `data/swe_tracks.json` `records[modelId=gpt-6.1-sol-high, leaf=aiCodingDaily].value` |
| GPT-6.1 Sol (high) | GDPval-AA v2.1 | 1508.57 | Elo | 50.43 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.gdpval` |
| GPT-6.1 Sol (high) | AutomationBench-AA | 0.6449523732184466 | fraction | 64.50 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.automationBenchPartialScore` |
| GPT-6.1 Sol (high) | AA-Omniscience | 41.45 | AA Omniscience Index | 70.72 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.omniscience` |
| GPT-6.1 Sol (high) | AA-LCR v1.1 | 0.823333333333333 | fraction | 82.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.lcr` |
| GPT-6.1 Sol (high) | Humanity's Last Exam | 0.513901760889713 | fraction | 51.39 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.hle` |
| GPT-6.1 Sol (high) | SciCode | 0.55787037037037 | fraction | 55.79 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.scicode` |
| GPT-6.1 Sol (high) | CritPt | 0.3 | fraction | 30.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-high].model.critpt` |
| GPT-6.1 Sol (medium) | FrontierCode 1.1 | 0.433330666666667 | fraction | 43.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.frontierCode` |
| GPT-6.1 Sol (medium) | Terminal-Bench 4.0 (AA run) | 47.979797979798 | percent | 47.98 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.terminalBench40` |
| GPT-6.1 Sol (medium) | Bug Hunt Bench | 29.0 | bugs fixed of 105 | 27.62 | GPT-6.1 Sol (medium effort) - mean of 2 | `data/bug_hunt.json` `models[modelId=gpt-6.1-sol-medium].fixedOf105` |
| GPT-6.1 Sol (medium) | AI Coding Daily (excl. bug finding) | 55.67 | points of 60 | 92.78 | GPT-6.1-Sol (Medium) | `data/swe_tracks.json` `records[modelId=gpt-6.1-sol-medium, leaf=aiCodingDaily].value` |
| GPT-6.1 Sol (medium) | GDPval-AA v2.1 | 1448.5 | Elo | 47.42 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.gdpval` |
| GPT-6.1 Sol (medium) | AutomationBench-AA | 0.6257350970435687 | fraction | 62.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.automationBenchPartialScore` |
| GPT-6.1 Sol (medium) | AA-Omniscience | 39.95 | AA Omniscience Index | 69.97 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.omniscience` |
| GPT-6.1 Sol (medium) | AA-LCR v1.1 | 0.833333333333333 | fraction | 83.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.lcr` |
| GPT-6.1 Sol (medium) | Humanity's Last Exam | 0.498609823911029 | fraction | 49.86 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.hle` |
| GPT-6.1 Sol (medium) | SciCode | 0.532407407407407 | fraction | 53.24 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.scicode` |
| GPT-6.1 Sol (medium) | CritPt | 0.277142857142857 | fraction | 27.71 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-1-sol-medium].model.critpt` |
| Claude Haiku 5.5 (high) | FrontierCode 1.1 | 0.436422666666667 | fraction | 43.64 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.frontierCode` |
| Claude Haiku 5.5 (high) | Terminal-Bench 4.0 (AA run) | 21.7171717171717 | percent | 21.72 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.terminalBench40` |
| Claude Haiku 5.5 (high) | Bug Hunt Bench | 16.0 | bugs fixed of 105 | 15.24 | Haiku 5.5 (high effort) - mean of 2 | `data/bug_hunt.json` `models[modelId=claude-haiku-5-5-high].fixedOf105` |
| Claude Haiku 5.5 (high) | AI Coding Daily (excl. bug finding) | 51.55 | points of 60 | 85.92 | Haiku 5.5 (High) | `data/swe_tracks.json` `records[modelId=claude-haiku-5-5-high, leaf=aiCodingDaily].value` |
| Claude Haiku 5.5 (high) | GDPval-AA v2.1 | 1415.97 | Elo | 45.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.gdpval` |
| Claude Haiku 5.5 (high) | AutomationBench-AA | 0.3372685311767238 | fraction | 33.73 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.automationBenchPartialScore` |
| Claude Haiku 5.5 (high) | AA-Omniscience | 5.75 | AA Omniscience Index | 52.88 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.omniscience` |
| Claude Haiku 5.5 (high) | AA-LCR v1.1 | 0.773333333333333 | fraction | 77.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.lcr` |
| Claude Haiku 5.5 (high) | Humanity's Last Exam | 0.3725671918443 | fraction | 37.26 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.hle` |
| Claude Haiku 5.5 (high) | SciCode | 0.487268518518519 | fraction | 48.73 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.scicode` |
| Claude Haiku 5.5 (high) | CritPt | 0.185714285714286 | fraction | 18.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-high].model.critpt` |
| Claude Haiku 5.5 (medium) | FrontierCode 1.1 | 0.404265666666667 | fraction | 40.43 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.frontierCode` |
| Claude Haiku 5.5 (medium) | Terminal-Bench 4.0 (AA run) | 15.151515151515198 | percent | 15.15 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.terminalBench40` |
| Claude Haiku 5.5 (medium) | Bug Hunt Bench | 12.0 | bugs fixed of 105 | 11.43 | Haiku 5.5 (medium effort) | `data/bug_hunt.json` `models[modelId=claude-haiku-5-5-medium].fixedOf105` |
| Claude Haiku 5.5 (medium) | AI Coding Daily (excl. bug finding) | 51.32 | points of 60 | 85.53 | Haiku 5.5 (Medium) | `data/swe_tracks.json` `records[modelId=claude-haiku-5-5-medium, leaf=aiCodingDaily].value` |
| Claude Haiku 5.5 (medium) | GDPval-AA v2.1 | 1272.78 | Elo | 38.64 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.gdpval` |
| Claude Haiku 5.5 (medium) | AutomationBench-AA | 0.2858961481429316 | fraction | 28.59 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.automationBenchPartialScore` |
| Claude Haiku 5.5 (medium) | AA-Omniscience | 4.466666666666667 | AA Omniscience Index | 52.23 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.omniscience` |
| Claude Haiku 5.5 (medium) | AA-LCR v1.1 | 0.773333333333333 | fraction | 77.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.lcr` |
| Claude Haiku 5.5 (medium) | Humanity's Last Exam | 0.337812789620019 | fraction | 33.78 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.hle` |
| Claude Haiku 5.5 (medium) | SciCode | 0.489583333333333 | fraction | 48.96 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.scicode` |
| Claude Haiku 5.5 (medium) | CritPt | 0.128571428571429 | fraction | 12.86 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=claude-haiku-5-5-medium].model.critpt` |
| GPT-6 Astra (high) | FrontierCode 1.1 | 0.5094 | fraction | 50.94 | GPT-6 Astra (high), harness codex | `data/cognition_frontiercode.json` `v1_1.data['GPT-6 Astra'].high.main.new_score` |
| GPT-6 Astra (high) | Terminal-Bench 4.0 (AA run) | 54.040404040404 | percent | 54.04 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.terminalBench40` |
| GPT-6 Astra (high) | Bug Hunt Bench | 35.0 | bugs fixed of 105 | 33.33 | GPT-6 Astra (high effort) | `data/bug_hunt.json` `models[modelId=gpt-6-astra-high].fixedOf105` |
| GPT-6 Astra (high) | AI Coding Daily (excl. bug finding) | 56.77 | points of 60 | 94.62 | GPT-6-Astra (High) | `data/swe_tracks.json` `records[modelId=gpt-6-astra-high, leaf=aiCodingDaily].value` |
| GPT-6 Astra (high) | GDPval-AA v2.1 | 1522.36 | Elo | 51.12 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.gdpval` |
| GPT-6 Astra (high) | AutomationBench-AA | 0.666122174975011 | fraction | 66.61 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.automationBenchPartialScore` |
| GPT-6 Astra (high) | AA-Omniscience | 43.733333333333334 | AA Omniscience Index | 71.87 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.omniscience` |
| GPT-6 Astra (high) | AA-LCR v1.1 | 0.8 | fraction | 80.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.lcr` |
| GPT-6 Astra (high) | Humanity's Last Exam | 0.530583873957368 | fraction | 53.06 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.hle` |
| GPT-6 Astra (high) | SciCode | 0.554398148148148 | fraction | 55.44 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.scicode` |
| GPT-6 Astra (high) | CritPt | 0.288571428571429 | fraction | 28.86 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-astra-high].model.critpt` |
| GPT-6 Luna (max) | AI Coding Daily (excl. bug finding) | 51.99 | points of 60 | 86.65 | GPT-6-Luna (Max) | `data/swe_tracks.json` `records[modelId=gpt-6-luna, leaf=aiCodingDaily].value` |
| GPT-6 Luna (xhigh) | FrontierCode 1.1 | 0.332155333333333 | fraction | 33.22 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.frontierCode` |
| GPT-6 Luna (xhigh) | Terminal-Bench 4.0 (AA run) | 8.08080808080808 | percent | 8.08 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.terminalBench40` |
| GPT-6 Luna (xhigh) | Bug Hunt Bench | 14.0 | bugs fixed of 105 | 13.33 | GPT-6 Luna (xhigh effort) | `data/bug_hunt.json` `models[modelId=gpt-6-luna-xhigh].fixedOf105` |
| GPT-6 Luna (xhigh) | AI Coding Daily (excl. bug finding) | 49.94 | points of 60 | 83.23 | GPT-6-Luna (Xhigh) | `data/swe_tracks.json` `records[modelId=gpt-6-luna-xhigh, leaf=aiCodingDaily].value` |
| GPT-6 Luna (xhigh) | GDPval-AA v2.1 | 1362.25 | Elo | 43.11 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.gdpval` |
| GPT-6 Luna (xhigh) | AutomationBench-AA | 0.47800686767566575 | fraction | 47.80 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.automationBenchPartialScore` |
| GPT-6 Luna (xhigh) | AA-Omniscience | -1.8333333333333333 | AA Omniscience Index | 49.08 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.omniscience` |
| GPT-6 Luna (xhigh) | AA-LCR v1.1 | 0.8 | fraction | 80.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.lcr` |
| GPT-6 Luna (xhigh) | Humanity's Last Exam | 0.343373493975904 | fraction | 34.34 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.hle` |
| GPT-6 Luna (xhigh) | SciCode | 0.517361111111111 | fraction | 51.74 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.scicode` |
| GPT-6 Luna (xhigh) | CritPt | 0.174285714285714 | fraction | 17.43 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-xhigh].model.critpt` |
| MiMo-V2.6-Pro | AI Coding Daily (excl. bug finding) | 47.56 | points of 60 | 79.27 | MiMo-V2.6 Pro (High) | `data/swe_tracks.json` `records[modelId=mimo-v2-6-pro, leaf=aiCodingDaily].value` |
| DeepSeek V4.1 Flash 1017 (max) | AI Coding Daily (excl. bug finding) | 52.24 | points of 60 | 87.07 | Deepseek-V4.1-Flash-1017 (Max) | `data/swe_tracks.json` `records[modelId=deepseek-v4-1-flash-1017, leaf=aiCodingDaily].value` |
| Gemini 4 Argon (high) | AI Coding Daily (excl. bug finding) | 49.9 | points of 60 | 83.17 | Gemini 4 Argon (High) | `data/swe_tracks.json` `records[modelId=gemini-4-argon, leaf=aiCodingDaily].value` |
| GPT-6 Luna (high) | FrontierCode 1.1 | 0.320254666666667 | fraction | 32.03 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.frontierCode` |
| GPT-6 Luna (high) | Terminal-Bench 4.0 (AA run) | 4.545454545454549 | percent | 4.55 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.terminalBench40` |
| GPT-6 Luna (high) | Bug Hunt Bench | 9.0 | bugs fixed of 105 | 8.57 | GPT-6 Luna (high effort) | `data/bug_hunt.json` `models[modelId=gpt-6-luna-high].fixedOf105` |
| GPT-6 Luna (high) | AI Coding Daily (excl. bug finding) | 47.73 | points of 60 | 79.55 | GPT-6-Luna (High) | `data/swe_tracks.json` `records[modelId=gpt-6-luna-high, leaf=aiCodingDaily].value` |
| GPT-6 Luna (high) | GDPval-AA v2.1 | 1339.36 | Elo | 41.97 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.gdpval` |
| GPT-6 Luna (high) | AutomationBench-AA | 0.4782449139916615 | fraction | 47.82 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.automationBenchPartialScore` |
| GPT-6 Luna (high) | AA-Omniscience | -5.5 | AA Omniscience Index | 47.25 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.omniscience` |
| GPT-6 Luna (high) | AA-LCR v1.1 | 0.793333333333333 | fraction | 79.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.lcr` |
| GPT-6 Luna (high) | Humanity's Last Exam | 0.329471733086191 | fraction | 32.95 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.hle` |
| GPT-6 Luna (high) | SciCode | 0.503472222222222 | fraction | 50.35 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.scicode` |
| GPT-6 Luna (high) | CritPt | 0.154285714285714 | fraction | 15.43 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-high].model.critpt` |
| GPT-6 Luna (medium) | FrontierCode 1.1 | 0.318060333333333 | fraction | 31.81 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.frontierCode` |
| GPT-6 Luna (medium) | Terminal-Bench 4.0 (AA run) | 2.52525252525253 | percent | 2.53 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.terminalBench40` |
| GPT-6 Luna (medium) | Bug Hunt Bench | 4.0 | bugs fixed of 105 | 3.81 | GPT-6 Luna (medium effort) | `data/bug_hunt.json` `models[modelId=gpt-6-luna-medium].fixedOf105` |
| GPT-6 Luna (medium) | AI Coding Daily (excl. bug finding) | 40.2 | points of 60 | 67.00 | GPT-6-Luna (Medium) | `data/swe_tracks.json` `records[modelId=gpt-6-luna-medium, leaf=aiCodingDaily].value` |
| GPT-6 Luna (medium) | GDPval-AA v2.1 | 1261.32 | Elo | 38.07 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.gdpval` |
| GPT-6 Luna (medium) | AutomationBench-AA | 0.4046136879135791 | fraction | 40.46 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.automationBenchPartialScore` |
| GPT-6 Luna (medium) | AA-Omniscience | -5.05 | AA Omniscience Index | 47.48 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.omniscience` |
| GPT-6 Luna (medium) | AA-LCR v1.1 | 0.783333333333333 | fraction | 78.33 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.lcr` |
| GPT-6 Luna (medium) | Humanity's Last Exam | 0.282669138090825 | fraction | 28.27 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.hle` |
| GPT-6 Luna (medium) | SciCode | 0.509259259259259 | fraction | 50.93 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.scicode` |
| GPT-6 Luna (medium) | CritPt | 0.105714285714286 | fraction | 10.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-6-luna-medium].model.critpt` |
| GPT-5.6 Luna (low) | FrontierCode 1.1 | 0.1538 | fraction | 15.38 | GPT-5.6 Luna (low), harness codex | `data/cognition_frontiercode.json` `v1_1.data['GPT-5.6 Luna'].low.main.new_score` |
| GPT-5.6 Luna (low) | Terminal-Bench 4.0 (AA run) | 0.0 | percent | 0.00 | mini-SWE-agent | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-luna-low].model.terminalBench40` |
| GPT-5.6 Luna (low) | Bug Hunt Bench | 4.0 | bugs fixed of 105 | 3.81 | GPT-5.6 Luna (low effort) | `data/bug_hunt.json` `models[modelId=gpt-5.6-luna-low].fixedOf105` |
| GPT-5.6 Luna (low) | AI Coding Daily (excl. bug finding) | 30.51 | points of 60 | 50.85 | GPT-5.6-Luna (Low) | `data/swe_tracks.json` `records[modelId=gpt-5.6-luna-low, leaf=aiCodingDaily].value` |
| GPT-5.6 Luna (low) | GDPval-AA v2.1 | 992.25 | Elo | 24.61 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-luna-low].model.gdpval` |
| GPT-5.6 Luna (low) | AutomationBench-AA | 0.11692162258271627 | fraction | 11.69 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-luna-low].model.automationBenchPartialScore` |
| GPT-5.6 Luna (low) | AA-Omniscience | -14.65 | AA Omniscience Index | 42.67 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-luna-low].model.omniscience` |
| GPT-5.6 Luna (low) | AA-LCR v1.1 | 0.7 | fraction | 70.00 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-luna-low].model.lcr` |
| GPT-5.6 Luna (low) | Humanity's Last Exam | 0.198331788693234 | fraction | 19.83 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-luna-low].model.hle` |
| GPT-5.6 Luna (low) | SciCode | 0.460648148148148 | fraction | 46.06 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-luna-low].model.scicode` |
| GPT-5.6 Luna (low) | CritPt | 0.0257142857142857 | fraction | 2.57 | — | `data/aa/aa_v432_snapshot.json` `pages[model.slug=gpt-5-6-luna-low].model.critpt` |

## Leaf gap fills and searches (O36)

Leaves a ranked configuration takes from beyond its primary source, in the order a newer AA capture, another party's run of the same benchmark on the exact configuration, then the model provider's published result (O36/O37). Tbench.ai Terminal-Bench rows used as gap fills are in the leaf inputs above with their agent.

| Configuration | Leaf | Value | Unit | Source type | Publisher | Evaluated configuration | Benchmark version | Metric (E237) | Source |
|---|---|---:|---|---|---|---|---|---|---|

Exhaustive searches for the leaves a cohort configuration still lacks (each within 7 days of the cutoff; the configuration is listed, not ranked). The sources searched are in [data/leaf_evidence.json](data/leaf_evidence.json).

| Configuration | Leaf | Searched | Result | Sources checked | Open-web discovery (E240) | Notes |
|---|---|---|---|---:|---|---|
| MiMo-V2.6-Flash | Bug Hunt Bench | 2026-10-21 | not found | 2 | 2026-10-23: 11 queries, 6 candidates (0 registered, 6 rejected) | The only Flash row is 'MiMo-V2.6-Flash - mean of 3' (OpenRouter, default effort; reasoning state not asserted and untested for Flash). No first-party or thinking-enabled Flash run exists. |
| Grok 4.6 (xhigh) | FrontierCode 1.1 | 2026-10-21 | not found | 7 | 2026-10-23: 8 queries, 6 candidates (0 registered, 6 rejected) | xAI publishes FrontierCode v1.1 Extended 61.3% for Grok 4.6 at High effort only; xhigh appears nowhere. Cognition and its relays list Grok 4.6 at high effort (Main 48.0%). No exact-effort (xhigh) score exists; efforts are not transferred. |
| DeepSeek V4 Flash | FrontierCode 1.1 | 2026-10-21 | not found | 8 | 2026-10-23: 7 queries, 5 candidates (0 registered, 5 rejected) | DeepSeek's model card and release note publish no FrontierCode result. Cognition (relayed by codingfleet) lists DeepSeek V4 Flash 0731 at high effort only (18.8%); AA's 44% is DeepSeek V4.1 Flash, a different version. No max-effort score exists. |
| MiniMax-M3.1-Flash | Bug Hunt Bench | 2026-10-23 | not found | 5 | 2026-10-23: 7 queries, 6 candidates (0 registered, 6 rejected) | Bug Hunt Bench's owner has published no MiniMax-M3.1-Flash run (the model was released 2026-10-19, the board and repo main date from 2026-10-19 12:02 CEST). The provider's launch post and model card carry no Bug Hunt Bench result, so the last-resort provider fill does not exist either. No other party reports a Bug Hunt score for this model: BenchLM shows 'Coming soon'. The repo's only MiniMax files are M2.7 effort-dial probes, a different model version. Limitation: the GitHub API was not reachable for this session (repository not enabled), so open issues or pull requests in the repo could not be listed; the pinned commit's files and the site's benchmark.json were inspected directly. Repeat the search on the next refresh. |
| Claude Haiku 5.5 | Vibe Code Bench v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (90.444), not xhigh; not transferred. |
| Claude Haiku 5.5 (high) | Vibe Code Bench v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (90.444), not high; not transferred. |
| Claude Haiku 5.5 (low) | Vibe Code Bench v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (90.444), not low; not transferred. |
| Claude Haiku 5.5 (medium) | Vibe Code Bench v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (90.444), not medium; not transferred. |
| Claude Opus 5.5 (high) | Vibe Code Bench v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (90.294), not high; not transferred. |
| Claude Opus 5.5 (medium) | Vibe Code Bench v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (90.294), not medium; not transferred. |
| Claude Opus 5.5 (xhigh) | Vibe Code Bench v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (90.294), not xhigh; not transferred. |
| Claude Sonnet 5.5 (xhigh) | Vibe Code Bench v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (92.392), not xhigh; not transferred. |
| GPT-5.6 Luna (low) | Vibe Code Bench v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (77.055), not low; not transferred. |
| GPT-6 Astra (high) | Vibe Code Bench v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (89.594), not high; not transferred. |
| GPT-6 Astra (xhigh) | Vibe Code Bench v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (89.594), not xhigh; not transferred. |
| GPT-6 Luna (high) | Vibe Code Bench v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (81.649), not high; not transferred. |
| GPT-6 Luna (low) | Vibe Code Bench v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (81.649), not low; not transferred. |
| GPT-6 Luna (medium) | Vibe Code Bench v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (81.649), not medium; not transferred. |
| GPT-6 Luna (xhigh) | Vibe Code Bench v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (81.649), not xhigh; not transferred. |
| GPT-6.1 Sol (high) | Vibe Code Bench v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (88.931), not high; not transferred. |
| GPT-6.1 Sol (medium) | Vibe Code Bench v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (88.931), not medium; not transferred. |
| GPT-6.1 Sol (xhigh) | Vibe Code Bench v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (88.931), not xhigh; not transferred. |
| MiMo-V2.6-Flash | Vibe Code Bench v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 1 candidates (0 registered, 1 rejected) | AA plots this model in reasoning mode with no effort label; Vals effort recorded as null (not stated). Vals model page: evaluated 'with reasoning enabled'. |
| MiniMax-M3.1-Flash | Vibe Code Bench v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 1 candidates (0 registered, 1 rejected) | AA plots this model in reasoning mode with no effort label; Vals effort recorded as max. |
| Claude Haiku 5.5 | Code Migration v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (52.360), not xhigh; not transferred. |
| Claude Haiku 5.5 (high) | Code Migration v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (52.360), not high; not transferred. |
| Claude Haiku 5.5 (low) | Code Migration v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (52.360), not low; not transferred. |
| Claude Haiku 5.5 (medium) | Code Migration v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (52.360), not medium; not transferred. |
| Claude Opus 5.5 (high) | Code Migration v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (81.012), not high; not transferred. |
| Claude Opus 5.5 (medium) | Code Migration v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (81.012), not medium; not transferred. |
| Claude Opus 5.5 (xhigh) | Code Migration v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (81.012), not xhigh; not transferred. |
| Claude Sonnet 5.5 (xhigh) | Code Migration v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (86.875), not xhigh; not transferred. |
| GPT-5.6 Luna (low) | Code Migration v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | No codeMigration record for this configuration at its exact effort. |
| GPT-6 Astra (high) | Code Migration v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (80.579), not high; not transferred. |
| GPT-6 Astra (xhigh) | Code Migration v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (80.579), not xhigh; not transferred. |
| GPT-6 Luna (high) | Code Migration v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (46.669), not high; not transferred. |
| GPT-6 Luna (low) | Code Migration v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (46.669), not low; not transferred. |
| GPT-6 Luna (medium) | Code Migration v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (46.669), not medium; not transferred. |
| GPT-6 Luna (xhigh) | Code Migration v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (46.669), not xhigh; not transferred. |
| GPT-6.1 Sol (high) | Code Migration v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (77.324), not high; not transferred. |
| GPT-6.1 Sol (medium) | Code Migration v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (77.324), not medium; not transferred. |
| GPT-6.1 Sol (xhigh) | Code Migration v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | Vals ran this model only at max (77.324), not xhigh; not transferred. |
| MiMo-V2.6-Flash | Code Migration v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 1 candidates (0 registered, 1 rejected) | AA plots this model in reasoning mode with no effort label; Vals effort recorded as null (not stated). Vals model page: evaluated 'with reasoning enabled'. |
| MiniMax-M3.1-Flash | Code Migration v1.1 (Vals) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | No codeMigration record for this configuration at its exact effort. |
| Claude Haiku 5.5 | LiveBench 2.0 Overall | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has one row per model at its highest effort only; this effort is not run. |
| Claude Haiku 5.5 (high) | LiveBench 2.0 Overall | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has one row per model at its highest effort only; this effort is not run. |
| Claude Haiku 5.5 (low) | LiveBench 2.0 Overall | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has one row per model at its highest effort only; this effort is not run. |
| Claude Haiku 5.5 (medium) | LiveBench 2.0 Overall | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has one row per model at its highest effort only; this effort is not run. |
| Claude Opus 5.5 (high) | LiveBench 2.0 Overall | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has one row per model at its highest effort only; this effort is not run. |
| Claude Opus 5.5 (medium) | LiveBench 2.0 Overall | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has one row per model at its highest effort only; this effort is not run. |
| Claude Opus 5.5 (xhigh) | LiveBench 2.0 Overall | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has one row per model at its highest effort only; this effort is not run. |
| Claude Sonnet 5.5 (xhigh) | LiveBench 2.0 Overall | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has one row per model at its highest effort only; this effort is not run. |
| GPT-5.6 Luna (low) | LiveBench 2.0 Overall | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has gpt-5.6-luna at max only (73.6). |
| GPT-6 Astra (high) | LiveBench 2.0 Overall | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has one row per model at its highest effort only; this effort is not run. |
| GPT-6 Astra (xhigh) | LiveBench 2.0 Overall | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has one row per model at its highest effort only; this effort is not run. |
| GPT-6 Luna (high) | LiveBench 2.0 Overall | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has one row per model at its highest effort only; this effort is not run. |
| GPT-6 Luna (low) | LiveBench 2.0 Overall | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has one row per model at its highest effort only; this effort is not run. |
| GPT-6 Luna (medium) | LiveBench 2.0 Overall | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has one row per model at its highest effort only; this effort is not run. |
| GPT-6 Luna (xhigh) | LiveBench 2.0 Overall | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has one row per model at its highest effort only; this effort is not run. |
| GPT-6.1 Sol (high) | LiveBench 2.0 Overall | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has one row per model at its highest effort only; this effort is not run. |
| GPT-6.1 Sol (medium) | LiveBench 2.0 Overall | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has one row per model at its highest effort only; this effort is not run. |
| GPT-6.1 Sol (xhigh) | LiveBench 2.0 Overall | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | LiveBench 2.0 has one row per model at its highest effort only; this effort is not run. |
| MiMo-V2.6-Flash | LiveBench 2.0 Overall | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | No MiMo-V2.6-Flash row in LiveBench 2.0. |
| MiniMax-M3.1-Flash | LiveBench 2.0 Overall | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 1 candidates (0 registered, 1 rejected) | Effort from bundle model metadata (main.074b2ee8.js); single run; 29 tasks. AA plots this model without an effort label (reasoning mode); a source row at one labelled effort is plausible, not exact. |
| Claude Haiku 5.5 | AI Coding Daily (excl. bug finding) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | AICD has Haiku 5.5 Medium/High only. |
| Claude Haiku 5.5 (low) | AI Coding Daily (excl. bug finding) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | AICD has Haiku 5.5 Medium/High only. |
| Claude Haiku 5.5 (max) | AI Coding Daily (excl. bug finding) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | AICD has Haiku 5.5 Medium/High only. |
| Claude Opus 5.5 | AI Coding Daily (excl. bug finding) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | AICD has Opus 5.5 Low/Medium/High only. |
| Claude Opus 5.5 (xhigh) | AI Coding Daily (excl. bug finding) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | AICD has Opus 5.5 Low/Medium/High only. |
| Claude Sonnet 5.5 | AI Coding Daily (excl. bug finding) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | AICD has Sonnet 5.5 Medium/High only. |
| Claude Sonnet 5.5 (xhigh) | AI Coding Daily (excl. bug finding) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | AICD has Sonnet 5.5 Medium/High only. |
| GPT-6 Astra | AI Coding Daily (excl. bug finding) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | AICD has GPT-6-Astra Medium/High only. |
| GPT-6 Astra (xhigh) | AI Coding Daily (excl. bug finding) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | AICD has GPT-6-Astra Medium/High only. |
| GPT-6 Luna (low) | AI Coding Daily (excl. bug finding) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | AICD has GPT-6-Luna Medium/High/Xhigh/Max only. |
| GPT-6.1 Sol | AI Coding Daily (excl. bug finding) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | AICD has GPT-6.1-Sol Low/Medium/High only. |
| GPT-6.1 Sol (xhigh) | AI Coding Daily (excl. bug finding) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 0 candidates (0 registered, 0 rejected) | AICD has GPT-6.1-Sol Low/Medium/High only. |
| MiMo-V2.6-Flash | AI Coding Daily (excl. bug finding) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 1 candidates (0 registered, 1 rejected) | Tested 2026-10-02 with OpenCode; cost/prompt $0.04. AA plots this model without an effort label (reasoning mode); a source row at one labelled effort is plausible, not exact. |
| MiniMax-M3.1-Flash | AI Coding Daily (excl. bug finding) | 2026-10-23 | not found | 1 | 2026-10-23: 4 queries, 1 candidates (0 registered, 1 rejected) | Tested 2026-10-20 with OpenCode; cost/prompt N/A. AA plots this model without an effort label (reasoning mode); a source row at one labelled effort is plausible, not exact. |

## Basket cost components

| Configuration | Component | Cost (USD) | Completeness | Tasks | USD per task | Source |
|---|---|---:|---|---:|---:|---|
| Claude Opus 5.5 (max) | AA-Briefcase | $1,915.18 | confirmed-complete | 91 | $21.0460 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | GDPval-AA | $1,962.05 | confirmed-complete | 220 | $8.9184 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | GDP.pdf | $155.23 | confirmed-complete | 100 | $1.5523 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | AutomationBench-AA | $938.69 | confirmed-complete | 657 | $1.4288 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | Terminal-Bench 4.0 (AA Index run) | $865.21 | confirmed-complete | 66 | $13.1093 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | SciCode | $135.11 | confirmed-complete | 288 | $0.4691 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | AA-LCR | $67.66 | confirmed-complete | 100 | $0.6766 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Opus 5.5 (max) | Coding Agent Index | $3,312.59 | confirmed-complete | — | — | AA Coding Agent Index v2.0 cost to run (mean API cost per task) x 290 tasks |
| Claude Opus 5.5 (max) | ITBench-AA | $146.00 | confirmed-complete | — | — | AA ITBench-AA total cost chart (labels rounded to USD 1) |
| Claude Sonnet 5.5 (max) | AA-Briefcase | $1,863.13 | confirmed-complete | 91 | $20.4739 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | GDPval-AA | $1,504.30 | confirmed-complete | 220 | $6.8377 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | GDP.pdf | $79.43 | confirmed-complete | 100 | $0.7943 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | AutomationBench-AA | $678.32 | confirmed-complete | 657 | $1.0324 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | Terminal-Bench 4.0 (AA Index run) | $834.67 | confirmed-complete | 66 | $12.6464 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | SciCode | $80.07 | confirmed-complete | 288 | $0.2780 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | AA-LCR | $33.93 | confirmed-complete | 100 | $0.3393 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Sonnet 5.5 (max) | Coding Agent Index | $3,857.44 | confirmed-complete | — | — | AA Coding Agent Index v2.0 cost to run (mean API cost per task) x 290 tasks |
| GPT-6.1 Sol (max) | AA-Briefcase | $210.45 | confirmed-complete | 91 | $2.3126 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | GDPval-AA | $196.57 | confirmed-complete | 220 | $0.8935 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | GDP.pdf | $41.99 | confirmed-complete | 100 | $0.4199 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | AutomationBench-AA | $195.01 | confirmed-complete | 657 | $0.2968 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | Terminal-Bench 4.0 (AA Index run) | $120.30 | confirmed-complete | 66 | $1.8228 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | SciCode | $12.50 | confirmed-complete | 288 | $0.0434 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | AA-LCR | $19.94 | confirmed-complete | 100 | $0.1994 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6.1 Sol (max) | Coding Agent Index | $436.35 | confirmed-complete | — | — | AA Coding Agent Index v2.0 cost to run (mean API cost per task) x 290 tasks |
| Claude Haiku 5.5 (max) | AA-Briefcase | $61.41 | confirmed-complete | 91 | $0.6749 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (max) | GDPval-AA | $48.90 | confirmed-complete | 220 | $0.2223 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (max) | GDP.pdf | $5.27 | confirmed-complete | 100 | $0.0527 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (max) | AutomationBench-AA | $27.80 | confirmed-complete | 657 | $0.0423 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (max) | Terminal-Bench 4.0 (AA Index run) | $43.02 | confirmed-complete | 66 | $0.6519 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (max) | SciCode | $3.15 | confirmed-complete | 288 | $0.0109 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (max) | AA-LCR | $1.93 | confirmed-complete | 100 | $0.0193 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Claude Haiku 5.5 (max) | Coding Agent Index | $775.43 | confirmed-complete | — | — | AA Coding Agent Index v2.0 cost to run (mean API cost per task) x 290 tasks |
| GPT-6 Astra (max) | AA-Briefcase | $864.69 | confirmed-complete | 91 | $9.5021 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | GDPval-AA | $996.49 | confirmed-complete | 220 | $4.5295 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | GDP.pdf | $207.58 | confirmed-complete | 100 | $2.0758 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | AutomationBench-AA | $1,048.30 | confirmed-complete | 657 | $1.5956 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | Terminal-Bench 4.0 (AA Index run) | $560.88 | confirmed-complete | 66 | $8.4981 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | SciCode | $66.89 | confirmed-complete | 288 | $0.2323 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | AA-LCR | $99.73 | confirmed-complete | 100 | $0.9973 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Astra (max) | Coding Agent Index | $2,040.49 | confirmed-complete | — | — | AA Coding Agent Index v2.0 cost to run (mean API cost per task) x 290 tasks |
| GPT-6 Astra (max) | ITBench-AA | $133.00 | confirmed-complete | — | — | AA ITBench-AA total cost chart (labels rounded to USD 1) |
| GPT-6 Luna (max) | AA-Briefcase | $15.47 | confirmed-complete | 91 | $0.1700 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | GDPval-AA | $19.66 | confirmed-complete | 220 | $0.0894 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | GDP.pdf | $2.85 | confirmed-complete | 100 | $0.0285 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | AutomationBench-AA | $23.91 | confirmed-complete | 657 | $0.0364 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | Terminal-Bench 4.0 (AA Index run) | $15.59 | confirmed-complete | 66 | $0.2362 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | SciCode | $1.06 | confirmed-complete | 288 | $0.0037 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | AA-LCR | $1.02 | confirmed-complete | 100 | $0.0102 | AA Intelligence Index evaluation cost (cost per task x task count) |
| GPT-6 Luna (max) | Coding Agent Index | $46.16 | confirmed-complete | — | — | AA Coding Agent Index v2.0 cost to run (mean API cost per task) x 290 tasks |
| MiMo-V2.6-Pro | AA-Briefcase | $34.60 | confirmed-complete | 91 | $0.3802 | AA Intelligence Index evaluation cost (cost per task x task count) |
| MiMo-V2.6-Pro | GDPval-AA | $35.47 | confirmed-complete | 220 | $0.1612 | AA Intelligence Index evaluation cost (cost per task x task count) |
| MiMo-V2.6-Pro | GDP.pdf | $2.40 | confirmed-complete | 100 | $0.0240 | AA Intelligence Index evaluation cost (cost per task x task count) |
| MiMo-V2.6-Pro | AutomationBench-AA | $27.77 | confirmed-complete | 657 | $0.0423 | AA Intelligence Index evaluation cost (cost per task x task count) |
| MiMo-V2.6-Pro | Terminal-Bench 4.0 (AA Index run) | $28.91 | confirmed-complete | 66 | $0.4381 | AA Intelligence Index evaluation cost (cost per task x task count) |
| MiMo-V2.6-Pro | SciCode | $2.25 | confirmed-complete | 288 | $0.0078 | AA Intelligence Index evaluation cost (cost per task x task count) |
| MiMo-V2.6-Pro | AA-LCR | $4.74 | confirmed-complete | 100 | $0.0474 | AA Intelligence Index evaluation cost (cost per task x task count) |
| DeepSeek V4.1 Flash 1017 (max) | AA-Briefcase | $61.72 | confirmed-complete | 91 | $0.6783 | AA Intelligence Index evaluation cost (cost per task x task count) |
| DeepSeek V4.1 Flash 1017 (max) | GDPval-AA | $77.91 | confirmed-complete | 220 | $0.3541 | AA Intelligence Index evaluation cost (cost per task x task count) |
| DeepSeek V4.1 Flash 1017 (max) | GDP.pdf | $4.23 | confirmed-complete | 100 | $0.0423 | AA Intelligence Index evaluation cost (cost per task x task count) |
| DeepSeek V4.1 Flash 1017 (max) | AutomationBench-AA | $114.26 | confirmed-complete | 657 | $0.1739 | AA Intelligence Index evaluation cost (cost per task x task count) |
| DeepSeek V4.1 Flash 1017 (max) | Terminal-Bench 4.0 (AA Index run) | $58.09 | confirmed-complete | 66 | $0.8801 | AA Intelligence Index evaluation cost (cost per task x task count) |
| DeepSeek V4.1 Flash 1017 (max) | SciCode | $4.65 | confirmed-complete | 288 | $0.0161 | AA Intelligence Index evaluation cost (cost per task x task count) |
| DeepSeek V4.1 Flash 1017 (max) | AA-LCR | $3.26 | confirmed-complete | 100 | $0.0326 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 4 Argon (high) | AA-Briefcase | $530.33 | confirmed-complete | 91 | $5.8277 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 4 Argon (high) | GDPval-AA | $400.23 | confirmed-complete | 220 | $1.8192 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 4 Argon (high) | GDP.pdf | $25.93 | confirmed-complete | 100 | $0.2593 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 4 Argon (high) | AutomationBench-AA | $399.89 | confirmed-complete | 657 | $0.6087 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 4 Argon (high) | Terminal-Bench 4.0 (AA Index run) | $447.49 | confirmed-complete | 66 | $6.7801 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 4 Argon (high) | SciCode | $30.44 | confirmed-complete | 288 | $0.1057 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 4 Argon (high) | AA-LCR | $23.64 | confirmed-complete | 100 | $0.2364 | AA Intelligence Index evaluation cost (cost per task x task count) |
| Gemini 4 Argon (high) | Coding Agent Index | $1,699.83 | confirmed-complete | — | — | AA Coding Agent Index v2.0 cost to run (mean API cost per task) x 290 tasks |

### AA Index total reconciliation

The seven Index components plus AA's residual reproduce AA's published Intelligence Index total cost.

| Configuration | Index SDLC components | Residual | Reconstructed total | Published total | Reconciled |
|---|---:|---:|---:|---:|---|
| Claude Opus 5.5 (max) | $6,039.13 | $2,669.07 | $8,708.20 | $8,708.20 | yes |
| Claude Sonnet 5.5 (max) | $5,073.84 | $2,185.66 | $7,259.50 | $7,259.50 | yes |
| GPT-6.1 Sol (max) | $796.76 | $284.79 | $1,081.55 | $1,081.55 | yes |
| Claude Haiku 5.5 (max) | $191.49 | $138.76 | $330.25 | $330.25 | yes |
| GPT-6 Astra (max) | $3,844.56 | $1,479.54 | $5,324.10 | $5,324.10 | yes |
| GPT-6 Luna (max) | $79.56 | $42.49 | $122.05 | $122.05 | yes |
| MiMo-V2.6-Pro | $136.13 | $70.53 | $206.66 | $206.66 | yes |
| DeepSeek V4.1 Flash 1017 (max) | $324.12 | $120.48 | $444.60 | $444.60 | yes |
| Gemini 4 Argon (high) | $1,857.94 | $549.30 | $2,407.24 | $2,407.24 | yes |

## DeepSWE v1.1 AA chart configurations (withdrawn by AA, not scored)

AA withdrew DeepSWE v1.1 from its Coding Agent Index (v2.0, October 2026) and the owner dropped it as a quality leaf in favour of FrontierCode (O49); this is AA's last capture, kept for the record. The AA chart published 42 DeepSWE v1.1 configurations across 113 tasks, observed 2026-10-17T19:26:26Z. Each keeps its displayed agent, model and effort; only exact matches enter a score.

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

23 official rows (13 of 51 cohort matches), observed 2026-10-23T05:35:48Z. The published ± is the source's 95% confidence interval (used by stream S1M). Since O37 the Terminal-Bench leaf is AA's own run; these rows cross-check it and fill a gap. Matched agents for cohort rows, in the registered preference order (E225): Claude Code 2, Codex 3.

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
| 12 | GLM-5.3-Flash | Claude Code | 35.8% ± 3.5% | 2.9B | $100 |
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

Owner-published runs at commit `46802fc312b6fd467b0baee519df05693f120232`; the score is the owner's largest-sample mean of bugs fixed of 105 for the exact model and effort, with the harness that result was run on (E206). Cross-harness results at the same effort (E224, diagnostic): DeepSeek V4.1 Flash 1017: Claude Code / DeepSeek API 39.1 (7 runs), DeepSeek Harness / DeepSeek API 42.7 (7 runs), OpenCode / DeepSeek API 37.6 (5 runs), Pi / DeepSeek API 42.2 (5 runs); Gemini 4 Argon: Antigravity CLI 40.7 (3 runs), Gemini CLI 33.0 (1 run).

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
| DeepSeek V4.1 Flash 1017 | DeepSeek V4.1 Flash 1017 (max effort, DeepSeek Harness) - mean of 7 | 42.7 | 7 | max | DeepSeek Harness / DeepSeek API |
| GPT-6 Luna (low) | GPT-6 Luna (low effort) | 4.0 | 1 | low | Codex CLI |
| GPT-6 Luna (medium) | GPT-6 Luna (medium effort) | 4.0 | 1 | medium | Codex CLI |
| GPT-6 Luna (high) | GPT-6 Luna (high effort) | 9.0 | 1 | high | Codex CLI |
| GPT-6 Luna (xhigh) | GPT-6 Luna (xhigh effort) | 14.0 | 1 | xhigh | Codex CLI |
| Claude Opus 5.5 (high) | Opus 5.5 (high effort) - mean of 3 | 31.7 | 3 | high | Claude Code |
| Claude Opus 5.5 (xhigh) | Opus 5.5 (xhigh effort) - mean of 3 | 36.0 | 3 | xhigh | Claude Code |
| Claude Opus 5.5 (medium) | Opus 5.5 (medium effort) - mean of 3 | 30.3 | 3 | medium | Claude Code |
| GPT-5.6 Luna (low) | GPT-5.6 Luna (low effort) | 4.0 | 1 | low | Codex CLI |
| GPT-6 Astra (high) | GPT-6 Astra (high effort) | 35.0 | 1 | high | Codex CLI |
| GPT-6 Astra (xhigh) | GPT-6 Astra (xhigh effort) | 43.0 | 1 | xhigh | Codex CLI |

## Plan routes

Route evidence as of 2026-10-08. Full allocation regimes, workloads and notes are in [data/plan_cost_routes.json](data/plan_cost_routes.json).

| Plan | Eligible configurations | Monthly fee | Value Multiple | Evidence | Source model | Source date | Source |
|---|---|---:|---:|---|---|---|---|
| ChatGPT Plus $20 · GPT-6.1 Sol | GPT-6.1 Sol | $20.00 | 10.55× | Controlled account measurement / workload projection | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · GPT-6 Astra | GPT-6 Astra | $20.00 | 8.1× | Controlled account measurement / workload projection | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-5.6 Sol | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-5.6 Luna | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-5.5 | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6 Sol | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6 Luna | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6.1 Sol (xhigh) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6.1 Sol (high) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6.1 Sol (medium) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6.1 Sol (low) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · GPT-6.1 Sol | GPT-6.1 Sol | $100.00 | 10.55× | Controlled account measurement / workload projection | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · GPT-6 Astra | GPT-6 Astra | $100.00 | 13.22× | Controlled account measurement / workload projection | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-5.6 Sol | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-5.6 Luna | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-5.5 | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6 Sol | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6 Luna | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6.1 Sol (xhigh) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6.1 Sol (high) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6.1 Sol (medium) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6.1 Sol (low) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · GPT-6.1 Sol | GPT-6.1 Sol | $200.00 | 10.42× | Controlled account measurement / workload projection | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · GPT-6 Astra | GPT-6 Astra | $200.00 | 14.485× | Controlled account measurement / workload projection | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-5.6 Sol | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-5.6 Luna | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-5.5 | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6 Sol | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6 Luna | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6.1 Sol (xhigh) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6.1 Sol (high) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6.1 Sol (medium) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6.1 Sol (low) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · GPT-6.1 Sol | GPT-6.1 Sol | $500.00 | 10.772× | Controlled account measurement / workload projection | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · GPT-6 Astra | GPT-6 Astra | $500.00 | 13.91× | Controlled account measurement / workload projection | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-5.6 Sol | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-5.6 Luna | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-5.5 | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6 Sol | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6 Luna | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6.1 Sol (xhigh) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6.1 Sol (high) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6.1 Sol (medium) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6.1 Sol (low) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · Opus 5.5 | Claude Opus 5.5 | $20.00 | 58.9× | Controlled account measurement / workload projection | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max $100 · Opus 5.5 | Claude Opus 5.5 | $100.00 | 57.25× | Controlled account measurement / workload projection | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max $200 · Opus 5.5 | Claude Opus 5.5 | $200.00 | 58.63× | Controlled account measurement / workload projection | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max $100 · Fable 5.1 | Claude Fable 5.1 | $100.00 | 12.73× | Controlled account measurement / workload projection | Fable 5.1 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max $200 · Fable 5.1 | Claude Fable 5.1 | $200.00 | 12.425× | Controlled account measurement / workload projection | Fable 5.1 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| SuperGrok Heavy $300 · Grok 4.7 XHigh | Grok 4.7 | $300.00 | 5.785× | user reported projection | Grok 4.7 XHigh | 2026-09-25 | [Source](https://www.remakebench.com/capacity/plans/supergrok-heavy) |
| MiMo Token Plan Lite $6 · quota ceiling (provider-derived) | MiMo-V2.6-Pro | $6.00 | 0.984× | Provider quota ceiling (owner decision O46; not a measurement) | — | 2026-10-21 | [Source](https://mimo.mi.com/docs/en-US/price/token-plan) |
| MiMo Token Plan Standard $16 · quota ceiling (provider-derived) | MiMo-V2.6-Pro | $16.00 | 0.99× | Provider quota ceiling (owner decision O46; not a measurement) | — | 2026-10-21 | [Source](https://mimo.mi.com/docs/en-US/price/token-plan) |
| MiMo Token Plan Pro $50 · quota ceiling (provider-derived) | MiMo-V2.6-Pro | $50.00 | 1.0944× | Provider quota ceiling (owner decision O46; not a measurement) | — | 2026-10-21 | [Source](https://mimo.mi.com/docs/en-US/price/token-plan) |
| MiMo Token Plan Max $100 · quota ceiling (provider-derived) | MiMo-V2.6-Pro | $100.00 | 1.1808× | Provider quota ceiling (owner decision O46; not a measurement) | — | 2026-10-21 | [Source](https://mimo.mi.com/docs/en-US/price/token-plan) |
| MiMo Token Plan Lite $6 · quota ceiling (provider-derived) | MiMo-V2.6-Flash | $6.00 | 0.9567× | Provider quota ceiling (owner decision O46; not a measurement) | — | 2026-10-21 | [Source](https://mimo.mi.com/docs/en-US/price/token-plan) |
| MiMo Token Plan Standard $16 · quota ceiling (provider-derived) | MiMo-V2.6-Flash | $16.00 | 0.9625× | Provider quota ceiling (owner decision O46; not a measurement) | — | 2026-10-21 | [Source](https://mimo.mi.com/docs/en-US/price/token-plan) |
| MiMo Token Plan Pro $50 · quota ceiling (provider-derived) | MiMo-V2.6-Flash | $50.00 | 1.064× | Provider quota ceiling (owner decision O46; not a measurement) | — | 2026-10-21 | [Source](https://mimo.mi.com/docs/en-US/price/token-plan) |
| MiMo Token Plan Max $100 · quota ceiling (provider-derived) | MiMo-V2.6-Flash | $100.00 | 1.148× | Provider quota ceiling (owner decision O46; not a measurement) | — | 2026-10-21 | [Source](https://mimo.mi.com/docs/en-US/price/token-plan) |
| Claude Pro $20 · common Claude assumption | Claude Opus 5 | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | Claude Fable 5 | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | Claude Opus 4.8 | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | Claude Sonnet 5 | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | Claude Haiku 5.5 | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | Claude Sonnet 5.5 | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | Claude Haiku 5.5 (max) | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | Claude Haiku 5.5 (high) | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | Claude Haiku 5.5 (medium) | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | Claude Haiku 5.5 (low) | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | Claude Sonnet 5.5 (xhigh) | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | Claude Sonnet 5.5 (high) | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | Claude Sonnet 5.5 (medium) | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | Claude Sonnet 5.5 (low) | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Opus 5 | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Fable 5 | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Opus 4.8 | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Sonnet 5 | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Haiku 5.5 | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Sonnet 5.5 | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Haiku 5.5 (max) | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Haiku 5.5 (high) | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Haiku 5.5 (medium) | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Haiku 5.5 (low) | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Sonnet 5.5 (xhigh) | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Sonnet 5.5 (high) | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Sonnet 5.5 (medium) | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Sonnet 5.5 (low) | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Opus 5 | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Fable 5 | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Opus 4.8 | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Sonnet 5 | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Haiku 5.5 | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Sonnet 5.5 | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Haiku 5.5 (max) | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Haiku 5.5 (high) | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Haiku 5.5 (medium) | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Haiku 5.5 (low) | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Sonnet 5.5 (xhigh) | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Sonnet 5.5 (high) | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Sonnet 5.5 (medium) | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Sonnet 5.5 (low) | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | Claude Opus 5.5 (high) | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Opus 5.5 (high) | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Opus 5.5 (high) | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | Claude Opus 5.5 (xhigh) | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Opus 5.5 (xhigh) | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Opus 5.5 (xhigh) | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Pro $20 · common Claude assumption | Claude Opus 5.5 (medium) | $20.00 | 58.9× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 5x $100 · common Claude assumption | Claude Opus 5.5 (medium) | $100.00 | 57.25× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| Claude Max 20x $200 · common Claude assumption | Claude Opus 5.5 (medium) | $200.00 | 58.63× | Provisional assumption | Opus 5.5 | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6 Luna (low) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6 Luna (low) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6 Luna (low) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6 Luna (low) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6 Luna (medium) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6 Luna (medium) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6 Luna (medium) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6 Luna (medium) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6 Luna (high) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6 Luna (high) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6 Luna (high) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6 Luna (high) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6 Luna (xhigh) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6 Luna (xhigh) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6 Luna (xhigh) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6 Luna (xhigh) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6 Astra (high) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6 Astra (high) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6 Astra (high) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6 Astra (high) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-6 Astra (xhigh) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-6 Astra (xhigh) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-6 Astra (xhigh) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-6 Astra (xhigh) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Plus $20 · common GPT assumption | GPT-5.6 Luna (low) | $20.00 | 8.1× | Provisional assumption | GPT-6 Astra | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 100 $100 · common GPT assumption | GPT-5.6 Luna (low) | $100.00 | 10.55× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 200 $200 · common GPT assumption | GPT-5.6 Luna (low) | $200.00 | 10.42× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |
| ChatGPT Pro 500 $500 · common GPT assumption | GPT-5.6 Luna (low) | $500.00 | 10.772× | Provisional assumption | GPT-6.1 Sol | 2026-10-06 | [Source](https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x) |

### Plan amounts and their lineage

Each routed row's amount with what it measures, how it was derived and which objects it comes from (E166, E168); API-fallback rows have none.

| Configuration | Amount (USD per fee period) | Measures | Derivation | Workload | Cash object | Measurement object |
|---|---:|---|---|---|---|---|
| Claude Sonnet 5.5 (max) | $1,178 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | claude-pro-claude-sonnet-5-5-common-opus55-assumption:month cash | claude-pro-claude-sonnet-5-5-common-opus55-assumption |
| Claude Opus 5.5 (max) | $1,178 | measured-workload capacity | measurement record: its recorded numerator U_obs = M_obs x F_obs (workload capacity projection) | the route's measurement workload | claude-pro-opus55-semianalysis:month cash | claude-pro-opus55-semianalysis |
| GPT-6.1 Sol (max) | $5,386 | measured-workload capacity | measurement record: its recorded numerator U_obs = M_obs x F_obs (workload capacity projection) | the route's measurement workload | chatgpt-pro500-gpt61sol-semianalysis:month cash | chatgpt-pro500-gpt61sol-semianalysis |
| GPT-6 Astra (max) | $2,897 | measured-workload capacity | measurement record: its recorded numerator U_obs = M_obs x F_obs (workload capacity projection) | the route's measurement workload | chatgpt-pro200-gpt6astra-semianalysis:month cash | chatgpt-pro200-gpt6astra-semianalysis |
| MiMo-V2.6-Pro | $118 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | mimo-tokenplan-max-mimo-v2-6-pro-quota-ceiling:month cash | mimo-tokenplan-max-mimo-v2-6-pro-quota-ceiling |
| Claude Haiku 5.5 (max) | $1,178 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | claude-pro-claude-haiku-5-5-max-common-opus55-assumption:month cash | claude-pro-claude-haiku-5-5-max-common-opus55-assumption |
| GPT-6 Luna (max) | $5,386 | assumed consumption | authorised assumption: the donor's multiple times this route's cash | the route's measurement workload | chatgpt-pro500-gpt-6-luna-common-gpt-assumption:month cash | chatgpt-pro500-gpt-6-luna-common-gpt-assumption |

## Evidence bundle

Bundle hash `754b577ee9e79b1133c48a5c9ef1fcdb6ac018789e9bca16d88f43029de9057b`: every published output is rebuilt from these artifacts at the pinned publication clock (npm run verify:docs), never from live pages.

| Key | Artifact | SHA-256 | Captured | Extractor |
|---|---|---|---|---|
| snapshot | `data/aa/aa_v432_snapshot.json` | `d572e37ee84df0a7f2ed7564acda9ebd31a726026821536a6c604208dae21d1e` | 2026-10-23T06:26:23Z | valuerank.capture_aa |
| bugHunt | `data/bug_hunt.json` | `c1fd0c80ebaf26aa57cb8f28ecd1009ac21724b29779f01078c04ef2c14c1827` | 2026-10-19 | editorial capture of the owner's published results (source commit recorded) |
| tb4 | `data/tb4.json` | `dee07f85c6286fa8a94b5205b539fb5c8929b7d72e240ff1ee525dd542fe96e5` | 2026-10-23T05:35:48Z | scripts/scrape-tb4.js, then valuerank.build_tb4 |
| codingAgents | `data/aa/coding_agents_capture.json` | `5babadfe73b2631e5d89554100f8b2186dd74f663618b2dd0f963d5d2bca4b88` | 2026-10-23T05:31:41Z | valuerank.capture_coding_agents |
| costCharts | `data/aa/cost_charts_capture.json` | `9c000c036842409d8de48163bd77ff2e64a18a8ac2a1562760ad368472c8ed80` | 2026-10-23T05:35:10.660Z | scripts/capture-aa-cost-charts.js |
| configurationMap | `data/v3_configuration_map.json` | `7b1b1020333c7a5056bc1b1e29d54bb70b65c278c24ed59ffb6a0e7770cb82a7` | 2026-10-23 | editorial pinning from the research capture |
| frontierCapture | `data/aa_frontier_capture.json` | `5bf1cf99ab60f97a5c250638a3001cad2f268df6b8e3cc13f44038ded361fb61` | — | browser capture of AA's Intelligence Index vs cost chart from public tooltips (frontier membership, E195; unevaluated cheaper siblings, E201) |
| roster | `data/aa_mapping.json` | `c5a3a57c71a093fed39353f1ccc18a6583b8bb2392964775ef802e6e78f5fd6f` | — | editorial roster: every configuration AA plots on its rendered frontier or within 3 Index points of it (O51) |
| bugHuntScoreboard | `data/bug_hunt_scoreboard.json` | `094855a7ca761618645c2da1c6c006190d97e77c1b1bce7a7bb5630f60a0862a` | 2026-10-23T05:37:06Z | the owner's combined scoreboard at the pinned commit (O31 roster check) |
| planRoutes | `data/plan_cost_routes.json` | `88c797a0f5fae2eb81c054a89beaba4d5c8db2d1f96e9f4c2006d88359b5293c` | 2026-10-08 | editorial Plan evidence registry |
| priceRecords | `data/price_records.json` | `9be099828d530cc4ad2294d6fdf6ff03a3d94cc5530e8d6ef3279133491930bd` | 2026-10-23T06:26:23Z | editorial E141 price-record registry (superseded and promotional tariffs) |
| leafEvidence | `data/leaf_evidence.json` | `8e61c9affd4bd352c14a2f01d0fcfe4665130ae10574b50a74fa1e4c48979eb4` | 2026-10-23 | editorial supplementary leaf evidence and the exhaustive-search log (O36) |
| cognitionFrontierCode | `data/cognition_frontiercode.json` | `ff0040778b7bdf69c705ad7474f771fb5e53cfaf5cf8573b3a4614153543d75f` | — | Cognition's FrontierCode leaderboard data (https://cognition.com/data/frontiercode-leaderboard/data.json), captured unchanged (O37) |
| sweTracks | `data/swe_tracks.json` | `1d66d2883af192b64dc43d612aee12bcd01907db1445ec167760cf0abb9fa460` | 2026-10-23T07:58:31Z | research/2026-10-23-swe-benchmarks/build_swe_tracks.py from the verified coverage captures (O53-O55) |
| anchors | `data/v3_frozen.json` | `6ede665b54495d1e1d1f75a4c46625eb719df6c1d024a4228e39ed0027735a13` | 2026-10-23 | valuerank.value_v3 freeze |
| anchors:aicd | `data/v3_frozen_aicd.json` | `bbd1b7f12d54e6dd7d13a0a96cc8314557bf6df2bd1abffc14769faf403af13c` | 2026-10-23 | valuerank.value_v3 freeze |


## AA intelligence and total-cost comparison

Observed 2026-10-23T05:27:39Z; Artificial Analysis Intelligence Index v4.3.2. Scope: Complete displayed intelligence versus total evaluation cost Pareto line with all 697 catalog models selected; 189 eligible plotted points, every one read from its public tooltip. This is not ValueRank's composite-quality frontier.. Reconciliation: reconciled. This view compares AA intelligence index with AA total evaluation cost in USD. Primary composite-rank eligibility is shown separately. Membership is AA's directly observed displayed frontier; no frontier is recomputed from these rows. Source selected 697 models, plotted 189 eligible points, and displayed 18 frontier points. Public metric/export gaps are shown explicitly. All 7 distinct frontier model families are required in the main ranking using exact selected configurations; 5 are included. Other effort configurations remain separate comparison entries. 11 plotted configurations from 8 families lie within 3 Index points of the rendered frontier; 5 of those families are in the main ranking, 0 are deferred.

| Exact AA model | AA ID | Intelligence index | Total evaluation cost (USD) | Observed comparison | Primary rank status | Primary evidence gaps |
|---|---|---|---|---|---|---|
| [GPT-6 Luna (low)](https://artificialanalysis.ai/models/gpt-6-luna-low) | gpt-6-luna-low | 22 (rounded) | $10.63 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [GPT-6 Luna (medium)](https://artificialanalysis.ai/models/gpt-6-luna-medium) | gpt-6-luna-medium | 30 (rounded) | $31.17 | Observed AA frontier | Primary ranked | None |
| [GPT-6 Luna (high)](https://artificialanalysis.ai/models/gpt-6-luna-high) | gpt-6-luna-high | 33 (rounded) | $47.85 | Observed AA frontier | Primary ranked | None |
| [Claude Haiku 5.5 (medium)](https://artificialanalysis.ai/models/claude-haiku-5-5-medium) | claude-haiku-5-5-medium | 34 (rounded) | $56.36 | Observed AA frontier | Primary ranked | None |
| [GPT-6 Luna (xhigh)](https://artificialanalysis.ai/models/gpt-6-luna-xhigh) | gpt-6-luna-xhigh | 35 (rounded) | $66.81 | Observed AA frontier | Primary ranked | None |
| [Claude Haiku 5.5 (high)](https://artificialanalysis.ai/models/claude-haiku-5-5-high) | claude-haiku-5-5-high | 38 (rounded) | $94.07 | Observed AA frontier | Primary ranked | None |
| [MiMo-V2.6-Flash](https://artificialanalysis.ai/models/mimo-v2-6-flash) | mimo-v2-6-flash | 38 (rounded) | $109.55 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Bug Hunt Bench, Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no Bug Hunt Bench, AI Coding Daily (excl. bug finding) |
| [GPT-6 Luna (max)](https://artificialanalysis.ai/models/gpt-6-luna) | gpt-6-luna | 38 (rounded) | $122.05 | Observed AA frontier | Primary ranked | None |
| [Claude Haiku 5.5 (xhigh)](https://artificialanalysis.ai/models/claude-haiku-5-5-xhigh) | claude-haiku-5-5-xhigh | 41 (rounded) | $157.58 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [MiMo-V2.6-Pro](https://artificialanalysis.ai/models/mimo-v2-6-pro) | mimo-v2-6-pro | 46 (rounded) | $206.66 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (medium)](https://artificialanalysis.ai/models/gpt-6-1-sol-medium) | gpt-6-1-sol-medium | 48 (rounded) | $361.37 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (high)](https://artificialanalysis.ai/models/gpt-6-1-sol-high) | gpt-6-1-sol-high | 50 (rounded) | $521.32 | Observed AA frontier | Primary ranked | None |
| [GPT-6.1 Sol (xhigh)](https://artificialanalysis.ai/models/gpt-6-1-sol-xhigh) | gpt-6-1-sol-xhigh | 51 (rounded) | $662.28 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [GPT-6.1 Sol (max)](https://artificialanalysis.ai/models/gpt-6-1-sol) | gpt-6-1-sol | 52 (rounded) | $1,081.55 | Observed AA frontier | Primary ranked | None |
| [Claude Opus 5.5 (high with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-high) | claude-opus-5-5-high | 54 (rounded) | $2,172.43 | Observed AA frontier | Primary ranked | None |
| [Claude Opus 5.5 (xhigh with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-xhigh) | claude-opus-5-5-xhigh | 56 (rounded) | $4,056.65 | Observed AA frontier | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [Claude Sonnet 5.5 (max with fallback)](https://artificialanalysis.ai/models/claude-sonnet-5-5) | claude-sonnet-5-5 | 56 (rounded) | $7,259.50 | Observed AA frontier | Primary ranked | None |
| [Claude Opus 5.5 (max with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5) | claude-opus-5-5 | 58 (rounded) | $8,708.20 | Observed AA frontier | Primary ranked | None |
| [GPT-5.6 Luna (low)](https://artificialanalysis.ai/models/gpt-5-6-luna-low) | gpt-5-6-luna-low | 21 (rounded) | $27.02 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Claude Haiku 5.5 (low)](https://artificialanalysis.ai/models/claude-haiku-5-5-low) | claude-haiku-5-5-low | 29 (rounded) | $34.31 | Near AA frontier (within 3 Index points) | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [MiniMax-M3.1-Flash](https://artificialanalysis.ai/models/minimax-m3-1-flash) | minimax-m3-1-flash | 43 (rounded) | $283.18 | Near AA frontier (within 3 Index points) | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Bug Hunt Bench, Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no Bug Hunt Bench, AI Coding Daily (excl. bug finding) |
| [Claude Haiku 5.5 (max)](https://artificialanalysis.ai/models/claude-haiku-5-5) | claude-haiku-5-5 | 43 (rounded) | $330.25 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [DeepSeek V4.1 Flash 1017 (max)](https://artificialanalysis.ai/models/deepseek-v4-1-flash-1017) | deepseek-v4-1-flash-1017 | 45 (rounded) | $444.60 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Claude Opus 5.5 (medium with fallback)](https://artificialanalysis.ai/models/claude-opus-5-5-medium) | claude-opus-5-5-medium | 51 (rounded) | $1,626.81 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [Claude Sonnet 5.5 (xhigh with fallback)](https://artificialanalysis.ai/models/claude-sonnet-5-5-xhigh) | claude-sonnet-5-5-xhigh | 52 (rounded) | $2,176.82 | Near AA frontier (within 3 Index points) | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [Gemini 4 Argon (high)](https://artificialanalysis.ai/models/gemini-4-argon) | gemini-4-argon | 53 (rounded) | $2,407.24 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [GPT-6 Astra (high)](https://artificialanalysis.ai/models/gpt-6-astra-high) | gpt-6-astra-high | 51 (rounded) | $2,925.01 | Near AA frontier (within 3 Index points) | Primary ranked | None |
| [GPT-6 Astra (xhigh)](https://artificialanalysis.ai/models/gpt-6-astra-xhigh) | gpt-6-astra-xhigh | 52 (rounded) | $3,802.98 | Near AA frontier (within 3 Index points) | Unranked: incomplete benchmark evidence (O36) | Incomplete benchmark evidence after an exhaustive search (O36, O53): Max-effort ranking: no Vibe Code Bench v1.1 (Vals), Code Migration v1.1 (Vals), LiveBench 2.0 Overall; AI Coding Daily ranking: no AI Coding Daily (excl. bug finding) |
| [GPT-6 Astra (max)](https://artificialanalysis.ai/models/gpt-6-astra) | gpt-6-astra | 53 (rounded) | $5,324.10 | Near AA frontier (within 3 Index points) | Primary ranked | None |
