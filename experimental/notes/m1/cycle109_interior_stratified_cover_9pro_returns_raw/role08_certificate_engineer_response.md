BANKABLE_LEMMA

1. Executive verdict

Verdict: I proved an exact finite-source truth kernel and a conditional certificate-soundness theorem for Cycle109. I also proved a route cut: a single Gate B separator on a HIGH affine-plane chart cannot yield a field-independent polynomial slope cap.

Confidence: high for these two implications; low for the full universal Cycle109 theorem.

This is not a prize proof and not a counterpacket. The unresolved content is the existence, for every official line, of the required LOW/BALANCED/HIGH certificates and the official implication

AP
corr
	​

⟹accepted Gate B certificate or named charge.

The source defines badness support-wise and counts distinct parameters in the line field. Its residue-line normal form is exact, but the source explicitly states that denominator closure alone supplies no packing bound.

2. Exact checker theorem

Let

C=RS[K
line
	​

,D,k],s=k+σ>k,

and let the official line be

u
z
	​

=f+zg,z∈K
line
	​

.
Theorem A: exact fixed-support syndrome kernel

For each S⊆D with ∣S∣=s, let V
S
	​

 be the s×k Vandermonde matrix and let H
S
	​

 have rows forming a basis of the left kernel of V
S
	​

. Define

a
S
	​

=H
S
	​

f∣
S
	​

,b
S
	​

=H
S
	​

g∣
S
	​

.

Then the exact official bad-slope set is

B
off
	​

={z
S
	​

:
S∈(
s
D
	​

), b
S
	​


=0,
a
S
	​

+z
S
	​

b
S
	​

=0
	​

}.

Whenever z
S
	​

 exists, it is unique. Thus the checker obtains z
S
	​

 from any coordinate i with (b
S
	​

)
i
	​


=0:

z
S
	​

=−
(b
S
	​

)
i
	​

(a
S
	​

)
i
	​

	​

,

and verifies the equation in every syndrome coordinate.

Finally,

N
off
	​

=∣B
off
	​

∣

is computed after grouping supports by the canonical field element z
S
	​

. Same-slope support collisions are recorded but contribute zero additional numerator. This is consistent with the source’s one-bad-parameter-per-support theorem.

Theorem B: conditional certificate soundness

Suppose the checker verifies:

exact completeness of B
off
	​

;

exactly one primary branch assignment for each distinct z;

exact distinct-slope caps c
b
	​

 for every paid branch b;

at most n
C
 retained-tag residual charts;

an injective normalization

ν
c
	​

:B
c
	​

↪K
line
	​

for each chart c;

a certified bound

∣ν
c
	​

(B
c
	​

)∣≤c
c
	​

;

source AP
corr
	​

 implies the chart certificate, or a named charge is verified;

the field ledger uses q
line
	​

=∣K
line
	​

∣ as the denominator.

Then

N
off
	​

≤N
cert
	​

:=
paid b
∑
	​

c
b
	​

+
charts c
∑
	​

c
c
	​

.

Consequently, if

N
cert
	​

≤⌊
2
128
q
line
	​

	​

⌋,

then

q
line
	​

N
off
	​

	​

≤2
−128
.

This theorem proves soundness of an accepted certificate. It does not prove that every official line possesses such a certificate.

3. Construction and proof
3.1 Why only supports of size s need enumeration

Suppose z has an official witness S
0
	​

 with ∣S
0
	​

∣≥s. Condition (i) persists on every s-subset of S
0
	​

.

Assume every s-subset simultaneously explains both f and g by degree-<k polynomials. Fix k points R⊆S
0
	​

 and an s-subset T
0
	​

⊇R. Let A
0
	​

,G
0
	​

 be the explanations on T
0
	​

.

For any x∈S
0
	​

∖T
0
	​

, choose an s-subset T
x
	​

 containing R∪{x}. Its explaining polynomial A
x
	​

 agrees with A
0
	​

 on the k points of R. Since both have degree <k, A
x
	​

=A
0
	​

, so A
0
	​

(x)=f(x). The same argument applies to G
0
	​

 and g.

Thus A
0
	​

,G
0
	​

 explain f,g on all of S
0
	​

, contradicting condition (ii). Therefore some s-subset remains bad.

3.2 Syndrome characterization

A word y∣
S
	​

 is in the punctured RS code exactly when

H
S
	​

y∣
S
	​

=0.

Hence u
z
	​

 is explained on S exactly when

a
S
	​

+zb
S
	​

=0.

If b
S
	​

=0, this equation forces a
S
	​

=0, so both f and g are individually explained and condition (ii) fails. Therefore every bad support has b
S
	​


=0, yielding at most one slope.

This proves Theorem A.

3.3 Primary branch records

Each distinct slope receives exactly one primary branch:

ENDPOINT,
TANGENT,
HIDDEN_ACTION_RANK,
	​

QUOTIENT_PERIODIC,
FIELD_CONFINEMENT,
INTERNAL_NORMALIZATION,
	​

CONTAINED_DELETE_ONE,
AFFINE_COLOR,
LOW,BALANCED,HIGH.
	​

SAME_SLOPE is an alias relation between support records, never a primary numerator branch.

For residual branches the checker verifies

LOW
BALANCED
HIGH
	​

:1≤t<σ,
:t=σ,
:t>σ,
	​

where t must have a separately verified intrinsic-denominator minimality certificate.

3.4 Retained chart tags

Every LOW/BALANCED/HIGH slope references exactly one chart. At minimum its retained tag contains:

source object;

support selector;

normalization identifier;

field embedding;

anchor and denominator gauge when applicable;

hidden quotient-action rank signature when applicable.

Thus a support-dependent affine or Möbius normalization cannot be silently identified with another chart.

The checker verifies that each normalization has source and target exactly K
line
	​

, that its domain equals the assigned slope set, and that its normalized values are pairwise distinct.

3.5 Gate B rank verification

For a chart, let A evaluate the chosen degree-bounded polynomial space on the exceptional layer, and let R give the coefficients of restrictions to the chart. The checker computes

rank(A)andrank(
A
R
	​

).

The exact separator condition is

rank(A)<rank(
A
R
	​

).

For a one-parameter complement line or syndrome pencil, this produces a nonzero univariate restriction. A degree-D separator then yields at most D normalized slopes.

3.6 Exact HIGH-plane route cut

A bare affine-plane separator is insufficient.

Let the chart parameter space be K
line
2
	​

, let

M={(0,y):y∈K
line
	​

},

and take

F(X,Y)=X.

Then F vanishes on M but is not identically zero on the affine plane, so rank escape holds. Nevertheless,

z⟼(0,z)

injects every one of the q
line
	​

 slopes into M.

Therefore

HIGH plane rank escape\centernot⟹∣B
c
	​

∣≤n
C
.

A HIGH certificate must instead include at least one of:

a curve equation G=0 with no common component with the separator, giving a Bézout cap;

two independent separators with zero-dimensional common zero set;

an injective reduction to a one-parameter slice;

an exact finite image or separately proved symbolic cap.

A bare transverse affine plane therefore terminates as UNPAID_HIGH_PLANE.

3.7 Field confinement

For a subfield B⊆K
line
	​

, if D,f,g are B-valued, every bad slope lies in B. Hence this branch has cap ∣B∣, while its probability denominator remains q
line
	​

. This is the source’s exact confinement theorem.

4. Executable checker contract

The input contains:

field_ledger:
    p, irreducible line-field modulus
    q_gen, q_code, q_line, q_chal
    field degrees/embeddings
    security_denominator = q_line
    target_bits = 128

instance:
    D, k, sigma, f, g

source truth:
    EXHAUSTIVE_SOURCE
    or PROOF_CARRYING_SOURCE

classifications:
    one record per distinct bad slope

charts:
    retained source tag
    normalization values
    Gate B matrices
    AP_corr receipt
    cap certificate

paid_caps:
    exact cap and proof receipt per paid branch

family_promotion:
    official family
    corrected reserve
    all charges paid/absent
    unbounded growth or systematic Gate B failure

The deterministic terminal precedence is:

FIELD_LEDGER_MISMATCH
UNPAID_LOW_RESIDUAL
UNPAID_BALANCED_COVER
UNPAID_HIGH_PLANE
AP_DESCENT_FAILURE
SOURCE_VALID_COUNTERPACKET / MODEL_ONLY_STRESS_FAMILY
STRATIFIED_COVER_CERTIFIED

SOURCE_VALID_COUNTERPACKET requires proof-kernel verification of an unbounded official family. A finite sequence, finite source instance, or model family is deliberately reported as MODEL_ONLY_STRESS_FAMILY.

The included implementation self-checks finite-field arithmetic, exact support enumeration, matrix ranks, slope deduplication, normalization injectivity, and the integer ledger. Universal branch semantics, denominator minimality, uniformity in k,σ,t, official AP descent, and asymptotic family promotion remain external proof obligations.

Download checker bundle

Read the certificate-engineering report

Open the executable checker

Open the JSON schema

5. Next exact lemma
L-CYCLE110-SOURCE-APCORR-TO-ACCEPTED-CHART-OR-CHARGE

For every official uncharged source object with retained tag and intrinsic denominator degree t, prove one of:

t<σ:
t=σ:
t>σ:
	​

same-field injective LOW residual-image chart with ∣B
c
	​

∣≤n
C
0
	​

;
same-field BALANCED line/pencil separator with ∣B
c
	​

∣≤n
C
0
	​

;
HIGH zero-dimensional plane certificate with ∣B
c
	​

∣≤n
C
0
	​

;
	​

or prove an official endpoint, quotient/periodic, contained/delete-one, tangent, field, affine-color, hidden-action-rank, or normalization charge.

The exponent and the number of tags must be bounded by fixed constants independent of k,σ,t.

The earliest unresolved branch in the checker order is the sharper sublemma:

L-CYCLE110-LOW-RESIDUAL-IMAGE-OR-CHARGE

For 1≤t<σ, after removing all named charges, prove that the official distinct-slope residual image admits at most n
C
1
	​

 retained tags and at most n
C
0
	​

 slopes per tag.

Self-audit

1. What implication did I prove, and what did I not prove?

I proved:

accepted exact certificate⟹N
off
	​

≤N
cert
	​

,

and hence the 2
−128
 bound when the explicit integer inequality passes. I also proved exact finite bad-slope extraction and the insufficiency of one HIGH-plane separator.

I did not prove:

official corrected reserve and AP
corr
	​

⟹such certificates exist for every line.

2. Official-prize relevance?

The truth kernel is source-faithful and officially relevant: it implements the source badness definition directly, not Cycle84’s model. A finite output is nevertheless only a finite research certificate. The universal prize theorem remains open.

3. First possible failure line?

In deterministic branch order:

uncharged LOW source object⟶polynomial same-field residual-image cap.

Across all branches, the central missing implication is source AP
corr
	​

 to an accepted decorated chart or official charge. The weaker HIGH implication using only one plane separator is false.

4. Are the fields and 2
−128
 used correctly?

Yes:

q
gen
	​

: corrected-reserve and entropy hypotheses only;

q
code
	​

: code alphabet/scalar-extension source;

q
line
	​

: distinct-slope field and security denominator;

q
chal
	​

: unused absent a verified protocol-transfer theorem;

target:

N
off
	​

≤⌊q
line
	​

/2
128
⌋.

If q
line
	​

<2
128
, the floor is zero, so only N
off
	​

=0 can pass this exact numerator test.

5. Can the listed structures reduce the numerator?

They can reduce the residual amount sent to Gate B, but they cannot simply be subtracted from raw N
off
	​

.

Same-slope support collisions genuinely do not add numerator.

Contained incidences may be removed after exact nonbadness verification.

Endpoint contributes at most its certified cap, normally one.

Field confinement gives a subfield-size cap but retains denominator q
line
	​

.

Quotient/periodic, tangent, and affine-color slopes still count as distinct bad slopes unless their exact paid cap is included.

Normalization only preserves the count when it is injective and its chart tag is retained.

6. What would convert this to PROOF or COUNTERPACKET?

PROOF requires a proof-kernel certificate for L-CYCLE110-SOURCE-APCORR-TO-ACCEPTED-CHART-OR-CHARGE, uniform chart exponents, every branch cap, and the final explicit q
line
	​

 ledger.

COUNTERPACKET requires an unbounded official above-reserve family with all charges paid or absent, plus a proof of superpolynomial residual slopes, superpolynomial mandatory chart cover, or systematic source-AP-corrected Gate B failure.
