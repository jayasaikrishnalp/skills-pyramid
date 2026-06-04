---
name: using-skills-pyramid
description: Use before any task involving existing skills, creating skills, improving skills, routing skills, extracting reusable procedures, or debugging repeated agent failures. This is the meta-skill for Skills Pyramid and should fire whenever the user mentions skills, skill libraries, SKILL.md, Claude/Codex skills, self-improving agents, or reusable agent workflows.
---

# Using Skills Pyramid

Use this skill to make skill use deliberate.

## Rule

Before loading or editing skill bodies, ask:

1. Is this a skill-routing problem?
2. Is this a skill-decomposition problem?
3. Is this a skill-verification problem?
4. Is this a skill-refinement problem?

Invoke only the next needed skill:

| Need | Use |
| --- | --- |
| Choose which skills apply | `skill-routing` |
| Split a large skill into reusable parts | `skill-decomposition` |
| Prove skill-driven work succeeded | `skill-verification` |
| Propose updates from a task trace | `skill-refinement-proposal` |

## Workflow

1. Read skill descriptions first.
2. Load full `SKILL.md` only when the description and task match.
3. Prefer the smallest useful set of skills.
4. Treat failure messages as event-driven repair candidates.
5. Never auto-edit live skills from one trace without checking reusability and verification.

## Output

When explaining a routing decision, use:

```text
Selected:
- <skill>: <reason>

Not selected:
- <skill>: <reason>

Missing:
- <candidate repair, verification check, or reusable operation>: <why it would help>
```
