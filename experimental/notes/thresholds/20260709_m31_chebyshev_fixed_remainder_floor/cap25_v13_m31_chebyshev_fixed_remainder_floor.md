# CAP25 v13 M31 Chebyshev fixed-remainder floor

Status: `BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT`.

This note records a narrow hostile-audited computation for the deployed
Mersenne-31 list row in the CAP25 v13 finite-adjacent program. It does not prove
the adjacent safe row, does not give a counterpacket, and does not close
row-sharp Q. Its value is to replace a loose "M31 symmetry" intuition by one
exact Chebyshev fixed-remainder floor and the resulting residual target.

## Board anchor

The live finite goal remains the adjacent certificate

```text
U(a0 + 1) <= B* < L(a0).
```

For the Mersenne-31 list row:

```text
p        = 2^31 - 1
n        = 2^21
k        = 2^20
a+       = 1116023
w        = a+ - k = 67447
B*       = 2^24 - 1 = 16777215
avg_ceil = ceil(binomial(n, a+) / p^w) = 1993678
```

Thus the full max-fiber target has only

```text
log2(B* / avg_ceil) = 3.072998926581202 bits
```

of visible overhead.

## Domain correction

The Mersenne-31 row should not be treated as a multiplicative-root coset in
`F_p^*`. The usable finite symmetry is the Chebyshev / twin-coset structure of
the line-round row. Consequently, multiplicative mode-at-null or primitive
orbit heuristics are not theorem-facing inputs for this deployed row.

The relevant dyadic operation is the Chebyshev fold at scale `c=2^j`. For a
fixed remainder class inside one fold fiber, the induced quotient problem has
parameters

```text
N_c = n / c
f_c = floor(a+ / c)
r_c = a+ mod c
t_c = floor(w / c)
```

and, when `r_c > 0`, one quotient point is reserved by the fixed remainder
choice. The fixed-remainder lower floor used here is

```text
F_c = ceil(binomial(N_c - 1, f_c) / p^t_c).
```

This is a lower-floor / residual-target computation, not an upper ledger.

## Exact replay values

For the list row, the largest fixed-remainder dyadic floor among
`c=2^j`, `0 <= j <= 20`, is at `c=2048`:

```text
c     = 2048
N_c   = 1024
f_c   = 544
r_c   = 1911
t_c   = 32
F_c   = ceil(binomial(1023, 544) / p^32) = 6796405
```

This consumes about `40.51%` of the budget:

```text
B* - F_2048                  = 9980810
log2(B* / F_2048)            = 1.303659518930735 bits
log2((B* - F_2048)/avg_ceil) = 2.3237244851910264 bits
```

For comparison, the already printed Mersenne-31 MCA watch item is

```text
ceil(binomial(1024, 545) / p^32) = 12769758
B* - 12769758                    = 4007457
```

The hostile audit also replayed the naive dyadic fixed-remainder sum

```text
sum_{0 <= j <= 20} F_{2^j} = 16548620
B* - sum_j F_{2^j}          = 228595
```

This is not a counterpacket, because no theorem currently co-locates those
dyadic floors in one target fiber and no additivity/stacking theorem is being
claimed here. It is only a sharp warning that the finite margin is extremely
thin if a future chaining theorem exists.

## Surviving lemma

The bankable local lemma is:

```text
CAP25-V13-M31-CHEBYSHEV-FIXED-REMAINDER-FLOOR.

In the Mersenne-31 list row, the c=2048 Chebyshev fixed-remainder quotient
floor contributes an exact lower floor of 6796405 to the corresponding planted
target condition, under the fixed-remainder convention above.
```

The exact arithmetic is replayed by
`m31_chebyshev_fixed_remainder_floor.py`.

## Nonclaims

This note does not claim:

- `U(1116023) <= B*`;
- row-sharp Q for the Mersenne-31 list row;
- a counterpacket to the Mersenne-31 list adjacent candidate;
- a proof that dyadic fixed-remainder floors stack additively;
- a finite safe-side certificate for any of the four deployed rows.

## Next exact target

The next theorem-facing obstruction is a planted-conditioned residual
flatness/chaining statement:

```text
CAP25-V13-CHEBYSHEV-CHAINED-TARGET-RESIDUAL-FLATNESS.

After conditioning on the c=2048 fixed-remainder planted floor in the
Mersenne-31 list row, prove that the remaining primitive residual target mass
is at most 9980810, or exhibit a co-located dyadic-chain counterpacket.
```

Equivalently, the residual family must fit inside only
`2.3237244851910264` bits above the identity average. This is now the sharper
M31-list finite audit target.
