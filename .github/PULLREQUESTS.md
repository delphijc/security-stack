# Pull Request Guidelines

This document outlines the process and expectations for submitting pull requests to Security Stack.

## Before You Start

1. **Check for existing work** - Search open PRs to avoid duplicate efforts
2. **Discuss significant changes** - For large features, open an issue first to discuss the approach
3. **Review the contributing guide** - See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup

## Branch Naming

Use descriptive branch names with the following prefixes:

| Prefix | Purpose | Example |
|--------|---------|---------|
| `feature/` | New functionality | `feature/add-threat-alerting` |
| `fix/` | Bug fixes | `fix/elasticsearch-connection-timeout` |
| `docs/` | Documentation changes | `docs/update-api-examples` |
| `refactor/` | Code refactoring | `refactor/simplify-docker-config` |
| `test/` | Test additions/changes | `test/add-wazuh-integration-tests` |
| `chore/` | Maintenance tasks | `chore/update-dependencies` |

## Pull Request Template

When opening a PR, please include:

```markdown
## Description
A clear and concise description of what this PR does.

## Related Issue
Fixes #(issue number) or Relates to #(issue number)

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] Documentation update
- [ ] Configuration change
- [ ] Refactoring (no functional changes)

## Affected Services
- [ ] Elasticsearch
- [ ] Kibana
- [ ] Wazuh Manager
- [ ] OpenCTI
- [ ] LLaMA2
- [ ] FAISS
- [ ] Stable Baselines
- [ ] Neo4j
- [ ] Docker Compose / General
- [ ] Documentation only

## Testing Performed
Describe the tests you ran and their results:
- [ ] Local docker-compose up successful
- [ ] Affected service(s) start correctly
- [ ] Existing functionality unaffected
- [ ] New functionality works as expected
- [ ] Documentation updated (if applicable)

## Checklist
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my code
- [ ] I have commented my code where necessary
- [ ] I have updated the documentation accordingly
- [ ] My changes generate no new warnings
- [ ] I have tested my changes locally

## Screenshots (if applicable)
Add screenshots to help explain your changes.

## Additional Notes
Any other information reviewers should know.
```

## Commit Guidelines

### Commit Message Format

We follow conventional commits for clear, readable history:

```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Formatting, missing semicolons, etc.
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `test`: Adding missing tests
- `chore`: Maintenance tasks

**Scope** (optional): The service or component affected
- `elasticsearch`, `kibana`, `wazuh`, `opencti`, `llama2`, `faiss`, `ml`, `neo4j`, `docker`, `docs`

**Examples:**
```
feat(wazuh): add custom rule for brute force detection
fix(elasticsearch): resolve memory allocation issue
docs: update installation instructions
chore(docker): upgrade base images to latest versions
```

### Commit Best Practices

- Keep commits atomic and focused
- Write meaningful commit messages
- Don't mix unrelated changes
- Squash WIP commits before requesting review

## Code Review Process

### For Authors

1. **Ensure CI passes** - All checks should be green before requesting review
2. **Self-review first** - Review your own changes before submitting
3. **Keep PRs focused** - Smaller PRs are easier to review
4. **Respond promptly** - Address reviewer feedback in a timely manner
5. **Be open to feedback** - Reviewers are trying to help

### For Reviewers

1. **Be constructive** - Focus on the code, not the person
2. **Explain your reasoning** - Help the author understand suggestions
3. **Approve when ready** - Don't block PRs for minor style preferences
4. **Test locally if needed** - For significant changes, pull and test

### Review Checklist

Reviewers should consider:

- [ ] Does the code do what it claims?
- [ ] Is the implementation approach reasonable?
- [ ] Are there any security concerns?
- [ ] Is the code readable and maintainable?
- [ ] Are edge cases handled?
- [ ] Is documentation updated?
- [ ] Do all services still work together?

## Merging

### Requirements for Merge

- At least one approving review from a maintainer
- All CI checks passing
- No unresolved review comments
- Branch is up to date with `main`

### Merge Strategy

We use **squash and merge**, which:
- Keeps `main` history clean
- Combines all PR commits into one
- Uses PR title as commit message

After merging, the feature branch will be deleted automatically.

## After Your PR is Merged

🎉 **Thank you for your contribution!**

- Your changes will be available in the next release
- You may be credited in release notes
- Consider helping review other PRs

## Need Help?

- Review [CONTRIBUTING.md](CONTRIBUTING.md) for development setup
- Check [ISSUES.md](ISSUES.md) to open a question
- Look at previous merged PRs for examples

Happy contributing! 🛡️
