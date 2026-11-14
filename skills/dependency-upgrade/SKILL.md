---
name: dependency-upgrade
description: Evaluate and implement dependency upgrades with security, compatibility, and reproducibility checks.
---

# Dependency upgrade workflow

1. Identify direct and transitive dependency changes.
2. Review release notes, support status, license, provenance, and known vulnerabilities.
3. Check runtime/toolchain compatibility and breaking changes.
4. Keep the upgrade isolated from unrelated feature work where practical.
5. Run tests, build, static analysis, and relevant security/license scans.
6. Report version changes, rationale, risks, and rollback.

Do not introduce unreviewed packages or silently change lockfile/package manager conventions.
