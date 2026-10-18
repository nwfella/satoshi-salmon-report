# Fundamental Analysis Report — `BTC-USD` (Bitcoin USD)

**Analysis date:** 2026-10-17 | **Venue:** CCC | **Vendor snapshot:** 2026-10-18 09:05 UTC
**Identity verification:** Confirmed as `Bitcoin USD` (Exchange: CCC). This is a **crypto asset**, not an operating company. No ticker substitution was made.

---

## 1. Data Availability Audit (Critical Caveat)

I queried the full fundamental data stack at both quarterly and annual frequency. Results:

| Request | Ticker | Frequency | Result |
|---|---|---|---|
| `get_fundamentals` | `BTC-USD` | — | ✅ Partial (market data only) |
| `get_balance_sheet` | `BTC-USD` | Quarterly | ❌ NO_DATA_AVAILABLE |
| `get_balance_sheet` | `BTC-USD` | Annual | ❌ NO_DATA_AVAILABLE |
| `get_income_statement` | `BTC-USD` | Quarterly | ❌ NO_DATA_AVAILABLE |
| `get_income_statement` | `BTC-USD` | Annual | ❌ NO_DATA_AVAILABLE |
| `get_cashflow` | `BTC-USD` | Quarterly | ❌ NO_DATA_AVAILABLE |
| `get_cashflow` | `BTC-USD` | Annual | ❌ NO_DATA_AVAILABLE |

**Interpretation:** This is the expected and correct outcome. `BTC-USD` is a decentralized bearer asset — there is no issuer, no board, no fiscal year, and therefore **no income statement, balance sheet, or cash flow statement to report**. The vendor's absence of these statements does not indicate a delisted or invalid symbol; the market data returned is live and internally consistent (market cap ≈ price × circulating supply, see §3).

**No values have been estimated or fabricated.** Where I derive figures below, they are arithmetic on the returned data or explicitly labeled reference constants.

---

## 2. Returned Fundamentals Data (verbatim)

| Field | Value |
|---|---|
| Name | Bitcoin USD |
| Market Cap | **$1,628,705,783,808** (~$1.63T) |
| 52-Week High | **$116,273.31** |
| 52-Week Low | **$57,747.766** |
| 50-Day Average | **$81,322.90** |
| 200-Day Average | **$72,425.69** |

---

## 3. Derived Price & Valuation Metrics

Using a circulating supply of ~19.98M BTC (post-April-2024 halving; external reference constant, ~95.1% of the 21M hard cap mined):

**Implied spot price = $1,628,705,783,808 ÷ 19,980,000 ≈ $81,517**

| Derived Metric | Value | Read |
|---|---|---|
| Implied spot price | ~$81,517 | Current mark |
| vs. 52W High ($116,273.31) | **−29.9%** | Approaching bear-market drawdown territory |
| vs. 52W Low ($57,747.77) | **+41.2%** | Recovered well off the cycle low |
| vs. 50-day MA | **+0.24%** | Pinned *exactly* to the 50DMA — no momentum edge |
| vs. 200-day MA | **+12.6%** | Structurally bullish |
| Position within 52W range | **40.6%** | Lower half of the range |
| 52W range width (high ÷ low) | **2.01×** | Extremely high realized volatility |
| 50DMA vs 200DMA spread | **+12.3%** (50 > 200) | Golden-cross regime intact |
| Market cap at 52W high | ~$2.32T | Peak valuation reached |
| Market cap at 52W low | ~$1.15T | Trough valuation |
| Market cap drawdown from peak | **≈ −$694B** | ~30% of peak value erased |

**Key structural observation:** The 50DMA sits $8,897 (12.3%) above the 200DMA — a bullish trend skeleton — yet price has stalled to within 0.2% of the 50DMA. This is a classic **trend-intact / momentum-neutral** configuration: buyers defended the medium-term average, but the market has not been able to extend. The 50DMA is now effectively acting as the battleground line.

---

## 4. What Would Constitute "Fundamentals" for This Asset — and Status

For an operating company I would report revenue, margins, leverage, and cash conversion. For `BTC-USD`, the economically equivalent fundamental drivers are:

| Fundamental Driver | Status | Notes |
|---|---|---|
| Income statement / revenue / earnings | **N/A** | No issuer, no earnings |
| Balance sheet / cash flow | **N/A** | No corporate entity |
| Supply schedule / issuance rate | Not in vendor feed | Protocol-level: 3.125 BTC/block post-halving ≈ ~450 BTC/day ≈ ~0.82% annual inflation |
| Hard cap / scarcity | Not in vendor feed | 21,000,000 BTC immutable cap; ~95% mined |
| Next halving | Not in vendor feed | ~2028 (4-year cadence from April 2024) |
| Hashrate / network security | Not in vendor feed | — |
| On-chain activity (active addresses, fees, MVRV) | Not in vendor feed | — |
| Spot ETF flows / institutional balances | Not in vendor feed | — |
| Realized volatility / funding rates / open interest | Not in vendor feed | — |
| Regulatory/custody regime | Not in vendor feed | — |

The scarcity and issuance mechanics are the only true "fundamental" of `BTC-USD`, and they are protocol-determined rather than reported. Everything else that matters is flow- and sentiment-driven.

---

## 5. Actionable Insights for Traders

**1. The 50DMA (~$81,323) is the single most important level to watch.** Price is sitting on it with only 0.24% of cushion. A clean daily close and hold above it keeps the uptrend constructive; a decisive loss opens a path toward the 200DMA at ~$72,426, which would imply roughly a further **−11%** and a market cap near $1.45T.

**2. The trend regime is still bullish but decelerating.** 50DMA > 200DMA with a 12.3% spread means the golden-cross structure has not broken. Absent a break of the 200DMA, the correct structural read is *uptrend in consolidation*, not *bear market* — despite being 30% off the high.

**3. Range positioning at 40.6% argues against chasing strength.** Buying in the lower-middle of a 2× wide annual range with flat short-term momentum offers poor asymmetry. The higher-probability entries are (a) a confirmed reclaim/hold of the 50DMA with expanding volume, or (b) a flush into the $72–75K zone that holds the 200DMA.

**4. Volatility is the dominant risk factor, not fundamentals.** A 2.01× high/low ratio within 12 months means position sizing — not thesis — is the primary determinant of outcome. Stops placed tighter than ~8–10% around current price are highly likely to be noise-stopped.

**5. Reclaim of the 52W high (−29.9% away) would confirm a new leg; a break of $57,747 (−29.2% away) would confirm a full bear cycle.** Both boundaries are roughly equidistant, reinforcing a balanced risk/reward at current levels.

**6. Fundamental due diligence is genuinely limited here.** Because the vendor provides no on-chain, flow, or network data for `BTC-USD`, a fundamentals-only mandate cannot generate a high-conviction directional call. Any strong conviction must come from a technical/flow overlay that is outside this toolset.

---

## 6. Assessment

The available evidence is **neutral-to-constructive**: the long-term trend structure (price > 200DMA, 50DMA > 200DMA) remains intact and price is up 41% off the annual low, but the asset is 30% below its high, sitting flat on its 50-day average, and positioned in the lower 41% of a very wide 52-week range. With zero reported financial fundamentals by design, there is no valuation anchor to argue the asset is cheap or expensive.

**Stance: HOLD** — maintain existing exposure, do not add aggressively at the 50DMA without confirmation, and use ~$72.4K (200DMA) as the structural invalidation level for the bullish trend thesis.

---

## 7. Summary Table

| Category | Metric | Value | Signal / Implication |
|---|---|---|---|
| **Identity** | Ticker / Name / Venue | `BTC-USD` / Bitcoin USD / CCC | Crypto asset — no corporate issuer |
| **Data Quality** | Income statement | ❌ Unavailable (Q & A) | Not applicable to an asset with no issuer |
| | Balance sheet | ❌ Unavailable (Q & A) | Not applicable |
| | Cash flow statement | ❌ Unavailable (Q & A) | Not applicable |
| | Fundamentals (market data) | ✅ Available | Partial coverage only |
| **Valuation** | Market Cap | $1,628,705,783,808 | ~$1.63T |
| | Implied spot price (≈19.98M supply) | ~$81,517 | Mark |
| | Market cap at 52W high | ~$2.32T | Peak cycle valuation |
| | Market cap drawdown from peak | ≈ −$694B | ~30% of value erased |
| **Range** | 52W High | $116,273.31 | −29.9% away |
| | 52W Low | $57,747.77 | +41.2% above; −29.2% away |
| | Position in 52W range | 40.6% | Lower half — poor chase setup |
| | Range width (H/L) | 2.01× | Very high volatility |
| **Trend** | 50-day MA | $81,322.90 | Price +0.24% above — battleground |
| | 200-day MA | $72,425.69 | Price +12.6% above — structural support |
| | 50DMA vs 200DMA | +12.3% (50 > 200) | Golden-cross regime intact |
| **Protocol** | Hard cap / issuance | 21M cap; ~0.82% annual inflation | Only true fundamental; not vendor-sourced |
| **Risk** | Primary risk | Volatility + data blind spots | Size positions, not theses |
| **Decision** | Recommendation | **HOLD** | Neutral; add only on 50DMA reclaim or 200DMA flush |

FINAL TRANSACTION PROPOSAL: **HOLD**