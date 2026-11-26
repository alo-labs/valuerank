# NOT A BYTE-EXACT COPY (O165): text returned by the WebFetch tool for https://github.com/anthropics/claude-code/issues/105621
# fetched 2026-11-26 (UTC, between 03:40Z and 03:50Z); direct github.com and api.github.com requests were refused by the session proxy, so no raw page exists.
# Prompt given to the tool: quote verbatim the comment by user smaug42 dated 2026-11-02 (and JCorners68's if present). The text below is the tool's reply, saved unchanged.

**smaug42, Nov 2, 2026:**

> Same pattern here. Claude Pro, Linux, Opus 5.5, unchanged workflow (one task per session, /clear between tasks).
>
> ccusage (local logs) shows Claude token volume of ~$60–140/day API-equivalent Oct 12–21, rising to ~$180–270/day from Oct 25 (versions 2.1.304→2.1.310), with cache creation <1% of cache reads throughout.
>
> Despite that volume, last week I used well under 5% of my weekly limit per day. Today (2.1.311), a single task of ~99M tokens ( approx $32 API-equivalent, 07:30–08:50 PT) used 16% of the 5-hour session and 3% of the weekly limit. At today’s rate, my Oct 25–29 volume would have exceeded the full weekly limit, which it did not.

**JCorners68, Oct 30, 2026:**

> Same regression, with measured numbers. This is a subscription-cancellation-severity bug and needs to be made right.
>
> Linux CLI, Max, Opus 5.5. I upgraded to Opus to get a higher-quality result on a design task, and had stopped using Claude Code for 5 hours beforehand, so the window was fresh.
>
> I typed one request: "redesign a page." That one request consumed 26% of my session in under a minute.
>
> I did not choose how many model calls, tool calls or tokens it would use, and I have no way to see or cap that before it happens. The engine decides all of it. From my local transcript: 48 calls on Opus 5.5 over a context of about 156k tokens, roughly 5.07M cache-read tokens, 424k cache-creation tokens, 75k output tokens.
>
> Those token counts are Anthropic's own unit, produced by the tool, and the conversion from them to my session percentage is not published, so I cannot audit it. Pointing at tokens as the cost when the user neither controls nor can verify them is circular. A user cannot be expected to budget for a cost the tool decides on its own.
>
> If one sentence from the user can use a quarter of a paid session, the plan is not usable for coding. This matches #102667, #105725, #92544 and the reports linked above. Please confirm whether metering or plan limits changed in October 2026, publish how cache-read tokens are weighted against the session limit, add hard per-prompt limits and a visible cost estimate, and make affected users whole. I will cancel if this isn't fixed.
