# Cycle 23 Audit: c-in-B D-Kernel Emptiness

Status: BANKABLE_LEMMA / ROUTE_CUT / AUDIT.

Harness status: HARNESS_MALFORMED_VISIBLE_TERMINAL.

## Run

- Run id: `2026-06-18T09-47-23-015Z-cycle23-nonemptiness-split-count-30f210ec`
- Run dir:
  `/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-18T09-47-23-015Z-cycle23-nonemptiness-split-count-30f210ec`
- Lane: isolated RS-MCA VS Code credited terminal lane.
- Launcher: `/Users/danielcabezas/packy-fable-ui/.codex-vscode-launchers/rs-mca-current`
- Harness result: `ok=false`,
  `classification=HARNESS_MALFORMED_VISIBLE_TERMINAL`,
  `answerSource=terminal_tui`, `terminalMalformedVisible=true`.
- `response.md`: absent.
- Audited provenance artifact: readable structured Claude JSONL recovery copied
  to `../raw/20260618_CYCLE23_NONEMPTINESS_SPLIT_COUNT_RECOVERED_CLAUDE_JSONL.md`.
- Malformed visible-terminal text is preserved separately and is not banked as
  mathematics.

## Verdict

Cycle 23 source-checks a decisive restricted lemma: in the `D=F_p`,
`B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3`, off-`R0` window, the branch

```text
c in B,
d notin B,
D=0,
kappa != 0
```

is empty. Therefore the Cycle 22 nonemptiness target for the `c in B`,
`d notin B` stratum is closed. The split-count question on that stratum is
vacuous.

This is a restricted local line-incidence/residue result only. It is not a
corrected-reserve theorem, not a `q_gen` statement, and not a protocol, list,
CA, MCA, line-decoding, curve-MCA, or SNARK statement.

## Field And Parameter Ledger

- `B=F_p`, `q_gen=p`.
- `F=F_{p^2}`, `q_line=p^2`.
- `q_chal` unused.
- `D=F_p`, so `n=p`.
- `t=sigma=2`.
- `j=n-a=r-t=3`; hence `a=n-3`, `k=n-5`.
- `eta=sigma/n=2/n`, sub-reserve.
- Work is off `R0`, meaning `kappa=u wedge b != 0`.
- This audit closes only the `c in B`, `d notin B` part of the `D=0` branch.

## Notation

Work in

```text
A=F[X]/E,
E=X^2+cX+d,
xi=[X]_E,
u=[W]_E,
b=[Bnum]_E,
ell=[X^p-X]_E,
kappa=u wedge b.
```

The Cycle 21/22 convention is

```text
x wedge y = x_0 y_1 - x_1 y_0,
P_E(x,y)=x_0 y_0 - c x_0 y_1 + d x_1 y_1,
```

and

```text
D=(ell wedge b)P_E(u,ell)+P_E(b,ell)(u wedge ell).
```

## Banked Lemma: `D` Is Nonzero On the `c in B`, `d notin B`, off-`R0` Stratum

Assume odd characteristic, `c in B`, `d notin B`, and `kappa != 0`. Put

```text
sigma=xi+c/2.
```

Then in `A`,

```text
sigma^2=c^2/4-d in F.
```

Since `c in B`, the Frobenius satisfies

```text
sigma^p=xi^p+c/2.
```

Because `sigma^2 in F`, write

```text
mu=sigma^{p-1}-1=(c^2/4-d)^{(p-1)/2}-1 in F.
```

Then

```text
ell=xi^p-xi=mu sigma.
```

Moreover `mu != 0`: if `mu=0`, then `ell=0`, so `E` divides `X^p-X`.
Since `E` is squarefree here, its roots lie in `B=F_p`; hence `E in B[X]`,
contradicting `d notin B`.

Using bilinearity,

```text
D=mu^2[(sigma wedge b)P_E(u,sigma)+P_E(b,sigma)(u wedge sigma)].
```

For `sigma=(c/2,1)`, direct expansion gives

```text
(sigma wedge b)P_E(u,sigma)+P_E(b,sigma)(u wedge sigma)
  = -(c^2/4-d) kappa.
```

Therefore

```text
D=-mu^2(c^2/4-d)kappa.
```

The three factors on the right are nonzero:

- `kappa != 0` by off-`R0`;
- `mu != 0` by the argument above;
- `c^2/4-d != 0` because `c^2/4 in B` and `d notin B`.

Hence

```text
D != 0
```

on this stratum.

## Consequence

The system

```text
c in B,
d notin B,
D=0,
off R0
```

has no source-valid points. The extra Cycle 23 conditions

```text
Delta1==0,
c_b=-Q_E(b)/kappa != 0,
W_{n-1} != 0
```

are therefore irrelevant on this branch.

This cuts the previous wall

```text
W-F1-AA-RES-T2J3-D-KERNEL-ALIGNMENT-NONEMPTINESS
```

on its `c in B`, `d notin B` subcase.

## Local Checker

Added:

```text
local_checks/20260618_cycle23_cinb_dkernel_identity_check.py
```

The checker verifies the identity

```text
D=-mu^2(c^2/4-d)kappa
```

in deterministic tiny-field samples for `p=3,5,7,11`. It is experimental
consistency evidence only; the banked result is the algebraic proof above.

Run output:

```text
p=3: checked 90 off-R0 samples from 90 deterministic trials
p=5: checked 500 off-R0 samples from 500 deterministic trials
p=7: checked 1470 off-R0 samples from 1470 deterministic trials
p=11: checked 6050 off-R0 samples from 6050 deterministic trials
PASS: Cycle 23 D=-mu^2*(c^2/4-d)*kappa identity verified in sampled tiny fields.
```

## Rejected Overclaims

Do not bank these statements from the recovered answer:

- any nonemptiness or split-count statement for the `c notin B` lane;
- any `C2` bound for the full `D=0` branch;
- any `Theta(q_line)` counterpacket;
- any corrected-reserve conclusion;
- any `q_gen`, protocol, list-decoding, line-decoding, CA, MCA, curve-MCA, or
  SNARK consequence.

The recovered answer also proposes a `Delta1==0` landing criterion
`delta_z in QR(F_p)`. That may be useful, but this audit does not bank it as a
proved lemma; it belongs in the next source-audit target if needed.

## New Live Wall

The only surviving `D=0`, off-`R0`, separated-`E` lane is now:

```text
W-F1-AA-RES-T2J3-D-KERNEL-NONSPLIT-C
```

meaning:

```text
D=0,
off R0,
E separated,
c notin B.
```

Next exact task:

1. Compute `ell=[X^p-X]_E` in closed form when `c notin B`.
2. Re-derive

```text
D=(ell wedge b)P_E(u,ell)+P_E(b,ell)(u wedge ell)
```

as a bilinear form in `(u,b)`.
3. Decide whether `D=0`, `Delta1==0`, and `off R0` are jointly solvable on
   `c notin B`.
4. If solvable, settle whether the split-cubic slope set is `O(p)` or
   `Omega(p^2)=Omega(q_line)` over growing primes.

