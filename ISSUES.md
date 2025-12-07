# Issue Guidelines

Thank you for taking the time to report issues and suggest improvements for Security Stack!

## Before Creating an Issue

1. **Search existing issues** to avoid duplicates
2. **Check the documentation** for answers to common questions
3. **Verify you're using the latest version** from the `main` branch

## Issue Types

### 🐛 Bug Reports

For reporting bugs, defects, or unexpected behavior.

#### Required Information

```markdown
**Environment**
- OS: [e.g., Ubuntu 22.04, macOS 14]
- Docker version: [e.g., 24.0.7]
- Docker Compose version: [e.g., 2.23.0]

**Affected Service(s)**
- [ ] Elasticsearch
- [ ] Kibana
- [ ] Wazuh Manager
- [ ] OpenCTI
- [ ] LLaMA2
- [ ] FAISS
- [ ] Stable Baselines
- [ ] Neo4j
- [ ] Docker Compose / General

**Description**
A clear and concise description of the bug.

**Steps to Reproduce**
1. Start the stack with '...'
2. Navigate to '...'
3. Perform action '...'
4. See error

**Expected Behavior**
What you expected to happen.

**Actual Behavior**
What actually happened.

**Logs**
Include relevant log output (use code blocks):
```
docker-compose logs <service-name>
```

**Screenshots**
If applicable, add screenshots to help explain the problem.

**Additional Context**
Any other relevant information.
```

### ✨ Feature Requests

For suggesting new features or enhancements.

#### Required Information

```markdown
**Problem Statement**
Describe the problem this feature would solve.

**Proposed Solution**
A clear description of what you want to happen.

**Alternatives Considered**
Other solutions you've considered and why they're less ideal.

**Affected Component(s)**
Which service(s) would this affect?

**Additional Context**
Any other relevant information, mockups, or examples.
```

### 📖 Documentation Issues

For reporting errors or gaps in documentation.

#### Required Information

```markdown
**Location**
Which file or section contains the issue?

**Current Content**
What does it currently say? (copy/paste or link)

**Suggested Change**
What should it say instead?

**Why**
Why is this change needed?
```

### ❓ Questions / Support

For asking questions about usage or configuration.

#### Required Information

```markdown
**What are you trying to accomplish?**
Describe your goal.

**What have you tried?**
Steps you've already taken.

**Environment**
- OS: 
- Docker version:
- Docker Compose version:

**Relevant Configuration**
Any custom configuration you're using.
```

## Labels

We use labels to categorize and prioritize issues:

| Label | Description |
|-------|-------------|
| `bug` | Something isn't working |
| `enhancement` | New feature or request |
| `documentation` | Documentation improvements |
| `question` | Further information is requested |
| `good first issue` | Good for newcomers |
| `help wanted` | Extra attention is needed |
| `wontfix` | This will not be worked on |
| `duplicate` | This issue already exists |
| `service: elasticsearch` | Related to Elasticsearch |
| `service: kibana` | Related to Kibana |
| `service: wazuh` | Related to Wazuh |
| `service: opencti` | Related to OpenCTI |
| `service: llm` | Related to LLaMA2 |
| `service: faiss` | Related to FAISS |
| `service: ml` | Related to Stable Baselines |
| `service: neo4j` | Related to Neo4j |

## Issue Lifecycle

1. **New**: Issue is created and awaiting triage
2. **Triaged**: Issue has been reviewed and labeled
3. **In Progress**: Someone is actively working on it
4. **Review**: Fix is ready for review
5. **Closed**: Issue is resolved or won't be fixed

## Security Issues

**⚠️ Do NOT create public issues for security vulnerabilities!**

Please review [SECURITY.md](SECURITY.md) for instructions on reporting security issues responsibly.

## Tips for Effective Issues

- **Be specific** - Vague issues are hard to act on
- **Be concise** - Get to the point, but include necessary details
- **One issue per report** - Don't combine multiple issues
- **Use formatting** - Code blocks, lists, and headers improve readability
- **Stay engaged** - Respond to follow-up questions promptly
- **Be respectful** - Remember there are humans on the other side

Thank you for helping improve Security Stack! 🛡️
