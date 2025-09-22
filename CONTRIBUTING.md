# Contributing to Multi-Agent Project Development Kit

Thank you for your interest in contributing to this project. This document provides guidelines and information for contributors.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Git
- Cursor IDE (for full development experience)
- OpenAI API access (GPT-5)
- Anthropic API access (Claude Sonnet)

### Development Setup

1. Fork the repository
2. Clone your fork locally
3. Set up the development environment:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt  # If available
```

4. Copy and configure environment variables:

```bash
cp .env.example .env
# Edit .env with your development API keys
```

## Development Guidelines

### Code Standards

- Follow PEP 8 Python style guidelines
- Use type hints for all function parameters and return values
- Write comprehensive docstrings for all public functions and classes
- Maintain test coverage above 85%

### Security Requirements

#### Mandatory Security Practices

1. **Never commit secrets**: All API keys, tokens, and sensitive data must be stored in `.env` files or environment variables
2. **Validate all inputs**: Implement proper input validation and sanitization
3. **Use least privilege**: Limit permissions and access to minimum required levels
4. **Log securely**: Never log sensitive data in plain text

#### Pre-commit Hooks

The project uses automated security scanning:

- `gitleaks` for secret detection
- `bandit` for security vulnerability scanning
- `safety` for dependency vulnerability checking

### Contribution Workflow

1. **Create an Issue**: Before starting work, create an issue describing the feature or bug
2. **Branch Naming**: Use descriptive branch names following the pattern:
   - `feature/description-of-feature`
   - `bugfix/description-of-bug`
   - `security/description-of-security-fix`

3. **Commit Messages**: Use clear, descriptive commit messages:
   ```
   type(scope): description

   - feat: new feature
   - fix: bug fix
   - security: security improvement
   - docs: documentation changes
   - test: test additions or modifications
   ```

4. **Pull Request Process**:
   - Fill out the PR template completely
   - Ensure all tests pass
   - Include security impact assessment
   - Add reviewer assignments

### Testing

#### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=graph --cov=cli --cov=executors

# Run security tests
bandit -r .
safety check
```

#### Test Requirements

- Unit tests for all new functions
- Integration tests for workflow components
- Security tests for any authentication or authorization code
- Performance tests for critical paths

### Documentation

#### Required Documentation

- Update README.md for user-facing changes
- Add docstrings to all new functions and classes
- Update API documentation for interface changes
- Include security considerations for new features

#### Documentation Standards

- Use clear, concise language
- Include code examples where appropriate
- Document security implications
- Maintain up-to-date installation and setup instructions

## Agent Development

### Adding New Agents

When contributing new agents to the workflow:

1. **Define Purpose**: Clearly document the agent's role and responsibilities
2. **Input/Output Contracts**: Specify expected input and output formats
3. **Error Handling**: Implement comprehensive error handling and recovery
4. **Testing**: Include both unit and integration tests
5. **Security**: Ensure proper input validation and output sanitization

### Agent Guidelines

- Keep agents focused on single responsibilities
- Implement proper logging and observability
- Use structured data formats (JSON/YAML)
- Handle timeouts and retries gracefully
- Provide clear error messages and debugging information

## Security Guidelines

### Vulnerability Reporting

For security vulnerabilities:

1. **Do not** create public issues for security vulnerabilities
2. Email security concerns to the maintainers privately
3. Include detailed reproduction steps
4. Allow reasonable time for response and fixing

### Security Review Process

All contributions undergo security review:

1. Automated security scanning (pre-commit hooks)
2. Manual security review for security-sensitive changes
3. Penetration testing for major features
4. Security documentation review

## Release Process

### Version Management

- Use semantic versioning (MAJOR.MINOR.PATCH)
- Tag releases with version numbers
- Maintain CHANGELOG.md with release notes

### Release Checklist

- [ ] All tests pass
- [ ] Security scans pass
- [ ] Documentation updated
- [ ] Version bumped
- [ ] Release notes prepared
- [ ] Backward compatibility verified

## Community Guidelines

### Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help newcomers learn and contribute
- Maintain professional communication

### Getting Help

- Check existing documentation first
- Search existing issues and discussions
- Create detailed issue reports with reproduction steps
- Join community discussions and help others

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

## Questions?

If you have questions about contributing, please:

1. Check this guide and existing documentation
2. Search existing issues and discussions
3. Create a new issue with the "question" label
4. Contact the maintainers directly for sensitive matters

Thank you for contributing to the Multi-Agent Project Development Kit!