---
name: test-strategy
description: Create a risk-based test plan and implement focused automated tests for a change.
---

# Test strategy

1. Extract acceptance criteria and affected behavior.
2. Identify unit, integration, contract, end-to-end, and regression test layers.
3. Cover normal, boundary, invalid, unauthorized, timeout, retry, and failure cases as relevant.
4. Reuse project fixtures and conventions; avoid brittle timing and shared mutable state.
5. Run focused tests first, then broader suites.
6. Report actual commands, results, skips, environment constraints, and gaps.

Never weaken assertions or remove tests solely to pass CI.
