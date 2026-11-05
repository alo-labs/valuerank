# Stage 1 (plain web search), Google AI plans — 2026-10-25

Summary: two qualifying Gemini 4 Argon reports, both Google AI Pro ($19.99/month) in Antigravity, both on the Google AI
developer forum (2026-10-19..23); none on Ultra, Gemini CLI, Jules or Code Assist. At Argon's introductory list price
they put Pro's separate weekly Argon quota at ≈$8.5/week and ≈$12.3/week (≈$37–54/month).

Gemini 4 Argon API (https://ai.google.dev/gemini-api/docs/pricing, 2026-10-25), Standard per 1M: $2.00 input / $0.10
cached / $10.00 output (incl. thinking) to 2026-11-30, then $4.00 / $0.20 / $20.00. Gemini 3.8 Flash $0.75 / $0.075 /
$3.75 to 2026-12-31.

## Qualifying (Gemini 4 Argon)
A. Muhammed_Alpler, https://discuss.ai.google.dev/t/190608, 2026-10-19 05:56Z. AI Pro, Antigravity, gemini-4-argon High:
   "2.61M total tokens ($0.864 wholesale API value) drained ~10.2% of the weekly pool" (baseline "$2.00/1M in, $10.00/1M
   out, $0.10/1M cached read") → ≈$8.47/week. No token split; single session; the post doubles as advocacy.
B. Faheem_Anis1, https://discuss.ai.google.dev/t/191879, 2026-10-23 14:54Z. AI Pro, Antigravity, LiteLLM, "Gemini Argon 4
   (Low)": "Requests: 16 / Fresh input: 185,443 / Output: 19,961 / Cache read: 1,684,364"; quota "Gemini 4 Argon Weekly
   Limit 94%" (6% used) → $0.739 / 0.06 ≈ $12.3/week (whole-percent display: ≈$11.4–13.4).

## Gemini 3.8 Flash (separate)
C. Faheem_Anis1, https://discuss.ai.google.dev/t/183629, 2026-09-18: 5,660,840 input / 48,601,098 cache / 182,640 output
   (≈$8.58) over several days against a just-reset weekly meter; the author's "$214 weekly" does not reproduce.
   Indicative only.

## Near-misses (percentages only)
HN: robertlane0 (OpenCode plan, not first-party), equasar, RGS1811, SwellJoe. Forum: t/190078 (RobW), t/188900 #14 and
t/190841 (Terabyte), t/192044 (DeSinc: VS Code extension cache-busting), t/186386, t/191634, t/190487, t/189381 #13,
t/192066 (Ultra, AI Studio). SmartScope (Ultra 5-hour 0.00% after ≈30 minutes, no tokens); cortexkit/insula #39
(`gemini-argon-wtu-weekly`, windowMinutes 10080); tddworks/ClaudeBar #646.

## Provider-published
Forum staff (t/189395, t/188900 #9): "a separate weekly-only Argon quota on top of your existing Gemini quota for 3.8
Flash" on paid Pro; Argon thinking Low / Medium / High; trials excluded; no numeric quota. antigravity.google/docs/plans:
Ultra "the highest, most generous quota, refreshed every five hours"; Pro "refreshed every five hours until the weekly
limit is reached"; no numbers. Gemini CLI quota page: requests per day (AI Pro 1,500, Ultra 2,000, …) and "Gemini CLI has
not been optimized for Gemini 4 Argon. To use Gemini 4 Argon, please use Antigravity." Jules: 15 / 100 / 300 tasks per day
(free / Pro / Ultra; Argon not confirmed).

## Unreachable
Reddit (403); GitHub search (blocked); X posts (snippets only); forum JSON rate-limited (raw endpoint used); YouTube not
searched.
