BANKABLE_LEMMA

## 1. Executive verdict and confidence

Bank the following as **finite-model theorems**:

* `L-CYCLE84-EXACT-COLOR-FILTERED-MMAX`
* `L-CYCLE84-EXACT-COLOR-FILTERED-SPECTRUM`

Record the execution evidence as:

* `V-CYCLE84-GITHUB-PUBLIC-REPLAY-27889140962`

Do **not** authorize an MCA, scalar-list, or official-prize ledger term from these entries. The registry permissions should remain empty until `L-CYCLE85-EXACT-ROLE05-OCCUPANCY-TRANSFER` is proved.

Confidence:

* Finite Cycle84 certificate: **high**.
* Public same-implementation replay: **high**.
* Offline reproducibility from the attached compact packet alone: **moderate**, because 19 manifest-listed artifacts are omitted.
* Independent-implementation confidence: **moderate**, because the public replay uses the original certificate bundle and implementations.
* Official-prize relevance: **unknown/unproved**.

The expression “full replay” must be interpreted exactly: GitHub reran the **full projected quotient census and kernel-3 lift**, not the independent 52.7-billion-pair direct census.

---

## 2. Exact theorem and replay statements

### `L-CYCLE84-EXACT-COLOR-FILTERED-MMAX`

Let (\rho_{84}) be the product map for the digest-locked explicit Cycle84 model over

[
\mathbf F_{17}[X]/(X^{16}+X^8+3),
\qquad \eta=6X^9,\qquad \beta=X+2,
]

with certificate-bundle SHA-256

```text
d119355626c3590f5d93191e1c8dddc61978ccad23cc8e2c431e530b3598789c
```

internal slot-log-table SHA-256

```text
d4379b3ed97c4ae2a43511796e3bcb15514d3f5f989f15b6fb1bc9fc85c779d8
```

and color constraint

```text
colorL + colorR == 4 mod 16.
```

Then

[
|\mathcal P_0|=52,747,567,104
]

and

[
m_{\max}(\beta)
=\max_v|\rho_{84}^{-1}(v)|
=2.
]

The canonical statement SHA-256 is

```text
c0187f434bbd207bddc07b04e1ec2af49e97a89341b4a7d1318e6cddc050e311
```

### `L-CYCLE84-EXACT-COLOR-FILTERED-SPECTRUM`

For the same finite map:

[
#{v:m(v)=1}=52,747,567,080,
]

[
#{v:m(v)=2}=12,
]

and there are no fibers of multiplicity at least (3). Consequently,

[
\operatorname{Occ}(\beta)=52,747,567,092
]

and

[
D=\sum_v m(v)(m(v)-1)=24.
]

The canonical statement SHA-256 is

```text
4b2e709cf6d8006ab6af998b7b0d2f4cd1c3e0712f887028b72468cb7ca50dc3
```

### `V-CYCLE84-GITHUB-PUBLIC-REPLAY-27889140962`

This is an execution-verification record, not a new mathematical transfer theorem.

```text
repository:  DannyExperiments/rs-mca-prz-fork
branch:      cycle58-5p5-audit
head commit: 3914f4d08b6ca5b919c84fe2598e4e74685caec4
workflow:    Cycle84 certificate replay
run id:      27889140962
status:      completed
conclusion:  success
completed:   2026-06-21T01:09:37Z
```

Jobs:

```text
Light certificate chain
job id: 82529457638
conclusion: success

Full projected census and kernel lift
job id: 82529457653
conclusion: success
```

The exact execution statements checked by the workflow were:

```text
CYCLE84_EXACT_MMAX2_CERTIFICATE_VERIFIED
TAU_FOLDED_PROJECTED_MMAX_LE_12
KERNEL_3_DUPLICATE_LIFT_COMPLETE
Projected census replay verified
Kernel lift replay verified
```

---

## 3. Audit proof and artifact chain

### Packet integrity

The attached context archive has SHA-256

```text
ab93bfcd0a6078af187dcf5660a565c917f571d50d1a22316150f19c3a4fc764
```

All 33 entries in `CONTEXT_SHA256SUMS.txt` passed. All 13 files in the Cycle85 prompt-packet manifest passed.

The selected Cycle84 raw directory contains 7 of the 26 files named by its `SHA256SUMS.txt`; all 7 present files match. The remaining 19 are omitted from the compact context packet. This is consistent with `CONTEXT_ZIP_MANIFEST.md`, which describes the packet as a selected snapshot, but it prevents offline re-execution from this attachment alone.

### Proof-relevant digest roots

```text
workflow
98da2539f37d477b8bc1f689c272c445d577f5b7bcc96562d3a295271425348f

raw SHA256SUMS.txt
4f8dbf527cc23a93957a1a98abe19479ee8fa4f3a47ac1ba4b22db3bf248092a

cycle84_mmax2_certificate_bundle.zip
d119355626c3590f5d93191e1c8dddc61978ccad23cc8e2c431e530b3598789c

CYCLE84_MMAX2_PROOF.md
8beafbaa373c4490d4090ef7fbb1cb3ed8fac5483be15cf4130455b553846018

cycle84_exact_mmax2_certificate.json
cfee92099c54e2f4d746f7f887d95610000d6c0985e25acf459bc9f9f2257c29

cycle84_master_proof_certificate.json
4abc98c8521856428c7c21b31ebfdb3380e32a9c1703202a50b3fcab85488088

LOCAL_VERIFIER_RESULT.json
2afa5a166e7df598ef94eb3b1ee767089ecb172f2a11040fed49cb10619022e7

fresh_full_certificate.json
1ba4fe9cbdcd51e2c8e7ac7c2d13795a258e5b267e2d2c83e2335a6953b1c6d1

cycle84_exact_mmax_checker.cpp
1ed541cb5b60629d6864082a006b672ad5b6c9f100dcd6e41d537ef0809b6189
```

Critical files inside the certificate bundle are pinned by the outer bundle hash and individually recorded as:

```text
verify_certificate.py
7cffe8e560e80a517ca56a8c71339382395c447c6b65424265121d514c61d9e7

src/tau_fold_full_optimized.cpp
f058d2e91be5630ec6a8c6d2f595ba6ba3b8689d59c8bf5c463f99974db99614

src/tau_duplicate_lift.cpp
fe3953e2051b13ea937e4855e99a0cc6942a665c0833fb709ad48a9c1e1088db

model/cycle68_slot_factorization_checker.py
7558ad5749bb2a4ecdd86a62030ba6290ff58de76ff9c2cad464344c728b9b31

data/slot_logs.json
d4379b3ed97c4ae2a43511796e3bcb15514d3f5f989f15b6fb1bc9fc85c779d8

data/cycle84_true_collision_pairs.json
d1196942d56bdd41e5b41295837d7d1c37ca18a3834ac95ccd42630e8051c604

src/logsM.hpp
d9a549578922fa3e62f62e527899b29e9064db635e367a2060e835a2a3f8c46f

src/logsN.hpp
037cb2a4c001980bfadaa3af9c0c6e0df533b2493007f52f2d26009de8bb428e
```

### What the two jobs checked

The light job, under `set -euo pipefail`:

1. Ran `sha256sum -c SHA256SUMS.txt` on all 26 repository artifacts.
2. Unpacked the exact bundle.
3. Ran `verify_certificate.py`.
4. Required the output to contain:

```text
CYCLE84_EXACT_MMAX2_CERTIFICATE_VERIFIED
"exact_true_m_max": 2
"exact_true_occupancy": 52747567092
```

The full job recompiled and reran the optimized quotient census. It asserted:

```text
tau_half_domain_counted                 = 26,373,783,552
fixed_selected_counts                   = [0, 0]
folded_ordered_energy                   = 60
projected_ordered_energy                = 120
max_canonical_projected_multiplicity    = 2
full_projected_max_including_fixed      = 2
number of duplicate canonical bins      = 30
multiplicity of every duplicate bin     = 2
```

It then recompiled and reran the kernel-3 lift and asserted:

```text
projection_duplicate_orbits_checked     = 30
selected_witnesses_recovered            = 60
true_collision_tau_orbits               = 6
true_double_fibers                       = 12
exact_true_ordered_offdiagonal_energy   = 24
exact_true_m_max                         = 2
exact_true_occupancy                     = 52,747,567,092
```

The resulting histogram is arithmetically rigid:

[
52,747,567,080+2\cdot12=52,747,567,104,
]

[
52,747,567,080+12=52,747,567,092,
]

[
12\cdot2=24.
]

Thus the certificate outputs are internally consistent.

---

## 4. Registry entry for `RS-PRIZE-FRONTIER-V1`

The conservative machine-registry policy is:

```text
status: PROVED_FINITE
allowed_objectives: []
allowed_directions: []
allowed_scopes: []
allowed_aggregation_roles: []
registered_producers: []
```

The empty permission arrays are deliberate. They prevent the finite occupancy theorem from entering an MCA or list numerator before the transfer theorem is registered.

The proposed evaluator ID is:

```text
cycle84.explicit-digest-locked-model.v1
```

Its exact contract should accept only the fixed field, (\eta), (\beta), color filter, bundle digest, slot-table digest and model cardinality above. It must not infer a code fingerprint, reserve, objective, field role, or frontier term.

The generated registry artifacts are:

* [Trusted-theorem registry fragment](sandbox:/mnt/data/cycle84_role07_registry/trusted_theorems_v1.fragment.json)
* [Public replay verification record](sandbox:/mnt/data/cycle84_role07_registry/V-CYCLE84-GITHUB-PUBLIC-REPLAY-27889140962.json)
* [Complete registry packet](sandbox:/mnt/data/cycle84_role07_registry.zip)

The registry-fragment SHA-256 is:

```text
b45ba011942167284903fc98cd892d6a2025b45a6d36274ab2091cd1309e08d5
```

The replay-record SHA-256 is:

```text
403e9864c853443d1baa68bf6cac7b0b31d910f6c07aa9b3fdfac270516955f1
```

---

## 5. Verification requirements and remaining reproducibility gaps

### Missing offline artifacts

The compact packet omits 19 top-level files, including:

```text
cycle84_mmax2_certificate_bundle.zip
cycle84_exact_mmax_checker.cpp
cycle84_mitm_certificate.cpp
cycle84_packet_verify.py
CYCLE84_MMAX2_PROOF.md
```

The successful GitHub light job implies that these files existed and matched the manifest at commit `3914f4d...`, but the current attachment alone cannot reproduce that check.

### No independent public implementation

The public replay recompiles the original bundle’s quotient census and kernel lift. It is valuable reproducibility evidence, but not an independently written implementation of the mathematical map.

The separate direct-census source and stored `fresh_full_certificate.json` are corroborating evidence, but the workflow did not publicly rerun that direct census.

### Compiler and runner dependence

The workflow uses:

```text
ubuntu-latest
actions/checkout@v4
unversioned g++
-O3 -march=native -fopenmp -D_GLIBCXX_PARALLEL
threads = nproc
```

The runner image, compiler version, standard library version, CPU instruction set and OpenMP implementation are not pinned by digest. A hermetic replay should use a container image and compiler identified by immutable hashes.

### Runtime outputs are not archived or hashed

The rerun creates:

```text
/tmp/cycle84_light_verification.json
/tmp/cycle84_tau_opt_rerun.json
/tmp/cycle84_tau_lift_rerun.json
```

but the workflow does not upload these as artifacts or record their SHA-256 values. The attached packet contains a Markdown receipt, not the raw GitHub run API response, logs, runner attestation or rerun JSON files.

### Census-to-lift binding is not explicit in the workflow

The workflow checks that the projected census emits 30 double bins, then separately runs the kernel lift. It does not explicitly:

1. canonicalize the actual 30 rerun bin keys;
2. hash them;
3. pass that exact file into the lift;
4. require the lift to echo the same digest.

The stored lightweight certificate may bind the original outputs, but the public rerun workflow does not expose this binding directly. This is the sharpest remaining replay-pipeline gap for the exact occupancy value. It is less serious for (m_{\max}\le2), since projected multiplicity (2) already bounds every exact fiber by (2).

### Generated certificate trust

The JSON certificates are not self-authenticating mathematical proofs. Their status comes from the verifier semantics, source-code review and replay. A malicious or jointly mistaken producer and verifier could consistently certify a misencoded model.

---

## 6. Next exact lemma and construction

The registry subtask is solved at the finite-model level. It does not give a full prize solve.

The next mathematical lemma is exactly:

```text
L-CYCLE85-EXACT-ROLE05-OCCUPANCY-TRANSFER
```

A sufficient precise statement is:

> Fix one official code fingerprint and reserve (\sigma). For every occupied value (v\in\rho_\beta(\mathcal P_0)), construct an admissible official MCA bad incidence (W_v) such that:
>
> 1. (W_v) survives all reserve, support, field and domain conditions;
> 2. (W_v) is transverse and noncontained;
> 3. its officially normalized slope is (a+bv) in (q_{\rm line}), for fixed (b\ne0);
> 4. no quotient, periodic, projective or affine normalization identifies (W_v) and (W_{v'}) for (v\ne v');
> 5. the construction is tied to the exact `code_fingerprint`, `q_gen`, `q_line`, `q_code`, `q_chal` and reserve.

Then, and only then,

[
N_{\rm MCA}(\sigma)\ge 52,747,567,092
]

is a valid registered lower certificate.

The next replay-hardening construction is:

```text
V-CYCLE85-CYCLE84-HERMETIC-REPLAY-BINDING
```

It should make the projected census emit a canonical `duplicate_bins.json` and `duplicate_bins_sha256`; make the lift consume that exact file and echo the digest; pin the compiler/container by digest; upload all canonical JSON outputs and runner metadata; and preferably rerun the independent direct-census implementation.

---

## 7. Self-audit

### 1. What exact implication did I prove, and what did I not prove?

Proved/banked:

```text
explicit digest-locked Cycle84 finite model
    =>
m_max(beta)=2,
Occ(beta)=52,747,567,092,
D=24,
with the stated fiber histogram.
```

Audited:

```text
GitHub run 27889140962
    =>
the light certificate and full projected-census/kernel-lift assertions passed.
```

Not proved:

```text
finite occupied products
    =>
official MCA numerator terms,
scalar-list numerator terms,
or an official prize counterpacket.
```

### 2. Is this official-prize-relevant?

It is a **finite/model/research certificate** and a prerequisite for a possible official lower certificate. It is not presently an official-prize term. The registry permissions are therefore empty.

### 3. What is the first line where the reduction chain could fail?

The first mathematical line is:

```text
the Cycle65-68 intended support/color construction
    =
the digest-locked 336-entry slot-log model enumerated by the bundle.
```

A shared model-encoding error would survive a same-code replay.

For this offline audit specifically, the first provenance gap is:

```text
the Markdown receipt
    =
the actual immutable GitHub run logs and outputs.
```

Those raw run records are not included in the attachment.

### 4. Are `q_gen`, `q_line`, `q_code`, `q_chal` and the (2^{-128}) target used correctly?

They are not used in the finite theorem. That is the only correct treatment at this stage.

The arithmetic fact

[
52,747,567,092>2^{32}
]

is not a comparison against

[
T_{\rm line}=\left\lfloor q_{\rm line}/2^{128}\right\rfloor
\quad\text{or}\quad
T_{\rm code}=\left\lfloor q_{\rm code}/2^{128}\right\rfloor.
]

No conclusion involving the (2^{-128}) target follows until the field ledger and objective denominator are fixed.

### 5. Could quotient structure, containment, same-slope collisions or affine normalization reduce the numerator?

Within the digest-locked finite product map, the tau quotient, fixed fibers and kernel-3 lift are already part of the certificate chain.

At the MCA transfer layer, the answer is **yes**:

* contained incidences may be inadmissible;
* nontransverse witnesses may be excluded;
* distinct product values might normalize to one official slope;
* projective or periodic quotients might identify values;
* affine color normalization might introduce identifications.

Multiplication by the fixed nonzero scalar from the locator factorization alone does not change occupancy. More general official normalization has not been audited.

### 6. What exact result would complete the route?

This answer is not a plan; it banks the finite certificate. The next theorem converting it into an MCA lower certificate is the five-condition transfer statement `L-CYCLE85-EXACT-ROLE05-OCCUPANCY-TRANSFER` above. The next construction strengthening reproducibility is `V-CYCLE85-CYCLE84-HERMETIC-REPLAY-BINDING`.
