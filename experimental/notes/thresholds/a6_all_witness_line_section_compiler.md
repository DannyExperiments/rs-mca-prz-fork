# A6 all-witness line-section compiler

**Status:** proved experimental theorem, conditional only on the cited
characteristic-free Noether-form theorem.

**Lane:** asymptotic A6 / hard input 3, transverse all-parameter line-section
frontier and canonical two-block stress family.

## Statement

Fix an integer `r>=1` and the canonical source parameters

```text
N=500r,  kappa=225r,  t=150r,  d=250r.
```

Work over any field containing the `N` distinct evaluation points. Fix one
received line and one active weighted-RS chart. Let `Z` be any set of slopes
which retain at least one actual completed witness of weight at most `t` on
that line. Then

```text
|Z| <= 1960 + 3744(1400r+5)^6.                         (1)
```

The bound is independent of the field size, of a witness selector, and of
the first-match order. In particular `|Z|=poly(r)=exp(o(N))`.

The all-parameter extension below sharpens (1) to

```text
|Z| <= 1165 + 3744 D_r^6,
D_r=floor((489950r-1372)/350)+1.                       (1a)
```

The theorem applies before partitioning by the punctured weight `e`.
Consequently it pays the entire fixed-line canonical A6 stress instance,
including the previously open strict central band `50r<e<100r`.

## Source interfaces

The canonical source construction supplies two facts used below.

1. Every actual completed witness has a polynomial representative `f` of
   degree less than `kappa` and a completed polynomial
   `C_gamma=f+Y+gamma V` with at least `N-t` evaluation-domain zeros.
2. Completed witnesses at two distinct slopes have at most `N-d` common
   evaluation-domain zeros. This follows from the literal minimum-lift
   distance `d`, not from an abstract mask-transversality assumption.

The source-valid nonvacuity and the equality `d=250r` are proved in
`completed_zero_mask_two_block.md`.

## One polynomial for every witness

Put

```text
w=kappa-1=225r-1,  m=4,  L=52,  D=1400r-1.
```

Let `Q` range over the span of the monomials

```text
X^alpha Z^beta W^c,
alpha+cw<=D,  beta+c<=L.                                (2)
```

At each evaluation point `x`, impose multiplicity four in the ideal

```text
I_x=(X-x, W+Y(x)+ZV(x)).                                (3)
```

Writing `A=X-x` and `T=W+Y(x)+ZV(x)`, reduction modulo `(A,T)^4`
shows that one coordinate imposes at most

```text
C=sum_(j=0)^3 (4-j)(52-j+1)=520                         (4)
```

linear conditions. The number of available monomials is

```text
U=sum_(c=0)^6 (53-c)((1400-225c)r+c)
 =260050r+1022,                                         (5)
```

where `floor(D/w)=6`. Since `NC=260000r`, the surplus is
`50r+1022>0`; hence a nonzero `Q` satisfying (3) exists.

Now take any actual witness at slope `gamma`. Substitution
`Z=gamma, W=f(X)` gives a polynomial of degree at most `D`. Every one
of the at least `N-t=350r` agreement points is a zero of multiplicity four,
so it has more than `D` zeros counted with multiplicity. Therefore

```text
Q(X,gamma,f(X))=0                                       (6)
```

identically. The same `Q` works for every actual witness; no selector was
used to construct it. This argument uses ideals rather than derivatives and
is valid in every characteristic.

## Specialization spectrum

Remove the `F[Z]`-content of `Q`. Its roots cost at most `L=52` slopes.
Over the algebraic closure of `F(Z)`, group the positive-`W`-degree factors
of the primitive polynomial into field-of-definition orbits. For orbit `i`,
let `q_i` be the degree, including inseparable degree, of its factor cover.
The orbit norms divide `Q`, so

```text
sum_i q_i <= q := deg_W Q <= 6.                         (7)
```

The coefficient map of `Q` has projective `Z`-degree at most `L`.
The projective multiplication identity `mu^*O(1)=O(1,1)` therefore bounds
the coefficient-map degree of the chosen factor on its cover by `q_i L`.

We import the characteristic-free integral Noether forms of Kaltofen,
Theorem 7, whose coefficient degree is at most `12 Delta^6` for a form of
degree `Delta`:

E. Kaltofen, *Effective Noether irreducibility forms and applications*,
J. Comput. Syst. Sci. 50 (1995), 274--295,
<https://doi.org/10.1006/jcss.1995.1023>.

Here every factor has total degree at most

```text
Delta <= D+q = 1400r+5.                                 (8)
```

Pulling back one generically nonzero Noether form charges at most
`12 q_i L Delta^6` reducible specializations on cover `i`.

There is one additional exceptional locus which reducibility forms do not
detect: the factor's `W`-degree can drop on specialization. A generically
nonzero leading-`W` coefficient is a section of degree at most `q_i L`, so
these fibers cost at most `q_i L`. This charge is necessary: for example,
`sW^2+W-X^2` remains irreducible at `s=0` while its `W`-degree drops.

After projecting exceptional cover points to slopes and summing (7), the
exceptional slope set `E` satisfies

```text
|E| <= L + qL(12 Delta^6+1)
     <= 52 + 3744(1400r+5)^6 + 312.                     (9)
```

Outside `E`, every graph factor `W-f(X)` in a specialized fiber comes from a
generic factor of `W`-degree one. Thus every nonexceptional actual witness
lies on one of finitely many integral factor covers, with total cover degree
at most six. This includes repeated, Galois, and purely inseparable factors.

## Moving-root count

On a `W`-linear factor cover write the factor as `A(X)W+B(X)` and form the
completed numerator

```text
P(X)=A(X)(Y(X)+pi V(X))-B(X).                            (10)
```

If the cover degree is `q_i`, the projective polynomial map defined by `P`
has degree at most

```text
delta_i <= q_i(L+1).                                    (11)
```

Assign each nonexceptional slope one representing cover point. On a cover
carrying at least two assigned slopes, the common fixed domain-root set has
size at most `N-d`; hence each assigned completed polynomial has at least
`d-t=100r` nonfixed roots. A nonfixed evaluation root cuts a hyperplane
section of degree at most `delta_i`. Double counting gives

```text
|Z_i|(d-t) <= N delta_i.                                (12)
```

The covers carrying at most one assigned slope contribute at most `q=6`.
Using (7) and (11),

```text
|Z\E| <= 6 + floor(N q(L+1)/(d-t))
      = 6 + 1590 = 1596.                               (13)
```

Adding (9) and (13) proves (1).

## Transverse all-parameter extension

Let

```text
N=R+kappa,  a=N-t,  w=kappa-1,
```

with `kappa>=2` and `0<=t<R`.  Fix one received syndrome line
`y_0+gamma y_1`, with `y_1!=0`, and one active weighted-RS chart.  Every
retained slope must carry an actual completed witness satisfying

```text
H_D c_gamma = y_0+gamma y_1,
wt(c_gamma)<=t.
```

Define the literal minimum-lift distance

```text
d=min{wt(v):H_D v=y_1}.
```

Assume also that every retained completed witness satisfies the source
transversality condition

```text
{y_0,y_1} is not contained in
span{h_x : x in supp(c_gamma)}.                         (T)
```

For integers

```text
mu>=1,  L>=q>=1,  qw<=D<mu a,
```

define

```text
C_mu(L) = sum_{j=0}^{min(mu-1,L)} (mu-j)(L-j+1),
U_w(D,L,q) = sum_{c=0}^q (D-cw+1)(L-c+1).              (14)
```

Call the tuple section-admissible when

```text
U_w(D,L,q)>N C_mu(L).                                  (15)
```

The interpolation and specialization proof above works verbatim with these
parameters.  The specialized total degree is in fact

```text
Delta<=D,                                               (16)
```

because every specialized monomial has total `(X,W)` degree
`alpha+c<=alpha+cw<=D`.

Define

```text
rho(t,d) = t+1       when d<=t,
           d/(d-t)  when d>t.                           (17)
```

Then every section-admissible tuple gives the exact integer bound

```text
|Z| <= L + qL(12D^6+1) + q
       + floor(q(L+1)rho(t,d)).                         (18)
```

The four terms charge `F[Z]`-content, reducible and vertical-degree-drop
specializations, singleton covers, and nonfixed moving roots.

### Transversality supplies the missing root

On one integral `W`-linear factor cover let `G` be the common fixed domain
root set and put `g=|G|`.  Every assigned witness has at least

```text
h=max(1,a-g)                                            (19)
```

nonfixed roots.  The ordinary `a-g` term is the weight bound.  If it vanishes
and a witness had no root outside `G`, its support would be exactly `D\G`.
Two slopes on the cover put both syndrome-line points, hence `y_0` and `y_1`,
in the span of those support columns, contradicting (T).

If the cover numerator map has degree `delta_i<=q_i(L+1)`, double counting
nonfixed roots gives

```text
|Z_i| max(1,a-g) <= (N-g)delta_i.                       (20)
```

Without direction distance, the maximum of the ratio on the right is `t+1`.
If two distinct-slope witnesses have at most `N-d` common roots, then
`g<=N-d`; maximizing over that interval gives `d/(d-t)` when `d>t` and the
same `t+1` bound when `d<=t`.  Summing the cover degrees proves (18).  Thus
`d<=t` is not a wall once the universal interpolation polynomial exists.

## Exact section-capacity frontier

Put

```text
J_sec=(N-t)^2-N(kappa-1)=a^2-Nw.                        (21)
```

There exists a section-admissible tuple in the four-parameter monomial family
if and only if

```text
J_sec>0.                                                (22)
```

This is an iff for the uniform dimension-count certificate (14)--(15).  It
does not forbid accidental instance-specific interpolation dependencies.

### Necessity

Assume `a^2<=Nw` and put `x=a/N`.  Since `D<mu a`, each summand of `U_w` is
bounded by a triangular weight times `(mu a-cw)_+`.  The inequality
`w/N>=x^2` and the prefix majorization

```text
x sum_{c=0}^s (mu-cx)_+
  <= sum_{c=0}^s (mu-c)_+                               (23)
```

imply `U_w(D,L,q)<=N C_mu(L)` after expressing the weights
`L-c+1` as sums of prefix indicators.  For `s<=mu-1`, (23) follows by direct
summation; after saturation, the full left sum is at most
`mu(mu+1)/2`.  Hence strict surplus is impossible.

### Sufficiency

Assume `a^2>Nw`.  Take `D=mu a-1` and `q=floor(D/w)`.  For
`L>=max(q,mu-1)`, the surplus is affine in `L`.  Its coefficient is positive
for all sufficiently large `mu`, because

```text
mu^-2 sum_{c=0}^q (mu a-cw)  -> a^2/(2w),
mu^-2 N mu(mu+1)/2           -> N/2.                    (24)
```

The strict inequality in (21) separates the limits.  After fixing such a
`mu`, choosing `L` large enough makes the affine surplus positive.  This
proves existence and completes (22).

For fixed positive margins `w>=theta N` and `J_sec>=epsilon N^2`, the choices
may be made with `mu,q,L=O_{theta,epsilon}(1)` and `D=O(N)`.  Equation (18)
then gives `|Z|=O_{theta,epsilon}(N^6)`.

## Exact optimizer and canonical sharpening

For fixed `(mu,L,q)`, write

```text
A_{L,q} = sum_{c=0}^q (L-c+1),
b_{w,L,q} = sum_{c=0}^q (1-cw)(L-c+1).
```

The least degree satisfying the strict dimension inequality is

```text
D*(mu,L,q)
  = max(qw, floor((N C_mu(L)-b_{w,L,q})/A_{L,q})+1).    (25)
```

It is feasible exactly when `D*<mu a`.  Since (18) increases with `D`, the
minimum of its right side over all feasible `(mu,L,q,D*)` is the strongest
bound certified by this monomial family.

For the canonical row retain `(mu,L,q)=(4,52,6)` and use

```text
D_r=floor((489950r-1372)/350)+1.                        (26)
```

Here `rho(t,d)=5/2`, `Delta<=D_r`, and (18) becomes exactly (1a).  This
strictly improves the earlier `1960+3744(1400r+5)^6` bound while preserving
all of its source and first-match hypotheses.

The source aperiodic-ray theorem supplies transverse exact-witness families
with `J_sec<0` and exponentially many slopes.  It therefore refutes a
universal polynomial theorem over the entire `J_sec<=0` transverse class.
It is not asserted here that those examples survive every earlier owner cell
or occupy the final unpaid balanced-core residual.

## Why this moves the board

Earlier A6 charges use a fixed witness selector, a nonnegative exponent
branch, or a bounded actual-core rank. The construction above is genuinely
all-witness: one interpolation polynomial contains every completed witness
on the fixed received line. The specialization and moving-root steps then
turn that universal containment into a polynomial distinct-slope bound.

This closes the canonical fixed-line hard-input-3 stress instance and proves
the exact all-parameter section-capacity frontier for the displayed monomial
family. It does
not sum the result over an unbounded collection of received lines, active
charts, or realized profiles; that still requires a witness-exhaustive
subexponential atlas.

## Audit correction record

The originating worker proposed an unsupported quartic Noether bound and did
not charge vertical-degree-drop fibers. Two independent hostile audits found
both defects. Equation (1) uses the published sixth-power Noether degree and
adds the missing `qL=312` charge. No quartic bound from that packet is used.

## Nonclaims

This note does not prove:

- the worker's quartic `O(r^4)` bound or its general `N^24` estimate;
- a multiplicity bound for witnesses sharing one slope;
- a witness-exhaustive atlas or a bound across different received lines,
  active charts, or realized profiles;
- a polynomial theorem for the entire `J_sec<=0` region or a theorem that its
  source obstruction survives every earlier first-match cell;
- hard input 2, the unsafe/lower reserve, a deployed finite-row crossing,
  Grand MCA, Grand List, or either prize question.

The official score remains `0/2`. No stable-paper TeX is changed.
