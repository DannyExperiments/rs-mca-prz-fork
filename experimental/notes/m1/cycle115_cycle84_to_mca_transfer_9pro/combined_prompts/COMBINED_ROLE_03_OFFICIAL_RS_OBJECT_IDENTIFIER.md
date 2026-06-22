# Combined Prompt: ROLE_03_OFFICIAL_RS_OBJECT_IDENTIFIER.md

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
# Role 03: Official RS Object Identifier

Use the common prompt. No Internet.

Your role is to identify the exact Reed--Solomon or generalized Reed--Solomon object, if any, that Cycle84 transfers to.

Do not focus on the finite computation. Focus on definitions and parameters.

For every plausible transfer row, fill the ledger:

```text
field F =
evaluation domain D =
is D a smooth multiplicative subgroup/coset? =
code type RS or GRS =
n =
k =
rate rho =
agreement size a or support size |S| =
radius delta =
line family f + z g =
bad-slope numerator =
q_gen =
q_code =
q_line =
q_chal =
target floor(q_line / 2^128) =
whether numerator > target =
first unsupported official-definition condition =
```

Analyze both:

- one-copy Cycle85-style row over `F_17^16`;
- two-copy / extension Cycle88-89-style row over `F_17^48`.

Use `readme.md`, `RS_disproof_v3.tex`, `slackMCA_v3.tex`, `snarks_v4.tex`, and the Cycle85/88/89 audits. Pay special attention to whether a row is merely finite/paper-facing or is actually within the smooth multiplicative RS family that the prize discussion cares about.

End with an exact classification:

```text
OFFICIAL_ROW_IDENTIFIED
FINITE_RS_ROW_ONLY
GRS_ONLY_NOT_RS
ARBITRARY_DOMAIN_ONLY
PRIZE_FAMILY_EMBEDDING_MISSING
Q_LEDGER_FAIL
SOURCE_DEFINITION_FAIL
```

Then justify it.
