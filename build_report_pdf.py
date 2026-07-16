#!/usr/bin/env python3
"""Generate a clean PDF report from TradingAgents BTC-USD analysis."""

import os
import re
import json
from pathlib import Path
from datetime import datetime, timedelta

import yfinance as yf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
from matplotlib.patches import FancyBboxPatch
from fpdf import FPDF

def sanitize(text):
    """Replace Unicode chars that latin-1 can't handle."""
    replacements = {
        '\u2014': '-',  # em dash
        '\u2013': '-',  # en dash
        '\u2018': "'",  # left single quote
        '\u2019': "'",  # right single quote
        '\u201c': '"',  # left double quote
        '\u201d': '"',  # right double quote
        '\u2022': '*',  # bullet
        '\u2026': '...', # ellipsis
        '\u00a0': ' ',  # non-breaking space
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

# Config
OUTPUT_DIR = Path.home() / "TradingAgents-output"
REPORT_DIR = OUTPUT_DIR / "reports"
CHART_DIR = OUTPUT_DIR / "charts"
CHART_DIR.mkdir(parents=True, exist_ok=True)

TICKER = "BTC-USD"
TRADE_DATE = "2026-07-14"
ANALYSIS_DATE = "2026-07-15"

# ============================================================
# 1. FETCH MARKET DATA FOR CHARTS
# ============================================================
print("Fetching BTC-USD data...")
btc = yf.Ticker(TICKER)
hist = btc.history(period="6mo")
hist.index = hist.index.tz_localize(None)

# Window around the analysis date
chart_data = hist.loc[:TRADE_DATE].tail(90)
close = chart_data['Close']
high = chart_data['High']
low = chart_data['Low']
volume = chart_data['Volume']

# Technical indicators
def ema(data, period):
    return data.ewm(span=period, adjust=False).mean()

def sma(data, period):
    return data.rolling(window=period).mean()

chart_data['EMA_10'] = ema(close, 10)
chart_data['SMA_50'] = sma(close, 50)
chart_data['SMA_200'] = sma(close, 200)

# MACD
chart_data['MACD'] = ema(close, 12) - ema(close, 26)
chart_data['MACD_signal'] = ema(chart_data['MACD'], 9)
chart_data['MACD_hist'] = chart_data['MACD'] - chart_data['MACD_signal']

# RSI
delta = close.diff()
gain = delta.where(delta > 0, 0).rolling(14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
rs = gain / loss
chart_data['RSI'] = 100 - (100 / (1 + rs))

# Bollinger Bands
chart_data['BB_mid'] = sma(close, 20)
bb_std = close.rolling(20).std()
chart_data['BB_upper'] = chart_data['BB_mid'] + 2 * bb_std
chart_data['BB_lower'] = chart_data['BB_mid'] - 2 * bb_std

# ATR
tr = np.maximum(
    high - low,
    np.maximum(
        abs(high - close.shift()),
        abs(low - close.shift())
    )
)
chart_data['ATR'] = tr.rolling(14).mean()

dates = chart_data.index

# ============================================================
# 2. GENERATE CHARTS (dark theme)
# ============================================================
plt.style.use('dark_background')
BG = '#1a1a2e'
GRID = '#2a2a4e'
TEXT_C = '#e0e0e0'
GREEN = '#00c853'
RED = '#ff1744'
YELLOW = '#ffd600'
ORANGE = '#ff9100'

def style_ax(ax, title=''):
    ax.set_facecolor(BG)
    ax.grid(True, color=GRID, alpha=0.5, linewidth=0.5)
    ax.tick_params(colors=TEXT_C, labelsize=8)
    ax.spines['bottom'].set_color(GRID)
    ax.spines['top'].set_color(GRID)
    ax.spines['left'].set_color(GRID)
    ax.spines['right'].set_color(GRID)
    ax.set_title(title, color=TEXT_C, fontsize=11, fontweight='bold', pad=8)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=30, ha='right', fontsize=7)

print("Generating charts...")

# --- Chart 1: Price + Moving Averages ---
fig, ax = plt.subplots(figsize=(10, 4.5))
fig.patch.set_facecolor(BG)
style_ax(ax, 'BTC-USD Price with Moving Averages')

ax.fill_between(dates, close, alpha=0.08, color=GREEN)
ax.plot(dates, close, color='#64ffda', linewidth=1.5, label='Close')
ax.plot(dates, chart_data['EMA_10'], color=YELLOW, linewidth=1, alpha=0.9, label='10 EMA')
ax.plot(dates, chart_data['SMA_50'], color=ORANGE, linewidth=1, alpha=0.9, label='50 SMA')
ax.plot(dates, chart_data['SMA_200'], color=RED, linewidth=1.5, alpha=0.9, label='200 SMA')
ax.axvline(x=pd.Timestamp(TRADE_DATE), color='#ffffff', linestyle='--', alpha=0.3, linewidth=0.8)

ax.legend(loc='upper left', facecolor=BG, edgecolor=GRID, labelcolor=TEXT_C, fontsize=7)
ax.set_ylabel('Price (USD)', color=TEXT_C, fontsize=8)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))
plt.tight_layout()
fig.savefig(CHART_DIR / 'price_mas.png', dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()

# --- Chart 2: MACD ---
fig, ax = plt.subplots(figsize=(10, 3))
fig.patch.set_facecolor(BG)
style_ax(ax, 'MACD (12, 26, 9)')

ax.plot(dates, chart_data['MACD'], color='#64ffda', linewidth=1.2, label='MACD')
ax.plot(dates, chart_data['MACD_signal'], color=ORANGE, linewidth=1.2, label='Signal')
colors = [GREEN if v >= 0 else RED for v in chart_data['MACD_hist']]
ax.bar(dates, chart_data['MACD_hist'], color=colors, alpha=0.6, width=1.5, label='Histogram')
ax.axhline(y=0, color=GRID, linewidth=0.8)
ax.axvline(x=pd.Timestamp(TRADE_DATE), color='#ffffff', linestyle='--', alpha=0.3, linewidth=0.8)
ax.legend(loc='upper left', facecolor=BG, edgecolor=GRID, labelcolor=TEXT_C, fontsize=7)
plt.tight_layout()
fig.savefig(CHART_DIR / 'macd.png', dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()

# --- Chart 3: RSI ---
fig, ax = plt.subplots(figsize=(10, 2.5))
fig.patch.set_facecolor(BG)
style_ax(ax, 'RSI (14)')

ax.plot(dates, chart_data['RSI'], color='#64ffda', linewidth=1.5)
ax.axhline(y=70, color=RED, linestyle='--', alpha=0.5, linewidth=0.8)
ax.axhline(y=30, color=GREEN, linestyle='--', alpha=0.5, linewidth=0.8)
ax.axhline(y=50, color=GRID, linestyle='-', alpha=0.3, linewidth=0.5)
ax.axvline(x=pd.Timestamp(TRADE_DATE), color='#ffffff', linestyle='--', alpha=0.3, linewidth=0.8)
ax.fill_between(dates, 70, 30, alpha=0.05, color='#ffffff')
ax.set_ylim(0, 100)
ax.set_ylabel('RSI', color=TEXT_C, fontsize=8)
plt.tight_layout()
fig.savefig(CHART_DIR / 'rsi.png', dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()

# --- Chart 4: Bollinger Bands ---
fig, ax = plt.subplots(figsize=(10, 3))
fig.patch.set_facecolor(BG)
style_ax(ax, 'Bollinger Bands (20, 2σ)')

ax.fill_between(dates, chart_data['BB_upper'], chart_data['BB_lower'], alpha=0.1, color='#64ffda')
ax.plot(dates, chart_data['BB_upper'], color=GRID, linewidth=0.8, alpha=0.7)
ax.plot(dates, chart_data['BB_mid'], color=YELLOW, linewidth=1, alpha=0.7, label='20 SMA')
ax.plot(dates, chart_data['BB_lower'], color=GRID, linewidth=0.8, alpha=0.7)
ax.plot(dates, close, color='#64ffda', linewidth=1.5, label='Close')
ax.axvline(x=pd.Timestamp(TRADE_DATE), color='#ffffff', linestyle='--', alpha=0.3, linewidth=0.8)
ax.legend(loc='upper left', facecolor=BG, edgecolor=GRID, labelcolor=TEXT_C, fontsize=7)
ax.set_ylabel('Price (USD)', color=TEXT_C, fontsize=8)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))
plt.tight_layout()
fig.savefig(CHART_DIR / 'bollinger.png', dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()

# --- Chart 5: Volume ---
fig, ax = plt.subplots(figsize=(10, 2))
fig.patch.set_facecolor(BG)
style_ax(ax, 'Trading Volume')

vol_colors = [GREEN if close.iloc[i] >= close.iloc[i-1] else RED for i in range(1, len(close))]
vol_colors.insert(0, GREEN)
ax.bar(dates, volume, color=vol_colors, alpha=0.5, width=1.5)
ax.axvline(x=pd.Timestamp(TRADE_DATE), color='#ffffff', linestyle='--', alpha=0.3, linewidth=0.8)
ax.set_ylabel('Volume', color=TEXT_C, fontsize=8)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}B'))
plt.tight_layout()
fig.savefig(CHART_DIR / 'volume.png', dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()

print("Charts saved.")

# ============================================================
# 3. READ REPORT TEXT
# ============================================================

report_path = REPORT_DIR / "complete_report.md"
report_text = report_path.read_text(encoding='utf-8')

# Extract sections
def extract_section(text, header):
    """Extract content under a markdown heading."""
    pattern = rf"## .*?{re.escape(header)}.*?\n(.*?)(?=\n## |\Z)"
    m = re.search(pattern, text, re.DOTALL)
    return m.group(1).strip() if m else ""

def extract_verdict(text):
    """Extract final trading decision section."""
    m = re.search(r"## Final Trading Decision.*?\n(.*?)$", text, re.DOTALL)
    return m.group(1).strip() if m else ""

# Extract key stats from market report
market_section = extract_section(report_text, "Market Analyst")
reports_section = extract_section(report_text, "Analyst Team Reports")

# Find specific stats
def extract_stat(text, label):
    pattern = re.escape(label) + r"\s*\*\*(.*?)\*\*"
    m = re.search(pattern, text)
    return m.group(1) if m else "N/A"

close_price = extract_stat(report_text, r"\$64,956")
print(f"Close price found: {close_price}")

# ============================================================
# 4. BUILD PDF
# ============================================================
print("Building PDF...")

class ReportPDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font('Helvetica', 'I', 7)
            self.set_text_color(120, 120, 120)
            self.cell(0, 5, sanitize(f'TradingAgents Analysis - BTC-USD | {ANALYSIS_DATE}'), align='C')
            self.ln(8)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 7)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

    def section_title(self, title):
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(0, 150, 100)
        self.cell(0, 10, sanitize(title))
        self.ln(3)
        # underline
        self.set_draw_color(0, 150, 100)
        self.set_line_width(0.5)
        y = self.get_y()
        self.line(self.l_margin, y, self.w - self.r_margin, y)
        self.ln(6)

    def sub_title(self, title):
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(0, 180, 130)
        self.cell(0, 8, sanitize(title))
        self.ln(6)

    def body_text(self, text):
        self.set_font('Helvetica', '', 9)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 4.5, sanitize(text))
        self.ln(2)

    def key_val(self, key, val):
        self.set_font('Helvetica', 'B', 9)
        self.set_text_color(60, 60, 60)
        self.cell(55, 5, sanitize(key))
        self.set_font('Helvetica', '', 9)
        self.set_text_color(40, 40, 40)
        self.cell(0, 5, sanitize(val))
        self.ln(5)

    def add_chart(self, path, w=175):
        if path.exists():
            self.image(str(path), x=self.l_margin + (self.w - self.l_margin - self.r_margin - w) / 2, w=w)
            self.ln(3)

    def verdict_box(self, verdict_text):
        """A nicely styled box for the final verdict."""
        self.set_fill_color(230, 248, 230)
        self.set_draw_color(0, 150, 100)
        y_before = self.get_y()
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(0, 100, 50)
        
        # Approximate height
        self.set_font('Helvetica', '', 8.5)
        self.set_text_color(40, 40, 40)
        
        x = self.l_margin
        w = self.w - self.l_margin - self.r_margin
        clean = sanitize(verdict_text)
        lines = self.multi_cell(w, 4, clean, dry_run=True, output="LINES")
        h = len(lines) * 4 + 10
        
        # Draw box
        y = y_before
        self.rect(x, y, w, h, style='DF')
        
        # Title in box
        self.set_xy(x + 3, y + 2)
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(0, 100, 50)
        self.cell(w - 6, 6, sanitize('Portfolio Manager - Final Decision'))
        self.ln(8)
        
        # Text in box
        self.set_x(x + 3)
        self.set_font('Helvetica', '', 8.5)
        self.set_text_color(40, 40, 40)
        self.multi_cell(w - 6, 4, sanitize(verdict_text))
        
        self.ln(5)


pdf = ReportPDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=20)

# ---- COVER PAGE ----
pdf.add_page()
pdf.ln(40)

# Title block
pdf.set_font('Helvetica', 'B', 28)
pdf.set_text_color(0, 120, 80)
pdf.cell(0, 15, 'BTC-USD', align='C')
pdf.ln(14)

pdf.set_font('Helvetica', '', 14)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 8, sanitize('Multi-Agent Trading Analysis Report'), align='C')
pdf.ln(10)

# Divider
pdf.set_draw_color(0, 150, 100)
pdf.set_line_width(0.5)
pdf.line(60, pdf.get_y(), pdf.w - 60, pdf.get_y())
pdf.ln(8)

# Key details
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(100, 100, 100)
details = [
    ('Ticker:', 'BTC-USD (Bitcoin)'),
    ('Analysis Date:', 'July 14, 2026'),
    ('Report Generated:', f'{ANALYSIS_DATE}'),
    ('Close Price:', '$64,956.11'),
    ('Framework:', 'TradingAgents v0.3.1 (Multi-Agent LLM)'),
    ('LLM Provider:', 'DeepSeek V4 Flash'),
    ('Data Sources:', 'Yahoo Finance, FRED, Polymarket, Reddit'),
    ('Macro Data:', 'Fed 3.63%, CPI -0.42%, 10Y 4.58%'),
]
for k, v in details:
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(60, 60, 60)
    pdf.cell(45, 7, sanitize(k), align='R')
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 7, sanitize(v))
    pdf.ln(7)

pdf.ln(15)

# Architecture diagram
pdf.set_font('Helvetica', 'I', 9)
pdf.set_text_color(120, 120, 120)
pdf.cell(0, 5, sanitize('Generated by TradingAgents - Multi-Agent LLM Financial Trading Framework'), align='C')
pdf.ln(5)
pdf.cell(0, 5, 'github.com/TauricResearch/TradingAgents', align='C')

# ---- PAGE 2: EXECUTIVE SUMMARY + KEY METRICS ----
pdf.add_page()
pdf.section_title('Executive Summary')

exec_summary = sanitize("""Bitcoin (BTC-USD) closed at $64,956.11 on July 14, 2026, at a critical inflection point
after a 13-month decline from $126K+ to a June low near $58K. Multiple technical indicators are
flashing early-stage bullish reversal signals (MACD crossover, RSI recovery from 15 to 56), while
the macro landscape remains mixed: the Fed holds at 3.63% with 82% probability of no cuts in 2026,
but CPI disinflation (-0.42% MoM) and stable unemployment (4.2%) create a nuanced backdrop. The
portfolio manager rated the asset a Hold -- maintaining positions without adding or reducing exposure.""")

pdf.body_text(exec_summary)
pdf.ln(3)

pdf.sub_title('Key Market Metrics')
metrics = [
    ('Close Price:', '$64,956.11', '52-Week High:', '$126,198.07'),
    ('52-Week Low:', '$57,747.77', 'Market Cap:', '~$1.296 Trillion'),
    ('10 EMA:', '$63,332.57', '200 SMA:', '$73,628.77'),
    ('RSI (14):', '56.20', 'MACD Histogram:', '+468.06 (rising)'),
    ('Fed Funds:', '3.63%', '10Y Treasury:', '4.58%'),
    ('CPI MoM:', '-0.42% (disinflation)', 'Unemployment:', '4.2%'),
    ('Polymarket:', '82% no rate cuts', 'Recession Prob:', '10%'),
]
for r1, r2, r3, r4 in metrics:
    pdf.set_font('Helvetica', 'B', 8.5)
    pdf.set_text_color(60, 60, 60)
    pdf.cell(28, 5, sanitize(r1))
    pdf.set_font('Helvetica', '', 8.5)
    pdf.set_text_color(40, 40, 40)
    pdf.cell(42, 5, sanitize(r2))
    pdf.set_font('Helvetica', 'B', 8.5)
    pdf.set_text_color(60, 60, 60)
    pdf.cell(28, 5, sanitize(r3))
    pdf.set_font('Helvetica', '', 8.5)
    pdf.set_text_color(40, 40, 40)
    pdf.cell(0, 5, sanitize(r4))
    pdf.ln(5.5)

pdf.ln(2)

# ---- PRICE CHART ----
pdf.add_chart(CHART_DIR / 'price_mas.png')

# ---- TECHNICAL CHARTS ----
pdf.add_page()
pdf.section_title('Technical Analysis')
pdf.add_chart(CHART_DIR / 'macd.png')
pdf.ln(2)
pdf.add_chart(CHART_DIR / 'rsi.png')
pdf.ln(2)
pdf.add_chart(CHART_DIR / 'bollinger.png')
pdf.ln(2)
pdf.add_chart(CHART_DIR / 'volume.png')

# ---- AGENT REPORTS SUMMARY ----
pdf.add_page()
pdf.section_title('Analyst Team Reports')

pdf.sub_title('Market Analyst')
market_body = """The 50 SMA ($64,335) is still declining but July 14 marks the first close above it since 
mid-May — a significant medium-term development. The 200 SMA ($73,629) acts as formidable overhead 
resistance. The MACD line has crossed above the signal line from deeply negative levels, a textbook 
bullish reversal with a positive and expanding histogram. The RSI recovered from an extreme oversold 
15.40 to 56.20, confirming the momentum shift with plenty of room before overbought (70). Bollinger 
Bands are contracting after the June expansion — a squeeze that often precedes an explosive move."""
pdf.body_text(market_body)

pdf.sub_title('Sentiment Analyst')
sentiment_body = """Overall Sentiment: Mildly Bullish (Score: 5.8/10) - Low Confidence. No Yahoo Finance articles found for BTC-USD in the past 7 days. Two Reddit r/wallstreetbets posts expressed leveraged long convictions through IBIT call options (Dec 2028 expiry) and a pseudo-quantitative 70% probability estimate for continued upside. However, the data deficiency is severe: no news, no StockTwits (HTTPError), and no engagement metrics. This signal should be treated as very low-convidence, narrow-scope retail speculation."""
pdf.body_text(sentiment_body)

pdf.sub_title('News Analyst - With FRED Macro Data')
news_body = sanitize("""Macro data from FRED (free API key now configured) provided rich context. The Fed Funds Rate sits at 3.63% (unchanged), with prediction markets pricing 82% probability of NO rate cuts in 2026. The 10-Year Treasury Yield closed at 4.58%, trending up from 4.48% a week earlier. CPI showed a disinflationary -0.42% month-over-month decline, while Core PCE (130.082) remained flat. Unemployment fell to 4.2% and Real GDP held at $24,180.4B (Q1 2026). The macro environment remains a headwind for liquidity-sensitive assets like Bitcoin.""")
pdf.body_text(news_body)

pdf.sub_title('Fundamentals Analyst')
fund_body = """BTC-USD is a decentralized cryptocurrency — not a corporation — so traditional metrics 
like balance sheets and income statements do not apply. Market cap of ~$1.296T confirms deep liquidity. 
Supply-side analysis shows Bitcoin is ~2+ years post-halving (April 2024), a phase that historically 
can show weakness before the next parabolic advance. The 52-week low ($57,748) held as support and 
is above all prior cycle all-time highs, suggesting a potential long-term accumulation zone."""
pdf.body_text(fund_body)

# ---- DEBATE SECTION ----
pdf.add_page()
pdf.section_title('Research Debate: Bull vs Bear')

pdf.sub_title('Bull Case')
bull_text = """The bull case is built on velocity of change: a genuine momentum shift with MACD bullish 
crossover from extreme oversold, RSI recovering to 56 from 15.40, and the 22pp collapse in the $55K 
dip probability on Polymarket. The quiet sentiment and absence of new negative catalysts support the 
view that the selling climax has passed. The recovery from the June sell-off has been orderly, with 
steady (not explosive) volume — healthy for trend continuation. Key support at the 52-week low 
($57,748) held firmly, and all prior cycle ATHs remain below current price levels."""
pdf.body_text(bull_text)

pdf.sub_title('Bear Case')
bear_text = """The bear case sees this rally as a trap, not a trend. The 200-day SMA at $73,629 (12.6% 
above current price) is declining and has capped every recovery attempt since May. Bounce volume 
($29.8B) is less than half the panic-low volume ($71.5B), signaling distribution rather than 
accumulation. Macro conditions are actively hostile — real yields at 1.8%, M2 contracting, and 
82% probability of zero Fed cuts make a poor environment for crypto. The death cross configuration 
(50 SMA below 200 SMA) is a classic long-term bearish signal that has historically preceded further 
weakness."""
pdf.body_text(bear_text)

pdf.sub_title('Judge Ruling')
judge_text = sanitize("""Recommendation: Hold. This debate was genuinely balanced, with neither side delivering a 
knockout punch. The bull's strongest points are the RSI recovery from 15.4 to 56.2, the MACD crossover 
with a +468 histogram, the disinflationary CPI (-0.42% MoM) from FRED data, and the Mayer Multiple at 
0.87 (historically an accumulation zone). The bear counters with the volume divergence ($30B bounce vs 
$71B capitulation), the 200 SMA gravity well at $73,629, and the macro headwind of 82% no-cut 
probability. The judge held that the evidence supports maintaining current positions without adding 
new exposure. Neither selling into the bounce nor aggressive buying is warranted.""")
pdf.body_text(judge_text)

# ---- FINAL VERDICT ----
pdf.add_page()
pdf.section_title('Final Decision & Execution Plan')

verdict_text = sanitize("""Rating: Hold
Action: Maintain existing positions at current size. No new exposure. No selling into the bounce.

The debate confirms a genuinely balanced risk profile. The aggressive analyst highlighted real technical improvement: RSI recovery from 15.4 to 56.2, MACD crossover with a +468 histogram, a Mayer Multiple at 0.87 (historically an accumulation zone), and the collapse in dip-to-$55K probability from 69% to 48%.

The conservative analyst correctly countered with the volume divergence ($30B bounce against $71B capitulation), the declining 200 SMA at $73,629 (11.8% above price), and the macro headwind of 82% probability of zero Fed cuts with the 10-year yield at 4.58%.

The neutral analyst synthesized both sides: the technical improvement is genuine but incomplete; the macro backdrop is mixed with disinflationary CPI (-0.42% MoM) but no cuts expected.

Execution Plan:
1. Maintain current BTC-USD spot allocation at current size
2. If price reclaims 200 SMA ($73,629) on >$50B daily volume, reconsider Overweight
3. If price loses 50 SMA support (~$64,335) on increasing volume, reduce exposure by 25-30%
4. Monitor the 10-year yield: a sustained move below 4.30% weakens the bear's macro case
5. No new options or leveraged positions at current levels""")

pdf.verdict_box(verdict_text)

pdf.ln(5)
pdf.sub_title('Decision Log (Memory System)')
mem_text = """This decision has been logged to the TradingAgents memory system (~/.tradingagents/memory/trading_memory.md) 
with status "pending". On the next BTC-USD analysis run, the system will:
1. Fetch the realised return (raw return and alpha vs benchmark)
2. Generate a one-paragraph reflection on what worked and what didn't
3. Inject the reflection into the next Portfolio Manager's prompt
This creates a continuous learning loop across analysis sessions."""
pdf.body_text(mem_text)

# ---- APPENDIX ----
pdf.add_page()
pdf.section_title('Agent Architecture')
arch_text = """This report was generated by TradingAgents, a multi-agent framework that mirrors the 
collaborative dynamics of real-world trading firms.

The pipeline consists of:

1. Analyst Team — Fundamental Analyst, Sentiment Analyst, News Analyst, Market (Technical) Analyst, 
   and Social Media Analyst. Each gathers data and produces a specialised report.

2. Researcher Team — Bull and Bear researchers critically assess the analyst reports through structured 
   debate rounds, challenging each other's assumptions and evidence.

3. Debate Judge — Evaluates both sides and produces a recommendation.

4. Risk Management Team — Aggressive, Conservative, and Neutral analysts assess portfolio risk 
   (market volatility, liquidity, exposure).

5. Portfolio Manager — Reviews all inputs and approves/rejects the final transaction proposal.

6. Memory System — Every decision is logged with its outcome. On subsequent runs, the system 
   reflects on past performance and injects lessons learned into the Portfolio Manager's context.

Framework: TradingAgents v0.3.1 | LLM: DeepSeek V4 Flash | Data: YFinance + Polymarket
arXiv: 2412.20138 | github.com/TauricResearch/TradingAgents"""
pdf.body_text(arch_text)

# ---- DISCLAIMER ----
pdf.ln(10)
pdf.set_draw_color(200, 50, 50)
pdf.set_line_width(0.3)
y = pdf.get_y()
pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
pdf.ln(4)
pdf.set_font('Helvetica', 'I', 7)
pdf.set_text_color(180, 80, 80)
disclaimer = """DISCLAIMER: This report is generated by an AI-driven research framework for educational and research 
purposes only. It is not financial, investment, or trading advice. Trading performance may vary based on 
the chosen language models, model temperature, trading periods, data quality, and other non-deterministic 
factors. Past performance does not guarantee future results."""
pdf.multi_cell(0, 3.5, disclaimer)

# Save
pdf_path = OUTPUT_DIR / "BTC-USD_TradingAgents_Report.pdf"
pdf.output(str(pdf_path))
print(f"\n✅ PDF saved to: {pdf_path}")
print(f"   Size: {pdf_path.stat().st_size / 1024:.1f} KB")
