# Affine-prefix whole-stratum pole obstruction

## Status

This note proves a finite, line-local Reed--Solomon MCA lower bound for one
explicit characteristic-five family.  It combines the existing
collision-aware simple-pole compiler with the exact affine-prefix source
census.  The delta is the parameterized whole-stratum application and its
field guard, not a new pole compiler.

The result is structural.  It does not identify a primitive semantic C1--C9
cell, prove survival after the official semantic first-match order, close a
finite or asymptotic ledger row, or move the official score from `0/2`.

The source base is
`999b8f3a1da959b8002ecf1819d37725af56d383`.  The verifier pins the generic
and affine-prefix source files used below and reconstructs the local compiler
from all 16 subsets of one affine square.

## Exact family

For every integer `t >= 1`, set

```text
B = 10t,  j = 9t,  n = 40t,  m = 20t,  k = 20t-1,
F_t = GF(5^(30t)).
```

Choose an `F_5`-basis

```text
a_1,u_1,v_1,...,a_B,u_B,v_B
```

of `F_t`, and define

```text
D_t = {a_i + eps*u_i + eta*v_i :
       1 <= i <= B and eps,eta in {0,1}}.
```

Basis independence makes the displayed `40t` evaluation points distinct.  Let

```text
C_t = RS_(F_t)(D_t,20t-1).
```

For an `m`-support `S` in `D_t`, write

```text
Q_S(X) = product_(x in S) (X-x).
```

Let `Omega_t` consist of the supports with exactly `9t` diagonal blocks and
with a non-diagonal local subset in every remaining block.  The non-diagonal
subsets in those remaining `t` blocks must contribute `2t` points in total.

## Literal source census

For one affine-square block, removal of the harmless global minus sign in the
first locator coefficient reduces the source signature to

```text
(|S|, sum eps(x), sum eta(x)) in F_5^3.
```

Enumeration of all 16 local subsets gives 15 signatures.  Fourteen occur
once.  The unique collision is the signature `(2,1,1)`, carried by the two
diagonals.  The nonambiguous choices by local support size are therefore

```text
Q(y) = 1 + 4y + 4y^2 + 4y^3 + y^4.
```

Because the `3B` displayed basis vectors are independent, a global first
locator coefficient determines every local signature.  Consequently the
source map has exactly

```text
L_t = binom(10t,t) [y^(2t)] Q(y)^t
```

images on `Omega_t`, every nonempty fiber has exactly `2^(9t)` supports, and

```text
M_t = |Omega_t| = 2^(9t) L_t.
```

The quantities `L_t`, `2^(9t)`, and the associated representation moments are
source data.  They are not, by themselves, distinct-slope payments.

## Whole-stratum pole theorem

There is an element `alpha_t` in `F_t \ D_t` for which the values
`Q_S(alpha_t)`, `S in Omega_t`, are pairwise distinct.  Indeed, for distinct
supports `S,T`, the nonzero polynomial `Q_S-Q_T` has degree at most
`m-1=k`.  Thus at most

```text
n + k binom(M_t,2)
```

field elements are forbidden by the domain and the pairwise locator
differences.

The crude bound

```text
M_t <= (2^19 * 14)^t
```

together with

```text
5^30 > 20 (2^19 * 14)^2
```

gives the all-`t` chain, with `A=2^19*14`,

```text
5^(30t) > 20^t A^(2t)
          >= (10t+1) A^(2t)
          > 10t M_t^2 + 40t
          > 40t + (20t-1) binom(M_t,2).
```

In particular,

```text
5^(30t) > 40t + (20t-1) binom(M_t,2)
```

for every `t >= 1`.  Hence such an `alpha_t` exists in the coefficient field;
no extension-valued challenge alphabet is used.

On `D_t`, define the received line

```text
r_0,t(x) = x^(20t)/(x-alpha_t),
r_1,t(x) = -1/(x-alpha_t).
```

For every `m`-support `S`, put

```text
gamma_S = alpha_t^(20t) - Q_S(alpha_t),
h_S(X) = (X^(20t) - Q_S(X) - gamma_S)/(X-alpha_t).
```

The numerator defining `h_S` vanishes at `alpha_t`.  Its leading degree-`m`
terms cancel, so `deg h_S <= m-2 < k`.  On `D_t`,

```text
r_0,t + gamma_S r_1,t - h_S = Q_S/(X-alpha_t).
```

Because `alpha_t` is outside the domain and `Q_S` is squarefree, the complete
agreement set is exactly `S`.

The direction is support-wise nontrivial.  If a polynomial `g` of degree less
than `k` agreed with `-1/(X-alpha_t)` on `m=k+1` points, then
`(X-alpha_t)g(X)+1` would be a nonzero polynomial of degree at most `k` with
`k+1` distinct roots, while its value at `alpha_t` is one.

Conversely, an exact-`m` witness `(gamma,S,h)` makes

```text
E(X) = X^m - gamma - (X-alpha_t)h(X)
```

a monic degree-`m` polynomial vanishing on `S`.  Hence `E=Q_S`, which uniquely
recovers `gamma` and `h`.  The exact-`m` witness incidence is therefore in
bijection with all `m`-subsets of `D_t`.

Place the `Omega_t` witnesses first and the complementary supports second.
The separator makes the `M_t` target slopes pairwise distinct.  A complement
support may share one of those raw slopes, but the deliberately first target
cell owns that slope and the later occurrence is deleted.  This gives a
literal witness-exhaustive, slope-level structural first-match partition and
proves the lower bound

```text
B_(C_t)^MCA(20t) >=
    2^(9t) binom(10t,t) [y^(2t)](1+4y+4y^2+4y^3+y^4)^t.
```

Only this lower bound is asserted.  The full pole-line bad-slope count may be
larger than `M_t`.

## Endpoint reconstruction

At `t=1`,

```text
B=10, n=40, m=20, k=19,
L_1=40, source fiber=512, M_1=20,480.
```

The exact forbidden-element bound and field margin are

```text
40 + 19 binom(20,480,2) = 3,984,394,280,
5^30 - 3,984,394,280 = 931,322,574,611,494,121,345.
```

The finite-slope normalization denominator is exactly `|F_t|=5^(30t)`, not a
projective or extension-field denominator.  Also `m=n/2=k+1`, so the agreement
fraction is exactly one half and lies strictly below `1-k/n`.

## Structural obstruction

The direct affine-prefix `j=9t` stratum has `L_t` occupied slopes and source
fiber size `2^(9t)`.  The pole construction uses the identical supports and
source fibers but has `M_t=2^(9t)L_t` pairwise distinct target slopes.  Thus
the source-fiber data do not determine the final slope projection.

Let

```text
lambda = H(9/10) + (1/10) log(14).
```

The exact coefficient bounds give

```text
lim_(t->infinity) log(L_t)/(40t) = lambda/4
                                  = 0.1472471765882435...
```

For every certified upper budget `U_t` for the unsplit target slope set,
`U_t >= M_t`; the unconditional source-safe consequence is only

```text
liminf_(t->infinity) log(1 + 2^(9t) U_t)/(40t) >= lambda/4.
```

An ordinary limit is not asserted for arbitrary budget sequences.

If the target slopes are first-match covered by `r_t` cells satisfying

```text
Nbar_i <= 2^(9t),
U_i <= K_t (1+Nbar_i),
log K_t = o(n),
```

then

```text
r_t >= M_t/(K_t(1+2^(9t))) > L_t/(2K_t)
```

and therefore

```text
liminf_(t->infinity) log(r_t)/n >= lambda/4.
```

Every hypothesis in this splitting statement is load-bearing.  In particular,
it is not an unconditional lower bound for semantic atlases, alternative
scales, or sufficiently lossy decompositions.

## Replay

Run

```bash
python3 experimental/scripts/verify_affine_prefix_pole_stratum.py
python3 -O experimental/scripts/verify_affine_prefix_pole_stratum.py
```

Both outputs must match the checked-in expected transcript.  The verifier
pins ten source/dependency files, reconstructs the 16-subset local census,
checks the exact `t=1` endpoint and all-t field guard, computes the asymptotic
constant, and rejects eleven theorem-specific semantic mutations.

## Nonclaims and remaining wall

This note does not prove:

- a primitive C1--C9 cell or survival after earlier semantic owners;
- separation of `Omega_t` from its complement;
- equality in the displayed MCA lower bound;
- a direct slope payment from the source moments;
- failure of every MI+MA, Fourier, signed, geometric-incidence, alternative-
  scale, or semantic-splitting method;
- an ordinary limit for arbitrary budgets;
- an unconditional exponential semantic-atlas lower bound;
- a row-uniform result over arbitrary fields, domains, support densities, or
  received lines;
- a deployed smooth/circle-row payment, recurrence parent, Grand MCA hard
  input, Grand List theorem, or official-score movement.

The exact remaining wall is to prove that a source-valid target of this size
survives the official semantic C1--C9 first-match order, or to derive a valid
budget at the actual semantic scales after earlier ownership.  Until then the
result is a zero-ledger structural route cut.
