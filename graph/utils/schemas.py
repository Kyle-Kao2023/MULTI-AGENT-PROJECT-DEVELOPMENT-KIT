"""
Defines the JSON Schemas used for validation in the VibeCoder project.
"""

TASK_SCHEMA = {
  "type": "object",
  "required": ["repo", "branch", "changes", "commands", "pr"],
  "properties": {
    "repo": {"type": "string", "format": "uri"},
    "branch": {"type": "string", "minLength": 1},
    "plan": {"type": "string"},
    "changes": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["file", "action"],
        "properties": {
          "file": {"type": "string", "minLength": 1},
          "action": {"type": "string", "enum": ["add", "modify", "delete"]},
          "content": {"type": "string"}
        }
      }
    },
    "commands": {
      "type": "array",
      "items": {"type": "string"}
    },
    "pr": {
      "type": "object",
      "required": ["title", "body"],
      "properties": {
          "title": {"type": "string", "minLength": 1},
          "body": {"type": "string"}
      }
    }
  }
}
