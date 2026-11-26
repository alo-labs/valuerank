As of 2026-10-23, the measured value multiple is undetermined for both MiMo-V2.6-Pro and MiMo-V2.6-Flash, at every current Xiaomi Token Plan tier. I found actual user-reported usage and API-equivalent cost observations, but none that establishes all the inputs needed for your calculation: a known plan fee, consumption within a defined billing period, and a defensible API-priced numerator attributable to the exact model.

The closest recent evidence consists of a Linux.do subscriber’s ¥17 API-cost estimate, detailed V2.6 token counts in a GitHub bug report, and a developer’s API-equivalent costing of tests through a Token Plan endpoint. Each has material gaps, documented below. None supports a publishable “this plan delivers X×” result.
linux
+2

1. Qualifying end-user results
Fully qualifying measurements: none found

“Not established” means no qualifying public measurement was found in this research—not that the multiple is zero, or that no such private measurement exists.

Edition and tier	MiMo-V2.6-Pro measured multiple	MiMo-V2.6-Flash measured multiple
Individual Lite	Not established	Not established
Individual Standard	Not established	Not established
Individual Pro	Not established	Not established
Individual Max	Not established	Not established
Team Standard	Not established	Not established
Team Pro	Not established	Not established
Team Max	Not established	Not established

This finding applies to both monthly and annual subscriptions. The evidence below does not justify extrapolating a partial session to a month, treating the published allowance as consumed usage, or assigning mixed-model consumption to either V2.6 variant.

Recent end-user evidence: 2026-09-22 through 2026-10-23

These are partial observations, not qualifying value-multiple data points.

Report and date	Plan tier / actual fee	Measurement window and model attribution	Actual reported usage / API-priced value	Why no multiple can be calculated
Linux.do, sun_omg, “关于mimo-2.6计费,” 2026-09-28. 
Direct URL
	Xiaomi Token Plan; tier and paid fee not established	Describes “one month” of Telegram auto-reply usage. The text discusses switching to 2.6 Flash; it does not securely identify the model responsible for the measured usage.	Says a usage screenshot is attached and that an AI calculated ordinary API usage would cost ¥17. The indexed text says Flash “output costs ¥1,” whereas Xiaomi’s current real-time output rate is ¥2/M. 
linux
+2
	No confirmed denominator, no securely matched model, and no auditable token split. Full-page retrieval failed, so the screenshot could not be checked. The ¥17 is an unverified user estimate, not an accepted numerator.
GitHub, Water-Run, MiMo-Code issue #2482, 2026-09-22. 
 #2482 — Direct URL
	No tier or fee. A later comment explicitly confirms Token Plan use for the repaired workload, but does not unambiguously tie the earlier measured generation to a particular subscription.	Flash generation, 10:05:51–11:05:51 CST on Sept. 22; subsequent step also recorded. Separate Pro session lacks comparable token totals.	Flash generation: 9,797 input and 127,952 output tokens, with 48 reasoning tokens reported. Next step: 1,028,090 input, zero output. Cache split is not supplied. Counts came from the local session database and worker log. 
github
	No fee or billing-period total; cache treatment is incomplete. The initial failure and later successful Token Plan workload must not be silently combined.
GitHub, trick77/llmwire, live probes dated 2026-09-22. 
Direct URL
	Explicitly uses a MiMo Token Plan host; tier and fee absent	Sept. 22 test runs, not an identified subscription billing window. Initial run includes V2.5 controls plus both V2.6 variants; subsequent tests mix V2.6-Pro and Flash.	About 63 calls, roughly $0.065 API-equivalent for the onboarding run; a further 46 calls, roughly $0.034, for effort/toggle tests. The author explicitly prices Token Plan traffic at vendor PAYG USD list rates rather than treating it as an invoice. 
github
	A useful actual API-equivalent usage observation, but no denominator, billing-cycle consumption, or model-by-model cost allocation. It stays at mixed-plan/test-run level.
Reddit, PilgrimofHaqq2 comment in a thread dated 2026-10-06. 
Direct URL
	Explicitly says Xiaomi Max plan; actual payment not given	MiMo 2.6 Pro A/B testing; duration unspecified	Qualitative account of using Pro through Max; no token counts, requests, or API-priced consumption. 
reddit
	Confirms a real Max/Pro user, but supplies no numerator.

The Linux.do report also describes automated Telegram replies. Xiaomi’s current terms restrict Token Plan usage to coding tools and prohibit clearly non-coding automated-script or application-backend usage. Consequently, even a complete measurement of that workload would need a permitted-use caveat before being presented as reproducible buyer value.
mimo.mi

Older reports, kept separate
Report date and direct source	Reported plan / model / window	Reported usage	Why excluded from the current multiple
2026-04-03, 
Reddit: Token Plan introduction
	Exact paid tier and model not securely identified; 20-minute implementation	19 million credits consumed. 
reddit
	Older generation and credit scheme; credits are not a cache/input/output token breakdown. No defensible API-priced numerator.
2026-05-01 thread, 
Reddit: MiMo-V2.5-Pro
	$50 plan; explicitly V2.5-Pro; approximately five hours, during off-peak usage	Dashboard consumption reported as 74,549,003 out of 700,000,000, described as 11%. 
reddit
	V2.5-Pro, not V2.6-Pro. No sufficient input/cache/output split; not a complete billing-period measurement.
2026-05-04, 
Reddit: ZedEditor discussion
	Original poster: tier unclear, V2.5-era discussion, ten small tasks. Separate commenter: tier/model unspecified, a little over three weeks, with an intervening account reset	Original poster: about 12M credits. Separate commenter: 600M tokens. 
reddit
	These are different users and cannot be joined. Neither supplies the fee, clean billing window, and token mix required for a multiple.
2026-05-27, 
Reddit: “4.1B for $6”
	$6 Lite; exact model and measurement boundaries not established from the retrievable material	Indexed excerpt: “82 million tokens used for a flat $6.00.” 
reddit
	Total tokens alone cannot establish API value without the model and token categories. Full-page retrieval failed, so I did not promote the excerpt into a qualifying measurement.

I also found an apparently strong older API measurement—387,380,436 tokens, including 373,124,480 cache-hit tokens, costing $70.12—but its author explicitly describes ordinary V2.5-Pro API usage, not consumption under a Xiaomi subscription. It therefore cannot supply a Token Plan numerator. 
Direct URL
reddit

2. Current official plan fees

These are Xiaomi’s published fees, checked for this answer on 2026-10-23. USD and CNY are separate regional price schedules, not currency conversions.

Individual Token Plan

The official individual subscription documentation is dated 2026-10-21. 
Official English page
 · 
Official Chinese page
.
mimo.mi
+1

Tier	Monthly fee, USD	Monthly fee, CNY	Annual fee, USD	Annual fee, CNY
Lite	$6/month	¥39/month	$63.36/year	¥408/year
Standard	$16/month	¥99/month	$168.96/year	¥1,044/year
Pro	$50/month	¥329/month	$528/year	¥3,468/year
Max	$100/month	¥659/month	$1,056/year	¥6,948/year

All fees above are directly transcribed from Xiaomi’s current table. In particular, the CNY annual prices should not be replaced with a calculated 12%-discount figure: Xiaomi describes approximately that discount, but its published CNY amounts do not exactly equal monthly price × 12 × 0.88.
mimo.mi
+1

Individual first purchases receive 12% off once per account; the first-purchase discount does not stack with annual subscriptions. For a measured multiple, the denominator should be the subscriber’s actual paid fee, not automatically the list price.
platform.xiaomimimo

Team Token Plan

The official team documentation is dated 2026-09-22. Team has Standard, Pro and Max—no Lite—and requires at least two seats. 
Official documentation
 · 
Official purchase page
.
mimo.mi
+1

Tier	Monthly fee per seat, USD	Monthly fee per seat, CNY	Annual fee per seat, USD	Annual fee per seat, CNY
Standard	$16	¥99	$168.96	¥1,044
Pro	$50	¥329	$528	¥3,468
Max	$100	¥659	$1,056	¥6,948

Team annual subscriptions are paid annually but reset each seat’s quota monthly. Team subscriptions do not receive the individual first-purchase discount. One-time purchases covering 1–12 months are also supported, with annual-package pricing available for a 12-month purchase.
mimo.mi

This table concerns Xiaomi’s API-platform Token Plan, not MiMo Desktop’s separate membership or third-party subscriptions such as OpenCode Go.

3. Xiaomi’s current PAYG API rates

Xiaomi’s fetched API pricing page displays “Update Time October 08, 2026.” The official V2.6 launch article dated 2026-09-22 independently lists the same real-time USD rates. 
Official API pricing
 · 
Official Chinese pricing
 · 
V2.6 launch article
.
mimo.mi
+2

Real-time API—the relevant default comparison

All prices are per million tokens.

Model	Region / currency	Uncached input	Cached input	Output	Published context-length price tiers
MiMo-V2.6-Pro	Overseas / USD	$0.435	$0.0036	$0.87	None listed
MiMo-V2.6-Pro	China / CNY	¥3.00	¥0.025	¥6.00	None listed
MiMo-V2.6-Flash	Overseas / USD	$0.14	$0.0028	$0.28	None listed
MiMo-V2.6-Flash	China / CNY	¥1.00	¥0.02	¥2.00	None listed

The current official price table does not publish separate ≤256K and >256K rates for these two V2.6 models. Older context-tier pricing should not be carried forward into this comparison. Cache writes are free for a limited time; web search is billed separately and is not included in token prices.
platform.xiaomimimo

Batch API—separate, non-real-time comparison
Model	Region / currency	Uncached input / M	Cached input / M	Output / M
MiMo-V2.6-Pro	Overseas / USD	$0.2175	$0.0018	$0.435
MiMo-V2.6-Pro	China / CNY	¥1.50	¥0.0125	¥3.00
MiMo-V2.6-Flash	Overseas / USD	$0.07	$0.0014	$0.14
MiMo-V2.6-Flash	China / CNY	¥0.50	¥0.01	¥1.00

These are official Batch rates, not the appropriate default valuation of interactive coding-plan traffic.
platform.xiaomimimo

For a qualifying report, with token quantities expressed in millions, the real-time numerator would be:

𝑉
A
P
I
=
𝐼
u
n
c
a
c
h
e
d
𝑃
i
n
p
u
t
+
𝐼
c
a
c
h
e
d
𝑃
c
a
c
h
e
d
+
𝑂
𝑃
o
u
t
p
u
t
V
API
	​

=I
uncached
	​

P
input
	​

+I
cached
	​

P
cached
	​

+OP
output
	​


The measured multiple is then 
𝑉
A
P
I
/
𝐹
a
c
t
u
a
l
l
y
 
p
a
i
d
V
API
	​

/F
actually paid
	​

, using matching currencies and the same billing period. A request count alone is insufficient unless the reporter supplies its API-priced cost or enough token data to price those requests.

4. Provider-claimed allowances—not measured consumption

The following figures come from Xiaomi. They are not end-user measurements and have not been used to produce a measured multiple.

Published quotas and task-count claims
Tier	Individual monthly quota	Individual published annual total	Team quota per seat/month, including annually paid seats	Xiaomi’s approximate monthly task claim, using V2.6-Flash
Lite	4.1B credits	49.2B credits	Not offered	200 medium-to-complex task rounds
Standard	11B credits	132B credits	11B credits	1,600 rounds
Pro	38B credits	456B credits	38B credits	5,600 rounds
Max	82B credits	984B credits	82B credits	12,800 rounds

Individual quota and task claims come from the Oct. 21 documentation; team quotas and task claims come from the Sept. 22 documentation. The published individual annual total must not be confused with the team arrangement, which explicitly resets monthly.
mimo.mi
+1

Published credit deduction rules
Model	Credits per cached-input token	Credits per uncached-input token	Credits per output token
MiMo-V2.6-Pro	2.5	300	600
MiMo-V2.6-Flash	2	100	200

Xiaomi applies a 0.8× credit-consumption coefficient during 00:00–08:00 Beijing time, equivalent to 16:00–24:00 UTC. Both variants consume the same subscription’s shared credit allowance; they do not each receive a separate full allowance. 
Official usage-and-quota page
.
mimo.mi

Xiaomi also advertises “no weekly cap” and “no 5-hour cap.” That does not mean unmetered usage: the documentation says service stops when the applicable quota is exhausted.
mimo.mi
+2

I have deliberately not turned these quotas into a theoretical maximum-value multiple. Such a calculation would answer a different question from your requested realized, end-user-measured value.

5. Evidence assessment and search limitations

The main evidence problem is not missing official prices; those are available. It is the lack of a public report joining consumption, billing period, exact model and actual fee.

The English- and Chinese-language searches covered Reddit—including the requested subreddits—X, V2EX, Linux.do, Zhihu, Bilibili, Hacker News, and GitHub issues involving MiMo and coding-agent integrations. Several relevant Linux.do and Reddit pages failed full-text retrieval. I have explicitly identified excerpt-only evidence rather than treating unseen screenshots as verified.

Two additional distinctions matter:

A statement such as “¥329 buys ¥380 of API allowance” is an allowance conversion, not proof that a subscriber actually consumed ¥380. A Sept. 22 V2EX discussion contains exactly that type of comparison, without the required consumption measurement. 
Direct URL
.
v2ex

Older V2.5 usage cannot be relabelled V2.6. Xiaomi says requests using V2.5 model IDs began auto-routing to V2.6 on Oct. 14, before those IDs were retired Oct. 21; a report spanning that migration would require additional attribution rather than a silent model substitution.
platform.xiaomimimo

Accordingly, there is no defensible current measured X× figure to report for either model or any tier from the public evidence located here. The official fee, rate and allowance tables are established; the requested realized-value numerator remains unestablished.