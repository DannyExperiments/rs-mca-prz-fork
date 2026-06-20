AUDIT

## 1. Executive verdict and confidence

**Verdict:** `RS-PRIZE-FRONTIER-V1-IMPLEMENTATION` is implementation-ready. The finite definitions are sufficiently precise; no new mathematical choice is required.

**Confidence:** high, `0.98`.

Two conventions must be explicit:

1. MCA maximizes over arbitrary anchors (u) and nonzero directions (v). Requiring (u\ne0) would break the exact zero-radius value.
2. `reserve_range` controls emitted rows only. Monotone propagation and frontier extraction always use the full lattice (0\le \sigma\le r).

The checker is sound relative to its immutable trusted registry. It does not certify the underlying non-core theorems itself.

[Download the complete implementation bundle](sandbox:/mnt/data/rs_prize_frontier_v1_spec_bundle.zip)

Bundle SHA-256:

```text
1dfd9a93f28bffcce13ff5f5893237dcd1d7686a14f90192f229ef9a62064012
```

## 2. Formal implementation claim

For a valid input instance and trusted registry, `rs_prize_frontier_v1.py` deterministically produces a canonical result satisfying the following contract.

Set

[
r=n-k,\qquad a_\sigma=k+\sigma,\qquad j_\sigma=r-\sigma.
]

Targets are

[
T_{\rm code}=\left\lfloor\frac{q_{\rm code}}{2^{128}}\right\rfloor,
\qquad
T_{\rm line}=\left\lfloor\frac{q_{\rm line}}{2^{128}}\right\rfloor.
]

Scalar and interleaved-list objectives use (T_{\rm code}). Native MCA uses (T_{\rm line}). An MCA comparison against (q_{\rm code}) requires a registered exact normalization bridge. The field (q_{\rm chal}) never pays a numerator, entropy, projection, line, or code bill.

For direct certified events, define

[
L(\sigma)=\max_{\tau\ge \sigma}L_{\rm dir}(\tau),
\qquad
U(\sigma)=\min_{\tau\le \sigma}U_{\rm dir}(\tau),
]

where (U) is absent if no complete whole-numerator upper program exists. The row verdict is exactly

[
\begin{aligned}
\texttt{FAIL}&\iff L(\sigma)>T,\
\texttt{SAFE}&\iff U(\sigma)\text{ exists and }U(\sigma)\le T,\
\texttt{UNKNOWN}&\iff\text{neither condition holds}.
\end{aligned}
]

For (T>0),

[
f=\max{\sigma:L(\sigma)>T},\qquad
c=f+1,\qquad
s=\min{\sigma:U(\sigma)\le T}.
]

The actual first safe reserve lies in ([c,s]), and is exact precisely when (c=s). For (T=0), every reserve fails, so

```text
f = r
c = null
s = null
no_safe_reserve = true
```

Conditional terms and conditional programs are evaluated in a separate ledger and cannot change certified `SAFE`, `FAIL`, (f), (c), or (s).

## 3. Full implementation construction

### 3.1 Command-line interface

```text
python rs_prize_frontier_v1.py check \
  --input INPUT.json \
  --registry trusted_theorems_v1.json \
  --artifact-root REPO_ROOT \
  --output RESULT.json

python rs_prize_frontier_v1.py validate-registry \
  --registry trusted_theorems_v1.json

python rs_prize_frontier_v1.py canonicalize \
  --input INPUT.json \
  --output INPUT.canonical.json
```

Exit codes:

| Code | Meaning                                                            |
| ---: | ------------------------------------------------------------------ |
|  `0` | Valid result, including rows classified `UNKNOWN`                  |
|  `2` | Malformed or semantically invalid input                            |
|  `3` | Invalid mathematical certificate or contradictory certified bounds |
|  `4` | Registry, source, producer, or artifact mismatch                   |
|  `5` | Output or budget-expansion resource limit                          |
| `70` | Internal implementation failure                                    |

### 3.2 Input JSON contract

All proof-relevant integers are canonical decimal strings:

```regex
0|[1-9][0-9]*
```

JSON numeric literals, leading zeros, signed zero, `NaN`, infinities, duplicate keys, duplicate IDs, and unknown object properties are rejected.

The top-level structure is:

```json
{
  "schema": "rs-prize-frontier-v1",
  "run_id": "...",
  "code_id": "...",
  "objective": {
    "kind": "mca | scalar_list | interleaved_list",
    "interleaving_arity": "...",
    "decision_denominator": "native | q_code_with_bridge",
    "normalization_bridge_ref": null
  },
  "profile": {
    "id": "proximity-prize-2026-v1",
    "mode": "official | research"
  },
  "n": "...",
  "k": "...",
  "q_gen": "...",
  "q_line": "...",
  "q_code": "...",
  "q_chal": "...",
  "domain_descriptor": {},
  "field_ledger": {},
  "reserve_range": {
    "min": "...",
    "max": "...",
    "mode": "dense | run_length"
  },
  "certified_lower_terms": [],
  "certified_upper_terms": [],
  "conditional_terms": [],
  "upper_programs": [],
  "conditional_upper_programs": [],
  "budget_programs": [],
  "options": {
    "emit_dense_rows": true,
    "emit_leave_one_out_relevance": true,
    "maximum_output_rows": "1000000",
    "maximum_budget_branches": "4096"
  }
}
```

A term contains exactly:

```text
id
status
objective
direction
term_type
scope
aggregation_role
reserve_data
field_debits
theorem_id
hypothesis_evidence
producer_certificate
dependencies
notes
```

`reserve_data` is either an exact table

```json
{
  "kind": "table",
  "entries": [
    {"sigma": "...", "bound": "..."}
  ]
}
```

or a closed registered evaluator:

```json
{
  "kind": "registered_evaluator",
  "evaluator_id": "...",
  "parameters": {}
}
```

Registry JSON cannot provide Python import paths or executable formulas.

Upper programs use only:

```json
{"op": "term", "term_id": "..."}
```

and justified `sum` or `max` nodes:

```json
{
  "op": "sum",
  "justification": {
    "kind": "union_bound",
    "certificate_ref": "..."
  },
  "args": []
}
```

```json
{
  "op": "max",
  "justification": {
    "kind": "exhaustive_outer_case_partition",
    "certificate_ref": "..."
  },
  "args": []
}
```

A `max` is valid only for an exhaustive partition of the outer maximization domain. It cannot replace addition of components occurring simultaneously in one numerator.

Budget programs additionally allow:

```json
{"op": "constant", "value": "..."}
{"op": "hole", "hole_id": "..."}
```

They are diagnostic templates and never certify safety directly.

### 3.3 Output JSON contract

The result contains:

```text
schema
input_sha256
checker_sha256
trusted_registry_sha256
code_fingerprint
validation
objective
targets
rows
frontier
term_relevance
conditional_conflicts
theorem_manifest
diagnostics
```

Each row records

```text
sigma, a, j, target
direct and propagated lower bounds
direct and propagated complete upper bounds
unresolved budget constraints
exact target differences
SAFE / FAIL / UNKNOWN
source and assumption IDs
field debits
exact rational radius interval
separate conditional-ledger result
```

The frontier record contains

```text
greatest_certified_failing_reserve
first_not_killed_reserve
least_certified_safe_reserve
sigma_star_interval
exact
sigma_star
previous_reserve_failure
candidate_status
candidate_unresolved_budget
largest_safe_grid_radius
supremal_safe_radius
supremal_endpoint_safe
radius_intervals
```

Every rational is emitted with raw and reduced numerator/denominator pairs. No decimal approximation influences a verdict.

### 3.4 Exact integer algorithms

The required implementation surface includes:

```python
parse_uint(s) -> int
parse_sint(s) -> int
ceil_div(a, b) -> int
emit_fraction(n, d) -> dict
comb_cmp(n, k, threshold) -> LT | EQ | GT
comb_value_if_leq(n, k, threshold) -> int | None
binom_sum_cmp(n, j, threshold) -> LT | EQ | GT
binom_sum_value_if_leq(n, j, threshold) -> int | None
verify_pocklington(cert) -> bool
verify_prime_trial(p, max_p) -> bool
verify_field_orders(instance, registry) -> None
verify_embedding_graph(instance, registry) -> None
```

For a binomial coefficient, use

[
\binom nk=\prod_{i=1}^{m}\frac{n-m+i}{i},
\qquad m=\min(k,n-k),
]

with exact division at every step. Under the official cap (T<2^{128}), if (m\ge128), then

[
\binom nk\ge\binom{2m}{m}\ge2^m>T,
]

so the comparison terminates immediately.

For a binomial sum, iterate with

[
\binom n{e+1}=\binom ne\frac{n-e}{e+1}
]

and stop once the nonnegative partial sum exceeds the comparison threshold.

Pocklington verification checks exact factorization, primality of each factored prime, the strict (F>\sqrt N) condition, modular exponentiation, and all required gcd conditions. Probable-prime output is insufficient.

Field validation checks

[
q_{\rm role}=p^{d_{\rm role}}
]

by exact exponentiation and constructs a directed embedding graph. Required paths are:

```text
q_gen -> q_code
q_code -> q_line   for MCA
```

The challenge field is not accepted as an intermediate substitute.

### 3.5 Injected core programs

Both objectives receive

[
N(\sigma)\ge1,\qquad N(r)=1.
]

MCA receives

[
M_C(\sigma)\ge\max{1,r-\sigma}.
]

At (\sigma=0), MCA upper alternatives are

[
q_{\rm line},
\qquad
\sum_{e=0}^{r}\binom ne.
]

At (\sigma\ge1), they are

[
q_{\rm line},
\qquad
\binom n{r-\sigma}.
]

Using exact-(j) padding at (\sigma=0) is an invalid certificate.

List objectives receive

[
L_{C,m}(\sigma)\le
\sum_{e=0}^{r-\sigma}\binom ne
]

and exact value one whenever

[
2(r-\sigma)<r+1.
]

Lower mechanisms combine by maximum, never by implicit summation. Complete alternative upper programs combine by a top-level minimum.

### 3.6 Budget normal form

Expansion branches are stored as ((c,m)), with constant (c) and a vector of nonnegative hole coefficients:

```text
Expand(constant c) = {(c,0)}
Expand(hole h_i)   = {(0,e_i)}
Expand(max(...))   = set union
Expand(sum(...))   = Cartesian Minkowski sum
```

Each branch becomes

[
m\cdot h\le b,\qquad b=T-c.
]

A constraint ((m,b)) may be removed only when another constraint ((m',b')) satisfies

[
m'_i\ge m_i\quad\text{for every }i,
\qquad
b'\le b.
]

For nonnegative holes, the second constraint then implies the first.

A branch is:

```text
IMPOSSIBLE  iff b < 0
CLOSED      iff m is empty and b >= 0
OPEN        otherwise
```

Exceeding `maximum_budget_branches` disables only that diagnostic expansion; it does not erase already certified row verdicts.

### 3.7 Radius staircase

For reserve (\sigma),

[
\delta_{\rm grid}=\frac{r-\sigma}{n}.
]

For (\sigma>0), the active radius interval is

[
\left[\frac{r-\sigma}{n},
\frac{r-\sigma+1}{n}\right).
]

At (\sigma=0), clipping to the prize domain produces the singleton (r/n).

From (f+1\le \sigma_*\le s), the checker emits

[
\frac{r-s}{n}
\le \delta_{\max}^{\rm grid}
\le \frac{r-f-1}{n},
]

and

[
\operatorname{clip}!\left(\frac{r-s+1}{n}\right)
\le \delta_{\sup}
\le
\operatorname{clip}!\left(\frac{r-f}{n}\right).
]

When (s=f+1>0), the supremal endpoint is unsafe. When (s=f+1=0), the capacity endpoint is safe.

### 3.8 Trusted registry format

The registry has exact arrays for:

```text
profiles
theorems
producers
field_certificates
embedding_certificates
domain_certificates
aggregation_certificates
normalization_bridges
```

A theorem entry fixes:

```text
theorem_id, version, status
statement_sha256, source_sha256
hypothesis_evaluator_id
allowed objectives, directions, scopes, aggregation roles
registered producers
```

A producer fixes:

```text
producer_id, version, status
adapter_id
producer-code SHA-256
accepted artifact SHA-256 values
accepted term types
```

All evaluators, adapters, and verifiers are selected from closed Python dispatch dictionaries. The registry cannot inject code.

Status handling is exact:

```text
PROVED_FINITE  -> may enter certified paths
PENDING_REVIEW -> conditional ledger only
REJECTED       -> refused
```

### 3.9 Refusal modes

The implementation has stable error codes. Principal categories are:

* malformed UTF-8/JSON, BOM, duplicate keys, numeric tokens;
* invalid decimal strings, duplicate IDs, unsorted set-like arrays;
* invalid (n,k,\sigma), official rate, (k)-cap, or strict field cap;
* wrong objective denominator;
* failed prime-power, primality, embedding, or domain-order check;
* challenge-field debit;
* missing or wrong-status registry entry;
* artifact path escape, missing artifact, or hash mismatch;
* unsupported term or arbitrary evaluator;
* false hypotheses, packet/fingerprint/reserve mismatch;
* component upper used as a whole numerator;
* unjustified `sum` or `max`;
* conditional or asymptotic data entering a certified path;
* exact-(j) MCA padding at zero;
* boundary-only list coverage;
* failed projection bridge;
* propagated certified lower/upper crossing;
* output-row or budget-branch resource limits.

The complete stable taxonomy is in `REFUSAL_CODES.md` in the bundle.

## 4. Parameter ledger and exact finite relevance

| Field       | Exact role                                                                          |
| ----------- | ----------------------------------------------------------------------------------- |
| `q_gen`     | Generated-domain, entropy, locator, GJ, and projection obligations where registered |
| `q_line`    | MCA slope/parameter field and native MCA denominator                                |
| `q_code`    | Code alphabet and scalar/interleaved-list denominator                               |
| `q_chal`    | External challenge accounting only                                                  |
| `sigma`     | Agreement reserve                                                                   |
| `a=k+sigma` | Agreement threshold                                                                 |
| `j=r-sigma` | Support/error-column budget                                                         |
| `f`         | Greatest certified failing reserve                                                  |
| `c=f+1`     | First reserve not already killed                                                    |
| `s`         | Least certified safe reserve                                                        |

Leave-one-out relevance is exact:

* A lower term moves the frontier iff deleting it lowers (f).
* It ties iff it attains the failing frontier and another term preserves that frontier.
* It is subfrontier-redundant iff it exceeds the target somewhere but not at the active failure frontier.
* An upper program moves the safe frontier iff deleting it raises (s) or removes all safe certificates.
* Deleting an upper leaf first invalidates every program depending on that leaf.

### Packet fixtures

| Packet                 |                                                                        Target | Default trust | Expected certified/promoted frontier                 |
| ---------------------- | ----------------------------------------------------------------------------: | ------------- | ---------------------------------------------------- |
| Role 04 scalar list    |                                                             (T_{\rm code}=21) | Certified     | (f=4,\ c=5,\ s=64)                                   |
| Role 07 projective MCA |                                                 (T_{\rm line}=16{,}776{,}960) | Conditional   | If promoted: (f=16{,}384,\ c=16{,}385,\ s=393{,}215) |
| Role 08 Lattès MCA     | (T_{\rm line}=80{,}951{,}559{,}894{,}234{,}747{,}884{,}481{,}262{,}824{,}352) | Conditional   | If promoted: (f=31,\ c=32,\ s=6{,}135)               |

Role 04 uses the exact lower event

[
7{,}045{,}058{,}086{,}196{,}679>21
]

at (\sigma=4).

Role 07 uses the conditional event

[
28{,}048{,}800>16{,}776{,}960
]

at (\sigma=16{,}384).

Role 08 uses the conditional event

[
183{,}062{,}151{,}498{,}210{,}163{,}887{,}302{,}260{,}440{,}015{,}706{,}432

>

80{,}951{,}559{,}894{,}234{,}747{,}884{,}481{,}262{,}824{,}352
]

at (\sigma=31).

If a separate certified reserve-32 lower event of

[
5{,}316{,}911{,}983{,}139{,}663{,}491{,}615{,}228{,}241{,}121{,}378{,}305
]

is supplied, then (f=32), and Role 08’s reserve-31 packet is classified `SUBFRONTIER_REDUNDANT`.

The included minimal suite covers target flooring, (T=0), zero radius, field separation, MCA padding at zero, monotone closure, `max` versus `sum`, strict JSON, certified-bound crossing, budget expansion, and the three packet fixtures.

## 5. Bankable versus conditional

### Bankable

* Strict input, result, and registry schemas.
* Canonical serialization and digest rules.
* Exact integer arithmetic algorithms.
* Objective-dependent target selection.
* Separation of `q_gen`, `q_line`, `q_code`, and `q_chal`.
* Full-lattice monotone closure.
* Core unit, zero-radius, tangent, support, and unique-decoding bounds.
* Typed upper-program aggregation.
* Exact budget normal form.
* Radius and endpoint staircase.
* Leave-one-out relevance.
* Role 04 packet adapter and fixture.

### Conditional

* Roles 07 and 08 until their theorem, producer, field, embedding, and domain registry entries are independently promoted.
* Roles 01, 02, and 05 as non-core theorem inputs.
* Any nontrivial apolar/GJ, quotient, block-trade, residual, occupancy, high-denominator, or collision-class upper.
* Any budget template with unfilled holes.
* Any component upper lacking a complete coverage program.

## 6. Failure point

The implementation wall closes.

The remaining failure is mathematical: at the candidate reserve

[
c=f+1,
]

the supplied lower mechanisms have stopped certifying failure, while no complete finite upper program may yet satisfy

[
U(c)\le T_{\rm decision}.
]

The checker reports that row as `UNKNOWN` together with the exact unresolved hole inequalities. It does not convert a promising component estimate, asymptotic expression, or incomplete budget into safety.

## 7. Next exact lemma or construction

There is a route to a full solve.

The immediate software construction is to implement `rs_prize_frontier_v1.py` from the supplied module skeleton and add the three packet adapters. The checker then provides a stable target interface for the mathematical wall.

The next mathematical producer should be:

```text
L-MODEL-GJ-MAXIMAL-BLOCK-TRADE-CHARGE
```

in the following exact form:

1. Assign every full-coordinate GJ-fiber configuration at the candidate reserve to a canonically specified maximal (K)-block-trade profile.
2. Prove that these profiles exhaust the whole numerator and either form disjoint classes or come with an exact authorized multiplicity.
3. Emit an explicit integer cap for each profile, with the block-collapse color (c^M) and all residual coordinates fully accounted for.
4. Handle configurations not covered by full blocks through the secondary finite lemma
   `W-LIST-MODEL-GJ-NEAR-SPLIT-COLLISION-CLASS-MASS`.
5. Compile the resulting component caps into a certified whole-numerator upper program with registered `sum`/`max` coverage.
6. Evaluate that program at (c). A value at most (T_{\rm decision}), together with the strict lower event at (c-1), closes the exact frontier mechanically.

A block-trade theorem that emits only component terms, without exhaustive coverage or authorized multiplicity, will not close the wall.
