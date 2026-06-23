# Dispatch Receipt

Date prepared: 2026-06-24

Status: prompts prepared, not dispatched by Codex.

## Context zip

```text
/Users/danielcabezas/fixed_jet_two_ended_5pro_audit_context.zip
```

The zip SHA-256 is recorded beside the zip as:

```text
/Users/danielcabezas/fixed_jet_two_ended_5pro_audit_context.zip.sha256
```

## Roles

1. `ROLE_01_TRANSFER_LEMMAS_HOSTILE_AUDIT.md`
2. `ROLE_02_COMPUTED_INPUT_INSTANTIATION_AUDIT.md`
3. `ROLE_03_ABF_DEFINITION_AUDIT.md`
4. `ROLE_04_PAPERS_AD_REUSABILITY_AUDIT.md`
5. `ROLE_05_SYMBOLIC_GENERALIZATION_ATTACK.md`

## Dispatch rule

Paste `COMMON_PROMPT.md` followed by exactly one role prompt.

Do not ask "did we solve the prize?" in this round.

The desired outputs are first-false-line audits and reusable proof targets.
