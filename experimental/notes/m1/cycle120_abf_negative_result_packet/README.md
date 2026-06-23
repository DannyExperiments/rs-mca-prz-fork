# Cycle120 ABF Negative Result Packet

Date: 2026-06-24

Purpose:

```text
Package the Cycle116/Cycle119 explicit-code RS-MCA theorems and supporting deterministic computations against the printed
ABF grand MCA challenge definition.
```

Open in this order:

```text
1. THEOREM_NOTE.md
2. SUBMISSION_CHECKLIST.md
3. REFEREE_CHECKLIST.md
4. PRO_AUDIT_PROMPTS.md
5. PRZ_HANDOFF.md
6. PROVENANCE.md
```

Core ABF-facing claim:

```text
K = F_17^32
H = <theta>, |H| = 512
C = RS[K,H,256]
N = 52,747,567,092

epsilon_mca(C,125/256) >= N / 17^32 > 2^-128.
```

Important refinement:

```text
Cycle116 agreement 262 is already sufficient for ABF Definition 4.3 because
(1 - 125/256) * 512 = 262 and ABF uses |S| >= (1-delta)n.

Cycle119 agreement 263 is a strict-ball strengthening:
512 - 263 = 249 < 250 = (125/256) * 512.
```

Claim discipline:

```text
This packet claims an ABF-admissible negative result at delta = 125/256,
conditional on the finite Cycle84/Cycle116 proof chain.

It does not claim the exact value of delta*_C, ordinary list decoding,
protocol soundness failure, an asymptotic theorem, or peer-reviewed prize
acceptance.
```

