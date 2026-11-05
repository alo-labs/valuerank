# Bug Hunt Bench, rescored: planted plus unplanted bugs fixed (O163)

Source: the pinned capture of Bug Hunt Bench (https://github.com/phuryn/bug-hunt-bench), board updated 2026-10-27, read 2026-11-01T05:59:30Z (`research/2026-11-01-recapture/third-party/bughunt/benchmark.json`).

**Score** = planted bugs fixed (of 105, the board's own score) + genuine unplanted bugs fixed (the board's "extras": real defects the model fixed that nobody planted, verified by the board's blind judge), at equal weight, as a plain sum (owner decision O163). Partial and claimed-only fixes do not count. Rows that average several runs use the board's per-run means for both counts. The board itself scores planted bugs only and lists extras separately, because unplanted fixes have no answer key or ceiling; this table departs from it on purpose.

Ranked: the board's 133 live rows (one per model, harness and effort; competition ranks, equal scores share the better rank). Its 74 superseded rows, earlier single runs since replaced by a mean of replicates or a re-run, are listed after the ranking. "Planted rank" is the row's rank on planted bugs alone among the same live rows. Cost is the board's figure for the run (list-rate estimate, bill, floor or free, as it labels it).

| Rank | Board row | Vendor | Harness | Effort | Runs | Planted | Unplanted | **Total** | Planted rank | Cost |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---|
| 1 | GPT-6.1 Sol (max effort) - mean of 3 | OpenAI | Codex CLI | max | 3 | 44.3 | 65.3 | **109.6** | 3 | $5.88 (list) |
| 2 | GPT-6 Astra (max effort) - mean of 3 | OpenAI | Codex CLI | max | 3 | 45 | 55 | **100** | 2 | $33.03 (list) |
| 3 | GPT-6.1 Sol (xhigh effort) - mean of 3 | OpenAI | Codex CLI | xhigh | 3 | 42.7 | 56.7 | **99.4** | 7 | $4.35 (list) |
| 4 | GPT-5.6 Sol (xhigh effort) | OpenAI | Codex CLI | xhigh | 1 | 39 | 59 | **98** | 19 | $52.75 (list) |
| 5 | GPT-6 Astra (xhigh effort) | OpenAI | Codex CLI | xhigh | 1 | 43 | 53 | **96** | 5 | $24.22 (list) |
| 6 | GPT-5.6 Sol (max effort) - mean of 2 | OpenAI | Codex CLI | max | 2 | 43.5 | 48.5 | **92** | 4 | $95.35 (list) |
| 7 | GPT-6.1 Terra (max effort) - mean of 3 | OpenAI | Codex CLI | max | 3 | 40.7 | 48 | **88.7** | 13 | $3.88 (list) |
| 8 | DeepSeek V4.1 Flash 1017 (max effort, DeepSeek Harness) - mean of 7 | DeepSeek | DeepSeek Harness / DeepSeek API | max | 7 | 42.7 | 44 | **86.7** | 7 | $1.84 (bill) |
| 9 | GPT-5.6 Luna (max effort) - mean of 3 | OpenAI | Codex CLI | max | 3 | 31.3 | 54.7 | **86** | 41 | $3.15 (list) |
| 10 | DeepSeek V4.1 Flash 1017 (max effort, Pi) - mean of 5 | DeepSeek | Pi / DeepSeek API | max | 5 | 42.2 | 41.8 | **84** | 9 | $0.83 (bill) |
| 11 | DeepSeek V4.1 Flash 1017 (high effort, DeepSeek Harness) - mean of 5 | DeepSeek | DeepSeek Harness / DeepSeek API | high | 5 | 39.2 | 43.8 | **83** | 17 | $1.27 (bill) |
| 12 | Muse Wonder Full 1.0 (max effort, Muse Code, Meta API) - mean of 2 | Meta | Muse Code / Meta API | max | 2 | 42 | 36.5 | **78.5** | 10 | — |
| 13 | Sonnet 5.5 (max effort) - mean of 3 | Anthropic | Claude Code | max | 3 | 51.3 | 26.3 | **77.6** | 1 | $154.03 (list) |
| 14 | GPT-5.6 Terra (max effort) | OpenAI | Codex CLI | max | 1 | 32 | 45 | **77** | 38 | $27.98 (list) |
| 15 | GPT-6.1 Sol (high effort) - mean of 2 | OpenAI | Codex CLI | high | 2 | 36.5 | 40 | **76.5** | 22 | $3.26 (list) |
| 16 | GPT-5.6 Luna (xhigh effort) | OpenAI | Codex CLI | xhigh | 1 | 23 | 53 | **76** | 63 | $2.50 (list) |
| 17 | GPT-6 Astra (high effort) | OpenAI | Codex CLI | high | 1 | 35 | 40 | **75** | 28 | $20.60 (list) |
| 18 | DeepSeek V4.1 Flash 1017 (max effort, OpenCode) - mean of 5 | DeepSeek | OpenCode / DeepSeek API | max | 5 | 37.6 | 36.2 | **73.8** | 20 | $0.96 (bill) |
| 19 | GPT-6 Sol (max effort) - mean of 3 | OpenAI | Codex CLI | max | 3 | 29.3 | 41.3 | **70.6** | 44 | $9.33 (list) |
| 20 | DeepSeek V4.1 Flash 1017 (high effort, Pi) - mean of 5 | DeepSeek | Pi / DeepSeek API | high | 5 | 40.4 | 29.4 | **69.8** | 15 | $0.64 (bill) |
| 21 | DeepSeek V4.1 Flash 1017 (low effort, DeepSeek Harness) - mean of 5 | DeepSeek | DeepSeek Harness / DeepSeek API | low | 5 | 34.8 | 34.4 | **69.2** | 29 | $1.06 (bill) |
| 22 | GPT-6 Astra (medium effort) | OpenAI | Codex CLI | medium | 1 | 34 | 33 | **67** | 32 | $15.78 (list) |
| 23 | Muse Wonder Full 1.0 (xhigh effort, Muse Code, Meta API) - mean of 2 | Meta | Muse Code / Meta API | xhigh | 2 | 41.5 | 24.5 | **66** | 12 | — |
| 24 | Kimi K3.1 Pro (max effort, Moonshot API) - mean of 3 | Moonshot AI | Claude Code / Moonshot API | max | 3 | 36 | 29.3 | **65.3** | 24 | $13.76 (bill) |
| 25 | DeepSeek V4.1 Flash 1017 (high effort, OpenCode) - mean of 5 | DeepSeek | OpenCode / DeepSeek API | high | 5 | 36.6 | 25.6 | **62.2** | 21 | $0.79 (bill) |
| 26 | DeepSeek V4.1 Flash 1017 (max effort) - mean of 7 | DeepSeek | Claude Code / DeepSeek API | max | 7 | 39.1 | 22.9 | **62** | 18 | $1.01 (bill) |
| 26 | GPT-5.6 Sol (re-run Jul 31) | OpenAI | Codex CLI | high | 1 | 34 | 28 | **62** | 32 | $33.92 (list) |
| 28 | Grok 4.7 (xhigh) - mean of 5 | xAI | Grok Build CLI (ACP) | xhigh | 5 | 29 | 32.2 | **61.2** | 45 | $22.96 (floor) |
| 29 | DeepSeek V4.1 Flash 1017 (high effort) - mean of 5 | DeepSeek | Claude Code / DeepSeek API | high | 5 | 36.4 | 24.4 | **60.8** | 23 | $0.82 (bill) |
| 30 | GPT-6.1 Sol (medium effort) - mean of 2 | OpenAI | Codex CLI | medium | 2 | 29 | 30.5 | **59.5** | 45 | $1.76 (list) |
| 31 | Muse Spark 1.3 (max effort, Muse Code, Meta API) - mean of 5 | Meta | Muse Code / Meta API | max | 5 | 32.2 | 24 | **56.2** | 37 | $18.11 (list) |
| 32 | Fable 5.1 (max effort) | Anthropic | Claude Code | max | 1 | 43 | 11 | **54** | 5 | $87.18 (list) |
| 33 | DeepSeek V4.1 Flash 1017 (low effort, Pi) - mean of 5 | DeepSeek | Pi / DeepSeek API | low | 5 | 33.8 | 19.6 | **53.4** | 34 | $0.46 (bill) |
| 34 | GPT-5.6 Sol (medium effort) | OpenAI | Codex CLI | medium | 1 | 29 | 24 | **53** | 45 | $15.77 (list) |
| 35 | GPT-6 Astra (low effort) | OpenAI | Codex CLI | low | 1 | 27 | 25 | **52** | 52 | $11.69 (list) |
| 36 | DeepSeek V4.1 Flash 1017 (low effort) - mean of 5 | DeepSeek | Claude Code / DeepSeek API | low | 5 | 34.4 | 16.8 | **51.2** | 30 | $0.71 (bill) |
| 37 | Opus 5.5 (max effort) - mean of 3 | Anthropic | Claude Code | max | 3 | 41.7 | 9 | **50.7** | 11 | $58.53 (list) |
| 38 | Gemini 4 Argon (medium effort, Antigravity CLI) - mean of 3 | Google | Antigravity CLI | medium | 3 | 39.3 | 11.3 | **50.6** | 16 | $7.50 (list) |
| 39 | DeepSeek V4.1 Flash 1017 (low effort, OpenCode) - mean of 5 | DeepSeek | OpenCode / DeepSeek API | low | 5 | 32.8 | 17.6 | **50.4** | 36 | $0.66 (bill) |
| 40 | Sonnet 5.5 (xhigh effort) - mean of 3 | Anthropic | Claude Code | xhigh | 3 | 36 | 14 | **50** | 24 | $42.86 (list) |
| 41 | Grok 4.7 (medium) - mean of 3 | xAI | Grok Build CLI (ACP) | medium | 3 | 26.7 | 22.7 | **49.4** | 54 | $16.76 (floor) |
| 42 | Opus 5.5 (xhigh effort) - mean of 3 | Anthropic | Claude Code | xhigh | 3 | 36 | 13.3 | **49.3** | 24 | $34.98 (list) |
| 43 | GPT-6 Sol (xhigh effort) | OpenAI | Codex CLI | xhigh | 1 | 25 | 24 | **49** | 58 | $7.67 (list) |
| 43 | GPT-5.6 Terra (xhigh effort) | OpenAI | Codex CLI | xhigh | 1 | 20 | 29 | **49** | 77 | $8.98 (list) |
| 45 | Gemini 4 Argon (high effort, Antigravity CLI) - mean of 3 | Google | Antigravity CLI | high | 3 | 40.7 | 7.3 | **48** | 13 | $7.16 (list) |
| 46 | Grok 4.6 (xhigh) seq - mean of 3 | xAI | Grok Build CLI (ACP) | xhigh | 3 | 28.7 | 18 | **46.7** | 51 | $18.60 (floor) |
| 47 | GPT-6.1 Sol (low effort) - mean of 2 | OpenAI | Codex CLI | low | 2 | 22.5 | 24 | **46.5** | 67 | $1.34 (list) |
| 48 | Sonnet 5.5 (high effort) - mean of 3 | Anthropic | Claude Code | high | 3 | 34.3 | 10.7 | **45** | 31 | $19.85 (list) |
| 48 | Muse Wonder 1.0 (max effort, Muse Code, Meta API) - mean of 3 | Meta | Muse Code / Meta API | max | 3 | 31.7 | 13.3 | **45** | 39 | $27.87 (list) |
| 50 | Opus 5.5 (medium effort) - mean of 3 | Anthropic | Claude Code | medium | 3 | 30.3 | 13.3 | **43.6** | 43 | $15.68 (list) |
| 51 | Opus 5.5 (high effort) - mean of 3 | Anthropic | Claude Code | high | 3 | 31.7 | 10.7 | **42.4** | 39 | $22.25 (list) |
| 52 | Gemini 4 Argon (low effort, Antigravity CLI) - mean of 3 | Google | Antigravity CLI | low | 3 | 35.3 | 5.7 | **41** | 27 | $6.47 (list) |
| 52 | Union Alpha (stealth; free) - mean of 3 | Unbiased | Claude Code / OpenRouter | default | 3 | 30.7 | 10.3 | **41** | 42 | $4.81 (list) |
| 52 | GPT-6 Luna (max effort) - mean of 3 | OpenAI | Codex CLI | max | 3 | 18.3 | 22.7 | **41** | 84 | $0.52 (list) |
| 55 | Fable 5.1 | Anthropic | Claude Code | high | 1 | 33 | 7 | **40** | 35 | $48.58 (list) |
| 56 | Grok 4.6 (high) | xAI | Grok Build CLI (ACP) | high | 1 | 23 | 16 | **39** | 63 | $15.73 (floor) |
| 57 | Muse Spark 1.3 (high effort, Muse Code, Meta API) - mean of 3 | Meta | Muse Code / Meta API | high | 3 | 18.7 | 19.3 | **38** | 83 | $12.94 (list) |
| 58 | Fable 5.1 (low effort) | Anthropic | Claude Code | low | 1 | 29 | 6 | **35** | 45 | $33.00 (list) |
| 58 | GPT-6 Sol (high effort) | OpenAI | Codex CLI | high | 1 | 20 | 15 | **35** | 77 | $4.16 (list) |
| 58 | Grok 4.7 (high) - mean of 3 | xAI | Grok Build CLI (ACP) | high | 3 | 19.3 | 15.7 | **35** | 79 | $12.29 (floor) |
| 58 | GPT-5.6 Terra (high effort) | OpenAI | Codex CLI | high | 1 | 18 | 17 | **35** | 86 | $5.89 (list) |
| 58 | GPT-5.6 Luna (high effort) | OpenAI | Codex CLI | high | 1 | 13 | 22 | **35** | 107 | $0.57 (list) |
| 63 | Fable 5 (max effort) | Anthropic | Claude Code | max | 1 | 29 | 5 | **34** | 45 | $112.40 (list) |
| 63 | Grok 4.7 (low) - mean of 3 | xAI | Grok Build CLI (ACP) | low | 3 | 15.7 | 18.3 | **34** | 98 | $9.36 (floor) |
| 65 | Muse Spark 1.3 (xhigh effort, Muse Code, Meta API) - mean of 3 | Meta | Muse Code / Meta API | xhigh | 3 | 20.3 | 13.3 | **33.6** | 76 | $13.71 (list) |
| 66 | Fable 5.1 (xhigh effort) | Anthropic | Claude Code | xhigh | 1 | 29 | 4 | **33** | 45 | $53.61 (list) |
| 66 | Qwen3.8-Flash (max effort) | Alibaba | Claude Code / Alibaba API | max | 1 | 26 | 7 | **33** | 55 | $1.81 (list) |
| 66 | Grok 4.6 (medium) seq | xAI | Grok Build CLI (ACP) | medium | 1 | 22 | 11 | **33** | 69 | $5.80 (floor) |
| 69 | Qwen3.8-Max (max effort, Alibaba API) - mean of 3 | Alibaba | Claude Code / Alibaba API | max | 3 | 25.7 | 7 | **32.7** | 57 | $26.76 (list) |
| 70 | Sonnet 5.5 (medium effort) - mean of 3 | Anthropic | Claude Code | medium | 3 | 23.3 | 8.7 | **32** | 61 | $11.11 (list) |
| 70 | Opus 5.5 (low effort) - mean of 3 | Anthropic | Claude Code | low | 3 | 22.3 | 9.7 | **32** | 68 | $8.34 (list) |
| 72 | MiMo-V2.6-Flash - mean of 3 | Xiaomi | Claude Code / OpenRouter | default | 3 | 23.3 | 7.3 | **30.6** | 61 | $0.49 (bill) |
| 73 | Haiku 5.5 (max effort) - mean of 2 | Anthropic | Claude Code | max | 2 | 21.5 | 9 | **30.5** | 72 | $5.83 (list) |
| 74 | Muse Spark 1.3 (medium effort, Muse Code, Meta API) - mean of 3 | Meta | Muse Code / Meta API | medium | 3 | 13 | 17.3 | **30.3** | 107 | $9.24 (list) |
| 75 | Qwen3.8-Flash (low effort) | Alibaba | Claude Code / Alibaba API | low | 1 | 23 | 7 | **30** | 63 | $1.37 (list) |
| 76 | Opus 5 (max effort) | Anthropic | Claude Code | max | 1 | 27 | 2 | **29** | 52 | $54.94 (list) |
| 76 | Opus 5 (xhigh effort) | Anthropic | Claude Code | xhigh | 1 | 26 | 3 | **29** | 55 | $63.25 (list) |
| 76 | Muse Spark 1.2 (xhigh, Meta API) | Meta | Claude Code / Meta API | xhigh | 1 | 17 | 12 | **29** | 91 | $13.99 (list) |
| 79 | DeepSeek V4.1 Flash (max effort) - mean of 3 | DeepSeek | Claude Code / DeepSeek API | max | 3 | 21.7 | 6.7 | **28.4** | 71 | $0.78 (bill) |
| 80 | GPT-6.1 Terra (xhigh effort) - mean of 3 | OpenAI | Codex CLI | xhigh | 3 | 11.3 | 17 | **28.3** | 112 | $0.75 (list) |
| 81 | Opus 5 (medium effort) | Anthropic | Claude Code | medium | 1 | 24 | 4 | **28** | 59 | $37.40 (list) |
| 81 | MiMo-V2.6-Pro - mean of 3 | Xiaomi | Claude Code / OpenRouter | default | 3 | 22.7 | 5.3 | **28** | 66 | $0.86 (bill) |
| 83 | Fable 5 | Anthropic | Claude Code | high | 1 | 24 | 3 | **27** | 59 | $74.52 (list) |
| 83 | Kimi K3 | Moonshot AI | Claude Code / OpenRouter | default | 1 | 21 | 6 | **27** | 73 | $25.27 (list) |
| 83 | Opus 5 | Anthropic | Claude Code | high | 1 | 21 | 6 | **27** | 73 | $41.51 (list) |
| 83 | Sonnet 5.5 (low effort) - mean of 3 | Anthropic | Claude Code | low | 3 | 19 | 8 | **27** | 80 | $5.73 (list) |
| 83 | Grok 4.5 (re-run Aug 6) | xAI | Grok Build CLI (ACP) | high | 1 | 17 | 10 | **27** | 91 | $8.50 (floor) |
| 83 | GPT-6 Sol (medium effort) | OpenAI | Codex CLI | medium | 1 | 14 | 13 | **27** | 104 | $2.39 (list) |
| 89 | Gemini 3.7 Flash (high) | Google | Gemini CLI (retired) + model-pinning gateway | high | 1 | 22 | 4 | **26** | 69 | $8.43 (list) |
| 89 | GPT-6 Luna (xhigh effort) | OpenAI | Codex CLI | xhigh | 1 | 14 | 12 | **26** | 104 | $0.39 (list) |
| 91 | Haiku 5.5 (xhigh effort) - mean of 3 | Anthropic | Claude Code | xhigh | 3 | 18.3 | 6.7 | **25** | 84 | $4.80 (list) |
| 92 | Fable 5.1 (medium effort) | Anthropic | Claude Code | medium | 1 | 21 | 3 | **24** | 73 | $23.73 (list) |
| 92 | Grok 4.6 (low) | xAI | Grok Build CLI (ACP) | low | 1 | 15 | 9 | **24** | 99 | $4.14 (floor) |
| 94 | DeepSeek V4.1 Flash (high effort) | DeepSeek | Claude Code / DeepSeek API | high | 1 | 19 | 4 | **23** | 80 | $0.31 (bill) |
| 95 | Gemini 3.8 Flash - mean of 3 | Google | Antigravity CLI | high | 3 | 18 | 4 | **22** | 86 | $11.03 (list) |
| 95 | MiMo-V2.6-Pro (first-party) | Xiaomi | Claude Code / Xiaomi first-party | enabled | 1 | 18 | 4 | **22** | 86 | $0.59 (list) |
| 97 | GLM-5.3 (max effort, Z.ai API) | Z.ai | Claude Code / Z.ai API | max | 1 | 19 | 2 | **21** | 80 | $15.93 (list) |
| 97 | GLM-5.3 Flash (max effort, Z.ai API) - mean of 3 | Z.ai | Claude Code / Z.ai API | max | 3 | 17.7 | 3.3 | **21** | 90 | $1.03 (list) |
| 97 | GPT-5.6 Terra (medium effort) | OpenAI | Codex CLI | medium | 1 | 15 | 6 | **21** | 99 | $3.87 (list) |
| 100 | Hy4 Preview | Tencent | Claude Code / OpenRouter | default | 1 | 18 | 2 | **20** | 86 | $3.13 (bill) |
| 100 | DeepSeek V4-Pro (max effort, DeepSeek API) | DeepSeek | Claude Code / DeepSeek API | max | 1 | 16 | 4 | **20** | 93 | $1.89 (bill) |
| 100 | GLM-5.3 Flash (high effort, Z.ai API) | Z.ai | Claude Code / Z.ai API | high | 1 | 16 | 4 | **20** | 93 | $0.94 (list) |
| 100 | Haiku 5.5 (high effort) - mean of 2 | Anthropic | Claude Code | high | 2 | 16 | 4 | **20** | 93 | $3.56 (list) |
| 104 | Ox Alpha (stealth; free) | Z.ai | Claude Code / OpenRouter | default | 1 | 16 | 3 | **19** | 93 | $0.00 (free) |
| 105 | Mistral Large 4 - mean of 3 | Mistral | Claude Code / OpenRouter | high | 3 | 15 | 3.3 | **18.3** | 99 | $11.95 (bill) |
| 106 | Gemini 3.7 Flash seq | Google | Antigravity CLI | high | 1 | 16 | 2 | **18** | 93 | $6.36 (list) |
| 106 | Opus 4.8 (max effort) | Anthropic | Claude Code | max | 1 | 15 | 3 | **18** | 99 | $58.11 (list) |
| 106 | GPT-6 Luna (high effort) | OpenAI | Codex CLI | high | 1 | 9 | 9 | **18** | 117 | $0.13 (list) |
| 109 | Qwen3.8-27B (xhigh effort, Alibaba API) - mean of 3 | Alibaba | Claude Code / Alibaba API | xhigh | 3 | 15 | 2.3 | **17.3** | 99 | $5.55 (list) |
| 110 | GLM-5.3 Flash | Z.ai | Claude Code / OpenRouter | default | 1 | 13 | 4 | **17** | 107 | $0.79 (bill) |
| 111 | GPT-6.1 Terra (high effort) - mean of 3 | OpenAI | Codex CLI | high | 3 | 9.7 | 6.7 | **16.4** | 115 | $0.56 (list) |
| 111 | Muse Spark 1.3 (low effort, Muse Code, Meta API) - mean of 3 | Meta | Muse Code / Meta API | low | 3 | 9.7 | 6.7 | **16.4** | 115 | $5.61 (list) |
| 113 | Haiku 5.5 (medium effort) | Anthropic | Claude Code | medium | 1 | 12 | 4 | **16** | 111 | $2.66 (list) |
| 114 | GPT-6.1 Terra (medium effort) - mean of 3 | OpenAI | Codex CLI | medium | 3 | 7.3 | 7.3 | **14.6** | 123 | $0.31 (list) |
| 115 | DeepSeek V4-Flash 0731 | DeepSeek | Claude Code / OpenRouter | default | 1 | 14 | 0 | **14** | 104 | $1.52 (bill) |
| 115 | DeepSeek V4-Pro (high effort, DeepSeek API) | DeepSeek | Claude Code / DeepSeek API | high | 1 | 13 | 1 | **14** | 107 | $1.08 (bill) |
| 115 | GPT-5.6 Luna (medium effort) | OpenAI | Codex CLI | medium | 1 | 9 | 5 | **14** | 117 | $0.33 (list) |
| 118 | Haiku 5.5 (low effort) | Anthropic | Claude Code | low | 1 | 11 | 2 | **13** | 113 | $1.61 (list) |
| 118 | GLM-5.3 Flash (low effort, Z.ai API) | Z.ai | Claude Code / Z.ai API | low | 1 | 9 | 4 | **13** | 117 | $0.42 (list) |
| 118 | Sonnet 5 | Anthropic | Claude Code | high | 1 | 9 | 4 | **13** | 117 | $11.38 (list) |
| 118 | GPT-6 Luna (low effort) | OpenAI | Codex CLI | low | 1 | 4 | 9 | **13** | 126 | $0.20 (list) |
| 122 | Qwen3.8-27B 8-bit (OpenRouter/Parasail) - mean of 3 | Alibaba | Claude Code / OpenRouter | default | 3 | 10.7 | 1.7 | **12.4** | 114 | $2.97 (bill) |
| 123 | Sonnet 5 (max effort) | Anthropic | Claude Code | max | 1 | 9 | 3 | **12** | 117 | $17.96 (list) |
| 124 | GPT-6 Sol (low effort) | OpenAI | Codex CLI | low | 1 | 6 | 5 | **11** | 124 | $1.08 (list) |
| 124 | GPT-6.1 Terra (low effort) - mean of 3 | OpenAI | Codex CLI | low | 3 | 6 | 5 | **11** | 124 | $0.30 (list) |
| 126 | Opus 4.8 | Anthropic | Claude Code | high | 1 | 9 | 1 | **10** | 117 | $21.30 (list) |
| 127 | Gemma 4 31B (OpenRouter/Crusoe) | Google | Claude Code / OpenRouter | default | 1 | 4 | 2 | **6** | 126 | $8.61 (bill) |
| 128 | GPT-5.6 Luna (low effort) | OpenAI | Codex CLI | low | 1 | 4 | 1 | **5** | 126 | $0.10 (list) |
| 128 | Gemma 4 31B 4-bit (OpenRouter/CoreWeave) | Google | Claude Code / OpenRouter | default | 1 | 3 | 2 | **5** | 130 | $0.56 (bill) |
| 130 | GPT-6 Luna (medium effort) | OpenAI | Codex CLI | medium | 1 | 4 | 0 | **4** | 126 | $0.06 (list) |
| 130 | Haiku 4.5 - mean of 2 | Anthropic | Claude Code | default | 2 | 1.5 | 2.5 | **4** | 131 | $2.22 (list) |
| 132 | gpt-oss-120b - mean of 3 | OpenAI | Claude Code / OpenRouter | default | 3 | 0 | 0.3 | **0.3** | 132 | $0.11 (bill) |
| 133 | gpt-oss-20b - mean of 3 | OpenAI | Claude Code / OpenRouter | default | 3 | 0 | 0 | **0** | 132 | $0.11 (bill) |

## Superseded rows (not ranked)

| Board row | Harness | Effort | Planted | Unplanted | Total |
|---|---|---|---:|---:|---:|
| GPT-6.1 Sol (xhigh effort) | Codex CLI | xhigh | 41 | 63 | 104 |
| GPT-6.1 Sol (max effort) | Codex CLI | max | 44 | 59 | 103 |
| Muse Wonder Full 1.0 (max effort, Muse Code, Meta API) | Muse Code / Meta API | max | 44 | 53 | 97 |
| GPT-6 Astra (max effort) | Codex CLI | max | 48 | 45 | 93 |
| Sonnet 5.5 (max effort) | Claude Code | max | 57 | 28 | 85 |
| GPT-6.1 Sol (high effort) | Codex CLI | high | 38 | 45 | 83 |
| GPT-5.6 Sol (max effort) | Codex CLI | max | 42 | 40 | 82 |
| GPT-6 Sol (max effort) | Codex CLI | max | 32 | 48 | 80 |
| Sonnet 5.5 (max effort) - mean of 2 | Claude Code | max | 55.5 | 24.5 | 80 |
| Muse Wonder Full 1.0 (xhigh effort, Muse Code, Meta API) | Muse Code / Meta API | xhigh | 44 | 35 | 79 |
| GPT-5.6 Luna (max effort) - mean of 2 | Codex CLI | max | 31.5 | 44 | 75.5 |
| GPT-6 Sol (max effort) - mean of 2 | Codex CLI | max | 31 | 41 | 72 |
| GPT-5.6 Sol | Codex CLI | high | 31 | 38 | 69 |
| DeepSeek V4.1 Flash 1017 (max effort) - mean of 5 | Claude Code / DeepSeek API | max | 39.4 | 24.6 | 64 |
| GPT-5.6 Luna (max effort) | Codex CLI | max | 33 | 31 | 64 |
| GPT-6.1 Sol (low effort) | Codex CLI | low | 31 | 32 | 63 |
| DeepSeek V4.1 Flash 1017 (max effort) - mean of 3 | Claude Code / DeepSeek API | max | 38.7 | 22.3 | 61 |
| Grok 4.7 (xhigh) seq - mean of 4 | Grok Build CLI (ACP) | xhigh | 28.8 | 31.8 | 60.6 |
| Grok 4.7 (xhigh) seq - mean of 3 | Grok Build CLI (ACP) | xhigh | 28.7 | 31.7 | 60.4 |
| GPT-6.1 Sol (medium effort) | Codex CLI | medium | 28 | 32 | 60 |
| Grok 4.7 (medium) | Grok Build CLI (ACP) | medium | 30 | 30 | 60 |
| Muse Spark 1.3 (max effort, Muse Code, Meta API) - mean of 3 | Muse Code / Meta API | max | 33.7 | 26.3 | 60 |
| Sonnet 5.5 (xhigh effort) | Claude Code | xhigh | 39 | 19 | 58 |
| DeepSeek V4.1 Flash 1017 (max effort) | Claude Code / DeepSeek API | max | 34 | 19 | 53 |
| DeepSeek V4.1 Flash 1017 (max effort) - mean of 2 | Claude Code / DeepSeek API | max | 35.5 | 17.5 | 53 |
| Opus 5.5 (max effort) | Claude Code | max | 43 | 9 | 52 |
| Opus 5.5 (xhigh effort) - mean of 2 | Claude Code | xhigh | 36 | 15.5 | 51.5 |
| DeepSeek V4.1 Flash 1017 (high effort) - mean of 2 | Claude Code / DeepSeek API | high | 32 | 18 | 50 |
| Opus 5.5 (max effort) - mean of 2 | Claude Code | max | 41 | 9 | 50 |
| Muse Spark 1.3 (max effort, Muse Code, Meta API) | Muse Code / Meta API | max | 33 | 16 | 49 |
| Opus 5.5 (xhigh effort) | Claude Code | xhigh | 35 | 14 | 49 |
| Gemini 4 Argon (medium effort, Antigravity CLI) - mean of 2 | Antigravity CLI | medium | 36 | 10.5 | 46.5 |
| Opus 5.5 (medium effort) | Claude Code | medium | 30 | 15 | 45 |
| Opus 5.5 (medium effort) - mean of 2 | Claude Code | medium | 30 | 14 | 44 |
| Sonnet 5.5 (high effort) | Claude Code | high | 32 | 12 | 44 |
| Grok 4.6 (xhigh) seq | Grok Build CLI (ACP) | xhigh | 27 | 16 | 43 |
| Union Alpha (stealth; free) | Claude Code / OpenRouter | default | 32 | 11 | 43 |
| Grok 4.6 (xhigh) | Grok Build CLI (ACP) | xhigh | 27 | 15 | 42 |
| Opus 5.5 (high effort) - mean of 2 | Claude Code | high | 32 | 9.5 | 41.5 |
| GPT-6 Luna (max effort) - mean of 2 | Codex CLI | max | 19 | 20.5 | 39.5 |
| GPT-6 Luna (max effort) | Codex CLI | max | 17 | 22 | 39 |
| Opus 5.5 (high effort) | Claude Code | high | 32 | 7 | 39 |
| Grok 4.7 (high) | Grok Build CLI (ACP) | high | 19 | 18 | 37 |
| Opus 5.5 (low effort) | Claude Code | low | 23 | 14 | 37 |
| Gemini 4 Argon (low effort, Antigravity CLI) | Antigravity CLI | low | 32 | 3 | 35 |
| Haiku 5.5 (max effort) | Claude Code | max | 22 | 13 | 35 |
| Muse Spark 1.3 (high effort, Muse Code, OpenRouter) | Muse Code / OpenRouter | high | 18 | 17 | 35 |
| Grok 4.6 (medium) | Grok Build CLI (ACP) | medium | 23 | 11 | 34 |
| Qwen3.8-Max (max effort, Alibaba API) | Claude Code / Alibaba API | max | 28 | 6 | 34 |
| Opus 5.5 (low effort) - mean of 2 | Claude Code | low | 24 | 9.5 | 33.5 |
| DeepSeek V4.1 Flash (max effort) | Claude Code / DeepSeek API | max | 24 | 7 | 31 |
| Gemini 3.7 Flash (high; Antigravity CLI retest) | Antigravity CLI | high | 18 | 11 | 29 |
| Muse Spark 1.3 (high effort, Muse Code, Meta API) | Muse Code / Meta API | high | 19 | 10 | 29 |
| MiMo-V2.6-Pro - mean of 2 | Claude Code / OpenRouter | default | 22 | 5.5 | 27.5 |
| Muse Spark 1.3 (xhigh effort, Muse Code, Meta API) | Muse Code / Meta API | xhigh | 20 | 7 | 27 |
| Gemini 3.8 Flash | Antigravity CLI | high | 20 | 6 | 26 |
| Sonnet 5.5 (medium effort) | Claude Code | medium | 18 | 8 | 26 |
| Qwen3.8-Max | Claude Code / OpenRouter | default | 19 | 6 | 25 |
| Sonnet 5.5 (low effort) | Claude Code | low | 20 | 5 | 25 |
| GLM-5.3 | Claude Code / OpenRouter | default | 19 | 4 | 23 |
| GLM-5.3 Flash (max effort, Z.ai API) | Claude Code / Z.ai API | max | 19 | 4 | 23 |
| Grok 4.5 | Grok Build CLI (ACP) | high | 16 | 7 | 23 |
| Grok 4.7 (low) | Grok Build CLI (ACP) | low | 11 | 12 | 23 |
| MiMo-V2.6-Pro | Claude Code / OpenRouter | default | 20 | 3 | 23 |
| Haiku 5.5 (high effort) | Claude Code | high | 15 | 4 | 19 |
| Grok 4.5 (high re-run - CLI has no max) | Grok Build CLI (ACP) | high | 13 | 5 | 18 |
| Muse Spark 1.2 (default effort, OpenRouter) | Claude Code / OpenRouter | default | 14 | 3 | 17 |
| Muse Spark 1.3 (medium effort, Muse Code, Meta API) | Muse Code / Meta API | medium | 9 | 8 | 17 |
| Qwen3.8-27B (xhigh effort, Alibaba API) | Claude Code / Alibaba API | xhigh | 15 | 2 | 17 |
| DeepSeek V4-Flash | Claude Code / OpenRouter | default | 8 | 4 | 12 |
| DeepSeek V4-Pro | Claude Code / OpenRouter | default | 10 | 1 | 11 |
| Qwen3.8-27B 8-bit (OpenRouter/Parasail) | Claude Code / OpenRouter | default | 8 | 2 | 10 |
| gpt-oss-120b | Claude Code / OpenRouter | default | 0 | 1 | 1 |
| gpt-oss-20b | Claude Code / OpenRouter | default | 0 | 0 | 0 |
