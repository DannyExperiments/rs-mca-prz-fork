# CYCLE87 Explicit `U` Separator and 464-Point Two-Copy Certificate

## Status

**PROOF**, conditional only on the Cycle84/Cycle85 facts explicitly banked in the Cycle87 common prompt.

This closes the active wall

```text
L-CYCLE86-EXPLICIT-TWO-COPY-SEPARATOR-CERTIFICATE
```

with the preferred package

```text
(n,k,sigma,j) = (464,232,6,226).
```

The separator is the concrete element

```text
y = U in L = F0[U]/(U^3-beta).
```

The exact census proves the stronger bound

```text
mu_proj(U) <= 2.
```

The resulting one-code, one-line GRS construction therefore has at least

```text
P*N/2 = 1,391,152,917,379,006,070,784
```

distinct transverse slopes, exceeding

```text
floor(17^48 / 2^128) = 338,617,018,271,848,945,628.
```

The margin is

```text
1,052,535,899,107,157,125,156.
```

This is an official-profile **MCA numerator lower counterpacket**. It is not, by itself, the full prize theorem.

---

## 1. Banked inputs and what is new

The following are treated as banked inputs, exactly as authorized by the common prompt:

```text
P = |P0| = 52,747,567,104
N = Occ(beta) = 52,747,567,092
m_max(beta) = 2
D = 24
```

The banked Cycle85 transfer supplies the support family `P0`, support size 113, the common six-jet

```text
J_T(t) = product_{x in T}(1-x t) == 1-t (mod t^6),
```

and the one-copy interpretation of `rho(T)=P_T(beta)`.

The new work in this packet is:

1. a fully specified degree-48 field and the explicit separator `y=U`;
2. an exact, deterministic smooth-quotient census proving `mu_proj(U)<=2`;
3. a materialized 464-point domain, 232-by-464 GRS parity-check matrix, and affine syndrome line;
4. the exact reciprocal-product slope formula and transverse-incidence proof;
5. a replay bundle with source, certificates, binary artifacts, and hashes.

The new projective census does **not** assume that the Cycle84 beta-product census controls evaluation at `U`. It recomputes the relevant 52,747,567,104 separator values through an independent quotient projection.

---

## 2. Exact field models

### 2.1 Base field

Let

```text
f(X) = X^16 + X^8 + 3
F0   = F_17[X]/(f)
q    = |F0| = 17^16 = 48,661,191,875,666,868,481.
```

Elements are encoded as sixteen bytes

```text
(a0,...,a15), 0<=ai<17,
```

representing `sum ai X^i`.

Multiplication is convolution followed by the reduction rule

```text
X^d = -X^(d-8) - 3 X^(d-16),  d>=16.
```

The standard-library setup verifier proves irreducibility by Rabin's criterion:

```text
X^(17^16) mod f = X,
X^(17^8)  mod f = -X,
gcd(f, X^(17^8)-X) = gcd(f,-2X) = 1.
```

Set

```text
eta  = 6 X^9,
beta = X+2.
```

The verifier checks

```text
eta^256 = 1,
eta^128 = -1,
```

so `eta` has exact order 256. It also checks

```text
beta^((q-1)/3) = 2 + 5 X^8 != 1.
```

Since `q == 1 (mod 3)`, this proves that `beta` is not a cube in `F0`.

### 2.2 Cubic extension and separator

Define

```text
L = F0[U]/(U^3-beta).
```

Because `beta` is not a cube, `U^3-beta` is irreducible. Hence

```text
[L:F0] = 3,
[L:F_17] = 48,
|L| = 17^48.
```

An element is encoded as

```text
a0 + a1 U + a2 U^2,  ai in F0,
```

using 48 bytes in the order `a0`, `a1`, `a2`.

Multiplication is exactly

```text
c0 = a0*b0 + beta*(a1*b2+a2*b1)
c1 = a0*b1 + a1*b0 + beta*a2*b2
c2 = a0*b2 + a1*b1 + a2*b0.
```

The chosen separator and translation are

```text
y = U,
c = beta-U.
```

---

## 3. Exact support circuit and `P_T(U)`

The three banked support-offset sets are

```text
E1 = {0,1,2,3,5,11,12,13}
E2 = {0,1,2,3,4,8,9,14}
E3 = {0,1,2,4,5,7,11,14}.
```

The shell colors are

```text
(s1,s2,s3) = (15,9,12).
```

A packet tuple is

```text
omega = (o1,...,o7),  0<=ot<48,
ot = 16*(it-1)+at,
it in {1,2,3}, at in Z/16Z.
```

It is admissible iff

```text
sum_{t=1}^7 (s_it + 8*(at mod 2)) == 4 (mod 16).
```

The corresponding support is

```text
T_omega = {1}
          union over t=1..7
          { eta^(t+8b), -eta^(t+8b) : b in at+E_it }.
```

Each slot contributes 16 points in a distinct residue class modulo 8, so every support has exactly

```text
1 + 7*16 = 113
```

points. No nonidentity element of `mu_32=<eta^8>` occurs in a support.

For `t=1,...,7`, `i=1,2,3`, and `a=0,...,15`, define

```text
G[t,i,a] = product_{b in a+E_i} (U^2 - eta^(2t+16b)).
```

Then

```text
P_T(U) = (U-1) * product_{t=1}^7 G[t,it,at].
```

The common factor `U-1` is omitted in the multiplicity census because multiplication of every value by one fixed nonzero element is a bijection on projective classes.

The 336 factors, in the order `(t,i,a)`, have canonical byte-stream SHA-256

```text
e64ab0c0e51c9f0487557916486a5fcb8360b8fb97de1000a6931afe5945851c.
```

The setup verifier reconstructs this stream from field arithmetic rather than trusting a supplied table.

---

## 4. Equality in `L^x/F0^x`

For nonzero `z,w in L`, define

```text
K(z) = z^(q-1).
```

Then

```text
[z]=[w] in L^x/F0^x
iff z/w is in F0^x
iff (z/w)^(q-1)=1
iff K(z)=K(w).
```

The kernel assertion is exact: `L^x` is cyclic of order `q^3-1`, and

```text
gcd(q-1,q^3-1)=q-1.
```

Thus the equation `x^(q-1)=1` has exactly `q-1` roots; the embedded group `F0^x` already supplies all of them.

An independent exact canonical key, useful for refinement, is pivot normalization. Write

```text
z = z0+z1 U+z2 U^2.
```

Choose the least `r` with `zr!=0`, multiply all three coordinates by `zr^(-1)`, and encode `r` plus the two nonpivot coordinates. Two nonzero elements have the same key iff they differ by a scalar in `F0^x`.

---

## 5. Smooth quotient domination

Direct discrete logarithms in the full projective quotient would encounter a large hard factor. They are unnecessary for the required upper bound.

The projective quotient has order

```text
Q = q^2+q+1
  = 2,367,911,594,760,467,245,892,767,489,196,618,115,843.
```

It factors as

```text
Q = R*M,
R = 48,661,191,868,691,111,041,
M = 48,661,191,882,642,625,923,
gcd(R,M)=1,
```

with

```text
M = 3*7*13*73*307*1321*72337*83233.
```

Define the coarser key

```text
pi(z) = z^((q-1)R).
```

This maps `L^x/F0^x` onto a cyclic group of order `M`. Therefore

```text
[z]=[w]  =>  pi(z)=pi(w).
```

Every exact projective fiber is contained in one `pi`-fiber. Consequently

```text
mu_proj(U) <= mu_M(U),
```

where `mu_M(U)` is the maximum multiplicity under `pi`.

This direction is the crucial soundness point: the smooth projection may create false **collisions**, but it cannot split an exact collision. Hence an upper bound on its larger fibers is automatically an upper bound on the true projective fibers.

---

## 6. Deterministic census algorithm

### 6.1 Exact logarithms modulo `M`

The checker chooses the first element in a fixed candidate sequence whose smooth projection has exact order `M`. It finds the projection of `U+1`, encoded as

```text
07000000070005000000100000000c00050f000c010d06070f000a0b000201050b0e0b0f01030e050106090807040a04.
```

Exact order is checked by exponentiation for every prime divisor of `M`.

For each of the 336 projected slot factors, the checker computes its logarithm modulo every prime factor of `M` by a complete lookup table, combines the residues by CRT, and verifies

```text
h^log == projected_slot_factor
```

in `L`. No unverified discrete logarithm is accepted.

### 6.2 Meet-in-the-middle representation

For every choice in slots 1--3, store

```text
(left_log, left_color, left_tuple_id).
```

There are

```text
48^3 = 110,592
```

left records.

For every choice in slots 4--7, store

```text
(right_log, right_tuple_id)
```

in one of 16 exact color buckets. There are

```text
48^4 = 5,308,416
```

right records.

A complete tuple is admissible exactly when

```text
left_color + right_color == 4 (mod 16).
```

The checker independently obtains exactly

```text
52,747,567,104
```

compatible records.

### 6.3 Exact deterministic sharding

The cyclic interval `[0,M)` is partitioned into 1,536 half-open intervals

```text
I_s = [floor(sM/1536), floor((s+1)M/1536)).
```

For every left record, binary searches in the appropriate sorted right-color bucket enumerate exactly the right records whose modular sum lies in `I_s`.

Each shard has exactly

```text
52,747,567,104 / 1,536 = 34,340,864
```

records on average, and every shard width is at most

```text
31,680,463,465,262,127 < 2^55.
```

The in-memory table stores the full shard offset, not a fingerprint. `mix64` is used only to select a probing location. Equality compares the exact offset. Hash collisions can affect runtime but cannot merge keys or hide multiplicity.

Every compatible tuple belongs to exactly one shard. Thread scheduling changes only progress-message order, never the mathematical output.

### 6.4 Executed output

The full four-thread execution returned

```text
records                              = 52,747,567,104
smooth projected occupancy           = 52,747,567,062
smooth ordered off-diagonal energy   = 84
smooth maximum multiplicity          = 2
threshold-9 hit                      = none
```

The identity

```text
84 = 2*(52,747,567,104 - 52,747,567,062)
```

and the maximum-two result imply the complete smooth histogram

```text
multiplicity 1: 52,747,567,020 classes
multiplicity 2: 42 classes
multiplicity >=3: 0 classes.
```

Therefore

```text
mu_proj(U) <= mu_M(U) = 2 <= 8.
```

Execution statistics:

```text
shards             = 1,536
threads            = 4
wall time           = 940.49 s (15:40.50 including /usr/bin/time wrapper)
maximum resident    = 2,299,780 KiB
exit status         = 0.
```

An independent sort-and-run-length reducer was executed on two audit shards. It does not use the open-address multiplicity table:

```text
shard 0:    pairs 34,348,932; unique 34,348,932; D=0; max=1
shard 1024: pairs 34,345,098; unique 34,345,097; D=2; max=2
```

These agree with the corresponding hash-table shard outputs, including the sampled double class in shard 1024.

---

## 7. No-false-negative exact fallback and failure output

The smooth checker is a one-sided certificate:

* if its maximum is at most 8, the desired theorem is proved;
* if it finds a class of size at least 9, that alone is **not** a counterexample, because the class may split under exact projective equality.

An always-exact fallback is:

1. Enumerate every admissible tuple.
2. Compute its product in `L` from the seven slot factors.
3. Compute the pivot-normalized 33-byte exact projective key.
4. Externally sort by `(key,tuple_id)`.
5. Scan exact equal-key runs.

This computes `mu_proj(U)` exactly and has no false negatives. A direct 40-byte record layout would require about 2.11 TB for all records, so the smooth-first protocol is preferable.

If the smooth stage ever reports a class of size at least 9, a low-storage exact refinement is sufficient:

1. emit every heavy smooth key and its exact smooth count;
2. make a second pass collecting only tuples in those heavy classes;
3. replace the smooth key by the exact pivot-normalized key;
4. sort and scan each heavy class.

A route-killing output for `y=U` must contain:

```text
PROJECTIVE_MMAX_GE_9
one exact projective key
nine distinct admissible tuple IDs
```

The verifier recomputes all nine `P_T(U)` values and verifies the scalar ratios in `F0^x`. Such a witness kills only the `mu_proj(U)<=8` shortcut for this separator. It does not disprove the generic product route or another separator.

---

## 8. The shortened 464-point domain

Let

```text
D = <eta> = mu_256.
```

Every packet support avoids `mu_32\{1}`. Delete the first 24 nonidentity `mu_32` points:

```text
Z0 = {eta^(8b): 1<=b<=24},
D- = D\Z0.
```

Then

```text
|D-|=232
```

and every `T in P0` remains contained in `D-`.

With `c=beta-U`, define

```text
D^(2) = D- union (c+D-).
```

The blocks are disjoint because `c` is not in `F0`. The materializer checks all 464 points are distinct and that `beta` is absent.

The domain generates `L`:

* `D-` contains `eta`, whose degree over `F_17` is 16, so it generates `F0`;
* the domain contains `1` and `c+1`, hence it generates `c`;
* it then generates `U=beta-c`.

Thus

```text
q_gen = q_code = q_line = q_chal = 17^48.
```

The ordered domain binary SHA-256 is

```text
2bda8227b5090cb4f9b30e96c2f3442c487a64349ff61fa48dd803e6d1c23abd.
```

---

## 9. One GRS code and one affine syndrome line

For every `x in D^(2)`, define the 232-coordinate column

```text
h_x = (1,x,...,x^230,(beta-x)^(-1))^T.
```

Multiplying the `x`-column by `beta-x` changes the row functions to

```text
1, (beta-Y), Y(beta-Y), ..., Y^230(beta-Y).
```

These form a basis of `L[Y]_{<=231}`: evaluation at `Y=beta` first isolates the constant term, then divisibility by `beta-Y` gives the remaining independence. Hence the matrix is row- and nonzero-column-equivalent to a 232-row Vandermonde parity-check matrix. It defines one GRS code with

```text
[n,k]=[464,232].
```

The full matrix binary SHA-256 is

```text
e0e6c4519490b2256d3df81c483f1c6697cbe2433852cf07c53c7f1f1726e281.
```

### 9.1 Combined supports

Choose the lexicographically first support `T_v` in each occupied beta-product fiber

```text
v in Omega = {P_T(beta):T in P0}.
```

There are exactly `N` such representatives by the banked Cycle84 census.

For `v in Omega` and `T in P0`, define

```text
S(v,T) = T_v union (c+T).
```

The blocks are disjoint, so this is a 226-point support. The support map is injective in its two support inputs.

### 9.2 Common six-jet

For a base support, banked Cycle85 gives

```text
J_T(t) == 1-t (mod t^6).
```

Translation gives

```text
J_{c+T}(t)
 = (1-ct)^113 J_T(t/(1-ct))
 == (1-ct)^112 (1-(c+1)t) (mod t^6).
```

Therefore every combined support has the same jet

```text
A(t) = (1-t)(1-ct)^112(1-(c+1)t) (mod t^6).
```

Write

```text
A(t)^(-1) == h0+h1 t+...+h5 t^5 (mod t^6).
```

For a combined support `S`, put

```text
a_x = 1/P_S'(x), x in S.
```

The partial-fraction identity

```text
1/P_S(Y) = sum_{x in S} a_x/(Y-x)
```

implies

```text
sum a_x x^m = 0,                0<=m<=224,
sum a_x x^(225+r) = h_r,       0<=r<=5,
sum a_x/(beta-x) = 1/P_S(beta).
```

Thus all supports represent points on the single affine line

```text
ell(z) = u+zv,
u = (0,...,0,h0,...,h5,0),
v = (0,...,0,1),
```

where `h0,...,h5` occupy rows 225 through 230 and the direction is the last coordinate.

The line binary SHA-256 is

```text
dce95315fed38dee0286888a252a16536888f9032d662cdd471cbb2b028a4eb7.
```

This is one affine syndrome line for one GRS code, not a direct sum or tensor of two lines.

### 9.3 Transversality and full coordinates

Every `a_x` is nonzero because each support is squarefree.

If the line direction belonged to the span of the 226 support columns, projection to the first 231 rows would produce a linear dependence among 226 distinct Vandermonde columns. The 231-by-226 Vandermonde matrix has full column rank, so all coefficients would be zero, contradicting the nonzero last coordinate of the direction.

Hence every counted incidence is transverse and no support span contains the line.

---

## 10. Exact slope formula and count

For `S(v,T)=T_v union(c+T)`,

```text
P_S(beta)
 = P_{T_v}(beta) * product_{x in T}(beta-(c+x))
 = v * P_T(U).
```

Therefore the direct line coordinate is

```text
z_{v,T} = 1/(v P_T(U)),
```

up to a single common nonzero scalar and/or affine sign convention. Inversion and any common affine normalization are bijections and preserve cardinality.

There are `N*P` input pairs. If

```text
v P_T(U) = v' P_T'(U),
```

then

```text
[P_T(U)] = [P_T'(U)] in L^x/F0^x.
```

For a fixed product and fixed second support `T`, the first factor `v` is uniquely determined. Thus every pair-product fiber has size at most `mu_proj(U)`. The census gives `mu_proj(U)<=2`, so

```text
# distinct slopes >= N*P/2
                  = 1,391,152,917,379,006,070,784.
```

The official target is

```text
T_line = floor(q_line/2^128)
       = floor(17^48/2^128)
       = 338,617,018,271,848,945,628.
```

Hence the official MCA numerator failure row is certified with margin

```text
1,052,535,899,107,157,125,156.
```

Even the originally requested conservative denominator 8 gives

```text
N*P/8 = 347,788,229,344,751,517,696
      > T_line
```

by `9,171,211,072,902,572,068`.

---

## 11. Certificate outputs

### PASS

The executed PASS is valid when all of the following hold:

```text
field/setup verifier: SETUP_VERIFIED
records:              52,747,567,104
smooth max:           <= 8
GRS artifact verifier: GRS464_ARTIFACTS_VERIFIED
profile:               (464,232,6,226), t=1
threshold comparison:  lower > floor(17^48/2^128)
```

The actual run is stronger: smooth maximum 2.

### Refinement required

A smooth class of size at least 9 produces

```text
COARSE_MMAX_GE_9_REFINEMENT_REQUIRED
```

and must not be mislabeled as a projective counterexample.

### Exact route kill for `U`

Only an exact projective class with nine distinct admissible tuple IDs proves

```text
PROJECTIVE_MMAX_GE_9.
```

The emitted witness must contain the exact canonical projective key and the nine tuple IDs, all independently replayed.

---

## 12. Scope separation

### Finite-model certificate

The Cycle84 values `P`, `N`, `m_max(beta)=2`, and `D=24` remain finite-model inputs. They are not reclassified as a prize theorem.

### One-copy RS/MCA transfer

The Cycle85 fixed-six-jet and reciprocal-slope transfer are used as banked lemmas. This packet does not claim to have independently reproved the entire Cycle65--85 chain.

### Official two-copy counterpacket

The new `U` census plus the materialized 464-point GRS line prove an official-profile MCA numerator lower counterpacket over `F_17^48`.

### Public replay artifact

The replay bundle contains the exact field/setup verifier, census source and output, materializer, binary domain/matrix/line artifacts, artifact verifier, schemas, report, and SHA-256 manifest.

### Full prize theorem

Not proved here. Any final prize-level theorem still has to splice this official MCA counterpacket into the complete public reduction and quantify exactly what overarching conjecture or claimed bound it refutes or establishes.

---

## 13. Self-audit

### 1. Exact implication proved and not proved

**Proved:** under the banked Cycle84/Cycle85 packet facts, the concrete separator `U` satisfies

```text
mu_proj(U) <= 2,
```

and the explicit `[464,232]` GRS code and one affine syndrome line contain at least

```text
N*P/2 = 1,391,152,917,379,006,070,784
```

distinct transverse bad slopes.

**Not proved:** the exact value of `mu_proj(U)` is not determined; the smooth quotient proves only the upper bound `<=2`. The full prize theorem and the entire historical reduction chain are not reproved.

### 2. Official relevance

This is official-prize-relevant as an official-profile **MCA numerator lower counterpacket**. It is more than a finite-model certificate. It is still not the full prize theorem.

### 3. First possible failure line

The first external dependency where the theorem could fail is the banked assertion that the Cycle84 tuple circuit gives `P` distinct 113-point supports with the fixed exact six-jet `J_T(t)==1-t mod t^6`, and that the beta-product occupancy is exactly `N`.

Inside the new work, the first possible failure would be a replay mismatch in the setup/slot-factor stream or a census result other than the recorded exact totals. Both are exposed by deterministic verifiers and hashes.

### 4. Field roles and target

```text
q_gen  = 17^48  because the domain generates F0 and U
q_code = 17^48  because the GRS matrix is over L
q_line = 17^48  because the affine line is over L
q_chal = 17^48  as the declared compatible challenge field
```

Only `q_line` enters

```text
floor(q_line/2^128).
```

No extra `q_chal` factor is inserted into the numerator or denominator.

### 5. Possible numerator reductions

* **Quotient/periodic structure:** paid exactly through projective classes; the stronger smooth coarsening has maximum 2.
* **Contained incidences:** excluded by the 231-by-226 Vandermonde rank argument.
* **Same-slope collisions:** bounded by `mu_proj(U)<=2` and already divided out.
* **Affine color normalization:** a common affine map with nonzero linear coefficient is bijective.
* **Support duplication:** excluded by disjoint blocks and the banked injectivity of the base support circuit.
* **Representative loss:** the first coordinate uses exactly one support for each of the `N` occupied beta values; the second uses all `P` supports. The numerator is `N*P`, not an unjustified `P^2`.

### 6. Next exact lemma toward a full solve

This answer is not a PLAN. The active separator wall is closed. The next exact theorem is the public splice lemma:

```text
L-CYCLE87-OFFICIAL-MCA-COUNTERPACKET-TO-FULL-PRIZE-REDUCTION
```

It must state the complete prize theorem's quantifiers and show exactly how this one official `(t,n,k,sigma,j,q_line)` failure row invalidates or resolves that theorem, without replacing the MCA numerator by a scalar-list numerator and without changing the field ledger.
