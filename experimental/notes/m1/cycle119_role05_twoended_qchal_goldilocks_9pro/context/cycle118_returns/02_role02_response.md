LABEL:

`ROUTE_CUT / BANKABLE_LEMMA / CHECKER_COUNTERMODEL` — confidence: high.

EXECUTIVE VERDICT:

Official promotion fails at the first official semantic clause:

```text
attached-manuscript extension-field admissibility
    ⇏ authority-adopted extension-field admissibility.
```

More precisely, an even earlier authentication precondition fails: the packet contains no authority-issued contract, authoritative document, or independently supplied trust pin. The local schema and checker are not official evidence.

The strongest additional result is:

```text
Cycle116 already gives a noncontained affine line containing at least
52,747,567,092 distinct closed-ball close points at Hamming distance <=250.
```

Thus agreement `262` is sufficient for any external line-decoding predicate using the closed ball

```text
dist_H(u,C) <= (125/256)·512 = 250.
```

It is not sufficient for a strict-ball predicate `dist_H(u,C)<250`, which requires agreement `263`.

There is also a concrete defect in the proposed official-contract checker: its v1 schema records neither the distance convention nor the official base predicate nor the challenge distribution. I constructed a schema-valid, hash-pinned synthetic contract whose source document explicitly requires the strict ball and whose row/event fields say `ACCEPT`/`RETAIN`. The unmodified checker emitted:

```text
label = PROOF
official_prize_counterpacket = true
agreement = 262
```

That is a checker false-positive path. The synthetic document is not official evidence; it is a countermodel proving that the present schema is insufficient even after a contract file is supplied.

THEOREM / COUNTERPACKET / ROUTE CUT:

### 1. Packet-maximal official-independence theorem

Let `P118` denote the complete, byte-exact Cycle118 packet.

Then `P118` proves the attached-manuscript theorem

```text
C = RS[F_17^32,H,256], |H|=512,
LD_sw(C,262) >= N,
N = 52,747,567,092,
epsilon_mca(C,125/256) >= N/17^32 > 2^-128,
```

but proves neither

```text
OFFICIAL_ACCEPT(C)
```

nor

```text
OFFICIAL_REJECT(C).
```

Within the requested ordered clause list, the first undecided clause is:

```text
extension-field admissibility.
```

The exact failed arrow is:

```text
SOURCE_ACCEPTED_CYCLE116_ROW
    ⇏ OFFICIAL_SOURCE_ACCEPTED_CYCLE116_ROW.
```

### 2. Closed-ball close-point adapter

For every linear code `C⊆F^D`, every agreement threshold `a`, and every line `f+Fg`,

```text
support-wise noncontained at agreement a
    ⇒ dist_H(f+zg,C) <= n-a.
```

Moreover, if any support-wise noncontained slope exists, the affine line is not contained in `C`.

Consequently Cycle116 proves:

```text
∃ an affine line L not contained in C such that

#{z∈F_17^32 : dist_H(f+zg,C) <= 250}
    >= 52,747,567,092.
```

This is a finite closed-ball close-point line-decoding lower bound. It is not ordinary fixed-word list decoding.

### 3. Strict-ball/schema countermodel

`OFFICIAL_CONTRACT_SCHEMA.json` requires only:

```text
authority
source_document
row
line_parameter
q_chal
nine event rules
exhaustive_event_registry
```

It contains no field for:

```text
base bad-event predicate
delta or agreement threshold
strict versus closed distance
external line-decodable predicate
challenge distribution
challenge-to-slope map
ordinary-list-decoding versus line-decoding scope
```

A synthetic source document was constructed with the clauses:

```text
The exact Cycle116 extension-field row is accepted.
The line parameter field has size 17^32.
No separate q_chal is defined.
Closeness uses dist_H(u,C) < 250, hence agreement >=263.
All nine listed event-rule families RETAIN.
```

Its v1 JSON contract cited the row, field, and event clauses but had nowhere to record the strict-ball clause. With its exact contract hash supplied as the trust-pin argument, the packet checker accepted it and emitted `PROOF`.

Therefore:

```text
v1-contract-valid + ACCEPT + EVENT_RETAINED
    ⇏ official strict-ball Cycle116 counterpacket.
```

The exact missing predicate is:

```text
OFFICIAL_DISTANCE_CONVENTION_AND_AGREEMENT_THRESHOLD.
```

PROOF DETAILS:

### A. The packet contains no official contract

The outer archive matches the supplied SHA-256, and all entries in its internal `SHA256SUMS.txt` verify. An inventory of the verified archive finds:

```text
OFFICIAL_CONTRACT_SCHEMA.json
checker code
documentation
synthetic self-test constructors
```

but no actual authority-issued `cycle117.official_source_contract.v1` instance, authoritative source document, or independently authenticated contract pin.

The default checker therefore correctly returns:

```text
SOURCE_CONTRACT_MISSING_NO_CLAIM.
```

Integrity proves what bytes are present. It does not turn the locally authored schema into an official authority statement.

### B. Official status is genuinely underdetermined

The checker’s own contract state machine admits both of the following completions:

```text
O+:
  row.decision = ACCEPT
  all event actions = RETAIN

O-:
  row.decision = REJECT
  all event actions = RETAIN
```

Both can satisfy every structural requirement of the v1 schema and every exact line-slice/hash check. They produce opposite terminals:

```text
O+ -> SOURCE_ACCEPTED_CYCLE116_ROW
O- -> SOURCE_REJECTED_CYCLE116_ROW.
```

Neither completion contradicts the attached-manuscript theorem because manuscript acceptance and official adoption are different predicates.

The synthetic completions do not establish either official conclusion. They prove logical independence: the packet supplies no proposition selecting `O+` rather than `O-`. Hence no stronger official conclusion follows from the packet.

### C. Proof of the closed-ball adapter

Let `z` be support-wise noncontained at agreement `a`. By definition there are a support `S`, `|S|≥a`, and `c∈C` such that

```text
(f+zg)|S = c|S.
```

Therefore `f+zg` and `c` differ on at most `n-|S|≤n-a` coordinates, so

```text
dist_H(f+zg,C) <= n-a.
```

If the whole affine line were contained in `C`, then linearity would give `f∈C` and `g∈C`. Their restrictions would simultaneously explain `f` and `g` on every support, contradicting support-wise noncontainment. Thus the line is not contained.

For Cycle116,

```text
n-a = 512-262 = 250.
```

Distinct slopes give distinct line points because a support-wise bad line cannot have `g=0`. Hence all `N` certified slopes give `N` distinct closed-ball close points.

### D. Exact strict-ball gap

At the stated radius,

```text
delta n = (125/256)·512 = 250.
```

Thus:

```text
closed ball: dist_H <=250  ⇔ agreement >=262;
strict ball: dist_H <250   ⇔ agreement >=263.
```

No rounding ambiguity remains because `250` is an integer.

The Cycle116 certificate explicitly supplies supports of size `262`. It neither supplies a common size-`263` support construction nor proves that all—or even seven—of the certified slopes have an additional agreement coordinate.

Within the same direct fixed-jet framework:

```text
r = n-k = 256.
```

The existing row uses:

```text
j = 250,
sigma = r-j = 6,
agreement = n-j = 262.
```

Agreement `263` requires:

```text
j = 249,
sigma = 7,
```

or a genuinely different construction. Accidental additional roots are not a certificate.

### E. Challenge-distribution cut

Let `B⊆F_Q` be the certified bad-slope set, `|B|≥N`. If an official protocol samples a challenge `ω` from a distribution `μ` on a space `Ω`, with slope map

```text
pi: Ω -> F_Q,
```

then the official event probability is

```text
μ(pi^{-1}(B_off)).
```

The count `|B|/Q` transfers only after proving both:

```text
B ⊆ B_off
```

and a measure statement such as

```text
pi_*μ = uniform distribution on F_Q.
```

Knowing only the size of the line field or challenge field proves neither condition. Since `Q>N`, an arbitrary distribution can place zero mass on a specified `N`-element subset.

The v1 schema records only `q_chal.status`, `q_chal.field_size`, and a `challenge_filter` action. It records no distribution, slope map, or pushforward-mass guarantee. Thus even a defined `q_chal` plus `challenge_filter=RETAIN` is insufficient for a protocol probability lower bound.

### F. Conditional full-transfer theorem

An official finite support-wise/closed-line counterpacket follows immediately if an independently authenticated contract proves all of:

```text
1. The exact row RS[F_17^32,H,256] is officially admissible.
2. The official line parameter is uniform on F_17^32,
   or an official challenge distribution has uniform slope pushforward.
3. The official bad predicate contains the Cycle116 support-wise events
   at agreement 262, equivalently uses the closed ball dist_H<=250.
4. Endpoint, quotient, periodic, tangent, contained-line, affine-color,
   retained-event, challenge-filter, and charge processing leave at least
   seven free distinct events.
5. The claimed scope is finite MCA or close-point line decoding,
   not ordinary fixed-word list decoding.
```

Seven events suffice because:

```text
floor(17^32/2^128)=6.
```

Retaining all `N` is far stronger than necessary.

FIELD AND PARAMETER LEDGER:

```text
Q = 17^32
  = 2,367,911,594,760,467,245,844,106,297,320,951,247,361

q_gen  = Q
q_code = Q
q_line = Q

q_chal = null
```

The `q_chal=null` statement is scoped only to the attached finite MCA theorem. Official `q_chal` remains unknown.

```text
n = 512
k = 256
r = 256
delta = 125/256
delta·n = 250

closed-ball agreement = 262
strict-ball agreement = 263

N = 52,747,567,092
floor(Q/2^128) = 6
```

The attached-source numerator already pays:

```text
12 same-slope double fibers,
contained-support noncontainment,
finite-slope/nonzero-evaluation requirements.
```

SELF-AUDIT:

1. **Exact statement and scope.**
   I proved a packet-scoped non-entailment theorem for official promotion, a finite/source-scoped closed-ball close-point adapter, and a checker countermodel showing v1 schema incompleteness. I did not prove official adoption.

2. **Field variables.**
   `q_gen=q_code=q_line=17^32` were used only for the finite/source theorem and uniform line denominator. `q_chal` was not invented; it remains null source-scoped and unknown officially.

3. **Numerator reductions.**
   Under attached manuscript definitions, endpoint, periodic, quotient, tangent, affine-color, retained-event, and charge rules do not reduce `N`; contained-line and same-slope losses are already paid. Official reductions remain unclassified. Strict-ball conversion can reduce the currently certified numerator to an unknown value, and nonuniform challenge sampling can reduce probability without changing the raw numerator.

4. **Object proved.**
   The result concerns support-wise `LD_sw` and, by a no-loss implication, closed-ball close-point line decoding. It does not concern ordinary fixed-word list decoding.

5. **First missing official clause.**
   The authentication precondition is an independently trusted authority contract. Within the requested semantic ordering, the first missing clause is official extension-field admissibility for `RS[F_17^32,H,256]`.

6. **Next exact attack.**
   Replace the v1 contract with an authority-pinned v2 receipt that explicitly records predicate identity, distance convention/agreement threshold, challenge distribution and slope pushforward, final free numerator, and claim scope.

NEXT EXACT STEP:

Target:

```text
V-CYCLE118-AUTHORITY-PINNED-OFFICIAL-CONTRACT-v2-CLOSED-BALL-UNIFORM-PUSHFORWARD-REPLAY
```

The checker must require these additional fields:

```text
base_predicate_id
radius = 125/256
distance_convention = CLOSED | STRICT
required_agreement = 262 | 263
challenge_space
challenge_distribution
challenge_to_slope_map
slope_pushforward = UNIFORM_ON_F_17^32 | explicit mass certificate
final_free_surviving_numerator
claim_scope
```

Acceptance should require `final_free_surviving_numerator≥7`, not merely the absence of every loss label.

If the authenticated authority selects `STRICT`, the exact mathematical construction is:

```text
L-CYCLE118-SEVEN-SLOPE-249-COSUPPORT-FIXED-7-JET
```

Construct seven subsets `J_i⊂H` such that

```text
|J_i| = 249,
P_i(X)=∏_{x∈J_i}(X-x)
```

have one common seven-coefficient top jet in the Cycle116 fixed-jet sense, while the values `P_i(beta)` are nonzero and pairwise distinct. The fixed-jet argument would then give seven distinct support-wise noncontained slopes at agreement `512-249=263`, already enough to exceed `2^-128`.
