# Engineering AI

A repository-first engineering standards and agent enablement hub for a GitHub Enterprise organization with 80+ repositories and Devin Enterprise.

This is a **safe starter scaffold**, not an autonomous organization-wide installer. It centralizes engineering policies, reusable agent skills, role guidance, repository metadata, and read-only inventory tooling. Roll it out gradually and require human approval for write actions and merges.

## Design principles

- **Devin remains the primary implementation agent.** This repo supplies shared context and repeatable workflows.
- **Review independently.** The agent that authors a change should not be the only reviewer.
- **Discover before enforcing.** Inventory and classify repositories before applying policy.
- **Opt in by cohort.** Pilot with a few representative repositories, then expand.
- **No broad credentials.** Use least-privilege GitHub App / token access; never store secrets here.
- **Local context wins where appropriate.** Shared standards are a baseline; repository-specific instructions can add detail but should not silently weaken security controls.

## Repository layout

```text
engineering-ai/
├── README.md
├── ORG_ADOPTION_PLAN.md
├── SECURITY.md
├── CONTRIBUTING.md
├── repo-catalog/
│   ├── README.md
│   ├── repositories.yaml
│   └── repository.schema.json
├── policies/
│   ├── engineering-principles.md
│   ├── pull-request-policy.md
│   ├── code-review-policy.md
│   ├── security-policy.md
│   ├── testing-policy.md
│   ├── dependency-policy.md
│   └── documentation-policy.md
├── agents/
│   ├── README.md
│   ├── architect.md
│   ├── implementer.md
│   ├── reviewer.md
│   ├── qa.md
│   ├── security.md
│   └── release-manager.md
├── skills/
│   ├── README.md
│   ├── code-review/SKILL.md
│   ├── debugging/SKILL.md
│   ├── test-strategy/SKILL.md
│   ├── secure-change-review/SKILL.md
│   ├── api-change/SKILL.md
│   ├── database-migration/SKILL.md
│   ├── dependency-upgrade/SKILL.md
│   └── documentation/SKILL.md
├── templates/
│   ├── pull-request-template.md
│   ├── issue-bug.md
│   └── change-plan.md
├── scripts/
│   ├── inventory-repos.sh
│   ├── classify-repos.py
│   └── validate-catalog.py
├── .github/
│   ├── CODEOWNERS
│   └── workflows/validate-catalog.yml
└── config/
    ├── organization.example.yaml
    └── rollout-matrix.yaml
```

## Quick start

### 1. Configure the organization

Copy `config/organization.example.yaml` to `config/organization.yaml` and set your GitHub organization slug and any approved defaults. Do not put tokens or secrets in this file.

### 2. Inventory the organization

Requirements: GitHub CLI (`gh`) authenticated to your enterprise host, `jq`, and Python 3.10+.

```bash
gh auth status
./scripts/inventory-repos.sh YOUR_ORG > /tmp/repos.json
python3 scripts/classify-repos.py /tmp/repos.json > repo-catalog/repositories.yaml
python3 scripts/validate-catalog.py repo-catalog/repositories.yaml
```

The inventory script is read-only. It lists repositories and basic metadata; it does not clone, modify, or configure them.

For GitHub Enterprise Server, set `GH_HOST` or authenticate with the appropriate hostname before running `gh`.

### 3. Curate the catalog

Review `repo-catalog/repositories.yaml`. Auto-classification is only a first pass. Add ownership, criticality, language/framework, deployment tier, data sensitivity, and service relationships with repository owners.

### 4. Pilot Devin

Start with 3–5 repositories representing different stacks and risk levels. Add only the relevant skill files and a short repository-specific `AGENTS.md` or Devin-supported repository instruction file after checking your current Devin workspace configuration. Do not assume every agent product reads the same instruction filename.

### 5. Roll out in cohorts

Follow `ORG_ADOPTION_PLAN.md` and `config/rollout-matrix.yaml`. Begin in advisory mode; move to required checks only after teams validate signal quality and false-positive rates.

## Devin Enterprise integration

Use Devin Enterprise's organization/workspace controls to configure access, repositories, secrets, and approved integrations. The exact controls and supported instruction/skill discovery paths can vary by Devin product version and deployment. Verify against your current Devin admin documentation before configuring organization-wide behavior.

Recommended pattern:
1. Keep this repository as the **source of truth** for shared policies and skill content.
2. Publish/version skills through the mechanism supported by your Devin Enterprise plan.
3. Provide repository-specific context in each repo, linking back to the approved shared standard.
4. Use separate read-only and write-capable identities where possible.
5. Require human approval for PR merge, production deploy, permission changes, and destructive operations.

## Important limitations

- This scaffold does not connect to your GitHub organization or Devin account.
- It does not automatically install files into 80+ repositories.
- The catalog classifier is heuristic and must be reviewed.
- The sample policies are starting defaults. Adapt them to your regulatory, security, architecture, and release requirements.
