---
name: skill-refinement-proposal
description: Propose safe improvements to a skill after a real task trace. Use when a skill caused confusion, missed a failure mode, repeated manual steps, used too much context, or succeeded in a reusable way. Produces human-reviewed proposals, not automatic live edits.
---

# Skill Refinement Proposal

Convert task traces into skill improvements.

## Inputs

- User task
- Skill(s) used
- Command/output trace
- Success/failure status
- Any user correction

## Proposal Gate

Propose a skill update only if the lesson is:

1. grounded in observed behavior
2. reusable beyond this one task
3. specific enough to guide future agents
4. safe to document
5. verifiable

Skip when the lesson is one-off, secret-bearing, speculative, or contradicted by the trace.

## Update Types

| Type | Use when |
| --- | --- |
| `description` | Skill under-triggered or over-triggered |
| `atomic` | Reusable operation is buried inside a large workflow |
| `event_repair` | Error or observation has a reliable response |
| `verification` | Agent claimed success without enough evidence |
| `guardrail` | Skill needs safety boundary |
| `merge_or_drop` | Skills overlap or one is redundant |

## Output Format

```text
Proposal:
- target skill:
- update type:
- evidence:
- change:
- verification:
- risk:

Apply now?
No. Human review required unless user explicitly asks to edit.
```
