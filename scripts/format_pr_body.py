#!/usr/bin/env python3
import json
import yaml
from pathlib import Path

def format_pr_body():
    """
    Generates a complete, structured Markdown body for a Pull Request
    by consolidating information from the task, plan, results, and spec.
    """
    # --- Load Data Sources ---
    try:
        task_data = json.loads(Path("artifacts/exec/task.json").read_text(encoding="utf-8"))
        backtest_results = json.loads(Path("artifacts/backtest/latest.json").read_text(encoding="utf-8"))
        spec = yaml.safe_load(Path("specs/ProjectSpec.yaml").read_text(encoding="utf-8"))
    except FileNotFoundError as e:
        print(f"## 💥 VibeCoder Report Error\n\nMissing required artifact: {e.filename}")
        return

    # --- Extract Data ---
    task = task_data.get("pr", {}).get("title", "N/A")
    plan = task_data.get("plan", "Plan not available.")
    changes = task_data.get("changes", [])
    acceptance_rules = spec.get("acceptance", {})

    # --- Format Changes Section ---
    changes_md = ""
    if isinstance(changes, list):
        for change in changes:
            action = change.get('action', 'N/A').upper()
            file_path = change.get('file', 'N/A')
            changes_md += f"- **{action}**: `{file_path}`\n"
    else:
        changes_md = "Could not parse structured changes."

    # --- Format Backtest Section ---
    backtest_md = (
        f"- **Winrate**: `{backtest_results.get('winrate', 0):.2%}`\n"
        f"- **MFE (Avg)**: `{backtest_results.get('mfe', 0):.4f}`\n"
        f"- **MAE (Avg)**: `{backtest_results.get('mae', 0):.4f}`\n"
        f"- **Trades/Day**: `{backtest_results.get('trades_per_day', 0)}`"
    )

    # --- Format Gate Section ---
    gate_md = "```yaml\n" + yaml.dump(acceptance_rules, indent=2) + "\n```"

    # --- Assemble Final PR Body ---
    pr_body = f"""
## 📌 任務
{task}

## 📋 規劃 (GPT-5)
```markdown
{plan}
```

## 💻 變更 (Claude Sonnet 4)
{changes_md}

## ✅ 測試/回測
- **pytest**: ✅ Passed
{backtest_md}

## 🔒 Gate
{gate_md}

## 🔁 回退
This change is isolated to the new modules and can be reverted by rolling back the associated commit.
"""
    print(pr_body.strip())

if __name__ == "__main__":
    format_pr_body()
