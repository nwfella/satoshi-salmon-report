# BTC-USD — Technical Analysis, 21 November 2026

## 1. Executive summary

BTC-USD is in a **confirmed primary downtrend** that has just produced its most violent capitulation candle of the trailing 12 months. The verified close is **60,094.09**, which sits **below every major moving average** and below the volume-weighted average price. Momentum is deeply negative and RSI is in single-digit-to-low-20s territory. However, the 21 November session printed a large lower wick (low **55,149.57** → close **60,094.09**, +8.97% off the low) on volume roughly 1.9× the recent average, which is a classic **exhaustion/reversal-attempt signature inside a still-unbroken downtrend**.

The honest read: **trend is down, momentum is washed out, and the risk/reward for fresh directional exposure in either direction is poor right now.** This argues for HOLD rather than chasing the breakdown or knife-catching the low.

---

## 2. Indicator selection and rationale

I selected eight complementary inputs, deliberately avoiding redundancy:

| # | Indicator | Why it is appropriate here |
|---|---|---|
| 1 | **close_10_ema** | Fast trend/momentum gauge; the first hurdle any bounce must reclaim. |
| 2 | **close_50_sma** | Medium-term trend spine and the level that defines the current distribution zone. |
| 3 | **close_200_sma** | Long-term regime filter; also needed to monitor a 50/200 death-cross risk. |
| 4 | **MACD (macd + macds + macdh)** | Quantifies the persistence and acceleration of the bearish momentum impulse. |
| 5 | **RSI** | The only mean-reversion/oversold gauge in the set — critical because price is already extended. |
| 6 | **Bollinger suite (boll / boll_ub / boll_lb)** | Measures statistical stretch and volatility expansion/mean-reversion potential. |
| 7 | **ATR** | Position sizing and stop placement in an unusually wide-range tape. |
| 8 | **VWMA** | Volume-confirmation filter: converts "price is below trend" into "volume actually transacted above the market," i.e. overhead supply. |

Deliberately excluded: StochRSI (redundant with RSI), and any additional volume oscillator (VWMA already captures the volume/price relationship in this regime).

**Data consistency note:** RSI (22.71), close_50_sma (77,135.95), close_200_sma (72,427.41) and MACD (−4,930.85) from `get_indicators` match the verified snapshot exactly — no discrepancy. VWMA is **not** part of the verified snapshot; the 65,786.46 figure is sourced only from the indicator tool and should be treated as a secondary reference.

---

## 3. Trend structure

**All trend measures are bearish and aligned.**

- Close **60,094.09** vs **close_10_ema 64,316.92** → price **6.6% below** the fast average.
- vs **close_50_sma 77,135.95** → **22.1% below**.
- vs **close_200_sma 72,427.41** → **17.0% below**.
- vs **VWMA 65,786.46** → **8.7% below**.

The ordering is emphatically not bullish: `50 SMA (77,136) > 200 SMA (72,427) > VWMA (65,786) > 10 EMA (64,317) > Price (60,094)`. Price is at the very bottom of that stack, meaning every timeframe of buyer is underwater.

The 50 SMA remains marginally **above** the 200 SMA (+6.50%), so the 2025–26 golden-cross structure is technically still intact — but it is a **failed golden cross**: price has fallen far below both averages, and the 200 SMA has begun to roll over (73,148.89 on 1 Nov → 72,427.41 on 21 Nov). The 50 SMA is falling much faster than the 200 SMA, so a **death cross is a live risk** over the coming weeks if price does not recover.

**Swing structure is a textbook sequence of lower highs and lower lows** across the dataset:
- Jan 2026 high **97,860.60** (14 Jan, close 96,929.33)
- Sep 2026 rally high **87,363.76** intraday (21 Sep, close 86,602.91)
- Oct 2026 high **86,971.78** (5 Oct), then a lower high of **84,840.05** (21 Oct)
- Nov 2026: no high above 81,079.79 (5 Nov)
- Nov 21 low **55,149.57** — the **lowest low in the entire 12-month dataset**, beneath the Feb low (60,074.20, 6 Feb) and June low (58,075.92, 25 Jun).

Measured declines: **−28.5%** from the 21 Oct close (84,011.97) to the 21 Nov close, and **−38.0%** from the 14 Jan close (96,929.33).

---

## 4. Momentum

**MACD:** −4,930.85 vs signal −3,941.65, histogram −989.20. The MACD line has fallen monotonically from **+1,689.20 on 7 Oct** and crossed below zero on **23 Oct** (−69.35). It is still making lower lows as of 21 Nov — from −3,953.16 (17 Nov) to −4,930.85 (21 Nov). **There is no bullish crossover and no flattening of the histogram**, so the intermediate momentum impulse is still pointing down.

**RSI:** **22.71**, up from **17.50** on 20 Nov. RSI has now closed below 30 for **nine consecutive sessions** (13–21 Nov, with the sequence 24.99 → 20.19 → 24.64 → 24.09 → 24.24 → 21.84 → 20.58 → 17.50 → 22.71). Two important nuances:

1. **Oversold persistence is a trend characteristic, not a buy signal** — RSI sat above 50 as recently as 21 Oct (56.68) and only broke down decisively after 12 Nov.
2. **A nascent short-term divergence has appeared:** on 21 Nov price printed a *lower* low (55,149.57 vs 57,708.70) while RSI *rose* (22.71 vs 17.50). This is a first hint of selling exhaustion, but one session does not constitute a confirmed divergence.

---

## 5. Volatility and statistical stretch

- **ATR = 2,967.22**, i.e. **4.94% of the close**. That is an extreme daily volatility regime; any stop closer than ~1 ATR will be noise.
- The **21 Nov true range alone was 5,694.19** (high 60,843.76 / low 55,149.57) = **9.48% of the close**, roughly **1.92× ATR**. That is volatility expansion, typically associated with capitulation or trend climax.
- **Bollinger:** middle **70,095.70**, upper **83,379.04**, lower **56,812.36**. Bandwidth is **37.9% of the middle band** — extraordinarily wide, confirming a volatility breakout regime rather than a coil.
- Price closed **5.8% above the lower band** (56,812.36) after trading **below** it intraday (low 55,149.57). A close back inside the band after a band pierce is the standard mechanism of a short-term mean-reversion attempt toward the middle band.
- Distance from close to Bollinger middle: **−14.3%**. Historically that is a stretched condition, but in a downtrend the middle band frequently acts as the retracement ceiling rather than a target that gets reached.

---

## 6. Volume / participation

**VWMA = 65,786.46**, i.e. **8.7% above spot**. The volume-weighted average price falling from **84,489.50 (7 Oct)** to **65,786.46 (21 Nov)** tells us the *bulk of recent transacted value* sits well above the current market — meaning the average participant is holding a loss and rallies into 64–66k will meet supply from trapped longs.

Volume confirms capitulation: **58.41B** on 21 Nov versus **60.70B** on 20 Nov, against a roughly ~31–33B daily average for the prior 20 sessions — approximately **1.8–1.9× average** on back-to-back sessions. Two consecutive high-volume down/reversal days after a month of decline is consistent with forced liquidation, not with quiet accumulation. There is no evidence yet of a volume-confirmed reversal (that would require an up-week on expanding volume and a VWMA that stops falling).

---

## 7. Key levels (all derived from verified tool output)

**Resistance (overhead stack):**
1. **60,843.76** — 21 Nov high (immediate).
2. **62,987 – 63,329** — 18 Nov close / 14 Nov low congestion.
3. **64,316.92** — 10 EMA (first trend reclaim test).
4. **64,855 – 65,305** — the 15–17 Nov plateau that broke down; now supply.
5. **65,786.46** — VWMA (trapped-longer breakeven zone).
6. **70,095.70** — Bollinger middle / ~20-day mean.
7. **72,427.41** — 200 SMA (regime line).
8. **77,135.95** — 50 SMA.

**Support:**
1. **55,149.57** — 21 Nov low, and the **lowest print in the 12-month dataset**.
2. Below that there is **no verified support** in the available history — any break would be into price discovery, and I will not invent a level.

---

## 8. Scenarios and actionable plan

**Base case (most likely, 1–3 weeks): volatile basing attempt between 55,000 and 66,000.** The hammer + volume spike + RSI uptick + band re-entry argue for a tactical bounce. The bounce should be treated as a *counter-trend retracement* until the 10 EMA / VWMA / 15–17 Nov plateau (64,300–65,800) is reclaimed and held on a daily close.

**Bullish confirmation triggers (would upgrade stance):**
- Daily close **above 64,317 (10 EMA)** and then **above 65,786 (VWMA)**, with RSI recovering above 40–45 and MACD histogram turning positive. That combination would mark the first credible trend-repair signal.
- A higher low above **55,149.57** on lower volume (successful retest) would strengthen the case.

**Bearish continuation triggers:**
- A daily close **below 55,149.57** invalidates the reversal candle and opens price discovery. MACD would remain deeply negative and the 50/200 death cross would likely complete.
- Failure at the 64–66k supply shelf (rejection candle with rising volume) is the higher-probability short setup, because it offers a defined invalidation level.

**Risk management specifics:**
- With ATR at **2,967 (4.94%)**, use **1.5–2.0× ATR** stops (≈ **4,450–5,930** points) or reduce position size proportionally. A stop inside 3,000 points of entry is statistically likely to be hit in this tape.
- Any tactical long from the 55–60k zone needs invalidation below **55,149.57** — a wide but objectively defined risk.
- Do **not** add to longs simply because RSI is 22.7; nine consecutive sub-30 closes demonstrate that oversold can persist.

**Why HOLD rather than BUY or SELL:**
- **Not a BUY:** price is below the 10 EMA, 50 SMA, 200 SMA and VWMA; MACD is still accelerating lower; the trend of lower highs/lower lows is intact; and no confirmed reversal signal exists yet.
- **Not a fresh SELL:** shorting at RSI 22.71 after a −28.5% month, on a 1.9× ATR capitulation candle that closed 8.97% off its low, is chasing an extended move with poor asymmetry — bounce risk into the 64–66k supply zone is high.
- **HOLD** existing exposure with reduced size and pre-defined invalidation, and let the 55,149.57 / 64,317 / 65,786 levels dictate the next action.

---

## 9. Key points summary

| Dimension | Evidence (verified 2026-11-21) | Read |
|---|---|---|
| **Verified close** | 60,094.09 (O 58,798.98 / H 60,843.76 / L 55,149.57) | +2.20% d/d; +8.97% off low — hammer/reversal attempt |
| **Primary trend** | Price 22.1% below 50 SMA (77,135.95); 17.0% below 200 SMA (72,427.41) | Strong downtrend |
| **Short-term trend** | Close 6.6% below 10 EMA (64,316.92) | No short-term repair yet |
| **MA structure** | 50 SMA > 200 SMA by +6.50%, but both falling and above price | Failed golden cross; death-cross risk |
| **Momentum** | MACD −4,930.85, signal −3,941.65, hist −989.20; lower lows since 7 Oct | Bearish, still accelerating |
| **Overbought/oversold** | RSI 22.71, up from 17.50; 9 straight closes <30 | Deeply oversold; early divergence, unconfirmed |
| **Volatility** | ATR 2,967.22 (4.94%); 21 Nov range 9.48% = 1.92× ATR | Extreme; size down, widen stops |
| **Bollinger** | Mid 70,095.70 / UB 83,379.04 / LB 56,812.36; bandwidth 37.9% | Volatility breakout; price re-entered band from below |
| **Volume** | VWMA 65,786.46 (8.7% overhead); 58.41B vs ~31–33B avg | Overhead supply; capitulation volume |
| **Swing lows** | 55,149.57 = lowest low in 12-month dataset | Only verified support; no level below |
| **Overhead targets** | 64,317 → 65,786 → 70,096 → 72,427 → 77,136 | Ladder of resistance |
| **Signal quality** | No MACD crossover; no confirmed divergence; no MA reclaim | Reversal is *possible*, not *confirmed* |
| **Proposed stance** | HOLD — no chase long, no chase short | Wait for 55,150 break or 64.3k/65.8k reclaim |

FINAL TRANSACTION PROPOSAL: **HOLD**