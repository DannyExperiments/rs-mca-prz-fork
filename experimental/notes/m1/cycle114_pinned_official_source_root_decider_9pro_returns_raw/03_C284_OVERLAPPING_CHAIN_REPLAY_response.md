PROOF

Terminal decision: SOURCE_REJECTED. Confidence: high.

First failed official source clause

The attached source root explicitly restricts M1 to smooth multiplicative evaluation domains:

context/source_docs/proximity_blueprint_v3.tex:102 defines a smooth domain as a multiplicative coset of a subgroup of power-of-two order.

Problem M1, proximity_blueprint_v3.tex:396–405, assumes generated-field smooth domains H
n

≤F
q
n

×

.

Paper B repeats this in context/source_docs/slackMCA_v3.tex:153–154: D or H is a multiplicative subgroup of order n, with “smooth” meaning n is a power of two.

C284 instead declares

D=
i=1
⋃
284

S
i

∪{h},∣D∣=285+284+1=570,

with h=6
7
, as recorded in
context/cycle113_returns/08_COUNTERPACKET_FALSIFIER_response.md:21–116.

The direct type check fails:

2
9
=512<570<1024=2
10
.

Hence 570 is not a power of two, so the C284 evaluation domain is not an official smooth source domain.

There is also a stronger no-embedding obstruction. C284 contains

1=x
1

∈D,h=6
7
∈D.

The packet certifies that 6 is primitive in F
p
×

, and

p−1=130⋅2
128
=2
129
⋅5⋅13,gcd(7,p−1)=1.

Therefore

ord(h)=ord(6
7
)=
gcd(7,p−1)
p−1

=p−1,

so h is primitive.

Suppose even that the C284 points merely lay inside some smooth multiplicative coset αH. Since 1,h∈αH, their ratio h/1=h would lie in H. A subgroup containing a primitive element is all of F
p
×

, forcing

H=F
p
×

,∣H∣=p−1=2
129
⋅5⋅13,

which is not power-of-two order. Thus C284 is not even contained in any official smooth multiplicative coset over F
p

.

Equivalently, directly from orders,

570=2⋅3⋅5⋅19,p−1=2
129
⋅5⋅13,

so 570∤p−1; no multiplicative subgroup or coset in F
p
×

 can have cardinality 570.

Why the residue-line normal form does not repair this

Paper B’s canonical source-to-residue-line theorem is thm:normalform,
context/source_docs/slackMCA_v3.tex:1189–1207.

Both directions of that theorem operate on the same tuple

(F,D,k).

Given a source line over D, it produces a residue-line datum over that same D; conversely, a residue-line datum over D produces a line for RS[F,D,k]. It does not replace an arbitrary domain by a smooth subgroup or coset.

Therefore the exact implication

C284 residue-line datum⟹official M1 datum over a generated-field smooth domain

is false at the domain-type clause.

C284 also sets k=1, hence ρ=1/570, rather than one of the prize rates listed in proximity_blueprint_v3.tex:102; this is a second source mismatch, but the smooth-domain failure occurs first.

Replay of the requested mechanisms
Mechanism	Exact result
Overlap/path incidences	The audited model calculation is correct: S
i

∩S
i+1

={(i+1)
2
}, and nonadjacent supports are disjoint. The intersection graph is P
284

. This does not repair the failed source-domain type.
Same-slope collapse	The 284 values z
i

=−u
i
2

(2u
i

+1) are pairwise distinct because their integer representatives are strictly increasing and remain below p. No same-slope compression occurs model-side.
Endpoint effect	Under the model one-endpoint allowance, at least 283 displayed colors remain. No official endpoint rule is defined in the source manuscripts, but it is downstream of the source rejection.
Contained/tangent effects	The model contained/delete-one branch is empty by the degree-one root bound, and the support polynomials are squarefree. Again, these tests are not reached officially.
Quotient/periodic structure	Paper B’s official quotient-periodic separation is formulated for residue lines over smooth H; C284 is outside that typed domain. The model t=1 residue algebra has no proper nonzero unital quotient, but this cannot promote the packet.
Affine stabilizer or affine-color normalization	The model packet has trivial affine stabilizer, and a fixed nonconstant affine color map is injective. The source files contain no official affine-color quotient map that could be evaluated.
Retained-tag normalization	No official retained-tag or final retained-color equivalence is defined in the source files. A tagged support-dependent affine map is injective model-side.
Interpolation-defect Fourier charge	C284 has the model lower bound Δ≥284p−(
3
570

)=284p−30,703,240. However, the source files contain no predicate named AP_corr and no theorem making this an official rejection or charge. It is unnecessary because the earlier domain clause already fails.

The literal strings AP_corr and APcorr occur zero times in context/source_docs/. Those files also contain no official final-retained-color map, retained-tag rule, or charge registry. These absences would prevent a downstream decision for a source-valid packet. They do not prevent this rejection because C284 fails before those downstream stages.

Exact q-ledger

Let T=2
128
. The packet uses

q
gen

=q
code

=q
line

=p=130T+1,q
chal

 unused.

Hence

⌊
2
128
q
line

⌋=130.

Conditionally on model acceptance and one endpoint deletion,

N
model

=283

would give

TN
model

−q
line

=283T−(130T+1)=153T−1>0.

Thus neither relabeling nor an additive charge allocation could pay the model packet without an exact rejection or at least 153 genuine final identifications/removals.

Officially, however, C284 contributes no retained event because the source datum is rejected:

N
free

(C284)=0,2
128
N
free

(C284)=0≤q
line

.

This is not a color compression and not a charge. There is no charged subset, cap, or allocation, and hence no double counting. The whole candidate fails the source gate.

q
line

 is the sole final denominator.

q
gen

 receives no denominator credit and would be used for entropy only after a relevant source theorem.

q
code

 is not a security denominator.

q
chal

 is unused.

Exact implications

Proved:

C284 as supplied⟹not an official smooth-domain M1 source datum⟹SOURCE_REJECTED.

More strongly, its marked points cannot all lie in any smooth multiplicative coset in F
p
×

.

Not proved:

Every overlapping-chain construction is source-invalid.

No source-valid chain with more than 130 slopes exists.

Any theorem involving official AP_corr.

Any official final-color compression or Fourier charge theorem.

The M1 upper bound or the Proximity Prize theorem.

Route to a source-valid counterpacket

The exact C284 packet cannot be converted unchanged into a counterpacket: its evaluation domain and its primitive padding point violate the first source hypothesis.

The first theorem needed for a replacement is:

SMOOTH-CHAIN-131 REALIZATION

Construct, for an official domain L=αH with ∣H∣=2
m
, official k,σ, and a residue-line datum (E,B,w) over L, at least 131 pairwise distinct slopes having noncontained witnesses at the required radius. The construction must use supports contained in L, meet the corrected reserve, and survive the source-defined quotient-periodic separation.

For q
line

=130⋅2
128
+1, 131 such Paper-B slopes would satisfy

131⋅2
128
>q
line

.

By thm:normalform, that would give a direct source-valid MCA counterpacket. A mere modification of the padding or a model embedding is insufficient; all support and witness identities must be rebuilt on the smooth source domain.

Self-audit

Exact implication proved: C284 fails the explicit smooth multiplicative source-domain clause. Not proved: any global M1 theorem or source-valid counterpacket.

Relevance: This is official-prize-relevant as a source-route rejection certificate for C284. It is not a prize theorem.

First failure line:

C284 datum⟶M1 datum over L=αH, ∣H∣=2
m
.

It fails because ∣D∣=570∈
/
2
N
, and indeed D cannot even be contained in a smooth coset.

Field discipline: q
line

 alone is the final denominator; q
gen

 is not credited absent an entropy theorem; q
code

 supplies no denominator; q
chal

 is unused; the target is 2
128
N
free

≤q
line

.

Possible numerator reductions: Same-slope, contained, tangent, endpoint, affine, retained-tag, quotient, and Fourier mechanisms were checked. None supplies an official model compression. The exact source exclusion instead removes the whole packet before numerator formation.

Full-solution status: The assigned C284 branch is fully decided by source rejection. A counterpacket requires the new SMOOTH-CHAIN-131 REALIZATION theorem; it cannot be obtained by relabeling the existing C284 packet.
