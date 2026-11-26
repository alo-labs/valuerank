# NOT A BYTE-EXACT COPY (O165): text returned by the WebFetch tool for https://github.com/anthropics/claude-code/issues/106375
# fetched 2026-11-26 (UTC, between 03:40Z and 03:50Z); direct github.com and api.github.com requests were refused by the session proxy ("GitHub access to this repository is not enabled for this session"), so no raw page exists.
# Prompt given to the tool: quote verbatim the comment by user douflou dated 2026-11-03. The text below is the tool's reply, saved unchanged.

Here is the comment by douflou dated Nov 3, 2026, quoted verbatim:

> Controlled measurement on a Max plan (2026-11-02/03, Claude Code 2.1.316, Opus 5.5, effort medium), in case it helps narrow this down.
>
> **Setup.** The same fixed task (read six frozen public text files, ~100k tokens, then write a summary), run as 12 fresh sessions per pass, with identical project-only settings (`--setting-sources project`), claude.ai connectors disabled, no subagents, no advisor. Each prompt carried a unique nonce, so cache writes were comparable across paths (~2.0M cache-write tokens per pass on every path). The 5-hour utilization was read before and after each pass through the Agent SDK usage endpoint, which makes no model call. Passes were interleaved over one night to rule out drift.
>
> | Pass | Path (entrypoint) | API-equivalent cost | 5h meter | 5h points per $10 | 5h points per 1M cache-write tokens |
> |---|---|---|---|---|---|
> | 1 | interactive TUI (`cli`) | $20.46 | 16 → 26 % | 4.9 | 4.9 |
> | 2 | `claude --no-session-persistence -p` (`sdk-cli`) | $19.83 | 26 → 45 % | 9.6 | 9.4 |
> | 3 | Agent SDK TS (`sdk-ts`) | $19.88 | 45 → 64 % | 9.6 | 9.4 |
> | 4 | interactive TUI (`cli`) | $20.38 | 64 → 74 % | 4.9 | 4.9 |
> | 5 | `claude --no-session-persistence -p` (`sdk-cli`) | $20.03 | 74 → 93 % | 9.5 | 9.4 |
> | 6 | Agent SDK TS (`sdk-ts`) | $19.74 | 0 → 19 % | 9.6 | 9.3 |
> | 7 | interactive TUI with `CLAUDE_CODE_ENTRYPOINT=sdk-cli` | $20.12 | 5 → 25 % | 9.9 | 9.9 |
>
> **Findings.**
>
> * For the same work, non-interactive paths (`claude --no-session-persistence -p`, Agent SDK) consume the 5-hour limit about **1.95×** faster than the interactive TUI. Both repetitions of each path agree to within 0.1 point per $10.
> * Pass 7 is the same interactive TUI, with only the entrypoint env var changed. It is metered like the SDK paths, so the multiplier appears to follow the **declared entrypoint**, not the execution mode or the token mix.
> * Weekly utilization moved 3 points per path in total (about $40 of work each). No difference is visible at the meter's 1-point resolution; a 2× difference would have shown, a smaller one might not.
>
> **Caveats.** Pass 7 is a single pass, run the next morning, with no same-morning TUI control. The interactive TUI started from a larger initial context (26k tokens, versus 15k and 13k). That works against the observed gap, not for it: the TUI read more tokens and cost slightly more, yet used less of the meter.
>
> This matches what Theo (t3.gg) reported on X on Oct 25. If the 5-hour multiplier for SDK and `-p` usage is intentional, documenting it would help; Remote Control sessions also run in `--print` mode, so they appear to be metered the same way. Session IDs are available on request.
