# 07_CHECKER_AND_STRESS_CERTIFICATE_ENGINEER Final Visible Assistant Response

URL: https://chatgpt.com/c/6a38720e-16e0-83ec-a225-865922b380c6
Title: M1 Proximity Prize Solve
Status: FINAL_CAPTURED
Completion: FINAL_LABELED
Label: BANKABLE_LEMMA
Extracted: 2026-06-22T00:10:46.361Z

BANKABLE_LEMMA

Terminal decision: FINITE_STRESS_ONLY_NO_CLAIM.

I proved an endpoint-corrected, checker-ready Gate B certificate lemma and implemented an independent emitter/verifier. I did not verify Gate A or prove the source-uniform Gate B implication.

Exact bankable lemma

Let d=σ+1≤n, m=n−s, and

V(X)=
U
(X)
−1
modX
d+1
=
j=0
∑
d
	​

v
j
	​

X
j
,v
0
	​

=1.

Define

ε
j
	​

={
1,
0,
	​

d=n and j=n,
otherwise,
	​


and the endpoint-aware complement line

L
U
	​

(θ)
j
	​

=v
j
	​

−θv
j−1
	​

−ε
j
	​

,1≤j≤d.

Then activity is exactly

θ active⟺L
U
	​

(θ)∈M
m
	​

.

The endpoint correction follows from

g
T
	​

=(1−X
n
)g
S
−1
	​

=(1−X
n
)(1−θX)V(X)(modX
n+1
).

Since (1−θX)V has constant coefficient 1, multiplication by 1−X
n
 subtracts exactly 1 from the X
n
-coefficient.

Now let I
m,D
	​

 be the space of total-degree-≤D polynomials vanishing on every point of M
m
	​

. Choose any basis {F
α
	​

} and define

R
α,j
	​

(
U
)=[T
j
]F
α
	​

(L
U
	​

(T)),0≤j≤D.

The following are equivalent:

∃F∈I
m,D
	​

:F(L
U
	​

(T))

=0,
∃α,j:R
α,j
	​

(
U
)

=0,

and the rank-increase condition used by the Cycle106 eliminant checker,

rankA
m,D
	​

<rank[
A
m,D
	​

B
U
,D
	​

	​

].

Whenever these equivalent conditions hold,

#{θ:L
U
	​

(θ)∈M
m
	​

}≤D.

Indeed, every active θ is a root of the nonzero polynomial
F(L
U
	​

(T)), whose degree is at most D.

A literal single eliminant can be written with auxiliary indeterminates:

R
m,D
	​

(
U
;Z)=
α,j
∑
	​

Z
α,j
	​

R
α,j
	​

(
U
).

Then

R
m,D
	​

(
U
;Z)

=0⟺L
U
	​

 escapes the degree-D closure of M
m
	​

.

Its degree in the inverse coefficients v
j
	​

 is at most D, and its degree in the coefficients of
U
 is at most dD.

Exact next Gate B lemma

The full proof now reduces to the following precise statement:

L-CYCLE107-APCORR-ELIMINANT-COORDINATE

There is an absolute constant C such that, for every official source-valid instance,

AP
corr
	​

(
U
)⟹∃α,j:R
α,j
	​

(
U
)

=0

with

D=n
C
,

uniformly in s and k, using the corrected endpoint line when d=n.

This immediately gives

#{θ:L
U
	​

(θ)∈M
m
	​

}≤n
C
.

The finite checker now verifies the conclusion of this lemma for any supplied instance and separator. What remains mathematical—not computational—is proving that the formal source predicate AP
corr
	​

 forces one coordinate to be nonzero.

Exact Gate A certificate still required

A sound SOURCE_COVER_VERIFIED checker needs an input certificate containing:

The official M1 bad-slope object and corrected-reserve inequality.

A formal, executable definition of AP
corr
	​

(
U
).

The normalization producing one shared
U
.

A map z↦θ(z) from every uncharged official bad slope to a complement-line incidence

L
U
	​

(θ(z))∈M
m
	​

.

Proof that this map is injective on the slopes counted in the official numerator.

Exact records for every removed periodic, quotient, contained-incidence, endpoint, or other charged branch.

Proof that any affine normalization has nonzero linear coefficient.

The supplied packet names these objects but does not formally define AP
corr
	​

, the corrected-reserve test, or the official bad-slope normalization map. Therefore Gate A cannot presently emit SOURCE_COVER_VERIFIED.

Executable checker

The checker uses only standard-library Python. It independently recomputes the subgroup, M
m
	​

, truncated inverse, endpoint correction, separator vanishing, line restriction, active-θ set, and root bound.

Bash
python3 cycle107_gate_b_separator_certificate.py emit \
  --p 17 --n 8 --sigma 1 --s 4 \
  --uhat 1,0,0 --D 10 \
  --certificate cycle107_p17_n8_s4_gate_b_separator.json

python3 cycle107_gate_b_separator_certificate.py verify \
  --certificate cycle107_p17_n8_s4_gate_b_separator.json

The verified output includes:

terminal_decision                 FINITE_STRESS_ONLY_NO_CLAIM
gate_b_instance_decision          COMPLEMENT_LINE_ESCAPE_CERTIFIED
certificate_verified              true
endpoint_mode                     ordinary_nonendpoint
M_m_subset_count                  70
M_m_distinct_point_count          69
distinct_active_theta_count       9
restriction_degree                10
separator_vanishes_on_all_M_m     true
restriction_nonzero               true
all_active_theta_are_roots        true
distinct_root_bound_verified      true
source_cover_verified              false
AP_corr_evaluated                 false

At D=9, this instance emits:

gate_b_instance_decision: NO_DEGREE_D_SEPARATOR_FOUND

The corrected endpoint is also executable:

Bash
python3 cycle107_gate_b_separator_certificate.py emit \
  --p 5 --n 4 --sigma 3 --s 4 \
  --uhat 1,3,0,0,4 --D 1 \
  --certificate cycle107_endpoint_p5_n4_separator.json

python3 cycle107_gate_b_separator_certificate.py verify \
  --certificate cycle107_endpoint_p5_n4_separator.json

This emits endpoint_mode: corrected_endpoint and verifies the sole active value θ=2. Without the −1
j=n
	​

 correction, the final coordinate would be wrong.

Checker bundle
Standalone checker
Checker theorem and invocation guide
Non-endpoint certificate
Independent verification output
Endpoint certificate

Self-audit

1. Exact implication proved and not proved

Proved:

∃α,j:R
α,j
	​

(
U
)

=0⟹#{θ:L
U
	​

(θ)∈M
m
	​

}≤D,

including the d=n endpoint correction, together with an independently verifiable finite certificate format.

Not proved:

AP
corr
	​

(
U
)⟹∃α,j:R
α,j
	​

(
U
)

=0,

or the Gate A implication from official M1 bad slopes to distinct active θ-values.

2. Official-prize relevance

The algebraic lemma and certificate interface are official-route-relevant. The generated certificates are finite/model research certificates only. They are not Proximity Prize certificates and are not source-valid counterpackets.

3. First possible failure in the reduction chain

The first failure line is Gate A:

official uncharged bad slope⟼distinct θ with L
U
	​

(θ)∈M
m
	​

 and AP
corr
	​

(
U
).

That implication is not presently defined or verified. Conditional on Gate A, the next failure is exactly L-CYCLE107-APCORR-ELIMINANT-COORDINATE.

4. Field ledger and 2
−128

No q
gen
	​

, q
line
	​

, q
code
	​

, q
chal
	​

, or 2
−128
 arithmetic is used in the proved structural lemma. This is correct.

In an eventual official transfer:

q
gen
	​

 governs generated-field and reserve/entropy hypotheses.

q
line
	​

 is the MCA slope field and controls the official MCA denominator.

q
code
	​

 is the code alphabet and list-object denominator.

q
chal
	​

 is protocol challenge accounting only.

The 2
−128
 comparison for MCA uses the native q
line
	​

 target, not q
chal
	​

 and not an entropy payment from another field.

5. Numerator reductions

The checker counts distinct θ-values, never witness multiplicity. Same-θ support collisions therefore do not inflate its count.

It does not claim to have charged quotient or periodic structure, removed officially contained incidences, or verified an affine normalization. Those mechanisms can reduce the official numerator and must be handled exactly by Gate A. The endpoint correction is handled explicitly.

6. Exact conversion to proof or counterpacket

This is not a PLAN, but converting it into PROOF requires both:

L-M1-OFFICIAL-BAD-SLOPE-TO-APERIODIC-GAMMA-COVER

with the explicit injection and branch charges above, and

L-CYCLE107-APCORR-ELIMINANT-COORDINATE

with D=n
C
.

A COUNTERPACKET would require a source-valid family satisfying the formal corrected reserve and AP
corr
	​

, together with superpolynomially many distinct active θ-values. For a proposed exponent C, an exact finite Gate B counter-row is equivalently an AP
corr
	​

 instance with more than n
C
 distinct active values, forcing every degree-≤n
C
 separator restriction to vanish. The p=97 Cycle106 stress seed does not meet this source-valid requirement.

Confidence: high for the endpoint algebra, eliminant equivalence, root bound, and executable verifier; unknown for the missing AP
corr
	​

-to-eliminant theorem and official source-cover transfer.
