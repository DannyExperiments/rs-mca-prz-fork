# Cycle 28 Prompt: Q4 Proof Audit

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet.

You are auditing a potentially decisive local branch cut in the RS-MCA
Proximity Prize repository. Work only from the mounted source files and the
listed current-loop audit files. Do not use the web.

Target:

```text
W-F1-AA-RES-T2J3-Q4-PROOF-AUDIT
```

Goal: independently rederive, verify, or refute Cycle 27's claimed `Q_4`
obstruction. Do not trust Cycle 27's algebra unless you can reproduce it from
the source/audit definitions.

Read first:

```text
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE15_SURFACE_SLOPE_FIBER_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE16_RANK_DETERMINANT_RESONANCE_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE20_RANKONE_GATE_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE24_NONSPLIT_C_DKERNEL_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE26_QZERO_RANK_CONSISTENCY_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE27_Q4_SPLIT_GATE_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/raw/20260618_CYCLE27_Q4_SPLIT_GATE_RECOVERED_CLAUDE_JSONL.md
```

Ledger constraints:

- Keep `q_gen=p`, `q_line=p^2`, `q_chal`, `B=F_p`, and `F=F_{p^2}` separate.
- Work only in the restricted residue-line incidence regime
  `D=F_p`, `n=p`, `t=sigma=2`, `j=3`, off `R0`, `kappa != 0`, source-valid
  separated `E=X^2+cX+d`, and `c_b != 0`.
- Do not promote anything to list-decoding, CA, MCA, line-decoding,
  curve-MCA, protocol, SNARK, corrected-reserve, or Proximity Prize status.

Exact questions:

1. Reconstruct the Cycle 15/16 columns `c_i(z)=s_i(z)u+t_i(z)b` and the Cycle
   25 six-term Plucker/Laplace expression for
   `Q(z_0,z_1)=det_B[c_1(z)|c_2(z)|c_3(z)|c_0(z)]`.
2. Extract the degree-4 coefficient `Q_4` directly from those definitions.
3. Verify or refute the formula

```text
Q_4 = N(c_b) * ( Im(d)^2 - Im(c) * Im(conj(c) d) ).
```

4. If the formula is correct, verify or refute the locator identity

```text
if c notin B:
  Q_4 = N(c_b) * Im(c)^2 * E(-Im(d)/Im(c)).
```

5. Decide whether source-validity and separatedness force `Q_4 != 0` on both
   `c notin B` and `c in B` branches.
6. If `Q_4 != 0` is source-validly forced, state exactly what is proved:
   `Q` is not identically zero, hence Cycle 16 gives `O(p)` affine-consistent
   slopes, and the distinct split-cubic gate only shrinks the set.
7. If there is any flaw, give the smallest exact wall or counterpacket:
   bad sign/scalar, missing hypothesis, false source-validity implication,
   failure of `q2` closed form, or a source-valid example with `Q_4=0`.

Output format:

- Start with one of:
  `PROOF`, `BANKABLE_LEMMA`, `ROUTE_CUT`, `EXACT_NEW_WALL`,
  `COUNTERPACKET`, or `AUDIT`.
- Then give:
  - field ledger;
  - proof or refutation;
  - dependency list;
  - hidden assumptions;
  - rejected overclaims;
  - next exact wall.

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?
