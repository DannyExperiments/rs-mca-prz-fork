# Cycle 48 Upper-Inverse Refresh Audit

Status: COUNTERPACKET / BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Confidence: high for the reductions, template lemmas, and quotient-component
counterpacket. Unknown for the remaining upper inverse theorem.

## Verdict

Cycle 48 is significant, but it is not a full solve. It changes the route board
in a more important way than a routine lemma: it cuts the naive matching-upper
route and replaces it with a sharper finite/inverse problem.

The Cycle 47 lower/failure branch remains the strongest banked theorem
candidate: the domain-uniform pair-rank and Bessel-shell argument gives the
smooth-domain scalar MCA failure branch throughout the strict entropy-subcritical
range.

The Cycle 48 upper-side round says the matching safe-side theorem is still open.
In particular, the old wall

```text
W-MCA-AA-RES-ENTROPY-BOUNDARY-MATCHING-UPPER
```

is too coarse. A balanced residue-cloud theorem alone is not enough, and a
quotient definition that removes only literal denominators of the form
`E_0(X^M)` is false for arbitrary anchors.

## What Was Banked

### Lower/failure branch

The finite lower theorem from Cycle 47 survives the audit:

- for arbitrary distinct domains, the pair-rank law is
  `rank(w -> (R_S(w), R_S'(w))) = t + min(t, |S\S'|)`;
- for smooth multiplicative domains, `E=X^t`, `B=1`, `f=w/E`,
  `g=-1/E` give the lower/failure MCA construction;
- the shell factor is bounded by
  `J <= I_0(2 sqrt(aj/Q)) <= exp(2 sqrt(aj/Q))`;
- an anchor exists with missed slopes at most `QJ/lambda`, where
  `lambda=binom(n,k+t)/Q^t`;
- every slope is bad once `lambda > QJ`.

This is a lower-branch theorem candidate, not a threshold theorem.

### Support-syndrome all-t reduction

Prompt 1 gave a bankable reformulation: every residue-line witness, for every
denominator degree `1 <= t <= n-k`, is a collinearity condition in a
support-dependent syndrome space of dimension exactly `sigma`. The pair rank in
this formulation is

```text
sigma + min(sigma, d).
```

This makes the official all-denominator maximum visible. It also shows that a
balanced-only theorem does not by itself prove the full scalar MCA upper branch.

### Template lemmas

The following template facts are bankable in the balanced reduced stratum:

- `B != 0` implies exact balanced witnesses are automatically noncontained.
- same-witness clusters contribute only one slope.
- a fixed `k`-point tangent core contributes at most `j+1` slopes.
- bounded-degree osculating witness curves contribute at most degree times
  `j+1` slopes.
- a lower effective denominator reduces to the actual RS residual-list problem.
- for `t < sigma`, slopes inject into a list for `RS[k+t]` with residual slack
  `sigma-t`.
- common-core peeling with core size `< k` reproduces the same balanced wall on
  a punctured domain, so it is not an independently solved template.

### Locator-scroll circuit certificate

Prompt 2 gave a useful algebraic certificate for superlinear balanced clouds.
For complement locators `p_z=Lambda_{T_z}`, define

```text
C_w(p) = [rem_ML(W p)]_E
D_B(p) = [B p]_E.
```

Successful locators satisfy the matrix-pencil condition

```text
C_w(p_z) = z D_B(p_z).
```

If the locator span does not meet `E F[X]_{<=j-t}`, then the number of slopes is
at most `j+1`. Therefore every cloud larger than `j+1` contains an
`E`-resonant locator circuit:

```text
sum c_i p_i = 0,
sum c_i z_i p_i = E H != 0,
```

with support size at most `j+2`, together with

```text
sum c_i Q_i p_i = 0,
sum c_i P_i p_i = -B H.
```

This does not prove the upper theorem, but it gives a finite certificate that
any high cloud must carry.

### Interleaved list diagonalization

Prompt 8 banked an exact list-side reduction at the official target scale. For
any linear code and interleaving arity `m`, if `binom(ell,2) < q`, then an
`m`-interleaved list of size at least `ell` projects injectively to a scalar list
of size at least `ell`.

For the official target `epsilon*=2^-128` and `q < 2^256`, taking
`ell=floor(epsilon* q)+1` gives

```text
delta_list^*(C,m,2^-128) = delta_list^*(C,1,2^-128).
```

Thus the interleaving-specific wall is closed at the official target scale. The
grand list challenge reduces to the scalar arbitrary-word actual-list/full
support local-limit problem.

## Counterpacket

Prompts 3 and 4 found the major route cut.

The proposed above-entropy upper theorem is false if aperiodicity only removes
literal quotient-pullback denominators `E(X)=E_0(X^M)`.

There are reduced, balanced, noncontained residue-line data with

```text
E | X^M - c
```

but `E` is not a literal pullback through `X^M`. A one-fiber punctured quotient
anchor then realizes roughly

```text
binom(n/M - 1, k/M)
```

distinct slopes. This can exceed `n^{1+o(1)}` even above the ambient entropy
boundary, while surviving the advertised tangent, same-witness, contained,
low-denominator, residual-list, and Frobenius/base-core checks.

The correct invariant is not only syntactic pullback form of `E`. For every
quotient scale `M`, one must inspect

```text
xi_M = [X^M]_E
d_M(E) = deg minpoly_F(xi_M).
```

Low `d_M(E)` is a quotient-component denominator. The extreme case
`d_M(E)=1` is exactly the construction above.

The source quotient term based on the canonical exponent
`(beta(rho)/H_2(rho)) Q_H` is not enough for arbitrary anchors unless these
broader quotient-component and fixed-defect quotient-anchor packets are
explicitly removed or charged. Raw arbitrary-anchor quotient packets can
saturate the full quotient-core profile.

## Finite Boundary Correction

Prompt 7 gave the finite checker correction. In finite form, a bare
`n^{1+o(1)}` upper bound immediately after `Q^t >= binom(n,k+t)` is not the
right statement.

Let

```text
N = binom(n,k+t).
```

The random line-occupancy scale is

```text
R_line = ceil(N / Q^(t-1)).
```

At the central equality `Q^t=N`, this is `R_line=Q`, so the candidate upper
bound is trivial at the center of the transition. A finite upper theorem has to
start only after the exact lower obstruction clears, and should have the shape

```text
|Cloud| <= U_quotient + R_line + A_theta(n),
```

with effective-degree and quotient-certified packets routed separately.

The finite checker should quotient anchor gauges:

```text
w ~ w + E A,  deg A < k
w ~ w + c B
B ~ c B.
```

For fixed `E,B`, the anchor quotient dimension is `n-k-1`.

## Current Correct Wall

The cleanest global replacement wall is:

```text
W-MCA-SYNDROME-TRANSVERSE-SECANT-ENTROPY-INVERSE
```

Syndrome form:

- let `syn:F^L -> F^r` be a parity-check/syndrome map for `RS[F,L,k]`;
- let `h_x` be the syndrome column at coordinate `x`;
- for `T subset L`, `|T|=j`, set `W_T=span{h_x:x in T}`;
- define

```text
Pi_j(C) = max_{u,v} #{ z : exists T, u+zv in W_T and v notin W_T }.
```

Then

```text
epsilon_mca(C, 1-(k+sigma)/n) = Pi_j(C)/q.
```

This exact syndrome formulation covers every denominator degree at once. The
positive half of the grand MCA challenge is equivalent to bounding transverse
intersections of a line with the family of `j`-secant syndrome subspaces, after
quotient and tangent templates are separated.

Important companion walls:

```text
W-MCA-QUOTIENT-ACTION-RANK-INVERSE
W-MCA-AA-RES-LOCATOR-SCROLL-SECTION-OR-QUOTIENT
W-MCA-HIGH-DENOMINATOR-THICK-RESIDUE-COMPRESSION
W-L1-ARBITRARY-WORD-FULL-SUPPORT-LOCAL-LIMIT-ABOVE-CORRECTED-RESERVE
```

## What Remains Open

The hard remaining MCA side is the safe-side upper theorem. The strongest exact
forms are equivalent:

1. syndrome transverse-secant entropy inverse theorem;
2. support-family rank-defect classification for the residue maps modulo the
   slope line;
3. locator-scroll section extraction or quotient theorem;
4. quotient-circuit extraction theorem after removing quotient-component and
   fixed-defect quotient-anchor packets.

The list side is also still open, but it is now scalar:

```text
W-LIST-FULL-SUPPORT-INTERSECTION-LOCAL-LIMIT
```

The interleaved-specific correlated-compression problem is not needed for the
official `2^-128` target once the scalar list problem is solved.

## PRZ-Facing Summary

Cycle 47 gives a strong lower/failure branch. Cycle 48 does not solve the upper
branch; it refreshes the route. The main new result is a route cut: literal
quotient-pullback aperiodicity is too narrow. Quotient-component denominators
`E | m(X^M)` and fixed-defect quotient anchors can produce large balanced
clouds above entropy. The upper theorem must either delete/charge these packets
at the full quotient-core scale or prove a sharper quotient-action-rank inverse
theorem.

The clean positive-side target should now be stated in syndrome coordinates as
a transverse-secant line inverse theorem. This avoids denominator-coordinate
ambiguity and includes `t<sigma`, `t=sigma`, and `t>sigma` in one object.

## Next Exact Lemma

Primary:

```text
W-MCA-SYNDROME-TRANSVERSE-SECANT-ENTROPY-INVERSE
```

Prove that above corrected entropy and quotient reserve, a line in the
Reed-Solomon syndrome space with more than `R_line + A_theta(n)` transverse
intersections with the `j`-secant subspace arrangement must descend through a
proper quotient or belong to an explicitly bounded tangent/common-envelope
template.

Concrete first sublemma:

```text
W-MCA-AA-RES-LOCATOR-SCROLL-SECTION-OR-QUOTIENT
```

Given many successful divisor locators on the pencil
`C_w - Z D_B`, quotient the common kernel, compute a Kronecker minimal basis,
and prove that either a large selected subset lies on a low-`Z`-degree locator
section, or the locator common-factor branch synchronizes to one fixed tangent
packet, or the data descend through a quotient-component packet.

Secondary finite-checker sublemma:

```text
W-MCA-LABELLED-SUBSPACE-DESIGN-RANK-DEFECT
```

For the quotient

```text
W_{E,B} = F^L / (E RS[F,L,k] + F B),
```

classify support-family systems whose label projection contains more than
`R_line + A_theta(n)` distinct labels. The allowed outcomes are lower effective
denominator, quotient symmetry, affine/tangent rank defect, or a new explicitly
defined template.
