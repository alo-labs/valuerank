I'll look up Xiaomi's current MiMo plan fees and API rates, then search for actual subscriber usage reports rather than marketing quotas.
Official fees and credit rules are up. Next I’ll pull the full rate tables and look for subscriber-reported token usage, not marketing quotas.
No measured value multiple exists for MiMo-V2.6-Pro or MiMo-V2.6-Flash on any Token Plan tier. The only in-window subscriber measurements are a one-day Pro token split with no plan fee, and a partial Pro-plan credit balance with no model split. Neither can be turned into a billing-period multiple.

Measured usage

Searches of Xiaomi’s docs, Reddit, Linux.do, V2EX, Zhihu, Bilibili, Hacker News, and GitHub issues for Claude Code, Codex, Cline, Roo, Kilo, and OpenCode did not find a subscriber who reported a full billing period of MiMo-V2.6-Pro or MiMo-V2.6-Flash use, with a plan fee, and with tokens that can be priced at Xiaomi’s API rates.

Point	Date	Window	Plan and fee	Model	Reported use	API-priced value	Multiple
A	2026-10-13	One day, not a billing period	Token Plan, Singapore endpoint. Tier and fee not stated	mimo-v2.6-pro	Xiaomi dashboard: 19,829,403 cache-miss input, 4,441,344 cache-hit input, 89,906 output (24,360,653 total). Local Codex logs are within about 1%	$8.72 at overseas real-time rates, or ¥60.14 at China rates. Computed as miss × $0.435 + hit × $0.0036 + output × $0.87 per million	Not computable. No fee
B	2026-10-07	Open period ending 2026-11-05 23:59:59. Not finished	Pro. Console planCode pro, limit 38,000,000,000 credits. Amount paid not stated. List fee is $50 or ¥329	Unidentified mix. Plan-level only	14,954,038,035 credits used (39.35%)	If those credits were all V2.6-Pro cache-miss or output: about $21.68. All Flash: about $20.94. China rates, either model: ¥149.54. Not a token measurement	Not a period multiple. Window incomplete, fee unpaid amount unknown, model unknown

Source for A: 
 #53752 — GitHub, openai/codex#53752
. Source for B: 
 #15753 — GitHub, OmniRoute#15753
.

No qualifying completed-period measurement exists for MiMo-V2.6-Pro, MiMo-V2.6-Flash, or any Lite, Standard, Pro, or Max tier. OpenCode’s public token totals are platform-wide traffic, not one subscriber’s Token Plan bill, so they are excluded.

Older reports, all before V2.6 and not usable as a V2.6 multiple: a May 2026 Lite subscriber reported 21,102,155 of 60,000,000 “tokens” with no input/output split (
review
); a DataCamp author hit about half a promotional Lite quota in three hours on V2.5-Pro with no token count (
tutorial
); an HN commenter burned 31% of a $16 plan in one to two hours on V2.5, again with no token split (
HN
). Those used the pre-27 May 2026 credit system or mislabeled credits as tokens.

Plan fees

Official individual and team Token Plan, docs updated 21 October 2026. Live checkout page checked 23 October 2026. Token Plan quota does not draw the pay-as-you-go balance. UltraSpeed is not in the supported-model list.

Tier	Monthly list	Annual list	Monthly credits	Annual credits
Lite, individual only	$6 or ¥39	$63.36 or ¥408	4.1 billion	49.2 billion
Standard	$16 or ¥99	$168.96 or ¥1,044	11 billion	132 billion
Pro	$50 or ¥329	$528 or ¥3,468	38 billion	456 billion
Max	$100 or ¥659	$1,056 or ¥6,948	82 billion	984 billion

Team is the same per seat for Standard, Pro, and Max. No Lite seat. Annual team credits reset monthly per seat at the monthly amount, not as one yearly lump. First personal purchase is 12% off once. Annual is 12% off versus twelve monthly payments, and the first-purchase discount does not stack. Off-peak, 00:00–08:00 Beijing time, credit burn is 0.8×. Unused credits do not carry past expiry. Refunds are not offered. The plan is limited to coding tools. TTS is free for a limited time and does not burn credits.

Sources: 
Individual Subscription
, 
Token Plan price page
, 
checkout
.

MiMo Desktop membership ($20 / $60 / $200 / $400) is a different product, not this Token Plan.

API rates

No context-length price tiers are published for V2.6. Cache writes are limited-time free. Web search is extra ($5 or ¥16 per 1,000 calls) and is not in the token price. English pricing page dated 8 October 2026; Chinese page dated 21 October 2026. The V2.6 numbers match.

Model	Cache-hit input	Cache-miss input	Output
mimo-v2.6-pro, real-time, overseas	$0.0036 / M	$0.435 / M	$0.87 / M
mimo-v2.6-flash, real-time, overseas	$0.0028 / M	$0.14 / M	$0.28 / M
mimo-v2.6-pro-ultraspeed, real-time, overseas	$0.036 / M	$4.35 / M	$8.70 / M
mimo-v2.6-pro, batch, overseas	$0.0018 / M	$0.2175 / M	$0.435 / M
mimo-v2.6-flash, batch, overseas	$0.0014 / M	$0.07 / M	$0.14 / M
mimo-v2.6-pro, real-time, China	¥0.025 / M	¥3.00 / M	¥6.00 / M
mimo-v2.6-flash, real-time, China	¥0.02 / M	¥1.00 / M	¥2.00 / M
mimo-v2.6-pro-ultraspeed, real-time, China	¥0.25 / M	¥30.00 / M	¥60.00 / M
mimo-v2.6-pro, batch, China	¥0.0125 / M	¥1.50 / M	¥3.00 / M
mimo-v2.6-flash, batch, China	¥0.01 / M	¥0.50 / M	¥1.00 / M

Token Plan burn, same on individual and team, per token:

Model	Cache hit	Cache miss	Output
mimo-v2.6-pro	2.5 credits	300 credits	600 credits
mimo-v2.6-flash	2 credits	100 credits	200 credits

Sources: 
English API pricing
, 
Chinese API pricing
, 
subscription credit table
.

Provider claims, not measurements

These are Xiaomi’s quotas and task slogans, not observed use. Do not read the ceiling column as a measured multiple.

Claimed monthly task rounds, using mimo-v2.6-flash as the baseline: Lite about 200, Standard about 1,600, Pro about 5,600, Max about 12,800. Annual is described as about 12× that. Xiaomi does not define a “round” in tokens.

Credit rates are pegged to API price. In China, every token type on both V2.6 models is exactly ¥10 of API value per billion credits. Overseas, Flash is $1.40 per billion credits. Pro cache-miss and output are $1.45 per billion. Pro cache-hit is $1.44 per billion. If someone used 100% of a monthly quota at peak rates, the API-equivalent ceiling would be:

Tier	China, either V2.6 model	Overseas, all Pro miss/output	Overseas, all Flash
Lite, ¥39 or $6	¥41, about 1.05×	$5.95, about 0.99×	$5.74, about 0.96×
Standard, ¥99 or $16	¥110, about 1.11×	$15.95, about 1.00×	$15.40, about 0.96×
Pro, ¥329 or $50	¥380, about 1.16×	$55.10, about 1.10×	$53.20, about 1.06×
Max, ¥659 or $100	¥820, about 1.24×	$118.90, about 1.19×	$114.80, about 1.15×

That ceiling is arithmetic on the published quota, not a measurement. A 12% discount raises it by 1/0.88. All-off-peak use raises it by 1/0.8, because the same tokens cost fewer credits. Unused credits expire, so a real multiple would be that ceiling times the share actually consumed. No in-window report shows that share for a finished period.