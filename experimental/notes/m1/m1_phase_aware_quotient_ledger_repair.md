# M1 Phase-Aware Quotient Ledger Repair

Status: PROVED / REPAIR / ROUTE_CUT / AUDIT.

This note records a Paper-B-native repair to the quotient accounting for
arbitrary residue lines.  It concerns `def:residue`, `lem:denom`,
`thm:normalform`, `thm:closure`, `def:qprofile`, `thm:qnecessity`,
`rem:aper`, `conj:B`, and `conj:final-mca`.

This is not an official prize solve, not a protocol soundness claim, not an
ordinary list-decoding theorem, and not a Paper-A no-slack example.  The point
is narrower: the canonical quotient profile using `D | gcd(n,k)` is not an
intrinsic quotient profile for arbitrary Paper-B residue lines.

## 1. Phase-Shifted Monomial Lift

Let `F=F_q`, let `H <= F^*` be cyclic of order `n`, and let

```text
0 < k < n,    r=n-k,    D | n,    1 <= a < D,    2a <= r.
```

Put

```text
s=k+a=mD+t,    0 <= t < D,    N=n/D,    Q=H^D.
```

If `t=0`, set `T=empty`, `L_T=1`, and `Omega=Q`.  If `t>0`, choose
`alpha0 in Q`, choose a fixed `t`-subset

```text
T subset {x in H : x^D=alpha0},
```

and put `Omega=Q \ {alpha0}`.  For `A subset Omega`, `|A|=m`, write

```text
F_A(Y)=prod_{alpha in A}(Y-alpha).
```

Assume there is an external `D`-th power

```text
c in (F^*)^D \ H^D
```

such that the values `F_A(c)` are pairwise distinct.  A sufficient condition is

```text
(q-1)/D > N + (m-1) binom(L,2),
L = binom(N - 1_{t>0}, m),
```

with the collision term interpreted as zero when `L=1`.

Choose an `a`-subset `R` of the external fiber `{x : x^D=c}` with nonzero sum,
and define

```text
E=L_R,    B=rem_E L_T,    w=(E X^k)|_H.
```

For each `A`, set

```text
U_A={x in H : x^D in A},
S_A=T union U_A,
Q_A=E X^k - L_T F_A(X^D),
z_A=-F_A(c).
```

Then

```text
|S_A|=k+a,
deg Q_A < k+a,
Q_A=w on S_A,
Q_A == z_A B mod E,
```

and the slopes `z_A` are nonzero and pairwise distinct.  Moreover `E` is
nonzero on `H`, `gcd(E,B)=1`, `tau_k([-B/E])=a`, the minimizing denominator is
unique up to scalar, and the constructed witnesses are noncontained and
nontangent.  The denominator is not a syntactic pullback, but it has hidden
quotient algebra

```text
E | X^D-c,    nu_D(E)=1.
```

Thus one fixed phase-shifted monomial skeleton gives at least

```text
binom(n/D - 1_{t>0}, floor((k+a)/D))
```

distinct noncontained slopes.  The support phase is governed by `k+a`, not by
`k` alone.  No assumption `D | k` is used.

## 2. Fixed-Skeleton Inverse Lemma

For a primitive denominator `E`, put

```text
A_E=F[X]/(E),    u_D=X^D mod E,
nu_D(E)=dim_F F[u_D].
```

Fix the same `D`-phase skeleton `(T,Omega)`.  If two distinct quotient choices
`A != A'` have projectively equal locator residues modulo `E`, then cancellation
of the common factors gives a nonzero annihilating polynomial for `u_D`.
Consequently

```text
nu_D(E) <= |A \ A'| <= n/D - 1_{t>0} - m,
```

and hence

```text
D nu_D(E) <= n-k-a - 1_{t>0}(D-t) < n-k.
```

Therefore the all-divisor condition

```text
D | n,    D > a,    D nu_D(E) <= n-k
```

removes repeated supports inside every fixed complete-`D`-fiber plus fixed
partial-fiber monomial skeleton.  This is a fixed-skeleton theorem; it does not
yet control varying partial fibers, mixtures of skeletons, or nonmonomial
locator pencils.

## 3. Ledger Repair

The canonical Paper-B profile `def:qprofile` remains correct for the canonical
quotient-core construction and `thm:qnecessity`.  There, `D | gcd(n,k)` appears
because the canonical support uses exactly `k/D` complete fibers.

For arbitrary residue lines, the corresponding monomial phase profile must
instead use the actual agreement gap

```text
a=s_delta-k
```

and scan quotient scales `D | n`.  The repaired fixed-skeleton monomial profile
is

```text
Q_RL^mon(k,a)
  = max_{D | n, D > a}
      log_2 binom(n/D - 1_{t_D>0}, floor((k+a)/D)),
where t_D = (k+a) mod D.
```

This is a lower/profile term for the phase-shifted monomial branch, not a
proved universal upper bound for all residue lines.  It also counts slopes
directly, so an arbitrary-residue quotient allowance must pay the full
`2^{Q_RL^mon}` scale for this branch, not the canonical-line
`2^{(beta/H) Q}` floor.

## 4. Finite Packet

The following finite packet verifies that the restriction `D | gcd(n,k)` is
not intrinsic to arbitrary residue lines:

```text
q=8375183617, n=256, k=129, D=16, a=15,
s=k+a=144=9*16,
gcd(n,k)=1,
L=binom(16,9)=11440.
```

The field arithmetic checks:

```text
q is prime,
256 | q-1,
(q-1)/16 = 523448976,
16 + 8*binom(11440,2) = 523448656,
margin = 320.
```

Thus the separator condition holds, and the construction gives at least
`11440` distinct nonzero noncontained, nontangent slopes for one degree-`15`
primitive residue-line datum.  The old `D | gcd(n,k)` scan is empty for this
row.

This finite packet is not meant as another no-slack example.  It has positive
reserve `a=15`, lies in the Paper-B residue normal form, and tests the
quotient/aperiodic allocation.

## 5. Exact-Dyadic Phase Collapse

The phase repair does not by itself produce a new superlinear obstruction on
exact dyadic deployed rows.  If

```text
n=2^ell,    rho=u/2^b in lowest terms,    k=rho n,
```

then every dyadic divisor `D | n` with `D` not dividing `k` has bounded quotient
order:

```text
n/D <= 2^{b-1}.
```

Hence the genuinely new `D | n` but `D not | k` phase-shifted branch contributes
only `O_rho(1)` slopes on exact dyadic rows.  For all sufficiently large `n` in
the final reserve regime `a asymp n/log n`, the superlinear monomial quotient
profile comes from the old `D | k` scales.

So the new phase issue repairs the arbitrary-line ledger and attacks
`k=rho n+O(1)` stability, but it does not supply a fresh exact-dyadic
superlinear counterpacket by itself.

The earlier full-profile correction at `D | k` remains: arbitrary residue lines
can realize the full quotient profile, not merely the canonical
`beta/H` quotient floor.

## 6. Remaining Target

The next Paper-B-native target is the scalar-faithful central-lift inverse after
active quotient structures are removed.

One clean dyadic formulation is:

```text
n=2^ell, k=rho n exactly, a >= C n/log_2 n, 2a <= n-k.
```

For a primitive unique-minimal datum `(E,B)` with `deg E=a`, define

```text
Z(E,B) = { z in F_q^* :
  exists monic R_z of degree k and S_z subset H, |S_z|=k+a,
  E R_z - z B = L_{S_z} }.
```

Prove that `|Z(E,B)| > n^{1+epsilon}` forces either:

```text
1 < D <= a,     nu_D(E) < a,     D nu_D(E) <= n-k,
```

or

```text
M | gcd(n,k),   M > a,           M nu_M(E) <= n-k.
```

After excluding low-base proper completions, this reduces the exact-dyadic
case back to the original central-lift inverse problem.  A genuine killing
counterpacket must be exact dyadic, satisfy the entropy reserve, have more than
`n^{1+epsilon}` scalar slopes, and avoid both the low-base and profile-scale
quotient completions.

The sharp local test case is a shifted-local denominator such as

```text
E=(X-alpha)^a,    alpha notin H,
```

where typically `nu_D(E)=a`.  The corresponding moment problem asks whether
fixed inverse moments

```text
sum_{x in S} (alpha-x)^(-j) = c_j,    1 <= j < a,
```

can carry more than `n^{1+o(1)}` distinct products

```text
prod_{x in S} (alpha-x).
```

That is the next concrete central-lift lemma rather than another finite
quotient packet.
