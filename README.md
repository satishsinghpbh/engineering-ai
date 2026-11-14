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

This repository is also a **Devin plugin**: install it once at account (org) scope and every Devin session loads it.

```text
engineering-ai/
├── .devin-plugin/plugin.json    # Devin plugin manifest
├── AGENTS.md                    # always-on org rules (keep short; loads in every session)
├── rules/                       # Devin rules (formerly policies/)
│   ├── engineering-principles.md   # always_on
│   ├── review-baseline.md          # OWASP ASVS 5.0 / NIST SSDF mapped review checklist
│   ├── code-review-policy.md       # model_decision (loaded when relevant)
│   ├── pull-request-policy.md
│   ├── security-policy.md
│   ├── testing-policy.md
│   ├── dependency-policy.md
│   └── documentation-policy.md
├── skills/<name>/SKILL.md       # /engineering-ai:<name> (code-review, fix-cve, onboard-repo, ...)
├── agents/<name>.md             # subagent role cards (Devin CLI/Desktop)
├── templates/                   # PR/issue templates + repo-* files used by onboard-repo
├── repo-catalog/                # repository inventory and schema
├── scripts/                     # read-only inventory tooling
├── config/                      # org config and rollout matrix
├── .github/CODEOWNERS
├── ORG_ADOPTION_PLAN.md, CONTRIBUTING.md, SECURITY.md, CHANGELOG.md
```

Standard layout for each application repository (created by the `onboard-repo` skill):

```text
<repo>/
├── AGENTS.md                    # repo setup, build/test commands, repo rules (< 16 KiB)
├── SECURITY.md
├── .github/REVIEW.md            # Devin Review rules (Devin Review reads the PR's repo, not this plugin)
├── .github/CODEOWNERS           # human approvers (maker-checker)
└── .agents/skills/<name>/SKILL.md   # optional repo-only procedures
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

Start with 3–5 repositories representing different stacks and risk levels. Run `/engineering-ai:onboard-repo` on each pilot repo to add `AGENTS.md`, `.github/REVIEW.md`, `.github/CODEOWNERS` and `SECURITY.md`.

### 5. Roll out in cohorts

Follow `ORG_ADOPTION_PLAN.md` and `config/rollout-matrix.yaml`. Begin in advisory mode; move to required checks only after teams validate signal quality and false-positive rates.

## Devin integration

1. **Install the plugin:** Customize > Plugins in Devin, install from `https://github.com/satishsinghpbh/engineering-ai` at organization scope. On Devin Enterprise, list it in `requiredPlugins` so no org, repo or user can remove it ([plugin governance](https://docs.devin.ai/product-guides/plugins#governance)).
2. **Change standards via PR** to this repo (CODEOWNERS review). After merge, confirm the installed plugin is on the new revision.
3. **Onboard each repo** with `/engineering-ai:onboard-repo`, which adds `AGENTS.md`, `.github/REVIEW.md`, `.github/CODEOWNERS` and `SECURITY.md`.
4. **Use the skills:** `/engineering-ai:fix-cve` for vulnerabilities (also from Devin Code Scans "Fix with Devin"), `/engineering-ai:code-review`, `/engineering-ai:dependency-upgrade`, and so on.
5. **Enforce in GitHub:** rulesets on `main` requiring a PR, CODEOWNER approval and passing checks. Devin never merges its own PRs.

References: [AGENTS.md](https://docs.devin.ai/onboard-devin/agents-md), [Skills](https://docs.devin.ai/product-guides/skills), [Devin Review instruction files](https://docs.devin.ai/work-with-devin/devin-review#agents-md-/-instruction-files), [Plugin layout](https://docs.devin.ai/product-guides/plugin-ecosystem#1-author-your-plugins), [OWASP ASVS](https://asvs.owasp.org/), [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final).

## Important limitations

- This scaffold does not connect to your GitHub organization or Devin account.
- It does not automatically install files into 80+ repositories.
- The catalog classifier is heuristic and must be reviewed.
- The sample rules are starting defaults. Adapt them to your regulatory, security, architecture, and release requirements.
