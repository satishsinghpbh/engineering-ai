---
name: database-migration
description: Plan and validate safe database schema and data migrations.
---

# Database migration workflow

1. Identify database engine, table size, write patterns, constraints, and consumers.
2. Assess locking, downtime, backfill volume, replication, and rollback constraints.
3. Prefer expand-and-contract for zero/low-downtime changes.
4. Make migrations deterministic, observable, and safe to retry where possible.
5. Test against representative data volume and failure/restart scenarios.
6. Define deployment order, backfill monitoring, rollback/forward-fix, and data validation.

Never run destructive migrations or production data operations without explicit human approval and an approved backup/recovery plan.
