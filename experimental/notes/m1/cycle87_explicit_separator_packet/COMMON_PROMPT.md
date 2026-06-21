# COMMON PROMPT FOR CYCLE 87

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

You are working on the RS-MCA / proximity-prize finite obstruction route. Do
not brainstorm from scratch. Read the attached context first, especially:

- `CYCLE87_CURRENT_STATE.md`
- `m1_cycle86_two_copy_affine_color_returns_audit.md`
- `m1_cycle85_role05_transfer_returns_audit.md`
- `m1_cycle84_wallbreaker_returns_audit.md`
- the Cycle86 raw returns if you need to inspect a worker's exact claim

The active target is:

```text
L-CYCLE86-EXPLICIT-TWO-COPY-SEPARATOR-CERTIFICATE
```

Prove, with a replayable certificate, that a concrete separator `y` for the
two-copy construction has projective multiplicity at most 8 and that the
resulting supports form one transverse affine syndrome line of a single
official-rate GRS code.

Equivalent checker wall:

```text
V-CYCLE86-U-PROJECTIVE-MMAX8-CENSUS
```

For `y` in an extension over the Cycle84 base field, define

```text
mu_proj(y) =
  max_kappa #{ T in P0 : [P_T(y)] = kappa in L^x / F0^x }.
```

If

```text
mu_proj(y) <= 8,
```

then the two-copy construction has enough distinct slopes to clear the
official `2^-128` finite target.

You must keep separate:

- finite-model certificate;
- one-copy RS/MCA transfer;
- official two-copy counterpacket;
- public replay artifact;
- full prize theorem.

Known banked facts:

```text
m_max(beta) = 2
Occ(beta) = 52,747,567,092
D = 24

P = 52,747,567,104
N = Occ(beta) = 52,747,567,092
q_line = 17^48
T_line = floor(q_line / 2^128)
       = 338,617,018,271,848,945,628

P*N = 2,782,305,834,758,012,141,568 > T_line
N^2 = 2,782,305,834,125,041,336,464 > T_line
```

Known cuts:

1. Do not use the naive additive two-copy formula as a banked theorem.
   The surviving mechanism is product/reciprocal product after common affine
   normalization.

2. Do not use direct tensor/direct-sum amplification as a one-line `t=1`
   theorem. A valid two-copy construction must be one GRS/RS code and one
   affine syndrome line.

3. The cleanest proposed package is:

```text
(n,k,sigma,j) = (464,232,6,226)
```

The padded fallback package is:

```text
(n,k,sigma,j) = (560,280,6,274)
```

Prefer the 464 package if valid. Fall back to 560 only if the shortening
argument fails.

Your answer must start with exactly one status label:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

Before finalizing, do a self-audit. Explicitly answer:

1. What exact implication did I prove, and what exact implication did I not
   prove?
2. Is the result official-prize-relevant, or only a finite/model/research
   certificate?
3. What is the first line in the reduction chain where the theorem could fail?
4. Are `q_gen`, `q_line`, `q_code`, `q_chal`, and the `2^-128` target being
   used correctly?
5. Could quotient/periodic structure, contained incidences, same-slope
   collisions, or affine color normalization reduce the claimed numerator?
6. If my answer is a PLAN, what exact theorem/checker/counterpacket would
   convert it into PROOF or COUNTERPACKET?

Do not hide behind broad language. Give the exact next lemma, exact missing
hypothesis, or exact counterexample mechanism.

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?

