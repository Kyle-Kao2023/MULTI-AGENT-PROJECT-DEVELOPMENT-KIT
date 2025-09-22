import json
from pathlib import Path
from typing import Dict

def handoff_to_cursor_background(payload: Dict):
    """
    Dumps the task payload to a JSON file for the Cursor Background Agent.
    """
    # Ensure the directory exists
    output_path = Path("artifacts/exec/task.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
