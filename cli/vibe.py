#!/usr/bin/env python3
import sys
import os
import argparse
import json
import shutil
from pathlib import Path
from dotenv import load_dotenv
from slugify import slugify

load_dotenv()

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from graph.app import build_app
from scripts.build_knowledge_base import build_knowledge_base

def handle_run(args):
    """Handles the 'run' command."""
    print(f"Starting VibeCoder run with task: '{args.task}'")
    app = build_app()
    
    # --- Dynamic Thread ID ---
    if args.thread:
        thread_id = args.thread
    else:
        # Slugify the task to create a deterministic, filesystem-safe thread_id
        thread_id = slugify(args.task)
    print(f"Using Thread ID: {thread_id}")

    # Set a recursion limit to prevent infinite loops
    config = {"recursion_limit": 3, "thread_id": thread_id}
    out = app.invoke({"task": args.task}, config=config)
    print(json.dumps(out, indent=2, ensure_ascii=False))

def handle_init(args):
    """Handles the 'init' command."""
    template_name = args.template
    template_path = Path("templates") / template_name / "template.yaml"
    
    if not template_path.exists():
        print(f"Error: Template '{template_name}' not found at {template_path}")
        # List available templates
        available = [d.name for d in Path("templates").iterdir() if d.is_dir()]
        print(f"Available templates: {', '.join(available)}")
        return

    target_path = Path("ProjectSpec.yaml")
    if target_path.exists():
        print(f"Warning: '{target_path}' already exists. Overwrite? (y/n)")
        if input().lower() != 'y':
            print("Initialization cancelled.")
            return

    shutil.copy(template_path, target_path)
    print(f"✅ ProjectSpec.yaml initialized from template '{template_name}'.")
    print("Next steps: Fill out your .env file and run 'python cli/vibe.py run --task \"Your first task\"'")

def handle_knowledge(args):
    """Handles the 'knowledge' command."""
    if args.subcommand == 'build':
        build_knowledge_base()
    else:
        print(f"Unknown knowledge command: {args.subcommand}")

def main():
    parser = argparse.ArgumentParser(description="VibeCoder CLI")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # --- Run Command ---
    parser_run = subparsers.add_parser("run", help="Run the VibeCoder agent workflow")
    parser_run.add_argument("--task", default="demo task", help="The task for the AI agents to execute")
    parser_run.add_argument("--thread", help="Specify a custom thread_id for the run. Defaults to a slug of the task.")
    parser_run.set_defaults(func=handle_run)

    # --- Init Command ---
    parser_init = subparsers.add_parser("init", help="Initialize ProjectSpec.yaml from a template")
    parser_init.add_argument("template", help="The name of the template to use (e.g., app_saas)")
    parser_init.set_defaults(func=handle_init)
    
    # --- Knowledge Command ---
    parser_knowledge = subparsers.add_parser("knowledge", help="Manage the knowledge base (Wave 2)")
    knowledge_subparsers = parser_knowledge.add_subparsers(dest="subcommand", required=True)
    parser_kb_build = knowledge_subparsers.add_parser("build", help="Build the vector store from documents")
    parser_kb_build.set_defaults(func=handle_knowledge)


    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
