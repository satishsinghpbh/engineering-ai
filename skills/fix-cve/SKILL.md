---
name: fix-cve
description: Remediate a CVE or dependency/code security finding in any repo and open a tested PR.
---

# Fix a CVE / security finding

Inputs: CVE or advisory ID (or a Devin Code Scan finding), affected repo, severity.

1. **Read the repo's `AGENTS.md`** for build, test and dependency commands. If it is missing, detect them from the build files (`pom.xml`, `build.gradle`, `package.json`, `requirements*.txt`/`pyproject.toml`, `go.mod`, `composer.json`).
2. **Confirm exposure.** Find where the vulnerable package or code is used, including transitive dependencies (`mvn dependency:tree`, `npm ls <pkg>`, `pip show`/`pipdeptree`, `go mod why`). If the repo is not affected, stop and report why.
3. **Pick the smallest safe fix**, in this order of preference:
   1. Bump to the lowest patched version in the same major version.
   2. Override the transitive version (Maven `<dependencyManagement>`, npm `overrides`, pip constraints).
   3. Code change (input validation, safe API) when no patched version exists.
   Do not do unrelated upgrades in the same PR.
4. **Update lockfiles** with the repo's own tool; never hand-edit them.
5. **Verify.** Build and run the full test suite. Add a regression test when the fix is a code change. Re-run the scanner or audit (`mvn org.owasp:dependency-check-maven:check`, `npm audit`, `pip-audit`, `govulncheck`) if available.
6. **Open a PR** titled `fix(security): <CVE-ID> <package> <old> -> <new>`. The body covers: advisory link, severity, affected path, fix chosen and why, test evidence, and any residual risk or follow-up.
7. **Breaking changes:** if the only fix needs a major upgrade or API changes, open the PR as a draft and list what breaks.
