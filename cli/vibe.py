#!/usr/bin/env python3
import sys
import os
import argparse, json
from dotenv import load_dotenv

load_dotenv()

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from graph.app import build_app

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", default="demo task")
    args = parser.parse_args()

    app = build_app()
    out = app.invoke({"task": args.task}, config={"thread_id": "local"})
    print(json.dumps(out, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
