# AI Software Lab

[![Framework quality](https://github.com/xuanbui79zombie-svg/AI-Software-Lab/actions/workflows/framework-quality.yml/badge.svg)](https://github.com/xuanbui79zombie-svg/AI-Software-Lab/actions/workflows/framework-quality.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

AI Software Lab is the operating system for my developer portfolio. It defines how projects are selected, designed, built, reviewed, maintained, and converted into verifiable career evidence.

This repository contains governance and reusable project infrastructure only. Each future business project will live in its own repository.

## Mission

My long-term goal is to become an independent developer capable of delivering commercial-quality software from problem discovery through deployment and iteration.

The full portfolio criteria are defined in [PORTFOLIO_MISSION.md](PORTFOLIO_MISSION.md).

## Framework

| Layer | Source of truth | Purpose |
| --- | --- | --- |
| Strategy | [PORTFOLIO_MISSION.md](PORTFOLIO_MISSION.md) | Long-term direction and portfolio quality bar |
| Planning | [PROJECT_ROADMAP.md](PROJECT_ROADMAP.md) | Candidate projects, priority, technical value, and commercial value |
| Evidence | [PORTFOLIO_STATUS.md](PORTFOLIO_STATUS.md) | Delivered projects, demos, completion, and resume value |
| Delivery | [DEVELOPMENT_WORKFLOW.md](DEVELOPMENT_WORKFLOW.md) | Eight-stage software delivery lifecycle |
| Architecture | [FRAMEWORK_ARCHITECTURE.md](FRAMEWORK_ARCHITECTURE.md) | Boundaries, information flow, and extension rules |
| Quality | [CODE_REVIEW_CHECKLIST.md](CODE_REVIEW_CHECKLIST.md) and [SECURITY_CHECKLIST.md](SECURITY_CHECKLIST.md) | Review and security gates |
| Execution | [`templates/project-template`](templates/project-template/) and [`.agents/skills`](.agents/skills/) | Reusable project and Codex operating assets |

## Operating Model

1. Test every project idea against the mission and selection criteria.
2. Rank accepted candidates in the roadmap; do not start from an unreviewed idea.
3. Create a separate repository from the project template.
4. Use the development workflow and the relevant Codex skills to deliver it.
5. Record only verifiable outcomes, demos, and evidence in the portfolio status.
6. Promote a project to a resume only after it meets the documented quality bar.

## Repository Map

```text
.
|-- .agents/skills/           # Reusable Codex role instructions
|-- .github/                  # Contribution templates and automation
|-- docs/adr/                 # Durable architecture decisions
|-- scripts/                  # Framework validation tools
|-- templates/project-template/
|-- PORTFOLIO_MISSION.md
|-- PROJECT_ROADMAP.md
|-- PORTFOLIO_STATUS.md
|-- DEVELOPMENT_WORKFLOW.md
`-- FRAMEWORK_ARCHITECTURE.md
```

## Quality and Maintenance

Run the repository's structural checks locally before opening a pull request:

```bash
python scripts/validate_framework.py
```

GitHub Actions runs the same validation for every pull request and every change to `main`. Maintenance ownership, review cadence, compatibility, deprecation, and release policy are defined in [MAINTENANCE.md](MAINTENANCE.md).

## Contributing and Support

- Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a change.
- Follow the [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) in all project spaces.
- Use [SUPPORT.md](SUPPORT.md) for help and [SECURITY.md](SECURITY.md) for private vulnerability reports.
- Follow [GITHUB_GUIDE.md](GITHUB_GUIDE.md) when maintaining portfolio repositories.

## Current Status

The portfolio framework is active. The first independently delivered project is [AI Idea Hunter](https://github.com/xuanbui79zombie-svg/AI-Idea-Hunter), with a public [GitHub Pages demo](https://xuanbui79zombie-svg.github.io/AI-Idea-Hunter/) and `v1.0.0` release.

Its current resume value remains evidence-bounded: complete delivery is verified, while external adoption and commercial outcomes are not yet measured.

## License

Licensed under the [MIT License](LICENSE).
