---
name: debugging
description: Diagnose a reproducible defect systematically without speculative code changes.
---

# Debugging workflow

1. Restate observed behavior, expected behavior, and reproduction steps.
2. Identify the narrowest failing component and gather logs/tests safely.
3. Form competing hypotheses and rank them by evidence.
4. Reproduce with a focused test or minimal case where possible.
5. Trace the failure to root cause; distinguish symptom from cause.
6. Implement the smallest fix and add a regression test.
7. Run relevant tests and inspect the diff.

Never suppress errors, delete tests, expose secrets in logs, or claim certainty without evidence. Report root cause, fix, verification, and residual risk.
