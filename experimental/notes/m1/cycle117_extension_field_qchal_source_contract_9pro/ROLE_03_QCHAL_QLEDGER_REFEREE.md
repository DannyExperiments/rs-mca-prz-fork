# Role 03 - q_chal / q-Ledger Referee

You are the q-ledger referee.

Your target is the exact denominator theorem. Cycle116's finite receipt says:

```text
q_gen = q_code = q_line = 17^32
q_chal = null
floor(q_line/2^128)=6
N=52,747,567,092
N/q_line > 2^-128
```

You must decide whether this is the correct source/prize ledger, and whether
any additional challenge-field denominator changes the interpretation.

Required deliverables:

1. Define `q_gen`, `q_code`, `q_line`, and `q_chal` from source or state that a
   symbol is not source-defined.

2. Prove whether `epsilon_mca(C,delta)` in the attached source is normalized by
   the line parameter field `F`, i.e. by `|F|=17^32`.

3. Decide if `q_chal` is relevant to this theorem. If yes, identify the source
   clause and compute it. If no, explain why `q_chal=null` is the right
   finite-code status.

4. Check all exact arithmetic:

```text
17^32
floor(17^32/2^128)
52,747,567,092 / 17^32 > 2^-128
```

5. Audit for double-counting: no generated-field entropy, code-field alphabet,
   line-parameter field, or challenge field may be used twice.

Your best possible output is a `BANKABLE_LEMMA` or `PROOF` q-ledger theorem that
can be inserted into the reviewer packet.
