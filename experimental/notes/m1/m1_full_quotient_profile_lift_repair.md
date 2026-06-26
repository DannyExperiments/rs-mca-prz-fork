# M1 Full Quotient-Profile Lift Repair

Status: PROVED / REPAIR / AUDIT.

This note records a repaired Paper-B residue-line construction and the
quotient-algebra definition it forces.  It concerns
`def:residue`, `lem:denom`, `thm:normalform`, `thm:closure`, `conj:B`,
`def:qprofile`, `thm:qnecessity`, `rem:aper`, and `conj:final-mca`.

This is not an official prize solve, not a protocol soundness claim, and not a
Paper-A no-slack example.  It is a repair to the quotient/aperiodic ledger for
arbitrary residue lines.

## 1. The Repaired Finite Lift

Let `F=F_q`, let `H <= F^*` be cyclic of order `n`, and let

```text
0 < k < n,   M | gcd(n,k),   N=n/M,   m=k/M,
1 <= sigma < M,   2 sigma <= n-k.
```

Fix `alpha0 in Q=H^M`, and put

```text
Acal = { A subset Q \ {alpha0} : |A|=m },
L = |Acal| = binom(N-1,m),
F_A(Y) = prod_{alpha in A} (Y-alpha).
```

Assume there is an `M`-th power

```text
c in (F^*)^M \ H^M
```

such that the values `F_A(c)` are pairwise distinct.  A sufficient condition is

```text
(q-1)/M > N + (m-1) binom(L,2).
```

Choose the external fiber `C_c={x : x^M=c}` and a `sigma`-subset
`R subset C_c` with nonzero sum.  Set

```text
E = L_R = prod_{r in R} (X-r).
```

Choose a `sigma`-subset `T` of the internal fiber

```text
C0 = { x in H : x^M=alpha0 },
```

and put

```text
L_T = prod_{t in T} (X-t),
B = L_T - E,
w = (E X^k)|_H.
```

For `A in Acal`, define

```text
U_A = { x in H : x^M in A },
S_A = T union U_A,
Q_A = E X^k - L_T F_A(X^M),
z_A = -F_A(c).
```

Then:

```text
|S_A| = k+sigma,
deg Q_A < k+sigma,
Q_A = w on S_A,
Q_A == z_A B mod E,
```

and the slopes `z_A` are distinct.  Thus the residue datum `(E,B,w)` has at
least

```text
binom(N-1,m)
```

distinct noncontained bad slopes at agreement `k+sigma`.

Moreover:

```text
E is nonzero on H,
gcd(E,B)=1,
tau_k([-B/E])=sigma,
the minimizing denominator is unique up to scalar,
E is not a syntactic pullback E0(X^d) for any d>1,
and the constructed witnesses are nontangent and noncontained.
```

The uniqueness statement follows from cross-multiplication: a competing
denominator `D` of degree `u <= sigma` gives a polynomial of degree at most
`k+sigma+u-1 < n`, so it vanishes identically on `H`; reducing modulo `E`
forces `E | D` because `gcd(E,B)=1`.

## 2. Hidden Quotient Structure

The same primitive minimal denominator is a factor of a quotient pullback:

```text
E | X^M-c.
```

Writing `X^M-c = E J`, the same direction has the nonprimitive pullback
completion

```text
-B/E = -(B J)/(X^M-c).
```

Thus a displayed primitive denominator can be non-pullback while the direction
still has active quotient structure.  The printed denominator-pullback test in
`rem:aper` is therefore not invariant under primitive cancellation.

The construction realizes the full quotient-core support count

```text
binom(N-1,m) = 2^{Q_H(eta)}
```

when deployed at a profile-maximizing scale.  This is larger than the
canonical-line quotient floor from `thm:qnecessity`,

```text
2^{(beta(rho)/HH(rho)) Q_H(eta)(1+o(1))}.
```

The necessity theorem remains correct as a canonical-line lower bound.  What
fails is using that canonical exponent as a universal upper allowance for all
quotient-structured arbitrary residue lines.

## 3. Quotient-Algebra Degree

For a primitive denominator `E`, define

```text
A_E = F[X]/(E),
u_M = X^M mod E,
nu_M(E) = dim_F F[u_M].
```

Equivalently, if `mu_{E,M}` is the monic generator of the kernel of

```text
F[Y] -> A_E,  Psi(Y) -> Psi(u_M),
```

then

```text
nu_M(E) = deg mu_{E,M}
        = min deg Psi with 0 != Psi in F[Y] and E | Psi(X^M).
```

In particular,

```text
nu_M(E)=1  iff  E | X^M-c
```

for a unique scalar `c`.

If `E` is nonzero on `H` and `M | n`, then `mu_{E,M}(X^M)` is also nonzero on
`H`.  Indeed, for every `alpha in H^M`, the class `u_M-alpha` is a unit in
`A_E`; hence `mu_{E,M}(alpha)` cannot vanish.

Therefore, when

```text
M nu_M(E) <= n-k,
```

the direction admits a pullback completion in the residue-line degree range.

## 4. Repaired Quotient Branch

The useful quotient test cannot be:

```text
there exists some pullback denominator representation.
```

That is too broad: normal-form denominator changes can make such a test nearly
vacuous.  The test should be attached to primitive minimal denominators.

One repaired branch is:

```text
[g] is divisibility-active quotient-algebraic at agreement gap a
if some primitive tau_k([g])-minimizing denominator E satisfies
M | gcd(n,k),  M > a,  and  M nu_M(E) <= n-k.
```

When `2 tau_k([g]) <= n-k`, the primitive minimizing denominator is unique up
to scalar, so this condition is unambiguous.

The finite lift above lies in this repaired quotient branch with `nu_M(E)=1`.
It should not be counted as genuinely quotient-free aperiodic evidence.

## 5. Consequence and Remaining Target

This note does not prove the final all-line MCA conjecture or its negation.
It shows that `rem:aper` and the quotient allowance in `conj:B` need repair
for arbitrary residue lines:

```text
active quotient-algebraic residue lines can carry the full quotient profile
2^{Q_H(eta)}, not just the canonical beta/H quotient floor.
```

A naive next formulation would ask for a projective locator bound in
`(F[X]/E)^*/F^*`.  That loses the scalar coordinate being counted as the
slope, so it is not the right theorem by itself.  The next Paper-B-native
target is the central lift of that projective problem:

```text
M1-CENTRAL-LIFT-SPLIT-PENCIL-INVERSE
```

Let `s=k+sigma`.  After removing every divisibility-active quotient-algebraic
primitive denominator, prove or refute the following inverse implication:

```text
If the split pencil F_z = E R_z - zB contains more than n^{1+epsilon}
completely H-split monic degree-s members with distinct z, then there are
M | gcd(n,k), M > sigma, and 0 != Psi in F[Y] such that
E | Psi(X^M) and M deg(Psi) <= n-k.
```

Equivalently, many distinct scalar lifts of one projective residue fiber
should force an active quotient-algebra completion.  The missing step is a
split-singular-fiber stabilizer theorem: many completely split members of the
pencil should force a nontrivial dilation stabilizer on ratios of locators.
That is the current candidate for the genuinely aperiodic residue-line packing
problem.
