# Role 04: Gate B Rank-Containment Counterpacket

Assume Gate A is true. Your job is to attack Gate B.

Try to construct an `AP_corr(Uhat)` for which the complement line:

```text
L_U(theta)=(v_j - theta*v_{j-1})_{j=1}^d
```

is contained in, or has too-large intersection with, the bounded-degree
exceptional closure of `M_m`.

The ideal `COUNTERPACKET` is a growing family with:

```text
AP_corr(Uhat) true
super-polynomially many distinct external active theta values
no quotient/periodic/coset/same-slope/affine-normalization collapse
```

If you only find a finite/model stress packet, label it as `BANKABLE_LEMMA`,
`ROUTE_CUT`, or `PLAN`, not `COUNTERPACKET`.

Use the provided scripts and certificates as data, but do not treat them as
source validity. The p97 packet is currently only finite stress:

```text
distinct_theta_count = 7
distinct_external_theta_count = 6
decision = ROUTE_CUT_FINITE_MODEL_TOO_WEAK
```

Return `COUNTERPACKET`, `BANKABLE_LEMMA`, `ROUTE_CUT`, `EXACT_NEW_WALL`, or
`PLAN`.
