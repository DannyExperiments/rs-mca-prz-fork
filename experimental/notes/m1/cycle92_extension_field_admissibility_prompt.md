# Cycle 92 Prompt: Extension-Field Prize Admissibility

You are working on RS-MCA / Proximity Prize research.

No Internet. Take all the time to reason you need. Use MAX reasoning.

Try to fully solve the problem. If you cannot fully solve it, progress it as much as possible. Do you see a route to a full solve? If yes, what is the next exact lemma or construction?

Before finalizing, do a self-audit.

Explicitly answer:

1. What exact implication did I prove, and what exact implication did I not prove?
2. Is the result official-prize-relevant, or only a finite/model/research certificate?
3. What is the first line in the reduction chain where the theorem could fail?
4. Are q_gen, q_line, q_code, q_chal, and the 2^-128 target being used correctly?
5. Could quotient/periodic structure, contained incidences, same-slope collisions, or affine color normalization reduce the claimed numerator?
6. If my answer is a PLAN, what exact theorem/checker/counterpacket would convert it into PROOF or COUNTERPACKET?

Do not hide behind broad language. Give the exact next lemma, exact missing hypothesis, or exact counterexample mechanism.

## Current State

Cycle91 returned a partial but promising extension-field construction:

```text
p = 5
q = 5^64
H <= F_q^*
|H| = 256
rho = 1/16
k = 16
ell = 17
delta = 1 - 1/16 - 1/256
gap = 1/256
```

The monomial line is:

```text
f(x) = x^17
g(x) = x^16
u_z(x) = f(x) + z g(x)
```

Every distinct 17-subset sum in `H` gives a noncontained bad slope. The
sign-digit / power-basis argument claims at least:

```text
binom(64,17) * 2^17
  = 180,796,807,614,761,533,440
```

distinct bad slopes.

The threshold is:

```text
floor(5^64 / 2^128) = 1,593,091
```

The leading reserve check is:

```text
H2(1/16) / log2(5^64) = 0.0022697332025462657
gap = 1/256 = 0.00390625
```

So the row appears to be above reserve and far above the `2^-128` numerator
threshold.

However, the Cycle91 response ended mid-proof at `stop_reason=tool_use`, and
its count estimate was off by about three bits. Use the corrected audit, not
the raw approximate numbers.

## Target

Attack:

```text
W-CYCLE92-EXTENSION-FIELD-PRIZE-ADMISSIBILITY
```

Decide whether the `F_{5^64}` smooth power-of-two subgroup row is:

1. an official Proximity Prize counterpacket;
2. a valid extension-field research certificate but not official-prize;
3. or invalid due to a hidden source condition.

You must source-audit this against the actual project files.

## Required Branches

### Branch A: Official Counterpacket

Prove that the official prize formulation permits finite fields of size
`q=5^64` and smooth multiplicative subgroup domains `H <= F_q^*` of order
`256`, at rate `rho=1/16`.

Then complete the theorem:

```text
epsilon_mca(RS[F_{5^64}, H, 16], 1 - 1/16 - 1/256)
  > 2^-128
```

with exact field ledger, noncontainment, distinct-slope count, and reserve
comparison.

### Branch B: Research Certificate Only

If the official prize is restricted to deployed prime fields, BabyBear-like
fields, or specific FFT domains, prove that limitation from source text and
state the exact deployed-prime wall.

### Branch C: Counterpacket To Cycle91

Try to falsify the Cycle91 construction:

- Does `F_{5^64}^*` really contain an order-256 subgroup?
- Does that subgroup generate `F_{5^64}`?
- Is the sign-digit subset-sum injection correct in characteristic 5?
- Are the generated objects genuine 17-subsets?
- Is noncontainment correct?
- Is the reserve inequality using the correct `tau_star`, not only a leading
  asymptotic proxy?
- Is `q_line=q_code=q_chal=5^64` correct?

If any fail, give the exact failure and repair if possible.

## Source Files To Read

Use the mounted project source. Read:

```text
readme.md
agents.md
tex/slackMCA_v3.tex
tex/RS_disproof_v3.tex
experimental/notes/m1/m1_cycle90_prize_family_embedding_audit.md
experimental/notes/m1/m1_cycle91_above_reserve_power_two_audit.md
experimental/notes/m1/cycle91_above_reserve_power_two_raw/response.md
experimental/scripts/cycle91_extension_power_two_arithmetic.py
```

## Required Output Format

Start with one of:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

Then give:

1. Executive verdict and confidence.
2. Exact theorem/counterpacket/route cut.
3. Proof or obstruction.
4. Verification requirements.
5. Next exact lemma or construction.

Do not promote to official prize counterpacket unless the extension-field
admissibility issue is source-validly discharged.

