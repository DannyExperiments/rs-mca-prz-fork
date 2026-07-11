# Affine-syndrome field confinement for bad slopes

## Status

PROVED as a gauge-invariant refinement of the received-line field bound in
c7_collapse_image_degree.md. This note also records the quantifier repair
needed in fi_field_discharge.md.

## Setup

Let C=RS_F(D,k), with D contained in a base field B contained in F, and
let H be the weighted-Vandermonde parity-check matrix over B. For a received
word u write s(u)=H u^T. For a line r=(r_0,r_1), put

~~~text
y_0=s(r_0), y_1=s(r_1).
~~~

If y_1=0, set F_aff(r)=B. Otherwise let

~~~text
L_r=F y_1,
W_r=F y_0+F y_1,
~~~

and define F_aff(r) to be the smallest intermediate field E, B subset E
subset F, over which the flag L_r subset W_r is defined.

## Exact covariance

Adding codewords to r_0 and r_1 preserves every witness support, slope, and
multiplicity after adding the corresponding low-degree polynomials to the
explanations.

For u,w nonzero and v arbitrary, the triangular change

~~~text
(r_0,r_1) -> (u r_0+v r_1, w r_1)
~~~

sends bad slopes by

~~~text
gamma -> (v+w gamma)/u.
~~~

Thus bad-slope incidence is invariant under codeword gauge and affine slope
reparametrization. The raw coordinate field of a representative pair is not
invariant under these operations.

## Affine-syndrome confinement theorem

For every agreement level a there exist alpha != 0 and beta in F such that

~~~text
Z_a(r) subset alpha F_aff(r)+beta.
~~~

Consequently,

~~~text
|Z_a(r)| <= |F_aff(r)|
delta_lambda(r) <= |F_aff(r)|
~~~

for every first-match cell lambda.

If y_1=0, there are no nontrivial finite bad slopes: r_1 is a codeword, so an
explanation of r_0+gamma r_1 on a support also explains r_0 there, making the
support common.

## Proof

Assume y_1 != 0 and put E=F_aff(r). Since the flag is E-defined, choose
z_1 in E^(n-k) spanning L_r and, in the rank-two case, z_0 in E^(n-k) so
that z_0,z_1 span W_r. Then

~~~text
y_1=w z_1,
y_0=u z_0+v z_1
~~~

for w != 0 and, in the rank-two case, u != 0.

The full-row-rank parity-check matrix has a B-linear right inverse J, obtained
from any invertible set of n-k parity columns. Extending J over E gives
q_i=J(z_i) in E^D with syndrome z_i.

If W_r=L_r has rank one, r is codeword-equivalent to
(v q_1,w q_1). For gamma != -v/w, an explanation of the nonzero multiple
(v+w gamma)q_1 also explains q_1 and hence both coordinates. Thus at most the
single cancellation slope -v/w can be bad, which already gives the claimed
affine E-coset containment.

In the rank-two case u != 0, and r differs by coordinatewise codewords from

~~~text
(u q_0+v q_1, w q_1).
~~~

After codeword gauge and the triangular affine change, a bad slope gamma for
r corresponds to delta=(v+w gamma)/u for the E-valued pair (q_0,q_1).
The source subfield-confinement theorem gives delta in E. Solving for gamma
proves the asserted affine E-coset containment.

The construction is minimal: an E-valued affine/codeword normal form makes
the syndrome flag E-defined, while an E-defined flag produces the displayed
normal form through the same right inverse.

## Raw-field counterexample mechanism

Start with the integrated base-pole family from
aperiodic_one_ray_saturation.md, whose syndrome flag and bad slopes are
defined over B. Apply an affine shear with a coefficient theta generating a
large extension F/B. The transformed pair has raw coordinate field F, while
its syndrome flag still has F_aff=B and its bad slopes are merely affinely
relabelled. Therefore the individual-line statements

~~~text
slope cost is exactly |F_r|,
small cost iff the raw received-line field is small
~~~

are false. The valid chain is

~~~text
delta_lambda(r) <= |F_aff(r)| <= |F_r|.
~~~

The C7 label for this example is conditional on adopting the collapse-cell
classification; the raw-field counterexample itself is unconditional.

## Ambient-field quantifier repair

The row-level condition

~~~text
log |F_n| = o(n)
~~~

is sufficient for every line to have subexponential F_aff, because
F_aff(r) subset F_n.

For a prize-relevant line with |Z_a(r)|>epsilon |F_n|, confinement gives

~~~text
|F_aff(r)| > epsilon |F_n|,
~~~

so log |F_aff(r)| is within log(1/epsilon) of log |F_n|. This converse is
conditional on existence of a prize-relevant line. If none exists, the row is
already safe and no lower bound on either the canonical or ambient field
follows.

## Nonclaims

- Small F_aff is sufficient, not necessary, for a line to be safe.
- Ledger admissibility or a target reserve alone does not prove small F_aff.
- No primitive A4 payment or post-atlas weighted-Vandermonde leaf is proved.
- No deployed row or grand threshold is closed.
