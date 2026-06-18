# Cycle 33 Prompt: A2_B Monodromy Certificate Or Obstruction

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet.

You are continuing the RS-MCA Proximity Prize residue-line incidence loop.
Work only from the mounted source files and current-loop audit files. Do not
use the web.

Target:

```text
W-F1-AA-RES-T2J4-A2B-MONODROMY-CERTIFICATE
```

Cycle 32 corrected the base-field model. The `t=2,j=4` quartic family is not
one-variable over `B(z)` or `F(z)`. It is a two-dimensional `B`-surface family
over `A^2_B`, with

```text
z = z_0 + alpha z_1,      z_0,z_1 in B=F_p,
F=F_{p^2},               q_line=p^2.
```

Read first:

```text
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_BASE_FIELD_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle32_t2_j4_monodromy_histogram.py
current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle32_t2_j4_monodromy_histogram_certificate.md
```

Ledger constraints:

- Keep `q_gen=p`, `q_line=p^2`, `q_chal`, `B=F_p`, and `F=F_{p^2}` separate.
- Stay in the restricted residue-line incidence setting:
  `D=F_p`, `n=p`, `t=sigma=2`, `j=4`, off `R0`, source-valid separated
  `E=X^2+cX+d`, and `c_b != 0` when using that branch.
- Do not promote anything to corrected-reserve, MCA, list-decoding, CA,
  line-decoding, curve-MCA, protocol, SNARK, or Proximity Prize status.

Known local facts to audit:

1. Off `Delta(z_0,z_1)=det_B M(z)=0`, the Cycle 29/30 Cramer system solves a
   unique `tau(z)` and forms

   ```text
   L_tau = X^4 - tau_1 X^3 + tau_2 X^2 - tau_3 X + tau_4.
   ```

2. Codex's local checker records the factorization type of `L_tau` over
   `B=F_p` for all `z in F_{p^2}`. The `1111` split count agrees with direct
   support enumeration away from the singular determinant curve. Discrepancies
   are `singular_split_C2`.

3. Current checker outputs include:

   ```text
   p=11 hist_C2=3 direct_C2=3 singular_split_C2=0
   p=13 hist_C2=3 direct_C2=3 singular_split_C2=0
   p=17 hist_C2=8 direct_C2=8 singular_split_C2=0
   p=19 seed=0 hist_C2=13 direct_C2=14 singular_split_C2=1
   p=29 seed=0 hist_C2=33 direct_C2=34 singular_split_C2=1
   ```

Exact task:

1. Decide whether the Cycle 32 local checker plus Cycle 29/30 equations can be
   upgraded to a proof/certificate of positive-density split slopes on the
   `A^2_B` surface, or whether it remains only experimental.
2. Prove, refute, or reduce the claim that the singular determinant curve
   `Delta=0` contributes only `O(p)` split slopes.
3. State the exact monodromy theorem needed over `\bar B(z_0,z_1)`:
   discriminant nonsquare, cubic resolvent irreducible, arithmetic=geometric,
   or something different.
4. Identify whether a smaller transitive group than `S_4` would still suffice
   for a `Theta(q_line)` counterpacket seed.
5. If positive density cannot be proved, find the sharpest obstruction:
   constant-field extension, singular curve dominance, failure of generic
   injectivity, wrong resolvent criterion, or an error in the Cramer-system
   checker.

Output format:

- Start with exactly one of:
  `PROOF`, `BANKABLE_LEMMA`, `ROUTE_CUT`, `EXACT_NEW_WALL`,
  `COUNTERPACKET`, or `AUDIT`.
- Then give field ledger, proof/counterpacket/reduction, dependency list,
  hidden assumptions, rejected overclaims, and next exact wall.

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?
