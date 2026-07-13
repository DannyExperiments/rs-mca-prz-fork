# Canonical reduced rational-host exact compiler

**Status:** PROVED under the explicit reduced rational-host hypotheses below;
AUDIT for the finite replays.  This is a narrow `J <= 0` theorem, not a
section-nonpositive extraction theorem and not a Grand MCA result.

**Base:** `origin/main@ea4eb0784417ca5ab503a3c31a7eef6464ad100a`.

**Exact delta:** a section-nonpositive received line that already admits one
reduced rational-host presentation has a unique canonical presentation and a
witness-exhaustive prefix/remainder compiler.  The genuinely new part is the
general denominator degree `d > 1` normal form and incidence bijection.  The
separating `d = 1` case is already present in the source; the nonseparating
`d = 1` formulas below are retained as a collision-literal audit
specialization.

The theorem does **not** extract such a presentation from an arbitrary
`J <= 0` line.  Its direct scale `M_RH` is not PR #714's image-normalized
partial-occupancy scale and is not compared with the complete profile
envelope.  Pending PR #715 records a global deduplicated `LineRay` census
target and leaves that target open; this note identifies the exact `LineRay`
object only on the reduced rational-host stratum.

## 1. Source anchors and ownership boundary

At the stated base, the principal source anchors are:

| source | stable label / line | role here |
| --- | --- | --- |
| `experimental/asymptotic_rs_mca_frontiers.tex` | `def:exact-witness-incidence`, L1324 | exact-`a` witness object |
| same | `def:first-match`, L1453; `def:profile-payment`, L1476 | actual slope ownership and payment convention |
| same | `prop:exact-prefix-list`, L1965 | locator-prefix/list precursor |
| same | `thm:exact-list-line-bijection`, L2097; `cor:exact-prefix-ray-realization`, L2157 | old separating simple-pole case |
| same | `thm:aperiodic-ray-obstruction`, L2184 | sharpness obstruction to scale one |
| same | `thm:exact-partial-occupancy`, L3609; `thm:canonical-partial-occupancy-atlas`, L3744 | optional support partition and exact add-back |
| same | `def:explanation-occupancy`, L5647; `lem:exact-occupancy-compiler`, L5674 | support, explanation-pair, and slope projections |
| `experimental/grande_finale.tex` | `def:line-rays`, L1857; `prop:line-ray-saturation`, L1867 | deduplicated `(slope, codeword)` pair object |

Pending PR #714 (`1df8a072`) proves a corrected arbitrary-remainder prefix
image theorem and gives a strict-deep finite example.  It does not identify
the slope projection of a received line.  Pending PR #715 (`20370115`)
re-records the global tier-(4) target on `|LineRay_E|`, corrects its model, and
explicitly leaves the target open.  The present theorem is compatible with
both: it supplies an exact local source map, but no global natural-scale
inequality.

The official score remains `0/2`.

## 2. Hypotheses and ledgers

Let `D subseteq B subseteq F`, where `B` and `F` are finite fields and
`|D| = n`.  Let

```text
C = RS_F(D,k),              1 <= k < n,
k+1 <= a <= n,
J = a^2 - n(k-1) <= 0.
```

Fix `1 <= d <= a-k`.  Suppose the received line
`r = (r_0,r_1) in (F^D)^2` has, at every `x in D`, a presentation

```text
r_0(x) = c_0(x) + U(x)/L(x),
r_1(x) = c_1(x) - T(x)/L(x),                         (RH1)
```

with

```text
c_0,c_1 in F[X]_{<k},
L in F[X] monic, deg L = d, L(x) != 0 for x in D,
0 != T in F[X]_{<d}, gcd(L,T) = 1,
deg U = a, ell = lc(U) != 0.
```

Impose the canonical host gauge

```text
[X^j]U = 0 for d <= j <= d+k-1.                      (RH2)
```

### Field ledger

- The support points and every support locator `Q_S` lie over `B`.
- The received words, hosts `c_0,c_1`, denominator `L`, direction `T`,
  numerator `U`, remainders, explaining polynomials, and slopes lie over `F`.
- The forced prefix below is initially an element of `F^w`; if the support
  family is nonempty, equality with a locator prefix forces it into `B^w`.
- No challenge field, challenge subset, list denominator, extension transfer,
  or `B_phi` normalization is used.

### Normalization ledger

- Monicity fixes denominator scaling.
- `gcd(L,T)=1` and `deg T<deg L` make the rational direction reduced.
- `T != 0` makes `gamma -> gamma T` injective.
- The gauge (RH2) fixes the polynomial/rational ambiguity in `r_0`.
- `ell` is retained explicitly; support locators are monic.
- Supports have size exactly `a`, and the constructed line/codeword agreement
  set is proved to be exactly that support.

Nothing in `J <= 0` constructs (RH1).  It supplies the degree room that makes
an already existing reduced form unique.

## 3. The theorem

Put

```text
w = a-k-d >= 0.
```

For `1 <= i <= w`, define the forced locator-prefix coordinates

```text
z_i = ell^{-1}[X^{a-i}]U.
```

For `S in binom(D,a)`, let

```text
Q_S(X) = product_{x in S}(X-x),
P_S = U - ell Q_S,
rho_{L,U}(S) = Rem_L(P_S) in F[X]_{<d}.
```

Let `Phi_w(S)` denote the first `w` coefficients below the leading
coefficient of `Q_S`, with the unique empty value when `w=0`, and define

```text
F_RH(r,a) = {S in binom(D,a):
             Phi_w(S)=z and rho_{L,U}(S) in F T}.     (RH3)
```

### Theorem (canonical reduced rational-host compiler)

Under the hypotheses above:

1. **Automatic degree room.** One has `a<n` and `k+2d<n`.

2. **Canonical normal-form uniqueness.** Among all reduced presentations
   (RH1) whose denominator degree is at most `a-k`, after imposing (RH2),
   the tuple

   ```text
   (d,L,T,c_0,c_1,U)
   ```

   is unique.

3. **Exact witness bijection.** For each `S in F_RH(r,a)`, there is a unique
   `psi(S) in F` satisfying

   ```text
   rho_{L,U}(S) = psi(S) T.
   ```

   Define

   ```text
   h_S = c_0 + psi(S)c_1 + (P_S-psi(S)T)/L.           (RH4)
   ```

   Then `h_S in F[X]_{<k}`, and

   ```text
   Theta: F_RH(r,a) -> W_a(r),
          S |-> (psi(S),S,h_S)                        (RH5)
   ```

   is a bijection onto the complete exact-`a` witness incidence of
   `def:exact-witness-incidence`.

4. **Exact agreement and nontriviality.** On `D`,

   ```text
   r_0 + psi(S)r_1 - h_S = ell Q_S/L.                 (RH6)
   ```

   Its zero set is exactly `S`.  Moreover, `r_1` is not explained on `S`
   by any degree-`<k` polynomial, so every displayed witness is
   support-wise nontrivial.

5. **Explanation pairs and slope fibers.** Define

   ```text
   m_gamma = |{S in Phi_w^{-1}(z):
                rho_{L,U}(S)=gamma T}|,
   M_RH = |F_RH(r,a)|.
   ```

   Every explanation pair `(gamma,h)` has retained-support occupancy one,
   and

   ```text
   |W_a(r)| = |LineRay_F(r_0,r_1;a)| = M_RH
            = sum_{gamma in F} m_gamma,               (RH7)

   |Z_a(r)| = |{gamma in F:m_gamma>0}|.                (RH8)
   ```

   Thus `M_RH` is exactly the deduplicated `(slope,codeword)` pair count on
   this line, not necessarily the number of slopes.

## 4. Proof

### 4.1 The section-nonpositive degree gate

From `a^2 <= n(k-1)`,

```text
(n+k)^2-4a^2 >= (n+k)^2-4n(k-1)
               = (n-k)^2+4n > 0.
```

Hence `2a<n+k`.  Since all parameters are integral,
`2a-k <= n-1`.  Therefore `a<n` and, for `d<=a-k`,

```text
k+2d <= 2a-k <= n-1.
```

This is the only role of `J<=0` in the compiler.

### 4.2 Existence and uniqueness of the host gauge

For fixed monic `L` of degree `d`, consider

```text
G |-> ([X^d](LG),...,[X^{d+k-1}](LG)),
G in F[X]_{<k}.
```

Reading coefficients from degree `d+k-1` downward gives a triangular linear
map with diagonal entries one.  It is invertible.  Thus there is a unique
`G` for which `U-LG` satisfies (RH2); replacing

```text
(c_0,U) by (c_0+G,U-LG)
```

does not change `r_0`.  Since `d+k-1<=a-1`, it does not change `deg U=a` or
`ell`.

### 4.3 Uniqueness of the reduced direction

Suppose a second reduced direction presentation has data
`(d',L',T',c_1')`, with `d'<=a-k`.  Equality on `D` makes

```text
N = (c_1-c_1')LL' - TL' + T'L
```

vanish at all `n` domain points.  Its degree is at most

```text
k+d+d'-1 <= 2a-k-1 < n,
```

so `N=0` as a polynomial.  If `c_1-c_1'` were nonzero, the first term would
have degree at least `d+d'`, while the other two have degree at most
`d+d'-1`, impossible.  Hence `c_1=c_1'` and `TL'=T'L`.  Reducedness gives
`L|L'` and `L'|L`; monicity then gives `L=L'`, and consequently
`d=d'` and `T=T'`.

### 4.4 Uniqueness of the canonical numerator

With `L` fixed, two canonical host pairs satisfy

```text
R = L(c_0-c_0') + U-U' = 0 on D.
```

Here `deg R<=a<n`, so `R=0` as a polynomial.  Thus
`U'-U=L(c_0-c_0')`.  Both numerators vanish in coefficient degrees
`d,...,d+k-1`; injectivity of the triangular map in Section 4.2 forces
`c_0=c_0'` and then `U=U'`.

### 4.5 Forward construction

If `Phi_w(S)=z`, the leading coefficient and next `w` coefficients of `U`
and `ell Q_S` agree.  Therefore

```text
deg P_S <= a-w-1 = k+d-1.                             (P1)
```

For `S in F_RH`, the remainder condition gives a unique `psi(S)` because
`T!=0`.  The numerator `P_S-psi(S)T` is divisible by `L`, and (P1) shows
that its quotient has degree at most `k-1`.  Thus (RH4) has degree less than
`k`, and direct substitution gives (RH6).

Because `L` has no root in `D`, (RH6) vanishes exactly at the roots of
`Q_S`, namely `S`.  If `r_1` were explained on `S` by some
`G in F[X]_{<k}`, then

```text
L(G-c_1)+T
```

would vanish at all `a` points of `S` while having degree at most
`k+d-1<=a-1`.  It would be the zero polynomial, forcing the nonzero
polynomial `T` of degree less than `d` to be divisible by `L`, impossible.
This proves support-wise nontriviality.

### 4.6 Converse and witness exhaustivity

Let `(gamma,S,h) in W_a(r)`.  On `S`, define

```text
P = L(h-c_0-gamma c_1)+gamma T.
```

Then `deg P<=k+d-1<a` and `P=U` on every point of `S`.  Hence `U-P` is a
degree-`a` polynomial with leading coefficient `ell` and the `a` roots in
`S`, so

```text
U-P = ell Q_S.
```

Therefore `P=P_S`; top-coefficient comparison gives `Phi_w(S)=z`, and
reduction modulo `L` gives `rho_{L,U}(S)=gamma T`.  Thus
`S in F_RH`, `gamma=psi(S)`, and exact division gives `h=h_S`.  This proves
surjectivity and uniqueness in (RH5).

### 4.7 Occupancy and `LineRay`

For a fixed explanation pair `(gamma,h)`, the polynomial

```text
P = L(h-c_0-gamma c_1)+gamma T
```

is fixed, and `Q_S=ell^{-1}(U-P)` reconstructs `S`.  Hence retained-support
occupancy is one.  By (RH6), every `(gamma,h_S)` has agreement exactly `a`,
so it is one element of `LineRay_F(r_0,r_1;a)`.  Conversely, choose any
`a`-subset of the agreement set of a `LineRay` pair.  The nontriviality
degree argument in Section 4.5 applies to every such subset, so this is an
exact witness and Section 4.6 captures the pair.  This proves (RH7) and also
rules out hidden agreement beyond `a`.  Forgetting `h` gives the literal
multiplicities `m_gamma` and (RH8); no slope injectivity is used.

## 5. Earlier ownership and first-match ledger

Let `E subseteq F` be the union of the **actual slope projections** of any
earlier owners.  Put

```text
F_RH^E = {S in F_RH:psi(S) notin E}.
```

Then the residual incidence is exactly

```text
W_a(r) intersect pi_gamma^{-1}(F\E) = Theta(F_RH^E). (FM1)
```

Thus earlier ownership deletes complete same-slope fibers, not chosen
support representatives.

For any ordered support partition

```text
binom(D,a) = disjoint_union_{lambda in Lambda} Omega_lambda,
```

define

```text
A_lambda = F_RH^E intersect Omega_lambda,
Y_lambda = psi(A_lambda),
Y_lambda^o = Y_lambda \ union_{mu<lambda}Y_mu,
M_lambda = |F_RH intersect Omega_lambda|.
```

Then

```text
Z_a(r)\E = disjoint_union_lambda Y_lambda^o,
|Y_lambda^o| <= |A_lambda| <= M_lambda,
sum_lambda M_lambda = M_RH.                           (FM2)
```

For a challenge set `Gamma subseteq F`, the exact residual count and its
direct certificate are

```text
|(Z_a(r)\E) intersect Gamma|
  = |{gamma in Gamma\E:m_gamma>0}|
  <= min(|Gamma\E|, sum_{gamma in Gamma\E}m_gamma)
  <= min(|Gamma|,M_RH).                               (FM3)
```

Taking `Omega_lambda` to be the canonical partial-occupancy slices gives at
most `(n+1)^4` support labels and exact support add-back.  However,
`M_lambda` remains a **direct rational-host support/LineRay scale**.  This
argument does not identify it with PR #714's realized prefix-image scale
`|Omega_lambda|/|Phi_w(Omega_lambda)|`, does not prove
`M_lambda <= exp(o(n))(1+bar N_lambda)`, and does not prove a global envelope
sum.

## 6. Degree-one specialization and old separating case

Take

```text
L=X-alpha, alpha notin D, T=tau in F^x.
```

Then `w=a-k-1`, every degree-`<1` remainder lies in `F T`, and

```text
F_RH = Phi_w^{-1}(z),
psi(S) = (U(alpha)-ell Q_S(alpha))/tau,                (SP1)
h_S = c_0+psi(S)c_1
      +(P_S-P_S(alpha))/(X-alpha).                     (SP2)
```

The exact collision relation is

```text
psi(S)=psi(S') iff Q_S(alpha)=Q_{S'}(alpha).           (SP3)
```

If the values `Q_S(alpha)` are pairwise distinct, this is exactly the old
separating-pole mechanism of `thm:exact-list-line-bijection` and
`cor:exact-prefix-ray-realization`; no novelty is claimed for that case.
Without separation, (SP1)-(SP3) retain every support and print the actual
same-slope fibers instead of replacing them by an injective model.

## 7. Exact `F_17`, `J=-1` collision census

Take

```text
F=B=F_17, D={0,1,...,12}, n=13, k=3, a=5,
J=5^2-13(3-1)=-1,
L=X-13, T=1, c_0=c_1=0, U=X^5.
```

Here `d=1`, `w=1`, and the forced prefix is zero.  Since the coefficient of
`X^4` in `Q_S` is `-sum_{x in S}x`,

```text
F_RH = {S in binom(D,5):sum_{x in S}x=0 in F_17},
psi(S)=13^5-Q_S(13).
```

The full multiplicity certificate is

```text
0:4, 1:4, 2:5, 3:7, 4:5, 5:6, 6:4, 7:4,
8:6, 9:5, 10:5, 11:7, 12:3, 14:5, 15:3, 16:3.
```

Consequently

```text
supports = LineRay pairs = 76,
distinct slopes = 16,
maximum same-slope fiber = 7,
slope 13 is absent.
```

For the actual earlier-owner set `E={3,11}`, literal slope deletion removes
the two complete fibers of sizes `7` and `7`: `14` witnesses are deleted,
`62` remain, and the residual slope set has size `14`.

The verifier also exercises a genuinely quadratic host on the same row:

```text
L=(X-13)(X-14)=X^2+7X+12, T=X+1, U=X^5,
c_0=2+3X+4X^2, c_1=5+6X+7X^2.
```

It independently finds one reduced direction normal form, one canonical
host, `77` exact witnesses/LineRay pairs, `15` slopes, and maximum slope
fiber `8`, matching a brute-force scan of every slope and every
degree-`<3` explaining polynomial.

## 8. Relation to PR #715's open `LineRay` target

PR #715 correctly separates three objects:

```text
raw exact supports -> (slope,codeword) LineRay pairs -> slopes.
```

For the rational-host lines here, the first arrow has loss one because every
explanation pair has occupancy one and agreement exactly `a`.  Thus

```text
raw exact supports = LineRay pairs = M_RH.
```

The second arrow can have collisions, as the `76 -> 16` finite example
shows.  This exact identification is useful input for the global census, but
it proves no upper model for `M_RH`.  In particular, it does not establish
PR #715's recorded bound on `|LineRay_E|`, does not settle its global
tier-(4) target, and does not close the balanced-core chart-decomposition
problem.

## 9. Reproducibility

Run

```bash
python3 experimental/scripts/verify_canonical_reduced_rational_host_compiler.py
python3 -O experimental/scripts/verify_canonical_reduced_rational_host_compiler.py
```

The script is stdlib-only and deterministic.  It:

1. self-scans its AST and fails if any Python `assert` statement is present;
2. exhausts the integer degree gate through `n=64`;
3. independently brute-forces the complete `F_17` witness incidence over all
   `17` slopes and all `17^3` degree-`<3` explaining polynomials;
4. compares that incidence with the compiler for `d=1` and `d=2`;
5. exhausts every reduced rational direction of denominator degree at most
   `a-k=2` in both cases;
6. exhausts every degree-`<3` host and checks the canonical gauge;
7. verifies occupancy one, exact agreement, support-wise nontriviality,
   slope multiplicities, first match, and the `E={3,11}` deletion.

Because no optimization-sensitive assertion is used, the normal and `-O`
runs execute the same checks.

## 10. Nonclaims and exact remaining wall

This note does not prove any of the following:

- every `J<=0` received line has a reduced rational-host presentation;
- a subexponential extraction of rational-host charts from every remaining
  C7/C8 balanced core;
- a decomposition of every higher-dimensional core into such charts;
- a comparison of `M_RH` or `sum M_lambda` with PR #714's image scale, the
  complete profile envelope, or a deployed finite budget;
- the open global `LineRay` census recorded by PR #715;
- slope injectivity, occupancy gain greater than one, or a scale-one theorem;
- C3, C9, outer UNIF, the phase-sensitive image-denominator input, Grand
  List, Grand MCA, or either official destination;
- an adjacent crossing `U(a_0+1) <= B* < L(a_0)`.

The exact next wall is **rational-host extraction plus aggregate payment**.
For every `J<=0` line and every live first-match partial-occupancy slice, one
must extract at most `exp(o(n))` line-determined reduced rational-host charts
and route the complement to named transverse/nonlinear owners.  One must then
prove that the sum of their exact `M_lambda` scales, together with the
transverse residual budgets, fits the complete C7/C8 profile envelope (or the
literal finite challenge denominator).  The theorem above proves only the
single-chart incidence compiler after such a chart has already been found.
