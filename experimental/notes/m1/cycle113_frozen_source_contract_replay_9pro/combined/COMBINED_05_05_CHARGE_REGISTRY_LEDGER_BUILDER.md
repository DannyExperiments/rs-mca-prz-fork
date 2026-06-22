# Cycle113 Combined Prompt - 05_05_CHARGE_REGISTRY_LEDGER_BUILDER

## Common Prompt


NO INTERNET. Do not browse, search, cite online sources, or use external tools.
Use only the attached packet and your own reasoning. Use maximum reasoning.

You are one of nine independent theorem workers on the RS-MCA / Proximity Prize
M1 upper-side route. Try to fully solve the assigned problem. If you cannot
fully solve it, progress as far as possible and isolate the exact next theorem,
checker, or counterpacket mechanism. Be ambitious, but do not overclaim.

Read `CURRENT_CYCLE113_STATE.md`, `MANIFEST.md`, the canonical tracker, the
Cycle110-112 audits, and the Cycle112 key returns before answering.

The active wall is:

```text
L-CYCLE113-OFFICIAL-APCORR-INTERVAL-PREFIX-REJECTION-OR-COUNTERPACKET
```

The replay harness target is:

```text
V-CYCLE113-FROZEN-SOURCE-CONTRACT-REPLAY
```

Cycle112 narrowed the problem to the interval / overlapping-prefix /
P190-style stress family. Role 02's conditional target was:

```text
p = 130 * 2^128 + 1
floor(p / 2^128) = 130
claimed colors = 190
after one endpoint = 189
additional official loss needed to avoid counterpacket >= 59 colors
```

This is not banked as a counterpacket. Your job is to push the official-source
decision as hard as possible.

Return under one of these labels only:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

Preferred terminal decisions, if you can justify one:

```text
SOURCE_REJECTED:
  name the first official source/APcorr/final-normalization clause that fails,
  with exact calculation.

COLOR_COMPRESSED_OR_CHARGED:
  give the exact final retained color map or official charge set, the number
  of colors removed/merged, the cap, and the integer q_line allocation.

SOURCE_VALID_LOW_T1_COUNTERPACKET:
  prove official source adapter and AP_corr acceptance, all charges absent or
  exactly paid, and final retained colors > floor(q_line / 2^128).

T1_APCORR_LOCAL_LIMIT:
  prove official AP_corr plus absence of frozen named charges implies bounded
  interpolation-defect Fourier mass, hence the t=1 local-limit and q_line
  closure.

SOURCE_RECEIPT_MISSING_NO_CLAIM:
  if the packet lacks a necessary official source/APcorr/final-color/charge
  receipt, name exactly which receipt is missing and what would decide it.
```

Do not answer with broad language like "probably charged" or "seems
aperiodic." A charge is valid only if it names:

```text
official predicate
exact final retained color subset or quotient map
exact cap
exact q_line allocation
no double counting with free colors or other charges
```

Correct q-ledger discipline:

```text
q_line = sole final color/security denominator
q_gen  = entropy denominator only after a source theorem proves the entropy loss
q_code = code field size / metadata; not a denominator
q_chal = unused absent a protocol transfer theorem
target = 2^128 * N_free <= q_line
```

Explicitly answer whether you see a route to a full solution. If yes, give the
first theorem/checker that would convert your answer into `PROOF` or
`COUNTERPACKET`. If no, give the exact route cut and the first failure line.

Verification bar:

1. State the exact implication proved.
2. State the exact implication not proved.
3. Identify the first line in the reduction chain where the theorem could fail.
4. Use `q_gen`, `q_line`, `q_code`, `q_chal`, and the `2^-128` target correctly.
5. Check whether quotient/periodic structure, contained incidences,
   same-slope collisions, endpoint effects, affine color normalization, or
   final retained normalization reduce the claimed numerator.
6. If you propose a checker, specify its exact inputs, outputs, terminal
   decisions, and no-false-positive/no-false-negative proof.



## Self-Audit Addendum


Before finalizing, do a self-audit.

Explicitly answer:

1. What exact implication did I prove, and what exact implication did I not
   prove?
2. Is the result official-prize-relevant, or only a finite/model/research
   certificate?
3. What is the first line in the reduction chain where the theorem could fail?
4. Are `q_gen`, `q_line`, `q_code`, `q_chal`, and the `2^-128` target being used
   correctly?
5. Could quotient/periodic structure, contained incidences, same-slope
   collisions, endpoint effects, affine color normalization, or final retained
   normalization reduce the claimed numerator?
6. If my answer is a `PLAN`, what exact theorem/checker/counterpacket would
   convert it into `PROOF` or `COUNTERPACKET`?

Do not hide behind broad language. Give the exact next lemma, exact missing
hypothesis, or exact counterexample mechanism.



## Role Prompt


Your task is to build the most complete exact charge registry and integer
`q_line` ledger the packet supports.

Include at least these possible charge families:

```text
endpoint
field-transfer
affine-color
periodic / quotient
same-slope
contained incidence
tangent/support
prefix-design / short restricted-sum
additive-energy
interpolation-defect Fourier
retained-tag normalization
hidden action rank
```

For each charge, state:

```text
official predicate
charged final color set
cap
q_line allocation
whether it overlaps another charge
whether it applies to interval/P190
```

Use Cycle112's no-double-spend theorem: an above-threshold final retained color
set cannot be saved by partitioning the same colors into charged/free bins
unless the charge has an exact disjoint cap and allocation.

Try to prove:

```text
COLOR_COMPRESSED_OR_CHARGED
```

or explain exactly why no official charge ledger is present. If you prove a
charge, show how many final colors remain and verify:

```text
2^128 * N_free <= q_line
```

If no complete ledger can be built, return `EXACT_NEW_WALL` with the first
missing charge receipt.

