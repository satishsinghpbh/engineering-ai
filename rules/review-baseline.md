---
trigger: model_decision
description: Org review baseline mapped to OWASP ASVS 5.0 and NIST SSDF. Apply when reviewing a pull request or self-reviewing a change before opening one.
---

# Review baseline

Cite the control in each finding, e.g. `[blocking][ASVS V8] missing ownership check on /accounts/{id}`.

## Blocking (must fix before merge)
| Check | Control |
|---|---|
| Injection: SQL/NoSQL, command, LDAP, template, XSS; unsafe output encoding | ASVS V1 |
| Missing input validation or business-logic limits (amounts, quantities, state transitions) | ASVS V2 |
| New endpoint or handler without authentication | ASVS V6 |
| Missing authorization or object-ownership check (IDOR) | ASVS V8 |
| Weak or custom crypto, hardcoded keys, non-constant-time secret comparison | ASVS V11 |
| TLS disabled or certificate validation turned off | ASVS V12 |
| Hardcoded secrets or credentials, debug or insecure defaults in prod config | ASVS V13, SSDF PW.9 |
| PII or account data logged, returned or stored unmasked or unencrypted | ASVS V14 |
| Unsafe deserialization, SSRF, path traversal, race conditions on money or state | ASVS V15 |
| Swallowed exceptions, stack traces returned to clients, security events not logged | ASVS V16 |
| New dependency with a known High/Critical CVE, an unpinned version or an incompatible license | SSDF PW.4, RV.1 |
| Changed logic with no new or updated tests | SSDF PW.8 |
| Irreversible migration or breaking API/event/schema change with no rollback or versioning | SSDF PW.1 |
| Changes that weaken CI, branch rules, CODEOWNERS or scanners | SSDF PO.5, PS.1 |

## Non-blocking (comment, don't block)
- Naming, readability, small simplifications.
- Style the linter does not catch.
- Missing or outdated docs.

## AI-authored changes
- Check for invented APIs, packages or config keys; confirm every new import exists in the dependency file.
- Check that tests assert behavior and are not tautological, and that no test was deleted or skipped to make CI pass.
- Flag changes outside the stated scope of the PR.
