# Provenance

## Git Commits

The Cycle119 strict-263 work is currently recorded on:

```text
branch: cycle58-5p5-audit
remote: przfork = https://github.com/DannyExperiments/rs-mca-prz-fork.git
```

Relevant commits:

```text
0f4419cd97ef8dea702379bfe3ac758f5a9242c4
  Audit Cycle119 strict-263 returns

d38247ad404058bde41610b3235958c2f4d76b6c
  Prepare Cycle119 cold strict-263 packet

e62898d44be5719e40b89e1945b34c16066cc1c2
  Harden Cycle119 cold packet
```

## Cold Packet

Current hardened cold packet:

```text
experimental/notes/m1/cycle119_cold_strict263_prize_candidate_packet.zip
```

SHA-256:

```text
8fc5efd09dd220dd5aa5e0edbc57df5e00bca67d4e1c08c10bbf7ee777839326
```

## Local Replay

Two-ended checker local replay terminal:

```text
CYCLE118_TWO_ENDED_AGREEMENT_263_TRANSFER_VERIFIED
```

Receipt:

```text
experimental/notes/m1/cycle119_role05_twoended_qchal_goldilocks_9pro_returns_raw/03_role03_local_replay_receipt.json
```

Key fields:

```text
agreement = 263
strict_hamming_distance_upper_bound = 249
distinct_slopes = 52,747,567,092
hidden_seventh_top_coefficient_used = false
two_ended_selector_degrees = [0,250,251,252,253,254,255]
q_chal = null
```

## Raw Artifacts

Preserved raw/generated returns:

```text
experimental/notes/m1/cycle119_role05_twoended_qchal_goldilocks_9pro_returns_raw/
```

Raw artifact hash list:

```text
experimental/notes/m1/cycle119_role05_twoended_qchal_goldilocks_9pro_returns_raw/SHA256SUMS.txt
```

## Notes Sent / Prepared For PRZ

Short PRZ-facing note:

```text
experimental/notes/m1/cycle119_prz_strict263_note.md
```

Cold theorem note:

```text
experimental/notes/m1/cycle119_cold_strict263_prize_candidate_packet.md
```

Submission-prep note:

```text
experimental/notes/m1/cycle119_submission_packet/THEOREM_NOTE.md
```

