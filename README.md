# Skills Pyramid

![Skills Pyramid hero](assets/skills-pyramid-hero.png)

Superpowers for skill use.

Skills Pyramid is a small skill suite that makes coding agents use skills deliberately instead of treating them as a flat folder of prompt files.

It does not change Claude Code, Codex, Cursor, Gemini, or any agent internals. It works like a methodology layer:

1. route to the right skills
2. decompose large skills into reusable parts
3. verify skill-driven work before claiming success
4. propose skill improvements from real traces

## Why

Most agents see only skill names and descriptions until a skill triggers. That is good for token cost, but it creates a problem: skills stay isolated. Agents miss reusable substeps, repeat failure fixes, and load whole procedures when only a small part matters.

Skills Pyramid gives agents a process for turning a flat skill library into a practical hierarchy:

```text
abstract pattern
  -> task-level skill
      -> atomic subskill
      -> event-driven repair
      -> verification check
```

## Included Skills

| Skill | Purpose |
| --- | --- |
| `using-skills-pyramid` | Meta-skill. Makes the agent check skill routing before doing skill-heavy work. |
| `skill-routing` | Selects which skills should be loaded and which should stay unloaded. |
| `skill-decomposition` | Extracts atomic skills, abstract patterns, and failure repairs from a large `SKILL.md`. |
| `skill-verification` | Verifies work done through skills with evidence before completion claims. |
| `skill-refinement-proposal` | Proposes safe skill updates from successful or failed task traces. |

## Install As Plugin

Claude Code:

```text
/plugin marketplace add jayasaikrishnalp/skills-pyramid
/plugin install skills-pyramid@skills-pyramid
```

Local Claude Code development:

```bash
claude --plugin-dir .
```

Codex CLI:

```bash
codex plugin marketplace add jayasaikrishnalp/skills-pyramid
codex plugin add skills-pyramid@skills-pyramid
```

Then start a new agent session so plugin skills and hooks reload.

## Manual Skill Install

Use this only when plugin install is unavailable. Manual skill copy installs the skills, but it does not install the SessionStart bootstrap hook.

Claude Code:

```bash
cp -R skills/* ~/.claude/skills/
```

Codex and other `.agents`-style hosts:

```bash
cp -R skills/* ~/.agents/skills/
```

Then start a new agent session so skill metadata reloads.

## Hook Bootstrap

The plugin includes a Claude/Codex-compatible `SessionStart` hook:

```text
session starts
  -> hooks/session-start reads skills/using-skills-pyramid/SKILL.md
  -> injects only the bootstrap skill into context
  -> agent routes to other pyramid skills only when needed
```

This keeps normal skill lazy-loading behavior. It does not inject every skill body.

## Validate

```bash
python3 scripts/validate_skills.py
```

## Core Rule

Do not auto-edit live skills after every task. Propose changes first. Apply only grounded, reusable, verified improvements.

## Status

Early plugin + skill-suite prototype. No database, no graph engine, no router service yet. The first goal is behavior change through skills, like Superpowers. A runtime indexer can come later if the manual workflow proves useful.
