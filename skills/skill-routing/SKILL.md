---
name: skill-routing
description: Select the smallest useful set of skills for a task. Use when a user asks which skill applies, when multiple skills overlap, when a task could combine several skills, or when an agent may be wasting context by loading too much skill content.
---

# Skill Routing

Choose skills by expected task utility, not by keyword match alone.

## Inputs

- User task
- Available skill names and descriptions
- Optional recent error/output
- Optional already-loaded skill bodies

## Routing Process

1. Classify the task:
   - cloud access
   - observability/log investigation
   - code change
   - skill maintenance
   - research/synthesis
   - other
2. List candidate skills from descriptions.
3. Reject skills that only share vague words.
4. Prefer task-level skill first.
5. Add atomic/event-driven skills only when they directly reduce risk or likely failure.
6. Keep context budget small.

## Selection Rules

Load a full skill body when:

- task directly matches description
- user names the skill
- failure matches a documented event-driven repair
- required verification lives in the skill body

Do not load a skill body when:

- match is only a shared noun
- user asks for explanation only and metadata is enough
- another selected skill covers it more directly

## Output Format

```text
Selected:
- <skill>: <why>

Deferred:
- <skill>: <why not now>

Route:
1. <first skill/action>
2. <second skill/action>
3. <verification>
```
