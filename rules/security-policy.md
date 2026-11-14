---
trigger: model_decision
description: Apply when a change touches authentication, authorization, input handling, secrets, crypto, data access or external calls.
---

# Secure engineering policy

- Apply least privilege at every trust boundary.
- Validate and normalize untrusted input at system boundaries.
- Enforce authorization server-side; never rely only on UI checks.
- Use parameterized queries and safe serialization.
- Protect secrets and sensitive data in logs, traces, errors, and analytics.
- Use secure defaults for CORS, cookies, TLS, headers, and session handling.
- Avoid unsafe deserialization, shell interpolation, dynamic code execution, and path traversal.
- Pin or constrain dependencies according to ecosystem practice; monitor known vulnerabilities.
- Add tests for authorization boundaries and abuse cases.
- Do not weaken security controls to make a test pass.
