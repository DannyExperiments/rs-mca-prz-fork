# Cycle 88 Prompt - Cycle87 Certificate To Official MCA Bridge

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?

## Context

You are working on the RS-MCA / Proximity Prize research lane. The latest
banked result is Cycle87, a certificate-level pass for an explicit
`U`-separator 464-point construction.

Attached context includes:

- `m1_cycle87_explicit_separator_returns_audit.md`
- `02_CYCLE87_U_SEPARATOR_PROOF.md`
- `02_cycle87_master_certificate.json`
- `02_cycle87_u_separator_replay_bundle.zip`
- `02_cycle87_explicit_two_copy_separator_certificate.zip`
- `06_cycle87_u_separator_pass.json`
- `06_cycle87_u_smooth_census_result.json`
- `08_cycle87_certificate_engineer_bundle.zip`
- raw-folder checksums and agents log excerpt

Codex local audit already verified:

- downloaded bundle internal SHA256SUMS;
- `cycle87_verify_master.py`;
- setup verifier;
- 464 GRS artifact verifier;
- projective census aggregation;
- symbolic threshold verifier;
- Role08 checker-bundle smoke verifiers.

Codex did **not** independently rerun the full 52,747,567,104-record census.
Treat Cycle87 as:

`PROOF_CERTIFICATE_PASS / BANKABLE_LEMMA / INDEPENDENT_REPLAY_PENDING`

not as a main-paper theorem.

## Decisive Cycle87 Certificate Values

The certificate claims:

```text
profile: (n,k,sigma,j,t) = (464,232,6,226,1)
q_gen = q_code = q_line = q_chal = 17^48
records P = 52,747,567,104
projected distinct keys = 52,747,567,062
projected ordered off-diagonal energy = 84
projected max multiplicity = 2
smooth/projective histogram: m1 = 52,747,567,020; m2 = 42; m_ge_3 = 0
floor(q_line / 2^128) = 338,617,018,271,848,945,628
certified distinct slopes = 1,391,152,917,379,006,070,784
margin over target = 1,052,535,899,107,157,125,156
```

The construction is said to be one fresh `[464,232]` GRS code over
`L = F_17^48`, not ordinary puncturing of the previous one-copy code. It uses a
single affine syndrome line and the explicit separator `U` where
`L = F0[U]/(U^3-(X+2))`, `F0 = F_17[X]/(X^16+X^8+3)`.

## Task

Audit and either prove or kill the exact bridge:

```text
L-CYCLE87-464-U-OFFICIAL-MCA-FAIL-ROW
```

Meaning:

> The Cycle87 certificate package, if its finite replay is trusted, yields a
> valid official finite MCA failure row at rate `rho = 1/2` with
> `(n,k,sigma)=(464,232,6)`, field/challenge size `17^48`, and numerator
> exceeding `floor(q_line / 2^128)`.

You must decide whether the bridge is theorem-valid, conditionally valid, or
false.

## Required Self-Audit

Before finalizing, explicitly answer:

1. What exact implication did you prove, and what exact implication did you not
   prove?
2. Is the result official-prize-relevant, or only a finite/model/research
   certificate?
3. What is the first line in the reduction chain where the theorem could fail?
4. Are `q_gen`, `q_line`, `q_code`, `q_chal`, and the `2^-128` target being used
   correctly?
5. Could quotient/periodic structure, contained incidences, same-slope
   collisions, projectivization, or affine color normalization reduce the
   claimed numerator?
6. If your answer is a `PLAN`, what exact theorem/checker/counterpacket would
   convert it into `PROOF` or `COUNTERPACKET`?

Do not hide behind broad language. Give the exact next lemma, exact missing
hypothesis, or exact counterexample mechanism.

## Output Format

Start with one label:

- `PROOF`
- `COUNTERPACKET`
- `BANKABLE_LEMMA`
- `ROUTE_CUT`
- `EXACT_NEW_WALL`
- `AUDIT`
- `PLAN`

Then include:

1. Executive verdict and confidence.
2. Exact theorem or counterpacket statement.
3. Proof or obstruction, with all field/cardinality arithmetic explicit.
4. Certificate/replay requirements.
5. Next exact lemma or construction.

If the certificate package is insufficient, say exactly what is missing. If the
bridge is valid only conditional on independent full replay, state that
condition precisely.
