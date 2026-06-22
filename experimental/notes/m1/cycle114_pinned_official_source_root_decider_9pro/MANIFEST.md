# Cycle114 Pinned Official Source Root Decider Packet

Purpose:

```text
V-CYCLE114-PINNED-OFFICIAL-SOURCE-ROOT-P190-OR-C284-DECIDER
```

This packet asks nine independent workers to decide whether the official source
root needed for the P190/C284 replay is present in the attached source files.
If present, they must replay the stress packets through source adapter,
official `AP_corr`, final retained events, charges, and `q_line` ledger. If
absent, they must fail closed with `SOURCE_RECEIPT_MISSING_NO_CLAIM`.

Important files:

```text
CURRENT_CYCLE114_STATE.md
prompts/COMMON_PROMPT.md
prompts/SELF_AUDIT_ADDENDUM.md
prompts/ROLE_01_...md through ROLE_09_...md
combined/COMBINED_01_...md through COMBINED_09_...md
context/source_docs/readme.md
context/source_docs/agents.md
context/source_docs/*.tex
context/RS_MCA_CANONICAL_TRACKER.md
context/agents-log.md
context/rs_mca_board_findings_for_codex_director_20260622.md
context/m1_cycle111_low_t1_occupancy_upper_returns_audit.md
context/m1_cycle112_source_apcorr_t1_block_packet_returns_audit.md
context/m1_cycle113_frozen_source_contract_replay_returns_audit.md
context/cycle112_returns/*_response.md
context/cycle113_returns/*_response.md
```

Terminal decisions:

```text
SOURCE_REJECTED
COLOR_COMPRESSED_OR_CHARGED
SOURCE_VALID_LOW_T1_COUNTERPACKET
T1_APCORR_LOCAL_LIMIT
SOURCE_RECEIPT_MISSING_NO_CLAIM
RESOURCE_EXHAUSTED_NO_CLAIM
```

Claim discipline:

- No internet.
- No official predicate may be invented.
- No finite/model/source-route evidence may be promoted to prize proof.
- `q_line` is the final denominator; `q_gen`, `q_code`, and `q_chal` cannot be
  double-counted.

