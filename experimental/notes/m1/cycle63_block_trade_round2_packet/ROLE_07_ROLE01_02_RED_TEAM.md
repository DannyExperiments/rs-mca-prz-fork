# ROLE 07 - Red-Team Audit Of Roles 01 And 02

Append this role prompt after `COMMON_PROMPT.md`.

## Wall

```text
AUDIT-L-LIST-APOLAR-CI-AND-MINIMAL-GJ-FIBER
```

## Objective

Red-team the two positive algebraic claims from Cycle 62:

```text
L-LIST-APOLAR-ALL-LAYER-CI
L-LIST-MINIMAL-CI-GJ-FIBER
```

Do not try to extend them. Try to find hidden edge-case failures.

## Required Checks

Audit:

- zero syndrome;
- equal generator degrees `j=d`;
- roots at infinity;
- repeated/nonreduced `Delta`;
- nonsplit closed points;
- small characteristic and divided-power issues;
- generator shear;
- non-full-coordinate padding;
- `D=L\\Supp(Delta)` empty or too small;
- endpoint `e=j`;
- projective versus affine normalization;
- compatibility with actual RS/GRS parity-check columns.

## Success Criteria

Output `AUDIT` if the lemmas survive and list exact wording corrections.
Output `COUNTERPACKET` if any lemma fails.

## Failure Criteria

Do not output a vague concern. Every negative point must include an explicit
finite example or a precise missing hypothesis.

