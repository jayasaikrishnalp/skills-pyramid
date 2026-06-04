---
name: skill-decomposition
description: Break a large SKILL.md into a Skills Pyramid: abstract parents, task-level workflow, atomic subskills, event-driven repairs, and verification checks. Use when improving existing skills, removing duplicate skill logic, or preparing skills for self-improving agents.
---

# Skill Decomposition

Turn one large skill into reusable structure without changing behavior.

## Decomposition Targets

| Target | Definition |
| --- | --- |
| Abstract parent | High-level pattern shared by multiple skills. |
| Task-level skill | Existing end-to-end workflow. |
| Atomic skill | Small reusable operation used by more than one task. |
| Event-driven repair | Trigger-response rule for an error or recurring observation. |
| Verification check | Evidence required before success claim. |

## Process

1. Read current `SKILL.md`.
2. Identify the main task-level workflow.
3. Extract repeated operations as atomic candidates.
4. Extract error rows or caveats as event-driven repairs.
5. Extract safety and completion checks as verification.
6. Preserve the original workflow.
7. Do not create new behavior not supported by the source skill.

## Output Format

```text
Skill type:
Parent abstract skill:
Domain parent:

Atomic candidates:
- name:
  trigger:
  provides:

Event-driven repairs:
- event:
  repair:

Verification:
- check:
  evidence:
```

## Guardrails

- Do not invent tools, accounts, commands, paths, or permissions.
- Do not split skills into tiny fragments that will never be reused.
- Keep source skill usable as standalone `SKILL.md`.
- Add pyramid metadata first; extract separate files later only when useful.
