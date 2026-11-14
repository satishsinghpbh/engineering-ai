---
trigger: always_on
---

# Engineering principles

1. Prefer the simplest maintainable solution that meets the requirement.
2. Follow the repository's established architecture and conventions unless the task explicitly calls for a migration.
3. Avoid unrelated refactors and opportunistic dependency upgrades.
4. Make changes observable, testable, reversible, and documented.
5. Preserve backward compatibility unless a breaking change is approved and communicated.
6. Treat security, privacy, reliability, and accessibility as design requirements.
7. Prefer explicit errors and safe failure modes over silent fallback.
8. Keep cross-repository changes coordinated through a written change plan.
9. Never invent test results, CI status, deployment status, or review approval.
10. If requirements are ambiguous or the change is high-risk, ask before making irreversible decisions.
