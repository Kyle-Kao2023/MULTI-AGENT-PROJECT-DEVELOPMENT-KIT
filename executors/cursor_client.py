def create_job(payload: dict) -> str:
    return "job-123"

def poll_job(job_id: str) -> dict:
    return {"status": "completed"}

def open_pr(branch: str, title: str, body: str) -> str:
    return "https://example.com/pr/123"
