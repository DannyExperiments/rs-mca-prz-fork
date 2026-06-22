# Cycle112 Source AP_corr / t=1 Block Packet 9-Pro Packet

Purpose: dispatch nine ChatGPT Pro theorem-worker lanes against the source
admissibility-or-charge wall left by Cycle111.

Live target:

```text
L-CYCLE112-SOURCE-APCORR-T1-BLOCK-PACKET-ADMISSIBILITY-OR-CHARGE
```

Packet layout:

- `CURRENT_CYCLE112_STATE.md`: concise live wall and guardrails.
- `context/RS_MCA_CANONICAL_TRACKER.md`: canonical board state at packet build.
- `context/agents-log.md`: experimental activity log at packet build.
- `context/m1_cycle111_low_t1_occupancy_upper_returns_audit.md`: Cycle111 audit.
- `context/m1_cycle110_low_calibrated_occupancy_returns_audit.md`: previous route context.
- `context/cycle111_clean_returns/`: clean Cycle111 role responses and hashes.
- `prompts/COMMON_PROMPT.md`: shared instructions.
- `prompts/SELF_AUDIT_ADDENDUM.md`: mandatory self-audit.
- `prompts/ROLE_*.md`: nine role prompts.
- `combined/COMBINED_*.md`: one-paste prompt per Pro instance.

Dispatch discipline:

1. Upload the zip to each of nine fresh Pro instances.
2. Paste exactly one `combined/COMBINED_*.md` prompt per instance.
3. No Internet. Use MAX reasoning.
4. Preserve raw returns and generated files before auditing.
5. Do not overclaim: source-validity and official charge receipts are the target.
