# File Index For Cycle119 Model Packet

Attach the zip and read this file first.

## Top-Level State

- `CURRENT_STATE.md` - director summary, target theorem, and success/failure criteria.
- `COMMON_PROMPT.md` - shared instructions for all nine instances.
- `SELF_AUDIT_ADDENDUM.md` - mandatory self-audit.
- `ROLE_01_TWO_ENDED_PROOF_BUILDER.md` through `ROLE_09_GRAND_REFEREE_SYNTHESIS.md` - role-specific prompts.
- `DISPATCH_RECEIPT.md` - dispatch record scaffold.

## Context

- `context/RS_MCA_CANONICAL_TRACKER_CURRENT.md` - current canonical board.
- `context/m1_cycle118_official_contract_strict_ball_qchal_returns_audit.md` - corrected Cycle118 audit.
- `context/base_cycle118_context/` - source docs and previous checker material from the Cycle118 packet.
- `context/cycle118_returns/05_role05_response.md` - Role05 target theorem candidate, verbatim.
- `context/cycle118_returns/07_role07_response.md` - corrected qchal/scalar-extension dichotomy, verbatim.
- `context/cycle118_returns/08_role08_response.md` - Goldilocks fallback candidate, verbatim.
- `context/cycle118_returns/09_role09_response.md` - safer 2187-slope strict packet, verbatim.
- `context/cycle118_returns/01_role01_response.md` through `09_role09_response.md` - all Cycle118 visible responses.
- `context/cycle118_returns/SHA256SUMS.txt` - raw return hashes after Role07 correction.

## Key Source/Verifier Files Inside Base Context

- `context/base_cycle118_context/source/slackMCA_v3.tex`
- `context/base_cycle118_context/source/RS_disproof_v3.tex`
- `context/base_cycle118_context/source/m2_line_decoding_mca_bridge.md`
- `context/base_cycle118_context/cycle116_verifier/14_V-CYCLE116-STANDALONE-C84-TO-RS-MCA-LD-TRANSFER-CERTIFICATE.md`
- `context/base_cycle118_context/cycle116_verifier/18_verify_cycle116_transfer_hypotheses.py`
- `context/base_cycle118_context/cycle116_verifier/19_cycle116_checker_receipt.json`
- `context/base_cycle118_context/cycle117_checker/CHECKER_SPEC.md`
- `context/base_cycle118_context/cycle117_checker/EXPECTED_RECEIPT.json`
- `context/base_cycle118_context/cycle117_checker/observed_checker_receipt.json`

## Priority Reading Order

1. `CURRENT_STATE.md`
2. `context/m1_cycle118_official_contract_strict_ball_qchal_returns_audit.md`
3. Your assigned role prompt
4. If you are a Role05 attacker or falsifier: `context/cycle118_returns/05_role05_response.md`
5. If you are a qchal role: `context/cycle118_returns/07_role07_response.md` and the source TeX files
6. If you are the Goldilocks role: `context/cycle118_returns/08_role08_response.md`
7. Use Cycle116/117 checker files only when needed to pin definitions or build replay specs.
