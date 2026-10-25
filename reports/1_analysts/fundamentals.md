# Fundamental Analysis Report — `BTC-USD` (Bitcoin USD, CCC)

**Analysis date:** 2026-10-24 | **Data retrieved:** 2026-10-25 (vendor snapshot timestamp) | **Ticker used in all calls:** `BTC-USD`

---

## 1. Executive summary & critical data caveat

`BTC-USD` is **Bitcoin, a decentralized crypto asset — not an operating company.** As anticipated, the standard corporate fundamental stack is **entirely unavailable** for this symbol. I queried both quarterly and annual frequencies across all three statement tools:

| Tool | Frequency attempted | Result |
|---|---|---|
| `get_fundamentals` | — | ✅ Returned market snapshot (price/market-cap data only) |
| `get_balance_sheet` | quarterly + annual | ❌ `NO_DATA_AVAILABLE` — "no balance sheet data" |
| `get_income_statement` | quarterly + annual | ❌ `NO_DATA_AVAILABLE` — "no income statement data" |
| `get_cashflow` | quarterly + annual | ❌ `NO_DATA_AVAILABLE` — "no cash flow data" |

**This is the correct and expected outcome, not a data failure to work around.** Bitcoin has no revenue, earnings, EPS, book value, debt, cash flow, or shareholder equity. Any report presenting such line items for `BTC-USD` would be fabricated. Per the tool's instruction, I have **not estimated or invented statement values.**

Accordingly, this report delivers (a) the full market-structure evidence the vendor *did* return, (b) arithmetic derivations from that data, (c) the protocol-level "fundamental" variables that actually drive Bitcoin, and (d) explicit guidance on what data must be substituted for a genuine fundamental view.

---

## 2. What the vendor actually returned (raw fundamentals)

| Metric | Value |
|---|---|
| Name | Bitcoin USD |
| Exchange | CCC |
| **Market Cap** | **$1,605,086,740,480** (≈ $1.605 trillion) |
| 52-Week High | $116,273.31 |
| 52-Week Low | $57,747.77 |
| 50-Day Moving Average | $81,800.72 |
| 200-Day Moving Average | $72,900.84 |

No price, volume, supply, or on-chain fields were returned. **The vendor did not supply a spot price**, so I derive an implied spot below and flag it clearly as an *estimate*, not vendor data.

---

## 3. Derived analytics (all arithmetic shown, no invented inputs)

**Implied spot price.** Market cap ÷ circulating supply. The vendor returned no supply figure; using Bitcoin's protocol-fixed issuance schedule (post-April-2024 halving; supply ≈19.6M–20.1M BTC in Oct 2026) gives:

- 1,605,086,740,480 ÷ 20.1M ≈ **$79,855**
- 1,605,086,740,480 ÷ 19.6M ≈ **$81,893**
- **Working estimate: ≈ $80,000–$81,000**

*Consistency check:* this sits ~1–2% below the 50-day average of $81,800.72 — internally coherent, indicating the snapshot is **fresh, not stale**. (Treat the exact spot as ±$1,500 and verify against a live quote before execution.)

**Position within the 52-week range**

| Derivation | Calculation | Result |
|---|---|---|
| 52-week range width | (116,273.31 − 57,747.77) ÷ 57,747.77 | **+101.3%** (high is 2.01× the low) |
| Position in range (at ~$80,400) | (80,400 − 57,747.77) ÷ 58,525.54 | **~38.7%** (lower-middle third) |
| Drawdown from 52-week high | 80,400 ÷ 116,273.31 − 1 | **−30.9%** |
| Premium to 52-week low | 80,400 ÷ 57,747.77 − 1 | **+39.2%** |
| Distance to 50-DMA | 80,400 ÷ 81,800.72 − 1 | **−1.7%** (just below) |
| Distance to 200-DMA | 80,400 ÷ 72,900.84 − 1 | **+10.3%** (above) |
| 50-DMA vs 200-DMA spread | 81,800.72 ÷ 72,900.84 − 1 | **+12.2%** (bullish alignment) |

**The structural read:** the 50-day average sits **12.2% above** the 200-day average — an intact intermediate-term uptrend — yet price is **below** the 50-day and **31% below** the 52-week high. That combination describes a **corrective consolidation inside a bull trend**, not a trend breakdown. Momentum has cooled; the primary structure has not broken.

**Risk/reward framing (from ~$80,400)**

| Scenario | Level | Move |
|---|---|---|
| Reclaim 50-DMA (first confirmation) | $81,800.72 | **+1.7%** |
| Retest 52-week high | $116,273.31 | **+44.6%** |
| Lose 200-DMA (trend invalidation) | $72,900.84 | **−9.3%** |
| Retest 52-week low | $57,747.77 | **−28.2%** |

A position risk-managed at the 200-DMA against a 52-week-high objective screens at roughly **4.8:1 reward-to-risk**. Note the gap between $81,800 and $116,273 is **devoid of reference levels in this dataset** (no intermediate MAs or prior pivots were returned) — expect low-friction, high-velocity movement through that zone in either direction.

**Volatility implication.** A 2.01× high/low ratio over twelve months is an extreme realized-volatility regime. For equal portfolio risk contribution, a `BTC-USD` allocation should be sized at roughly **one-third to one-half** of an equivalent-volatility equity position.

---

## 4. The actual "fundamentals" of `BTC-USD` (protocol mechanics)

Because corporate statements don't exist, Bitcoin's fundamental drivers are supply schedule, network security, and demand flows. The supply side is **protocol-fixed and verifiable**, not vendor data:

- **Issuance:** post-April-2024 halving, block subsidy = **3.125 BTC**, ~144 blocks/day → **~450 BTC/day**, **~164,000 BTC/year**.
- **Inflation rate:** ~164k ÷ ~19.9M supply ≈ **0.8%/yr** — structurally below gold (~1.5–2%) and far below fiat expansion. This is Bitcoin's core scarcity thesis.
- **Next halving:** ~April 2028 (subsidy → 1.5625 BTC), mechanically cutting new supply in half again.
- **Hard cap:** 21,000,000 BTC; ~95% already mined. Supply is **perfectly inelastic to price** — the defining difference from every commodity, where higher prices elicit new production.
- **No counterparty/issuer:** no management, no board, no earnings revisions, no credit risk, no dividend, no dilution of the traditional kind.

**Implication for traders:** there is no "earnings catalyst." Bitcoin reprices on **liquidity, real yields, and flow** — spot ETF creations/redemptions, corporate treasury accumulation, exchange balances, and derivatives funding — none of which this toolset exposes.

---

## 5. Explicit data gaps (do not infer these from this report)

The following were **not** available and must be sourced before sizing a position:

1. Live spot price, volume, bid/ask, order-book depth, futures basis, funding rates, open interest.
2. On-chain valuation: MVRV, realized cap, SOPR, net unrealized P/L, dormancy, long-term-holder supply, exchange netflows.
3. Miner economics: hashrate, difficulty, hashprice, miner capitulation signals.
4. Flow data: spot ETF net creations/redemptions, stablecoin supply growth, CME positioning.
5. Macro: real yields (10Y TIPS), DXY, global M2, equity risk appetite.
6. Regulatory/event calendar specific to the 2026-10-24 window.
7. Whether the $116,273.31 52-week high is also an all-time high — **not determinable** from this dataset.

---

## 6. Actionable conclusions

1. **Regime classification: bullish structure, corrective phase.** 50-DMA > 200-DMA by 12.2% keeps the medium-term trend constructive; price under the 50-DMA and 31% off the high means near-term momentum is negative. **Do not chase; do not panic-sell.**
2. **$81,800 is the pivot.** A daily close reclaiming the 50-DMA reopens the path toward the $116k high. Failure to reclaim keeps the market in "lower-middle of range" chop.
3. **$72,900 (200-DMA) is the invalidation line.** A sustained break there flips the structural read to bearish and puts $57,748 (52-week low) in play — a further 21%. This is the single most important risk trigger.
4. **Asymmetry favors patient accumulation.** ~4.8:1 reward-to-risk from ~$80.4k against a 200-DMA stop is attractive for swing positioning; scale entries in tranches rather than a single clip given the 101% annual range.
5. **Volatility-adjust sizing** to ⅓–½ of an equity-equivalent risk budget.
6. **Fundamental conviction is not establishable with this toolset.** This is a price-structure and positioning call, not a fundamental one. Any trader requiring an on-chain/flow-confirmed thesis must augment with the data in §5 before committing capital.

---

## 7. Key points summary

| Category | Item | Value / Read | Evidence status |
|---|---|---|---|
| Identity | Asset | Bitcoin USD (`BTC-USD`), crypto asset — **not a company** | Resolved identity |
| Market cap | Total network value | **$1.605 trillion** | ✅ Vendor |
| Price | Implied spot (derived) | ≈ **$80,000–$81,000** | ⚠️ Derived (cap ÷ est. supply) |
| Range | 52-week high / low | $116,273.31 / $57,747.77 | ✅ Vendor |
| Range | Width / high-to-low ratio | **+101.3% / 2.01×** | ✅ Derived |
| Position | Spot within 52-wk range | **~38.7%** (lower-middle) | ✅ Derived |
| Trend | 50-DMA / 200-DMA | $81,800.72 / $72,900.84 | ✅ Vendor |
| Trend | 50-DMA vs 200-DMA | **+12.2% — uptrend intact** | ✅ Derived |
| Trend | Spot vs 50-DMA / 200-DMA | **−1.7% / +10.3%** | ✅ Derived |
| Drawdown | From 52-wk high / above low | **−30.9% / +39.2%** | ✅ Derived |
| Levels | Support / Resistance | $81,800 pivot, $72,900 invalidation, $57,748 floor / $116,273 target | ✅ Derived |
| Risk/Reward | To 52-wk high vs 200-DMA stop | **≈ 4.8 : 1** | ✅ Derived |
| Supply | Issuance / inflation / cap | 3.125 BTC/block, ~450 BTC/day, ~0.8%/yr, 21M hard cap | Protocol mechanics (not vendor) |
| Fundamentals | Balance sheet, income, cash flow | **UNAVAILABLE — no data at any frequency** | ❌ Tool-verified absence |
| Fundamentals | On-chain, flows, funding, macro | **Not exposed by toolset — must be sourced externally** | ❌ Gap |
| Volatility | Sizing guidance | ⅓–½ of equity-equivalent risk budget | Judgment |
| Stance | Verdict | Constructive **HOLD**; accumulate in tranches on dips toward $72.9k–$76k; hard stop below 200-DMA | Synthesis |

---

**Bottom line:** `BTC-USD` cannot be analyzed fundamentally in the corporate sense — all three statement tools returned verified `NO_DATA_AVAILABLE` across quarterly and annual frequencies, and I have not fabricated financials. What the data supports is a clear structural read: an intact uptrend (50-DMA 12.2% above the 200-DMA) currently in a corrective pullback (31% off the 52-week high, just under the 50-DMA), offering favorable asymmetry while $72,900 holds.

FINAL TRANSACTION PROPOSAL: **HOLD**