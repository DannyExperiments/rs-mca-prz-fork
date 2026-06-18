# Cycle 35 Prompt: A2_B Geometric S4 / Constant-Field Gate

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet.

You are continuing the RS-MCA / Proximity Prize Fable loop as a skeptical
mathematical co-director. Work only from the mounted repository/context files.
Do not use web access. Keep these ledgers separate:

- `q_gen = p`
- `B = F_p`
- `F = F_{p^2}=B(alpha)`
- `q_line = |F| = p^2`
- `q_chal` unused

Do not promote anything to corrected-reserve, MCA, CA, list-decoding,
line-decoding, curve-MCA, protocol, SNARK, or prize status.

## Current Wall

```text
W-F1-AA-RES-T2J4-A2B-GEOMETRIC-S4
```

Restricted branch:

- `D=F_p`, `n=p`;
- `t=sigma=2`, `j=n-a=r-t=4`;
- off `R0`;
- source-valid separated quadratic `E=X^2+cX+d` nonzero on `F_p`;
- use the branch where `c_b != 0`, `kappa != 0`, and Cycle 28/29 top-symbol
  nonvanishing applies.

## Source Context To Read First

Read these files before answering:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_BASE_FIELD_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle32_t2_j4_monodromy_histogram.py`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle32_t2_j4_monodromy_histogram_certificate.md`

Use `.tex` files only if you need to check a definition or hypothesis.

## Banked Before This Prompt

Cycle 33 banks only the singular boundary:

```text
Delta(z_0,z_1)=det_B M(z)
```

has total degree at most four and is not identically zero under the Cycle 29
top-symbol hypotheses, so `Delta=0` contributes at most `4p=O(p)` slopes.

Cycle 34 banks the off-curve dominance lemma:

```text
psi: A^2_B --> A^4_B, z |-> tau(z)=M(z)^(-1)(-C_0(z))
```

has generic `B`-Jacobian rank two and is birational onto its image, the Cycle
30 quadric `{Phi=0}`. Thus the off-curve image is surface-sized; any remaining
`O(p)` route must come from monodromy, geometric reducibility, transitivity, or
constant-field obstruction, not dimension collapse.

## The Task

Attack the geometric monodromy / constant-field gate directly.

1. Try to prove a seed-sufficient monodromy lemma:

   ```text
   L-T2J4-A2B-GEOM-TRANSITIVE.
   The quartic L_tau over B(z_0,z_1), after tau=tau(z_0,z_1), is
   geometrically irreducible/transitive and has no constant-field obstruction.
   ```

   Full `G_geom=S_4` is ideal, but not necessary. Any transitive geometric
   group with `G_arith=G_geom` gives positive split density.

2. Analyze the quartic

   ```text
   L_tau = X^4 - tau_1 X^3 + tau_2 X^2 - tau_3 X + tau_4,
   ```

   and its cubic resolvent

   ```text
   R(y)=y^3 - tau_2 y^2
          + (tau_1 tau_3 - 4 tau_4)y
          - (tau_1^2 tau_4 - 4 tau_2 tau_4 + tau_3^2).
   ```

   After substituting `tau_i=det M_i/Delta`, decide whether:

   - `disc_X L_tau` is nonsquare over `bar(F_p)(z_0,z_1)`;
   - `R(y)` is irreducible over `bar(F_p)(z_0,z_1)`;
   - the splitting field has constant field exactly `F_p`.

3. If a proof is out of reach, produce a precise certificate/checker plan,
   preferably with an explicit file in `output_files/`, that Codex can run or
   translate. The checker should build:

   - `M(z)` and `C_0(z)` symbolically with
     `z=z_0+alpha*z_1`, `m_z=z_0 I_4 + z_1 A_alpha`;
   - `Delta=det_B M(z)` and the Cramer numerators `det M_i`;
   - `R(y)` and `disc_num(z_0,z_1)` after denominator clearing;
   - tests for nonsquare discriminant, resolvent irreducibility, and constant
     field stability.

4. If the current route is false, give a source-valid counterpacket or name the
   exact obstruction. A valid counterpacket is higher value than another wall.

Use these labels literally: `PROOF`, `COUNTERPACKET`, `BANKABLE_LEMMA`,
`ROUTE_CUT`, `EXACT_NEW_WALL`, `AUDIT`, `EXPERIMENTAL`.

End by answering:

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?
