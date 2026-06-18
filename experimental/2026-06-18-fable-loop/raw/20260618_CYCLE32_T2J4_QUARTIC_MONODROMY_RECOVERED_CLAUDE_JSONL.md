I attempted to run the decisive monodromy experiment (the kernel is what every prior cycle lacked), but code execution is denied in this harness, exactly as in Cycles 29–31. So this remains a source-grounded audit by hand. I read the Cycle 29/30/31 audits, both certificates, the recovered Cycle 29/31 JSONL, and the Cycle 30 scanner (with its Cycle 11 finite-field backend). The result is a correction plus a reduction, not a full solve.

---

AUDIT

## Field ledger (kept separate)

- `q_gen = p`; `B = F_p`; `F = F_{p^2} = B(alpha)`, `alpha^2 = theta` nonsquare; `q_line = |F| = p^2`; `q_chal` unused.
- `D = F_p`, `n = p`; restricted `t = sigma = 2`, `j = n-a = r-t = 4`; off `R0` (`kappa = u wedge b != 0`); source-valid separated `E = X^2+cX+d` nonzero on `F_p`, `gcd(E,E^tau)=1`; `c_b != 0` on that branch.
- `A = F[X]/E`, `dim_F A = 2`, `dim_B A = 4`. Residue-line / bad-slope incidence only. No promotion to corrected-reserve, MCA, list-decoding, CA, line-decoding, curve-MCA, protocol, SNARK, or Proximity Prize.

## Headline judgments

1. Cycle 31's choice of invariant is correct: quartic monodromy of `L_{tau(z)}` is the right next object. Keep `W-F1-AA-RES-T2J4-QUARTIC-MONODROMY-S4`.
2. Cycle 31's reduction contains a genuine base-field error that the prompt's task 1 flagged as "not cosmetic." The family is **not** a one-variable function field `B(z)` or `F(z)`. It is a **two-dimensional `B`-parameter family over the affine plane `A^2_B` with coordinates `(z_0,z_1)`**. The `p^2` in the count is `|A^2(F_p)|`, not `|F_{p^2}|`. They coincide numerically, which is the only reason Cycle 31's one-variable Chebotarev story produced the right magnitude `(1/24)p^2` from the wrong model.
3. No source invariant forces an `O(p)` collapse. The affine/quadric layer (Cycles 28–30) provably gives a generically unique, generically injective preimage `z -> tau(z)` with **2-dimensional image**, so it cannot pin the count below `Theta(p^2)`. The only surviving route to sub-`Theta(p^2)` is monodromy degeneracy (arithmetic-vs-geometric), which the scan data refute. This does not bank `Theta(p^2)`; the splitting density itself is exactly the uncomputed monodromy invariant.

## Task 1 — the base field (the decisive correction)

ROUTE_CUT on the framing "over the function field `B(z)` (resp. `F(z)`)" in the Cycle 31 JSONL.

Write `z = z_0 + alpha z_1`, `z_0,z_1 in B`. Multiplication `m_z` on `A` is `B`-linear and
```text
m_z = z_0 * I_4 + z_1 * A_alpha,   A_alpha = fixed B-matrix of mult-by-alpha on A ≅ B^4.
```
Each Cycle 29 column is `C_i(z) = P_i - m_z(R_i) = P_i - z_0 R_i - z_1 (alpha R_i)`, a `B^4`-vector **affine-linear in `(z_0,z_1)`**. Hence:
```text
M(z) in B^{4x4} has degree-1 entries in (z_0,z_1);
Delta(z) := det_B M(z) is degree <= 4 in (z_0,z_1);
tau_i(z) = det_B M_i(z) / Delta(z),  numerator degree <= 4 in (z_0,z_1).
```
Cross-check with Cycle 29's banked top symbol: `det_B(m_z) = N_{F/B}(z)^2` and `N(z) = z_0^2 - theta z_1^2` is degree 2 in `(z_0,z_1)`, so `N(z)^2` is degree 4 — exactly `deg Delta`. Consistent.

Correct model: a genuinely **bivariate** rational map
```text
tau : A^2_B  -->  A^4_B = {monic quartics},   tau(z_0,z_1) in F_p^4,
```
and the wall counts `F_p`-points of `A^2_B` where `L_{tau} = X^4 - tau_1 X^3 + tau_2 X^2 - tau_3 X + tau_4` splits into four distinct `B`-roots. The right "Chebotarev" is Lang–Weil + Frobenius classes for an `S_4`-cover of the surface `A^2_B`, giving `(density)*p^2 + O(p^{3/2})` for a geometrically irreducible cover — not a one-variable Weil bound. Cycle 31's `O(p^{3/2})` error term and `1/24` constant survive only under this corrected two-variable reading.

## Task 2 — exact discriminant/resolvent objects from the Cycle 29 columns

These are fully determined symbolically (no missing mounted formula for *writing* them; what is missing is an explicit numeric source-valid instance to *evaluate* them). By Cramer with `Delta = det_B M(z)`:
```text
tau_i(z) = det_B M_i(z) / Delta(z),   M_i = M with column i replaced by -C_0(z).
```
With `b_coef=-tau_1, c_coef=tau_2, d_coef=-tau_3, e_coef=tau_4`, the standard invariants are:
```text
Resolvent cubic:
R(y) = y^3 - tau_2 y^2 + (tau_1 tau_3 - 4 tau_4) y - (tau_1^2 tau_4 - 4 tau_2 tau_4 + tau_3^2).

disc_X L  = degree-6 polynomial in (tau_1,...,tau_4)  (= disc of the resolvent cubic R).
```
Substituting `tau_i = det_B M_i / Delta` clears to:
```text
disc_X L_{tau(z)} = P_disc(z_0,z_1) / Delta(z)^6,     deg P_disc <= 24 in (z_0,z_1),
R(y; z) with coefficients in B[z_0,z_1] localized at Delta(z).
```
`C_0(z)` is the `tau`-free part of `iota - z mu`: from the Cycle 29 quotient, `C_0 = (u - z b)*xi_4 - ell*[W_{n-1}xi_3 + W_{n-2}xi_2 + W_{n-3}xi_1 + W_{n-4}xi_0]_E`, with `R_i = (-1)^i b xi_{4-i}` and `P_i` as listed in the Cycle 29 JSONL. Nothing else is needed to assemble `R(y;z)` and `disc_X L_{tau(z)}` symbolically. What is genuinely missing: a reduced numeric instance `(P_i, R_i)` over a concrete prime, which needs the disabled kernel or a hand instance.

## Task 3 — prove / refute / reduce `S_4` (REDUCE)

I can neither prove nor refute `G = S_4` source-only; I reduce it to two checkable conditions over the **two-variable** base:
```text
G_geom( L_{tau(z)} / \bar B(z_0,z_1) ) = S_4
  <=>  (a) disc_X L_{tau(z)} is a non-square in \bar B(z_0,z_1),    [G ⊄ A_4]
  AND  (b) resolvent cubic R(y;z) is irreducible over \bar B(z_0,z_1). [3 | |G|, transitive]
```
Both must be read **geometrically** (over `\bar B`), so the count's constant field is controlled and arithmetic monodromy `=` geometric monodromy. Cycle 31 omitted the `\bar B` (geometric) qualifier; over `B(z)` alone one cannot separate a true small group from a constant-field artifact, and that artifact is precisely the `O(p)`-vs-`Theta(p^2)` hinge (Task 5).

Crucially: refuting `O(p)` does **not** require full `S_4`. It requires only that the arithmetic monodromy's totally-split (identity) Frobenius class be realized with positive proportion. Any transitive `G in {S_4, A_4, D_4, C_4, V_4}` with `geometric = arithmetic` already yields a positive split density `>= 1/|G| >= 1/24`, hence `Theta(p^2)`. `S_4` only fixes the constant to `1/24`.

## Task 4 — smallest checker / certificate

Two minimal certificates, in increasing strength:

(C1) Frobenius cycle-type histogram, one instance. Fix one source-valid `(W,E,b)` off `R0` with `c_b != 0`. For every `z in F` (equivalently every `(z_0,z_1) in F_p^2`): solve `M(z) tau = -C_0(z)` over `B`, form `L_{tau(z)}`, discard `Delta(z)=0` and `disc=0`, and record the factorization type over `F_p`. Compare the empirical proportions against the `S_4` class fractions
```text
id : 6/24-... -> {1^4:1/24, 2 1^2:6/24, 2^2:3/24, 3 1:8/24, 4:6/24}.
```
A match across `p in {31,53,101,...}` certifies `G_arith = S_4` (and that `id` is realized, killing `O(p)`). This is the single decisive run all prior cycles were blocked from doing.

(C2) Symbolic non-degeneracy, smaller. At a handful of random `(z_0,z_1)` over moderate primes, check `disc_X L_{tau(z)}` is a non-square and `R(y;z)` is irreducible over `F_p`; persistence across several `(z,p)` is a Frobenius-style certificate of (a)+(b), i.e. geometric `S_4`.

Both are pure finite-field computations on the Cycle 11 backend extended by the explicit `M(z),C_0(z)` columns above; neither needs anything beyond a working kernel.

## Task 5 — the only invariant that could force `O(p)`

Not a rational-root/quadric collapse. The affine layer is banked the other way:

BANKABLE_LEMMA (no-affine-collapse). Off the degree-`<=4` curve `Delta(z)=0`, `tau(z) in B^4` is the unique preimage (Cycle 29), and `z -> tau(z)` is generically injective: if `tau(z)=tau(z')` then `(z-z') mu = 0` in `A` with `mu = b*lambda != 0` (source-valid: `b != 0`, `lambda=[L_T]_E` a non-zero-divisor), forcing `z=z'` whenever `A` is a domain / `mu` is a non-zero-divisor. Hence the image `tau(F)` is **2-dimensional** (`~p^2` points). Therefore the two `B`-quadrics of Cycle 30 cut out the image curve-of-points but impose **no** further `O(p)` thinning; `C2 = #(tau(F) cap TSD)` is bounded below only by the splitting density, not by the affine geometry.

Consequence: the unique remaining mechanism for sub-`Theta(p^2)` is **monodromy degeneracy** — arithmetic monodromy whose totally-split Frobenius class is empty (a constant-field extension forcing all four roots into `F_{p^2} \ F_p`), i.e. geometric `!=` arithmetic monodromy. That, and only that, is the exact `O(p)`-forcing invariant. The Cycle 30/31 scans (`C2 > 0`, `avg_C2/p^2` rising `0.011 -> 0.037`, `max_C2 ~ p^2/24`) are inconsistent with an empty split class, so `O(p)` is experimentally refuted though not source-proved.

## Route to a full solve?

Yes, and it is now narrow and concrete. Full solve of this wall = execute (C1) on one source-valid instance to certify `G_arith = S_4` (or identify the transitive subgroup), then invoke Lang–Weil/Frobenius over the **surface** `A^2_B` to bank
```text
C2 = (1/|G|) p^2 + O(p^{3/2}) = Theta(q_line),   restricted t=2, j=4, off R0, c_b != 0, source-valid separated branch.
```
The next exact lemma is therefore not "monodromy over `B(z)`" but:

Lemma (target, corrected base). The universal quartic `L_{tau(z)}`, viewed over the **two-variable** function field `\bar B(z_0,z_1)` with `tau_i = det_B M_i / Delta` from the Cycle 29 columns, has geometric Galois group `S_4`, certified by (a) `disc_X L_{tau(z)}` a non-square and (b) `R(y;z)` irreducible over `\bar B(z_0,z_1)`; and arithmetic `=` geometric monodromy (no constant-field extension), certified by the (C1) cycle-type histogram matching `S_4` proportions.

## Dependencies

- Cycle 29: square `4x4` `B`-system, `tau(z)=M^{-1}(-C_0)`, top symbol `-N(kappa)N(z)^2 Q_4`, columns `C_i = P_i - z R_i`, `R_i=(-1)^i b xi_{4-i}`.
- Cycle 28: `Q_4` source-valid nonzero (so `Delta` not identically zero; `tau` defined off a degree-`<=4` curve).
- Cycle 30: the `tau_4`-quadratic `Phi(tau)=kappa N_{A/F}(lambda) - (ell[Q_S]_E) wedge_F (b lambda)`; EXPERIMENTAL scan.
- Cycle 31: correct identification of monodromy as the invariant; its `B(z)/F(z)` framing is cut here.
- Cycle 11/12: quotient form, `line_scalar`, `residue2`, finite-field backend used by the scanner.

## Hidden assumptions

- Generic injectivity of `z -> tau(z)` uses `mu=b lambda` a non-zero-divisor; in the split branch `A ≅ F x F` a measure-`O(p)` set of `z` can collide — does not change the `p^2` scale.
- The `1/24` constant assumes geometric `S_4` AND geometric `=` arithmetic; a smaller transitive `G` changes the constant, not the `Theta(p^2)` order, provided the totally-split class is realized.
- `disc`/`R` degrees (`<=24/Delta^6`, cubic) are the generic bounds; a source-valid instance could lower them via cancellation.
- The Lang–Weil error `O(p^{3/2})` requires geometric irreducibility of the `S_4`-cover of `A^2_B`; unproved here.
- No finite checker was run (kernel denied), so (C1)/(C2) are specified, not executed.

## Rejected overclaims

- Not a proof that `G = S_4`; not a proof of a Chebotarev density constant.
- Not a banked `Theta(q_line)` counterpacket; only a corrected reduction + the exact certificate needed.
- Not a proof of `O(p)` (refuted in mechanism and data, not source-proved impossible).
- Not a one-variable `B(z)`/`F(z)` statement — that framing is explicitly cut.
- No corrected-reserve, MCA, list-decoding, CA, line-decoding, curve-MCA, protocol, `q_gen`/`q_line` merge, SNARK, or Proximity Prize consequence. Sub-reserve (`eta = 2/n`), local only.

## Next exact wall

```text
W-F1-AA-RES-T2J4-QUARTIC-MONODROMY-S4  (base corrected to A^2_B)
```
Execute checker (C1) on one source-valid instance to certify `G_arith` (target `S_4`) via the Frobenius cycle-type histogram, and/or (C2) to certify geometric `(disc nonsquare, R irreducible)` over `\bar B(z_0,z_1)`. Then bank `C2 = (1/|G|)p^2 + O(p^{3/2})` by Lang–Weil over the surface. The single remaining counterpacket-blocker is a constant-field extension making geometric `!=` arithmetic monodromy with empty totally-split class — the one invariant that, if present, would restore an `O(p)` count.
