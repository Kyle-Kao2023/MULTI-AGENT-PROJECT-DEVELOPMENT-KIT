#!/usr/bin/env python3
import argparse
import json
import random
import pandas as pd
from pathlib import Path

def run_backtest(pair: str, tf: str, out_path: str):
    """
    A minimal, simulated backtesting script.
    It generates a randomized summary report and a detailed trade log.
    """
    print(f"Running simulated backtest for {pair} on {tf} timeframe...")
    
    # --- Generate Detailed Trade Log ---
    num_trades = random.randint(80, 120)
    pnl = [(random.random() * 0.02 - 0.007) for _ in range(num_trades)]
    trade_data = {
        'entry_time': pd.to_datetime(pd.date_range(start='2024-01-01', periods=num_trades, freq='4H')),
        'pnl_usd': [p * 1000 for p in pnl],
        'mfe': [max(0, p + random.random() * 0.005) for p in pnl],
        'mae': [max(0, -p + random.random() * 0.005) for p in pnl],
    }
    trade_log = pd.DataFrame(trade_data)
    
    # --- Calculate Summary Metrics from Trade Log ---
    winrate = (trade_log['pnl_usd'] > 0).mean()
    mfe_mean = trade_log['mfe'].mean()
    mae_mean = trade_log['mae'].mean()
    trades_per_day = num_trades / (trade_log['entry_time'].max() - trade_log['entry_time'].min()).days

    result = {
        "winrate": round(winrate, 4),
        "mfe": round(mfe_mean, 4),
        "mae": round(mae_mean, 4),
        "trades_per_day": round(trades_per_day, 2),
        "notes": "Simulated run. This version now generates a detailed trade log."
    }
    
    # --- Save Artifacts ---
    output_path = Path(out_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Save summary JSON
    with open(output_path, 'w', encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print(f"Backtest summary saved to {output_path}")
    print(json.dumps(result, indent=2))

    # Save detailed trade log CSV
    trade_log_path = output_path.parent / "trade_log.csv"
    trade_log.to_csv(trade_log_path, index=False, encoding="utf-8")
    print(f"Detailed trade log saved to {trade_log_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pair", default="ETHUSDT", help="Trading pair")
    parser.add_argument("--tf", default="15m", help="Timeframe")
    parser.add_argument("--out", default="artifacts/backtest/latest.json", help="Output summary JSON path")
    args = parser.parse_args()

    run_backtest(args.pair, args.tf, args.out)
