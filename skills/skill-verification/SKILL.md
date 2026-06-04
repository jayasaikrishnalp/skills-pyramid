---
name: skill-verification
description: Verify skill-driven work before claiming success. Use after any task that used cloud credentials, logs, traces, generated skills, modified SKILL.md files, or followed a skill checklist. Requires fresh evidence, not confidence.
---

# Skill Verification

Evidence before completion claims.

## Verification Questions

1. Which skill(s) were used?
2. What did each selected skill require?
3. Which command/output proves the required context was correct?
4. Which failure mode was considered?
5. What remains unverified?

## Evidence Types

| Task | Evidence |
| --- | --- |
| Cloud account operation | caller identity, account/subscription match, region/context |
| Log or trace lookup | fetched object key, timestamp, trace id, source profile |
| Skill edit | YAML frontmatter parses, expected sections exist |
| Skill routing | selected and rejected skill rationale |
| Skill creation | test prompts or verifier checks |

## Output Format

```text
Verified:
- <claim>: <evidence>

Not verified:
- <gap>: <why>

Result:
<plain status>
```

## Failure Rule

If evidence is missing, say what is missing. Do not say done, fixed, clean, or complete.
