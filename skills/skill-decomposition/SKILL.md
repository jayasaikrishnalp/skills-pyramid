---
name: skill-decomposition
description: Identify reusable structure inside a large SKILL.md without premature extraction: task-level workflow, atomic candidates, event-driven repairs, and verification checks. Use when improving existing skills, capturing repeated failures, removing duplicate skill logic, or preparing skills for a measured router experiment.
---

# Skill Decomposition

Turn one large skill into reusable structure without changing behavior. Prefer durable repairs and verification first. Treat atomic skills as candidates until reuse is proven.

## Decomposition Targets

| Target | Definition |
| --- | --- |
| Abstract parent | High-level pattern shared by multiple skills. |
| Task-level skill | Existing end-to-end workflow. |
| Atomic candidate | Small reusable operation that may become a skill only after reuse is proven. |
| Event-driven repair | Trigger-response rule for an error or recurring observation. |
| Verification check | Evidence required before success claim. |

## Process

1. Read current `SKILL.md`.
2. Identify the main task-level workflow.
3. Identify repeated operations as atomic candidates.
4. Extract error rows or caveats as event-driven repairs.
5. Extract safety and completion checks as verification.
6. Preserve the original workflow.
7. Do not create new behavior not supported by the source skill.

## Earned Extraction Rule

Keep an operation inline unless all are true:

1. Three or more task-level skills reuse it.
2. The operation has enough complexity or risk to need its own instructions.
3. Separate loading reduces mistakes, wrong-skill loads, or context in a measured router test.
4. The original task skill remains usable without the extracted skill.

Do not create separate atomic skill files for tiny one-command checks. Example: `aws sts get-caller-identity` is a verification line until it becomes part of a broader cross-cloud identity verification workflow.

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
- Add repair and verification metadata first; extract separate files later only when reuse and measurement justify it.
