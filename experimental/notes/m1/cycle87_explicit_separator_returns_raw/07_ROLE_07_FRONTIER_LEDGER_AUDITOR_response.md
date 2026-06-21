AUDIT

Confidence: high on the conditional ledger implication; moderate on the unmaterialized 464 construction.

Verdict

A certificate proving the selected one-GRS/one-line construction and

μ
proj
	​

(y)≤8

would certify

M
C
	​

(6)≥
8
PN
	​

=347,788,229,344,751,517,696>338,617,018,271,848,945,628.

That is an official-profile finite MCA FAIL row.

No row can currently be added: the archive contains neither the required projective census nor a replayed 464-point one-GRS/one-line materialization.

Parameter audit
Package	Rate	n−k	j+σ	Support accounting	Verdict
(464,232,6,226)	1/2	232	232	113+113=226	Profile-valid, construction pending
(560,280,6,274)	1/2	280	280	113+113+48=274	Profile-valid, construction pending

Both satisfy the shifted t=1 identity

j=n−k−σ,

and 1/2 is an official rate.

The qualifications are essential:

The 464 construction must be emitted as an actual [464,232] GRS code or parity-check restriction. Ordinary puncturing language alone does not establish k=232.

The 48 points in the 560 construction must be fixed coordinates contained in every witness support. If they merely pad the domain, then j

=274.

The reserve remains one global σ=6. It must not be inferred by adding or doubling local reserves.

Exact target
17
48
=115,225,400,457,255,426,923,013,053,222,916,919,834,651,165,519,677,685,328,641.

Therefore

T
line
	​

=⌊
2
128
17
48
	​

⌋=338,617,018,271,848,945,628.

Also 17
48
<2
256
, so the supplied field cap is satisfied.

Which numerator is correct?

Let Ω⊂F
0
×
	​

 be the N distinct one-copy colors and choose one first-block support for each element of Ω. This removes exactly the twelve known double ρ
β
	​

-fibers. The second block still ranges over all P supports.

Assume the actual common-line slope has the form

z
v,T
	​

=A+
c
0
	​

vP
T
	​

(y)
B
	​

,v∈Ω,T∈P
0
	​

,

with B,c
0
	​


=0, after all quotient and normalization operations.

Let Q
proj
	​

(y) be the number of projective classes represented by the P
T
	​

(y). Then

#{final slopes}≥NQ
proj
	​

(y).

Indeed, one representative of each projective class supplies N distinct products, and products from different classes cannot coincide because the ratio of two first factors lies in F
0
×
	​

.

Consequently:

Certified collision statement	Correct guaranteed numerator
Product map injective on Ω×P
0
	​

, or μ
proj
	​

=1	PN=2,782,305,834,758,012,141,568
μ
proj
	​

≤8 on all P second-copy supports	N⌈P/8⌉=PN/8=347,788,229,344,751,517,696
Independent injectivity on a representative packet Ω
2
	N
2
=2,782,305,834,125,041,336,464
Final slope multiplicity ≤8 only on Ω
2
	N
2
/8=347,788,229,265,630,167,058

Thus PN is the raw asymmetric pair count, not the numerator supplied by a multiplicity-eight theorem. The active projective checker gives PN/8. The N
2
 number belongs to the separate representative-pair injectivity construction.

The margin for the active checker is

8
PN
	​

−T
line
	​

=9,171,211,072,902,572,068.
Why eight succeeds and nine does not

Since P is divisible by 8,

μ
proj
	​

≤8⟹Q
proj
	​

≥
8
P
	​

=6,593,445,888,

which gives the certified bound above.

By contrast, μ
proj
	​

≤9 forces only

Q
proj
	​

≥⌈
9
P
	​

⌉=5,860,840,790,

and hence only

N⌈
9
P
	​

⌉=309,145,092,786,055,282,680<T
line
	​

.

So a uniform bound of nine is insufficient.

It would not kill the route. The exact occupancy condition is

Q
proj
	​

(y)≥⌊
N
T
line
	​

	​

⌋+1=6,419,576,048.

A census having some ninefold fibers could still pass this sharper test. A ninefold witness only kills the μ≤8 shortcut for that particular y.

Field ledger

For either package, the intended promoted declaration is

q_gen  = 17^48
q_code = 17^48
q_line = 17^48
q_chal = 17^48

These equalities require different checks:

q_gen: the actual ordered domain must generate L=F
17
48
	​

. For the translated construction, the base block must generate F
0
	​

, and the difference between corresponding translated and untranslated points must recover c=β−y, hence F
0
	​

(y)=L.

q_code: the emitted GRS code must be declared over L.

q_line: the affine syndrome line and its parameter must be over L.

q_chal: this must be explicitly declared in the official instance. It is not inferred from the other fields.

Only q_line enters

T
line
	​

=⌊q
line
	​

/2
128
⌋.

Neither q_code, q_chal, q_gen, 2
32
, nor the projective quotient size may replace it.

Numerator-loss audit

Quotient and periodic structure. The Cycle84 τ-quotient was computational compression. The exact lift produced the literal counts P and N. The separator census must account for all P supports, including orbit multiplicities. Projectivization modulo F
0
×
	​

 is only a collision-bucketing device; it does not change the MCA denominator or quotient the actual slope line.

Contained incidences. No support may be counted unless its span meets the affine line transversely. The certificate must verify noncontainment for every symbolic support family. If this check fails, the corresponding supports must be removed before counting.

Tangent term. The baseline tangent lower bound is only j=226 or 274, far below T
line
	​

. It must not be added to the packet count because overlap is uncontrolled. The packet lower bound stands independently.

Same-slope collisions. The twelve one-copy double fibers are already deducted by using N, not P, in the first coordinate. All remaining cross-pair collisions are charged by the projective census. The banked fact m
max
	​

(β)=2 does not control projective multiplicity at y.

Support collisions. Disjoint domain blocks must allow recovery of both component supports from their union. The fixed marker set in the 560 construction does not affect this.

Affine normalization. Reciprocal, multiplication by a fixed nonzero scalar, and one common affine map z↦A+Bz, B

=0, preserve cardinality. Separate block-dependent gauges or a pair-dependent normalization would invalidate the projective argument.

Exact preferred ledger row after PASS
YAML
id: C-CYCLE86-OFFICIAL-TWO-COPY-MCA-FAIL-ROW-464
status: PROVED_FINITE
classification: OFFICIAL_MCA_FAIL_COUNTERPACKET
profile: RS-PRIZE-FRONTIER-V1

objective: mca
direction: lower
term_type: packet.explicit_mca_slope_set
scope:
  kind: whole_numerator
  id: M_C
aggregation_role: standalone

certificate:
  theorem_id: L-CYCLE86-EXPLICIT-TWO-COPY-SEPARATOR-CERTIFICATE
  checker_id: V-CYCLE86-U-PROJECTIVE-MMAX8-CENSUS
  decision: PASS

code:
  family: GRS
  t: 1
  n: 464
  k: 232
  rate: 1/2
  sigma: 6
  j: 226
  one_code: VERIFIED
  one_affine_syndrome_line: VERIFIED
  full_coordinate: VERIFIED
  transversality: VERIFIED
  contained_incidences: 0

finite_source:
  packet_supports_P: 52747567104
  occupied_first_colors_N: 52747567092
  first_color_selector: VERIFIED
  projective_max_multiplicity: 8

slope:
  form: common_affine_reciprocal_product
  projective_quotient: L^x/F0^x
  common_normalization: VERIFIED

field_ledger:
  q_gen: 115225400457255426923013053222916919834651165519677685328641
  q_code: 115225400457255426923013053222916919834651165519677685328641
  q_line: 115225400457255426923013053222916919834651165519677685328641
  q_chal: 115225400457255426923013053222916919834651165519677685328641

lower_bound:
  raw_pairs: 2782305834758012141568
  collision_divisor: 8
  certified_M_C_lower: 347788229344751517696
  T_line: 338617018271848945628
  margin: 9171211072902572068
  decision: FAIL

claim_limits:
  scalar_list_numerator: NOT_CLAIMED
  whole_MCA_numerator_equality: NOT_CLAIMED
  full_proximity_prize_theorem: NOT_CLAIMED
  public_replay_receipt: SEPARATE_ARTIFACT

For the padded fallback, exactly one selected row replaces the code block by

YAML
n: 560
k: 280
rate: 1/2
sigma: 6
j: 274

All field and lower-bound numbers remain unchanged.

Why no row can currently be added

The current material does not establish the implication

(T
v
	​

,T)⟼Ψ
y
	​

(T
v
	​

,T)

as a family of full-coordinate transverse incidences on one affine syndrome line of one concrete GRS code with final slope

A+
c
0
	​

ρ(T
v
	​

)P
T
	​

(y)
B
	​

.

It also does not contain a replayed P-record census proving either

μ
proj
	​

(y)≤8

or the sharper occupancy condition

Q
proj
	​

(y)≥6,419,576,048.

Without those facts, PN is only a count of candidate support pairs. It is not a lower bound for the actual MCA bad-slope set.

Self-audit

Proved: conditional on the one-GRS/one-line slope formula, transversality, field ledger, and μ
proj
	​

(y)≤8, the official row satisfies M
C
	​

(6)≥PN/8>T
line
	​

.
Not proved: the existence or replay validity of that certificate for either package.

A passing certificate is official-prize-relevant as a finite MCA counterpacket. This audit alone is not such a counterpacket, not a public replay artifact, and not the full prize theorem.

The first unbanked implication is the assertion that the shortened or padded two-block supports all lie on one transverse affine syndrome line of one GRS code with the stated final reciprocal-product slope. For the 464 route, this includes the parity-check restriction/shortening step.

The target uses only q
line
	​

=17
48
. The other three field quantities require their own certificates or declaration and supply no denominator credit.

Quotient and periodic structure are harmless only after exact lift accounting; contained incidences must be excluded; tangent bounds are not additive; first-copy duplicates are removed by the N-selector; projective collisions are paid by μ
proj
	​

; one common affine normalization is bijective.

This is not a plan. The exact converter is a PASS for V-CYCLE86-U-PROJECTIVE-MMAX8-CENSUS bundled with the 464-point domain, [464,232] GRS fingerprint, common six-jet syndrome line, slope formula, and transversality verifier. If the 464 shortening check fails, the same census can be bundled with the 560-point materializer.