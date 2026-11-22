# Fundamental Analysis Report — `BTC-USD` (Bitcoin USD)

**Analysis date:** 2026-11-21 | **Data pull timestamp:** 2026-11-22 10:45 UTC | **Exchange:** CCC
**Resolved identity:** Bitcoin USD — confirmed (market cap ~$1.22T and 52-week range of $55,149–$97,861 are consistent with BTC, not with any equity sharing the symbol).

---

## 1. Headline finding: there are no "company fundamentals" to analyze

I ran the full statement suite against `BTC-USD`. Results:

| Requested statement | `BTC-USD` result |
|---|---|
| `get_income_statement` (quarterly) | **NO_DATA_AVAILABLE** — no income statement data from any configured vendor |
| `get_balance_sheet` (quarterly) | **NO_DATA_AVAILABLE** — no balance sheet data |
| `get_cashflow` (quarterly) | **NO_DATA_AVAILABLE** — no cash flow data |
| `get_fundamentals` | **Partial** — market/price data only (cap, 52-wk range, 50/200-DMA) |

This is the *expected and correct* outcome, not a vendor failure. Bitcoin is a bearer asset on a decentralized network — there is no issuer, no board, no fiscal year, no revenue, no debt, no working capital, no EPS, no guidance, and no management to interview. Any "balance sheet" or "income statement" produced for `BTC-USD` would be fabricated. I will not estimate or invent those values.

**Implication for the desk:** for `BTC-USD`, the fundamental layer is *supply mechanics, cost-basis cohorts, and network adoption* — not corporate financials. Below I separate (a) hard vendor data, (b) arithmetic derived strictly from that data, and (c) known structural facts about Bitcoin's protocol, flagged as such. I explicitly note where crypto-native valuation inputs are **missing** and should be sourced separately.

---

## 2. Hard data returned by the vendor

| Metric | Value |
|---|---|
| Market capitalisation | **$1,219,764,944,896** (~$1.22T) |
| 52-week high | **$97,860.60** |
| 52-week low | **$55,149.57** |
| 50-day moving average | **$77,135.95** |
| 200-day moving average | **$72,427.41** |

---

## 3. Derived metrics (arithmetic from the data above — no assumptions beyond an explicit supply estimate)

**Implied spot price.** Dividing vendor market cap by circulating supply. Bitcoin's circulating supply is ~19.8–20.0M coins in this period; the implied price is remarkably insensitive to that range:

| Assumed circulating supply | Implied spot |
|---|---|
| 19.8M BTC | ~$61,600 |
| 19.9M BTC | ~$61,300 |
| 20.0M BTC | ~$61,000 |

→ **Implied spot ≈ $61.0–61.6k.** (Flag: supply figure is external context, not vendor-supplied. The *conclusion* below holds across the whole band.)

**Trend and positioning math:**

| Derived metric | Calculation | Result | Read |
|---|---|---|---|
| Drawdown from 52-wk high | (61,300 − 97,860.6)/97,860.6 | **−37.4%** | Deep bear-phase drawdown |
| Premium to 52-wk low | (61,300 − 55,149.6)/55,149.6 | **+11.2%** | Thin cushion above the low |
| Price vs 200-DMA | 61,300 / 72,427.4 − 1 | **−15.4%** | Below the long-term trend line |
| Price vs 50-DMA | 61,300 / 77,136.0 − 1 | **−20.5%** | Sharply below the short-term trend line |
| 50-DMA vs 200-DMA | 77,136 / 72,427.4 − 1 | **+6.5%** (compressing) | Death-cross setup forming |
| Position within 52-wk range | (61,300 − 55,149.6)/(97,860.6 − 55,149.6) | **14.4%** | Bottom ~1/7th of the range |
| 52-wk range midpoint | (97,860.6 + 55,149.6)/2 | **$76,505** | Price is ~20% below mid-range |

**Interpretation:** the 50-DMA is still *above* the 200-DMA, so the long-term trend configuration has not officially flipped — but the gap is only 6.5% and narrowing, while price trades 15–20% *below both* averages. That is the classic signature of a trend in the process of rolling over: averages lag price, and the short average is falling toward a bearish cross. Price sitting in the bottom 14% of the 52-week range with a −37% drawdown is a **confirmed corrective/bear regime**, not a dip within an uptrend.

---

## 4. Structural "fundamentals" of the asset (protocol-level facts, not vendor data)

These are the only fundamental-style anchors that genuinely apply to `BTC-USD`:

- **Hard-capped supply:** 21,000,000 BTC maximum; ~19.8–20.0M already issued (>94% of terminal supply). Issuance is algorithmic, not discretionary — there is no dilution risk from a treasury decision, and no buyback.
- **Halving-driven supply shock:** block subsidy stepped down to **3.125 BTC/block** at the April 2024 halving (≈450 BTC/day gross new issuance). The next reduction is scheduled at block 1,050,000 (~2028). Current flow: new issuance is a small fraction of daily spot volume — supply is structurally inelastic to price.
- **No cash flows → no DCF, no P/E, no EV/EBITDA.** Intrinsic value cannot be computed from financial statements. Any valuation must come from flow-of-funds, cost-basis cohorts, or adoption curves — **none of which the vendor returned for this ticker.**
- **Cost-of-production / miner economics** (a genuine fundamental floor candidate): hinges on hashprice, network hashrate, and energy costs, plus post-halving miner margins. **Data unavailable in this workflow** — needs a separate on-chain/mining data source.
- **Reflexivity:** because there are no earnings to anchor price, `BTC-USD` is unusually sensitive to positioning, leverage, and liquidity conditions — trend and flow data carry *more* signal weight than they would for an equity.

---

## 5. Explicit data gaps (must be sourced before high-conviction sizing)

The following are the correct fundamental inputs for `BTC-USD` and were **not** available from the configured vendor:

1. MVRV ratio and realized price (aggregate cost-basis / holder profit-and-loss — the single best cycle-position gauge)
2. NUPL / net unrealized profit-loss, and the STH vs LTH cost-basis split (short-term-holder cost basis is a textbook overhead-resistance level; LTH capitulation marks cycle lows)
3. Realized cap vs market cap (capital inflow/outflow proxy)
4. Exchange netflows, spot ETF creations/redemptions, stablecoin supply
5. Perpetual funding rates, open interest, futures basis, options skew/IV
6. Network hashrate, hashprice, miner reserves, Puell Multiple
7. Spot volume/depth for execution-cost sizing (cap is $1.22T but daily liquidity is unquantified here)

**Without items 1–3 in particular, no credible statement can be made about whether $61k is cheap or expensive relative to aggregate holder cost basis** — which is exactly the question a "fundamental" view of BTC must answer.

---

## 6. Actionable read for traders

**What the data supports:**
- The asset is in a **confirmed corrective regime**: −37% from the 52-week high, below both the 50- and 200-DMA, in the bottom 14% of its annual range.
- Momentum is still negative and the 50/200-DMA gap is compressing → **risk of a formal death cross**, which historically triggers systematic/CTA de-risking and can extend downside.
- The **52-week low at $55,149.57** is the single most important reference level: it is only ~11% below implied spot, meaning risk/reward for fresh longs is poor relative to a level that has already been tested.
- **Resistance stack:** $72,427 (200-DMA) → $77,136 (50-DMA) → $76,505 (range midpoint). A reclaim of $72.4k is the minimum bar for a trend-repair thesis; failure to reclaim keeps rallies classified as counter-trend bounces.
- There is **no financial-statement floor** under the price — no earnings, book value, or dividend to catch a fall. The only "floor" candidates are cost-basis cohorts and miner economics, both currently unmeasured here.

**Stance:** I cannot validate a fundamental valuation for `BTC-USD` — the inputs required to do so are absent, and treating price structure as if it were a fundamental signal would be a category error. What the hard data *does* say is that the technical/positioning backdrop is bearish and defensive, with asymmetric downside to the $55k shelf and heavy overhead supply at $72–77k. For a fundamental-driven mandate with the required on-chain data unavailable, the correct action is to **hold existing exposure at benchmark weight, avoid fresh adds, and wait for either (a) a reclaim of the 200-DMA at ~$72.4k on volume, or (b) a retest of $55.1k accompanied by MVRV/STH-cost-basis capitulation readings** — the latter being the historically higher-quality accumulation zone, contingent on the missing on-chain confirmation.

**Invalidation / triggers to flip:**
- *Bullish repair:* sustained close above $72,427 (200-DMA), then $77,136 (50-DMA); MVRV back above its realized-price band.
- *Bearish acceleration:* break of $55,149.57 with funding-rate reset and rising exchange inflows → expect trend-following supply.

---

## 7. Key points summary

| Category | Item | Value / Finding | Signal |
|---|---|---|---|
| Data availability | Income statement | **NO_DATA_AVAILABLE** — no issuer, no earnings | N/A (expected) |
| Data availability | Balance sheet | **NO_DATA_AVAILABLE** — no corporate B/S | N/A (expected) |
| Data availability | Cash flow | **NO_DATA_AVAILABLE** — no cash flows | N/A (expected) |
| Market data | Market cap | **$1.2198T** | Large-cap, deep market |
| Market data | 52-week high | **$97,860.60** | Reference peak |
| Market data | 52-week low | **$55,149.57** | Critical support shelf |
| Market data | 50-day MA | **$77,135.95** | Overhead resistance (1st) |
| Market data | 200-day MA | **$72,427.41** | Overhead resistance (key) |
| Derived | Implied spot (cap ÷ ~19.9M supply) | **≈$61.3k** | — |
| Derived | Drawdown from 52-wk high | **−37.4%** | Bear regime |
| Derived | Premium to 52-wk low | **+11.2%** | Thin cushion |
| Derived | Price vs 200-DMA | **−15.4%** | Bearish |
| Derived | Price vs 50-DMA | **−20.5%** | Bearish |
| Derived | 50-DMA minus 200-DMA | **+6.5%, compressing** | Death-cross risk |
| Derived | Position in 52-wk range | **14.4% (bottom sixth)** | Weak |
| Structural | Supply cap / issued | 21.0M hard cap; ~19.8–20.0M mined (>94%) | Inelastic supply |
| Structural | Issuance | 3.125 BTC/block (~450 BTC/day) | Post-2024-halving scarcity |
| Structural | Valuation method | No DCF/P/E possible; requires MVRV, realized cap, flows | **Data gap** |
| Data gap | MVRV / realized price / NUPL | **Not available** | Blocks valuation conviction |
| Data gap | ETF flows, exchange netflow, funding/OI | **Not available** | Blocks flow confirmation |
| Data gap | Hashrate, hashprice, miner reserves | **Not available** | Blocks cost-floor analysis |
| Trade level | Support | $55,149.57 | Break = bearish acceleration |
| Trade level | Resistance | $72,427.41 → $77,135.95 | Reclaim = trend repair |
| Action | Posture | Hold benchmark weight; no fresh adds; wait for confirmation | Defensive |

---

FINAL TRANSACTION PROPOSAL: **HOLD** `BTC-USD`

*(Rationale: the asset is in a confirmed −37% corrective regime trading 15–20% below both key moving averages and in the bottom 14% of its 52-week range, with a compressing 50/200-DMA spread flagging death-cross risk — while the crypto-native fundamental inputs required to justify either accumulation or outright exit (MVRV, realized price, cost-basis cohorts, flows, miner economics) are unavailable in this workflow and must not be fabricated. Hold at benchmark weight with no fresh adds until either a reclaim of $72,427 or a capitulation retest of $55,150 with on-chain confirmation.)*