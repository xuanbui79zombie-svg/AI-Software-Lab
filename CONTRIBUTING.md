# Contributing

Thank you for helping improve AI Software Lab. Contributions should strengthen portfolio governance, reusable project standards, or Codex-assisted delivery without adding a business project to this repository.

## Before You Start

1. Read the [mission](PORTFOLIO_MISSION.md), [architecture](FRAMEWORK_ARCHITECTURE.md), and [development workflow](DEVELOPMENT_WORKFLOW.md).
2. Search existing issues and pull requests before creating a new one.
3. Use the appropriate issue form for a confirmed bug or a proposed improvement.
4. For a large, cross-cutting, or breaking change, agree on the direction in an issue before implementation.
5. Report vulnerabilities privately according to [SECURITY.md](SECURITY.md).

## Change Process

1. Create a short-lived branch from `main`.
2. Make one focused change and update all affected sources of truth.
3. Add or update an ADR for a durable cross-project decision.
4. Run `python scripts/validate_framework.py`.
5. Review the code, documentation, security, compatibility, and changelog impact.
6. Open a pull request using the repository template.
7. Resolve review threads and wait for required checks before merge.

## Documentation Standards

- Write for a reader who does not have private context.
- Use verifiable claims; do not invent users, metrics, demos, or outcomes.
- Keep instructions executable and links relative when they refer to this repository.
- Update the source of truth instead of copying the same policy into several files.
- Explain intent and trade-offs for changes that affect long-term maintenance.

## Commit and Pull Request Standards

- Use an imperative commit subject that describes the outcome.
- Keep commits reviewable and exclude secrets, generated noise, and unrelated changes.
- Describe what changed, why it changed, validation evidence, risks, and documentation impact.
- Prefer squash merge for a focused public history.

## Scope Boundaries

Do not add application source code, customer data, credentials, personal secrets, unverified resume claims, or a speculative project backlog. Future applications must use their own repositories.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
