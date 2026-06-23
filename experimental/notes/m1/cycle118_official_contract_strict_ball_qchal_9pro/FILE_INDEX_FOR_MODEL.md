# File Index For Model - Cycle118

Read in this order.

## Orientation

```text
CURRENT_STATE.md
COMMON_PROMPT.md
SELF_AUDIT_ADDENDUM.md
ROLE_XX_*.md
```

## Canonical Board And Audits

```text
context/RS_MCA_CANONICAL_TRACKER.md
context/audits/m1_cycle117_extension_field_qchal_source_contract_returns_audit.md
context/audits/m1_cycle116_standalone_c84_to_rs_mca_ld_transfer_returns_audit.md
context/audits/m1_cycle115_cycle84_to_mca_transfer_returns_audit.md
context/audits/m1_cycle114_pinned_official_source_root_decider_returns_audit.md
context/audits/m1_cycle113_frozen_source_contract_replay_returns_audit.md
```

## Source Definitions

```text
context/source/RS_disproof_v3.tex
context/source/slackMCA_v3.tex
context/source/m2_line_decoding_mca_bridge.md
```

Important anchors:

```text
RS_disproof_v3.tex: definition of support-wise line-MCA error
RS_disproof_v3.tex: smooth extension tower theorem
slackMCA_v3.tex: support-wise agreement / line-MCA definition
m2_line_decoding_mca_bridge.md: exact eps_mca / LD_sw bridge and strict external-LD warning
```

## Cycle116 Finite Transfer Certificate

```text
context/cycle116_verifier/14_V-CYCLE116-STANDALONE-C84-TO-RS-MCA-LD-TRANSFER-CERTIFICATE.md
context/cycle116_verifier/18_verify_cycle116_transfer_hypotheses.py
context/cycle116_verifier/19_cycle116_checker_receipt.json
context/cycle116_verifier/cycle116_role08_verifier/
```

Use these for the already-banked theorem:

```text
C = RS[F_17^32,H,256], |H|=512
LD_sw(C,262) >= 52,747,567,092
epsilon_mca(C,125/256) >= 52,747,567,092 / 17^32
q_gen = q_code = q_line = 17^32
q_chal = null
```

## Cycle117 Source-Contract Checker

```text
context/cycle117_checker/CHECKER_SPEC.md
context/cycle117_checker/EXPECTED_RECEIPT.json
context/cycle117_checker/observed_checker_receipt.json
context/cycle117_checker/observed_self_tests.out
context/cycle117_checker/cycle117_source_contract_checker.zip
context/cycle117_checker/unpacked/cycle117_source_contract_checker/
```

Use these for the current source-contract result:

```text
SOURCE_ACCEPTED_CYCLE116_ROW
QCHAL_UNDEFINED_FINITE_MCA_ONLY
EVENT_RETAINED
SOURCE_CONTRACT_MISSING_NO_CLAIM
```

## Dispatch Metadata

```text
DISPATCH_RECEIPT.md
SHA256SUMS.txt
```

## Claim Boundary

This packet is not asking you to re-prove Cycle116 from scratch unless your role
requires it. It is asking you to push the next boundary:

```text
official adoption
strict-ball / agreement-263 upgrade
q_chal / field-thickening
accepted-field compiler fallback
```

