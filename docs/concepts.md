# Skills Pyramid Concepts

## Flat Skills

Flat skill libraries work like this:

```text
user task -> skill description match -> full SKILL.md loads
```

This is simple and useful, but it has limits:

- repeated logic across skills
- no explicit dependency graph
- failures become chat history, not reusable repair knowledge
- verification habits are easy to skip under pressure
- wrong-scope work can look valid until account/role/region is checked

## Pyramid Skills

Skills Pyramid keeps existing skill loading behavior, but adds a planning discipline. The first useful layer is not a deep taxonomy; it is durable repairs and evidence checks:

```text
task-level skill
  -> event-driven repair
  -> verification check
  -> atomic candidate
```

## Skill Types

| Type | Meaning |
| --- | --- |
| `abstract` | High-level pattern shared by multiple task skills. |
| `task_level` | End-to-end workflow for a class of tasks. |
| `atomic` | Small reusable operation inside multiple workflows. |
| `event_driven` | Trigger-response repair for an error, observation, or recurring local event. |
| `verification` | Evidence checklist proving work used the right context and succeeded. |

## Earned Hierarchy Rule

Do not split every repeated-looking step into its own skill file.

Create separate atomic skills only when all are true:

1. At least three task-level skills reuse the operation.
2. The operation has enough detail or risk to justify separate instructions.
3. Separate loading reduces mistakes or context, measured against flat skill use.
4. The source task skills can still run standalone.

Examples:

| Keep inline | Candidate for extraction |
| --- | --- |
| `aws sts get-caller-identity` verification | Multi-cloud account identity verification used by AWS, Azure, GCP skills |
| One `AccessDenied` repair in one skill | Cross-account role-selection repair shared by several cloud skills |
| One command syntax note | Reusable all-region scan workflow with pagination, retries, and evidence output |

Hierarchy is scaffolding until a router uses it. The repo should avoid taxonomy tax unless a measurable router or repeated repair proves payoff.

## Agent Host Boundary

Skills Pyramid does not require agent internals to change. It can run as plain skills first:

1. meta-skill checks whether skill-heavy routing is needed
2. routing skill selects likely skills
3. decomposition skill identifies reusable candidates, repairs, and verification checks
4. verification skill checks evidence
5. refinement skill proposes safe edits

Later, the same concepts can power a real indexer or router. That router must prove better selectivity, fewer wrong-skill loads, or fewer verification misses before the library commits to a deep hierarchy.
