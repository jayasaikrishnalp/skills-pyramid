# Example: WK AWS Skill Pyramid

Current flat skill:

```text
connecting-to-wk-aws
```

Pyramid view:

```text
enterprise-cloud-account-access
  -> federated-aws-account-access
      -> connecting-to-wk-aws
          -> lookup-wk-fedroles-table
          -> choose-wk-aws-role-type
          -> assume-aws-sts-role
          -> preserve-sts-creds-in-single-shell
          -> verify-aws-caller-identity
```

Event-driven repairs:

```text
ExpiredTokenException -> re-assume role in same shell
AccessDenied on operation -> reconsider role type
empty results -> verify caller identity and region
account not found -> report missing WK-FedRoles onboarding
```

Runtime behavior goal:

```text
User: list EC2 instances in account 123456789012

Load:
- connecting-to-wk-aws
- preserve-sts-creds-in-single-shell
- verify-aws-caller-identity

Do not load:
- Azure subscription login
- OpenRouter trace analysis
- unrelated cloud skills
```
