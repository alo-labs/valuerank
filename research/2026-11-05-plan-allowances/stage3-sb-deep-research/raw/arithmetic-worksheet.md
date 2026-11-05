# Researcher arithmetic worksheet (stage 3, 2026-11-05)

Prices (per 1M tokens): Opus 5.5 input $4, output $20, cache read $0.20, 5-minute cache write $5, 1-hour cache write $8. GPT-6.1 Sol $2 input, $0.10 cached, $10 output. GPT-6 Astra $10, $1, $50. Gemini 4 Argon introductory $2, $0.10, $10. Kimi K3.1 Pro $2, $0.20, $10. Each integer meter reading is widened by 0.5 percentage points at each end.

## Anthropic

- jbdamask: 2,449M cache reads x $0.20 = $490; 27M x $5 = $135 (table $136); 35M x $5 = $175 (table $176); total table $831. $831 / 0.36 = $2,308 per week. At 35.5% $2,341; at 36.5% $2,277. Range $2,277 to $2,341 per week.
- deepfoundationdesign: 3.19B cache read x $0.20 = $638.00; 24.2M cache write x $5 = $121.00 or x $8 = $193.60; 5.9M output x $20 = $118.00; total $877.0 to $949.6 for 64% (63.5% to 64.5%). Value $1,360 to $1,495 per week.
- x2v Pro, cumulative API dollars minus the start row ($0.23): A1 $2.88 over 11 points = $26.2 per 5-hour window; A2 $5.25 over 19 points = $27.6; B0+B1 $7.09 over 23 points = $30.8; B2 $9.16 over 28 points = $32.7 (range $32.1 to $33.3 with 0.5 point rounding; overall $25.0 to $33.3). Weekly meter 4% to 7%: $9.16 / 3 points = $3.05 per point = $305 per week; with 2 to 4 points $229 to $458 per week. The $8 cache-write price was used; at $5 the B2 row is about $8.5 and the 5-hour value about $30.3.
- douflou: $20.46 over 10 points (16% to 26%) = $204.6 per 5-hour window interactive; $20.38 over 10 points = $203.8; $19.83 over 19 points = $104.4 and $19.88 over 19 points = $104.6 through the SDK paths. About $40 per 3 weekly points = $1,333 per week (2.5 to 3.5 points: $1,143 to $1,600).
- ricardoraposo: $15.6 to $30.87 per weekly point x 100 = $1,560 to $3,087 per week; interactive uncached $20.6 x 100 = $2,060.
- sergiokapone (Opus 5.5 part only): 97k output x $20 = $1.94; 31M cache read x $0.20 = $6.20; 1.2M cache write x $5 to $8 = $6.00 to $9.60; total $14.1 to $17.7.
- smaug42: $32 / 0.16 = $200 per 5-hour window ($194 to $206 at 15.5% to 16.5%); $32 / 0.03 = $1,067 per week ($914 to $1,280 at 2.5% to 3.5%).
- leolim031: window 1 = 34.8M x $0.20 + 0.96M x $5..$8 + 186k x $20 = $15.5 to $18.4, over 38 points = $41 to $48 per 5-hour window; window 2 = $7.4 to $8.4 over 13 points = $57 to $64.

## OpenAI

- Oleg-125: 232,120 x $2 = $0.464; 14,130,560 x $0.10 = $1.413; 55,692 x $10 = $0.557; total $2.434. Over 67 points (66 to 68) $3.58 to $3.69 per 5-hour window. The earlier $7.4 upper bound assumed 67% remained; the comment says 67% was consumed.
- jitendersingh0411: Oct 25: cached 13.08M x $0.10 = $1.308, uncached 132K x $2 = $0.264, output 68.9K x $10 = $0.689, total $2.261 per 30 points = $7.5 per 5-hour window. Oct 31: 5.16M x $0.10 = $0.516, 31K x $2 = $0.062, 29K x $10 = $0.29, total $0.868 per 30 points = $2.9. Spread 2.6 times.
- aiplans 2026-10-28 Astra: 2,320,149 x $10 = $23.20; 271,104 x $1 = $0.27; 4,070 x $50 = $0.20; total $23.68 over 3 points (2 to 4) = $789 per week ($592 to $1,184).
- aiplans 2026-10-30 Astra: 4,765,206 x $10 = $47.65; 806,400 x $1 = $0.81; 8,733 x $50 = $0.44; total $48.90 over 4 points (3 to 5) = $1,222 per week ($978 to $1,630).
- aiplans 2026-10-30 Sol: 4,725,504 x $2 = $9.45; 750,208 x $0.10 = $0.075; 8,803 x $10 = $0.088; total $9.61 over at most 2 points = at least $481 per week.

## Google

- Yiji_Kong: $0.0722 / 0.0014434 = $50.0; 42-step session 220,998 x $2 + 3,948,273 x $0.10 + 71,432 x $10 = $1.551, over 0.0315481 = $49.2 per 5-hour window.
- jamie950315 weekly probes at $2, $0.10, $10 including output tokens: (15,683 x $2 + 5 x $10) = $0.031416 / 0.00015703 = $200.06; (16,088 x $2 + 25,193 x $10) = $0.284106 / 0.00142053 = $200.00; (41,355 x $2 + 14 x $10) = $0.08285 / 0.0004142 = $200.03; (2,136 x $2 + 39,306 x $0.10 + 14 x $10) = $0.0083426 / 0.00004174 = $199.87. Range $199.9 to $200.1 per week. At his stated $6, $30, $0.30 the values triple.
- Alpler: $0.864 / 0.102 = $8.47 per week.
- Faheem_Anis1 and Ultimitehand: 185,443 x $2 + 1,684,364 x $0.10 + 19,961 x $10 = $0.739; 94% remaining means 5.5% to 6.5% used, so $11.4 to $13.4 per week. Ratio of $12 to $8.47 = 1.42.
- Ad_Content420: 450M tokens at 96% cache = 432M x $0.10 + 18M x $2 = $79.2 over 29% used = $273 per 5-hour window.

## Kimi

- Astralyn coefficients: input 0.2810, cache read 0.001407, output 2.247 per million tokens per 5-hour window. A 2.5%, 0.5%, 97% mix costs 0.025 x $2 + 0.97 x $0.20 + 0.005 x $10 = $0.294 per million at K3.1 Pro list; 51.0M tokens = $15.0 per 5-hour window; 254.8M per 7d = $74.9.
- SunnyDoll 2026-10-26: 30.43M cache x $0.20 = $6.09 plus 1.47M uncached at $2 to $10 = $2.94 to $14.68, total $9.0 to $20.8.
- PaperPlane: 100M at 98.5% cache = $19.70 + $3.0 to $15.0 = $22.7 to $34.7.
- SunnyDoll 2026-10-29: 148.8M x $0.20 = $29.76 + 1.2M at $2 to $10 = $2.4 to $12.0, total $32.2 to $41.8.

## Results as stated in the report

- Dividing $831 by 0.36 gives about $2,308 per week, or $2,277 to $2,341 with integer rounding.
- Pricing those tokens gives $877.0 to $949.6, so the weekly value is about $1,360 to $1,495.
- Pricing each row gives $26.2 to $32.7 per 5-hour window and about $305 per week with a range of $229 to $458.
- Pricing gives about $7.5 and $2.9 per 5-hour window, a 2.6 times spread, for jitendersingh0411.
- Pricing gives $23.68, so $789 per week with a range of $592 to $1,184 for the 2026-10-28 aiplans Astra batch.
- That is $48.90, so $1,222 per week with a range of $978 to $1,630 for the 2026-10-30 aiplans Astra batch.
- Priced at $2, $0.10 and $10, the two Yiji_Kong readings give $50.0 and $49.2 per 5-hour window.
- The jamie950315 probes price to $199.9 to $200.1 per week at the introductory price.
- The ratio of $12 to $8.47 is 1.42 and matches the 1.5 times step reported for Google AI Pro.
- At a 2.5%, 0.5% and 97% mix the Kimi 5-hour window holds 51.0M tokens, which is about $15 at K3.1 Pro list prices, and 7d is 5 times 5h.
- The x2v dollars use the $8 one-hour cache-write price, and the $5 five-minute price would lower the 5-hour figure by about 7%.
- Dollar arithmetic is done at the list prices above, with each meter reading widened by 0.5 percentage points at each end.
