#!/usr/bin/env python3
"""Validate Skills Pyramid skill folders without external dependencies."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter marker")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("missing closing frontmatter marker")
    raw = text[4:end].splitlines()
    data: dict[str, str] = {}
    for line in raw:
        if not line.strip() or line.startswith(" "):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def main() -> int:
    failures: list[str] = []
    skill_files = sorted(SKILLS.glob("*/SKILL.md"))
    if not skill_files:
        failures.append("no skills found")
    for path in skill_files:
        try:
            data = parse_frontmatter(path)
            name = data.get("name")
            description = data.get("description")
            if not name:
                raise ValueError("frontmatter missing name")
            if not description:
                raise ValueError("frontmatter missing description")
            if path.parent.name != name:
                raise ValueError(f"folder name {path.parent.name!r} does not match skill name {name!r}")
            print(f"ok {name}")
        except Exception as exc:
            failures.append(f"{path}: {exc}")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
