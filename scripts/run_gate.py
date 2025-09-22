#!/usr/bin/env python3
import json
import sys
import yaml
from pathlib import Path

def evaluate_gate():
    """
    Reads backtest results and spec criteria to determine if the gate passes.
    Exits with status code 0 for pass, 1 for fail.
    """
    print("--- VibeCoder Gate Evaluation ---")

    # 1. Load acceptance criteria from spec
    spec_path = Path("specs/ProjectSpec.yaml")
    if not spec_path.exists():
        print(f"❌ Error: Specification file not found at {spec_path}")
        sys.exit(1)
        
    with open(spec_path, "r") as f:
        spec = yaml.safe_load(f)
    criteria = spec.get("acceptance", {}).get("backtest", {})
    print(f"✅ Loaded acceptance criteria from {spec_path}")

    # 2. Load backtest results from artifact
    results_path = Path("artifacts/backtest/latest.json")
    if not results_path.exists():
        print(f"❌ Error: Backtest result artifact not found at {results_path}")
        sys.exit(1)

    with open(results_path, "r") as f:
        results = json.load(f)
    print(f"✅ Loaded backtest results from {results_path}")
    print("\n--- Backtest Results ---")
    print(json.dumps(results, indent=2))
    
    # 3. Compare results against criteria
    passed = True
    report_lines = ["\n--- Gate Report ---"]
    
    # Winrate check
    winrate_crit_str = criteria.get("sample_out_winrate", ">=0.0").replace(">=", "")
    winrate_crit = float(winrate_crit_str)
    if results["winrate"] < winrate_crit:
        passed = False
        report_lines.append(f"❌ Winrate: {results['winrate']:.2%} < required {winrate_crit:.2%}")
    else:
        report_lines.append(f"✅ Winrate: {results['winrate']:.2%} >= required {winrate_crit:.2%}")

    # MFE check
    mfe_crit_str = criteria.get("mfe_target", ">=0.0").replace(">=", "")
    mfe_crit = float(mfe_crit_str)
    if results["mfe"] < mfe_crit:
        passed = False
        report_lines.append(f"❌ MFE: {results['mfe']:.3%} < target {mfe_crit:.3%}")
    else:
        report_lines.append(f"✅ MFE: {results['mfe']:.3%} >= target {mfe_crit:.3%}")

    # MAE check
    mae_crit_str = criteria.get("mae_limit", "<=1.0").replace("<=", "")
    mae_crit = float(mae_crit_str)
    if results["mae"] > mae_crit:
        passed = False
        report_lines.append(f"❌ MAE: {results['mae']:.3%} > limit {mae_crit:.3%}")
    else:
        report_lines.append(f"✅ MAE: {results['mae']:.3%} <= limit {mae_crit:.3%}")

    # Trades per day check
    trades_crit_str = criteria.get("trades_per_day", "<=100").replace("<=", "")
    trades_crit = float(trades_crit_str)
    if results["trades_per_day"] > trades_crit:
        passed = False
        report_lines.append(f"❌ Trades/Day: {results['trades_per_day']} > limit {trades_crit}")
    else:
        report_lines.append(f"✅ Trades/Day: {results['trades_per_day']} <= limit {trades_crit}")

    # Final result
    print("\n".join(report_lines))
    if passed:
        print("\n[RESULT] ✅ Gate PASSED")
        sys.exit(0)
    else:
        print("\n[RESULT] ❌ Gate FAILED")
        sys.exit(1)

if __name__ == "__main__":
    evaluate_gate()
