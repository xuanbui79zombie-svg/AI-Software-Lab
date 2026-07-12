# Maintenance Policy

## Scope and Ownership

The repository owner is the accountable maintainer. Ownership covers framework policy, templates, Codex skills, automation, security response, releases, and the accuracy of portfolio records.

If maintainers are added, each durable area must have an explicit owner. Access is granted with least privilege and reviewed regularly.

## Maintenance Horizon

This framework is designed for at least five years of use. Longevity depends on stable concepts, small reversible changes, automated validation, recorded decisions, and scheduled cleanup rather than on preserving every current tool choice.

## Review Cadence

| Frequency | Required review |
| --- | --- |
| Every change | Scope, links, validation, security impact, and changelog need |
| Monthly | Open issues and pull requests, failed automation, stale guidance, and broken links |
| Quarterly | Repository access, GitHub settings, skill boundaries, template relevance, and security controls |
| Every six months | Roadmap priorities, portfolio evidence, resume relevance, and maintenance cost |
| Annually | Mission fit, framework architecture, supported tooling, succession risk, and five-year viability |

Review dates and material outcomes should be recorded in an issue or an ADR, not only in private notes.

## Versioning and Releases

- Use semantic versions for framework milestones.
- Keep `main` releasable and protect it from force pushes and deletion.
- Prefer squash merges for a clear public history.
- Record user-visible framework changes in `CHANGELOG.md`.
- Create a GitHub Release when a version establishes a reusable or breaking framework baseline.

## Compatibility

Template and skill improvements apply to newly created projects. Existing projects are not silently rewritten. A migration must state affected files, required actions, validation, and rollback.

## Deprecation

A policy, template field, or skill should be deprecated before removal when projects may depend on it. The deprecation notice must include:

- what is deprecated and why;
- the replacement or migration path;
- the earliest removal version or date;
- compatibility and rollback notes.

Security fixes may shorten the notice period, but the reason must be documented.

## Archival and Succession

If the framework is no longer maintained, the README must state the status and date, open work must be closed or transferred, and the repository should be archived only after export and ownership options are reviewed.

At least annually, confirm that the owner can recover the GitHub account, that critical credentials are not held by an unavailable person, and that another maintainer could understand the framework from repository documentation alone.
