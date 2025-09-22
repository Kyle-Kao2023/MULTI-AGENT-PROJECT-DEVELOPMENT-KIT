#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

TRADE_LOG_PATH = Path("artifacts/backtest/trade_log.csv")
CHART_DIR = Path("artifacts/charts")

def generate_charts():
    """Reads the detailed trade log and generates performance charts."""
    if not TRADE_LOG_PATH.exists():
        print(f"Trade log not found at {TRADE_LOG_PATH}. Run backtest first.")
        return

    df = pd.read_csv(TRADE_LOG_PATH)
    CHART_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Cumulative P/L Chart
    df['cumulative_pnl'] = df['pnl_usd'].cumsum()
    plt.figure(figsize=(10, 6))
    plt.plot(df['entry_time'], df['cumulative_pnl'], label='Cumulative P/L', color='blue')
    plt.title('Cumulative Profit/Loss Over Time')
    plt.xlabel('Time')
    plt.ylabel('P/L (USD)')
    plt.grid(True)
    plt.legend()
    pnl_chart_path = CHART_DIR / "pnl_curve.png"
    plt.savefig(pnl_chart_path)
    plt.close()
    print(f"P/L curve chart saved to {pnl_chart_path}")

    # 2. MFE/MAE Distribution Chart
    plt.figure(figsize=(10, 6))
    plt.scatter(df['mae'], df['mfe'], alpha=0.5, c=df['pnl_usd'].apply(lambda x: 'g' if x > 0 else 'r'))
    plt.title('MFE vs. MAE Distribution')
    plt.xlabel('Max Adverse Excursion (MAE)')
    plt.ylabel('Max Favorable Excursion (MFE)')
    plt.grid(True)
    plt.axline((0, 0), slope=1, color='gray', linestyle='--') # Profit/Loss line
    dist_chart_path = CHART_DIR / "mfe_mae_distribution.png"
    plt.savefig(dist_chart_path)
    plt.close()
    print(f"MFE/MAE distribution chart saved to {dist_chart_path}")

if __name__ == "__main__":
    generate_charts()
