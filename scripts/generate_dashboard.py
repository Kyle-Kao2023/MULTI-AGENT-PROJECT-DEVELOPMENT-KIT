#!/usr/bin/env python3
import pandas as pd
from pathlib import Path
from datetime import datetime

LOG_FILE = Path("artifacts/logs/observability_log.csv")
DASHBOARD_FILE = Path("DASHBOARD.md")

def generate_dashboard():
    """Reads the observability log and generates a Markdown dashboard."""
    if not LOG_FILE.exists():
        print(f"Log file not found at {LOG_FILE}. Run the main app first.")
        return

    df = pd.read_csv(LOG_FILE)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # --- Calculations ---
    total_cost = df['cost_usd'].sum()
    total_tokens = df['total_tokens'].sum()
    
    # Node-level stats
    node_stats = df.groupby('node_name').agg(
        avg_latency_ms=('latency_ms', 'mean'),
        success_rate=('status', lambda x: (x == 'success').mean()),
        total_cost=('cost_usd', 'sum'),
        total_tokens=('total_tokens', 'sum')
    ).reset_index()

    # Gate stats (PR pass rate)
    gate_df = df[df['node_name'] == 'gate']
    pr_pass_rate = gate_df['status'].eq('success').mean() if not gate_df.empty else 0

    # --- Build Markdown ---
    md = []
    md.append("# VibeCoder Observability Dashboard")
    md.append(f"_{datetime.utcnow().isoformat()}_")

    md.append("\n## 🚀 Overall Performance")
    md.append("| Metric | Value |")
    md.append("|---|---|")
    md.append(f"| **Total Cost (USD)** | `${total_cost:.4f}` |")
    md.append(f"| **Total Tokens** | `{total_tokens:,.0f}` |")
    md.append(f"| **PR Pass Rate (Gate Success)** | `{pr_pass_rate:.2%}` |")

    md.append("\n## 📊 Node-Level Statistics")
    md.append("| Node Name | Avg Latency (ms) | Success Rate | Total Cost (USD) | Total Tokens |")
    md.append("|---|---|---|---|---|")
    for _, row in node_stats.iterrows():
        md.append(f"| `{row['node_name']}` | `{row['avg_latency_ms']:.2f}` | `{row['success_rate']:.2%}` | `${row['total_cost']:.4f}` | `{row['total_tokens']:,.0f}` |")

    md.append("\n## 📜 Recent Runs")
    md.append(df.tail(10).to_markdown(index=False))

    # --- Write to file ---
    with open(DASHBOARD_FILE, 'w', encoding="utf-8") as f:
        f.write("\n".join(md))

    print(f"Dashboard successfully generated at {DASHBOARD_FILE}")

if __name__ == "__main__":
    generate_dashboard()
