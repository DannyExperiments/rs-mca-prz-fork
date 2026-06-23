# Role 07: qchal Sampler-Map Contract

Your job is to turn corrected Role07's dichotomy into a precise checker/contract.

Read:

```text
context/cycle118_returns/07_role07_response.md
context/base_cycle118_context/source/slackMCA_v3.tex
context/base_cycle118_context/source/RS_disproof_v3.tex
context/base_cycle118_context/cycle117_checker/CHECKER_SPEC.md
context/base_cycle118_context/cycle117_checker/EXPECTED_RECEIPT.json
context/base_cycle118_context/cycle117_checker/observed_checker_receipt.json
```

Define a fail-closed receipt schema with fields:

```text
authority_root
source_definition_hash
challenge_space
challenge_distribution
q_chal
line_field
challenge_to_line_parameter_map
bad_event_pullback_or_filter
duplicate_policy
quotient_or_charge_policy
final_retained_numerator
```

The checker must output exactly one of:

```text
DIRECT_K_SAMPLING_CYCLE116_DENSITY_RETAINED
BALANCED_CHALLENGE_PROJECTION_NO_LOSS
IDENTITY_E_SCALAR_EXTENSION_CYCLE116_LINE_KILLED
OFFICIAL_EVENT_FILTER_DROPS_BELOW_THRESHOLD
UNDEFINED_MAP_NO_OFFICIAL_CLAIM
```

Also prove the mathematical lemma behind each terminal: why balanced projection preserves density, why identity scalar extension kills density, and why missing map means no official claim.

Do not invent official authority. If it is absent from the packet, return that exact absence.
