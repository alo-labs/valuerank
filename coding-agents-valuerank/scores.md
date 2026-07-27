# Coding Agent ValueRank - Scores

Last updated: July 28, 2026

Formula:

```text
0.25*CostNorm + 0.60*AAIndexNorm + 0.15*TB21Norm
```

Rows without official Terminal Bench 2.1 coverage receive neutral TB2.1 normalization.

| Rank | Agent Variant | Overall | Quality | CostNorm | AAIndexNorm | TB2.1Norm | TB2.1 Coverage |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | Codex + GPT-5.6 Terra (max) | 71.5 | 83.1 | 36.6 | 90.2 | 54.8 | Covered |
| 2 | Codex + GPT-5.5 (xhigh) | 69.5 | 87.8 | 14.6 | 85.4 | 97.6 | Covered |
| 3 | Codex + GPT-5.6 Sol (high) | 69.4 | 86.1 | 19.5 | 95.1 | 50.0 | Neutralized |
| 4 | Codex + GPT-5.6 Sol (xhigh) | 69.1 | 88.1 | 12.2 | 97.6 | 50.0 | Neutralized |
| 5 | Claude Code + Opus 5 (high) | 68.6 | 84.2 | 22.0 | 92.7 | 50.0 | Neutralized |
| 6 | Claude Code + Opus 5 (medium) | 67.5 | 80.2 | 29.3 | 87.8 | 50.0 | Neutralized |
| 7 | Claude Code + Opus 5 (max) | 67.5 | 90.0 | 0.0 | 100.0 | 50.0 | Neutralized |
| 8 | Codex + GPT-5.6 Luna (max) | 67.2 | 67.6 | 65.9 | 78.0 | 26.2 | Covered |
| 9 | Codex + GPT-5.6 Terra (xhigh) | 66.2 | 69.5 | 56.1 | 73.2 | 54.8 | Covered |
| 10 | Codex + GPT-5.6 Sol (medium) | 65.2 | 76.3 | 31.7 | 82.9 | 50.0 | Neutralized |
| 11 | Codex + GPT-5.6 Terra (high) | 63.6 | 63.7 | 63.4 | 65.9 | 54.8 | Covered |
| 12 | Claude Code + Opus 5 (low) | 61.5 | 66.6 | 46.3 | 70.7 | 50.0 | Neutralized |
| 13 | Codex + GPT-5.5 (medium) | 61.0 | 68.3 | 39.0 | 61.0 | 97.6 | Covered |
| 14 | Claude Code + Opus 4.8 (max) | 61.0 | 80.6 | 2.4 | 80.5 | 81.0 | Covered |
| 15 | Codex + GPT-5.6 Luna (xhigh) | 60.9 | 56.0 | 75.6 | 63.4 | 26.2 | Covered |
| 16 | Claude Code + Opus 4.8 (xhigh) | 59.3 | 76.7 | 7.3 | 75.6 | 81.0 | Covered |
| 17 | Claude Code + Opus 4.8 (high) | 59.2 | 70.8 | 24.4 | 68.3 | 81.0 | Covered |
| 18 | Codex + GPT-5.6 Sol (low) | 57.2 | 56.8 | 58.5 | 58.5 | 50.0 | Neutralized |
| 19 | Codex + GPT-5.6 Terra (medium) | 56.7 | 48.0 | 82.9 | 46.3 | 54.8 | Covered |
| 20 | Codex + GPT-5.6 Luna (high) | 56.3 | 48.2 | 80.5 | 53.7 | 26.2 | Covered |
| 21 | Claude Code + Opus 4.8 (medium) | 52.5 | 61.1 | 26.8 | 56.1 | 81.0 | Covered |
| 22 | Claude Code + Opus 4.6 (medium) | 50.7 | 43.2 | 73.2 | 41.5 | 50.0 | Neutralized |
| 23 | Claude Code + Opus 4.8 (low) | 50.7 | 51.3 | 48.8 | 43.9 | 81.0 | Covered |
| 24 | Cursor CLI + Composer 2.5 | 46.5 | 29.5 | 97.6 | 24.4 | 50.0 | Neutralized |
| 25 | Codex + GPT-5.6 Sol (none) | 45.6 | 37.3 | 70.7 | 34.1 | 50.0 | Neutralized |
| 26 | Opencode + Opus 4.7 (medium) | 45.3 | 49.0 | 34.1 | 48.8 | 50.0 | Neutralized |
| 27 | Codex + GPT-5.6 Luna (medium) | 44.9 | 30.6 | 87.8 | 31.7 | 26.2 | Covered |
| 28 | Cursor CLI + GPT-5.5 (medium) | 43.7 | 41.2 | 51.2 | 39.0 | 50.0 | Neutralized |
| 29 | Codex + GPT-5.6 Terra (low) | 39.8 | 24.6 | 85.4 | 17.1 | 54.8 | Covered |
| 30 | Cursor CLI + Opus 4.7 (medium) | 39.8 | 39.3 | 41.5 | 36.6 | 50.0 | Neutralized |
| 31 | Cursor CLI + Composer 2 | 36.9 | 15.8 | 100.0 | 7.3 | 50.0 | Neutralized |
| 32 | Cursor CLI + GPT-5.4 (medium) | 36.3 | 25.6 | 68.3 | 19.5 | 50.0 | Neutralized |
| 33 | Codex + GPT-5.4 (medium) | 34.6 | 31.4 | 43.9 | 26.8 | 50.0 | Neutralized |
| 34 | Claude Code + Opus 4.7 (max) | 34.2 | 42.4 | 9.8 | 51.2 | 7.1 | Covered |
| 35 | Claude Code + Sonnet 4.6 (medium) | 34.1 | 27.6 | 53.7 | 22.0 | 50.0 | Neutralized |
| 36 | Claude Code + Opus 4.7 (medium) | 33.9 | 24.9 | 61.0 | 29.3 | 7.1 | Covered |
| 37 | Claude Code + Kimi K2.6 | 32.9 | 17.8 | 78.0 | 9.8 | 50.0 | Neutralized |
| 38 | Codex + GPT-5.6 Terra (none) | 32.2 | 12.9 | 90.2 | 2.4 | 54.8 | Covered |
| 39 | Codex + GPT-5.6 Luna (low) | 30.6 | 9.2 | 95.1 | 4.9 | 26.2 | Covered |
| 40 | Codex + GPT-5.6 Luna (none) | 27.1 | 5.2 | 92.7 | 0.0 | 26.2 | Covered |
| 41 | Claude Code + Qwen3.7 Plus (thinking) | 16.0 | 19.8 | 4.9 | 12.2 | 50.0 | Neutralized |
| 42 | Claude Code + GLM-5.1 | 13.0 | 11.7 | 17.1 | 14.6 | 0.0 | Covered |
