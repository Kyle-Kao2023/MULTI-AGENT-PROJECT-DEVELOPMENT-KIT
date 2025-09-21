from typing import TypedDict, Optional, Dict, Any

class P1State(TypedDict, total=False):
    task: str
    plan: Optional[str]
    code_diff: Optional[str]
    backtest_report: Optional[Dict[str, Any]]
    pr_url: Optional[str]
    gate_passed: bool
    current_step: str
    error: Optional[str]
