# MiniMax-M3.1-Flash reasoning effort (O135, read 2026-11-01)

AA plots MiniMax-M3.1-Flash (`https://artificialanalysis.ai/models/minimax-m3-1-flash`) without an effort. O135 names this
model with MiMo-V2.6-Flash: "each provider's documented effort levels and default are researched as for Kimi K3.1 Pro (O66),
and AA's plotted configuration is taken at the documented default". O140 settled MiMo-V2.6-Flash. MiniMax-M3.1-Flash left
the cohort at v5 before its research was done. It is back for one release under O145, so the research is done here.

## MiniMax's API documentation

Read at the time in `minimax/readAt.txt`. The pages' Markdown is saved in `minimax/`.

1. **OpenAI-compatible Chat Completions.** https://platform.minimax.io/docs/api-reference/text-openai-api
   (`minimax/api-reference_text-openai-api.md`):
   - `reasoning_effort`: "Thinking depth, effective for `MiniMax-M3.1-Flash` only. Accepts `low`, `medium`, `high`, `xhigh`,
     and `max`; higher levels think more thoroughly. Defaults to `max` when omitted. `none` is not supported."
   - `thinking`: "`MiniMax-M3.1-Flash` always thinks and returns `400` if `disabled` is sent."
2. **Anthropic-compatible Messages.** https://platform.minimax.io/docs/api-reference/text-anthropic-api
   (`minimax/api-reference_text-anthropic-api.md`). `output_config.effort`: "Tunes thinking depth for `MiniMax-M3.1-Flash`.
   Accepts `low`, `medium`, `high`, `xhigh`, and `max`; defaults to `max` when omitted."
3. **Text-generation guide.** https://platform.minimax.io/docs/guides/text-generation
   (`minimax/guides_text-generation.md`):
   - "Thinking is **on by default and needs no configuration**."
   - "For `MiniMax-M3.1-Flash`, omitting `effort` defaults to `max`."

## Finding

MiniMax documents a graded effort ladder: low, medium, high, xhigh and max. **Max is the default.** Thinking cannot be
disabled. This is the same shape as Moonshot's documentation for Kimi K3.1 Pro (O66), not Xiaomi's on/off switch (O140).
Under O135, AA's plotted configuration is therefore **MiniMax-M3.1-Flash at max**.

Rows labelled max are matched as exact:

- Vals: `compute_effort` max. Vals' model page says the run used "the official MiniMax API at ... compute effort max".
- LiveBench: the site's model metadata gives effort "max".
- AI Coding Daily: "MiniMax M3.1-Flash (Max)".

The owner has not yet confirmed this outcome. O140 confirmed the equivalent outcome for MiMo-V2.6-Flash.
