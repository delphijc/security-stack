# Security Policy

## Reporting a Vulnerability

The Security Stack team takes security vulnerabilities seriously. We appreciate your efforts to responsibly disclose your findings.

### How to Report

**Please DO NOT report security vulnerabilities through public GitHub issues.**

Instead, please report security vulnerabilities by:

1. **Email**: Send a detailed report to the project maintainers (jayson.cavendish@yahoo.com)
2. **Encrypted Communication**: For sensitive disclosures, request our PGP key for encrypted communication

### What to Include

When reporting a vulnerability, please include:

- **Type of vulnerability** (e.g., SQL injection, XSS, authentication bypass, container escape)
- **Affected component(s)** - Which service(s) are affected:
  - Elasticsearch
  - Kibana
  - Wazuh Manager
  - OpenCTI
  - LLaMA2
  - FAISS
  - Stable Baselines
  - Neo4j
  - Docker Compose configuration
- **Steps to reproduce** - Detailed steps to reproduce the vulnerability
- **Proof of concept** - Code or screenshots demonstrating the vulnerability
- **Potential impact** - Your assessment of the severity and potential impact
- **Suggested fix** - If you have recommendations for remediation

### Response Timeline

- **Initial Response**: Within 48 hours of receiving your report
- **Status Update**: Within 5 business days with our assessment
- **Resolution Timeline**: Depends on severity and complexity

| Severity | Target Resolution |
|----------|-------------------|
| Critical | 24-72 hours |
| High | 1-2 weeks |
| Medium | 2-4 weeks |
| Low | Next release cycle |

### Safe Harbor

We consider security research conducted in accordance with this policy to be:

- Authorized in accordance with any applicable anti-hacking laws
- Exempt from DMCA restrictions on security research
- Conducted in good faith

We will not pursue legal action against researchers who:
- Act in good faith to avoid privacy violations and service disruptions
- Provide us reasonable time to address the issue before public disclosure
- Do not access or modify data belonging to others

## Security Best Practices

When deploying Security Stack, we recommend:

### Infrastructure Security

1. **Network Isolation**: Deploy services in a private network
2. **Firewall Rules**: Restrict port access to necessary endpoints only
3. **TLS/SSL**: Enable encryption for all service communications
4. **Secrets Management**: Use environment variables or secret managers for credentials

### Container Security

1. **Image Updates**: Regularly update base images for security patches
2. **Non-root Users**: Run containers as non-root when possible
3. **Resource Limits**: Set memory and CPU limits for containers
4. **Read-only Filesystems**: Use read-only mounts where feasible

### Access Control

1. **Strong Passwords**: Change all default passwords immediately
   - Neo4j default: `neo4j/neo4jpassword` - **MUST BE CHANGED**
2. **Authentication**: Enable authentication on all services
3. **Least Privilege**: Grant minimum required permissions
4. **Audit Logging**: Enable and monitor access logs

### Data Protection

1. **Encryption at Rest**: Enable encryption for persistent data
2. **Backup Security**: Encrypt and secure backup data
3. **Data Classification**: Identify and protect sensitive data
4. **Retention Policies**: Implement appropriate data retention

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| main    | :white_check_mark: |
| < main  | :x:                |

We only provide security updates for the latest version on the `main` branch. Users are encouraged to stay up to date.

## Third-Party Components

This project integrates several third-party open source components. Security issues in these components should typically be reported to their respective maintainers:

- [Elasticsearch Security](https://www.elastic.co/community/security)
- [Kibana Security](https://www.elastic.co/community/security)
- [Wazuh Security](https://wazuh.com/community/security)
- [Neo4j Security](https://neo4j.com/security/)

However, if you discover a security issue in how we configure or integrate these components, please report it to us.

## Acknowledgments

We thank all security researchers who help keep Security Stack and its users safe. Responsible disclosure of vulnerabilities helps us ensure that security issues are fixed in a timely manner.

Contributors who report valid security vulnerabilities may be acknowledged in our security hall of fame (with their permission).
