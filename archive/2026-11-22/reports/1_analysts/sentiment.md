**Overall Sentiment:** **Neutral** (Score: 5.0/10)
**Confidence:** Low

## BTC-USD Sentiment Report — 2026-11-14 to 2026-11-21

**Bottom line: no measurable sentiment signal. This is a data-availability failure, not a neutral market read.** All three sentiment sources failed to return content for the window. I am scoring `Neutral` / 5.0 strictly because the inputs are silent, and I am flagging `confidence: low`. A trader should treat this as "no sentiment input" and rely on price/technical and on-chain evidence, not as evidence that positioning is balanced.

---

### 1. Source-by-source breakdown

**News headlines (Yahoo Finance, past 7 days) — UNAVAILABLE**
- Tool returned a hard failure: `Error fetching news for BTC-USD: *** YAHOO! FINANCE IS CURRENTLY DOWN! ***`
- Zero headlines retrieved. No institutional framing signal exists for this window.
- Consequence: the slower-moving, fact-driven institutional layer is entirely missing. There is no way to confirm or rule out event risk (regulatory action, ETF flows, macro prints, exchange/news incidents) around 2026-11-14 to 2026-11-21.

**StockTwits (retail cashtag flow) — UNAVAILABLE**
- Tool returned `<stocktwits unavailable: HTTPError>`.
- Zero messages, therefore **no Bullish/Bearish ratio can be computed**. I explicitly decline to infer a ratio; there is no sample. The usual guidance (70/30 = moderately bullish, ≥90/10 = contrarian over-extension risk, 50/50 = uncertainty) cannot be applied.
- Consequence: the fast-moving retail layer is also missing. Notably, the two most *responsive* sources failed simultaneously, which often indicates a vendor/API outage rather than genuine retail silence on BTC-USD. Outages tend to cluster across Yahoo properties and connected endpoints.

**Reddit (r/wallstreetbets, r/stocks, r/investing, past 7 days) — EMPTY**
- `<no Reddit posts found mentioning BTC across r/wallstreetbets, r/stocks, r/investing in the past 7 days>`
- Zero posts, zero upvotes, zero comments. No engagement weighting is possible.
- This is the most informative of the three negatives: an absence of BTC mentions across three high-traffic communities is *unusual*, since BTC typically surfaces in r/wallstreetbets during either sharp drawdowns or melt-up phases. Either (a) the retrieval/indexing layer failed, or (b) BTC discussion has genuinely migrated off these subreddits. I cannot distinguish between these with available data, so I treat it as non-signal.

### 2. Cross-source divergences and alignments

There is nothing to compare. Because all three sources returned null/error states, there is **no divergence to exploit and no alignment to corroborate**. Any claim of "retail bullish vs. institutional cautious" for this week would be fabricated.

The one pattern worth noting: news *errored*, StockTwits *errored*, Reddit *returned empty*. Two distinct failure modes (transport error vs. successful-but-empty query) across three independent pipelines is more consistent with a broken collection run than with a real, market-wide sentiment blackout. This matters diagnostically — it argues for **re-running collection before acting**, not for concluding that sentiment is flat.

### 3. Dominant narrative themes

**None identifiable.** With zero documents, I cannot extract recurring topics (ETF flows, halving-cycle framing, macro liquidity, regulatory posture, leverage/liquidation cascades, dominance rotation). I will not synthesize themes from model priors — that would misrepresent this report as data-driven when it is not.

### 4. Catalysts and risks

No catalysts or risks can be surfaced *from the data*, since no data was retrieved. What I can state as a process risk rather than a market view:

- **Risk: acting on a silent feed.** `Neutral` here must not be read as "calm market." It is an empty input. Downstream sizing should not be nudged by this report.
- **Risk: event blindness.** Because the news feed failed, a material BTC-USD event in the 2026-11-14 → 2026-11-21 window would be invisible to this workflow. If the trading decision is materially BTC-sensitive, news retrieval should be independently re-attempted before the decision is finalized.
- **Risk: stale sentiment substitution.** There is a temptation to backfill with remembered or prior-period sentiment. I have not done so; prior-period sentiment is not evidence for this window.
- **Remediation:** re-run news (alternate vendor or retry after outage), re-run StockTwits, and broaden the Reddit query (e.g., add r/CryptoCurrency, r/Bitcoin, r/CryptoMarkets) with a wider date window — BTC conversation plausibly lives outside r/wallstreetbets, r/stocks, and r/investing, which would explain the empty result without implying market silence.

### 5. Summary table of key sentiment signals

| Signal | Direction | Source | Supporting evidence |
|---|---|---|---|
| Institutional news framing | **No signal (unavailable)** | Yahoo Finance | Request failed: "YAHOO! FINANCE IS CURRENTLY DOWN!" — 0 headlines retrieved |
| Retail cashtag sentiment | **No signal (unavailable)** | StockTwits | `HTTPError` — 0 messages, so no Bullish/Bearish ratio exists |
| Community discussion / engagement | **No signal (empty)** | Reddit: r/wallstreetbets, r/stocks, r/investing | 0 posts, 0 upvotes, 0 comments in past 7 days |
| Cross-source divergence | **Not assessable** | All three | No non-null source pairs available for comparison |
| Dominant narrative theme | **None identifiable** | All three | Zero documents to extract themes from |
| Data-quality flag | **Degraded** | Meta | 2 transport failures + 1 empty result across 3 independent pipelines → likely collection outage, warrants re-run |

**Actionable read for the trader:** this is an informational null. Sentiment should be assigned **zero weight** in the BTC-USD decision for 2026-11-21 until collection is successfully re-run. If a directional sentiment read is required to complete the workflow, flag the gap upstream rather than relying on this Neutral score, which reflects missing data rather than balanced positioning.