# Cycle 75 Direct Maximum-Fiber Audit

## Verdict

```text
BANKABLE_LEMMA / PLAN
```

Confidence: high for the meet-in-the-middle design and route corrections;
high for the local left-half product-injectivity certificate; unknown for the
full `m_max(beta)<=12` target because no full census was executed.

Cycle 75 does **not** prove:

```text
m_max(beta) <= 12.
```

It gives the first concrete direct-max-fiber architecture below the Role 05
model packet and clarifies that the constrained domain, not the full
unconstrained `48^7` domain, is the right heuristic scale.

## Banked Lemmas / Corrections

### L-CYCLE75-MITM-SUBFIELD-NORM-SHARD-CENSUS

Split the seven slots as:

```text
L = {1,2,3},   R = {4,5,6,7}.
```

Use:

- packed field product as the equality key;
- the color sum constraint as the `P_0` domain filter;
- a multiplicative subfield norm, preferably `N_{F/F_{17^8}}`, as a lossless
  shard because it is a function of the product.

This yields a bounded-memory exact census architecture for:

```text
m_max(beta) = max_v #{T in P_0 : product(T)=v}.
```

It does not materialize all `|P_0|=52,747,567,104` tuples at once. Time is
still `Theta(|P_0|)`, so the actual pass requires compiled/sharded execution.

### W-CYCLE75-CONSTRAINED-ENERGY-IS-THE-RIGHT-SCALE

Cycle 74's `~7082` total-collision heuristic used the full unconstrained
domain:

```text
48^7.
```

For the actual constrained domain `P_0`, Cycle 75 estimates:

```text
|P_0|^2 / (17^16-1) ~= 57.2,
```

which lies below `155`. This rehabilitates the original energy gate at the
correct scale, while still keeping direct `m_max` as the target.

### W-CYCLE75-LADDER-CANNOT-FINISH

Even if the ladder passes through `k=5`, it only forces collisions to differ
in at least six of seven slots. A Singleton-style bound over alphabet size
`48` gives at best:

```text
m_max <= 48^2 = 2304,
```

not `12`. The ladder is a useful accelerator and structural diagnostic, not a
complete proof of the fiber bound.

## Local Follow-Up

Codex added:

```text
experimental/scripts/cycle75_mitm_half_rung_check.py
```

and executed the bounded left-half check:

```text
experimental/notes/m1/cycle75_mitm_half_rung_certificate.json
```

The certificate proves product-only injectivity for the exact MITM left half:

```text
slots {1,2,3}: 48^3 = 110592 tuples, 110592 distinct products.
```

The right half `{4,5,6,7}` remains unrun.

## New Active Wall

```text
V-CYCLE76-RIGHT-HALF-AND-MMAX-CENSUS
W-CYCLE74-DIRECT-MMAX-BUCKET-BOUND
```

The next exact target is either:

1. execute/certify product-only injectivity for right half `{4,5,6,7}`;
2. produce a compiled/sharded exact direct max-fiber census;
3. find an explicit 13-fold fiber in `P_0`.

