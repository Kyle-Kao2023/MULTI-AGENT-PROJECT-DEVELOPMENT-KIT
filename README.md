# MULTI-AGENT PROJECT DEVELOPMENT KIT

A sophisticated LangGraph + Cursor based multi-agent workflow system for automated project development, with specialized focus on trading systems and application prototyping.

## Overview

This development kit provides an automated workflow pipeline that transforms natural language task descriptions into production-ready code through a series of specialized AI agents. The system integrates planning, development, execution, and quality gates to ensure reliable and secure code delivery.

### Core Features

- **Multi-Agent Architecture**: Coordinated AI agents for planning, development, execution, and quality control
- **Dynamic Model Routing**: Intelligent selection between GPT-5 for planning and Claude Sonnet for development
- **Automated Quality Gates**: Built-in acceptance criteria validation and backtesting
- **Security-First Design**: Comprehensive secret scanning and security controls
- **Cursor IDE Integration**: Seamless handoff to Cursor for automated branch creation and PR generation

## Architecture

The system follows a structured pipeline with multi-agent coordination:

![System Architecture](docs/system-architecture.svg)

```
START → Planner → Dev → Executor → Gate → END
                           ↑              ↓
                           ←─────── (retry loop)
```

### Agent Responsibilities

- **Planner**: Uses GPT-5 to break down tasks into executable specifications
- **Dev**: Uses Claude Sonnet to generate minimal, mergeable code changes
- **Executor**: Hands off to Cursor IDE for branch creation, testing, and PR generation
- **Gate**: Validates results against acceptance criteria with automatic retry loops

## Quick Start

### Prerequisites

- Python 3.9+
- Cursor IDE
- OpenAI API key (for GPT-5)
- Anthropic API key (for Claude)

### Installation

1. Clone the repository
2. Set up the environment:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. Configure environment variables:

```bash
cp .env.example .env
# Edit .env with your API keys
```

### Usage

Execute a development task:

```bash
python cli/vibe.py run --task "your development task description"
```

The system will:
1. Generate a comprehensive plan
2. Create structured code changes
3. Hand off to Cursor for execution
4. Validate results against quality gates
5. Create a pull request with all changes

## Project Structure

```
├── cli/                    # Command line interface
├── graph/                  # LangGraph workflow definitions
│   ├── app.py             # Main workflow logic
│   └── utils/             # State types and schemas
├── executors/             # Cursor integration handlers
├── specs/                 # Project specifications and acceptance criteria
├── artifacts/             # Generated artifacts and execution results
├── .cursorrules          # Cursor IDE configuration
└── requirements.txt       # Python dependencies
```

## Configuration

### Project Specifications

Edit `specs/ProjectSpec.yaml` to configure:

- Project goals and objectives
- Acceptance criteria for quality gates
- Model routing preferences
- Cost optimization policies

### Environment Variables

Key environment variables in `.env`:

```bash
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GIT_REPO=https://github.com/your/repo
```

## Quality Gates

The system enforces quality through automated gates:

- **Trading Systems**: Winrate ≥ 70%, MFE ≥ 1%, MAE ≤ 0.3%, ≤ 6 trades/day
- **Applications**: Test coverage ≥ 95%, Performance benchmarks
- **Security**: Secret scanning, dependency validation, code quality checks

Failed gates trigger automatic retry loops with corrective feedback.

## Security

### Key Management

- **Local Development**: All secrets managed via `.env` file (git-ignored)
- **Production**: Integration with HashiCorp Vault, AWS Secrets Manager, or similar
- **Separation**: Trading API keys isolated from development services

### Automated Security Scans

Every PR includes:
- Secret scanning with `gitleaks`
- License compliance checking
- Sensitive keyword detection
- Code quality validation

## Advanced Features

### Cost Optimization

- **Dynamic Model Selection**: Cheap-first policy with fallback to premium models
- **Usage Tracking**: Comprehensive token and cost monitoring
- **Performance Metrics**: Latency and success rate tracking

### Extensibility

- **Custom Agents**: Add specialized agents for domain-specific tasks
- **Template System**: Project templates for different use cases
- **Knowledge Base**: RAG integration for project-specific context

## Troubleshooting

### Common Issues

1. **API Rate Limits**: Configure retry policies and fallback models
2. **Validation Failures**: Check `artifacts/exec/task.json` for detailed error logs
3. **Cursor Integration**: Ensure `.cursorrules` configuration matches your setup

### Debugging

Enable verbose logging:

```bash
python cli/vibe.py run --task "your task" --thread custom-debug-session
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes following the security guidelines
4. Submit a pull request

All contributions are subject to automated security and quality checks.

## License

This project is licensed under the MIT License. See LICENSE file for details.

## Support

For issues and questions:
- Create an issue in the GitHub repository
- Follow the security guidelines for sensitive reports
- Check existing documentation and troubleshooting guides

---

**Note**: This is a development toolkit designed for experienced developers familiar with AI-driven development workflows. Proper API key management and security practices are essential for safe usage.