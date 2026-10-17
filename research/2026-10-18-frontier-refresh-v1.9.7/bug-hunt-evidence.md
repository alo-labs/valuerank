# Bug Hunt Bench re-pin evidence (2026-10-18)

Source (immutable, benchmark owner): `phuryn/bug-hunt-bench` at commit `aec976170df89a371384174ca87646a9a8c82415` (committed 2026-10-17T18:49:24Z; scoreboard 192 rows; run notes 'Updated Oct 17, 2026'). Captured 2026-10-18 with curl from raw.githubusercontent.com. Previous snapshot: commit `0630b120a81363c343ed7dfaf3c6d3be7f7da38c` (2026-09-30) plus supplemental captures for GPT-6.1 Sol (931c1ff...) and MiMo (7dd3c23...).

## Retrieval and hashes

```
B=https://raw.githubusercontent.com/phuryn/bug-hunt-bench/aec976170df89a371384174ca87646a9a8c82415/results
curl -fsSL -o combined-scoreboard.csv $B/combined-scoreboard.csv
curl -fsSL -o run-notes.md $B/run-notes.md
curl -fsSL -o updates.html https://api-docs.deepseek.com/updates/   # alias check only
```

| File | SHA-256 | Bytes |
|---|---|---|
| combined-scoreboard.csv | `fcf4b396c46fa07ad8bb0836ddaa1eb227fae776e356f78f03df482033d5e987` | 14187 |
| run-notes.md | `d3200281a839204914d154692d355a8236810871898ca3311547e6171150cb22` | 505406 |
| DeepSeek updates page (fetched 2026-10-18, not pinned) | `44aa1245d5d65d5fc54c8f47a9a3d3235e1ab064a8fc64d6a6e57f570ec8c99c` | 52380 |

No other file under `results/` was needed: the scoreboard and run notes carry the per-run scores, dates, efforts, harnesses and walls used here.

## Matches (31 roster models)

| Model id | Evaluated identity | fixedOf105 | sampleN | Effort | Harness | Route | Status | Run-notes anchor |
|---|---|---|---|---|---|---|---|---|
| gpt-6-astra | GPT-6 Astra (max effort) - mean of 3 | 45.0 | 3 | max | Codex CLI | OpenAI | matched | `user-content-gpt-6-astra-max-effort---mean-of-3` |
| gemini-3.8-flash | Gemini 3.8 Flash - mean of 3 | 18.0 | 3 | high | Antigravity CLI | Google | matched | `user-content-gemini-38-flash---mean-of-3` |
| claude-opus-5 | Opus 5 (max effort) | 27.0 | 1 | max | Claude Code | Anthropic | matched | `user-content-opus-5-max-effort` |
| claude-opus-5-5 | Opus 5.5 (max effort) - mean of 3 | 41.7 | 3 | max | Claude Code | Anthropic | matched | `user-content-opus-55-max-effort---mean-of-3` |
| gpt-5.6-sol | GPT-5.6 Sol (max effort) - mean of 2 | 43.5 | 2 | max | Codex CLI | OpenAI | matched | `user-content-gpt-56-sol-max-effort---mean-of-2` |
| claude-fable-5 | Fable 5 (max effort) | 29.0 | 1 | max | Claude Code | Anthropic | matched | `user-content-fable-5-max-effort` |
| glm-5.3 | GLM-5.3 (max effort, Z.ai API) | 19.0 | 1 | max | Claude Code / Z.ai API | Z.ai API | matched | `user-content-glm-53-max-effort-zai-api` |
| kimi-k3 | Kimi K3 | 21.0 | 1 | default | Claude Code / OpenRouter | OpenRouter | matched | `user-content-kimi-k3` |
| grok-4.6 | Grok 4.6 (xhigh) seq - mean of 3 | 28.7 | 3 | xhigh | Grok Build CLI (ACP) | xAI | matched | `user-content-grok-46-xhigh-seq---mean-of-3` |
| gpt-5.6-luna | GPT-5.6 Luna (max effort) - mean of 3 | 31.3 | 3 | max | Codex CLI | OpenAI | matched | `user-content-gpt-56-luna-max-effort---mean-of-3` |
| gpt-5.5 | - | - | - | - | - | - | owner_result_missing | `-` |
| gemini-3.7-flash | - | - | - | - | - | - | variant_mismatch | `-` |
| glm-5.3-flash | GLM-5.3 Flash (max effort, Z.ai API) - mean of 3 | 17.7 | 3 | max | Claude Code / Z.ai API | Z.ai API | matched | `user-content-glm-53-flash-max-effort-zai-api---mean-of-3` |
| deepseek-v4-pro | DeepSeek V4-Pro (max effort, DeepSeek API) | 16.0 | 1 | max | Claude Code / DeepSeek API | DeepSeek API | matched | `user-content-deepseek-v4-pro-max-effort-deepseek-api` |
| claude-opus-4.8 | Opus 4.8 (max effort) | 15.0 | 1 | max | Claude Code | Anthropic | matched | `user-content-opus-48-max-effort` |
| qwen3.8-max | Qwen3.8-Max (max effort, Alibaba API) - mean of 3 | 25.7 | 3 | max | Claude Code / Alibaba API | Alibaba API | matched | `user-content-qwen38-max-max-effort-alibaba-api---mean-of-3` |
| muse-spark-1.2 | Muse Spark 1.2 (default effort, OpenRouter) | 14.0 | 1 | default | Claude Code / OpenRouter | OpenRouter | matched | `user-content-muse-spark-12-default-effort-openrouter` |
| claude-sonnet-5 | Sonnet 5 (max effort) | 9.0 | 1 | max | Claude Code | Anthropic | matched | `user-content-sonnet-5-max-effort` |
| deepseek-v4-flash | DeepSeek V4.1 Flash (max effort) - mean of 3 | 21.7 | 3 | max | Claude Code / DeepSeek API | DeepSeek API | current_route_alias | `user-content-deepseek-v41-flash-max-effort---mean-of-3` |
| gemini-3.6-flash | - | - | - | - | - | - | owner_result_missing | `-` |
| glm-5.2 | - | - | - | - | - | - | owner_result_missing | `-` |
| gemini-3.5-flash | - | - | - | - | - | - | owner_result_missing | `-` |
| gpt-6-sol | GPT-6 Sol MAX - mean of 3 | 29.3 | 3 | max | Codex CLI | OpenAI | matched | `user-content-gpt-6-sol-max-effort---mean-of-3` |
| gpt-6.1-sol | GPT-6.1 Sol (max effort) - mean of 3 | 44.3 | 3 | max | Codex CLI | OpenAI ChatGPT account | matched | `user-content-gpt-61-sol-max-effort---mean-of-3` |
| gpt-6-luna | GPT-6 Luna MAX - mean of 3 | 18.3 | 3 | max | Codex CLI | OpenAI | matched | `user-content-gpt-6-luna-max-effort---mean-of-3` |
| grok-4.7 | Grok 4.7 (xhigh) - mean of 5 | 29.0 | 5 | xhigh | Grok Build CLI (ACP) | xAI | matched | `user-content-grok-47-xhigh---mean-of-5` |
| mimo-v2-6-pro | MiMo-V2.6-Pro (first-party, thinking enabled) | 18 | 1 | enabled | Claude Code / Anthropic-compatible shim | Xiaomi first-party | matched | `user-content-mimo-v26-pro-first-party` |
| mimo-v2-6-flash | - | - | - | - | - | - | reasoning_variant_unverified | `user-content-mimo-v26-flash---mean-of-3` |
| claude-haiku-5-5 | Haiku 5.5 (xhigh effort) - mean of 3 | 18.3 | 3 | xhigh | Claude Code | Anthropic | matched | `user-content-haiku-55-xhigh-effort---mean-of-3` |
| claude-sonnet-5-5 | Sonnet 5.5 (max effort) - mean of 3 | 51.3 | 3 | max | Claude Code | Anthropic | matched | `user-content-sonnet-55-max-effort---mean-of-3` |
| gemini-4-argon | Gemini 4 Argon (high effort, Antigravity CLI) - mean of 3 | 40.7 | 3 | high | Antigravity CLI | Google | matched | `user-content-gemini-4-argon-high-effort-antigravity-cli---mean-of-3` |

## Changes versus the previous snapshot

Provenance changes common to every matched record (and the unmatched MiMo Flash record): `observedAt` set to 2026-10-18, `sourceCommit` and `sourceUrl` re-pinned to the new commit with `user-content-` anchors, `reportedOn` added/confirmed from the owner's run-notes date (unchanged where already present). Top level: `snapshotDate` 2026-09-30 -> 2026-10-17, `sourceCommit` and `sources` re-pinned, new full re-pin entry in `supplementalSourceCaptures` (earlier entries retained and marked superseded), `providerClaimAudit.repeatedOn` = null.

| Model id | Change | Previous | New |
|---|---|---|---|
| gpt-5.5 | note rewritten | see previous snapshot in git | see data/bug_hunt.json |
| gemini-3.7-flash | note rewritten | see previous snapshot in git | see data/bug_hunt.json |
| muse-spark-1.2 | note rewritten | see previous snapshot in git | see data/bug_hunt.json |
| deepseek-v4-flash | note rewritten | see previous snapshot in git | see data/bug_hunt.json |
| deepseek-v4-flash | availableOwnerConfigurations | 0 | 1 (DeepSeek V4.1 Flash 1017 mean of 5 = 39.4, unselected) |
| gemini-3.6-flash | note rewritten | see previous snapshot in git | see data/bug_hunt.json |
| glm-5.2 | note rewritten | see previous snapshot in git | see data/bug_hunt.json |
| gemini-3.5-flash | note rewritten | see previous snapshot in git | see data/bug_hunt.json |
| grok-4.7 | evaluatedModel | Grok 4.7 (xhigh) seq - mean of 4 | Grok 4.7 (xhigh) - mean of 5 |
| grok-4.7 | fixedOf105 | 28.8 | 29.0 |
| grok-4.7 | sampleN | 4 | 5 |
| grok-4.7 | note rewritten | see previous snapshot in git | see data/bug_hunt.json |
| claude-haiku-5-5 | New roster model, matched (xhigh effort) | - | 18.3/105, n=3, Haiku 5.5 (xhigh effort) - mean of 3 |
| claude-sonnet-5-5 | New roster model, matched (max effort) | - | 51.3/105, n=3, Sonnet 5.5 (max effort) - mean of 3 |
| gemini-4-argon | New roster model, matched (high effort) | - | 40.7/105, n=3, Gemini 4 Argon (high effort, Antigravity CLI) - mean of 3 |

Excluded results added: Gemini 3.7 Flash high-effort Antigravity rows (18, 16); Haiku 5.5 max (21.5, n=2), high (16, n=2), medium (12), low (11); Sonnet 5.5 xhigh (36), high (34.3), medium (23.3), low (19), all means of 3. Gemini 4 Argon Gemini CLI high single run (33), medium mean of 3 (39.3), low mean of 3 (35.3). Single-run Haiku max (22) and high (15) and Sonnet 5.5 single/mean-of-2 rows are superseded by the owner's means and not listed.

## Judgement calls to review

- **deepseek-v4-flash**: kept on the owner's DeepSeek V4.1 Flash (max) mean of 3 (21.7). The owner now also publishes DeepSeek V4.1 Flash 1017 (max) mean of 5 (39.4). DeepSeek's updates page says `deepseek-flash` serves the 1017 model, and that `deepseek-v4-flash` was routed to V4.1 Flash as of 2026-08-21; it does not say the old alias now routes to 1017. The 1017 result is stored as an unselected `availableOwnerConfigurations` entry. If the alias is confirmed to route to 1017, switching would raise this score to 39.4.
- **muse-spark-1.2**: the owner tags the 14/105 default-effort OpenRouter row 'Superseded' by the 17/105 Meta-API xhigh row, which the owner's own caveat calls a mixed-route result. Kept 14/105 as the single-route match per the matching policy.
- **grok-4.7**: updated from the mean of 4 (28.8, 'seq') to the owner's mean of 5 (29.0) of the same xhigh configuration; run 5 ran both repos concurrently (wall contended), score/cost unaffected.
- **claude-haiku-5-5**: selected variant is xhigh (AA frontier configurations medium/high/xhigh), matched to the owner's mean of 3 (16, 19, 20); effort was read off the wire, accepted, not magnitude-probed. Max (21.5) is excluded.
- **claude-sonnet-5-5**: AA 'max with fallback' mapped to the owner's '(max effort)' mean of 3 (51.3; 57, 54, 43), following the Opus 5.5 precedent (effort max, effortStatus max).
- **gemini-4-argon**: selected variant high; matched to the owner's Antigravity CLI mean of 3 (40.7; 40, 45, 37), the owner's current agent CLI and the same harness as Gemini 3.8 Flash. The owner's Gemini CLI single run (33) is a separate-harness row and excluded. High is the ceiling per the owner (API rejects max).
- **Unmatched (6)**: gpt-5.5, gemini-3.6-flash, glm-5.2, gemini-3.5-flash have no owner row; gemini-3.7-flash has only high-effort rows (cohort selects medium); mimo-v2-6-flash remains reasoning_variant_unverified. The 2026-09-29 provider-claim search was not repeated.
