---
trigger: model_decision
description: Apply when adding, upgrading or removing a dependency.
---

# Dependency policy

- Add a dependency only when standard library or existing dependencies are insufficient.
- Check maintenance status, license, security history, transitive dependencies, and package provenance.
- Avoid unpinned floating versions in production deployment paths where reproducibility matters.
- Separate dependency upgrades from feature changes when practical.
- Run relevant tests and vulnerability/license checks.
- Document material runtime, size, licensing, or operational impact.
