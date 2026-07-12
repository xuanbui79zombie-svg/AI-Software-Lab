#!/usr/bin/env python3
"""Validate deterministic invariants of the AI Software Lab framework."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]

ROOT_FILES = {
    ".editorconfig",
    ".gitattributes",
    ".gitignore",
    "CHANGELOG.md",
    "CODE_OF_CONDUCT.md",
    "CODE_REVIEW_CHECKLIST.md",
    "CONTRIBUTING.md",
    "DEVELOPMENT_WORKFLOW.md",
    "FRAMEWORK_ARCHITECTURE.md",
    "GITHUB_GUIDE.md",
    "LICENSE",
    "MAINTENANCE.md",
    "PORTFOLIO_MISSION.md",
    "PORTFOLIO_STATUS.md",
    "PROJECT_ROADMAP.md",
    "README.md",
    "SECURITY.md",
    "SECURITY_CHECKLIST.md",
    "SUPPORT.md",
}

TEMPLATE_FILES = {
    ".editorconfig",
    ".gitattributes",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".gitignore",
    "AGENTS.md",
    "CHANGELOG.md",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "PROJECT_RULES.md",
    "README.md",
    "SECURITY.md",
    "SUPPORT.md",
    "TASKS.md",
    "TECH_STACK.md",
    "docs/API.md",
    "docs/ARCHITECTURE.md",
    "docs/DATABASE.md",
    "docs/PRODUCT.md",
    "docs/adr/0000-template.md",
    "docs/adr/README.md",
    "src/.gitkeep",
    "tests/.gitkeep",
}

SKILLS = {
    "ai-engineer",
    "career-reviewer",
    "code-reviewer",
    "database-engineer",
    "full-stack-engineer",
    "open-source-maintainer",
    "portfolio-manager",
    "product-manager",
    "qa-engineer",
    "software-architect",
}

SKILL_SECTIONS = {
    "角色定位",
    "负责范围",
    "工作流程",
    "输入要求",
    "输出格式",
    "禁止行为",
}

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FRONTMATTER_KEY = re.compile(r"^([A-Za-z0-9_-]+)\s*:", re.MULTILINE)


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def check_required_files(errors: list[str]) -> None:
    for name in sorted(ROOT_FILES):
        if not (ROOT / name).is_file():
            errors.append(f"missing root file: {name}")

    template = ROOT / "templates" / "project-template"
    for name in sorted(TEMPLATE_FILES):
        if not (template / name).is_file():
            errors.append(f"missing project template file: {name}")

    required_github_files = {
        ".github/CODEOWNERS",
        ".github/ISSUE_TEMPLATE/bug_report.yml",
        ".github/ISSUE_TEMPLATE/config.yml",
        ".github/ISSUE_TEMPLATE/feature_request.yml",
        ".github/PULL_REQUEST_TEMPLATE.md",
        ".github/dependabot.yml",
        ".github/workflows/framework-quality.yml",
    }
    for name in sorted(required_github_files):
        if not (ROOT / name).is_file():
            errors.append(f"missing GitHub governance file: {name}")


def check_skills(errors: list[str]) -> None:
    skills_root = ROOT / ".agents" / "skills"
    actual = {path.name for path in skills_root.iterdir() if path.is_dir()}
    missing = SKILLS - actual
    unexpected = actual - SKILLS

    for name in sorted(missing):
        errors.append(f"missing Codex skill: {name}")
    for name in sorted(unexpected):
        errors.append(f"unexpected Codex skill directory: {name}")

    for name in sorted(SKILLS & actual):
        skill_dir = skills_root / name
        skill_file = skill_dir / "SKILL.md"
        agent_file = skill_dir / "agents" / "openai.yaml"
        if not skill_file.is_file():
            errors.append(f"missing SKILL.md: {name}")
            continue
        if not agent_file.is_file():
            errors.append(f"missing agents/openai.yaml: {name}")

        text = skill_file.read_text(encoding="utf-8")
        lines = text.splitlines()
        if not lines or lines[0] != "---":
            errors.append(f"{relative(skill_file)}: missing opening frontmatter delimiter")
            continue
        try:
            closing = lines.index("---", 1)
        except ValueError:
            errors.append(f"{relative(skill_file)}: missing closing frontmatter delimiter")
            continue

        frontmatter = "\n".join(lines[1:closing])
        keys = set(FRONTMATTER_KEY.findall(frontmatter))
        if keys != {"name", "description"}:
            errors.append(
                f"{relative(skill_file)}: frontmatter keys must be name and description; got {sorted(keys)}"
            )
        if f"name: {name}" not in frontmatter:
            errors.append(f"{relative(skill_file)}: name must match directory")
        if not re.search(r"^description:\s*\S", frontmatter, re.MULTILINE):
            errors.append(f"{relative(skill_file)}: description must not be empty")

        for section in sorted(SKILL_SECTIONS):
            if f"## {section}" not in text:
                errors.append(f"{relative(skill_file)}: missing section '{section}'")


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts
    )


def normalize_link(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if " " in target and not target.startswith(("http://", "https://")):
        target = target.split(" ", 1)[0]
    return unquote(target)


def check_markdown(errors: list[str]) -> None:
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        if text and not text.endswith("\n"):
            errors.append(f"{relative(path)}: file must end with a newline")

        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in MARKDOWN_LINK.finditer(line):
                target = normalize_link(match.group(1))
                if not target or target.startswith("#"):
                    continue
                parsed = urlsplit(target)
                if parsed.scheme or target.startswith("//"):
                    continue

                link_path = parsed.path
                if not link_path:
                    continue
                candidate = (ROOT / link_path.lstrip("/")) if link_path.startswith("/") else (path.parent / link_path)
                if not candidate.exists():
                    errors.append(
                        f"{relative(path)}:{line_number}: broken local link '{target}'"
                    )


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_skills(errors)
    check_markdown(errors)

    if errors:
        print(f"Framework validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Framework validation passed: "
        f"{len(ROOT_FILES)} root files, "
        f"{len(TEMPLATE_FILES)} template entries, "
        f"{len(SKILLS)} Codex skills, and "
        f"{len(markdown_files())} Markdown files checked."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
