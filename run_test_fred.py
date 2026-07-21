#!/usr/bin/env python3
"""Test run of TradingAgents on BTC-USD with DeepSeek V4 Flash + FRED data."""

import os
import sys
import logging
from pathlib import Path

# Load .env manually
env_path = Path(__file__).parent / ".env"
if env_path.exists():
    for line in env_path.read_text().strip().splitlines():
        if line.strip() and not line.startswith("#"):
            k, _, v = line.partition("=")
            os.environ.setdefault(k.strip(), v.strip())

print("=" * 70)
print("TRADINGAGENTS — BTC-USD TEST RUN (WITH FRED MACRO DATA)")
print("=" * 70)
print(f"DEEPSEEK_API_KEY set:     {'✓' if os.environ.get('DEEPSEEK_API_KEY') else '✗'}")
print(f"FRED_API_KEY set:         {'✓' if os.environ.get('FRED_API_KEY') else '✗'}")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "deepseek"
config["deep_think_llm"] = "deepseek-v4-flash"
config["quick_think_llm"] = "deepseek-v4-flash"
config["max_debate_rounds"] = 1
config["max_risk_discuss_rounds"] = 1
config["news_article_limit"] = 5
config["global_news_article_limit"] = 3
config["output_language"] = "English"
config["temperature"] = 0.3
config["data_vendors"] = {
    "core_stock_apis": "yfinance",
    "technical_indicators": "yfinance",
    "fundamental_data": "yfinance",
    "news_data": "yfinance",
    "macro_data": "fred",
    "prediction_markets": "polymarket",
}

ticker = "BTC-USD"
trade_date = "2026-07-14"

print(f"\nTicker:     {ticker}")
print(f"Date:       {trade_date}")
print(f"Provider:   {config['llm_provider']}")
print(f"Model:      {config['deep_think_llm']}")
print(f"Macro:      FRED (enabled)")
print()

ta = TradingAgentsGraph(debug=True, config=config)
print("✓ Graph initialized\n")

print("=" * 70)
print("RUNNING PROPAGATION...")
print("=" * 70)

try:
    final_state, signal = ta.propagate(ticker, trade_date, asset_type="crypto")
    
    print("\n" + "=" * 70)
    print("RESULTS")
    print("=" * 70)
    print(f"\n📊 TRADE DECISION: {signal}")
    
    # Print key reports with more context
    print("\n📋 MARKET REPORT (first 300 chars):")
    print(final_state.get("market_report", "N/A")[:300])
    
    print("\n📰 NEWS REPORT (first 500 chars - should include FRED data):")
    print(final_state.get("news_report", "N/A")[:500])
    
    print("\n💬 SENTIMENT REPORT (first 300 chars):")
    print(final_state.get("sentiment_report", "N/A")[:300])
    
    # Show debate summary
    debate = final_state.get("investment_debate_state", {})
    print("\n⚖️ JUDGE DECISION:")
    print(debate.get("judge_decision", "N/A")[:400])
    
    # Final decision
    print("\n🛡️ FINAL DECISION:")
    print(final_state.get("final_trade_decision", "N/A")[:500])
    
    # Save reports
    report_path = ta.save_reports(final_state, ticker)
    print(f"\n📝 Full reports saved to: {report_path}")
    
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
