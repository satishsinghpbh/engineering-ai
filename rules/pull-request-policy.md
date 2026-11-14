---
trigger: model_decision
description: Apply when opening, updating or describing a pull request.
---

# Pull request policy

Every PR should:
- state the user/business problem;
- describe the implementation and important alternatives;
- identify affected services, APIs, schemas, and dependencies;
- include tests run and their actual results;
- describe migrations, rollout, monitoring, and rollback where relevant;
- link issues and related cross-repository PRs;
- identify security/privacy implications.

Keep PRs focused and reasonably sized. Split unrelated work. Do not claim checks passed unless the checks actually ran and passed. Require human approval according to repository tier and branch rules. Agents must not approve or merge their own changes.
