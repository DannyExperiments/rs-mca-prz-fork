AUDIT

Terminal decision

SOURCE_REJECTED

The literal P190 and C284 packets fail the first official M1 source-domain clause. This occurs before AP_corr, endpoint processing, color normalization, charging, or the q
line

 ledger.

Exact rejection

The official source root requires a smooth multiplicative evaluation domain:

context/source_docs/slackMCA_v3.tex, Theorem thm:integrated-package and the following paragraph “Setting and notation”: D or H≤F
q
×

 is a multiplicative subgroup of order n, with “smooth” meaning n=2
m
.

context/source_docs/proximity_blueprint_v3.tex, Problem prob:M1: the M1 problem is stated for generated-field smooth domains H
n

≤F
q
n

×

.

The broader coset formulation in context/source_docs/cs25_cap_v4.tex, §sec:prelim, requires D=αH, where H is a cyclic multiplicative subgroup.

context/source_docs/RS_disproof_v3.tex, Conjecture conj:capacity, similarly states the prize problem for smooth-domain Reed–Solomon codes.

For the stress field,

p−1=130⋅2
128
=5⋅13⋅2
129
.

For P190,

∣D∣=571.

This is not a power of two, and

gcd(571,p−1)=1,

so 571∤p−1. Hence D cannot be a multiplicative subgroup or a multiplicative coset in F
p
×

.

For C284,

∣D∣=570=2⋅3⋅5⋅19.

Again 570 is not a power of two, and

gcd(570,p−1)=10,

so 570∤p−1. Hence this D also cannot be a multiplicative subgroup or coset in F
p
×

.

Thus both literal packets fail the source-domain clause. Multiplicative rescaling or an affine relabelling cannot repair this failure because it preserves ∣D∣.

There is a second, downstream prize-formulation mismatch: both packets use k=1, giving rates 1/571 and 1/570, not the deployed rates in conj:capacity. The domain failure is earlier and already decisive.

Strongest source root actually present
Requested object	Exact source root	Status
Source adapter	slackMCA_v3.tex, Definition def:residue, Lemma lem:denom, Theorem thm:normalform, Proposition thm:closure	A fixed-(F,D,k) line/residue normal form exists. A model-packet-to-smooth-domain adapter is MISSING.
Official AP_corr	No occurrence or definition in any attached source document	MISSING. Definitions def:mca and def:ca are present, but no theorem identifies either with a predicate called AP_corr.
Endpoint convention	No source definition for deletion of one slope/color	MISSING. Source occurrences of “endpoint” concern radius endpoints, not a retained-event deletion.
Final retained K
line

 color/event map	No K
line

, retained-color quotient, or final event map appears	MISSING. Official MCA directly counts distinct bad slopes in RS_disproof_v3.tex, Definition def:mca, and cs25_cap_v4.tex, Definition def:mca.
Retained-tag normalization	No definition or theorem	MISSING.
Charge registry	No exhaustive registry with charged subsets, caps, ownership, overlap rules, and allocations	MISSING. slackMCA_v3.tex, Remark rem:aper, only defines quotient-periodic residue lines; its quantitative separation is part of Conjectures conj:B and conj:final-mca, not a proved charge registry.
Field transfer	slackMCA_v3.tex, Theorem thm:subfield, proves confinement only for base-field-valued lines	General q
gen

-to-q
line

 MCA transfer is MISSING. snarks_v4.tex, Assumption ass:extension-mca-lift, explicitly labels it an assumption.
Integer q
line

 ledger	snarks_v4.tex, Definition def:cert, equation eq:mca-budget; Design Rules rule:no-double-credit and rule:qchal; Theorem thm:ledger	Aggregate denominator ledger PRESENT. Per-color charge allocations are MISSING.

The exact normal form does not rescue the stress packets. Its converse constructs

f=w/E,g=−B/E

on the same domain D. It does not replace an arbitrary 570- or 571-point set with a smooth multiplicative domain, embed it into one, or preserve its displayed bad slopes under such an embedding.

Ledger audit

Let T=2
128
. Then

q
line

=130T+1,⌊
T
q
line

⌋=130.

Hence an official integer numerator would have to satisfy

TN
free

≤q
line

⟺N
free

≤130.

Under the provisional, nonofficial one-endpoint convention:

189T−q
line

=59T−1>0

for P190, and

283T−q
line

=153T−1>0

for C284.

Therefore those model counts would fail the ledger if they were official final retained events. They are not: source acceptance fails first, and no official endpoint or retained-event map exists. I do not assign N
free

=0; rather, the official final event set is never formed.

The field roles are:

q
gen

=q
line

=q
code

=p

numerically, but only q
line

 is the final MCA/security denominator.

q
gen

 is available only for an entropy loss after a theorem proving that loss.

q
code

 supplies no denominator and is not defined as such in the source manuscripts.

q
chal

 is unused here; no protocol-transfer theorem permits spending it.

Numerical equality of the fields does not create multiple copies of the denominator.

Degeneracy and normalization audit

The following possible reductions do not alter the source decision:

Quotient/periodic structure: rem:aper applies to smooth subgroup domains. Moreover, its proper quotient condition requires M∣gcd(n,k) with M>1; for the model packets k=1, this branch would be empty. It is not an official compression receipt.

Contained incidences and tangency: Cycle113’s model calculations check the displayed witnesses, but those checks do not establish smooth-domain source acceptance.

Same-slope collisions: The displayed P190 and C284 model colors were independently checked as distinct. This is downstream of the failed source gate.

Endpoint effects: the deletion of one color is provisional and has no source reference.

Affine color normalization: no official quotient map is present. An invertible affine map of the slope field would in any event preserve the number of distinct colors.

Final retained normalization and retained tags: both are absent.

Final source exclusions: the smooth multiplicative-domain exclusion is the first and decisive exclusion.

Exact implications

Proved:

P190 as written∈
/
{official smooth multiplicative-domain M1 instances},
C284 as written∈
/
{official smooth multiplicative-domain M1 instances}.

Equivalently, the literal route

stress datum⟶official smooth-domain RS source

fails at the domain clause.

Not proved:

that no different, newly constructed adapter could encode analogous incidences in a power-of-two multiplicative domain;

an official AP_corr rejection of either packet;

any final-color compression or charge ledger;

the M1 upper bound;

a source-valid low-t=1 counterpacket;

the finite-length local limit requested by prob:M1.

This is an official-prize-relevant source-route rejection, not a proof of the Proximity Prize theorem. It eliminates these two literal packets from the M1 source class but does not establish the desired upper bound for valid smooth domains.

Route to a full result

There is a complete route to deciding the literal P190/C284 replay, and it terminates in the source rejection above.

To convert this into a genuine counterpacket, the first required theorem or checker is a smooth-source adapter certificate with:

Inputs: the exact stress packet; a proposed (F
q

,α,H,k); an explicit map from packet coordinates and witnesses to αH; official line data f,g; bad slopes and agreement sets.

Required outputs:

H=⟨h⟩≤F
q
×

, ∣H∣=2
m
, and D
off

=αH;

the official rate/dimension conditions;

for every retained slope, exact MCA agreement and noncontainedness under Definition def:mca;

preservation of at least 131 distinct final slopes after the official endpoint and retained-event map;

exact charged subsets, caps, ownership, and a non-double-spent q
line

 allocation.

The checker would have no false positive because every field identity, subgroup order, agreement equation, interpolation condition, retained image, and integer allocation is exactly checkable. It would have no false negative relative to a supplied finite contract because all displayed witnesses and every registry entry could be exhaustively evaluated. It cannot be complete relative to unspecified predicates or an absent charge registry.

For a full upper-side PROOF, the first missing theorem is a finite-length proved version of slackMCA_v3.tex, Conjecture conj:final-mca, equivalently proximity_blueprint_v3.tex, Problem prob:M1, with explicit constants strong enough to give

#{official MCA-bad slopes}≤130

at the stated q
line

. The attached source explicitly marks that all-line practical-field theorem as open.

Confidence: high for the literal source rejection and the missing-object inventory.
