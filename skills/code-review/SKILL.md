---
name: code-review
description: Independently review a code change for correctness, regressions, security, compatibility, and test gaps.
---

# Code review

1. Read the task, acceptance criteria, repository instructions, and PR diff.
2. Inspect surrounding code and callers for behavioral impact.
3. Check error handling, authorization, data integrity, concurrency, retries, and compatibility.
4. Evaluate whether tests prove the intended behavior and cover important edge cases.
5. Report only actionable findings.

For each finding include:
- Severity: critical / high / medium / low.
- Exact file and line.
- Concrete triggering scenario.
- User or system impact.
- Suggested remediation.
- Confidence and any assumptions.

Do not invent defects, repeat lint output without added context, or claim tests passed unless they ran. If no findings exist, say so and list review scope and unverified areas. Follow `policies/code-review-policy.md`.
