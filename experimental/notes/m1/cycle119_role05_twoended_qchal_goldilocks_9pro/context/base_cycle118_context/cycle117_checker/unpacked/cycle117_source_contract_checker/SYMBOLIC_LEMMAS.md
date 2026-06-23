# Symbolic / Source-Text Lemmas

The checker verifies bytes, line slices, JSON fields, arithmetic, the existing Cycle116 executable verifier, and absence/presence of literal contract keys. It does **not** prove the semantic implications below by program synthesis. These are the only proof obligations left as compact, hash-pinned lemmas.

## L1 — Attached-manuscript row admissibility

**Statement.** Under the definitions in the pinned manuscripts, the row

```text
C = RS[F_17^32,H,256],  H=<theta>,  |H|=512
```

is a smooth multiplicative Reed–Solomon row admitted by the source.

**Proof.** `RS_GENERAL_SMOOTH_ROW` defines `RS[F,D,k]` over a field `F` and calls a power-of-two multiplicative subgroup smooth. `RS_EXTENSION_FIELD_CONSTRUCTION` and `RS_EXTENSION_FIELD_THEOREM` explicitly admit generated extension-field rows `RS[F_{p^d},D,k]`. Instantiate `p=17`, `m=2^{v_2(16)}=16`, `d=32`, `n=md=512`, and `rho=1/2`, so `k=256`. The executable Cycle116 verifier proves that `theta` has order `512` and that `H=<theta>` generates `F_17^32`. Hence the exact Cycle116 row satisfies the source’s mathematical row contract. This proves `SOURCE_ACCEPTED_CYCLE116_ROW` **only for the attached manuscript source profile**.

## L2 — Field ledger and denominator

**Statement.** For the Cycle116 row,

```text
q_gen = q_code = q_line = 17^32,
q_chal = null.
```

**Proof.** `C116_Q_LEDGER_AND_SCOPE` proves that `H` generates `K=F_17^32`, so `q_gen=17^32`; the code alphabet is `K`, so `q_code=17^32`. `RS_SUPPORTWISE_MCA_DEFINITION` and `SLACK_SUPPORTWISE_MCA_DEFINITION` quantify the line parameter as `z in F` and divide by `|F|`; with `F=K`, `q_line=17^32`. `SLACK_SUBFIELD_CORRECTION` does not reduce this ledger because `H` is not contained in a proper subfield. No attached clause defines a protocol challenge field, so `q_chal` stays null. It must not be set equal to `q_line` by inference.

## L3 — Event retention under the attached source definition

**Statement.** The `N=52,747,567,092` distinct Cycle116 slopes are retained as `N` support-wise MCA-bad parameters under the pinned manuscript definitions.

**Proof.** The Cycle116 verifier and `C116_PADDING_RETENTION_AND_THRESHOLD` provide one affine line and `N` distinct slopes, each with a support of size `262` on which the line point is code-explained. `C116_NONCONTAINMENT_PROOF` proves that the direction word is not code-explainable on each designated support, which is stronger than the simultaneous-explanation failure required by `RS_SUPPORTWISE_MCA_DEFINITION` and `SLACK_SUPPORTWISE_MCA_DEFINITION`. The raw source event is the field element `z`; the definitions contain no endpoint deletion, affine-color quotient, retained-event map, or charge registry. Same-slope collisions have already been deducted in the occupancy `N`. `SLACK_QUOTIENT_PERIODIC_ANALYTIC_ROLE` and `SLACK_QUOTIENT_PERIODIC_FLOOR_SEPARATION` place quotient-periodic structure in later analytic bounds and explicitly separate its floor; they do not alter the raw event definition. The tangent floor is an additional lower bound. Therefore the attached-source event terminal is `EVENT_RETAINED`.

This lemma does **not** assert that an absent official protocol wrapper retains the events.

## L4 — Exact `LD_sw` adapter, and the external line-decodability cut

**Statement.** For the support-wise object defined in the bridge note,

```text
epsilon_mca(C,delta)
  = LD_sw(C,ceil((1-delta)n)) / |F|.
```

At `n=512`, `delta=125/256`, the agreement is exactly `262`.

**Proof.** `M2_LDSW_EXACT_BRIDGE` defines `LD_sw` using the same pairs `(f,g)`, slopes `z`, witness supports, and simultaneous-explanation failure as the manuscript MCA definition. The only conversion is the integer condition `|S| >= (1-delta)n`, equivalent to `|S| >= ceil((1-delta)n)`. Direct arithmetic gives `ceil((1-125/256)512)=262`.

The attached materials do not define an external official `(delta,a_LD,n+1)` line-decodability predicate. `M2_EXTERNAL_DEFINITION_STILL_TO_MATCH` explicitly leaves that comparison as a follow-up check. Therefore the package certifies `LD_sw`, not an unqualified external line-decodability theorem and not ordinary list decoding.

## L5 — `2^-128` threshold arithmetic

**Statement.** The threshold crossing is true:

```text
floor(17^32 / 2^128) = 6,
52,747,567,092 > 6.
```

**Proof.** This is checked by exact integer arithmetic. It is not the main mathematical content: only seven distinct slopes would cross the threshold. The substantive content is the explicit one-line packet of `52,747,567,092` support-wise noncontained slopes and its finite transfer proof.

## L6 — Primitive-log gauge normalization

**Statement.** The reviewer package uses only the executable primitive-log gauge `beta=X+2`.

**Proof.** The executable slot logs and Cycle116 verifier bind the generator to coefficient vector `[2,1]`, i.e. `X+2`, and verify it is primitive. The legacy master-display field `[1,1]`, i.e. `X+1`, is retained only as quarantined metadata. No numerical log from the `X+1` display gauge is consumed by this package. Thus no two-gauge numerical identity is asserted and no reindexing receipt is required.

## L7 — Official-contract wall

**Statement.** The attached files do not decide official/prize admission.

**Proof.** `RS_CAPACITY_TRANSCRIPTION_SCOPE` says the manuscript’s conjecture is a minimal no-slack transcription of the challenge. `RS_PROTOCOL_SCOPE_CUT` says protocol-specific constraints are absent and protocol soundness is untouched. `C116_OFFICIAL_CONTRACT_WALL` names the missing authority-pinned admission/source/challenge-field contract. Therefore the official terminal is

```text
SOURCE_CONTRACT_MISSING_NO_CLAIM.
```

It is neither `SOURCE_REJECTED_CYCLE116_ROW` nor an official acceptance.

## L8 — Optional official-contract semantic attestation

**Statement.** A future official contract can be machine-checked for byte identity, authority pinning, schema completeness, exact clause locations, field ledgers, and exhaustive event classifications, but the checker cannot decide natural-language entailment from the authoritative document by syntax alone.

**Proof obligation.** The independently supplied SHA-256 trust pin must authenticate a contract curated or issued by the relevant authority. That contract attests the semantic readings `ACCEPT`/`REJECT`, the role of `q_chal`, and each event action. The checker verifies that every attestation cites an exact hash-pinned source slice and that challenge-field filtering is one of the exhaustive event families. It does not treat an unpinned JSON file, a self-declared authority, or a keyword match as semantic evidence. Thus a future `PROOF` result is conditional on the external trust pin authenticating the contract's semantic extraction; without that pin the terminal remains `SOURCE_CONTRACT_MISSING_NO_CLAIM` or the checker rejects.
