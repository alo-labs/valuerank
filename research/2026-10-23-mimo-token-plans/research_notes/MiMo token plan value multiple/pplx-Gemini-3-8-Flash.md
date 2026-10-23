Xiaomi's MiMo Token Plans do not provide outsized subscription value multiples (such as 3x–10x); instead, they function as prepaid credit bundles that yield a measured and mathematical maximum value multiple between 1.05x and 1.24x at normal daytime rates, and up to 1.55x during off-peak night hours. Because Xiaomi's quota conversion rate pegs 100 million Credits directly to ¥1.00 (or ~1 billion Credits to $1.45) of pay-as-you-go API consumption across both mimo-v2.6-pro and mimo-v2.6-flash, plan allowances strictly constrain API-equivalent value to the purchased credit cap.
mimo.mi
+2

End-User Measurements and Value Multiples

Within the qualifying window following the release of the MiMo-V2.6 series (September 22, 2026 to October 23, 2026), no public end-user report documents a completed, 100% exhausted monthly billing cycle for mimo-v2.6-pro or mimo-v2.6-flash. Available end-user reports reflect partial consumption runs, single-task measurements, or older V2.5 usage.
v2ex
+1

User & Platform	Tier & Price	Date & Window	Model Variant	Usage Reported	API Value & Computation	Computed Value Multiple	Source Link
mimiga (V2EX) 
v2ex
	Lite (¥39 / mo)	2026-09-22 (single session)	MiMo-V2.6-Pro (thread context)	52,841,980 Credits consumed (1.0% of plan); 1,542,683 total tokens	¥0.5284 (52.84M credits × ¥1.00 / 100M credits)	0.0135x (partial run against full fee; max plan ceiling is 1.051x)	
V2EX Thread #1243834
 
v2ex

Linux.do Topic 2258823 
linux
	Pro (¥329 / mo)	2026-05-28 (older, 1-day run)	MiMo-V2.5-Pro (legacy)	350M tokens used; ~4.7B credits equivalent	~¥47.00 (derived from credit consumption)	0.143x (partial daily run against monthly fee)	
Linux.do Topic #2258823
 
linux

Wcowin (V2EX) 
v2ex
	Standard / Promo (100T Plan)	2026-04-29 (older, single task)	MiMo-V2.5-Pro (legacy)	1,736,656 tokens (144.6k in, 10.8k out, 517.1k cached)	$1.25 (API rate equivalent reported by user)	N/A (promotional grant, not a cash plan)	
V2EX Thread #1209234
 
v2ex

Community analyses on developer forums (including V2EX and Linux.do) verify that because Xiaomi sets 1 Credit = ¥0.00000001 (100M Credits = ¥1.00), subscribers cannot extract surplus value beyond the nominal credit allocation unless they run tasks during off-peak hours.
v2ex
+2

Official Token Plan Tiers

Xiaomi offers four subscription tiers under its Token Plan, split into Individual and Team editions. Quotas are distributed in "Credits" valid across all supported models.
mimo.mi

Plan Tier	Individual Monthly Fee	Individual Annual Fee	Team Monthly Fee (per seat)	Team Annual Fee (per seat)	Monthly Credit Quota	Annual Credit Quota
Lite	$6.00 / ¥39.00	$63.36 / ¥408.00	N/A (Individual Only)	N/A	4.1 Billion Credits	49.2 Billion Credits
Standard	$16.00 / ¥99.00	$168.96 / ¥1,044.00	$16.00 / ¥99.00	$168.96 / ¥1,044.00	11.0 Billion Credits	132.0 Billion Credits
Pro	$50.00 / ¥329.00	$528.00 / ¥3,468.00	$50.00 / ¥329.00	$528.00 / ¥3,468.00	38.0 Billion Credits	456.0 Billion Credits
Max	$100.00 / ¥659.00	$1,056.00 / ¥6,948.00	$100.00 / ¥659.00	$1,056.00 / ¥6,948.00	82.0 Billion Credits	984.0 Billion Credits

Official sources and rules: Documented on 
Xiaomi MiMo Token Plan Pricing
 and 
Xiaomi MiMo Subscription Guide
 (updated October 21, 2026). First purchases on Individual plans receive a 12% discount. Off-peak night usage (00:00–08:00 Beijing Time / UTC 16:00–24:00) applies a 0.8x consumption coefficient.
mimo.mi
+1

Xiaomi Pay-As-You-Go API Rates

Xiaomi's standard pay-as-you-go rates for the MiMo-V2.6 series (effective September 22, 2026) remain unchanged from the V2.5 series. Both models share a 1,050,000 token context window, with cache writes temporarily free.
mimo.xiaomi
+1

Model Variant	Cache-Hit Input (per 1M tokens)	Cache-Miss Input (per 1M tokens)	Output Tokens (per 1M tokens)	Context Window
mimo-v2.6-flash	$0.0028 / ¥0.02	$0.1400 / ¥1.00	$0.2800 / ¥2.00	1,050,000 tokens
mimo-v2.6-pro	$0.0036 / ¥0.025	$0.4350 / ¥3.00	$0.8700 / ¥6.00	1,050,000 tokens
mimo-v2.6-pro-ultraspeed	$0.0360 / ¥0.25	$4.3500 / ¥30.00	$8.7000 / ¥60.00	1,050,000 tokens

Official sources: Published on 
Xiaomi MiMo V2.6 Launch
 and 
Artificial Analysis MiMo-V2.6 Report
. Note that mimo-v2.6-pro-ultraspeed is not eligible for Token Plan deductions and is billed separately via standard API balances.
mimo.xiaomi
+2

Provider Claims and Mathematical Multiples

The figures below represent official provider specifications and consumption rates rather than empirical user measurements.
mimo.mi

Model	Cache-Hit Input Burn	Uncached Input Burn	Output Token Burn
mimo-v2.6-pro	2.5 Credits / token	300 Credits / token	600 Credits / token
mimo-v2.6-flash	2.0 Credits / token	100 Credits / token	200 Credits / token

Xiaomi claims the following task capacities based on mimo-v2.6-flash executing medium-to-complex programming workflows:
mimo.mi

Lite: ~200 task rounds per month.
mimo.mi

Standard: ~1,600 task rounds per month.
mimo.mi

Pro: ~5,600 task rounds per month.
mimo.mi

Max: ~12,800 task rounds per month.
mimo.mi

Because 300M Credits of mimo-v2.6-pro uncached input costs exactly ¥3.00 at API rates, 100M Credits translates directly to ¥1.00 of API value. Consequently, full quota exhaustion yields fixed nominal value ceilings:
mimo.mi
+1

Lite (¥39 / $6): 4.1B Credits = ¥41.00 ($5.95) API value $\rightarrow$ 1.051x (Day) / 1.314x (Night 0.8x coefficient).

Standard (¥99 / $16): 11B Credits = ¥110.00 ($15.95) API value $\rightarrow$ 1.111x (Day) / 1.389x (Night 0.8x coefficient).

Pro (¥329 / $50): 38B Credits = ¥380.00 ($55.10) API value $\rightarrow$ 1.155x (Day) / 1.444x (Night 0.8x coefficient).

Max (¥659 / $100): 82B Credits = ¥820.00 ($118.90) API value $\rightarrow$ 1.244x (Day) / 1.555x (Night 0.8x coefficient).

No subscriber has reported an empirical 30-day value multiple exceeding these boundaries, and any claim of multi-fold savings (e.g. 3x+) is mathematically incompatible with Xiaomi's fixed credit burn architecture.
v2ex
+1