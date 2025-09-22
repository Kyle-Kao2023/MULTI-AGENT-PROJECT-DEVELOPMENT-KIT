from typing import TypedDict, Optional, Dict, Any, NotRequired

class P1State(TypedDict):
    task: str
    plan: NotRequired[str]
    code_diff: NotRequired[str]
    backtest_report: NotRequired[dict]
    pr_url: NotRequired[str]
    gate_passed: NotRequired[bool]
    current_step: NotRequired[str]
    job_id: NotRequired[str]
    correction_suggestion: NotRequired[str]
