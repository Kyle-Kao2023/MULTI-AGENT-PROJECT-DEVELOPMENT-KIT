import csv
import os
from datetime import datetime
from pathlib import Path
from typing import Optional

LOG_FILE = Path("artifacts/logs/observability_log.csv")
BUDGET_FILE = Path("artifacts/logs/budget_tracker.json")

# Placeholder costs per 1 million tokens (input/output)
MODEL_COSTS = {
    "gpt-5": (10.0, 30.0),
    "claude-4-sonnet": (3.0, 15.0),
    "claude-3-haiku": (0.25, 1.25),
}

def ensure_log_file():
    """Ensures the log file and its directory exist with a header."""
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not LOG_FILE.exists():
        with open(LOG_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp", "node_name", "status", "latency_ms",
                "input_tokens", "output_tokens", "total_tokens", "cost_usd", "is_fallback"
            ])

def log_metric(
    node_name: str,
    status: str,
    latency_ms: float,
    input_tokens: int = 0,
    output_tokens: int = 0,
    cost_usd: float = 0.0,
    is_fallback: bool = False
):
    """Logs a metric entry to the CSV file."""
    ensure_log_file()
    with open(LOG_FILE, 'a', newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.utcnow().isoformat(),
            node_name,
            status,
            round(latency_ms, 2),
            input_tokens,
            output_tokens,
            input_tokens + output_tokens,
            round(cost_usd, 6),
            is_fallback
        ])

def calculate_cost(model_name: str, input_tokens: int, output_tokens: int) -> float:
    """Calculates the cost of an LLM call based on predefined rates."""
    input_cost_per_mil, output_cost_per_mil = MODEL_COSTS.get(model_name, (0.0, 0.0))
    cost = ((input_tokens / 1_000_000) * input_cost_per_mil) + \
           ((output_tokens / 1_000_000) * output_cost_per_mil)
    return cost
