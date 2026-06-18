# Cycle 17 Audit: Rank-Det Split Scanner Attempt

Status: AUDIT / HARNESS_MALFORMED_VISIBLE_TERMINAL.

Primary classification: AUDIT.

## Target

`W-F1-AA-RES-T2J3-RANK-DET-SPLIT`

Cycle 16 banked the safe side:

```text
D=F_p, t=sigma=2, j=3, off R0,
Q(z_0,z_1) not identically zero => C2 <= 4p = O(n).
```

The Cycle 17 prompt asked for an implementable scanner/certificate for the
remaining `Q==0` branch with the distinct `D`-split cubic condition retained.

## Harness Result

The VS Code credited-terminal wrapper completed but classified the run as
`HARNESS_MALFORMED_VISIBLE_TERMINAL`.

Recorded harness facts:

- `run_result.json`: `ok=false`, `classification=HARNESS_MALFORMED_VISIBLE_TERMINAL`.
- `response.md`: absent.
- `output_files/`: no deliverables were written.
- `response_malformed_visible_terminal.md`: visibly corrupted terminal scrape.
- `response_recovered_claude_jsonl.md`: readable structured-JSONL recovery, but
  the normalized run did not promote it to `response.md`.

Under the loop rules, this is not a theorem artifact and should not be treated
as a promoted mathematical result.

## What Can Be Preserved

The readable recovered text is useful as provenance only. It proposes an
AUDIT-only checker/spec for the `Q==0` branch:

- keep ledgers separate: `B=F_p`, `q_gen=p`, `F=F_{p^2}`, `q_line=p^2`,
  `q_chal` unused;
- test `Q(z_0,z_1) == 0` directly by evaluating the determinant
  `det[c1(z)|c2(z)|c3(z)|c0(z)]` over all of `B^2`;
- retain the distinct `D`-split cubic condition `T subset F_p`, `|T|=3`;
- emit certificates with `p`, `q_gen`, `q_line`, `E`, `Bnum`, `off_R0`,
  `Q_identically_zero`, `split_triples_examined`, `C2`, fiber summaries, and
  status;
- regard a single-prime run as EXPERIMENTAL only;
- require a growing-prime family with `Q==0` and `C2/p^2` bounded below before
  calling a counterpacket candidate.

These are reasonable scanner-design desiderata, but Cycle 17 did not produce an
executed checker, a verified certificate, or a source-checked proof.

## What Is Not Banked

Do not bank any of the following from Cycle 17:

- a proof of `conj:B`;
- a counterpacket;
- a corrected-reserve statement;
- a `q_gen` / `q_line` transfer;
- a protocol, MCA, CA, list-decoding, line-decoding, or SNARK consequence;
- the inline scanner as a working script;
- any finite sample result.

## Current State After Cycle 17

The live wall remains:

```text
W-F1-AA-RES-T2J3-RANK-DET-SPLIT
```

The next useful technical task is either:

1. write and execute a source-checked scanner for the `Q==0` split-distinct
   branch; or
2. attempt a higher-level proof/counterpacket that bypasses the scanner and
   makes a larger leap on F1 / corrected MCA.

Cycle 18 is therefore allowed to be a high-upside "homerun" prompt, provided it
keeps all field ledgers separate and does not promote experimental statements to
proof.
