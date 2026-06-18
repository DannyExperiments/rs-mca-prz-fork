I have what I need. Note: code execution is disabled in this harness (the `executeCode` permission was denied and there is no shell tool), so I cannot run the finite checker myself. The audits flag the same constraint for Cycles 24–29. I will therefore deliver the exact reduction I derived by hand from the source-valid `c11`/`c12` conventions, the dimension/density analysis, and a runnable checker spec — and I will mark clearly what is proven versus heuristic.

---

EXACT_NEW_WALL

`W-F1-AA-RES-T2J4-SPLIT-QUARTIC-GATE` does not close as `O(p)`. I reduce it to an explicit two-quadric / split-locus incidence problem, show the affine layer alone gives only the trivial `O(p^2)` bound, and show the honest expectation is `Theta(p^2)=Theta(q_line)` (a counterpacket seed), gated on one geometric fact I cannot certify without running the checker.

## Field and parameter ledger

- `B = F_p`, `q_gen = p`. `F = F_{p^2} = B(alpha)`, `alpha^2 = NR` nonsquare. `q_line = |F| = p^2`. `q_chal` unused, kept separate.
- `D = F_p`, `n = p`. `t = sigma = 2`, `j = n-a = r-t = 4`; `eta = 2/n`, sub-reserve.
- `A = F[X]/E`, `E = X^2+cX+d` source-valid (nonzero on `F_p`), separated (`gcd(E,E^tau)=1`); `xi_m=[X^m]_E`, `u=[W]_E`, `b=[Bnum]_E`, `ell=[X^p-X]_E`, `kappa = u wedge_F b != 0` (off `R0`), `c_b != 0`.
- `wedge_F(x,y) = x_0 y_1 - x_1 y_0` is the alternating `F`-area form on `A ~= F^2` in basis `{1,xi}`.

Residue-line / bad-slope incidence calculation only. Not list-decoding/CA/MCA/line-decoding/curve-MCA/protocol/SNARK/Proximity-Prize, no `q_gen`/`q_line` merge.

## 1. Exact algebraic split condition (item 1)

From the banked `c11`/`c12` incidence test, a co-support 4-subset `T = D\S` (always a **distinct** 4-subset of `F_p` by construction) realizes a bad slope iff, with `W = L_S Q_S + I_S`, `L_S = L_D/L_T`, `L_D = X^p-X`:

```text
[I_S]_E  =  z * b   for some z in F,
```

i.e. `[I_S]_E` and `b` are `F`-collinear in the 2-dimensional `F`-space `A`. Multiplying by the unit `lambda = [L_T]_E` (a unit because `E` has no `F_p`-root, so `E` is coprime to every `X-x`, `x in T`) and using `[I_S]_E * lambda = iota` gives the clean source-correct gate

```text
Phi(T) := iota wedge_F mu = 0,
   iota = u*lambda - ell*[Q_S]_E,   mu = b*lambda,   lambda = [L_T]_E.
```

This is the single `F`-valued equation behind `line_scalar`. Two structural facts:

- **The "splits into 4 distinct roots in F_p" requirement is the parametrization, not the gate.** Writing `tau=(tau_1,...,tau_4)=e(T)` (elementary symmetrics), `P_z(X)=X^4-tau_1X^3+tau_2X^2-tau_3X+tau_4 = L_T`, which splits into 4 distinct `F_p`-roots **automatically** because `T subset F_p` is a distinct 4-set. Equivalently, in the slope→tau direction (off the curve), `P_z` splits distinct iff `P_z | X^p-X`. The real cut is `Phi=0`.
- `lambda`, `[Q_S]_E` are affine in `tau` (`Q_S` depends on `tau_1,tau_2,tau_3` only; `lambda` on all four), so **`Phi` is a quadratic form in `tau`** — one `F`-quadric = two `B`-quadrics.

Closed form (the useful one). Since `(u lambda) wedge_F (b lambda) = N_{A/F}(lambda)*(u wedge_F b) = kappa*N_{A/F}(lambda)`:

```text
Phi(tau) = kappa * N_{A/F}(lambda)  -  (ell*[Q_S]_E) wedge_F (b*lambda).
```

Splitting `lambda = lambda' + tau_4`, `lambda' = xi_4 - tau_1 xi_3 + tau_2 xi_2 - tau_3 xi_1` (independent of `tau_4`), and `[Q_S]_E` independent of `tau_4`:

```text
Phi = kappa*tau_4^2
    + tau_4*( kappa*Tr_{A/F}(lambda') - (ell[Q_S]_E) wedge_F b )
    + ( kappa*N_{A/F}(lambda') - (ell[Q_S]_E) wedge_F (b lambda') ).
```

The leading `kappa*tau_4^2` term is the affine-layer shadow of the Cycle 29 top symbol `TopSym(det_B M) = -N(kappa)N(z)^2 Q_4`: same locator-controlled, source-valid-nonzero leading coefficient (`kappa != 0`).

## 2-3. The slope count is not O(p); it is a split-locus incidence (items 2,3,5)

Let `V = { tau in A^4(B) : Phi(tau)=0 }`, the intersection of the two `B`-quadrics (the `B`-components of the single `F`-quadric `Phi`). Three exact steps:

(a) **Off-curve bijection.** By Cycle 29, off the noninvertibility curve `det_B M(z)=0` (`<= 4p` slopes, kept separate per item 5) the map `z -> tau(z)` is a well-defined rational map, and `M(z)tau + C_0(z)=0` is affine in `z`, so `tau` determines `z`. Hence `z <-> T` is a **bijection** between realized off-curve slopes and bad distinct 4-subsets. Therefore

```text
C2 = #{ distinct 4-subsets T subset F_p : Phi(e(T)) = 0 }  +  O(p).
```

(b) **Dimension.** `Phi=0` is two `B`-equations in four `B`-variables. Eliminating the single `B`-unknown `tau_4` between the two `B`-components (the `tau_4^2` coefficient is `kappa != 0`, so the resultant is nondegenerate) yields **one** `B`-equation in `(tau_1,tau_2,tau_3)`. Thus `V` is a **2-dimensional** variety of bounded degree (`<= ` a few). The affine/consistency layer that gave `C2<=4p` at `j=3` (codim-1 obstruction `Q`) is **gone**: at `j=4` the system is square, the determinant is the uniqueness determinant, and `Phi=0` is codim-2 in a 4-space, i.e. dimension `2`, not `1`.

(c) **Count = split-distinct quartics on `V`.** As `T` ranges over `C(p,4) ~ p^4/24` distinct 4-subsets, `e(T)` ranges bijectively over all **totally-split-distinct** monic quartic coefficient tuples. So

```text
C2 = #{ totally-split-distinct quartics whose tau lies on V }  +  O(p).
```

`|V(F_p)| ~ p^2` (Lang-Weil, if `V` geometrically irreducible of dim 2). Being totally split with distinct `F_p`-roots is the Frobenius/Chebotarev condition "factorization type `(1,1,1,1)`", which holds for a `1/24` proportion of quartics when the universal quartic `X^4 - tau_1 X^3 + tau_2 X^2 - tau_3 X + tau_4` restricted to `F_p(V)` has Galois group `S_4`. Under that genericity,

```text
C2 ~ |V(F_p)| / 24 ~ p^2/24 = Theta(p^2) = Theta(q_line).
```

So **the `O(p)` bound is implausible at `j=4`**, and the natural value saturates `q_line`. This is precisely the sub-reserve counterpacket seed Cycle 28/29 flagged. It is **not** yet a counterpacket: it needs (i) a growing-prime family of source-valid `(E, Bnum, W)` for which `V` is geometrically irreducible of dimension 2, and (ii) the `S_4` Galois condition on `F_p(V)` (or weaker: positive lower density of split type), neither of which I certify here.

The only way `C2=O(p)` survives is if `V` is **non-generic** for splitting: e.g. the universal quartic factors over `F_p(V)` (a root rational on `V`), concentrating the split locus on a curve. There is no structural reason in `Phi = kappa N(lambda) - (ell[Q_S]) wedge (b lambda)` to force such factorization, but I cannot exclude it by hand.

## 4. Smallest exact next wall + finite-checker spec

Next wall:

```text
W-F1-AA-RES-T2J4-SPLIT-QUADRIC-IRREDUCIBILITY
```

Decide, for source-valid separated off-`R0` `(E,Bnum,W)`:
1. Is `V = {Phi=0}` geometrically irreducible of dimension 2? (Eliminate `tau_4`; test the resulting `(tau_1,tau_2,tau_3)`-surface.)
2. Is the Galois group of the universal quartic over `F_p(V)` equal to `S_4` (density `1/24` split)? — or does the quartic acquire an `F_p(V)`-rational root (split locus collapses to a curve, restoring `O(p)`)?

Either answer settles the gate: `S_4`/positive-density => `C2 = Theta(q_line)` counterpacket; rational-root collapse => `C2 = O(p)` and the `t=2` law extends to `j=4`.

Finite-checker spec (directly runnable on the banked module; I could not execute it here). Using `c11` from `20260618_cycle11_t2_j2_line_incidence_verify.py`:

```text
for p in {5,7,11,13(,17,19)}, several seeds:
  c11.set_field(p, NR);  D=[c11.b(x) for x in range(p)];  LD=c11.locator(D)
  E=c11.random_separated_quadratic(rng);  bnum=c11.random_bnum(rng)
  Bres=c11.residue2(bnum,E)
  W=c11.interp(D, random F-valued vector)
  slopes=set()
  for T in combinations(D,4):                # distinct 4-subsets
      LT=c11.locator(T);  Ls,rem=c11.pdivmod(LD,LT)   # rem must be 0
      _,Is=c11.pdivmod(W,Ls)
      z=c11.line_scalar(c11.residue2(Is,E), Bres)     # bad-slope test
      if z is not None: slopes.add(z)
  report C2=len(slopes), C2/p, C2/p^2, off_R0=(kappa!=0)
DECISION:  C2/p bounded as p grows  => O(p) (law extends);
           C2/p^2 bounded below     => Theta(q_line) counterpacket seed confirmed.
```

(Also emit, per `T`, the symbolic check `Phi(e(T))==0  <=>  z is not None` to validate the quadric `Phi = kappa N(lambda) - (ell[Q_S]) wedge (b lambda)` against the direct division test, exactly as `c11`/`c12` validate their `det` against `line_scalar`.)

## Bankable sub-lemma (inside this wall)

In the restricted `D=F_p`, `t=sigma=2`, `j=4`, off-`R0`, source-valid separated `c_b!=0` window: the split-quartic gate equals the vanishing of the single source-valid `F`-quadric

```text
Phi(tau) = iota wedge_F mu = kappa N_{A/F}(lambda) - (ell[Q_S]_E) wedge_F (b lambda),
```

`tau=e(T)` for a distinct 4-subset `T`. Its zero locus `V` is the intersection of two `B`-quadrics with leading coefficient `kappa != 0`, hence `dim V = 2`. Consequently, via the off-curve `z<->T` bijection,

```text
C2 = #{ totally-split-distinct quartics on V } + O(p),
```

so the affine/consistency layer **cannot** bound `C2` below `O(p^2)`: the `j<=3` mechanism provably terminates at `j=4`.

## Dependency list

- Cycle 11/12: `c11`/`c12` source conventions, `Q_S` closed form, `line_scalar` bad-slope test, `e(T)`-parametrization.
- Cycle 16/25: `det_B M` is the `z`-free invariant; `Q(z)` fiber separation; the codim-1-obstruction-at-`j=3` contrast.
- Cycle 24: `N(ell)=prod_{a}E(a)`, source-valid nonvanishing of the locator factor.
- Cycle 28: `Q_4 = N(c_b)(Im(d)^2-Im(c)Im(cbar d))`, source-valid nonzero — the leading-`tau_4^2` coefficient `kappa` here is the same locator-controlled top symbol.
- Cycle 29: square system, unique off-curve pre-image `tau(z)`, top symbol `-N(kappa)N(z)^2 Q_4`, off-curve `z->tau` well-defined.

## Hidden assumptions

- `Q_S` closed form uses `p` large enough that `W_{n-1..n-4}` are genuine top coefficients (Cycle 11/12 hypothesis).
- `N_{A/F}(lambda)`, `Tr_{A/F}(lambda')` use multiplication-determinant/trace of `lambda` acting `F`-linearly on `A`.
- The `Theta(p^2)` value assumes `V` geometrically irreducible of dim 2 **and** `S_4` (or positive-density) splitting on `F_p(V)`; **unproven** (this is the wall). The `O(p)` alternative requires an `F_p(V)`-rational root of the universal quartic; not excluded by hand.
- **No finite checker was run** (kernel execution disabled in this harness). The spec above converts the wall to a decidable experiment for `p=5,7,11,13`.

## Rejected overclaims

- NOT a proof of `C2=O(p)` for `j=4`; the `j<=3` consistency mechanism provably stops here.
- NOT a counterpacket: no growing-prime family, no proven irreducibility/`S_4`, no executed scan. `Theta(q_line)` is the **expected**, not proven, value.
- NOT a claim that `Phi` forces splitting density `1/24`; that is conditional on the next wall.
- Sub-reserve (`eta=2/n`), local. No corrected-reserve, `q_gen`/`q_line` merge, `q_chal`, list/CA/MCA/line-decoding/curve-MCA/protocol/SNARK, or Proximity-Prize consequence.
- `det_B M(z)=0` curve kept separate: `O(p)` slopes, absorbed into the `+O(p)` term; it neither proves nor refutes the gate.

## Do I see a route to a full solve?

Yes, but it is a single decidable step, not a closed proof from the desk. The split-quartic gate is now exactly `#(V cap split-distinct quartics)` with `V` an explicit dim-2 two-quadric variety. The next exact lemma/construction is `W-F1-AA-RES-T2J4-SPLIT-QUADRIC-IRREDUCIBILITY`: either prove the universal quartic over `F_p(V)` has an `F_p(V)`-rational root (=> `C2=O(p)`, `t=2` law extends to `j=4`), or prove `V` is geometrically irreducible of dim 2 with `S_4`/positive-density splitting (=> `C2=Theta(q_line)` counterpacket seed). The finite checker for `p in {5,7,11,13}` discriminates between the two in one run by testing whether `C2/p` or `C2/p^2` stabilizes.
