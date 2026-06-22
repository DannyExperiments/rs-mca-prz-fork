# Combined Prompt: ROLE_04_SMOOTH_512_256_LIFT_PROVER.md

Attach the packet zip, then paste this entire prompt into one fresh Pro instance.

--- COMMON PROMPT ---

You are one of nine independent theorem/certificate workers. Use only the attached packet. **No Internet. Do not browse.** Take all the time to reason you need. Use MAX reasoning.

Try to fully solve the problem. If you cannot fully solve it, progress it as much as possible. Do you see a route to a full solve? If yes, state the next exact lemma, checker, or counterpacket.

This is not a brainstorming round. Your target is:

```text
V-CYCLE116-STANDALONE-C84-TO-RS-MCA-LD-TRANSFER-CERTIFICATE
```

We already have a standalone Cycle84 finite certificate:

```text
m_max(beta)=2
Occ(beta)=52,747,567,092
D=24
12 double fibers, no fibers of size >= 3
```

Cycle115 suggests a much stronger semantic bridge:

```text
Cycle84 finite packet
  -> fixed-jet locator-to-RS-MCA theorem
  -> native row RS[F_17^16,<eta>,137]
  -> smooth lifted row RS[F_17^32,H,256], |H|=512
```

The desired final statement is:

```text
There is a smooth Reed--Solomon row

C = RS[F_17^32, H, 256], |H|=512,

with

LD_sw(C,262) >= 52,747,567,092
epsilon_mca(C,125/256) >= 52,747,567,092 / 17^32 > 2^-128.
```

Your job is to either make this into a clean standalone certificate, or find the exact fatal gap.

Read first:

```text
TARGET_CERTIFICATE_BLUEPRINT.md
context/audits/m1_cycle115_cycle84_to_mca_transfer_returns_audit.md
context/cycle84_finite_certificate/STANDALONE_FINITE_CERTIFICATE.md
context/audits/m1_cycle85_role05_transfer_returns_audit.md
context/audits/m2_line_decoding_mca_bridge.md
context/source/slackMCA_v3.tex
context/source/RS_disproof_v3.tex
```

Claim labels must be literal:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

Do not overclaim. In particular, do **not** call this an ordinary list-decoding lower bound, protocol soundness failure, asymptotic theorem, official Proximity Prize counterpacket, or accepted/deployed prime-field theorem unless you prove that exact implication from source definitions.

Before finalizing, explicitly answer:

1. What exact theorem/certificate did I prove, and what did I not prove?
2. Does the fixed-jet locator-to-MCA theorem really construct one affine line `f+zg`, support witnesses, explaining codewords, and noncontainment?
3. Does the Cycle84 instantiation really give `P_T(X)=X^113-X^112+O(X^107)` and `P_T(beta)=kappa Phi(T)` with `kappa != 0`?
4. Does the smooth `[512,256]` lift preserve agreement and noncontainment?
5. Are `q_gen`, `q_code`, `q_line`, `q_chal`, and the `2^-128` comparison used correctly?
6. What exact verifier or missing checker clause would make this PRZ-reviewable?

Output format:

```text
LABEL:
EXECUTIVE VERDICT:
STANDALONE CERTIFICATE SECTION OR ROUTE CUT:
PROOF DETAILS:
VERIFIER / CHECKER REQUIREMENTS:
FIELD AND PARAMETER LEDGER:
SELF-AUDIT:
NEXT EXACT STEP:
```

Be precise. The best answer is something we can almost paste into a standalone proof note.


--- ROLE PROMPT ---
# Role 04: Smooth `[512,256]` Lift Prover

Use the common prompt. No Internet.

Your job is to prove or break the smooth lift:

```text
F0 = F_17^16
eta has order 256
K = F0(theta), theta^2=eta = F_17^32
H=<theta>, |H|=512
C = RS[K,H,256]
```

Starting from the native Cycle85/Cycle84 line over `D0=<eta>`, prove that agreement-padding on `H=D0 union theta D0` preserves the numerator:

```text
LD_sw(RS[K,H,256],262) >= 52,747,567,092
epsilon_mca(C,125/256) >= 52,747,567,092 / 17^32.
```

You must explicitly verify:

- `eta` nonsquare and `theta` order `512`;
- choice of padding set `A` of size `119` and unused set `R`;
- polynomial multiplication by `L_A`;
- preserved agreement on `S_z union A`;
- preserved noncontainment after dividing by `L_A`;
- no hidden GRS/RS or field-extension loss.

If the lift is false, identify the first invalid line.
