---
name: onboard-repo
description: Add the org-standard Devin and governance files (AGENTS.md, .github/REVIEW.md, .github/CODEOWNERS, SECURITY.md) to a repository.
---

# Onboard a repo for Devin

1. Read the README, CONTRIBUTING, build files and CI config to find the real setup, build, test, lint and run commands. Do not invent commands; mark unknowns as `TODO`.
2. Create `AGENTS.md` at the repo root from the template below. Keep it under ~60 lines and list only repo-specific facts.
3. Create `.github/REVIEW.md`. Add only rules specific to this repo; the org baseline already covers the generic ones. For paths with stricter rules add a folder-level `REVIEW.md` (e.g. `src/payments/REVIEW.md`).
4. Create `.github/CODEOWNERS` (ask for owners if unknown) and a root `SECURITY.md` if missing.
5. Repo-specific procedures that repeat (release, data backfill, local env) go in `.agents/skills/<name>/SKILL.md`. Do not add other agent-specific folders.
6. Open a PR titled `docs: add Devin AGENTS.md and review/governance files`.

Standard layout:
```
AGENTS.md              # agent rules, < 16 KiB
SECURITY.md
.github/REVIEW.md      # Devin Review rules (repo-wide scope)
.github/CODEOWNERS
.agents/skills/<name>/SKILL.md   # optional
```

## AGENTS.md template
```markdown
# <repo-name>
<One line: what it does.>
Org-wide standards come from the `engineering-ai` Devin plugin; this file adds repo-specific rules.
## Setup
- Runtime: <...>
- Install: `<cmd>`
## Commands
- Build: `<cmd>` / Test: `<cmd>` / Lint: `<cmd>` / Run: `<cmd>`
## Dependencies & CVE fixes
- Dependency file, lockfile update command, audit command
## Repo-specific rules
- <...>
```

## .github/REVIEW.md template
```markdown
# Review rules for <repo-name>
Org baseline applies (secrets, injection, authz, data loss, breaking changes, untested logic, vulnerable deps).
## Blocking
- <repo-specific>
## Non-blocking
- <repo-specific>
## Paths needing extra care
- `<path/>`: <why>
```
