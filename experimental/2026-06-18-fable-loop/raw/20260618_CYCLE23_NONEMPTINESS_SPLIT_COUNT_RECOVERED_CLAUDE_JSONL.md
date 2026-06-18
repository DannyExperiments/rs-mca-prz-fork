Code execution and file writing are denied in this harness (the same constraint Cycles 19–22 recorded), so I worked the algebra by hand from the banked Cycle 12/14/20/21/22 multiplication table and the source scripts (`cycle11`/`cycle12` define `wedge`, `P_E`, the residue pipeline, and `L_D = X^p - X` for `D = F_p`). The result is decisive and does not need a scan.

---

## Primary label

```text
PROOF
```

The stratum is **empty**. Question B is therefore vacuous. This closes the `c in B, d notin B` portion of the `D=0` branch in the restricted `t=2, j=3` window.

## Direct answer

**Question A: No — the stratum is empty.** On `c in B`, `d notin B` (separated `E`), off `R0`, the gate `D` is *forced nonzero*. Concretely

```text
D = -mu^2 * sigma^2 * kappa,     sigma^2 = c^2/4 - d,   mu in F^*,
```

and all three factors are nonzero, so `D != 0` everywhere on `{c in B, d notin B, off R0}`. The extra conditions `Delta1==0`, `c_b!=0`, `W_{n-1}!=0` never get a chance to act.

**Question B: vacuous** (no points), hence no `Omega(p^2)` and no `O(p)` to report on this stratum.

## Proof that `D != 0` on `{c in B, d notin B, off R0}`

Work in `A = F[X]/E`, `E = X^2 + cX + d`, basis `{1, xi}`, `xi = [X]_E`, `xi^2 = -c xi - d`. The source scripts fix
`x wedge y = x0 y1 - x1 y0` and `P_E(x,y) = x0 y0 - c x0 y1 + d x1 y1`; both are confirmed by the banked Cycle 21 expansions
`(ell Q) wedge b = (ell wedge b)Q0 - P_E(b,ell)Q1` and `u wedge (ell Q) = (u wedge ell)Q0 + P_E(u,ell)Q1` (I re-checked `(ell·xi) wedge b = -P_E(b,ell)` and `u wedge (ell·xi) = P_E(u,ell)` directly).

**Step 1 — the locator residue `ell` when `c in B`.**
For `D = F_p`, `L_D = X^p - X`, so `ell = [X^p - X]_E = xi^p - xi`. Put

```text
sigma := xi + c/2  in A,    sigma^2 = xi^2 + c xi + c^2/4 = (-d) + c^2/4 = c^2/4 - d  in F.
```

The `p`-power map is a ring endomorphism of `A`, semilinear over the Frobenius of `F`. Because `c in B` we have `(c/2)^p = c/2`, so

```text
sigma^p = (xi + c/2)^p = xi^p + c/2.
```

But `sigma^2 = c^2/4 - d in F`, hence `sigma^{p-1} = (sigma^2)^{(p-1)/2} in F`; write `mu := sigma^{p-1} - 1 in F`, so `sigma^p = (mu+1) sigma`. Then

```text
ell = xi^p - xi = (sigma^p - c/2) - (sigma - c/2) = sigma^p - sigma = mu * sigma.
```

So **`ell = mu * sigma`** with `mu in F`, `sigma = (c/2, 1)` in coordinates.

`mu != 0`: if `mu = 0` then `ell = 0`, i.e. `X^p == X (mod E)`, i.e. both roots of `E` lie in `F_p`, forcing `E in B[X]` and `d in B` — contradicting `d notin B`. Hence `mu != 0`.

**Step 2 — the four forms collapse onto `sigma`.**
Since `ell = mu sigma`, bilinearity gives `g1 = mu (sigma wedge b)`, `g2 = mu P_E(b,sigma)`, `h1 = mu (u wedge sigma)`, `h2 = mu P_E(u,sigma)`. Therefore

```text
D = g1 h2 + g2 h1 = mu^2 [ (sigma wedge b) P_E(u,sigma) + P_E(b,sigma)(u wedge sigma) ].
```

**Step 3 — evaluate the bracket.** With `sigma = (c/2, 1)`, `b = (b0,b1)`, `u = (u0,u1)`:

```text
sigma wedge b = (c/2) b1 - b0,        P_E(u,sigma) = -c u0/2 + d u1,
P_E(b,sigma)  = -c b0/2 + d b1,       u wedge sigma = u0 - c u1/2.
```

Multiplying and summing, the `b1u1` and `b0u0` terms cancel and the cross terms combine to

```text
(sigma wedge b)P_E(u,sigma) + P_E(b,sigma)(u wedge sigma)
   = (c^2/4 - d)(b0 u1 - b1 u0)
   = -sigma^2 * kappa,
```

using `b0 u1 - b1 u0 = -(u0 b1 - u1 b0) = -kappa`. Hence

```text
D = -mu^2 * sigma^2 * kappa.
```

**Step 4 — nonvanishing.**
- `kappa != 0` (off `R0`, given);
- `mu != 0` (Step 1, since `d notin B`);
- `sigma^2 = c^2/4 - d != 0`, because `c^2/4 in B` while `d notin B`, so `c^2/4 - d notin B`, in particular `!= 0`.

Therefore `D != 0`. The conditions `c in B`, `d notin B` (separated), off `R0`, and `D = 0` are mutually inconsistent: the stratum is empty. ∎

(Equivalently: `D = 0` off `R0` forces `mu sigma^2 = 0`. `sigma^2 = 0` is discriminant ramification `disc = c^2 - 4d = 0`; `mu = 0` is `E in B[X]` non-separation. Both are excluded by the stratum hypotheses, so the alignment gate cannot vanish there at all.)

## Why this is consistent with — and sharper than — Cycle 22

Cycle 22's `(DECOUPLE)` identity `Im_alpha(J_A) = 2 Im_alpha(d) + Im_alpha(c) f_2` proved alignment *impossible* on this stratum **conditional on the stratum being nonempty**. The present computation removes the conditional in the strongest possible way: on `c in B, d notin B` (off `R0`) the kernel gate `D` is identically nonzero, so the locus `D=0` it conditioned on does not exist. The banked Cycle 21 fact "`D != 0` blocks simultaneous branch collapse" then says directly that simultaneous slope-collapse is impossible here — no need to inspect `J_A` at all.

So Cycle 22's `Im_alpha(J_A) = 2 Im_alpha(d)` and the present `D = -mu^2 sigma^2 kappa` are two consistent witnesses to the same structural fact: the `c in B` separated stratum lives strictly *off* the `D=0` kernel.

## Sharpened live wall (where a `Theta(q_line)` seed could still hide)

`D = 0` off `R0` is now pinned to the complementary geometry:

```text
W-F1-AA-RES-T2J3-D-KERNEL-NONSPLIT-C:
  D = 0, off R0, E separated   ==>   c notin B   (equivalently Im_alpha(c) != 0).
```

This is the only surviving lane. There Cycle 22's `(DECOUPLE)` does *not* force impossibility; alignment instead needs the single extra scalar `f_2 = -2 Im_alpha(d)/Im_alpha(c)` plus `Re(J_A)=0`. The relocated question is whether `{c notin B, Delta1==0, D=0, off R0}` is nonempty and, if so, its split count.

A byproduct I verified by hand and bank as a tool for that lane (no scan needed): on **any** `Delta1==0` point (`p1+q2, detP in B[tau]`),

```text
delta_z := (p1+q2)^2 - 4 detP  in B[tau_1,tau_2]   (degree 2),
tau_3 = ((p1+q2) -/+ sqrt(delta_z))/2,    z = (p1 - tau_3)/(c_b eta) = ((p1-q2) +/- sqrt(delta_z))/(2 c_b eta),
```

so on `Delta1==0` the **landing condition is exactly `delta_z(tau_1,tau_2) in QR(F_p)`**, and `A/kappa` is a function of `eta` alone iff `J_A = 0` (alignment). Hence on any *nonempty* alignment-failing `Delta1==0` point the slope does not collapse to `eta`, giving the lower bound `C2 = Omega(p)` per `eta`-fibre; the `Omega(p^2)` vs `O(p)` split then reduces to a single finite cross-fibre slope-collision count. This is the precise residual object for the `c notin B` lane — but it is **not** invoked for the present stratum, which is simply empty.

## Inline checker specification (Write denied; copy to `output_files/CHECKER.py`)

Identity-confirmation only, not the proof:

```text
For p in {7,11,13,17,19}, NR a nonresidue, F=F_{p^2}, A=F[X]/(X^2+cX+d):
  for many (c in B, d with Im(d)!=0, u, b with kappa=u∧b != 0):
    ell = residue of X^p - X mod E       # expect ell == mu*(c/2,1) for scalar mu
    g1=ell∧b; g2=P_E(b,ell); h1=u∧ell; h2=P_E(u,ell); D=g1*h2+g2*h1
    assert D == -mu^2 * (c^2/4 - d) * kappa     # closed form
    assert D != 0                               # emptiness witness
  Report: zero counterexamples expected over all sampled (c in B, d notin B).
```

Ledger discipline: `q_gen=p` and `q_line=p^2` kept separate; `eta=2/n` stays sub-reserve; no protocol/list/line/CA/MCA/curve-MCA/SNARK consequence; no internet; no scan cited as proof (the proof is the closed form in Steps 1–4).

## Banked vs not

Bank (proven, exact, restricted `D=F_p`, `t=sigma=2`, `j=3`, off `R0`): **`ell = [X^p-X]_E = mu*(xi+c/2)` for `c in B`**; the closed form **`D = -mu^2 sigma^2 kappa`** with `sigma^2 = c^2/4 - d`; the corollary **`{c in B, d notin B, D=0, off R0}` is empty**, hence Question A negative and the `c in B` part of the `D=0` branch closed; and the `Delta1==0` landing criterion `delta_z in QR(F_p)` with the explicit `tau_3`, `z` formulas and the collapse-iff-`J_A=0` dictionary.

Do **not** bank: nonemptiness or split count in the `c notin B` lane; any `C2` bound there; any `Theta(q_line)` counterpacket; anything at/above corrected reserve; any `q_gen`, protocol, list/line/curve-decoding, CA, MCA, or SNARK consequence.

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

Not a Prize solve — this is the sub-reserve `eta=2/n` toy window, so closing it closes only the restricted `t=2, j=3` local-F1 wall. But there is now a sharp route. This cycle closes the `c in B` half of the `D=0` branch outright (empty). The next exact step is the mirror computation in the only surviving lane:

```text
NEXT EXACT LEMMA (c notin B lane; finite, CAS-checkable, no asymptotics):
  Compute ell = [X^p - X]_E for c notin B. Now (c/2)^p != c/2, so the Step-1
  collapse ell = mu*(xi+c/2) fails; instead xi^p is the second root of E^tau in A
  and ell is a genuine 2-dimensional A-element. Re-derive D in closed form:
    D = (ell wedge b)P_E(u,ell) + P_E(b,ell)(u wedge ell)
  as a bilinear form in (u,b) with coefficients in F determined by (c,d) and the
  Frobenius image xi^p. Decide whether D=0 (off R0) is solvable jointly with
  Delta1==0 and Im(c)!=0 (the f_2 = -2Im(d)/Im(c) gate). 
  Then, on any solution, apply the banked 'delta_z in QR(F_p)' landing criterion and
  settle the cross-fibre slope-collision count: Omega(p^2) => first source-valid
  Theta(q_line) seed; O(p) => the whole D=0 branch closes and C2=O(p) in this window.
```

The decisive reduction this cycle delivers: the `D=0` branch is no longer a two-parameter `(c,d)` surface to search — it is forced entirely into `c notin B`, and the gate there is one explicit bilinear-form vanishing plus one finite collision count.
