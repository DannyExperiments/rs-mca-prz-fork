# Cycle 24 Prompt: Nonsplit-c D-Kernel Branch

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet.

You are working on the RS-MCA / Proximity Prize repository as a skeptical
mathematical co-director. This is Cycle 24.

## Target

```text
W-F1-AA-RES-T2J3-D-KERNEL-NONSPLIT-C
```

Do not summarize the repository. Attack this exact wall.

## Read first

- `input_project/ROUTE_BOARD_CURRENT.md`
- `input_project/ACTIVE_WALLS.md`
- `input_project/BANKED_LEMMAS.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE21_B_RANKONE_DESCENT_AUDIT.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE22_D_KERNEL_ALIGNMENT_AUDIT.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE23_CINB_DKERNEL_EMPTINESS_AUDIT.md`

## Ledger

Keep these separate:

```text
B=F_p,        q_gen=p
F=F_{p^2},    q_line=p^2
q_chal unused
D=F_p,        n=p
t=sigma=2
j=n-a=r-t=3, so a=n-3, k=n-5
eta_reserve=sigma/n=2/n, sub-reserve
work off R0, i.e. kappa=[W]_E wedge [Bnum]_E != 0
```

This remains a restricted line-incidence/residue calculation. Do not claim any
corrected-reserve, `q_gen`, protocol, list, CA, MCA, line-decoding, curve-MCA,
or SNARK consequence without a theorem.

## Banked Reduction

Use notation:

```text
E=X^2+cX+d,
A=F[X]/E,
xi=[X]_E,
u=[W]_E,
b=[Bnum]_E,
ell=[L_D]_E=[X^p-X]_E,
kappa=u wedge b,
g1=ell wedge b,
g2=P_E(b,ell),
h1=u wedge ell,
h2=P_E(u,ell),
D=g1 h2+g2 h1.
```

Cycle 23 proves the `c in B`, `d notin B` branch is empty:

```text
if c in B, d notin B, kappa != 0, then
ell=mu*(xi+c/2),
D=-mu^2(c^2/4-d)kappa != 0.
```

Therefore `D=0` off `R0` can survive only in the complementary separated lane

```text
c notin B.
```

Cycle 21/22 banks:

```text
D != 0 blocks simultaneous branch collapse.
On D=0, alignment is equivalent to J_A=0.
On Delta1==0:
  Im_alpha(J_A)=2 Im_alpha(d)+Im_alpha(c) f_2.
```

For `c notin B`, this no longer kills alignment; it imposes

```text
f_2=-2 Im_alpha(d)/Im_alpha(c)
```

plus the real part of `J_A=0`.

## Exact Question

Settle the nonsplit-c branch:

```text
c notin B,
E separated,
D=0,
off R0,
Delta1==0,
c_b=-Q_E(b)/kappa != 0,
W_{n-1} != 0.
```

Questions:

1. Compute `ell=[X^p-X]_E` in a usable closed form for `c notin B`.
2. Re-derive `D` as an explicit bilinear form in `(u,b)` with coefficients
   determined by `(c,d)` and Frobenius.
3. Decide whether the system above is empty, curve-sized, or surface-sized.
4. If nonempty, determine whether it yields only `O(p)` distinct split-cubic
   bad slopes or a growing-prime `Omega(p^2)=Omega(q_line)` counterpacket seed.

## Desired Output

Return exactly one primary label:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
```

`PROOF`: close the nonsplit-c branch by proving emptiness or `O(p)` slopes.

`COUNTERPACKET`: give a source-valid symbolic/growing-prime family with
`Omega(p^2)=Omega(q_line)` distinct split-cubic bad slopes. Single-prime
evidence alone is not enough.

`BANKABLE_LEMMA`: prove a smaller exact implication, such as a closed form for
`ell`, a rank bound for the `D=0` bilinear form, or a descent obstruction on
`Delta1==0`.

`ROUTE_CUT`: identify a false premise in Cycle 21/22/23.

`EXACT_NEW_WALL`: isolate a strictly sharper algebraic condition, elimination
ideal, resultant, or finite checker specification.

If tool writing is unavailable, do not spend time trying to create files. Give
the proof, counterpacket, or checker specification inline.

End by answering:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

## Forbidden Upgrades

- Do not claim the Proximity Prize is solved.
- Do not treat this `eta=2/n` window as corrected-reserve.
- Do not merge `q_gen` and `q_line`.
- Do not infer protocol denominator savings.
- Do not use internet or web sources.
- Do not cite finite scans as proof.

