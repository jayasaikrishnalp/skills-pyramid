#!/usr/bin/env python3
"""Validate Skills Pyramid skill folders without external dependencies."""

import json
import os
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

PLUGIN_MANIFESTS = [
    ROOT / ".claude-plugin" / "plugin.json",
    ROOT / ".codex-plugin" / "plugin.json",
]
HOOK_FILES = [
    ROOT / "hooks" / "hooks.json",
    ROOT / "hooks" / "run-hook.cmd",
    ROOT / "hooks" / "session-start",
]
MARKETPLACE_FILES = [
    ROOT / ".claude-plugin" / "marketplace.json",
]


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


def validate_plugin_manifest(path: Path) -> list[str]:
    failures: list[str] = []
    if not path.exists():
        return [f"{path}: missing plugin manifest"]
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path}: invalid JSON: {exc}"]
    if data.get("name") != "skills-pyramid":
        failures.append(f"{path}: name must be skills-pyramid")
    if not data.get("description"):
        failures.append(f"{path}: missing description")
    if not data.get("version"):
        failures.append(f"{path}: missing version")
    return failures


def validate_hook_files() -> list[str]:
    failures: list[str] = []
    for path in HOOK_FILES:
        if not path.exists():
            failures.append(f"{path}: missing hook file")
    hooks_json = ROOT / "hooks" / "hooks.json"
    if hooks_json.exists():
        try:
            data = json.loads(hooks_json.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.append(f"{hooks_json}: invalid JSON: {exc}")
        else:
            session_start = data.get("hooks", {}).get("SessionStart", [])
            if not session_start:
                failures.append(f"{hooks_json}: missing SessionStart hook")
    session_start_script = ROOT / "hooks" / "session-start"
    if session_start_script.exists() and not os.access(session_start_script, os.X_OK):
        failures.append(f"{session_start_script}: not executable")
    return failures


def validate_marketplace(path: Path) -> list[str]:
    failures: list[str] = []
    if not path.exists():
        return [f"{path}: missing marketplace file"]
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path}: invalid JSON: {exc}"]
    if data.get("name") != "skills-pyramid":
        failures.append(f"{path}: marketplace name must be skills-pyramid")
    plugins = data.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        failures.append(f"{path}: missing plugins list")
        return failures
    names = [plugin.get("name") for plugin in plugins if isinstance(plugin, dict)]
    if "skills-pyramid" not in names:
        failures.append(f"{path}: missing skills-pyramid plugin entry")
    for plugin in plugins:
        if not isinstance(plugin, dict) or plugin.get("name") != "skills-pyramid":
            continue
        source = plugin.get("source")
        if isinstance(source, str):
            if source != "https://github.com/jayasaikrishnalp/skills-pyramid.git":
                failures.append(f"{path}: source must point to GitHub repo")
        elif isinstance(source, dict):
            if source.get("url") != "https://github.com/jayasaikrishnalp/skills-pyramid.git":
                failures.append(f"{path}: source.url must point to GitHub repo")
        else:
            failures.append(f"{path}: invalid source for skills-pyramid")
    return failures


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
    for path in PLUGIN_MANIFESTS:
        manifest_failures = validate_plugin_manifest(path)
        failures.extend(manifest_failures)
        if not manifest_failures:
            print(f"ok {path.relative_to(ROOT)}")
    hook_failures = validate_hook_files()
    failures.extend(hook_failures)
    if not hook_failures:
        print("ok hooks")
    for path in MARKETPLACE_FILES:
        marketplace_failures = validate_marketplace(path)
        failures.extend(marketplace_failures)
        if not marketplace_failures:
            print(f"ok {path.relative_to(ROOT)}")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
