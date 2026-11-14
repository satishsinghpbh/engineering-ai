# Testing policy

Choose tests proportional to risk:
- unit tests for local logic and edge cases;
- integration tests for persistence, queues, APIs, and service boundaries;
- contract tests for shared APIs and events;
- end-to-end tests for critical user journeys;
- regression tests for every fixed defect where practical.

Tests must be deterministic, isolated, and meaningful. Do not delete or loosen tests merely to obtain a green build. If a test cannot be run, state why and identify the residual risk. Include negative, boundary, and failure-path tests for security- or data-critical changes.
