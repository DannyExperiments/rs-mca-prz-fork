# Cycle 34 A2_B Dominance And Resolvent Audit

Status: BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT.

Harness status: HARNESS_MALFORMED_VISIBLE_TERMINAL. No clean `response.md`
was produced. The visible terminal scrape is not used as mathematics. The
readable Claude structured JSONL recovery is preserved as provenance; the
mathematical content below is audited conservatively from that recovery and
the prior committed companion files.

Source artifacts:

- `raw/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_RAW.json`
- `raw/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_RUN_RESULT.json`
- `raw/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_CREDIT_SURFACE_RUNNER_RESULT.json`

## Ledger

- `q_gen = p`.
- `B = F_p`.
- `F = F_{p^2} = B(alpha)`.
- `q_line = |F| = p^2`.
- `q_chal`: unused.
- Domain: `D = F_p`, so `n=p`.
- Restricted regime: `t=sigma=2`, `j=n-a=r-t=4`.
- Branch: off `R0`, source-valid separated quadratic `E=X^2+cX+d`
  nonzero on `F_p`, with `c_b != 0`, `kappa != 0`, and the Cycle 28/29
  top-symbol nonvanishing hypotheses in force.

This is only a residue-line / bad-slope incidence calculation. It is not a
corrected-reserve theorem, MCA claim, list-decoding claim, CA claim,
line-decoding claim, curve-MCA claim, protocol claim, SNARK claim, or
Proximity Prize solution.

## Banked Restricted Lemma

Cycle 34 banks the following local dominance lemma:

```text
L-T2J4-A2B-DOMINANCE.
In the restricted t=2, j=4 A^2_B model on the source-valid branch
(kappa != 0, c_b != 0, Cycle 29 top symbol != 0), the rational map
psi: A^2_B --> A^4_B, z |-> tau(z)=M(z)^(-1)(-C_0(z)), has generic
B-Jacobian rank 2, is birational onto its image, and that image is the
Cycle 30 quadric {Phi=0}. Dependencies: Cycle 29/30 affine-linear column
structure; b != 0; lambda(tau(z)) not identically zero; cotangent
functoriality. No monodromy input is used.
```

Proof skeleton:

1. Work with the graph equation in `A=F[X]/E`:

   ```text
   G(z,tau) = (u - z b) lambda(tau) - ell [Q_S(tau)]_E = 0.
   ```

2. For fixed `z`, this is the square affine-linear system
   `M(z) tau = -C_0(z)`, so off `Delta=det_B M(z)=0` it defines
   `psi(z)=tau(z)`.
3. For fixed `tau`, the same equation is linear in `z`:

   ```text
   z (b lambda(tau)) = u lambda(tau) - ell [Q_S(tau)]_E.
   ```

4. On the dense open where `b lambda(tau) != 0`, this defines a rational
   inverse coordinate map `chi(tau)` by the unique collinearity scalar `z`.
5. If `tau=psi(z)`, then `G(z,psi(z))=0`, hence `chi(psi(z))=z` generically.
   Therefore `chi o psi = id` as rational maps on a dense open.
6. Functoriality of cotangent maps gives `D chi * D psi = I_2` generically.
   Thus the `4 x 2` `B`-Jacobian of `psi` has generic rank exactly two.

The audit accepts this as a local algebraic argument, subject to the stated
dense-open hypotheses. It explicitly avoids any Frobenius-style inseparability
shortcut: the inverse `chi` is a rational map built from the same source
equation, not a formal set-theoretic inverse.

## Route Cut

Cycle 34 cuts the attempted dimension-collapse explanation for an `O(p)` split
count:

```text
ROUTE_CUT: rank <= 1 / image-collapses-to-curve is not the live mechanism
for the off-curve t=2,j=4 A^2_B branch.
```

Together with Cycle 33, the current restricted picture is:

- singular boundary `Delta=0`: at most `4p` slopes;
- off-curve map `z -> tau(z)`: genuinely surface-sized, generic rank two.

Therefore any remaining `O(p)` route must come from monodromy, transitivity,
geometric reducibility, or a constant-field obstruction, not from a hidden
rank-one image.

## Resolvent Reduction

For

```text
L_tau = X^4 - tau_1 X^3 + tau_2 X^2 - tau_3 X + tau_4,
```

with cubic resolvent

```text
R(y)=y^3 - tau_2 y^2
       + (tau_1 tau_3 - 4 tau_4)y
       - (tau_1^2 tau_4 - 4 tau_2 tau_4 + tau_3^2),
```

Cycle 34 records the standard quartic criterion in characteristic not `2` or
`3`:

```text
G_geom = S_4
  iff R(y) is irreducible over bar(F_p)(z_0,z_1)
      and disc_X L_tau is nonsquare in bar(F_p)(z_0,z_1).
```

After substituting `tau_i=det M_i/Delta`, the square class reduces to

```text
disc_X L_tau = disc_num(z_0,z_1) / Delta^6,
```

so the discriminant square-class test is the square class of the numerator
`disc_num`, since `Delta^6` is a square. This is a reduction, not a completed
certificate.

## Experimental Evidence Not Banked As Proof

Cycle 34 notes that Cycle 32's `p=29` squarefree factorization histogram
matches the `S_4` cycle index closely, and that recorded cycle types include a
4-cycle and a transposition. This is useful evidence for arithmetic `S_4` in
the tested finite instance, but it remains `EXPERIMENTAL`:

- finite histograms are not all-large-`p` geometric monodromy proofs;
- they do not rule out constant-field effects by themselves;
- they do not prove positive split density in the source theorem;
- they do not create a counterpacket or prize-level result.

## Next Exact Wall

```text
W-F1-AA-RES-T2J4-A2B-GEOMETRIC-S4
```

The remaining gate is to prove or refute geometric transitivity, ideally full
`S_4`, and constant-field stability for the off-curve quartic family over
`B(z_0,z_1)`.

A seed-sufficient target is weaker than full `S_4`: any transitive geometric
group with arithmetic/geometric equality gives a positive split density. Full
`S_4` would identify the constant as `1/24`.

## Next Checker / Certificate Target

The next run should build or specify the symbolic certificate:

1. Construct `M(z)` and `C_0(z)` with `z=z_0+alpha z_1` and
   `m_z=z_0 I_4 + z_1 A_alpha`.
2. Cross-check `Delta=det_B M(z)` has degree four and the Cycle 29 top symbol.
3. Compute `tau_i=det M_i/Delta`.
4. Form `R(y)` and `disc_X L_tau`; clear denominators.
5. Test:
   - whether `disc_num` is nonsquare over `bar(F_p)[z_0,z_1]`;
   - whether `R(y)` is irreducible over `bar(F_p)(z_0,z_1)`;
   - whether the splitting field has constant field exactly `F_p`.

## Rejected Overclaims

- Do not cite Cycle 34 as a proof of `Theta(q_line)` split slopes.
- Do not cite Cycle 34 as a counterpacket.
- Do not cite Cycle 34 as a proof of geometric `S_4`.
- Do not merge `q_gen=p` and `q_line=p^2`.
- Do not promote the local `t=2,j=4` branch to corrected-reserve, MCA, CA,
  list-decoding, line-decoding, curve-MCA, protocol, SNARK, or prize status.
