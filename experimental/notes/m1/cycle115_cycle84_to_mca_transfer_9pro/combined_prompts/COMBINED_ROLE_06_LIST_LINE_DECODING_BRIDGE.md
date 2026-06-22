# Combined Prompt: ROLE_06_LIST_LINE_DECODING_BRIDGE.md

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
# Role 06: List / Line-Decoding Bridge

Use the common prompt. No Internet.

Your role is to decide whether Cycle84's finite certificate transfers more cleanly through line-decoding or list-decoding than through raw MCA.

Use `context/notes_m2/m2_line_decoding_mca_bridge.md`, `snarks_v4.tex`, `proximity_blueprint_v3.tex`, and the source definitions. Your task is to produce a clean theorem or route cut of the form:

```text
Cycle84 finite slope/product occupancy
  -> support-wise line-decoding numerator a_LD
  -> MCA numerator or protocol-facing line-decoding failure
```

Questions to answer:

- What exact line-decoding definition is being used?
- Is the Cycle84 support-wise bad-slope set identical to a line-decoding obstruction set?
- Does line-decoding avoid any support-wise MCA bookkeeping, or does it require the same noncontainment data?
- What are the exact `(delta, a_LD, b)` parameters?
- Does the denominator use `q_line`, `q_code`, or `q_chal`?
- Can line-decoding make the Cycle88/89 two-copy row paper-facing even if the MCA phrasing is awkward?
- Is there a list-decoding implication, or would using list-decoding here be a category error?

If you prove a bridge, state the theorem in a form usable in a paper. If not, state the exact missing conversion theorem.
