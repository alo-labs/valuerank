# Coverage of candidate benchmarks outside AA and Vals (2026-10-23)

This note backs owner decision O52: ValueRank picks a benchmark set, and only configurations that have every benchmark in it are ranked. It covers the 29 configurations in `cohort-2026-10-23.json`. Vals AI is covered separately.

- The machine-readable matrix is `other-coverage-2026-10-23.json`. It has one entry per scored column, with values, source labels, efforts and per-cell notes.
- Raw captures are in `other-capture/`. They were fetched 2026-10-23 between 07:40 and 07:58 UTC.

**Status labels.**
- **Exact:** the source row names the same model version and the same reasoning effort as AA.
- **Plausible:** the model matches, but the effort or snapshot cannot be confirmed. AA plots MiMo-V2.6-Pro, MiMo-V2.6-Flash and MiniMax-M3.1-Flash without an effort label, so their rows are always plausible. Rows where the source states no effort or snapshot are also plausible.
- Nothing is transferred across efforts or versions.

## Counts over the 29 configurations

| Leaf key | Exact | Plausible | Exact configurations | Plausible configurations |
|---|---|---|---|---|
| `aicd-total` | 13 | 3 | claude-haiku-5-5-high, claude-haiku-5-5-medium, claude-opus-5-5-high, claude-opus-5-5-medium, deepseek-v4-1-flash-1017, gemini-4-argon, gpt-6-astra-high, gpt-6-luna, gpt-6-luna-high, gpt-6-luna-medium, gpt-6-luna-xhigh, gpt-6.1-sol-high, gpt-6.1-sol-medium | mimo-v2-6-flash, mimo-v2-6-pro, minimax-m3-1-flash |
| `aicd-non-bug` | 14 | 3 | claude-haiku-5-5-high, claude-haiku-5-5-medium, claude-opus-5-5-high, claude-opus-5-5-medium, deepseek-v4-1-flash-1017, gemini-4-argon, gpt-5.6-luna-low, gpt-6-astra-high, gpt-6-luna, gpt-6-luna-high, gpt-6-luna-medium, gpt-6-luna-xhigh, gpt-6.1-sol-high, gpt-6.1-sol-medium | mimo-v2-6-flash, mimo-v2-6-pro, minimax-m3-1-flash |
| `aicd-laravel-quality` | 14 | 3 | claude-haiku-5-5-high, claude-haiku-5-5-medium, claude-opus-5-5-high, claude-opus-5-5-medium, deepseek-v4-1-flash-1017, gemini-4-argon, gpt-5.6-luna-low, gpt-6-astra-high, gpt-6-luna, gpt-6-luna-high, gpt-6-luna-medium, gpt-6-luna-xhigh, gpt-6.1-sol-high, gpt-6.1-sol-medium | mimo-v2-6-flash, mimo-v2-6-pro, minimax-m3-1-flash |
| `aicd-react-quality` | 14 | 3 | claude-haiku-5-5-high, claude-haiku-5-5-medium, claude-opus-5-5-high, claude-opus-5-5-medium, deepseek-v4-1-flash-1017, gemini-4-argon, gpt-5.6-luna-low, gpt-6-astra-high, gpt-6-luna, gpt-6-luna-high, gpt-6-luna-medium, gpt-6-luna-xhigh, gpt-6.1-sol-high, gpt-6.1-sol-medium | mimo-v2-6-flash, mimo-v2-6-pro, minimax-m3-1-flash |
| `aicd-bug-finding` | 13 | 3 | claude-haiku-5-5-high, claude-haiku-5-5-medium, claude-opus-5-5-high, claude-opus-5-5-medium, deepseek-v4-1-flash-1017, gemini-4-argon, gpt-6-astra-high, gpt-6-luna, gpt-6-luna-high, gpt-6-luna-medium, gpt-6-luna-xhigh, gpt-6.1-sol-high, gpt-6.1-sol-medium | mimo-v2-6-flash, mimo-v2-6-pro, minimax-m3-1-flash |
| `aicd-edge-case` | 14 | 3 | claude-haiku-5-5-high, claude-haiku-5-5-medium, claude-opus-5-5-high, claude-opus-5-5-medium, deepseek-v4-1-flash-1017, gemini-4-argon, gpt-5.6-luna-low, gpt-6-astra-high, gpt-6-luna, gpt-6-luna-high, gpt-6-luna-medium, gpt-6-luna-xhigh, gpt-6.1-sol-high, gpt-6.1-sol-medium | mimo-v2-6-flash, mimo-v2-6-pro, minimax-m3-1-flash |
| `livebench2-coding` | 8 | 2 | claude-haiku-5-5-max, claude-opus-5-5, claude-sonnet-5-5, deepseek-v4-1-flash-1017, gemini-4-argon, gpt-6-astra, gpt-6-luna, gpt-6.1-sol | mimo-v2-6-pro, minimax-m3-1-flash |
| `livebench2-agentic` | 8 | 2 | claude-haiku-5-5-max, claude-opus-5-5, claude-sonnet-5-5, deepseek-v4-1-flash-1017, gemini-4-argon, gpt-6-astra, gpt-6-luna, gpt-6.1-sol | mimo-v2-6-pro, minimax-m3-1-flash |
| `livebench2-reasoning` | 8 | 2 | claude-haiku-5-5-max, claude-opus-5-5, claude-sonnet-5-5, deepseek-v4-1-flash-1017, gemini-4-argon, gpt-6-astra, gpt-6-luna, gpt-6.1-sol | mimo-v2-6-pro, minimax-m3-1-flash |
| `livebench2-browser` | 8 | 2 | claude-haiku-5-5-max, claude-opus-5-5, claude-sonnet-5-5, deepseek-v4-1-flash-1017, gemini-4-argon, gpt-6-astra, gpt-6-luna, gpt-6.1-sol | mimo-v2-6-pro, minimax-m3-1-flash |
| `livebench2-data-analysis` | 8 | 2 | claude-haiku-5-5-max, claude-opus-5-5, claude-sonnet-5-5, deepseek-v4-1-flash-1017, gemini-4-argon, gpt-6-astra, gpt-6-luna, gpt-6.1-sol | mimo-v2-6-pro, minimax-m3-1-flash |
| `livebench2-research` | 8 | 2 | claude-haiku-5-5-max, claude-opus-5-5, claude-sonnet-5-5, deepseek-v4-1-flash-1017, gemini-4-argon, gpt-6-astra, gpt-6-luna, gpt-6.1-sol | mimo-v2-6-pro, minimax-m3-1-flash |
| `livebench2-design` | 8 | 2 | claude-haiku-5-5-max, claude-opus-5-5, claude-sonnet-5-5, deepseek-v4-1-flash-1017, gemini-4-argon, gpt-6-astra, gpt-6-luna, gpt-6.1-sol | mimo-v2-6-pro, minimax-m3-1-flash |
| `surge-complex-constraints` | 3 | 1 | claude-opus-5-5, gemini-4-argon, gpt-6-astra | deepseek-v4-1-flash-1017 |
| `surge-sudo-l7` | 5 | 0 | claude-opus-5-5, claude-sonnet-5-5, gemini-4-argon, gpt-6-astra, gpt-6.1-sol | - |
| `cursorbench-4` | 13 | 0 | claude-haiku-5-5, claude-haiku-5-5-high, claude-haiku-5-5-low, claude-haiku-5-5-max, claude-haiku-5-5-medium, claude-opus-5-5, claude-opus-5-5-high, claude-opus-5-5-medium, claude-opus-5-5-xhigh, claude-sonnet-5-5, claude-sonnet-5-5-xhigh, gemini-4-argon, gpt-5.6-luna-low | - |
| `arena-webdev` | 8 | 3 | claude-haiku-5-5-high, claude-opus-5-5, claude-sonnet-5-5-xhigh, deepseek-v4-1-flash-1017, gemini-4-argon, gpt-6-astra, gpt-6-luna, gpt-6.1-sol | mimo-v2-6-flash, mimo-v2-6-pro, minimax-m3-1-flash |
| `arena-agent` | 8 | 2 | claude-haiku-5-5-high, claude-opus-5-5, claude-sonnet-5-5, gemini-4-argon, gpt-6-astra, gpt-6-luna, gpt-6-luna-low, gpt-6.1-sol | mimo-v2-6-flash, mimo-v2-6-pro |
| `frontierswe-v2` | 0 | 5 | - | claude-haiku-5-5-max, claude-opus-5-5, claude-sonnet-5-5, gemini-4-argon, gpt-6-astra |
| `swe-rebench` | 0 | 0 | - | - |
| `ifbench` | 0 | 0 | - | - |
Five configurations have no exact result in any benchmark above: GPT-6 Astra xhigh, GPT-6.1 Sol xhigh, MiMo-V2.6-Pro, MiMo-V2.6-Flash and MiniMax-M3.1-Flash. The last three have plausible rows in AICD, Arena and LiveBench (Pro and MiniMax only).

## Overlaps relevant to an O52 set (exact only; exact plus plausible in brackets)

| Set | Configurations with every leaf |
|---|---|
| AICD non-bug + CursorBench | 6 (Haiku high/medium, Opus high/medium, Argon, GPT-5.6 Luna low) |
| AICD non-bug + Surge | 1 (Argon) [2] |
| LiveBench 2.0 Agentic + Surge | 3 (Opus max, Argon, Astra max) [4] |
| LiveBench Agentic + Arena WebDev + Arena Agent | 5 (Opus max, Argon, Astra max, Luna max, Sol max) [6] |
| Surge + any SWE candidate | at most 3 (Opus max, Argon, Astra max) |

Surge's three exact rows are all max or high efforts of models AA also plots at lower efforts. So any set that includes Surge ranks at most 3 of 29 configurations, or 4 if DeepSeek's snapshot is confirmed to be 1017.

## Surge ComplexConstraints: the full current leaderboard (44 rows, percent)

The page shows no leaderboard date. The blog is dated 2026-06-03 and was updated 2026-10-21. The Webflow site was last published 2026-10-23T03:58:45Z.

Every row's rank field renders as "1", which is a CMS artefact. The rows below are in page order.

The metric is the share of prompts where every rubric criterion passes (`all_pass/mean` in the harness README).

| Model (Surge label) | Score |
|---|---|
| GPT 6 Astra (Max reasoning) | 57.7 |
| Gemini 4 Argon (High reasoning) | 53.3 |
| Muse Spark 1.3 (xHigh reasoning) | 51.9 |
| GPT 6 Sol (Max reasoning) | 50.8 |
| GPT 5.6 Sol (Max reasoning) | 50.5 |
| Claude Opus 5.5 (Adaptive/Max) | 49.9 |
| DeepSeek V4.1 Flash (Max reasoning) | 49.7 |
| GPT 5.5 (xHigh reasoning) | 49.5 |
| Grok 4.7 (xHigh reasoning) | 48.9 |
| Gemini 3.8 Flash (High reasoning) | 48.4 |
| Hy Hy4 Preview (High reasoning) | 46 |
| GPT 5.4 (xHigh reasoning) | 46 |
| Qwen 3.8 Max (xHigh reasoning) | 45.5 |
| Claude Fable 5.1 (Adaptive/Max) | 45.1 |
| Gemini 3.1 Pro (High reasoning) | 43.7 |
| Qwen 3.8 Flash (xHigh reasoning) | 43.3 |
| Gemini 3.7 Flash (High reasoning) | 42.4 |
| DeepSeek V4 Pro (Max reasoning) | 42 |
| Gemini 3.6 Flash (High reasoning) | 40 |
| DeepSeek V4 Flash Vision (experimental) (Max reasoning) | 39.9 |
| Muse Spark 1.2 (xHigh reasoning) | 39.9 |
| Muse Spark 1.1 (xHigh reasoning) | 38.1 |
| Claude Fable 5 (Max reasoning) | 38.1 |
| Kimi K3 (Max reasoning) | 37.9 |
| Claude Opus 5 (Adaptive/Max) | 37.3 |
| Grok 4.6 (xHigh reasoning) | 36.5 |
| Grok 4.5 (High reasoning) | 35.9 |
| Claude Opus 4.8 (Max reasoning) | 35.6 |
| Hy Hy3 (High reasoning) | 34.3 |
| Qwen 3.7 Max (Thinking on) | 33.5 |
| GLM 5.3 (Max reasoning) | 30.5 |
| Kimi K2.6 (Thinking on) | 30.1 |
| GLM 5.2 (Max reasoning) | 29.3 |
| GLM 5.3 Flash (Max reasoning) | 27.6 |
| Muse Glimmer 30B (xHigh reasoning) | 23.9 |
| Gemini 3.5 Flash-Lite (High reasoning) | 23.2 |
| Kimi K2.5 (Thinking on) | 18.2 |
| Nemotron 3 Ultra | 17.8 |
| Qwen 3.5 Plus (Thinking on) | 17.8 |
| Grok 4.20 Beta | 16.4 |
| Ernie 5.1 | 14.7 |
| Nemotron Lightning 3.5 30B A3B (Thinking on) | 7.1 |
| Mistral Large 3 | 0.4 |
| Ernie 4.5 300B | 0 |
**Mapping to the cohort.**
- Exact: GPT-6 Astra (max) 57.7, Gemini 4 Argon (high) 53.3, and Claude Opus 5.5 (max) 49.9. Surge labels the Opus row "Adaptive/Max"; AA plots "max with fallback".
- Plausible: DeepSeek V4.1 Flash (Max) 49.7. The snapshot is not stated: 20260910 and 20261017 both exist.
- Absent:
  - GPT-6.1 Sol (all efforts; only GPT 6 Sol, a different version, is listed)
  - GPT-6 Luna, GPT-5.6 Luna, Claude Haiku 5.5 and Claude Sonnet 5.5
  - Astra high/xhigh and Opus high/medium/xhigh
  - MiMo-V2.6 and MiniMax-M3.1-Flash

**Sources checked:**
- The page (`surge-complex-constraints.html`, which is identical to `/leaderboards/complex-constraints`). It has 44 rows, no pagination and no JSON feed.
- The blog and the training-on-ComplexConstraints blog.
- The harness repository, read through raw.githubusercontent.com: README and `task.py`. The harness's default judge is `google/gemini-3.5-flash`. The judge used for the leaderboard is not stated.
- The Hugging Face dataset `surgeai/ComplexConstraints`. It returned HTTP 401 under both spellings and is not in the surgeai public dataset list. The surgeai org has no Spaces.
- Web search for Surge results for the missing models found nothing.

## Caveats

- **AI Coding Daily.**
  - The harness varies by model. DeepSeek V4.1 Flash 1017 (max) has two rows: DeepSeek Harness 61.2 and OpenCode 60.97. The matrix uses the first-listed row and notes the other.
  - The hidden older rows were read by posting the page's Livewire update with the hidden-model filter cleared. This added GPT-5.6 Luna low. That row was tested 2026-09-12, before the Bug Finding project, so it has no /70 total or bug score. It is exact on the non-bug, Laravel, React and Edge-case columns.
  - `aicd-non-bug` (Laravel + React-TS + Edge-case, out of 60) is computed here. AICD does not publish it.
  - The Bug Finding column overlaps ValueRank's Bug Hunt leaf in construct, though it is a different project.
  - Edge-case Testing is saturated at the top: 19.5–20 of 20.
- **LiveBench 2.0.**
  - Each model has one row, at the effort given in the bundle's model metadata (the expanded row's "Effort:" field). That covers only the max/high rows of each family.
  - There is no MiMo-V2.6-Flash row. Coding is near-saturated (91–96 for the exact rows).
  - LiveBench 2.0 has no instruction-following suite. Its seven suites are Long Agentic, Reasoning, Coding, Browser, Data Analysis, Research and Design, with 18, 202, 29, 25, 150, 22 and 25 tasks.
- **CursorBench 4.0.**
  - It was verified against cursor.com page text, not only Epoch's mirror. The current page has Opus 5.5 at every effort and GPT-5.6 Luna low (16.0%). The earlier notes lacked these.
  - It still has no GPT-6-family, MiMo, DeepSeek or MiniMax rows. The task count is not disclosed.
- **Arena.**
  - Values come from Arena's official Hugging Face dataset `lmarena-ai/leaderboard-dataset`. WebDev was published 2026-10-22 and Agent Arena 2026-10-20.
  - arena.ai itself serves a Cloudflare 403 challenge. Epoch's WebDev mirror is older and has different values.
  - Both boards are human-preference or user-outcome signals, not task success. Arena labels MiMo-V2.6 and MiniMax-M3.1-Flash without an effort.
  - Agent Arena has an exact GPT-6 Luna (low) row, which no other candidate has.
- **FrontierSWE V2.** frontierswe.com states no effort for any row, so all five matches are plausible; the effort labels come only from Epoch's mirror. There is one row per model and no GPT-6.1 Sol, Luna, MiMo, DeepSeek V4.1 or MiniMax.
- **SWE-rebench.** It has no model released after July 2026; the latest date on the page is 2026-07-24.
- **Surge sudo L7.** It is included for reference only; it was not one of the requested benchmarks. Each lab's own agent is the harness.
- **IFBench.**
  - AA removed IFBench from the Intelligence Index in v4.1 (2026-06-16), saying "We will continue to run it and publish results on new model releases".
  - Yet the AA v4.3.2 snapshot (2026-10-23T06:26Z) has `ifbench` null for all 29 configurations. AA's IFBench page shows 5 of 450 models, none of them in the cohort.
  - BenchLM's IFBench page (updated 2026-10-20) lists none of the cohort.
  - No current source publishes IFBench for any cohort configuration.

## Fetch failures

- **arena.ai** (`/leaderboard`, `/leaderboard/webdev`, `/leaderboard/agent`) and **lmarena.ai** returned HTTP 403 (Cloudflare challenge). The official Hugging Face parquet was used instead.
- The **Hugging Face dataset** `surgeai/ComplexConstraints` returned HTTP 401.
- **github.com** pages and the API for `surge-ai/complex-constraints` returned 403, because GitHub access through the session proxy is limited to configured repositories. raw.githubusercontent.com worked.
