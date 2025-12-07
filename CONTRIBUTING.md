# Contributing to Security Stack

Thank you for your interest in contributing to Security Stack! This project aims to bring AI-powered security capabilities to small and medium businesses through open source toolsets.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment. We expect all contributors to:

- Use welcoming and inclusive language
- Respect differing viewpoints and experiences
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other community members

## How to Contribute

### Getting Started

1. **Fork the repository** to your own GitHub account
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/security-stack.git
   cd security-stack
   ```
3. **Add the upstream remote**:
   ```bash
   git remote add upstream https://github.com/smbsec/security-stack.git
   ```
4. **Create a new branch** for your work:
   ```bash
   git checkout -b feature/your-feature-name
   ```

### Development Environment

This project uses Docker Compose to orchestrate multiple services. To set up your development environment:

1. Ensure you have Docker and Docker Compose installed
2. Copy any required environment files (check each service's directory)
3. Run the stack:
   ```bash
   docker-compose up -d
   ```

### Service Components

The stack includes the following services:
- **Elasticsearch** - Search and analytics engine (port 9200)
- **Kibana** - Visualization dashboard (port 5601)
- **Wazuh Manager** - Security monitoring (port 55000)
- **OpenCTI** - Threat intelligence platform (port 8080)
- **LLaMA2** - Large language model service (port 8000)
- **FAISS** - Vector similarity search (port 5000)
- **Stable Baselines** - Reinforcement learning (port 8001)
- **Neo4j** - Graph database (ports 7474, 7687)

### Making Changes

1. **Keep changes focused** - Each pull request should address a single concern
2. **Write clear commit messages** - Use conventional commits format when possible:
   ```
   feat: add new threat detection algorithm
   fix: resolve memory leak in vector search
   docs: update API documentation
   ```
3. **Test your changes** - Ensure all services start correctly and existing functionality works
4. **Update documentation** - If your changes affect how users interact with the project

### Submitting Changes

1. **Push your branch** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
2. **Open a Pull Request** against the `main` branch
3. **Fill out the PR template** with all required information
4. **Respond to feedback** and make requested changes

## Types of Contributions

### Bug Reports

Found a bug? Please check [ISSUES.md](ISSUES.md) for guidelines on submitting bug reports.

### Feature Requests

Have an idea? We'd love to hear it! Please check [ISSUES.md](ISSUES.md) for guidelines on submitting feature requests.

### Documentation

- Fix typos or clarify existing documentation
- Add examples or tutorials
- Improve README files for individual components

### Code Contributions

- Bug fixes
- New features
- Performance improvements
- Test coverage improvements

## Licensing

By contributing to Security Stack, you agree that your contributions will be licensed under the [MIT License](LICENSE).

## Questions?

If you have questions about contributing, feel free to:
- Open a discussion issue
- Review existing issues and pull requests for context

Thank you for helping make Security Stack better! 🛡️
