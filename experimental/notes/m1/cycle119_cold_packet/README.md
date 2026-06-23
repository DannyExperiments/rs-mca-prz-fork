# Cycle119 Cold Strict-263 Packet

Date: 2026-06-23

## Open First

Read:

```text
cycle119_cold_strict263_prize_candidate_packet.md
```

This is the clean theorem note. It removes the Pro-role/process chatter and states:

```text
LD_sw(RS[F_17^32,H,256],263) >= 52,747,567,092.
```

The strict radius arithmetic is:

```text
512 - 263 = 249 < 250 = (125/256)*512.
```

Thus, under the source support-wise MCA definition with line parameter sampled uniformly from `F_17^32`,

```text
epsilon_mca(C,125/256)
  >= 52,747,567,092 / 17^32
  > 2^-128.
```

## What Is New Relative To Cycle116

Cycle116 proved the agreement-262 finite/source theorem.

Cycle119 proves a two-ended locator theorem that upgrades the same Cycle84 numerator to agreement 263. The two-ended theorem uses:

```text
common top six locator coefficients
+
common nonzero constant coefficient
```

for the augmented degree-249 locators.

It uses selected product coefficients:

```text
0, 250, 251, 252, 253, 254, 255
```

and explicitly does not use the varying degree-243 coefficient. This avoids assuming a hidden seventh top jet.

It also avoids the invalid naive padding argument:

```text
degree <137 + degree 120 can hit degree 256,
but RS[*,*,256] requires degree <256.
```

Instead the final line is constructed directly in the final `[512,256]` parity-check space.

## Key Files

```text
cycle119_cold_strict263_prize_candidate_packet.md
  Clean theorem note.

cycle119_prz_strict263_note.md
  Short PRZ-facing explanation.

m1_cycle119_role05_twoended_qchal_goldilocks_returns_audit.md
  Full director audit of the nine Pro returns and downloaded artifacts.

03_role03_local_replay_receipt.json
  Local replay receipt for the two-ended transfer checker.

08_role08_local_checker_receipt.json
  Local Goldilocks fallback checker receipt.

raw_SHA256SUMS.txt
  Hashes for the preserved raw/generated return artifacts.
```

## Local Replay Terminal

The important local terminal is:

```text
CYCLE118_TWO_ENDED_AGREEMENT_263_TRANSFER_VERIFIED
```

The receipt records:

```text
agreement = 263
strict_hamming_distance_upper_bound = 249
distinct_slopes = 52,747,567,092
hidden_seventh_top_coefficient_used = false
two_ended_selector_degrees = [0,250,251,252,253,254,255]
q_gen = q_code = q_line = 17^32
q_chal = null
```

## What This Packet Does Not Claim

This packet does not claim:

```text
ordinary fixed-word list decoding;
protocol soundness failure;
an asymptotic theorem;
an official Proximity Prize solve without definition matching;
a prime-field theorem for this exact Cycle84 row;
any independent q_chal denominator;
any challenge-map or event-retention theorem.
```

## Official Admissibility Question

The exact remaining question is:

```text
Does the official grand MCA challenge admit:

1. the row RS[F_17^32,H,256], |H|=512;
2. H as a smooth multiplicative evaluation domain;
3. support-wise epsilon_mca as the governing predicate;
4. gamma sampled uniformly from F_17^32;
5. no additional endpoint, quotient, periodic, charge, challenge-map,
   or event-retention filter?
```

If yes, this packet is a Proximity Prize counterexample candidate at:

```text
delta = 125/256,
epsilon_mca > 2^-128.
```

If no, the next theorem target is determined by the first rejected clause.

