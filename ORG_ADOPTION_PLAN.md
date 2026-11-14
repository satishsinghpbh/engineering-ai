# Organization adoption plan

## Phase 0 — Governance and access (before automation)

- Name an engineering platform owner and repository owners.
- Confirm GitHub Enterprise Cloud vs GitHub Enterprise Server and the enterprise hostname.
- Confirm Devin Enterprise workspace boundaries, repository access model, audit/logging capabilities, and supported shared skill distribution.
- Create a dedicated GitHub App or service identity with least-privilege read access for inventory.
- Keep write permissions separate and grant them only to approved automation workflows.
- Define data classification and repositories that must be excluded from external model context.

**Exit criteria:** approved owner, access model, data boundaries, and escalation path.

## Phase 1 — Inventory and baseline

1. Run the read-only inventory script.
2. Validate the generated catalog with repository owners.
3. Identify archived, forked, template, generated, and security-sensitive repositories.
4. Group repositories by stack and criticality.
5. Record cross-repository dependencies and shared libraries.
6. Capture current CI, branch protection/rulesets, CODEOWNERS, test coverage, and release patterns.

**Exit criteria:** 100% of active repositories have an owner, tier, stack, and lifecycle status, or are explicitly marked unknown.

## Phase 2 — Pilot (3–5 repositories)

Choose:
- one common service;
- one frontend or client;
- one shared library;
- one high-criticality service;
- optionally one legacy repository.

Enable skills in advisory mode. Measure:
- PR review turnaround;
- actionable finding rate;
- false-positive rate;
- escaped defects;
- test failures caught before merge;
- agent rework and human override rate.

Do not let an agent approve its own PR or merge its own changes.

## Phase 3 — Standardize

- Adopt PR template and review policy.
- Add relevant skills to Devin's supported shared skill mechanism.
- Add local repository context and ownership.
- Integrate independent static analysis, dependency scanning, secret scanning, and tests.
- Configure review routing by CODEOWNERS and repository criticality.

## Phase 4 — Expand by cohort

Expand to 10–15 repositories per cohort. Each cohort must have:
- named technical owner;
- tested skill set;
- documented exceptions;
- rollback plan;
- baseline metrics.

## Phase 5 — Continuous improvement

Monthly:
- review false positives and missed defects;
- update skills through PRs;
- retire obsolete rules;
- review agent permissions and tool access;
- review repository ownership and catalog drift;
- publish organization-level quality trends.

## Rollback

Disable the affected skill/workflow or return it to advisory mode. Do not delete repository policy files or bypass required security checks as a first response. Record the reason, affected repos, owner, and remediation plan.
