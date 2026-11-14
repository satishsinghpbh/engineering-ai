---
trigger: model_decision
description: Apply when reviewing a pull request or self-reviewing a change.
---

# Code review policy

Review for correctness before style. Prioritize:
1. behavioral bugs and regressions;
2. security, privacy, and authorization;
3. data integrity and migration safety;
4. concurrency, retries, idempotency, and failure handling;
5. API and backward compatibility;
6. missing or weak tests;
7. performance and resource use;
8. maintainability and clarity.

A finding must include file/line, concrete scenario, impact, and a practical fix. Distinguish confirmed defects from questions or suggestions. Do not report speculative issues as blockers. Avoid repeating findings already caught by deterministic linters or scanners unless context changes severity.
