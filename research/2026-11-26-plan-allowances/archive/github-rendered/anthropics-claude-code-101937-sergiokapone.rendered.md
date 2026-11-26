# NOT A BYTE-EXACT COPY (O165): text returned by the WebFetch tool for https://github.com/anthropics/claude-code/issues/101937
# fetched 2026-11-26 (UTC, between 03:40Z and 03:50Z); direct github.com and api.github.com requests were refused by the session proxy, so no raw page exists.
# Prompt given to the tool: quote verbatim the comment by user sergiokapone dated 2026-10-27. The text below is the tool's reply, saved unchanged.

Here is the comment by **sergiokapone** dated Oct 27, 2026, quoted verbatim:

> Adding a data point from a Pro plan (not Max). Same pattern as reported above: the 5-hour meter got much stricter, while the weekly one did not.
>
> **Environment**
>
> * Plan: Claude Pro
> * Claude Code 2.1.311, Windows
> * Models: Opus 5.5 (main session), Haiku 4.5, 1 Sonnet 5.5 request
>
> **What happened (27 Oct 2026, Kyiv time, UTC+2)**
>
> * Window started ~13:30, the 5h limit reached 100% at ~15:07 (reset 18:29)
> * /usage at that moment: weekly limit only 10% (resets Nov 3)
>
> **Local logs for 13:30-15:07**
>
> * Opus 5.5: 153 requests, ~97k output tokens, ~31M cache-read, ~1.2M cache-write
> * Haiku 4.5: 22 requests (~13k output total)
> * Sonnet 5.5: 1 request
> * API-equivalent cost of the whole window: roughly $13-14
>
> Per-30-minute breakdown (deduplicated by message id, local time):
>
> ```
> Slot  Model                     Requests OutputK CacheWrM CacheRdM
> ----  -----                     -------- ------- -------- --------
> 13:30 claude-haiku-4-5-20251001        1    0.20     0.01     0.00
> 13:30 claude-opus-5-5                 10    5.80     0.91     2.23
> 14:00 claude-haiku-4-5-20251001       21   12.90     0.67     0.00
> 14:00 claude-opus-5-5                130   84.90     0.23    25.75
> 14:30 claude-opus-5-5                 13    6.70     0.04     3.25
> 15:00 claude-sonnet-5-5                1    1.50     0.02     0.03
> ```
>
> **Sessions in that window (entrypoint from the session .jsonl)**
>
> * Main Opus session: entrypoint "cli" (interactive), ~150 requests. So this is not the sdk-cli metering issue from [[BUG] Headless `claude -p` (entrypoint `sdk-cli`) uses ~1.8× more of the 5-hour window per token than interactive `cli`, same workload #97074](https://github.com/anthropics/claude-code/issues/97074).
> * One old session resumed at 13:53: file is ~223 MB, ~850k cache-write on resume (4 requests).
> * 22 separate one-request sessions with entrypoint "sdk-ts" (Haiku) between 13:59 and 14:29, which I did not start manually; I'm still tracking down the source. They account for only ~13k output tokens in total.
> * No subagents, no parallel heavy sessions.
>
> Note: average cache-read per Opus request in this window is ~200k tokens (31M / 153), i.e. a large context. I'm aware this raises per-request cost, but I have not compared context sizes with 23-24 Oct yet.
>
> **Comparison, same machine and project, no early cutoff**
>
> * 23 Oct: ~$95 API-equivalent (Opus: ~876k output, ~308M cache-read)
> * 24 Oct: ~$250 API-equivalent (Opus: ~1.49M output, ~645M cache-read)
> * Windows then lasted ~3.5 h before the limit; now ~1.5 h.
>
> I know API-dollar figures are not the real quota, and I'm not claiming a confirmed change. But the gap is roughly 20x and I can't fully explain it with my own usage.
>
> **What I checked**
>
> * status.claude.com: the only incident that day (elevated errors for Sonnet 5.5, 09:14-09:56 UTC) ended before my window started and doesn't overlap.
> * Support (Fin bot) only replied that no change was announced and that no per-request log exists.
> * /usage shows this machine only, so I can't see usage from other surfaces.
>
> Possibly related: [#103437](https://github.com/anthropics/claude-code/issues/103437), [#97074](https://github.com/anthropics/claude-code/issues/97074), [#104614](https://github.com/anthropics/claude-code/issues/104614).
>
> **Questions**
>
> 1. Did anything change in how the 5h window is metered between 24 and 27 Oct (Opus weighting, cache reads, context size)?
> 2. Does resuming a very large old session (cache rewrite) count against the 5h window in a way that was different last week?
>
> /usage screenshot: [Image]

The comment's embedded /usage screenshot is omitted from this quote because it is only an image link.
