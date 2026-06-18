# Cycle 31 Prompt: T2J4 Split-Quadric Collapse

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet.

You are continuing the RS-MCA Proximity Prize residue-line incidence loop.
Work only from the mounted source files and current-loop audit files. Do not
use the web.

Target:

```text
W-F1-AA-RES-T2J4-SPLIT-QUADRIC-COLLAPSE
```

Goal: reconcile Cycle 30's two-quadric split-gate reduction with Codex's finite
scan, which leans toward `O(p)` rather than positive-density `Theta(q_line)`.

Read first:

```text
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE28_Q4_PROOF_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle30_t2_j4_split_quartic_scan_certificate.md
current_loop_20260618/2026-06-18-fable-loop/raw/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_RECOVERED_CLAUDE_JSONL.md
```

Ledger constraints:

- Keep `q_gen=p`, `q_line=p^2`, `q_chal`, `B=F_p`, and `F=F_{p^2}` separate.
- Stay in the restricted residue-line incidence setting:
  `D=F_p`, `n=p`, `t=sigma=2`, `j=4`, off `R0`, source-valid separated
  `E=X^2+cX+d`, and `c_b != 0` when using that branch.
- Do not promote anything to corrected-reserve, MCA, list-decoding, CA,
  line-decoding, curve-MCA, protocol, SNARK, or Proximity Prize status.

Exact task:

Cycle 30 reduces the split-quartic gate to

```text
Phi(tau)=iota wedge_F mu
        = kappa*N_{A/F}(lambda)
          - (ell*[Q_S]_E) wedge_F (b*lambda) = 0,
```

where `tau=e(T)` for a distinct 4-subset `T subset F_p`. This is one
`F`-quadric, i.e. two `B`-quadrics, in four elementary-symmetric parameters.

Codex's direct finite scan reports:

```text
p=17 avg_C2/p=0.482, avg_C2/p^2=0.0284
p=19 avg_C2/p=0.618, avg_C2/p^2=0.0325
p=23 avg_C2/p=0.739, avg_C2/p^2=0.0321
p=29 avg_C2/p=1.078, avg_C2/p^2=0.0372
```

This does not look like a generic `p^2/24` split-density count. Attack the
hidden collapse directly:

1. Prove or refute that `Phi(e(T))=0` imposes a hidden rational-root,
   discriminant, trace, norm, or Frobenius condition that cuts the totally
   split distinct locus down to `O(p)`.
2. If such collapse exists, state the exact theorem and dependencies needed
   for an `O(p)` bound in the restricted `t=2,j=4` window.
3. If no collapse exists, construct a source-valid growing-prime family that
   realizes `Theta(q_line)` slopes and explain why the finite random scan
   missed it.
4. If neither direction closes, output the smallest exact algebraic invariant
   to check next: resultant, discriminant, rational-root criterion over
   `F_p(V)`, Galois group condition, or a refined finite checker.

Output format:

- Start with exactly one of:
  `PROOF`, `BANKABLE_LEMMA`, `ROUTE_CUT`, `EXACT_NEW_WALL`,
  `COUNTERPACKET`, or `AUDIT`.
- Then give field ledger, proof/counterpacket/reduction, dependency list,
  hidden assumptions, rejected overclaims, and next exact wall.

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?
