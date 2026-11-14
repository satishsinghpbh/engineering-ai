# Engineering AI standards (org-wide)

Applies to every repo. A repo's own `AGENTS.md` / `.github/REVIEW.md` wins where it is more specific.

- Never commit secrets; read them from env vars or the secret manager.
- Every behavior change ships with tests; run the repo's build and test commands before opening a PR.
- Keep PRs small and single-purpose; use Conventional Commit prefixes (`feat:`, `fix:`, `chore:`, `docs:`, `test:`, `refactor:`). Link the ticket or CVE in the PR body.
- AI-authored PRs are never self-approved or merged by Devin; a human CODEOWNER approves (maker-checker).
- Never push to `main`/`master`, disable checks, or weaken branch rules, CODEOWNERS, linters or security scanners.
- Pin dependency versions; check license and maintenance status before adding a dependency.
- Never paste customer data, PII or production credentials into prompts, logs, tests or fixtures; use synthetic data.
- Follow the repo's existing style and linters; do not reformat unrelated code.
- Use the `fix-cve` skill for vulnerabilities and `onboard-repo` to add Devin files to a repo. Apply the `review-baseline` rule when reviewing.
