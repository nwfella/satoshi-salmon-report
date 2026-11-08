FINAL TRANSACTION PROPOSAL: **SELL**

# BTC-USD — Technical Deep-Dive (as of 2026-11-07)

## 1. Bottom line

Bitcoin is trading at **75,747.58** (verified close 2026-11-07), which puts it **~39.3% below the 2025-10-06 closing peak of 124,752.53** and **12.5% below the 2026-09-21 close of 86,602.91**. The primary trend remains down (unbroken sequence of lower highs), the medium-term picture is a *compression* between a still-rising 200-day SMA and a just-rolled-over 50-day SMA, and the short-term picture deteriorated sharply after a **failed breakout on 2026-11-04** was fully reversed on 2026-11-05.

Momentum is bearish but **not yet oversold** (RSI 38.11), and MACD is *re-accelerating* to the downside rather than bottoming. The only genuinely constructive evidence is micro-scale: price has spent two sessions undercutting the lower Bollinger Band intraday and closing back inside it, with a mild 6-session positive RSI divergence. That favours selling strength / holding a bearish bias rather than aggressively shorting into the band.

---

## 2. Verified indicator dashboard (2026-11-07)

| Indicator | Value | Price vs. level | Read |
|---|---:|---:|---|
| Close | 75,747.58 | — | Lowest close since 2026-08-19 (69,266.19) outside the Nov 5–6 dip |
| close_10_ema | 77,486.71 | −2.25% | Short-term trend down; 10 EMA falling 9 of last 10 sessions |
| close_50_sma | 81,871.81 | −7.49% | Bearish; 50 SMA just ticked down from 81,992.18 (Nov 4) |
| close_200_sma | 73,187.78 | +3.50% | Bullish cushion; 200 SMA still *rising* |
| boll (20 SMA) | 79,330.38 | −4.52% | Bearish; mid-band sliding ~300/day |
| boll_ub | 84,321.08 | −10.17% | Upper band collapsing from 87,359.96 (2026-10-08) |
| boll_lb | 74,339.67 | +1.89% | Price in bottom ~14% of channel |
| rsi | 38.11 | — | Weak, but 30 not reached; mild positive divergence |
| macd | −1,486.63 | — | Below zero, most negative value in the sample |
| macds | −1,159.96 | — | MACD below signal since 2026-10-23 |
| macdh | −326.68 | — | Re-widening bearishly after Nov 4's −160.48 |
| atr | 2,251.42 | 2.97% of spot | ~1.6% below the 2026-09-23 reading of 2,510.48 |
| vwma | 78,282.65 | −3.24% | Volume-weighted cost basis sits *above* spot |
| Volume | 9.36B | — | Lowest of the last 30 sessions |

No conflicts were found between the OHLCV feed and the verification snapshot; both agree on the 2026-11-07 row (O 75,746.93 / H 76,138.68 / L 75,485.69 / C 75,747.58).

---

## 3. Why these eight indicators

`close_10_ema` + `close_50_sma` + `close_200_sma` give three separated time horizons so I can distinguish "short-term noise" from "primary trend" from "structural floor" — critical here because they disagree. `macd`/`macds`/`macdh` are used as one momentum family (crossovers + rate-of-change of the gap). `rsi` adds a bounded oscillator that the MACD cannot provide. `boll`/`boll_ub`/`boll_lb` quantify the *compression* the moving averages hint at and locate price within the distribution. `atr` converts every level into a risk unit. `vwma` is the only close-weighted-by-volume measure, testing whether the decline is being *accepted* at these prices. I deliberately excluded a second oscillator (no stochrsi) to avoid duplicated signals.

---

## 4. Long-term structure: primary downtrend, but a higher-low shelf exists

The sequence of closing highs is unambiguously descending:

| Peak | Date | Close |
|---|---|---:|
| Cycle high | 2025-10-06 | 124,752.53 |
| 2026 high | 2026-01-14 | 96,929.33 |
| September high | 2026-09-21 | 86,602.91 |
| October high | 2026-10-21 | 84,011.97 |

The 2025-10-10 session (open 121,704.74, low 104,582.41, close 113,214.37 on **153.1B** volume, the largest in the dataset) marks the regime change from trend-up to trend-down.

On the downside, the sequence is *not* cleanly bearish: capitulation low 62,353.54 (2026-02-05 intraday), then a *lower* low at 57,747.77 (2026-07-01 intraday), then a *higher* low at 64,111.07 (2026-08-19). Since July, BTC has been coiling in a contracting pattern — higher lows against lower highs — and the current price of 75,747.58 sits in the lower third of that coil, **~3.7% above the 2026-08-21 low of 73,011.41**, which is the hinge of the structure.

That matters: the August leg up (2026-08-19 close 69,266.19 → 2026-08-21 close 78,335.19, a two-day +13.1% move) is now almost entirely retraced. Price at 75,747.58 is *inside* the body of that 2026-08-21 breakout candle (open 73,031.09 / close 78,335.19). A break of that candle's base removes the last higher-low in the sequence.

---

## 5. Medium term: the 50/200 SMA configuration is still bullish — and that is the key tension

This is the most misunderstood part of the current tape:

- **50 SMA = 81,871.81**, **200 SMA = 73,187.78**. The 50 remains **8,684 points (11.9%) ABOVE** the 200. The golden-cross regime inherited from 2025 is **still intact**. A "death cross" narrative is premature and not supported by the data.
- However, the **50 SMA has just turned down**: 81,992.18 (2026-11-04) → 81,974.88 (2026-11-06) → 81,871.81 (2026-11-07). It had risen almost monotonically from 74,531.87 (2026-09-23) as the Feb–Jun 2026 crash prints rolled out of the window.
- Simultaneously the **200 SMA is rising** (+87 points over the nine sessions from 2026-10-29's 73,101.84 to 73,187.78), moving *up* toward price from below.

So BTC is trapped in a **narrowing corridor**: it is being squeezed between a falling 50-day above and a rising 200-day below. The gap has compressed from 18,023 on 2026-09-23 (74,531.87 vs 70,758.85) to 8,684 today — a ~52% compression in six weeks. Compression of this kind is a regime that resolves directionally; it is *not* a trend signal by itself. What tips the odds is that price is sitting near the **bottom** of the corridor while short-term momentum points down — i.e., the pressure is on the 200-day, not the 50-day.

**Practical implication:** 73,188 is the single most important number on the chart. It is the 200 SMA *and* it sits next to the 2026-08-20/21 watershed (73,032.76 close, 73,011.41 low). A weekly close below it would invalidate the entire post-July higher-low structure.

---

## 6. Short term: a textbook failed breakout, and momentum is re-accelerating lower

The last five sessions contain the most actionable information in the dataset:

| Date | Close | Change | Volume |
|---|---:|---:|---:|
| 2026-11-03 | 77,345.05 | — | 22.4B |
| 2026-11-04 | 80,405.29 | **+3.96%** | 40.9B |
| 2026-11-05 | 75,942.12 | **−5.55%** | **48.4B** |
| 2026-11-06 | 75,746.93 | −0.26% | 29.3B |
| 2026-11-07 | 75,747.58 | +0.00% | 9.4B |

On **2026-11-04** price broke out of the 76,677–78,248 range with a 81,079.79 high on 40.9B and closed near the high at 80,405.29. On **2026-11-05** it opened there and closed at 75,942.12 near the low (75,114.29) on **48.4B** — roughly **1.9× the ~25–26B average volume of the prior 25 sessions**. That is a bearish engulfing / failed-breakout reversal, and the heavy volume indicates *acceptance* of lower prices rather than a liquidity vacuum.

Since then the bounce attempts have died at successively lower levels: the 2026-11-06 high was 76,291.06 and the 2026-11-07 high 76,138.68, both below the 2026-10-30 to 2026-11-01 shelf of **77,198–78,248**. Note also the **2026-11-07 range is only 652.99 points** and volume at 9.36B is the lowest in 30 sessions — a thin, non-informative session. Do not read the flat close as stabilization.

**MACD is the clearest bearish tell.** The MACD line peaked at +2,486.05 on 2026-09-24, crossed below zero on 2026-10-23 (−69.35), and has made a *new low* on the most recent session at **−1,486.63**. After the 2026-11-04 bounce narrowed the histogram to −160.48, it has re-widened to −264.40 → −319.03 → **−326.68**. Re-widening histogram after a failed bounce = downside momentum re-accelerating. There is **no bullish MACD crossover and no histogram divergence** anywhere in the last 45 sessions.

---

## 7. Mean-reversion evidence is thin and unconfirmed

The bull case rests on three fragile observations:

1. **Price in the bottom 14% of the Bollinger channel** (+1.89% above the 74,339.67 lower band).
2. **Two consecutive intraday band undercuts that closed back inside:** 2026-11-05 low 75,114.29 vs lower band 75,407.24; 2026-11-06 low 74,795.11 vs lower band 74,815.71 (an undercut of ~21 points). In strong downtrends this pattern usually precedes continuation, not reversal — it is a *warning against chasing shorts*, not a buy signal.
3. **A mild positive RSI divergence** over six sessions: 2026-10-29 close 77,775.11 → RSI 35.85; 2026-11-02 close 76,677.30 → RSI 35.00; 2026-11-07 close 75,747.58 → RSI 38.11. Lower prices, marginally higher RSI.

Against that: RSI at **38.11** is nowhere near the 30 threshold, and the 2026-11-04 spike to 50.65 was rejected immediately (38.54 the next day). There is no divergence on MACD, no volume climax, and no reclaimed moving average. **The oversold case is not confirmed.**

---

## 8. Volume structure: distribution, not accumulation

VWMA at **78,282.65** means the volume-weighted average transacted price of the last 20 sessions is **3.24% above spot**. Recent buyers are, on a volume-weighted basis, underwater — that is overhead supply, and it explains why 76,291 / 76,564 / 77,200 have capped every bounce. The VWMA has fallen in an almost unbroken line from 84,141.99 (2026-10-09) to 78,282.65, while price has fallen faster. Price persistently below a falling VWMA is a *distribution* signature, not an accumulation one.

---

## 9. Actionable plan

**Bias: bearish / sell strength.** The trend, momentum, and volume evidence all align; only the lower band and the 200 SMA argue for caution.

**Level map (all from verified data):**

| Role | Zone | Source |
|---|---|---|
| Resistance 3 | 81,080 – 81,872 | 2026-11-04 high 81,079.79; 50 SMA 81,871.81 |
| Resistance 2 | 79,330 – 80,405 | 20-day SMA 79,330.38; 2026-11-04 close 80,405.29 |
| Resistance 1 | 76,291 – 78,283 | 2026-11-06 high 76,291.06; Oct 30–Nov 1 shelf 77,198–78,248; VWMA 78,282.65 |
| Spot | **75,747.58** | 2026-11-07 close |
| Support 1 | 74,340 – 75,114 | Lower Bollinger 74,339.67; Nov 5/6 lows 75,114.29 / 74,795.11 |
| Support 2 | **73,031 – 73,188** | 200 SMA 73,187.78; 2026-08-21 low/open 73,011.41 / 73,031.09 |
| Support 3 | 70,556 – 69,282 | 2026-02-06 close 70,555.39; 2026-02-07 close 69,281.97 |

**Execution options**

1. **Preferred — sell the rally.** Scale into shorts at 77,200 / 78,280 / 79,330, i.e., into the 10 EMA (77,486.71), the VWMA (78,282.65) and the 20 SMA (79,330.38). This avoids entering at the lower band. Stop on a daily close above **80,410** (reclaim of the 2026-11-04 close) — about 1.0–1.4 ATR from the first tranche.
2. **Alternative — momentum continuation.** Short on a decisive daily close below **74,795** (2026-11-06 low) that also clears the lower band. First target 73,031–73,188. Stop at 76,300 (0.7 ATR above entry) or above 77,200 for a swing version.
3. **Do not buy here.** A long at 75,747 has ~1,400 points of room to the lower band and ~5,900 points of overhead supply to the 50 SMA. Reward/risk is inferior to simply waiting.

**Invalidation of the bearish bias (three conditions, need at least two):**
- Daily close above **78,283** (VWMA) and above the 10 EMA;
- MACD histogram positive for two consecutive sessions (currently −326.68);
- RSI back above **45–50** with price holding above 76,291.

**Risk management**
- ATR 2,251.42 = **2.97% of spot**. 1.5 ATR = ~3,377 (4.5%).
- Position size = (equity × risk %) ÷ (1.5 × ATR). At 1% equity risk that implies a notional of roughly **22% of equity** per unit of risk — i.e., scale, don't lump.
- Expect volatility compression to precede the corridor resolution: ATR has already fallen from 2,510.48 (2026-09-23) to 2,251.42. A quiet weekend tape (9.36B volume) often precedes an expansion session — do not leave stops tight into that.

**What would flip the medium-term picture:** A weekly close above the 2026-10-21 high of 84,840.05 (the most recent lower high) would break the descending-highs sequence and put the 50 SMA back in play as support. Until then, every rally is a counter-trend rally inside a primary downtrend.

---

## 10. Key points summary

| Dimension | Evidence | Signal |
|---|---|---|
| Primary trend | Lower highs 124,752.53 (2025-10-06) → 96,929.33 → 86,602.91 → 84,011.97 | **Bearish** |
| Drawdown | 75,747.58 = −39.3% vs 2025-10-06 close; −40.2% vs 126,198.07 intraday ATH | Bearish |
| 2026 performance | −14.6% vs 2026-01-01 close 88,731.98 | Bearish |
| Short-term trend | Price below 10 EMA (77,486.71) and 20 SMA (79,330.38) | **Bearish** |
| Medium-term trend | Price −7.49% vs 50 SMA (81,871.81), which just rolled over | **Bearish** |
| Long-term trend | Price +3.50% above rising 200 SMA (73,187.78) | Bullish (cushion) |
| Golden/death cross | 50 SMA 81,871.81 still 11.9% above 200 SMA, but gap halved in 6 weeks | Neutral / deteriorating |
| MACD | −1,486.63 vs signal −1,159.96; histogram re-widening to −326.68 | **Bearish** |
| RSI | 38.11; 2026-11-04 spike to 50.65 rejected; mild 6-day divergence | Bearish, unconfirmed divergence |
| Bollinger | Price in bottom 14% of a 9,981-wide channel; 2 intraday band undercuts closed back inside | Bearish with short-term squeeze risk |
| Volume | 2026-11-05 −5.55% on 48.4B (~1.9× avg) after failed +3.96% breakout | **Distribution** |
| VWMA | 78,282.65, i.e., 3.24% above spot = overhead supply | Bearish |
| Volatility | ATR 2,251.42 (2.97%); 1.5 ATR stop = 4.5% | Size down |
| Decision | Trend + momentum + volume aligned lower; no confirmed oversold reversal | **SELL** (sell rallies 77.2–79.3k; add below 74.8k) |
| Hard invalidation | Daily close > 80,410 and MACD histogram > 0 | Cover / stand aside |
| Structural break | Weekly close < 73,031 would target 70,556 → 69,282 | Accelerated downside |

*This is a technical assessment derived solely from the supplied OHLCV and indicator data; it is not investment advice and does not account for fundamentals, positioning, or macro catalysts.*