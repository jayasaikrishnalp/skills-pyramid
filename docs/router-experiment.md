# Router Experiment

## Goal

Prove whether Skills Pyramid routing beats flat skill description matching before migrating a whole skill library into a hierarchy.

## Scope

Start with three real skills:

| Skill | Why |
| --- | --- |
| `connecting-to-wk-aws` | Has role choice, account verification, and real event-driven repairs. |
| `connect-to-wk-azure` | Similar enterprise cloud access shape, useful for cross-cloud verification comparison. |
| `openrouter-trace-lookup` | Different domain: observability lookup with S3/log verification behavior. |

## Baseline

Flat matching:

```text
user task -> skill description match -> load task skill -> execute
```

## Pyramid Candidate

Minimal routing:

```text
user task
  -> classify task
  -> select task-level skill
  -> attach inline repair/verification expectations
  -> execute
  -> record missed repair or verification gap
```

Do not extract atomic skill files during the first experiment. Mark only candidates.

## Metrics

Track per task:

| Metric | Meaning |
| --- | --- |
| selected skills | Count and names of full `SKILL.md` bodies loaded. |
| wrong-skill loads | Skills loaded but not used. |
| missing-skill events | Needed repair/verification not present in selected skill. |
| verification misses | Cases where account, role, region, trace ID, or data source was not proven before reporting. |
| repair hits | Event-driven repair used successfully, such as `AccessDenied -> re-pick role`. |
| task outcome | Success, blocked, or wrong result. |

Token counts are useful only if measured from real runs. Do not claim token savings from hierarchy alone.

## Success Gate

Keep router work if at least one is true across a small eval set:

1. Fewer wrong-skill loads than flat matching.
2. Fewer verification misses.
3. More successful repair hits.
4. Lower measured context use without lower task quality.

If none hold, keep Skills Pyramid as a lightweight repairs + verification methodology and avoid deeper hierarchy.

## Extraction Gate

Extract an atomic skill only when:

1. Three or more task-level skills reuse the operation.
2. Extraction reduces mistakes or repeated instructions in measured runs.
3. The operation is large or risky enough to justify its own `SKILL.md`.

Tiny checks stay inline.
