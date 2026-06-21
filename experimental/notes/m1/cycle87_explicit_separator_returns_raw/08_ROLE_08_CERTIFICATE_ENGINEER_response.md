BANKABLE_LEMMA

Verdict

The full multiplicity census is still unrun, so this is not yet a proof of μ
proj
	​

(U)≤8. Two substantial walls are now discharged:

The census can be exactly tau-folded from 52,747,567,104 packets to 26,373,783,552 canonical packets.

The preferred (464,232,6,226) package is valid for the audited explicit model; the 560 fallback is unnecessary.

The remaining wall is exactly

V-CYCLE87-U-TAU-FOLDED-SMOOTH-MMAX8-CENSUS
	​

.

Confidence is high for the reductions, field setup, and 464 geometry. The actual census outcome is unknown.

Exact new reductions

Let

q
0
	​

=17
16
,S=48,661,191,882,642,625,923,r=48,661,191,868,691,111,041,

where

∣L
×
/F
0
×
	​

∣=(q
0
2
	​

+q
0
	​

+1)=Sr.

Here

S=3⋅7⋅13⋅73⋅307⋅1321⋅72337⋅83233

and r is prime by the complete factorization

r−1=2
7
3
2
517
8
2941761

with Pocklington witness 7.

For nonzero b∈L, define

z(b)=b
q
0
	​

−1
,s(b)=z(b)
r
.

Since z has kernel exactly F
0
×
	​

, it is an exact projective key. Since s is a quotient of that key,

μ
proj
	​

(U)≤μ
s
	​

(U)
	​

.

Thus a smooth census proving μ
s
	​

(U)≤8 proves the active projective wall. A smooth collision of size nine does not prove projective failure; it only triggers exact refinement.

Exact tau folding

For the audited option involution

τ(1,a)=(2,a+6),τ(2,a)=(1,a+10),τ(3,a)=(3,a+8),

each slot satisfies

G
t,k
	​

(U)G
t,τ(k)
	​

(U)=C
t
	​

(U).

The color relation is

col(k)+col(τ(k))≡8(mod16),

so tau preserves the seven-slot color-4 shell. These option sets and color conventions agree with the pinned Cycle84 model surfaces. 

cycle84_tau_fixed_fiber_checker

The generated smooth logs give

κ=13,943,676,897,899,455,034,δ=κ/2=6,971,838,448,949,727,517(modS).

Writing

x(T)=e(T)−δ,q(T)=min(x(T),S−x(T)),

and selecting the first-slot options

{0,…,15,32,…,39},

chooses exactly one tuple from every tau orbit. If n(q) denotes the resulting canonical count, then

q>0:m
s
	​

(δ+q)=m
s
	​

(δ−q)=n(q),

while

q=0:m
s
	​

(δ)=2n(0).

Therefore

μ
s
	​

(U)≤8⟺n(q)≤8 ∀q>0,n(0)≤4.
	​


This is an exact equivalence. It is the extension-field analogue of the exact tau-folded counting principle already used in the Cycle84 checker.

Materialized finite-field setup

The bundle contains an executable C++20 producer that:

constructs all 336 factors G
t,i,a
	​

(U);

proves the selected smooth generator has order S;

computes every smooth logarithm by exact Pohlig–Hellman and CRT;

re-exponentiates every logarithm;

checks all exact tau-product identities;

checks the full and folded color-shell counts.

The independent Python verifier reconstructs every factor separately and verifies all 336 exponent identities.

Key hashes are:

C++ slot producer:
2998c0015025c8777cbf27eeb7cad0160c28659ab258014b87243ca552d514e7

336-row slot table:
bc9e8ef7dfe4fc8cca89e82b3ec150a12ec0cfbe1be3e641b62b05e623ba9987

Canonical record content:
54c9af836c48a7a8bfa40b8121a82b8c25c180feb8387f371aba2772b7913670
The 464 package is valid

For

D
−
=⟨η⟩∖{η
8b
:1≤b≤24},∣D
−
∣=232,

and

c=β−U,D
2
	​

=D
−
∪(c+D
−
),

the verifier establishes:

all one-copy supports survive the shortening;

the 464 domain elements are distinct;

β∈
/
D
2
	​

;

the domain generates L;

every option block has jet 1modt
6
;

every one-copy support has J
T
	​

(t)=1−tmodt
6
;

every combined support has the fixed jet

(1−t)(1−ct)
112
(1−(c+1)t)(modt
6
);

the columns

H
x
	​

=(1,x,…,x
230
,(β−x)
−1
)
T

form one [464,232] GRS parity-check matrix;

all supports lie on one affine syndrome line;

every incidence is transverse.

It additionally verifies one complete 226-point barycentric syndrome identity, including the reciprocal row.

The resulting hashes are:

domain:
6aa1eb735afbaaf36eefb3ac080123fb49c9e32d0dd861cd635c54ad42991f76

464×232 code matrix:
5ee34d5a29e09180fa82d09ea07abec9006cdead736ce1c9506b76a887f7bcce

affine syndrome line:
6b49252971502a27e49a673b20f3ed2457557432232eb8116f56da602e272e2a

Thus the shortening argument does not fail, and the 560 fallback is not needed for this explicit model.

Certificate-engineering specification
1. Source files and languages

The bundle specifies:

C++20:
  cycle87_build_u_slot_logs.cpp
  cycle87_tau_folded_scan.cpp       [implementation-complete pseudocode supplied]
  cycle87_exact_refine.cpp          [logic included in the same pseudocode]

Python 3, standard library:
  field_reference.py
  verify_u_slot_logs.py
  verify_geometry_464.py
  verify_result_envelope.py

Independent expensive verifier:
  Rust verify_shard.rs              [exact contract specified]

The C++ producer uses no floating point and no randomized equality test. Rust is reserved for independent shard regeneration, so the expensive verifier does not share the producer implementation.

2. Field representation

An F
0
	​

 element is 16 coefficients in increasing powers of X, each stored as one byte. Reduction uses

X
16
=−X
8
−3.

An L element is

b
0
	​

+b
1
	​

U+b
2
	​

U
2

encoded as 48 bytes in U-block-major, X-coefficient-minor order.

The exact projective key is

encode
48
	​

(P
T
	​

(U)
q
0
	​

−1
).

Smooth exponents require 66-bit arithmetic. Folded q-keys require 65 bits.

3. Inputs and hashes

inputs/INPUTS.lock.json pins:

the Cycle87 state and Cycle84–86 audits;

the authoritative Cycle68 slot-factor model;

the Cycle84 exact m
max
	​

=2 certificate;

the twelve double-ρ fibers;

the independent original slot verifier;

the public full-run and acceptance certificates;

the newly generated U-slot table and 464 geometry.

The raw Cycle86 worker slot-table hash is explicitly untrusted because its claimed byte artifact was absent.

4. JSON schemas

The normative schemas are:

schemas/cycle87_result.schema.json
schemas/cycle87_shard.schema.json
schemas/cycle87_geometry_464.schema.json

The result schema distinguishes:

PASS
FAIL_PROJECTIVE_MMAX_GE_9
REFINE_REQUIRED
ERROR

It separately records finite-model status, one-copy transfer, official two-copy counterpacket status, public replay status, and full-prize-theorem status.

5. Independent verifier

A theorem-grade verifier must independently:

hash every dependency;

reconstruct F
0
	​

, L, and all 336 factors;

verify every smooth logarithm by exponentiation;

verify tau constants and both shell counts;

rebuild the folded MITM side tables;

regenerate every shard;

refine every threshold-crossing key;

verify any nine-tuple FAIL witness;

verify the pinned 464 geometry hashes;

recompute NP/8, T
line
	​

, and the margin.

An aggregate result JSON is not evidence for collision absence.

6. Memory-bounded sharding

The folded key space has size

H=
2
S+1
	​

=24,330,595,941,321,312,962.

With 1536 shards, the largest interval width is

15,840,231,732,631,064<2
54
.

The MITM sides contain

folded left records = 55,296
right records       = 5,308,416

and the average shard contains exactly

17,170,432 compatible pairs.

Each shard first counts its records using binary-search interval lengths, then allocates an exact open-address table. A 64-bit table word stores a shard-local offset and a counter saturated at nine. Equality always compares the full offset; the hash only chooses the probe location.

Absolute folded keys can exceed 2
64
−1. Consequently, saturated-key files store 64-bit local offsets plus the decimal shard lower endpoint—not absolute uint64_t keys.

7. FAIL certificate

For q>0, canonical tuples are normalized into the δ+q smooth fiber:

x=q: T↦T,x=S−q: T↦τ(T).

For q=0, both T and τ(T) are included.

A valid FAIL contains:

decision = FAIL_PROJECTIVE_MMAX_GE_9
folded_q
common_projective_key_48_hex
exactly nine distinct packed tuple IDs

The verifier reconstructs all nine complete locators, including the common U−1 factor, verifies admissibility, and checks exact 48-byte key equality.

8. PASS certificate

A smooth-domination PASS requires:

all 1,536 shards complete
sum record_count = 26,373,783,552
max n(q) <= 8 for q > 0
n(0) <= 4

Alternatively, coarse thresholds may be exceeded if every such key is exactly refined and the exact projective maximum is at most eight.

The result must also carry the three pinned 464 geometry hashes and verify

8
PN
	​

=347,788,229,344,751,517,696>338,617,018,271,848,945,628=⌊
2
128
17
48
	​

⌋.
9. Reviewer reproduction

The local bundle replay is:

Bash
unzip cycle87_certificate_engineer_bundle.zip
cd cycle87_certificate_engineer_bundle
./scripts/reproduce.sh

The verified markers are:

FIELD_REFERENCE_SELFTEST_PASS
U_SLOT_LOGS_VERIFY_PASS
GEOMETRY_464_VERIFY_PASS
STATIC_RESULT_ENVELOPE_PASS
BUNDLE_SELFTEST_PASS

The full theorem replay then fetches and hash-checks the pinned Cycle84 artifacts, runs all folded shards, merges them, performs exact refinement when necessary, and independently regenerates all shards in Rust. Exact commands are in SPEC.md.

Self-audit

Proved: smooth-projective domination, exact tau folding, the complete 336-row setup, and the preferred 464 one-GRS/one-line construction.
Not proved: the numerical inequalities n(q)≤8 and n(0)≤4, because the 26.37-billion-record census has not been executed.

This is an official-prize-relevant finite/model certificate and replay design. It is not yet an official two-copy counterpacket, public replay artifact, or full prize theorem.

The first unproved mathematical line is:

n(q)≤8(q>0),n(0)≤4.

The first public-replay operational failure could instead be a mismatch between the pinned authoritative model bytes and the audited explicit constants.

q
0
	​

=17
16
 is used only internally. For this explicit construction,

q
gen
	​

=q
code
	​

=q
line
	​

=q
chal
	​

=17
48
.

The denominator is q
line
	​

, and the target is exactly
⌊q
line
	​

/2
128
⌋.

Smooth quotienting can only enlarge fibers, so its PASS implication is safe. Tau folding is exact. The first-copy selector removes all twelve duplicate ρ-representatives, same-slope collisions are charged to μ
proj
	​

, universal shortening loses no supports, and transversality excludes contained incidences. Affine reciprocal normalization is bijective and does not reduce the numerator.

This is not a PLAN. The exact checker converting it to PROOF is
V-CYCLE87-U-TAU-FOLDED-SMOOTH-MMAX8-CENSUS, followed when necessary by exact saturated-key refinement. Nine verified exact witnesses convert it to COUNTERPACKET against y=U.

Download the Cycle87 certificate-engineer bundle

bundle SHA-256:
cb2794edcd2c4add5bd43620fa761b5c2d4b6411c932645e5cbfd2d7bede820a