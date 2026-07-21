#!/usr/bin/env python3
"""Generate a clean PDF report from TradingAgents analysis for any ticker."""
import os, re, sys
from pathlib import Path
from datetime import datetime

import yfinance as yf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
from fpdf import FPDF

TICKER = sys.argv[1].upper() if len(sys.argv) > 1 else "META"
TRADE_DATE = "2026-07-16"
ANALYSIS_DATE = datetime.now().strftime("%Y-%m-%d")
TICKER_LOWER = TICKER.lower().replace("-", "")

OUTPUT_DIR = Path.home() / "TradingAgents-output"
OUTPUT_TICKER_DIR = OUTPUT_DIR / TICKER_LOWER
CHART_DIR = OUTPUT_TICKER_DIR / "charts"
CHART_DIR.mkdir(parents=True, exist_ok=True)

# ---- HELPER: sanitize text for latin-1 PDF ----
def sanitize(text):
    """Replace/filter Unicode chars that latin-1 can't handle."""
    if not text:
        return ""
    replacements = {
        '\u2014': '-', '\u2013': '-', '\u2018': "'", '\u2019': "'",
        '\u201c': '"', '\u201d': '"', '\u2022': '*', '\u2026': '...',
        '\u00a0': ' ', '\u2010': '-',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    # Strip any remaining non-latin-1 characters (emojis, etc.)
    return text.encode('latin-1', errors='replace').decode('latin-1')
    return text.encode('latin-1', errors='replace').decode('latin-1')

def ema(data, period):
    return data.ewm(span=period, adjust=False).mean()

def sma(data, period):
    return data.rolling(window=period).mean()

# ---- FETCH DATA ----
print(f"Fetching {TICKER} data...")
yft = yf.Ticker(TICKER)
hist = yft.history(period="6mo")
hist.index = hist.index.tz_localize(None)

chart_data = hist.loc[:TRADE_DATE].tail(90)
close = chart_data['Close']
high = chart_data['High']
low = chart_data['Low']
volume = chart_data['Volume']

# Technical indicators
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

# Bollinger
chart_data['BB_mid'] = sma(close, 20)
bb_std = close.rolling(20).std()
chart_data['BB_upper'] = chart_data['BB_mid'] + 2 * bb_std
chart_data['BB_lower'] = chart_data['BB_mid'] - 2 * bb_std

# ATR
tr = np.maximum(high - low, np.maximum(abs(high - close.shift()), abs(low - close.shift())))
chart_data['ATR'] = tr.rolling(14).mean()
dates = chart_data.index

last_price = close.iloc[-1]
last_close_str = f"${last_price:,.2f}" if last_price < 1000 else f"${last_price:,.2f}"

# ---- CHARTS (dark theme) ----
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

# Chart 1: Price + MAs
fig, ax = plt.subplots(figsize=(10, 4.5))
fig.patch.set_facecolor(BG)
style_ax(ax, f'{TICKER} Price with Moving Averages')
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

# Chart 2: MACD
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

# Chart 3: RSI
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

# Chart 4: Bollinger
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

# Chart 5: Volume
fig, ax = plt.subplots(figsize=(10, 2))
fig.patch.set_facecolor(BG)
style_ax(ax, 'Trading Volume')
vol_colors = [GREEN if close.iloc[i] >= close.iloc[i-1] else RED for i in range(1, len(close))]
vol_colors.insert(0, GREEN)
ax.bar(dates, volume, color=vol_colors, alpha=0.5, width=1.5)
ax.axvline(x=pd.Timestamp(TRADE_DATE), color='#ffffff', linestyle='--', alpha=0.3, linewidth=0.8)
ax.set_ylabel('Volume', color=TEXT_C, fontsize=8)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:,.0f}'))
plt.tight_layout()
fig.savefig(CHART_DIR / 'volume.png', dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()

# Chart 6: ATR
fig, ax = plt.subplots(figsize=(10, 2))
fig.patch.set_facecolor(BG)
style_ax(ax, 'ATR (14) — Volatility')
ax.plot(dates, chart_data['ATR'], color='#ff9100', linewidth=1.5)
ax.axvline(x=pd.Timestamp(TRADE_DATE), color='#ffffff', linestyle='--', alpha=0.3, linewidth=0.8)
ax.fill_between(dates, chart_data['ATR'], alpha=0.1, color='#ff9100')
ax.set_ylabel('ATR', color=TEXT_C, fontsize=8)
plt.tight_layout()
fig.savefig(CHART_DIR / 'atr.png', dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()

print("Charts saved.")

# ---- FIND LATEST REPORT ----
reports_base = Path.home() / ".tradingagents" / "logs" / "reports"
all_reports = sorted(reports_base.glob(f"{TICKER}_*"), key=lambda p: p.stat().st_mtime, reverse=True)
report_dir = all_reports[0] if all_reports else None

# ---- READ REPORT TEXT ----
if report_dir:
    report_path = report_dir / "complete_report.md"
    if report_path.exists():
        report_text = report_path.read_text(encoding='utf-8')
    else:
        report_text = ""
else:
    report_text = ""

def extract_section(text, header):
    pattern = rf"## .*?{re.escape(header)}.*?\n(.*?)(?=\n## |\Z)"
    m = re.search(pattern, text, re.DOTALL)
    return m.group(1).strip() if m else ""

def extract_verdict(text):
    m = re.search(r"## Final Trading Decision.*?\n(.*?)$", text, re.DOTALL)
    return m.group(1).strip() if m else ""

# Extract individual agent report sections
market_section = extract_section(report_text, "Market Analyst")
sentiment_section = extract_section(report_text, "Sentiment Analyst")
news_section = extract_section(report_text, "News Analyst")
fund_section = extract_section(report_text, "Fundamentals Analyst")
bull_section = extract_section(report_text, "Bull")
bear_section = extract_section(report_text, "Bear")
manager_section = extract_section(report_text, "Research Manager")
trader_section = extract_section(report_text, "Trader")
pm_section = extract_section(report_text, "Portfolio Manager")
verdict = extract_verdict(report_text)

# Extract signal
signal_match = re.search(r"SIGNAL:\s*(\S+)", report_text) if report_text else None
signal = signal_match.group(1) if signal_match else "N/A"

# ---- PDF CLASS ----
class ReportPDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font('Helvetica', 'I', 7)
            self.set_text_color(120, 120, 120)
            self.cell(0, 5, sanitize(f'TradingAgents Analysis - {TICKER} | {ANALYSIS_DATE}'), align='C')
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
        self.set_fill_color(230, 248, 230)
        self.set_draw_color(0, 150, 100)
        y_before = self.get_y()
        x = self.l_margin
        w = self.w - self.l_margin - self.r_margin
        clean = sanitize(verdict_text)
        lines = self.multi_cell(w, 4, clean, dry_run=True, output="LINES")
        h = len(lines) * 4 + 10
        y = y_before
        self.rect(x, y, w, h, style='DF')
        self.set_xy(x + 3, y + 2)
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(0, 100, 50)
        self.cell(w - 6, 6, sanitize('Portfolio Manager - Final Decision'))
        self.ln(8)
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
pdf.set_font('Helvetica', 'B', 28)
pdf.set_text_color(0, 120, 80)
pdf.cell(0, 15, TICKER, align='C')
pdf.ln(14)
pdf.set_font('Helvetica', '', 14)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 8, 'Multi-Agent Trading Analysis Report', align='C')
pdf.ln(10)
pdf.set_draw_color(0, 150, 100)
pdf.set_line_width(0.5)
pdf.line(60, pdf.get_y(), pdf.w - 60, pdf.get_y())
pdf.ln(8)

# Try to get company info
try:
    info = yft.info
    company_name = info.get('longName', info.get('shortName', TICKER))
    mkt_cap = info.get('marketCap', 0)
    sector = info.get('sector', 'N/A')
    industry = info.get('industry', 'N/A')
except:
    company_name = TICKER
    mkt_cap = 0
    sector = 'N/A'
    industry = 'N/A'

mkt_cap_str = f"${mkt_cap:,.0f}" if mkt_cap else "N/A"
details = [
    ('Ticker:', f'{TICKER} ({company_name})'),
    ('Analysis Date:', ANALYSIS_DATE),
    ('Close Price:', last_close_str),
    ('Sector:', f'{sector} / {industry}'),
    ('Market Cap:', mkt_cap_str),
    ('Framework:', 'TradingAgents v0.3.1 (Multi-Agent LLM)'),
    ('LLM Provider:', 'DeepSeek V4 Flash'),
    ('Data Sources:', 'Yahoo Finance, FRED, Polymarket'),
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
pdf.set_font('Helvetica', 'I', 9)
pdf.set_text_color(120, 120, 120)
pdf.cell(0, 5, 'Generated by TradingAgents - Multi-Agent LLM Financial Trading Framework', align='C')
pdf.ln(5)
pdf.cell(0, 5, 'github.com/TauricResearch/TradingAgents', align='C')

# ---- PAGE 2: EXEC SUMMARY + KEY METRICS ----
pdf.add_page()
pdf.section_title('Executive Summary')
exec_text = report_text[:2000] if report_text else f"{TICKER} closed at {last_close_str}. See full analysis in agent reports."
pdf.body_text(sanitize(exec_text[:1500]))
pdf.ln(3)

pdf.sub_title('Key Technical Metrics')
last_row = chart_data.iloc[-1] if len(chart_data) > 0 else {}
rsi_val = f"{last_row.get('RSI', 0):.1f}" if 'RSI' in last_row else "N/A"
macd_val = f"{last_row.get('MACD_hist', 0):.2f}" if 'MACD_hist' in last_row else "N/A"
ema10_val = f"${last_row.get('EMA_10', 0):.2f}" if 'EMA_10' in last_row else "N/A"
sma50_val = f"${last_row.get('SMA_50', 0):.2f}" if 'SMA_50' in last_row else "N/A"
sma200_val = f"${last_row.get('SMA_200', 0):.2f}" if 'SMA_200' in last_row else "N/A"
atr_val = f"{last_row.get('ATR', 0):.2f}" if 'ATR' in last_row else "N/A"

try:
    high_52w = yft.info.get('fiftyTwoWeekHigh', 'N/A')
    low_52w = yft.info.get('fiftyTwoWeekLow', 'N/A')
    high_52w = f"${high_52w:,.2f}" if isinstance(high_52w, (int, float)) else str(high_52w)
    low_52w = f"${low_52w:,.2f}" if isinstance(low_52w, (int, float)) else str(low_52w)
    beta = yft.info.get('beta', 'N/A')
    beta = f"{beta:.2f}" if isinstance(beta, (int, float)) else str(beta)
except:
    high_52w = low_52w = beta = "N/A"

metrics = [
    ('Close:', last_close_str, '52W High:', high_52w),
    ('10 EMA:', ema10_val, '52W Low:', low_52w),
    ('50 SMA:', sma50_val, 'Beta:', beta),
    ('200 SMA:', sma200_val, 'RSI (14):', rsi_val),
    ('MACD Hist:', macd_val, 'ATR (14):', atr_val),
]
for r1, r2, r3, r4 in metrics:
    pdf.set_font('Helvetica', 'B', 8.5)
    pdf.set_text_color(60, 60, 60)
    pdf.cell(22, 5, sanitize(r1))
    pdf.set_font('Helvetica', '', 8.5)
    pdf.set_text_color(40, 40, 40)
    pdf.cell(48, 5, sanitize(r2))
    pdf.set_font('Helvetica', 'B', 8.5)
    pdf.set_text_color(60, 60, 60)
    pdf.cell(22, 5, sanitize(r3))
    pdf.set_font('Helvetica', '', 8.5)
    pdf.set_text_color(40, 40, 40)
    pdf.cell(0, 5, sanitize(r4))
    pdf.ln(5.5)

pdf.ln(2)
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
pdf.ln(2)
pdf.add_chart(CHART_DIR / 'atr.png')

# ---- AGENT REPORTS ----
pdf.add_page()
pdf.section_title('Analyst Team Reports')

if market_section:
    pdf.sub_title('Market Analyst')
    pdf.body_text(market_section[:1200])

if sentiment_section:
    pdf.sub_title('Sentiment Analyst')
    pdf.body_text(sentiment_section[:1200])

if news_section:
    pdf.sub_title('News Analyst (FRED Macro)')
    pdf.body_text(news_section[:1200])

if fund_section:
    pdf.sub_title('Fundamentals Analyst')
    pdf.body_text(fund_section[:1200])

# ---- RESEARCH DEBATE ----
pdf.add_page()
pdf.section_title('Research Debate: Bull vs Bear')

if bull_section:
    pdf.sub_title('Bull Case')
    pdf.body_text(bull_section[:1200])

if bear_section:
    pdf.sub_title('Bear Case')
    pdf.body_text(bear_section[:1200])

if manager_section:
    pdf.sub_title('Research Manager Decision')
    pdf.body_text(manager_section[:1200])

if trader_section:
    pdf.sub_title('Trader Execution Plan')
    pdf.body_text(trader_section[:800])

# ---- VERDICT ----
pdf.add_page()
pdf.section_title('Final Verdict')

if verdict:
    pdf.verdict_box(verdict)
elif pm_section:
    pdf.verdict_box(pm_section)
else:
    pdf.body_text(f"Signal: {signal}. See complete report markdown for full analysis.")

pdf.ln(5)
pdf.set_font('Helvetica', 'I', 8)
pdf.set_text_color(120, 120, 120)
pdf.cell(0, 5, sanitize(f'Analysis generated on {ANALYSIS_DATE} by TradingAgents v0.3.1 (DeepSeek V4 Flash)'), align='C')
pdf.ln(4)
pdf.cell(0, 5, 'Not financial advice. For educational/research purposes only.', align='C')

# ---- SAVE PDF ----
pdf_path = OUTPUT_TICKER_DIR / f"{TICKER}_TradingAgents_Report_{ANALYSIS_DATE}.pdf"
OUTPUT_TICKER_DIR.mkdir(parents=True, exist_ok=True)
pdf.output(str(pdf_path))
print(f"\nPDF saved to: {pdf_path}")
print(f"---PDF_OUTPUT---\nTICKER={TICKER}\nPDF_PATH={pdf_path}\n---END_PDF_OUTPUT---")
