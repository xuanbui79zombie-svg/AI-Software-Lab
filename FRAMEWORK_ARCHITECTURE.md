# Portfolio Framework Architecture

## Purpose

AI Software Lab is a governance repository, not a monorepo for business applications. Its architecture separates long-term strategy, project planning, delivery standards, evidence, and reusable execution assets so each concept has one authoritative home.

## Design Principles

- Keep business projects in independent repositories with independent release histories.
- Maintain one source of truth for each decision or status field.
- Prefer version-controlled files over undocumented personal process.
- Automate structural rules that can be checked deterministically.
- Keep human judgment for product value, architecture trade-offs, and resume evidence.
- Record durable decisions without turning temporary discussion into permanent policy.

## Layers

```text
Portfolio strategy
        |
        v
Candidate roadmap ------> Portfolio status and evidence
        |
        v
Development workflow
        |
        +------> Quality and governance controls
        |
        v
Project template + Codex skills
        |
        v
Independent project repositories
```

### 1. Strategy

`PORTFOLIO_MISSION.md` defines the long-term outcome, selection criteria, growth path, project quality bar, and resume standard. It changes rarely.

### 2. Planning

`PROJECT_ROADMAP.md` is the only source of truth for proposed projects and their priority. An idea should not appear in `PORTFOLIO_STATUS.md` until a repository exists and delivery has started.

### 3. Evidence

`PORTFOLIO_STATUS.md` records actual repositories, technology, completion, demos, and resume value. Claims must be backed by repository or demo evidence.

### 4. Delivery

`DEVELOPMENT_WORKFLOW.md` defines the lifecycle from discovery through open-source packaging. Checklists and repository automation implement its quality gates.

### 5. Execution Assets

- `templates/project-template/` supplies the minimum structure for a new repository.
- `.agents/skills/` supplies bounded Codex roles with explicit inputs and outputs.
- `scripts/validate_framework.py` verifies the framework's deterministic invariants.

Project-specific code, credentials, deployment configuration, user data, and business backlogs do not belong in this repository.

## Source-of-Truth Rules

| Information | Authoritative location | Do not duplicate in |
| --- | --- | --- |
| Long-term portfolio criteria | `PORTFOLIO_MISSION.md` | README or individual project rules |
| Candidate priority | `PROJECT_ROADMAP.md` | Portfolio status |
| Delivered evidence | `PORTFOLIO_STATUS.md` | Roadmap descriptions |
| Delivery stages | `DEVELOPMENT_WORKFLOW.md` | Skill files |
| Cross-project defaults | Project template | Individual portfolio records |
| Role-specific Codex procedure | Matching `SKILL.md` | Root workflow |
| Durable architecture decision | `docs/adr/` | Commit message alone |

The README is a navigation and orientation layer. It summarizes but does not replace these sources.

## Change Boundaries

- A mission change requires reviewing the roadmap and portfolio scoring model.
- A workflow change requires reviewing templates, checklists, automation, and affected skills.
- A template change applies to new projects by default; existing projects adopt it through an explicit migration.
- A skill change must preserve its declared role boundary and must not silently change project policy.
- A breaking framework change requires an architecture decision record and a migration note in `CHANGELOG.md`.

## Architecture Decisions

Use [`docs/adr`](docs/adr/) for decisions that affect multiple files, repositories, or future contributors. ADRs are immutable after acceptance except for status and typo corrections; superseding decisions receive a new record.

## Evolution

The framework uses semantic versions for published milestones. Backward-compatible documentation and automation improvements are minor changes; incompatible template or governance requirements are major changes. See [MAINTENANCE.md](MAINTENANCE.md) for review and deprecation policy.
