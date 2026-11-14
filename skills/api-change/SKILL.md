---
name: api-change
description: Safely design and implement API changes with compatibility and contract validation.
---

# API change workflow

1. Identify consumers, public contracts, schemas, auth scopes, and versioning rules.
2. Determine whether the change is backward compatible.
3. Update API schema/specification and examples.
4. Add contract tests for success, validation, authorization, and error responses.
5. Coordinate client/server rollout for breaking or cross-repository changes.
6. Document deprecation, migration, observability, and rollback.

Do not silently change response shape, status codes, field semantics, or auth behavior.
