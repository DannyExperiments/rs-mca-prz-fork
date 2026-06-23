# Focused Pro Audit Prompts

Use these after the Cycle120 note is attached. Do not ask for encouragement.
Ask for the first fatal line.

## Role 1: Hostile Finite-Chain Auditor

```text
No internet. Use only the attached Cycle120 packet and its cited local
receipts.

Your job is to falsify the proof chain:

Cycle84 occupancy
  -> fixed-jet/product-scalar bridge
  -> Cycle116 smooth RS transfer
  -> LD_sw(RS[F_17^32,H,256],262) >= 52,747,567,092.

Check the line construction, supports, explaining codewords, noncontainment,
field arithmetic, smooth lift, and slope-count preservation.

Return PROOF if the chain is correct.
Return ROUTE_CUT with the first false statement if it fails.
```

## Role 2: Hostile ABF Definition Auditor

```text
Use the attached ABF PDF excerpts and Cycle120 note.

Question:
Does ABF's printed grand MCA challenge admit the row
  RS[F_17^32,H,256], |H|=512,
with gamma sampled uniformly from F_17^32 and the support-wise same-support
noncontainment event?

Check Definition 2.11, Definition 2.12, Definition 4.3, the uniform sampling
notation, the rate/envelope text, and the absence/presence of extra filters.

Return ABF_ACCEPT if the implication is valid.
Return ABF_REJECT with the first rejected clause if invalid.
Return ABF_UNKNOWN only if a needed clause is absent from the attached text.
```

## Role 3: Hostile Cycle116 Fixed-Jet Auditor

```text
No internet. Audit only the Cycle116 route:

P_T=X^113-X^112+O(X^107),
P_T(beta)=4(beta-1)Phi(T),
fixed-jet locator-to-MCA transfer,
agreement 262 smooth lift to RS[F_17^32,H,256].

Find the first fatal mathematical line, if any. Pay special attention to:
common line versus one line per support,
noncontainment,
scalar normalization,
padding support size,
field degree/order,
and numerator preservation.

Return PROOF or ROUTE_CUT.
```

## Role 4: Hostile Cycle119 Strict-Addendum Auditor

```text
No internet. Audit the Cycle119 strict-263 addendum.

Check whether the two-ended locator theorem really upgrades the same row to
agreement 263 while preserving all 52,747,567,092 slopes.

Critical issues:
common constant P_J(0),
selected degrees 0,250,...,255,
no hidden seventh top coefficient,
J_T* size 249,
P_R*(beta) nonzero,
Vandermonde noncontainment,
strict distance 249 < 250.

Return PROOF or ROUTE_CUT. If it fails, state whether Cycle116 agreement-262
still suffices for ABF Definition 4.3.
```

## Role 5: Submission-Prose Referee

```text
Audit the Cycle120 theorem note as if for a coding theory referee.

Does it use standard notation?
Does it overclaim?
Does it clearly distinguish theorem, ABF consequence, strict addendum,
and non-claims?
Is it suitable to become the main PDF for an arXiv/ePrint timestamp after
human editing?

Return ACCEPTABLE_DRAFT or REVISION_REQUIRED with exact edits.
```

## Role 6: Prize-Facing Implication Auditor

```text
Audit the exact implication:

If ABF Definition 4.3 is the grand MCA challenge definition, and the
Cycle116 theorem is correct, does
  LD_sw(C,262) >= 52,747,567,092
imply
  epsilon_mca(C,125/256) >= 52,747,567,092 / 17^32 > 2^-128
for C=RS[F_17^32,H,256]?

Check all denominators, quantifiers, support thresholds, and monotonicity.

Return IMPLICATION_VALID or ROUTE_CUT with the first fatal line.
```
