# Cycle 20 Audit: Rank-One Gate Lemma

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Harness status: HARNESS_MALFORMED_VISIBLE_TERMINAL.

## Run

- Run id: `2026-06-18T08-35-22-491Z-cycle20-rankone-gate-audit-d049f9ca`
- Run dir:
  `/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-18T08-35-22-491Z-cycle20-rankone-gate-audit-d049f9ca`
- Lane: isolated RS-MCA VS Code credited terminal ads lane.
- Launcher: `/Users/danielcabezas/packy-fable-ui/.codex-vscode-launchers/rs-mca-current`
- Harness result: `ok=false`,
  `classification=HARNESS_MALFORMED_VISIBLE_TERMINAL`,
  `answerSource=terminal_tui`, `terminalMalformedVisible=true`.
- `response.md`: absent.
- Audited provenance artifact: readable structured Claude JSONL recovery copied
  to `../raw/20260618_CYCLE20_RANKONE_GATE_RECOVERED_CLAUDE_JSONL.md`.
- Malformed visible-terminal text is preserved separately and is not banked as
  mathematics.

## Verdict

Cycle 20 source-checks the Cycle 19 rank-one/gate candidate. The closed forms
for `p1,p2,q1,q2`, the rank-one leading coefficient, the quadric-branch normal
form, and the `D` gate are bankable in the restricted
`D=F_p`, `t=sigma=2`, `j=3`, off-`R0` window.

Do not bank slope collapse, non-collapse, or a counterpacket. The live residual
wall is the finer `B`-level condition on the `Delta1==0` branch.

## Field And Parameter Ledger

- `B=F_p`, `q_gen=p`.
- `F=F_{p^2}`, `q_line=p^2`.
- `q_chal` unused.
- `D=F_p`, so `n=p`.
- `t=sigma=2`.
- `j=n-a=r-t=3`; hence `a=n-3`, `k=n-5`.
- `eta=sigma/n=2/n`, sub-reserve.
- Work is off `R0={kappa=[W]_E wedge [Bnum]_E=0}`.
- This is a restricted line-incidence/residue calculation only.

## Notation

Let

```text
E=X^2+cX+d,
xi=[X]_E, xi^2=-c xi-d,
u=[W]_E,
b=[Bnum]_E,
ell=[L_D]_E=[X^p-X]_E,
kappa=u wedge b.
```

For `x=x0+x1 xi`, define

```text
Q_E(x)=x0^2 - c x0 x1 + d x1^2,
P_E(x,y)=x0 y0 - c x0 y1 + d x1 y1,
x wedge y=x0 y1-x1 y0.
```

The useful expansion identity is

```text
(lambda_0 x) wedge y =
lambda_0^(0)(x wedge y) - lambda_0^(1) P_E(y,x).
```

Cycle 12 gives

```text
lambda_0 = xi^3 - tau_1 xi^2 + tau_2 xi,
lambda_0^(0)=cd+d tau_1,
lambda_0^(1)=eta=(c^2-d)+c tau_1+tau_2.
```

Cycle 14 gives `A0=u lambda_0-ell Q`, `B0=lambda_0 b`, and, in the
`{u,b}` basis,

```text
p1=(A0 wedge b)/kappa,
p2=(u wedge A0)/kappa,
q1=(B0 wedge b)/kappa,
q2=(u wedge B0)/kappa.
```

## Banked Closed Forms

The following formulas are source-checked:

```text
q1 = -(Q_E(b)/kappa) eta,
q2 = lambda_0^(0) + (P_E(u,b)/kappa) eta,
p1 = lambda_0^(0) - (c + P_E(u,b)/kappa) eta
     - (1/kappa)((ell Q) wedge b),
p2 = (1/kappa)(Q_E(u) eta - (u wedge ell Q)).
```

The `Q`-dependent terms are

```text
(ell Q) wedge b = (ell wedge b) Q^(0) - P_E(b,ell) Q^(1),
u wedge (ell Q) = (u wedge ell) Q^(0) + P_E(u,ell) Q^(1).
```

## Banked Lemma 1: Rank-One Leading Coefficient

The leading coefficient of the slope quadratic

```text
q1 z^2 - (p1-q2) z - p2 = 0
```

is

```text
q1=-(Q_E(b)/kappa) eta.
```

Thus `q1` is a fixed `F`-scalar times the single affine form
`eta=(c^2-d)+c tau_1+tau_2`. Also `lambda_0^(0)=cd+d tau_1` cancels from
`q1`, `p1-q2`, and `p2`, surviving only in `p1+q2`.

## Banked Lemma 2: Quadric-Branch Normal Form

The determinant polynomial is

```text
Delta=tau_3^2-(p1+q2)tau_3+(p1 q2-p2 q1).
```

Therefore the quadric branch `Delta1==0` is exactly the condition that
`p1+q2` and `det P:=p1 q2-p2 q1` descend to `B[tau_1,tau_2]`. On this branch,

```text
delta_z := (p1-q2)^2+4 q1 p2
         = (p1+q2)^2-4 det P
```

lies in `B[tau_1,tau_2]`.

With

```text
c_b=-Q_E(b)/kappa,
A=(ell Q) wedge b,
```

the slopes are, up to fixed `F`-translation,

```text
w^+-=(+-sqrt(delta_z)-A/kappa)/(2 c_b eta).
```

This normal form is bankable only where `c_b!=0`, i.e. where `b` is a unit in
`F[X]/E`.

## Banked Lemma 3: The Gate `D`

In the frame `{eta,Q^(0),Q^(1)}`, the coefficient matrix for
`q1`, `p1-q2`, `p2` has determinant

```text
det M = (c_b/kappa^2) D,
D=(ell wedge b)P_E(u,ell)+P_E(b,ell)(u wedge ell).
```

Thus, when `c_b!=0` and `kappa!=0`,

```text
D=0
```

is exactly the `P^2(F)`-level degeneration condition for the slope-coefficient
image. The gate is proper: it is not identically zero as a formal expression.

## What Is Not Banked

Do not bank:

- `D=0` iff `C2=O(p)`;
- slope collapse on the `Delta1==0` branch;
- non-collapse or a `Theta(q_line)` counterpacket;
- any above-reserve result;
- any `q_gen` conclusion;
- any protocol, list-decoding, line-decoding, CA, MCA, or SNARK statement.

## Sharpened Live Wall

The live wall becomes:

```text
W-F1-AA-RES-T2J3-B-RANKONE-DESCENT
```

On the `Delta1==0` locus, prove

```text
dim_B Im(w)=1,
```

equivalently prove the appropriate `B`-level Jacobian condition such as

```text
dw wedge d eta == 0
```

after imposing the two `B`-descent equations

```text
Im_alpha(p1+q2)=0,
Im_alpha(det P)=0.
```

If this fails on a source-valid stratum, the failure is the precise seed for a
growing-prime `Theta(q_line)` counterpacket in the sub-reserve toy window.
