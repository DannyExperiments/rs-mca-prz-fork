# Cycle 98 Prompt: B1 Active External-Root Incidence

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

Cycle97 gives a corrected bandwidth-`1` decomposition:

```text
L-CYCLE97-BANDWIDTH1-ROOT-CONFIGURATION-DECOMPOSITION
```

For monic `U` of degree `s+1`, list codewords correspond to monic `V=U-P` of
degree `s+1` with prescribed top `sigma+1` coefficients and at least `s` roots
in `H`.

The root configurations split into:

```text
Type A:   all s+1 roots in H;
Type B:   V=(X-theta)L_S, |S|=s, theta in F_p.
```

The raw Cycle97 response omitted the `theta in H` repeated-root branch. Codex
corrected this by finite checker. The `theta in H` branch is only an `n`-sized
union of bandwidth-`0` prefix slices. The real wall is:

```text
theta in F_p \\ H.
```

## Target

Attack:

```text
L-CYCLE98-B1-ACTIVE-EXTERNAL-ROOT-INCIDENCE
```

Given prefix target `c=(c_1,...,c_{sigma+1})`, define:

```text
c(theta)_j = sum_{i=0}^j (-theta)^{j-i} c_i, c_0=1.
```

Prove or kill:

```text
#{ theta in F_p \\ H :
   Phi_{sigma+1}^{-1}(c(theta)) is nonempty and aperiodic }
   <= n^{O(1)}
```

for `p == 1 mod n`, smooth generated-field subgroup `H`, `k=rho n`,
`s=k+sigma`, `sigma >= C n/log n`, and above corrected reserve after quotient
periodic cores are charged.

Equivalently: bound the intersection of the explicit degree-`sigma+1` curve
`theta -> c(theta)` with the aperiodic prefix image of `s`-subsets of `H`.

## Required Tasks

1. Read the Cycle97 audit correction carefully. Do not assume the raw
   external-only Type B statement is literally true.
2. Prove a polynomial active-external-root bound if possible.
3. If not, reduce it to the smallest exact finite incidence/character-sum
   statement.
4. If false, produce a source-valid counterpacket:
   superpolynomially many external `theta`, nonempty aperiodic prefix fibers,
   not charged by quotient-periodic cores.
5. Explicitly separate:

```text
theta in H      -> polynomially many bandwidth-0 slices;
theta notin H   -> active external-root wall.
```

## Source Files To Read

Use the mounted project source. Read:

```text
readme.md
agents.md
tex/slackMCA_v3.tex
experimental/notes/m1/m1_cycle97_fixed_prime_two_support_audit.md
experimental/notes/m1/cycle97_fixed_prime_two_support_raw/response.md
experimental/scripts/cycle97_bandwidth1_decomposition_check.py
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
fixed-prime active-root incidence wall.

