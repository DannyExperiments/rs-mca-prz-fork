# ROLE 06 - Frontier Checker Implementation Spec

Append this role prompt after `COMMON_PROMPT.md`.

## Wall

```text
RS-PRIZE-FRONTIER-V1-IMPLEMENTATION
```

## Objective

Turn the Role 06 frontier-checker audit into an implementation-ready spec.

Do not prove a theorem. Produce exact data structures, JSON schema, integer
algorithms, and a minimal test suite for the finite checker.

The checker must evaluate:

- scalar/list target `T_code=floor(q_code/2^128)`;
- MCA target `T_line=floor(q_line/2^128)`;
- lower certificates;
- upper certificates;
- conditional terms;
- unknown budget;
- reserve/radius staircase;
- field separation `q_gen`, `q_line`, `q_code`, `q_chal`.

## Required Deliverable

Give a complete script plan for:

```text
rs_prize_frontier_v1.py
```

including:

- input JSON schema;
- output JSON schema;
- integer functions;
- certificate registry format;
- refusal modes;
- sample inputs for Role 04, Role 07, and Role 08 packets.

## Success Criteria

Output `AUDIT` with an implementation-ready spec.

## Failure Criteria

Output `ROUTE_CUT` if the current finite definitions remain too ambiguous to
implement without new mathematical choices.

