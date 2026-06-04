# Skills Pyramid Concepts

## Flat Skills

Flat skill libraries work like this:

```text
user task -> skill description match -> full SKILL.md loads
```

This is simple and useful, but it has limits:

- repeated logic across skills
- no explicit dependency graph
- full skill content loaded when one substep is enough
- failures become chat history, not reusable repair knowledge

## Pyramid Skills

Skills Pyramid keeps existing skill loading behavior, but adds a planning discipline:

```text
abstract skill
  -> task-level skill
      -> atomic skill
      -> event-driven repair
      -> verification check
```

## Skill Types

| Type | Meaning |
| --- | --- |
| `abstract` | High-level pattern shared by multiple task skills. |
| `task_level` | End-to-end workflow for a class of tasks. |
| `atomic` | Small reusable operation inside multiple workflows. |
| `event_driven` | Trigger-response repair for an error, observation, or recurring local event. |
| `verification` | Evidence checklist proving work used the right context and succeeded. |

## Agent Host Boundary

Skills Pyramid does not require agent internals to change. It can run as plain skills first:

1. meta-skill checks whether skill-heavy routing is needed
2. routing skill selects likely skills
3. decomposition skill extracts reusable parts
4. verification skill checks evidence
5. refinement skill proposes safe edits

Later, the same concepts can power a real indexer or router.
