# Cycle 30 T2J4 Split-Quartic Gate Audit

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.

Harness status: HARNESS_MALFORMED_VISIBLE_TERMINAL. No clean `response.md`
was produced. The visible terminal scrape is not used as mathematics. The
readable Claude structured JSONL recovery is preserved as provenance and the
content below is audited conservatively.

Source artifacts:

- `raw/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_RAW.json`
- `raw/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_RUN_RESULT.json`
- `raw/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_CREDIT_SURFACE_RUNNER_RESULT.json`
- `local_checks/20260618_cycle30_t2_j4_split_quartic_scan.py`

## Ledger

- `q_gen = p`.
- `B = F_p`.
- `F = F_{p^2}`.
- `q_line = |F| = p^2`.
- `q_chal`: unused.
- Domain: `D = F_p`, so `n = p`.
- Restricted regime: `t = sigma = 2`, `j = n-a = r-t = 4`.
- Branch: off `R0`, `kappa = u wedge b != 0`, source-valid separated
  quadratic `E=X^2+cX+d` nonzero on `F_p`, with `c_b != 0` in the source
  wall.

This is a residue-line / bad-slope incidence calculation only. It is not a
list-decoding, CA, MCA, line-decoding, curve-MCA, protocol, `q_gen`, or SNARK
claim.

## Banked Reduction

Cycle 30 identifies the source-correct split-quartic gate in co-support
coordinates. For a distinct 4-subset `T subset F_p`, write

```text
L_T = X^4 - tau_1 X^3 + tau_2 X^2 - tau_3 X + tau_4,
tau=e(T).
```

The bad-slope condition is equivalent to collinearity

```text
[I_S]_E = z b
```

in the two-dimensional `F`-space `A=F[X]/E`. Multiplying by the unit
`lambda=[L_T]_E` gives the single `F`-valued quadric

```text
Phi(tau) = iota wedge_F mu = 0,
iota = u*lambda - ell*[Q_S]_E,
mu = b*lambda.
```

Equivalently,

```text
Phi(tau)
  = kappa * N_{A/F}(lambda)
    - (ell*[Q_S]_E) wedge_F (b*lambda).
```

Here `Q_S` is independent of `tau_4` and `lambda=lambda' + tau_4`, so

```text
Phi = kappa*tau_4^2
    + tau_4*(kappa*Tr_{A/F}(lambda') - (ell[Q_S]_E) wedge_F b)
    + (kappa*N_{A/F}(lambda') - (ell[Q_S]_E) wedge_F (b lambda')).
```

Thus the `j=4` split gate is a one-`F`-quadric / two-`B`-quadric incidence
problem on the elementary-symmetric image of distinct 4-subsets.

This banks the reduction only. It does not bank a proof of `O(p)` or a
counterpacket.

## Experimental Local Check

Codex added and ran
`local_checks/20260618_cycle30_t2_j4_split_quartic_scan.py`, a direct finite
scan using the existing Cycle 11 finite-field utilities. It counts distinct
slopes by direct division and `line_scalar` tests over `D=F_p`.

Summaries:

```text
p=7   trials=20  avg_C2=0.55   avg_C2/p=0.079  avg_C2/p^2=0.0112
p=11  trials=20  avg_C2=2.40   avg_C2/p=0.218  avg_C2/p^2=0.0198
p=13  trials=16  avg_C2=4.31   avg_C2/p=0.332  avg_C2/p^2=0.0255
p=17  trials=10  avg_C2=8.20   avg_C2/p=0.482  avg_C2/p^2=0.0284
p=19  trials=8   avg_C2=11.75  avg_C2/p=0.618  avg_C2/p^2=0.0325
p=23  trials=6   avg_C2=17.00  avg_C2/p=0.739  avg_C2/p^2=0.0321
p=29  trials=4   avg_C2=31.25  avg_C2/p=1.078  avg_C2/p^2=0.0372
```

The evidence does not support the recovered answer's heuristic expectation of
a generic positive-density `Theta(q_line)` split locus, at least not in these
random small cases. It instead suggests a hidden `O(p)`-scale collapse may be
present. This remains EXPERIMENTAL only.

## Exact New Wall

The live wall is sharpened to:

```text
W-F1-AA-RES-T2J4-SPLIT-QUADRIC-COLLAPSE
```

Decide whether the explicit two-quadric split gate above has a hidden
structure forcing only `O(p)` totally split distinct quartics, or whether a
source-valid growing-prime family can still realize `Theta(q_line)` slopes.

Concrete possibilities:

1. Prove a rational-root/factorization/collapse theorem for the universal
   quartic over the quadric surface `Phi=0`, giving `O(p)`.
2. Prove geometrically irreducible dimension-2 plus positive-density splitting
   for an explicit source-valid family, giving a counterpacket seed.
3. Derive the exact additional invariant measured by the finite scan that
   suppresses the naive `p^2/24` heuristic.

The finite scan currently makes option 1 look more plausible, but this is not
a proof.

## Dependencies

- Cycle 11/12: source conventions, quotient form, `line_scalar`, and
  co-support elementary-symmetric parametrization.
- Cycle 24: source-valid nonvanishing of the locator norm.
- Cycle 28: restricted `t=2,j=3` determinant proof and `Q_4` nonvanishing.
- Cycle 29: square system / top-symbol transition for `t=2,j=4`.

## Rejected Overclaims

- Not a proof of `C2=O(p)` for `j=4`.
- Not a `Theta(q_line)` counterpacket.
- Not a proof that `Phi=0` has geometrically irreducible dimension 2.
- Not a proof of `S_4` splitting density, nor a proof of rational-root
  collapse.
- No corrected-reserve theorem, full MCA bound, `q_gen` consequence,
  protocol/list/CA/MCA/line-decoding/curve-MCA/SNARK statement, or prize solve.

## Next Prompt

Attack `W-F1-AA-RES-T2J4-SPLIT-QUADRIC-COLLAPSE` directly. The next worker
should reconcile Cycle 30's two-quadric geometry with the finite scan's
`O(p)`-leaning counts, preferably by finding the hidden factorization or by
constructing a source-valid family that defeats the small random scans.
