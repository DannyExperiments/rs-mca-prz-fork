# Cycle 97 Prompt: Fixed-Prime Two-Support Aperiodic Collision

You are working on RS-MCA / Proximity Prize research.

No Internet. Take all the time to reason you need. Use MAX reasoning.

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. Do you see a route to a full solve? If yes, what is the next
exact lemma or construction?

Before finalizing, do a self-audit.

Explicitly answer:

1. What exact implication did I prove, and what exact implication did I not prove?
2. Is the result official-prize-relevant, or only a finite/model/research certificate?
3. What is the first line in the reduction chain where the theorem could fail?
4. Are q_gen, q_line, q_code, q_chal, and the 2^-128 target being used correctly?
5. Could quotient/periodic structure, contained incidences, same-slope collisions, or affine color normalization reduce the claimed numerator?
6. If my answer is a PLAN, what exact theorem/checker/counterpacket would convert it into PROOF or COUNTERPACKET?

Do not hide behind broad language. Give the exact next lemma, exact missing
hypothesis, or exact counterexample mechanism.

## Current State

Cycle95 banked:

```text
L-CYCLE95-ANCHORED-T1-EVAL-LIST
```

The `t=1` anchored MCA cloud equals the `eval_alpha` image of the
arbitrary-word dimension-`k+1` RS list; noncontainment is automatic.

Cycle96 banked/cut:

```text
L-CYCLE96-NORM-SIEVE-IS-DEAD
L-CYCLE96-WORD-HEIGHT-FLOOR
```

The monomial Galois/norm sieve cannot be repaired for arbitrary words because
arbitrary word lifts carry height about `p^(1-rho-o(1))`, while the norm
contradiction needs height below roughly `p^(sigma/n)/n`.

Thus the next proof route must be fixed-prime, not archimedean norm-sieve.

## Target

Attack the fixed-prime two-support wall:

```text
S1 / L-CYCLE97-FIXED-PRIME-TWO-SUPPORT-APERIODIC-COLLISION
```

For `p == 1 mod n`, smooth generated-field domain `H`, `k=rho n`,
`s=k+sigma`, `sigma >= C n/log n`, and arbitrary interpolant
`U in F_p[X]`, `deg U<n`, define the arbitrary-word fiber:

```text
Fib_U(s) = { S subset H, |S|=s : deg(rem_{L_S} U) <= k }.
```

For fixed `S in Fib_U(s)`, prove or kill:

```text
#{ S' in Fib_U(s) :
   S triangle S' is aperiodic / not explained by quotient cosets }
   <= n^{O(1)}.
```

Equivalently, prove a polynomial degree bound for the maximal-secant graph on
the arbitrary-word fiber after charging quotient-periodic cores.

## First Restricted Target

Use the syndrome-bandwidth filtration:

```text
F_b = { U : deg U <= s+b }.
```

The `b=0` case is the monomial/prefix layer. Do not reprove only `b=0`.

Try first:

```text
b=1
```

or, if `b=1` is still too broad:

```text
b=1 with fixed S and explicit equations in the elementary symmetric
coordinates of S'.
```

Produce one of:

```text
PROOF: polynomial bound for b=1 aperiodic two-support collisions;
COUNTERPACKET: b=1 aperiodic superpolynomial collision family;
ROUTE_CUT: proof that b=1 is already equivalent to full arbitrary-word local limit;
EXACT_NEW_WALL: smallest exact algebraic object below b=1.
```

## Source Files To Read

Use the mounted project source. Read:

```text
readme.md
agents.md
tex/slackMCA_v3.tex
experimental/notes/m1/m1_cycle96_arbitrary_word_norm_sieve_audit.md
experimental/notes/m1/cycle96_arbitrary_word_norm_sieve_raw/response.md
experimental/scripts/cycle96_word_height_floor_toy.py
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

Do not return a lower-side quotient-floor construction. This is the upper-side
fixed-prime arbitrary-word collision wall.

