# Cycle111 LOW t=1 Occupancy Upper 9-Pro Packet

Purpose: dispatch nine fresh ChatGPT Pro theorem-worker lanes against the first
charge-irreducible LOW wall:

```text
L-CYCLE111-LOW-T1-OCCUPANCY-UPPER
```

Packet layout:

- `CURRENT_CYCLE111_STATE.md`: concise current target and guardrails.
- `context/RS_MCA_CANONICAL_TRACKER.md`: canonical board state at packet build.
- `context/agents-log.md`: experimental activity log at packet build.
- `context/m1_cycle110_low_calibrated_occupancy_returns_audit.md`: previous
  round audit.
- `context/m1_cycle109_interior_stratified_cover_returns_audit.md`: prior
  route context.
- `context/cycle110_returns_raw/`: preserved Cycle110 raw returns and hashes.
- `prompts/COMMON_PROMPT.md`: shared instructions.
- `prompts/SELF_AUDIT_ADDENDUM.md`: mandatory self-audit.
- `prompts/ROLE_*.md`: nine role prompts.
- `combined/COMBINED_*.md`: one-paste prompt per Pro instance.

Dispatch discipline:

1. Upload the zip to each of nine fresh Pro instances.
2. Paste exactly one `combined/COMBINED_*.md` prompt per instance.
3. No Internet. Use MAX reasoning.
4. Preserve raw returns and generated files before auditing.
5. Audit with literal labels:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

