Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet.

You are working on the RS-MCA / Proximity Prize repository as a skeptical
mathematical co-director. This is Cycle 21.

# Target

```text
W-F1-AA-RES-T2J3-B-RANKONE-DESCENT
```

The goal is to settle the `B`-level descent condition exposed by Cycle 20.
Do not summarize the whole repo. Attack this exact wall.

# Read first

- `input_project/ROUTE_BOARD_CURRENT.md`
- `input_project/ACTIVE_WALLS.md`
- `input_project/BANKED_LEMMAS.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE18_HOMERUN_AUDIT.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE20_RANKONE_GATE_AUDIT.md`

# Ledger

Keep these separate:

```text
B=F_p,        q_gen=p
F=F_{p^2},    q_line=p^2
q_chal unused
D=F_p,        n=p
t=sigma=2
j=n-a=r-t=3, so a=n-3, k=n-5
eta_reserve=sigma/n=2/n, sub-reserve
work off R0={kappa=[W]_E wedge [Bnum]_E=0}
```

This is still a restricted line-incidence/residue calculation. Do not claim any
corrected-reserve, `q_gen`, protocol, list, CA, MCA, line-decoding, or SNARK
consequence without a theorem.

# Banked Cycle 20 facts

Let

```text
E=X^2+cX+d,
xi=[X]_E,
u=[W]_E,
b=[Bnum]_E,
ell=[L_D]_E=[X^p-X]_E,
kappa=u wedge b.
```

For `x=x0+x1 xi`, define `Q_E`, `P_E`, and `wedge` as in the Cycle 20 audit.
Cycle 20 banked:

```text
q1 = -(Q_E(b)/kappa) eta,
eta=(c^2-d)+c tau_1+tau_2,
```

so the leading coefficient of the slope quadratic is rank-one.

On the `Delta1==0` quadric branch, `p1+q2` and `det P=p1 q2-p2 q1` descend to
`B[tau_1,tau_2]`, and

```text
delta_z=(p1-q2)^2+4q1p2=(p1+q2)^2-4 det P in B[tau_1,tau_2].
```

For `c_b=-Q_E(b)/kappa` and `A=(ell Q) wedge b`, slopes are, up to fixed
`F`-translation,

```text
w^+-=(+-sqrt(delta_z)-A/kappa)/(2 c_b eta).
```

Cycle 20 also banked the `P^2(F)` gate

```text
D=(ell wedge b)P_E(u,ell)+P_E(b,ell)(u wedge ell),
det M=(c_b/kappa^2)D.
```

But `D=0` is only the `P^2(F)`-level degeneration. The open wall is the finer
`B`-level condition.

# Exact question

On the `Delta1==0` locus, the two `B`-descent equations are:

```text
Im_alpha(p1+q2)=0,
Im_alpha(det P)=0.
```

Do these force the `B`-rank-one dependence

```text
dw wedge d eta == 0
```

for the slope normal form above, hence `dim_B Im(w)=1` and `C2=O(p)`?

Or can one produce source-valid data where the descent equations hold but

```text
dw wedge d eta != 0,
```

giving a seed for `C2=Theta(p^2)=Theta(q_line)` over growing primes?

# Desired output

Return exactly one primary label:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
```

`PROOF`: prove the descent equations force `dw wedge d eta == 0` on the
`Delta1==0` branch, including hypotheses such as `c_b!=0`.

`COUNTERPACKET`: give source-valid symbolic or growing-prime data with descent
conditions satisfied and `dw wedge d eta != 0`, plus a route to
`C2/p^2` bounded below. Single-prime evidence is not enough.

`BANKABLE_LEMMA`: prove a smaller exact implication involving the descent
equations, `D`, `dw wedge d eta`, or the resultant/common-component structure.

`ROUTE_CUT`: identify a false premise in Cycle 20's banked setup or in the
formulation above.

`EXACT_NEW_WALL`: isolate a strictly sharper algebraic condition below
`dw wedge d eta == 0`, preferably an explicit resultant, common-component, or
function-field criterion.

End by answering:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

# Forbidden upgrades

- Do not claim the Proximity Prize is solved.
- Do not treat this `eta=2/n` window as corrected-reserve.
- Do not merge `q_gen` and `q_line`.
- Do not infer protocol denominator savings.
- Do not use internet or web sources.
- Do not cite finite scans as proof.
