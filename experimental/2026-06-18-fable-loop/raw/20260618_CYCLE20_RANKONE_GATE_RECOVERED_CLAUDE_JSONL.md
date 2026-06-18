I have all the source identities needed. Code execution was denied (the IDE tool is blocked and this matches Cycle 19's own no-code constraint), so this is an analytic audit worked directly from the Cycle 12/14 multiplication table in `A=F[X]/E` — re-deriving each candidate from first principles rather than pattern-matching.

---

## Primary label

```text
BANKABLE_LEMMA
```

All five Cycle 19 closed forms are **correct exactly off `R0`**, with no hidden genericity beyond `kappa=u wedge b != 0`. No formula is false, so this is not a `ROUTE_CUT`. I also isolate the sharper collapse condition (the `EXACT_NEW_WALL` refinement) below, but the headline is that the formulas are now proven, not candidate.

## Ledger (kept separate)

`B=F_p`, `q_gen=p`; `F=F_{p^2}=B+alpha B`, `q_line=p^2`; `q_chal` unused. `D=F_p`, `n=p`. `t=sigma=2`, `j=3`, `a=n-3`, `k=n-5`. `eta_reserve=2/n` sub-reserve. Work off `R0={kappa=[W]_E wedge [Bnum]_E=0}`. Line-incidence/residue calculation only.

## The multiplication engine (source-checked)

Write `x=(x^{(0)},x^{(1)})` for `x=x^{(0)}+x^{(1)}xi`, `xi^2=-c xi-d`. Then

```text
(xy)^{(0)}=x0 y0 - d x1 y1,   (xy)^{(1)}=x0 y1 + x1 y0 - c x1 y1,
x wedge y = x0 y1 - x1 y0,
Q_E(x)=x0^2 - c x0 x1 + d x1^2 = N(x)  (norm form),
P_E(x,y)=x0 y0 - c x0 y1 + d x1 y1,   P_E(x,x)=Q_E(x).
```

Two structural facts I use repeatedly (both proven by 2x2 expansion):

```text
(R1)  P_E(x,y) - P_E(y,x) = -c (x wedge y).
(R2 master)  (lambda_0 x) wedge y = lambda_0^{(0)} (x wedge y) - lambda_0^{(1)} P_E(y,x).
```

From Cycle 12 (`D=F_p`): `lambda_0=xi^3-tau_1 xi^2+tau_2 xi` reduces to

```text
lambda_0^{(0)} = c d + d tau_1,
lambda_0^{(1)} = (c^2-d) + c tau_1 + tau_2 =: eta,    [matches candidate]
```

and `Q:=[Q_S]_E` has `Q^{(0)}=W_{n-3}-d W_{n-1}-W_{n-2}tau_1+W_{n-1}tau_2`, `Q^{(1)}=(W_{n-2}-c W_{n-1})-W_{n-1}tau_1`. From Cycle 14, off `R0`, `A0=u lambda_0-ell Q`, `B0=lambda_0 b`, and in the `F`-basis `{u,b}`:

```text
p1=(A0 wedge b)/kappa,  p2=(u wedge A0)/kappa,  q1=(B0 wedge b)/kappa,  q2=(u wedge B0)/kappa.
```

## Verification of the four closed forms (each exact)

**q1.** By (R2) with `x=b,y=b` (so `x wedge y=0`, `P_E(b,b)=Q_E(b)`):
`(lambda_0 b) wedge b = -eta Q_E(b)`. Hence

```text
q1 = -(Q_E(b)/kappa) eta.            [CANDIDATE CONFIRMED]
```

**q2.** `u wedge(lambda_0 b) = -[(lambda_0 b) wedge u] = -[lambda_0^{(0)}(b wedge u) - eta P_E(u,b)] = lambda_0^{(0)}kappa + eta P_E(u,b)`. Hence

```text
q2 = lambda_0^{(0)} + (P_E(u,b)/kappa) eta.       [CONFIRMED]
```

**p1.** `(u lambda_0) wedge b = lambda_0^{(0)}kappa - eta P_E(b,u)` by (R2). Using (R1), `P_E(b,u)=P_E(u,b)+c kappa`, so `P_E(b,u)/kappa=c+P_E(u,b)/kappa`. With `A0=u lambda_0-ell Q`:

```text
p1 = lambda_0^{(0)} - (c + P_E(u,b)/kappa) eta - (1/kappa)((ell Q) wedge b).   [CONFIRMED]
```

**p2.** `u wedge(u lambda_0) = -[(lambda_0 u) wedge u] = eta Q_E(u)` (since `u wedge u=0`, `P_E(u,u)=Q_E(u)`). Hence

```text
p2 = (1/kappa)(Q_E(u) eta - (u wedge ell Q)).      [CONFIRMED]
```

The two `Q`-dependent pieces also reduce exactly as claimed (project onto `Q^{(0)}1+Q^{(1)}xi` and apply (R2) with `lambda_0->xi`):

```text
(ell Q) wedge b = (ell wedge b)Q^{(0)} - P_E(b,ell)Q^{(1)},
u wedge (ell Q) = (u wedge ell)Q^{(0)} + P_E(u,ell)Q^{(1)}.
```

## Lemma 1 (rank-one) — PROVEN

`q1=-(Q_E(b)/kappa) eta` is a fixed `F`-scalar times the single affine form `eta`. So the leading coefficient of the slope quadratic `q1 z^2-(p1-q2)z-p2=0` is rank-one in `(tau_1,tau_2)`, vanishing exactly on the `F`-line `eta=0`. Also `lambda_0^{(0)}=cd+d tau_1` cancels from `q1`, `p1-q2`, `p2` and survives only in the trace `p1+q2=2lambda_0^{(0)}-c eta-(1/kappa)((ell Q) wedge b)`. Both claims hold unconditionally off `R0`.

## Lemma 2 (quadric normal form) — PROVEN

The discriminant identity is algebraic (always true):

```text
delta_z := (p1-q2)^2 + 4 q1 p2 = (p1+q2)^2 - 4 det P,   det P := p1 q2 - p2 q1.
```

`Delta=tau_3^2-(p1+q2)tau_3+det P`, so `Delta1==0` is **exactly** `{p1+q2 in B[tau_1,tau_2]} and {det P in B[tau_1,tau_2]}`; on that locus `delta_z=(p1+q2)^2-4 det P in B[tau_1,tau_2]`. With `c_b=-Q_E(b)/kappa` and `A=(ell Q) wedge b`, the quadratic formula gives (using `p1-q2=-c eta-2(P_E(u,b)/kappa)eta-A/kappa`):

```text
z = const_F + w^±,   w^± = (±sqrt(delta_z) - A/kappa)/(2 c_b eta),
const_F = (-c - 2 P_E(u,b)/kappa)/(2 c_b)   [tau-independent].
```

The `eta` in `q1` cancels the `eta`-proportional part of `p1-q2`, leaving a fixed `F`-translation; since translation is a bijection, `C2=#{z}=#{w^±}`. **Confirmed** (requires `b` a unit, `Q_E(b)!=0`, so `c_b!=0`).

## The scalar gate D — definition and role PROVEN (collapse role still open)

Express the three slope-coefficient forms in the frame `{eta, Q^{(0)}, Q^{(1)}}`. The coefficient matrix is

```text
M = [ c_b                       0                 0            ]   (q1)
    [ *              -(ell wedge b)/kappa     P_E(b,ell)/kappa ]   (p1-q2)
    [ *              -(u wedge ell)/kappa    -P_E(u,ell)/kappa ]   (p2)
```

Expanding along the first row:

```text
det M = (c_b/kappa^2) * [ (ell wedge b) P_E(u,ell) + P_E(b,ell)(u wedge ell) ] = (c_b/kappa^2) * D.
```

So with `c_b!=0`, `kappa!=0`:

```text
D = 0  <=>  {q1, p1-q2, p2} are F-linearly dependent in the frame {eta,Q^{(0)},Q^{(1)}}
            (the P^2(F) coefficient image lies in a fixed line).
```

`D=(ell wedge b)P_E(u,ell)+P_E(b,ell)(u wedge ell)` depends only on `(E,u,b,ell)` and is **not identically zero**: `u=ell` gives `D=(ell wedge b)Q_E(ell)`, nonzero whenever `ell` is a unit independent of `b`. So `D=0` is a proper closed gate. This confirms the candidate gate is well-defined and correctly placed as the `P^2(F)`-level degeneration obstruction.

What this does **not** settle: `D=0` is the `F`-linear (`P^2`) degeneration, which is *necessary* for `C2=O(p)`, but `eta,Q^{(0)},Q^{(1)}` are three affine forms in only two `B`-variables, so the genuine collapse is a finer `B`-level condition. This is the residual wall.

## What is banked vs not

Bank (proven, exact, off `R0`, restricted `D=F_p, t=sigma=2, j=3` window): the four closed forms `p1,p2,q1,q2`; Lemma 1 (rank-one `q1`, `lambda_0^{(0)}` cancellation); Lemma 2 (discriminant identity, `Delta1==0` ⟺ `{p1+q2,det P}∈B`, descent of `delta_z` to `B[tau_1,tau_2]`, normal form `w^±`); the gate identity `det M=(c_b/kappa^2)D` with `D≢0`.

Do **not** bank: collapse or non-collapse; any `C2` bound on `Delta1==0`; any `Theta(q_line)` counterpacket; the claim `D=0 <=> C2=O(p)` (only the `P^2`-level equivalence is proven); anything at/above corrected reserve; any `q_gen`, protocol, list/line/curve-decoding, CA, or MCA consequence.

## Sharpened wall (EXACT_NEW_WALL refinement)

```text
W-F1-AA-RES-T2J3-RESONANCE-SLOPE-MAP-COLLAPSE  (sharpened)

On the Delta1==0 locus { p1+q2 in B[tau1,tau2], det P in B[tau1,tau2] }, with
q1=c_b eta (rank one), delta_z in B[tau1,tau2], and
w^± = (±sqrt(delta_z) - A/kappa)/(2 c_b eta),  A=(ell Q) wedge b :
prove dim_B Im(w)=1  (equivalently  dw wedge d eta == 0  on the locus)  => C2=O(p),
OR build source-valid growing-p data with dim_B Im(w)=2  => C2=Theta(p^2)=Theta(q_line).
```

The gate `D=0` is the `P^2(F)`-level necessary condition; the open question is whether the `Delta1==0` resonance conditions on `(p1+q2, det P)` force the finer `B`-level dependence `dw wedge d eta==0`. This corrects Cycle 18's "collapse plausible": the normal form shows collapse is a **non-generic degeneration that must be forced**, since `A=(ell Q) wedge b` is a rank-two `F`-affine form while `eta` is rank-one. The Cycle 15 `p=7`, `C2<=6` data are consistent with the gate firing but are single-prime EXPERIMENTAL and decide nothing.

Which prior wall survives: none is cut. Cycles 12–18 all check out against the multiplication identities; Cycle 16's `Q!=0 => C2<=4p` safe side stands, and the live residual is exactly the `Delta1==0` / `Q==0` branch, now equipped with the proven normal form and gate.

## Forbidden-upgrade compliance

No Proximity-Prize solve/disproof; no `conj:B`; `eta=2/n` stays sub-reserve (even a `Theta(q_line)` here would not refute corrected MCA); `q_gen` and `q_line` kept separate; no protocol denominator saving; no list/line/curve decoding, CA, MCA; finite scans cited only as EXPERIMENTAL; malformed terminal text not used as math.

---

Do you see a route to a full solve? If yes, what is the next exact lemma or construction?

Not a full solve from here — this is a sub-reserve `eta=2/n` toy window, so even a positive collapse result closes only restricted `t=2,j=3` local F1, not the Prize. But there is a concrete, code-free route to closing this window. The next exact lemma is the **`B`-rank-one descent on the `Delta1==0` locus**:

```text
NEXT EXACT LEMMA (finite symbolic, no growing prime):
On Delta1==0, the two B-descent conditions are
  (i)  Im_alpha(p1+q2) ≡ 0  in B[tau1,tau2],
  (ii) Im_alpha(det P) ≡ 0  in B[tau1,tau2].
Compute dw wedge d eta as a polynomial in (tau1,tau2) modulo the ideal (i),(ii).
Prove dw wedge d eta ≡ 0 on V(i,ii)  (=> C2=O(p), window closed),
or find one source-valid (E,Bnum,W) on V(i,ii) with dw wedge d eta ≢ 0
(the precise counterpacket seed; only then run p=11,13,17,19,23 filtered to Delta1==0,
watching C2/p^2).
```

Equivalently: factor `Res_{tau_3}(Delta0,Delta1)` and test whether the gate `D` together with conditions (i),(ii) forces the resultant to carry the `eta`-rank-one structure. This is a finite Gröbner/resultant computation in `B[tau_1,tau_2]` — it needs a working CAS but no asymptotics, and it would either bank `C2=O(p)` for the full `t=2,j=3` window or expose the first source-valid `Theta(q_line)` seed. That is the single decisive next construction.
