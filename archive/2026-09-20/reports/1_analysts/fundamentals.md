# Fundamental Analysis Report — `BTC-USD` (Bitcoin USD)
**Exchange:** CCC | **Analysis Date:** 2026-09-19 | **Data Retrieval Timestamp:** 2026-09-20 09:03:52

---

## 1. Executive Summary

`BTC-USD` is **Bitcoin**, a decentralized digital asset — **not a company**. Accordingly, the standard fundamental analysis toolkit (income statement, balance sheet, cash flow statement) is **structurally inapplicable**, and this was confirmed empirically: **all three financial-statement endpoints returned `NO_DATA_AVAILABLE`** at both quarterly and annual frequencies, across every configured vendor.

The **only usable fundamental data** available for `BTC-USD` is market/valuation data returned by the `get_fundamentals` endpoint. This report presents that data, explicitly flags what is unavailable, and derives actionable trading insights strictly from the verified figures. Per the tool's explicit instruction, **no financial values have been estimated or fabricated**.

---

## 2. Company Profile / Asset Identity

| Attribute | Value |
|---|---|
| Resolved Name | Bitcoin USD |
| Ticker | `BTC-USD` |
| Exchange | CCC |
| Asset Class | Cryptocurrency (Layer-1 digital asset) |
| Issuer / Legal Entity | **None** — decentralized protocol, no corporate issuer |
| Reporting Currency | USD (quote currency only) |
| Sector / Industry Classification | Not applicable (not a corporation) |

**Key implication:** There is no management team, no board, no earnings, no dividend, no shareholder equity, no debt structure, and no SEC/regulatory filings of the kind that populate equity fundamentals. Bitcoin's "fundamentals" are instead driven by on-chain metrics (hashrate, active addresses, supply issuance, mining economics), macro liquidity, and regulatory/flow dynamics (e.g., spot ETF flows) — **none of which are exposed by the four tools available in this workflow.**

---

## 3. Available Fundamental / Market Data

Source: `get_fundamentals("BTC-USD", "2026-09-19")`

| Metric | Value (USD) |
|---|---|
| **Market Capitalization** | **$1,623,935,680,512 (~$1.624 trillion)** |
| 52-Week High | $126,198.07 |
| 52-Week Low | $57,747.77 |
| 50-Day Moving Average | $72,841.10 |
| 200-Day Moving Average | $70,462.16 |

### Derived Metrics (calculated from verified inputs)

| Derived Metric | Calculation | Result | Interpretation |
|---|---|---|---|
| 50DMA vs 200DMA spread | (72,841.10 − 70,462.16) / 70,462.16 | **+3.38%** | 50DMA above 200DMA → **bullish medium-term structure** (post-golden-cross regime) |
| 52-Week Range Width | (126,198.07 − 57,747.77) / 57,747.77 | **+118.5%** | Extreme annual volatility — range spans >2x |
| 52-Wk High vs. 200DMA | (126,198.07 − 70,462.16) / 70,462.16 | **+79.1%** | Price structure has cooled substantially from peak trend |
| 52-Wk Low vs. 200DMA | (57,747.77 − 70,462.16) / 70,462.16 | **−18.0%** | Deep trough occurred meaningfully below trend |
| Midpoint of 52-Wk Range | (126,198.07 + 57,747.77) / 2 | **$91,972.92** | Statistical mean-reversion reference |
| Implied price (approx.)* | $1.624T ÷ ~19.9M BTC supply | **~$81,600** | Price above both MAs, but ~35% below 52-wk high |

> \* **Caveat:** The tools did **not** return a spot price or circulating supply. The implied price above is a *rough approximation* using Bitcoin's widely known ~19.9M circulating supply. Treat it as directional only — **not** as a verified quote. The genuinely verified anchor is the **~$1.62T market cap**.

### Positional Read (using the ~$81.6K implied price, directional only)
- **vs. 50DMA ($72,841):** ~+12% above → short-term momentum constructive
- **vs. 200DMA ($70,462):** ~+16% above → trend support intact
- **vs. 52-wk high ($126,198):** ~−35% → significant drawdown / distribution phase above
- **vs. 52-wk low ($57,748):** ~+41% → strong recovery off the lows

---

## 4. Financial Statements — Data Unavailability Report

| Statement | Frequency Attempted | Result |
|---|---|---|
| Balance Sheet | Quarterly | **NO_DATA_AVAILABLE** |
| Balance Sheet | Annual | **NO_DATA_AVAILABLE** |
| Cash Flow Statement | Quarterly | **NO_DATA_AVAILABLE** |
| Cash Flow Statement | Annual | **NO_DATA_AVAILABLE** |
| Income Statement | Quarterly | **NO_DATA_AVAILABLE** |
| Income Statement | Annual | **NO_DATA_AVAILABLE** |

**Reason:** `BTC-USD` is a cryptocurrency, not an operating company. It has no financial statements to report. This is an **expected and correct outcome**, not a data error, delisting, or coverage failure — the vendor simply has no corporate fundamentals for a decentralized asset.

**Explicit statement per tool guidance:** No values have been estimated or fabricated to fill these gaps.

---

## 5. Actionable Insights for Traders

Based on the **only verified data available** (market cap, 52-week range, moving averages), the following are actionable:

1. **Trend structure is bullish but decelerating.** The 50DMA ($72,841) sits **+3.4% above** the 200DMA ($70,462), confirming a positive medium-term trend. However, the narrow spread suggests the trend is **early-cycle or consolidating**, not steeply accelerating.

2. **Large overhead supply exists.** With the 52-wk high at **$126,198**, any price in the ~$80K area faces **~35% of overhead resistance** to revisit highs — implying a thick distribution zone and capping near-term upside potential.

3. **Volatility is extreme; size positions accordingly.** A **118% annual range** means risk management (position sizing, stop placement) must be far wider than for equities. ATR-based stops are essential.

4. **Range mid-point ~$91,973 is a key pivot.** It serves as the mean-reversion magnet between the $57.7K low and $126.2K high — a useful reference for target/resistance planning.

5. **Fundamentals are macro/flow-driven, not earnings-driven.** Since no income/balance/cashflow exists, traders **must not** rely on P/E, EPS, or book-value frameworks for `BTC-USD`. Substitute catalysts: spot ETF flows, Fed liquidity/policy, regulatory developments, halving-cycle supply dynamics, and on-chain data — **but note these are outside the scope of the available tools and could not be verified here.**

6. **Combined read:** Bullish trend (50DMA > 200DMA) + deep discount to highs + extreme range = a **constructive-but-consolidating** regime. Momentum-favorable for trend traders, while value/would-be dip buyers should note the ~35% drawdown shows the market has not yet reclaimed leadership highs.

---

## 6. Data Gaps & Limitations (Transparency Statement)

| Gap | Impact on Analysis |
|---|---|
| No spot price returned | Position vs. MAs derived from approximated supply — directional only |
| No circulating supply / issuance data | Cannot compute exact valuation per coin |
| No volume / liquidity data | Cannot assess market depth or flow |
| No on-chain metrics (hashrate, addresses, whale flows) | Core Bitcoin "fundamentals" unverifiable with given tools |
| No ETF flow / macro data | Key demand drivers unverifiable |
| No income/balance/cashflow statements | Standard fundamental analysis structurally impossible |
| 52-wk high/low are point-in-time, no timestamps | Cannot date the high/low for cycle positioning |

**Analyst note:** This workflow's toolkit is designed for **equity** fundamental analysis. For a crypto asset like `BTC-USD`, only the market-data layer of `get_fundamentals` is productive; the three financial-statement tools are inapplicable by construction. A complete Bitcoin analysis would require crypto-native/on-chain data sources not present in this toolset.

---

## 7. Summary Table — Key Points

| Category | Metric / Finding | Value | Signal / Insight |
|---|---|---|---|
| **Identity** | Asset | Bitcoin USD (`BTC-USD`) | Crypto asset, **not a company** |
| **Valuation** | Market Cap | **$1.624 Trillion** | Large-cap/mega-cap crypto by market value |
| **Range** | 52-Week High | $126,198.07 | Major overhead resistance (~35% above implied price) |
| **Range** | 52-Week Low | $57,747.77 | Cycle trough / support reference |
| **Range** | 52-Wk Range Width | +118.5% | Extreme volatility — wide risk parameters required |
| **Trend** | 50-Day MA | $72,841.10 | Short-term trend support |
| **Trend** | 200-Day MA | $70,462.16 | Long-term trend support |
| **Trend** | 50DMA vs 200DMA | **+3.38%** | **Bullish** medium-term structure (golden-cross regime) |
| **Derived** | Range Midpoint | ~$91,972.92 | Mean-reversion pivot |
| **Derived** | Implied Price* | ~$81,600 | Above both MAs, below range midpoint |
| **Financials** | Balance Sheet | **UNAVAILABLE** | No corporate financials exist |
| **Financials** | Income Statement | **UNAVAILABLE** | No earnings; no EPS/P-E applicable |
| **Financials** | Cash Flow Statement | **UNAVAILABLE** | No corporate cash flows |
| **Methodology** | Framework | Market-data only | Avoid equity valuation models for `BTC-USD` |
| **Overall** | Regime | Constructive-but-consolidating | Trend up, deeply off highs, extreme range |

---

### Bottom Line
`BTC-USD` cannot be analyzed with company fundamentals because it is not a company — all financial statements are unavailable by design, and no values were fabricated. The **only verified fundamental signal is market structure**: a **~$1.62T market cap**, a **bullish 50DMA > 200DMA alignment (+3.4%)**, tempered by a **~35% discount to the 52-week high** and an **extraordinary 118% annual range**. Traders should treat this as a **trend-following / macro-liquidity asset** with wide volatility bands, not an earnings-driven equity.

**No transaction proposal is issued on this asset**, as the fundamental evidence base is limited to market structure and no corroborating equity-style data exists in this workflow's toolset.