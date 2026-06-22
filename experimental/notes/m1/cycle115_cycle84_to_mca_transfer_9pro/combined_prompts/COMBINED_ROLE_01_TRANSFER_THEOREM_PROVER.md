# Combined Prompt: ROLE_01_TRANSFER_THEOREM_PROVER.md

Attach the packet zip, then paste this entire prompt into one Pro instance.

--- COMMON PROMPT ---

You are one of nine independent theorem workers on an open mathematics project about Reed--Solomon MCA / list / line-decoding and the Proximity Prize frontier.

Use only the attached packet. **No Internet. Do not browse.** Take all the time to reason you need. Use MAX reasoning.

Try to fully solve the problem. If you cannot fully solve it, progress it as much as possible. Do you see a route to a full solve? If yes, state the next exact lemma, checker, source contract, or counterpacket.

Your task is not to recompute Cycle84. Treat the supplied standalone Cycle84 finite certificate as the finite black-box anchor unless you find an internal contradiction. The verified finite anchor is:

```text
m_max(beta) = 2
Occ(beta) = 52,747,567,092
D = 24
12 double fibers and no fibers of size >= 3
```

The actual task is PRZ's question:

```text
What exact transfer theorem would turn Cycle84's finite color-filtered
m_max(beta)=2 certificate into an MCA / list / line-decoding statement
over Reed--Solomon parameters?
```

You must aggressively separate claim levels:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

Do not call a finite/model certificate a prize proof. Do not call a source-route stress packet a counterpacket unless it satisfies the official RS-MCA / list / line-decoding definitions and field ledger. Do not use broad language like "should transfer" or "morally equivalent" without naming the exact theorem and first possible failure line.

Important context:

1. Cycle84 is a clean finite certificate.
2. Cycle85 tried a one-copy finite MCA slope transfer over `F_17^16`.
3. Cycle88/Cycle89 tried a two-copy / extension-field bridge to a `[464,232]` row over `F_17^48`.
4. Cycles90-114 found many source/field/charge/official-contract hazards. They matter. Use the audited notes, not only Cycle84.
5. The most dangerous objects are `q_gen`, `q_line`, `q_code`, `q_chal`, the `2^-128` denominator target, smooth multiplicative subgroup/coset admissibility, support-wise MCA definitions, line-decoding conversion, and numerator loss from quotient/periodic/contained/same-slope/affine-color/endpoint/tangent normalization.

Before finalizing, do a self-audit and explicitly answer:

1. What exact implication did I prove, and what exact implication did I not prove?
2. Is the result official-prize-relevant, paper-facing finite RS-MCA/list/line-decoding, or only finite/model/research-certificate level?
3. What is the first line in the reduction chain where the theorem could fail?
4. Are `q_gen`, `q_line`, `q_code`, `q_chal`, and the `2^-128` target being used correctly?
5. Could quotient/periodic structure, contained incidences, same-slope collisions, endpoint/tangent losses, or affine color normalization reduce the claimed numerator?
6. If my answer is a `PLAN`, what exact theorem/checker/source contract/counterpacket would convert it into `PROOF` or `COUNTERPACKET`?

Output format:

```text
LABEL: one of PROOF / COUNTERPACKET / BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT / PLAN
EXECUTIVE VERDICT:
EXACT THEOREM OR OBSTRUCTION:
PROOF / DISPROOF / ROUTE CUT:
FIELD AND PARAMETER LEDGER:
SELF-AUDIT:
NEXT EXACT STEP:
```

Be ambitious. A useful answer either proves a real transfer theorem, kills a false one, or names the exact missing official theorem with enough precision that the next worker can attack it.


--- ROLE PROMPT ---
# Role 01: Transfer Theorem Prover

Use the common prompt. No Internet.

Your role is to prove the strongest source-valid transfer theorem you can from the Cycle84 finite certificate to a Reed--Solomon MCA / list / line-decoding statement.

Start from the candidate chain:

```text
Cycle84 finite color-filtered product spectrum
  -> Cycle85 one-copy finite slope occupancy over F_17^16
  -> Cycle88/89 two-copy or extension-row bridge over F_17^48
  -> support-wise MCA or line-decoding numerator over an RS/GRS code
```

Do not assume this chain is valid. Prove every arrow you use from the supplied definitions. If a full prize-facing transfer is impossible, prove the maximal finite/paper-facing theorem that is actually supported.

You should try to produce one of these:

1. A `PROOF` theorem with exact RS/GRS parameters `(F,D,n,k,delta,q_gen,q_code,q_line,q_chal)` and an exact bad-slope or line-decoding numerator.
2. A `BANKABLE_LEMMA` that states the transfer conditionally on named missing hypotheses, with no vague phrases.
3. A `ROUTE_CUT` locating the first false or unsupported arrow.

Mandatory checks:

- Does the reciprocal-affine map from product values to slopes stay injective after all normalizations?
- Does support-wise `def:mca` in `slackMCA_v3.tex` match the finite packet's color shell and witness sets?
- Is GRS-to-RS diagonal scaling harmless for the exact error notion?
- Is the row arbitrary-domain only, or smooth multiplicative subgroup/coset as required by the prize-facing RS setting?
- Does the numerator survive quotient/periodic/contained/same-slope/endpoint/tangent/affine-color charges?

Finish by writing the exact theorem statement that PRZ could review.
