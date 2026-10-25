# BTC-USD — Multi-Timeframe Technical Report
**Analysis date:** 2026-10-24 (Saturday session) | **Verified close:** $80,790.84 | **Exchange:** CCC (spot)

All price/indicator figures below are taken from the verified market snapshot for 2026-10-24, which is the source of truth. Where I derive a percentage or distance, the arithmetic is shown so it can be checked.

---

## 1. Where price sits right now

| Field | Value |
|---|---:|
| Open | 81,074.19 |
| High | 81,098.24 |
| Low | **79,145.54** |
| Close | **80,790.84** |
| Volume | 21.27B |

Today's candle is a bearish continuation bar: opened near the high, sold to 79,145.54, and closed 83% down the range. Two facts matter more than the candle itself:

1. **The 2026-10-24 low of 79,145.54 is the lowest intraday print since 2026-09-18** (low 76,228.33). Every session from 2026-09-19 through 2026-10-23 printed a low above it.
2. **80,790.84 is the lowest close of the last 30 sessions** (the prior 30-session closing low was 81,074.19 on 2026-10-23, and before that 81,311.89 on 2026-10-22).

So price is at the bottom edge of a five-week distribution range, with the sequence of recent closes being literally monotonic down: 84,011.97 (10-21) → 81,311.89 (10-22) → 81,074.19 (10-23) → 80,790.84 (10-24), i.e. **−3.83% in three sessions**.

---

## 2. 12-month context: a repaired bear market, not a resurgent bull market

From the retrieved OHLCV (2025-10-24 → 2026-10-24):

- **Cycle high in window:** 116,273.31 intraday on 2025-10-27.
- **Cycle low:** 60,074.20 intraday on 2026-02-05, then a *lower low* of **57,747.77 on 2026-07-01**.
- **Recovery high:** 87,363.76 intraday on 2026-09-21.

Against those anchors:
- Current 80,790.84 is **−30.5% below the 2025-10-27 high** and **−27.2% below the 2025-10-24 close of 111,033.92** (a negative 12-month return).
- It is **+34.5% above the 2026-02-05 low** (60,074.20) and **+39.9% above the 2026-07-01 low** (57,747.77).
- It is **−7.53% below the 2026-09-21 high** and **−16.6% below the 2026-01-14 close** (96,929.33).

The structural read: the July low at 57,747.77 was a *lower* low versus February, yet it was followed by a +51.3% impulse to 87,363.76 — a higher high versus the May 2026 peak of 82,792.21 (2026-05-06). That is a legitimate intermediate-term bullish reversal. The current move is a **pullback within that recovery**, not (yet) a resumption of the 2025–2026 bear leg. But it is a deep pullback that has now given back roughly half of the July→September advance (retracement of 57,747.77→87,363.76 at 50% = 72,555.77; price at 80,790.84 has retraced ~22%).

---

## 3. Indicator selection and why

I selected **8 complementary indicators** — three trend layers, one momentum pair, one volatility envelope, one volatility-scalar, and one volume-integrated average. I deliberately avoided stacking oscillators (no StochRSI alongside RSI) and avoided selecting MACD's three components as three separate "indicators."

| # | Indicator | Value 2026-10-24 | Why it earns a slot here |
|---|---|---:|---|
| 1 | **close_200_sma** | 72,900.84 | The only clean long-term trend arbiter. Price is +10.82% above it and the line is *rising* off its 2026-08-21 low of 68,973.59 — tells us whether this is a dip or a regime change. |
| 2 | **close_50_sma** | 81,800.72 | Medium-term trend + the level price just lost (first close below it on 2026-10-22). Also quantifies how stretched the 50/200 spread has become (+12.2%). |
| 3 | **close_10_ema** | 81,912.01 | Captures the speed of the short-term deterioration. Falling 3 straight sessions (82,645.11 → 82,402.71 → 82,161.16 → 81,912.01) and now above the 50 SMA — a short-term death cross is forming. |
| 4 | **macd** (+ signal 107.67, hist −287.85) | −180.18 | The cleanest measure of *trend regime*. MACD crossed below zero on 2026-10-23 for the first time in the 60-session window and sits below its signal line. |
| 5 | **rsi** | 44.21 | Momentum exhaustion gauge. Needed to test whether the selloff is becoming oversold (it is not) and to check for divergence. |
| 6 | **boll_lb** (envelope: mid 82,544.00 / ub 85,320.06 / lb 79,767.95) | 79,767.95 | Defines a statistically-derived downside objective and tells us where price sits inside the envelope (%B ≈ 0.18). The band *width* collapse is the single most important volatility observation right now. |
| 7 | **atr** | 2,112.38 (2.61% of spot) | Position sizing and stop placement. Critically, ATR is *not* expanding — it is near the low end of its 2-month range (2,043–2,511). |
| 8 | **vwma** | 82,114.28 | Volume-weighted cost basis. Price is 1.61% *below* it, meaning recent turnover occurred at higher prices — sellers are holding the marginal advantage. Confirms the breakdown isn't purely a price artifact. |

---

## 4. Trend analysis: three layers disagreeing

### Long-term (200 SMA) — intact bullish, but low conviction
- Price 80,790.84 vs 200 SMA 72,900.84 → **+7,890.00, or +10.82%**.
- The 200 SMA bottomed at **68,973.59 on 2026-08-21** and has risen every session since, to 72,900.84 — **+5.69%**. Its slope reaccelerated recently: 72,425.69 (10-17) → 72,900.84 (10-24) is +475.15 in five sessions, versus only +771.11 over the prior 90 days (72,129.73 on 2026-07-26 → 72,900.84). In other words, the *rate of change* of the long-term line is improving even as price falls. That is a genuinely constructive signal.
- Price reclaimed the 200 SMA on **2026-08-19** (close 69,266.19 vs 200 SMA 68,995.07) and has not closed below it since.

### Medium-term (50 SMA) — still rising, but the price/50SMA relationship just broke
- The 50 SMA has risen from **63,510.94 (2026-08-15) to 81,800.72 — +28.8%** — and is still climbing about $22/day.
- **However: 2026-10-22 was the first daily close below the 50 SMA within the entire 90-session retrieval window.** Close 81,311.89 vs 50 SMA 81,782.29. Price has stayed below for three sessions.
- The 50/200 spread is **+12.2%** (50 SMA ÷ 200 SMA = 1.1221). That is a wide, mature cross spread — mechanically it means the medium-term average has a lot of air beneath it, and the 50 SMA's own slope will flatten quickly if price simply goes sideways here (it is lapping the August–September rally).

### Short-term (10 EMA) — clearly bearish
- The 10 EMA has rolled from **84,841.47 (2026-10-06) to 81,912.01** and is now *above* the 50 SMA (81,912.01 vs 81,800.72). With price 1.37% below both, the 10 EMA is on course to cross down through the 50 SMA within days — the classic short-term trend-change trigger.
- The 10 EMA also crossed below the 20-period Bollinger mid (82,544.00), and price is 2.12% below that mid-line.

**Synthesis:** the hierarchy is bullish long-term (price > rising 200 SMA), neutral-to-rolling-over medium-term (50 SMA rising but just lost), and bearish short-term (price < 10 EMA < losing momentum). This is the signature of a **failed breakout inside an uptrend** — the most ambiguous of all configurations, and one that argues for patience rather than aggression.

### The golden cross
The 50 SMA crossed **above** the 200 SMA on **2026-09-08** (50 SMA 69,958.49 vs 200 SMA 69,866.57; on 2026-09-07 the 50 SMA at 69,694.32 was still below the 200 SMA at 69,814.41). That cross is still valid — there is no death cross anywhere near, since the spread is +8,899.88.

---

## 5. Momentum: a decisive regime shift on 2026-10-22/23

### MACD
- MACD line: **−180.18** vs signal **107.67** → line is below signal, histogram **−287.85**.
- The MACD line peaked at **2,070.54 on 2026-09-30** and has fallen essentially monotonically since: 1,994 (10-05) → 1,689 (10-07) → 1,134 (10-09) → 440 (10-14) → 44.28 (10-22) → **−69.35 (10-23)** → −180.18 (10-24).
- **The zero-line break occurred on 2026-10-23** — the first negative MACD reading in the 60-session series.
- The histogram has been negative since **2026-09-29** (+74.04 on 09-28 → −34.10 on 09-29), i.e. the MACD/signal bearish cross is now **three and a half weeks old**. It bottomed at −584.91 (10-12), narrowed to −126.82 (10-21), then **re-widened to −287.85 (10-24)**. That re-widening after a brief narrowing is important: the bounce attempt on 2026-10-21 failed to repair momentum. Downside acceleration, not deceleration, is the current reading.

### RSI
- **44.21**, down from 56.68 on 2026-10-21 and 68.51 on 2026-10-04. Below the 50 mid-line since 2026-10-22.
- RSI is **not oversold**. There is no 30-line capitulation signal and no bullish divergence: on 2026-10-08 price closed 81,676.34 with RSI 46.86; today price is 1.08% *lower* (80,790.84) with RSI 2.65 points lower. Momentum is *confirming* the new price low, which means there is no technical brake on further downside yet.
- One useful historical note (observed, not predictive): a **mild bearish RSI divergence** formed at the top — 2026-09-21 close 86,602.91 with RSI 73.85, versus 2026-10-04 close 86,480.30 with RSI 68.51 (lower RSI on marginally lower price). The subsequent 6.6% decline from 86,480.30 to 80,790.84 is consistent with that signal, but a single instance proves nothing about the next one.

**Momentum verdict: bearish and still deteriorating.** The one thing missing from a true momentum washout is an oversold RSI reading. Until RSI is in the mid-30s (or a bullish divergence appears), rallies have to be treated as counter-trend.

---

## 6. Volatility: the most under-appreciated part of this setup

### Bollinger envelope
| Band | Value | Distance from close |
|---|---:|---:|
| Upper | 85,320.06 | +5.61% above |
| Middle (20 SMA) | 82,544.00 | +2.12% above |
| Lower | **79,767.95** | **−1.28% below** |

- **%B = (80,790.84 − 79,767.95) / (85,320.06 − 79,767.95) = 1,022.89 / 5,552.11 ≈ 0.18.** Price is in the bottom 18% of the envelope — leaning on the lower band, but *at* the band rather than through it.
- **Band width has collapsed:** 5,552.11 now = **6.73% of the mid-line**, versus (89,498.12 − 76,217.30) = 13,280.82 = **16.03% of the mid-line on 2026-10-04**. That is a **~58% contraction in under three weeks**.
- Important nuance: much of that contraction is mechanical — the enormous 2026-09-21/22 impulse candles (80,867→87,363 intraday, close 86,602.91) have rolled out of the 20-day standard-deviation window. So this is a *statistical* squeeze rather than proof of a coiled spring.
- **ATR, the honest test of realized volatility, disagrees with the "squeeze" narrative:** ATR is **2,112.38 (2.61% of spot)**, versus 2,169.74 on 2026-10-04 and 2,510.48 on 2026-09-23. Realized daily range has compressed only ~3% in three weeks and remains in the middle of its 2-month band (2,043–2,511). Translation: **the market has stopped trending, not stopped moving.**

### What this means for risk
With ATR at 2,112, a normal daily range is ±$2.1k, and a 2×ATR stop is **$4,224.77 = 5.23% of spot**. Any position taken at market has a genuine ~5% noise band. This argues for *smaller* size, not tighter stops.

---

## 7. Volume and participation: distribution, but no capitulation

- **VWMA (82,114.28)** sits 1,323.44 (1.61%) *above* the close. The volume-weighted average transacted price over the indicator window is above spot — buyers from the last several weeks are underwater, which creates overhead supply on any bounce.
- **The decisive day was 2026-10-22:** −3.21% (84,011.97 → 81,311.89) on **33.45B** volume. Using the 30-session volume series from the retrieved data, the mean is approximately **27.4B**, so that was a roughly **+22% distribution day** — above-average volume on a sharp decline is a bearish tell.
- **But the follow-through is thin:** 23.49B on 2026-10-23 and **21.27B today, ~22% below the 30-day mean.** The break to a new 5-week low is happening on *declining* volume. That is drift/absence-of-bids rather than forced liquidation, and it makes the downside look more like a slow bleed than a capitulation.
- For scale: the 2026-02-05 low (60,074.20) printed **125.5B**, and 2025-11-21 printed **129.2B**. Today's volume is a sixth of those. **No climactic seller exhaustion has occurred.**

---

## 8. Reference levels (drawn only from tool output, not assumed behaviour)

**Overhead — now a supply cluster between 81.8k and 82.5k:**
- 81,800.72 — 50 SMA (lost 2026-10-22)
- 81,912.01 — 10 EMA
- 82,114.28 — VWMA
- 82,544.00 — Bollinger mid
This tight four-level band is the nearest meaningful hurdle. A daily close above 82,544 would be the first objective evidence that the breakdown failed.

**Further resistance:**
- 84,011.97 (2026-10-21 close) / 84,840.05 (2026-10-21 high)
- 86,480.30–86,766.15 (2026-10-04 close/high)
- 87,363.76 — 2026-09-21 high (the structural ceiling)

**Downside references:**
- **79,767.95** — Bollinger lower band
- **79,145.54** — 2026-10-24 low (the immediate line in the sand)
- 77,830.29 / 76,909.35 — 2026-08-28 close / low
- 76,470.64–74,944.59 — 2026-09-10/11 and 2026-09-15 lows (the September higher-low shelf)
- **72,900.84** — 200 SMA (the bull/bear line)

**Constructive observation:** the 79.1k–80.9k region is precisely where the September impulse originated — 2026-09-18 closed 80,901.46 and 2026-09-19 closed 81,233.68 before the vertical move to 86,602.91 by 2026-09-21. Price is retesting the base of that impulse. That is a reason for caution on fresh shorts, not a reason to buy blindly.

---

## 9. Scenario map with explicit triggers

**Scenario A — Range resolution lower (near-term risk, ~45% implicit weight).**
Trigger: a daily close below **79,145.54**. Confirmation: close below the Bollinger lower band 79,767.95 with volume >27B.
Path: 77.8k → 76.5k–74.9k. Invalidation of the intermediate uptrend would only come at a close below 72,900.84 (200 SMA), which is 9.8% lower.

**Scenario B — Base-building / chop (highest-probability path, ~35%).**
Trigger: price holds 79,145.54 and oscillates in a 79.1k–84.8k box. Evidence for this: ATR flat, band width compressed, RSI mid-range at 44, and today's low-volume drift.
Tactically this is a "do nothing at market" regime; the 81.8k–82.5k cluster is the pivot.

**Scenario C — Bear trap / reclaim (~20%).**
Trigger: a daily close back above **82,544.00** (Bollinger mid) that also reclaims the VWMA at 82,114.28, ideally with RSI back above 50 and MACD histogram narrowing for 3+ sessions.
Path: 84.8k → 86.5k → 87.4k retest. Only a close above 87,363.76 re-establishes the primary uptrend and opens the 2026-01-14 high of 97,860.60 as an objective.

---

## 10. Position management

- Because the trend layers conflict, **the correct action is no new exposure at these prices.** Spot longs should be held, not added to, unless Scenario C triggers.
- If a tactical long is taken at the 79.1k–79.8k shelf: **stop below 78,850** (below the 10-24 low minus a small buffer), which is a ~1,900–2,000 point risk ≈ 0.9×ATR — acceptable only with **reduced size** (use 1.5% of ATR, not 2×, given the ATR is not expanding).
- For existing longs from the August–September advance: **the structural stop is a weekly close below 72,900.84 (200 SMA)**. A tighter tactical stop under 79,145.54 is defensible only for leveraged positions.
- For anyone short: 79.1k is the obvious level; given the light volume and the September-base overlap, taking partials into the 79.1k–79.8k band rather than pressing is the higher-expectancy management.
- **Invalidation rule:** the bearish short-term read is void on a close above 82,544.00; the bullish long-term read is void on a close below 72,900.84.

---

## 11. Honest limitations

- The toolset contains no on-chain, funding-rate, open-interest, ETF-flow, or macro-liquidity data. For BTC-USD those are frequently the marginal drivers, and none of the above captures them. This report is technical only.
- Bollinger band-width contraction here is partly an artifact of the September impulse rolling out of the 20-day window; I have weighted ATR more heavily as the honest realized-volatility measure.
- My statement that 2026-10-22 was the "first close below the 50 SMA" is bounded by the 90-session indicator window retrieved (starting 2026-07-26); a prior breach before that window cannot be excluded from this data.

---

## 12. Summary table

| Dimension | Reading (2026-10-24) | Signal | Interpretation |
|---|---|---|---|
| Close | 80,790.84 | — | Lowest close in 30 sessions; 3-day drop −3.83% from 84,011.97 |
| Session range | 79,145.54 – 81,098.24 | Bearish | Closed at 17% of range; new low since 2026-09-18 |
| 200 SMA | 72,900.84 (+10.82% below price) | **Bullish (LT)** | Rising since 2026-08-21 low of 68,973.59; slope improving |
| 50 SMA | 81,800.72 (price −1.23%) | **Bearish flip** | First close below it since at least 2026-07-26 (happened 2026-10-22) |
| 10 EMA | 81,912.01 (price −1.37%) | Bearish | Above 50 SMA; downside cross imminent |
| 50/200 spread | +12.2% | Stretched | Mature golden cross (2026-09-08); mean-reversion risk |
| MACD / signal / hist | −180.18 / 107.67 / −287.85 | **Bearish** | Zero-line break 2026-10-23; hist re-widening after brief narrowing |
| RSI | 44.21 | Weak-neutral | Not oversold; no bullish divergence; confirming the low |
| Bollinger | mid 82,544.00 / ub 85,320.06 / lb 79,767.95 | Lower-half | %B ≈ 0.18; close is 1.28% above lower band |
| Band width | 6.73% of mid (was 16.03% on 2026-10-04) | Compression | ~58% contraction, partly window artifact |
| ATR | 2,112.38 (2.61%) | Stable | Flat vs 2,169.74 (2026-10-04); no expansion, no capitulation |
| VWMA | 82,114.28 (price −1.61%) | Bearish | Overhead supply; blended holders underwater |
| Volume | 21.27B vs ~27.4B 30-day mean | **Divergent** | Break lower on light volume; 10-22 was a 33.45B distribution day |
| Key resistance cluster | 81,800.72 / 81,912.01 / 82,114.28 / 82,544.00 | Pivot zone | Daily close above 82,544 = breakdown failed |
| Key support | 79,767.95 / 79,145.54 / 76,909–77,830 / 74,944.59 / 72,900.84 | Downside ladder | 200 SMA is the regime line |

**Bottom line:** BTC-USD has broken short-term trend (below 10 EMA, 50 SMA, VWMA and Bollinger mid) on a fresh 5-week low, with MACD through zero and RSI falling — but it has done so on *shrinking* volume, with ATR flat, while sitting 10.8% above a *rising* 200 SMA and directly on the base of the September impulse. The evidence does not support either adding longs into weakness or initiating new shorts into a low-volume retest of a prior launch zone. The correct posture is to hold existing exposure, shrink risk, and let the 79,145.54 / 82,544.00 bracket decide the next leg.

FINAL TRANSACTION PROPOSAL: **HOLD**