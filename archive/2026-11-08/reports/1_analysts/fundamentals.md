# Fundamental Analysis Report — `BTC-USD` (Bitcoin USD)
**Exchange:** CCC | **Analysis date:** 2026-11-07 | **Data retrieved:** 2026-11-08 09:05

---

## 1. Executive Summary

`BTC-USD` is a **crypto asset, not an operating company**. As expected, the vendor's corporate-fundamental data layer returned **no balance sheet, no income statement, and no cash flow statement** at either quarterly or annual frequency. Bitcoin has no revenue, no earnings, no equity, no debt, no management team, and no filing obligations — so any report that filled those fields would be fabricated. **I did not estimate or substitute values for the missing statements.**

What *is* available is a market-data snapshot, which is the only genuine "fundamental" input the toolset supplied:

| Item | Value |
|---|---|
| Market Cap | **$1,522,629,083,136** (~$1.52 trillion) |
| 52-Week High | **$107,428.26** |
| 52-Week Low | **$57,747.77** |
| 50-Day Average | **$81,871.81** |
| 200-Day Average | **$73,187.78** |

**Verdict: HOLD / neutral-with-a-defensive-tilt.** The asset is the dominant, institutionally-integrated crypto reserve asset with a fixed, programmatically scarce supply — a genuinely strong long-horizon fundamental. But the price structure is deteriorating: spot is ~7% below its 50-day average, ~29% off its 52-week high, and sitting in the bottom third of its 52-week range while **directly testing the 200-day average as the last major support**.

---

## 2. Data Availability — Explicit Disclosure

| Statement / Dataset | Frequency | Result |
|---|---|---|
| Comprehensive fundamentals | — | **Partial** (market data only: name, market cap, 52-wk high/low, 50/200-DMA) |
| Balance sheet | Quarterly | **NO_DATA_AVAILABLE** |
| Balance sheet | Annual | **NO_DATA_AVAILABLE** |
| Income statement | Quarterly | **NO_DATA_AVAILABLE** |
| Income statement | Annual | **NO_DATA_AVAILABLE** |
| Cash flow statement | Quarterly | **NO_DATA_AVAILABLE** |
| Cash flow statement | Annual | **NO_DATA_AVAILABLE** |

**Reason:** the configured vendor does not cover crypto assets for financial-statement endpoints. This is a **structural coverage limitation, not a sign of distress, delisting, or invalidity** — the ticker `BTC-USD` is live and returned valid market data, so the resolved identity (Bitcoin USD, Exchange CCC) is **confirmed, not disproved**.

**Analytical implication:** the classic company-fundamental workflow (margins, ROE, leverage, FCF, guidance, filings) is *inapplicable*. It must be replaced by the crypto-native fundamental stack, laid out in Sections 4–7. I flag clearly below which observations are **tool-derived** versus **framework/general market knowledge** versus **derived arithmetic**.

---

## 3. Price Structure — Derived Analytics from Tool Data

Using the returned market snapshot, and an assumed circulating supply of roughly **19.9–20.1M BTC** (post-April-2024-halving issuance of 3.125 BTC/block plus historical issuance; *estimated, not vendor-supplied*), the implied spot price is approximately **$76,000–$76,500**. All figures below are **derived arithmetic, clearly labeled as estimates**:

| Metric | Derived Value | Interpretation |
|---|---|---|
| Implied spot (market cap ÷ ~20.0M BTC) | **~$76,300** | Consistent with the DMA/range geometry |
| Position in 52-week range | **~37%** (bottom-middle of range) | Weak, but not capitulation territory |
| Drawdown from 52-wk high ($107,428) | **~-29%** | A cyclical-scale correction, not a collapse |
| Gain from 52-wk low ($57,748) | **~+32%** | Structure still net higher over 12 months |
| Spot vs 50-day avg ($81,872) | **~-6.8%** | Short-term trend is down; holders below water on a 2-month basis |
| Spot vs 200-day avg ($73,188) | **~+4.3%** | Long-term trend still intact — barely |
| 50-DMA vs 200-DMA | **50-DMA ~+11.9% above** | Golden-cross configuration **still nominally bullish** |

### The single most important structural read
The 50-day average ($81,872) is **still decisively above** the 200-day average ($73,188). That is diagnostic: **this is a recent, sharp breakdown, not a year-long grind lower.** If price had been falling for twelve months, the 50-DMA would already be below the 200-DMA. Instead, spot has sliced through the 50-DMA quickly and is now **parked on top of the 200-DMA**.

**Two concrete scenarios:**
- **Bull resolution (defense of ~$73.2k):** failure to break the 200-DMA, reclaim of $81.9k, and the 50-DMA holds above the 200-DMA. The golden cross remains valid and the -29% drawdown reads as a mid-cycle reset.
- **Bear resolution (loss of ~$73.2k):** a daily/weekly close below the 200-DMA flips the long-term trend negative for the first time in this window, and a 50/200 **death cross** becomes mechanically likely within weeks — an event that historically triggers systematic/CTA de-risking. Downside magnet then becomes the **$57,748** 52-week low, ~24% below current levels.

---

## 4. The Correct "Fundamentals" for `BTC-USD`: Supply-Side (Protocol Level)

Bitcoin's substitute for a capital structure and a cash-flow statement is its **monetary policy code**:

- **Hard cap of 21,000,000 BTC** enforced by consensus rules — the only asset in the toolset's universe with a mathematically fixed terminal supply.
- **Halving cycle:** block subsidy stepped to **3.125 BTC** in April 2024 and steps to **1.5625 BTC around 2028**. Annualized new issuance is now well under 1% of circulating supply and falling — structurally tighter than gold's mine supply growth.
- **Zero counterparty liabilities:** no debt, no pension obligations, no dilution risk from management, no refinancing wall. The "balance sheet" is the unspent transaction output set — verifiable by any node, not attested by an auditor.
- **No cash flows ⇒ no DCF.** Valuation must be relative (monetary premium, network value) rather than discounted-cash-flow. Anyone applying P/E, EV/EBITDA, or book value to `BTC-USD` is using a category error.

**Fundamental strength:** supply is inelastic and *decreasingly* elastic. This is the core, non-negotiable bullish pillar, and it is unaffected by the current price weakness.

## 5. Demand-Side Fundamentals (What Actually Drives the Price)

Since there are no earnings to model, demand is the entire fundamental equation. The demand stack to monitor:

1. **Spot ETF access (US and other jurisdictions)** — creates persistent, price-insensitive, adviser-driven allocation flows. This is the single largest structural demand change of the post-2024 era. ETF net creations/redemptions are the closest analogue to "institutional order flow" data.
2. **Corporate treasury adoption** — public companies holding BTC as a reserve asset create reflexive equity-linked demand and, conversely, forced-seller risk if those equities de-rate.
3. **Sovereign/state-level accumulation and strategic reserves** — a slow, lumpy, but structurally sticky bid.
4. **Network settlement and fee demand** — the only genuine "revenue" analogue; watch fee revenue, active addresses, and Layer-2 settlement volumes.
5. **Macro liquidity** — real rates, USD strength, and global liquidity conditions remain the dominant short-to-medium-term beta driver. Crypto is a long-duration liquidity asset.

## 6. Valuation & Sentiment Metrics That Must Be Sourced Externally

**None of the following are available from the configured toolset** — I am naming them so the trading desk knows exactly where the evidence gap is, not asserting values:

| Metric | What It Tells You | Status |
|---|---|---|
| MVRV / MVRV Z-score | Aggregate holder profit/loss → cycle extremes | Not available |
| Realized price / realized cap | On-chain cost basis; the "true" support line | Not available |
| NVT ratio | Network value vs transaction throughput | Not available |
| Puell Multiple | Miner revenue stress → capitulation timing | Not available |
| Hashrate & difficulty | Security budget and miner economics | Not available |
| Exchange netflow/balances | Supply available to sell | Not available |
| Perp funding & open interest | Leverage build-up → liquidation risk | Not available |
| 200-week moving average | Historical cycle floor (never broken in prior cycles) | Not available |

**Actionable gap:** before sizing any position in `BTC-USD`, obtain realized price and MVRV. Whether spot is above or below aggregate on-chain cost basis is the difference between "orderly correction" and "broad capitulation," and it is precisely the input this vendor cannot supply.

## 7. Comparative / Cycle Context

- **Dominance:** at ~$1.52T market cap, `BTC-USD` remains the reserve asset and liquidity anchor of the crypto complex. In drawdowns, capital rotates *into* BTC from altcoins — so BTC typically outperforms on the downside and underperforms early in recoveries.
- **Cycle positioning:** a 52-week high of $107,428 followed by a ~29% drawdown, with a still-bullish 50/200 configuration, is the geometry of a **maturing post-halving advance that has lost momentum and is now retesting its trend.** Historical cycles have featured 30–40% drawdowns *within* uptrends as well as 75–85% bear markets. The 200-DMA is the discriminator between the two.
- **Diminishing returns:** each successive halving cycle has produced a smaller percentage gain. Do not extrapolate the 2017 or 2021 magnitudes.

## 8. Risk Register (Asset-Specific)

| Risk | Severity | Note |
|---|---|---|
| Loss of 200-DMA → death cross → systematic de-risking | **High, immediate** | The live technical trigger |
| Sustained spot-ETF net redemptions | High | Removes the post-2024 structural bid |
| Leverage unwind / liquidation cascade | High | Crypto's reflexive amplifier; funding data unavailable here |
| Macro liquidity tightening / real-rate shock | High | Dominant beta driver, outside the asset's control |
| Regulatory action on access rails (ETF, custody, banking) | Medium | Structural, slow-moving, but high-impact |
| Miner capitulation → forced selling | Medium | Watch hashprice and difficulty adjustments |
| Concentration among large holders / custodians | Medium | Custodial and governance concentration risk |
| Quantum / cryptographic transition | Low near-term, high tail | Long-horizon protocol risk, not a 2026 trading input |

## 9. Actionable Insights

1. **`BTC-USD` cannot be traded off reported financials.** The data layer returned nothing usable for statements. Any signal must come from price structure, flow data, and on-chain metrics sourced elsewhere. Do not let a downstream process treat the NO_DATA flags as deterioration.
2. **The trade is defined by $73,188 (200-DMA).** This is the highest-information level in the dataset.
3. **Treat $81,872 (50-DMA) as the trend-repair line.** A reclaim restores the bullish read; repeated rejection confirms the breakdown.
4. **Position sizing should reflect the unresolved binary.** Long-term holders: the fixed-supply thesis is unimpaired, so no fundamental reason to exit — but the -29% drawdown and sub-50-DMA price argue against *adding* until the 200-DMA is defended on a closing basis.
5. **Scale, don't knife-catch.** If building exposure, ladder bids between $73.2k and the $57.7k 52-week low rather than committing at spot.
6. **Invalidation is objective:** a weekly close below $73,188 followed by a 50/200 death cross should cut gross exposure and flip the stance from HOLD to defensive.

---

## 10. Key Points Summary

| Category | Finding | Evidence / Source | Read |
|---|---|---|---|
| **Identity** | Bitcoin USD, Exchange CCC | `get_fundamentals` | Confirmed, valid, tradable |
| **Asset type** | Crypto asset — no corporate entity | Tool output + structure | Corporate fundamentals N/A |
| **Balance sheet** | **Unavailable** (Q & A) | `get_balance_sheet` | NO_DATA — vendor coverage gap, not distress |
| **Income statement** | **Unavailable** (Q & A) | `get_income_statement` | NO_DATA — no revenue/earnings exist |
| **Cash flow** | **Unavailable** (Q & A) | `get_cashflow` | NO_DATA — no FCF concept applies |
| **Market cap** | $1.5226 trillion | `get_fundamentals` | Largest crypto reserve asset |
| **52-wk high** | $107,428.26 | `get_fundamentals` | Reference peak |
| **52-wk low** | $57,747.77 | `get_fundamentals` | Downside magnet if 200-DMA fails |
| **50-day avg** | $81,871.81 | `get_fundamentals` | Overhead resistance / trend-repair line |
| **200-day avg** | $73,187.78 | `get_fundamentals` | **Critical support; the whole thesis hinges here** |
| **Implied spot** | ~$76,300 *(derived, est. ~20.0M supply)* | Market cap ÷ estimated supply | Between the two DMAs |
| **Range position** | ~37% of 52-wk range *(derived)* | Arithmetic | Weak but not capitulative |
| **Drawdown from high** | ~-29% *(derived)* | Arithmetic | Cyclical correction scale |
| **50 vs 200-DMA** | 50-DMA ~+11.9% above 200-DMA *(derived)* | Arithmetic | Golden cross intact — breakdown is recent |
| **Supply mechanics** | 21M hard cap; 3.125 BTC/block; ~2028 next halving | Protocol design (not tool-supplied) | Structural scarcity intact |
| **Valuation inputs** | MVRV, realized price, NVT, funding — **not available** | Toolset gap | Must be sourced externally before sizing |
| **Primary risk** | Close below $73,188 → death cross → systematic selling | Technical structure | Objective invalidation level |
| **Stance** | No fundamental sell signal; technical structure deteriorating | Synthesis | **HOLD**, ladder bids, don't add at spot |

---

**Bottom line for the desk:** `BTC-USD` has no financial statements to analyze and this vendor cannot supply them — that is a data-coverage fact, not a red flag on the asset. The genuine fundamentals (fixed 21M supply, decelerating issuance, institutional access via ETFs, zero counterparty liabilities) remain intact and unchanged. But the market-data snapshot shows spot ~7% below its 50-DMA, ~29% off its 52-week high, and sitting directly on the 200-DMA — a binary decision point. Hold existing exposure, do not add at current levels, accumulate toward $73.2k–$57.7k, and treat a weekly close below the 200-DMA plus a death cross as the objective signal to reduce risk.

FINAL TRANSACTION PROPOSAL: **HOLD**