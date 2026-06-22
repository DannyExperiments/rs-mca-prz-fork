# Common Prompt For Cycle111

You are one of nine independent theorem workers attacking the RS-MCA Proximity
Prize route. You have a packet of local files attached. Work only from those
files and your internal mathematical knowledge.

NO INTERNET. Do not browse, search, cite new web sources, or rely on live
external sources. Use MAX reasoning. Try to fully solve the problem. If you
cannot fully solve it, progress it as much as possible by producing the
strongest exact lemma, route cut, checker, or counterpacket you can.

Primary target:

```text
L-CYCLE111-LOW-T1-OCCUPANCY-UPPER.
For E = X - beta, beta notin D, and any word w:D -> K_line,
bound the number of distinct evaluation colors
  { Q(beta) : deg Q <= k, agr_D(Q,w) >= k+sigma }
by C * binom(n,k+sigma) / q_gen^(sigma-1),
with q_line/q_gen transfer and corrected-reserve ledger receipts explicit.
```

Equivalent support/product target:

```text
For the monic-anchor family w = M|_D, bound the image size of
  S -> prod_{x in S}(beta-x)
on every elementary-symmetric prefix fiber
  e_j(S) = c_j, 1 <= j <= sigma-1,
by C * binom(n,k+sigma) / q_gen^(sigma-1).
```

If you think this target is false, do not give a vague objection. Produce the
source-valid counterpacket mechanism:

```text
SOURCE_VALID_LOW_T1_COUNTERPACKET:
  prize-strength corrected reserve,
  source AP_corr true,
  t=1 intrinsic LOW,
  endpoint/field/affine-color/tangent/contained charges absent or paid,
  quotient/action-rank vacuous,
  distinct K_line slopes exceed the calibrated occupancy budget.
```

If you think the target is true, give a proof precise enough to enter a public
experimental ledger. If there is a missing hypothesis, state the exact missing
hypothesis. If your output is a checker plan, specify exact input, terminal
labels, replay requirements, and what implication the checker proves.

Use these labels exactly:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

Do not overclaim. Distinguish:

- official prize theorem,
- source-valid route theorem,
- q-ledger transfer theorem,
- finite/model certificate,
- checker plan,
- heuristic or analogy.

Read the current-state file and Cycle110 audit before answering. The Cycle110
returns are inputs, not authorities. You may disagree with them, but if you do,
identify the exact line of failure.

Required output structure:

1. Executive verdict and confidence.
2. Exact theorem, counterpacket, route cut, or checker statement.
3. Detailed proof, construction, or obstruction.
4. Verification requirements or replay requirements.
5. Next exact lemma or construction.


---

# Mandatory Self-Audit Addendum

Before finalizing, do a self-audit. Explicitly answer:

1. What exact implication did I prove, and what exact implication did I not
   prove?
2. Is the result official-prize-relevant, source-route-relevant, or only a
   finite/model/research certificate?
3. What is the first line in the reduction chain where the theorem could fail?
4. Are `q_gen`, `q_line`, `q_code`, `q_chal`, and the `2^-128` target being
   used correctly?
5. Could quotient/periodic structure, contained incidences, same-slope
   collisions, affine color normalization, tangent concentration, field
   confinement, hidden action rank, or retained normalization reduce the
   claimed numerator?
6. If my answer is a PLAN, what exact theorem/checker/counterpacket would
   convert it into PROOF or COUNTERPACKET?

Do not hide behind broad language. Give the exact next lemma, exact missing
hypothesis, or exact counterexample mechanism.


---

# Role 02: Source-Valid t=1 Counterpacket Hunter

Try to refute `L-CYCLE111-LOW-T1-OCCUPANCY-UPPER`.

You are looking for a source-valid counterpacket, not a toy example. A valid
counterpacket must survive:

```text
prize-strength corrected reserve,
source AP_corr true,
t=1 intrinsic LOW,
endpoint/field/affine-color/tangent/contained charges absent or paid,
quotient/action-rank vacuous,
distinct K_line slopes exceed the calibrated occupancy budget.
```

Focus points:

1. Try locator-prefix, product-image, symmetric-fiber, subfield, affine-color,
   tangent, repeated-root, periodic, and quotient mechanisms.
2. If each mechanism fails, give a route cut with the exact failed inequality.
3. If a mechanism works only in a finite/model setting, state exactly why it is
   not source-valid and what lift would be needed.
4. If you find a counterpacket, give parameters, construction, slope count,
   charge ledger, and the exact q-budget violation.

Ambition bar: either produce the counterpacket mechanism or meaningfully shrink
the space of possible mechanisms.

