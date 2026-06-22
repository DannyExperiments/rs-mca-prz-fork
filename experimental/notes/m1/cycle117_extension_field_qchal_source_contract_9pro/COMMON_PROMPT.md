# Common Prompt - Cycle117 Extension-Field Source Contract

You are one of nine independent theorem workers. You have an attached context
packet. Your task is to attack the next exact wall in the RS-MCA / Proximity
Prize project:

```text
V-CYCLE116-EXTENSION-FIELD-QCHAL-SOURCE-CONTRACT
```

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning. Do you see a route to a full solve? If yes, what is the next exact
lemma or construction?

## Known Banked Finite Theorem

Cycle116 proves the following finite smooth-domain standard Reed-Solomon
support-wise MCA / `LD_sw` theorem:

```text
C = RS[F_17^32, H, 256],  H=<theta>,  |H|=512

LD_sw(C,262) >= 52,747,567,092

epsilon_mca(C,125/256)
  >= 52,747,567,092 / 17^32
  > 2^-128
```

The proof uses:

```text
P_T(X)=X^113-X^112+O(X^107)
P_T(beta)=4(beta-1) Phi(T)
```

plus a fixed-jet locator-to-RS-MCA transfer and a smooth agreement-padding lift.

Do not reprove Cycle116 unless needed. Treat it as a finite theorem supported by
the verifier package in `context/cycle116_verifier/`.

## Your Target

Decide whether the attached source materials promote this finite theorem into
the official/source setting, or identify the first exact blocking clause.

You must answer:

1. Does the source formulation accept the extension-field row
   `RS[F_17^32,H,256]` as a valid smooth-domain RS row?
2. Is the line parameter field for `z` exactly `F_17^32`, so that
   `q_line=17^32` is the denominator in `epsilon_mca`?
3. Is `q_chal` relevant? If yes, what is it and what source clause defines it?
   If no, state why it remains unset for the code/line-MCA theorem.
4. Do endpoint, periodic, quotient, tangent, contained-line, affine-color,
   retained-event, or charge rules remove/pay any of the
   `52,747,567,092` support-wise bad slopes?
5. Does the result imply any source notion of line-decodability failure, or only
   support-wise MCA / `LD_sw`?
6. If the extension-field row is rejected, what is the next exact compiler
   theorem needed to move the fixed-jet occupancy into an accepted field/domain?

## Allowed Labels

Use exactly one primary label:

```text
PROOF
```

Use only if you prove the source/admissibility theorem: the row is admitted, the
denominator is correct, events are retained, and the official/source implication
follows.

```text
COUNTERPACKET
```

Use only if you establish a source-valid official counterpacket, not merely the
finite Cycle116 theorem.

```text
BANKABLE_LEMMA
```

Use if you prove a durable adapter lemma but do not close the whole source
contract.

```text
ROUTE_CUT
```

Use if you identify the first exact clause rejecting or failing to define the
promotion.

```text
EXACT_NEW_WALL / AUDIT / PLAN
```

Use only if no proof/cut is possible; name the next theorem/checker precisely.

## Required Output Format

Return a structured markdown answer with these sections:

1. `LABEL`
2. `EXECUTIVE VERDICT`
3. `SOURCE-PINNED THEOREM OR ROUTE CUT`
4. `PROOF DETAILS`
5. `FIELD AND PARAMETER LEDGER`
6. `EVENT RETENTION / CHARGE AUDIT`
7. `LINE-DECODING VS LD_SW ADAPTER`
8. `VERIFIER / REVIEWER CHECKLIST`
9. `SELF-AUDIT`
10. `NEXT EXACT STEP`

Be aggressive about not overclaiming. If the source does not contain an
authority-pinned contract, say so and give the smallest exact missing clause.

No Internet. Use only the attached files.
