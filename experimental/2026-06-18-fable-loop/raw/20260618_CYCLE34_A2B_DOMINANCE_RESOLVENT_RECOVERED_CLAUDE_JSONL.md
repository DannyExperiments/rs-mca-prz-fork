I have the four required audits, the Cycle 32 histogram checker and its certificate, the Cycle 28 `Q_4` proof, the Cycle 11 utility API, and the Cycle 33 recovered reasoning. Code execution is blocked in this harness, so I verified the load-bearing claims analytically against the recorded data rather than by running new scans. Here is the result.

---

## Ledger (kept separate, not merged)

`q_gen = p`; `B = F_p`; `F = F_{p^2} = B(alpha)`; `q_line = |F| = p^2`; `q_chal` unused. `D = F_p`, `n = p`, `t = sigma = 2`, `j = n-a = r-t = 4`, off `R0`, source-valid separated `E = X^2+cX+d` nonzero on `F_p`, `c_b != 0`, Cycle 28/29 top-symbol nonvanishing in force. Scope: residue-line / bad-slope incidence only. Nothing below is promoted to corrected-reserve, MCA, CA, list-decoding, line-decoding, curve-MCA, protocol, SNARK, or prize status.

---

## Task 1 — generic `B`-Jacobian rank of `tau`

`PROOF` — the rank is exactly two, and the route to an `O(p)` collapse *through dimension collapse* is cut.

Set up the graph instead of the inverse. The Cycle 29/30 equation is, for `z in F` and `tau in B^4`,

```text
G(z,tau) := (u - z b)·lambda(tau) - ell·[Q_S(tau)]_E = 0   in A = F[X]/E,
```

with `u=[W]_E`, `ell=[L_D]_E`, `b=bnum_res`, `lambda(tau)=xi_4 - tau_1 xi_3 + tau_2 xi_2 - tau_3 xi_1 + tau_4` (affine-linear in `tau`), `[Q_S(tau)]_E` affine-linear in `(tau_1,tau_2,tau_3)`. `G` is affine-linear in `tau` and degree one in `z`, so it is simultaneously:

- the square system `M(z)tau = -C_0(z)` (fix `z`, solve for `tau`): defines `psi(z)=tau(z)=M(z)^{-1}(-C_0(z))` off `Delta=0`;
- linear in `z` (fix `tau`, solve for `z`): `z·(b·lambda(tau)) = u·lambda(tau) - ell·[Q_S(tau)]_E` in `A`.

Define the rational map `chi: A^4_B --> F`, `chi(tau) =` the unique scalar `z` with `u·lambda - ell·[Q_S]_E = z·(b·lambda)`, read off any `F`-coordinate where `b·lambda(tau) != 0`. `chi` is a ratio of two `F`-linear forms in `tau` — a genuine rational map, no inseparable operation.

Claim: `chi ∘ psi = id` as rational maps on `A^2_B`. For generic `z`, `psi(z)` solves `M(z)tau+C_0(z)=0`, i.e. `G(z,psi(z))=0`, i.e. `u·lambda(psi(z)) - ell·[Q_S(psi(z))]_E = z·(b·lambda(psi(z)))`. Where `b·lambda(psi(z)) != 0` (a dense open set, since `b != 0` and `lambda(psi(z))` is not identically annihilated), the collinearity scalar is unique and equals `z`. Hence `chi(psi(z)) = z`. ∎

Consequence in characteristic `p`: because `chi` is a bona fide rational map (this is exactly what defeats the Frobenius `x↦x^p` pseudo-counterexample, which has no rational inverse), functoriality of the cotangent map gives `D chi|_{psi(z)} · D psi|_z = I_2` generically. A `4×2` Jacobian with a left inverse has full column rank, so

```text
generic rank_B( D psi ) = 2.
```

`psi` is therefore generically injective and separable, birational onto its image, and the image is 2-dimensional. As a corollary the image is (the closure of) Cycle 30's quadric `{Phi(tau)=0}`, since `Phi(tau)=(u·lambda - ell[Q_S]_E) ∧_F (b·lambda)` is precisely the collinearity obstruction that `psi(z)` satisfies.

`ROUTE_CUT` — the "rank ≤ 1 / image collapses to a curve" explanation for a possible `O(p)`, floated in Cycle 30 and named as the sharpest obstruction in Cycle 33 Task 5, is eliminated. The split count is a genuine 2-dimensional surface count, not a 1-dimensional Lang–Weil count. Any residual `O(p)` can now come *only* from the monodromy/transitivity or constant-field layer, not from dimension.

`BANKABLE_LEMMA`

```text
L-T2J4-A2B-DOMINANCE.
In the restricted t=2, j=4 A^2_B model on the source-valid branch
(kappa != 0, c_b != 0, Cycle 29 top symbol != 0), the rational map
psi: A^2_B --> A^4_B, z |-> tau(z)=M(z)^{-1}(-C_0(z)), has generic
B-Jacobian rank 2, is birational onto its image, and that image is the
Cycle 30 quadric {Phi=0}. Dependencies: Cycle 29/30 affine-linear column
structure; b != 0; lambda(tau(z)) not identically zero; cotangent
functoriality. No monodromy input is used.
```

This is independent of, and complementary to, Cycle 33's `L-T2J4-A2B-SINGULAR-OP` (the `Delta=0` locus contributes `≤ 4p`). Together: the singular boundary is `O(p)` and the off-curve image is a true surface.

---

## Task 2 — cubic resolvent and discriminant square class

`PROOF` (conditional reduction) — for `L_tau = X^4 - tau_1 X^3 + tau_2 X^2 - tau_3 X + tau_4` with the stated resolvent `R(y)`, the standard quartic criterion gives over any field of char `≠ 2,3`:

```text
G_geom = S_4   <=>  R(y) irreducible over \bar F_p(z_0,z_1)
                    AND disc_X L_tau a nonsquare in \bar F_p(z_0,z_1).
R irreducible, disc square            => A_4.
R has exactly one root, disc nonsquare => D_4 or C_4.
R splits, disc square                  => V_4.
```

What I can establish rigorously now:

- Square-class normalization. Substituting `tau_i = det_B M_i / Delta` and clearing denominators, `disc_X L_tau = disc_num(z_0,z_1) / Delta^6`. Since `Delta^6=(Delta^3)^2` is a perfect square, the square class of `disc_X L_tau` equals the square class of the bivariate polynomial `disc_num`, `deg ≤ 24` (this matches Cycle 32's degree-24 count). So the `A_4`-vs-not test reduces to: is `disc_num` a perfect square in `F_p[z_0,z_1]` (resp. `\bar F_p[z_0,z_1]`)? A finite, decidable bivariate test.

- `G_arith = S_4` is exhibited per prime by the recorded histogram, and this part is not merely heuristic: each squarefree factorization type of `L_{tau(z)}` over `F_p` at a concrete point `(z_0,z_1)` IS the cycle type of the Frobenius at that point, an element of `G_arith`. The certificate shows, at `p=29`, points of type `4` (a 4-cycle), type `211` (a single transposition), and type `13` (a 3-cycle). A transposition together with a 4-cycle generate `S_4`. Hence for each such prime `G_arith = S_4`. This is an arithmetic, per-prime statement, not yet the geometric "all large `p`" statement.

What remains genuinely open: `G_geom = S_4` over `\bar F_p(z_0,z_1)` (the all-large-`p` geometric group), and `G_arith = G_geom` (no constant-field extension). Those require the explicit `tau_i(z)` (Cramer over the `4×4` affine-linear `M(z)`), which I cannot evaluate without code here.

`EXPERIMENTAL` — the histogram is a clean `S_4` fingerprint, and it points away from `O(p)`, contrary to the earlier Cycle 30 lean. Comparing squarefree densities at the largest recorded prime `p=29` (squarefree total 783) to the `S_4` cycle index:

```text
type    data (p=29)   S_4 cycle index
1111    0.0421        0.0417   (1/24)
211     0.2465        0.2500   (6/24)
13/31   0.3308        0.3333   (8/24)
22      0.1290        0.1250   (3/24)
4       0.2516        0.2500   (6/24)
```

Every class agrees to within `0.004`. The `1111` density tracks `1/24` and is rising across `p=7..29`, not decaying to `0`. This is consistent with `G_arith=G_geom=S_4`, split density `1/24 > 0`, hence a `Theta(p^2)=Theta(q_line)` slope family — and is inconsistent with an `O(p)` collapse. It is evidence, not a certificate; a finite-prime histogram can certify neither a geometric group nor the absence of a constant-field extension (the audits are correct to refuse promotion).

No `COUNTERPACKET` is banked: positive density is still unproven.

---

## Task 3 — the constant-field-extension test actually needed

`AUDIT` — the needed test is whether the field of constants of the splitting field of `L_tau` over `F_p(z_0,z_1)` is exactly `F_p`. Concretely it is two geometric-irreducibility checks, both reading off objects already named:

```text
(C1) disc_num(z_0,z_1) is geometrically irreducible / its square-free part
     defines a geometrically irreducible double cover  (=> the A_4 vs S_4
     discriminant cover does not acquire new constants);
(C2) the resolvent cubic R(y) over F_p(z_0,z_1) stays irreducible over
     \bar F_p(z_0,z_1)  (=> the order-3 layer gains no constants).
```

If both hold, `G_arith = G_geom`, and surface Chebotarev / Lang–Weil gives `#{split (z_0,z_1) in A^2(F_p)} = p^2/|G_geom| + O(p^{3/2})`, i.e. `p^2/24 + O(p^{3/2})` for `S_4`. Does current data rule out a constant-field extension? No, not rigorously. But the histogram is mild evidence against one: a constant-field extension of the identity layer would typically either suppress the `1111` class (pushing its density below `1/24`) or rescale it by a rational factor; the observed density sits right at `1/24`. This must stay `EXPERIMENTAL`. The only way to discharge `(C1)`,`(C2)` for all large `p` is the symbolic computation, since they are statements over `\bar F_p(z_0,z_1)`.

---

## Task 4 — sharpest next wall and exact checker spec

`EXACT_NEW_WALL`

```text
W-F1-AA-RES-T2J4-A2B-GEOMETRIC-S4
```

With rank 2 now proved and `G_arith=S_4` exhibited per prime, the single remaining gate between the current state and a `Theta(q_line)` counterpacket seed is the geometric/constant-field layer: prove `G_geom` is transitive (seed-sufficient) — ideally `= S_4` — and `G_arith=G_geom`, by a symbolic computation valid for all large `p`.

`EXPERIMENTAL` — local checker spec precise enough for Codex (pure symbolic, all-large-`p`; reuses the Cycle 11/32 finite-field and polynomial utilities, but now over the rational function field `F_p(z_0,z_1)` for a few moderate primes `p in {11,13,17,19,23,29}` as a uniform-pattern probe, plus an exact bivariate run):

```text
1. Build the 4x4 matrix M(z) and vector C_0(z) symbolically as entries
   affine-linear in (z_0,z_1):
     z = z_0 + alpha*z_1;  m_z = z_0 I_4 + z_1 A_alpha  (A_alpha from Cycle 32);
     columns C_i(z) from d/dtau_i of (u - z b) lambda - ell [Q_S]_E,
     using the Cycle 29 derivative table
       dlambda/dtau = (-xi_3, xi_2, -xi_1, 1),
       dQ_S/dtau_1 = -(W_{n-1}X^2 + W_{n-2}X + W_{n-3}),
       dQ_S/dtau_2 =  (W_{n-1}X + W_{n-2}),  dQ_S/dtau_3 = -W_{n-1}.
2. Delta = det_B M(z); tau_i = det_B M_i(z)/Delta  (Cramer), as elements of
   F_p(z_0,z_1).  Assert deg Delta = 4 and TopSym(Delta) = -N(kappa) N(z)^2 Q_4
   (Cycle 29 cross-check).
3. Form R(y) and disc_X L_tau with these tau_i; clear denominators:
     disc_X L_tau = disc_num / Delta^6,  deg disc_num <= 24.
4. GEOMETRIC TESTS (the actual certificate):
   (a) bivariate-factor disc_num over F_p and over a few F_{p^k};
       square-class: is disc_num a perfect square?  (square => G in A_4).
   (b) factor R(y) over F_p(z_0,z_1): treat as cubic in y with coefficients
       in F_p[z_0,z_1]; test irreducibility, and test whether any factor
       acquires constants over F_{p^k} (constant-field probe).
   (c) Jacobian cross-check of Task 1: confirm rank_B(d tau/d(z_0,z_1)) = 2
       at random non-singular points (must always be 2; a single rank-<=1
       point that is generic would refute L-T2J4-A2B-DOMINANCE).
5. Report (G_geom candidate, G_arith candidate, equal?) with the cycle-index
   table as a consistency check against the existing histogram.
```

Decision rule: `disc_num` nonsquare and `R` irreducible over `\bar F_p(z_0,z_1)` with no constant-field gain ⟹ `G_geom=G_arith=S_4` ⟹ `Theta(p^2)` seed (`ROUTE_CUT` against `O(p)`). Any geometric reducibility of `R`/`L_tau` or a constant-field gain ⟹ smaller density or a possible `O(p)` mechanism — record exactly which.

`AUDIT` — provenance caveat: every Cycle 29–33 source file carries `HARNESS_MALFORMED_VISIBLE_TERMINAL`; I used only the recovered structured content and the committed checker code, and I re-derived the Task 1 proof from the equations directly rather than trusting any scrape. The histogram numbers are quoted from the committed certificate file, not regenerated.

---

## Do you see a route to a full solve?

Yes, conditionally, for the restricted `t=2, j=4` sub-reserve wall (not the prize). The structure has narrowed to a single decidable gate:

- Cycle 33 proved the singular boundary is `O(p)` (`L-T2J4-A2B-SINGULAR-OP`).
- This cycle proves the off-curve image is a genuine surface, generic Jacobian rank 2, birational onto Cycle 30's quadric (`L-T2J4-A2B-DOMINANCE`), cutting the dimension-collapse route in char `p`.
- The remaining off-curve question is purely the geometric monodromy + constant-field layer, and `G_arith=S_4` is already exhibited per prime with a histogram matching the `S_4` cycle index to within `0.004` at `p=29`.

Next exact lemma to attempt:

```text
L-T2J4-A2B-GEOM-TRANSITIVE (seed-sufficient form):
prove L_tau is geometrically irreducible over \bar F_p(z_0,z_1) with
G_arith = G_geom, by showing disc_num is a nonsquare and the resolvent
cubic R(y) is irreducible and constant-field-stable over \bar F_p(z_0,z_1)
— via the explicit Cramer tau_i(z) of the step-4 checker.
```

Proving transitivity plus no-constant-extension yields split density `1/|G_geom| > 0`, hence a source-valid `Theta(q_line)` slope family on this restricted branch — a counterpacket *seed*, with `L-T2J4-A2B-SINGULAR-OP` already disposing of the boundary. Full `S_4` would pin the constant to `1/24`; a smaller transitive group (`V_4`,`C_4`,`D_4`,`A_4`) would give a larger constant but the same `Theta(p^2)` conclusion. The construction needed is the symbolic resolvent/discriminant over `F_p(z_0,z_1)`, not another finite histogram.
