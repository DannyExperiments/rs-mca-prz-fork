# Cycle106 9-Pro Wallbreaker Packet

Purpose: run nine independent ChatGPT Pro instances against the live RS-MCA M1
upper-side wall:

```text
W-CYCLE106-KFREE-APERIODIC-MOMENT-CURVE-INCIDENCE
```

Upload the whole directory or the zip made from this directory. The context is
small by design and excludes raw historical JSONL dumps.

Use this sequence in each instance:

1. Upload `context/` or the packet zip.
2. Paste `COMMON_PROMPT.md`.
3. Paste exactly one role file from `ROLE_01_...md` through `ROLE_09_...md`.
4. Let it run to completion.
5. Save every visible answer and any generated files.

Do not reuse the failed Cycle106 Fable answer as math evidence. It is included
only as a warning that the previous run failed because the source snapshot was
not mounted.

## Role Map

```text
ROLE_01_PROOF_BUILDER_DIRECT_INCIDENT_BOUND.md
ROLE_02_COUNTERPACKET_APERIODIC_GROWING_K.md
ROLE_03_ELIMINANT_SUBRESULTANT_WRONSKIAN.md
ROLE_04_APERIODIC_DEPHASING_DISTINCT_SUPPORT.md
ROLE_05_SYMMETRIC_FUNCTION_GEOMETRY.md
ROLE_06_CHARACTER_SUM_FOURIER_CAP.md
ROLE_07_FINITE_STRESS_CHECKER.md
ROLE_08_SOURCE_AUDITOR_OFFICIAL_CHAIN.md
ROLE_09_REFEREE_SYNTHESIS_NEXT_THEOREM.md
```

## Required Output Labels

Every answer must begin with exactly one of:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

## Current Known State

Cycle103 proved the bandwidth-1 upper-side numerator bound.

Cycle104 proved the fixed-bandwidth bound:

```text
|Theta_U| <= binom(n,k)(sigma+1)
```

Cycle105 banked the k-free collapse:

```text
theta active
<=> (g_1(theta),...,g_{sigma+1}(theta)) in M_s
```

and complement duality:

```text
M_s ~= M_{n-s}.
```

Cycle106 remains open because the first Fable launch failed at the harness
layer. The live wall is the aperiodic, k-free incidence bound.

