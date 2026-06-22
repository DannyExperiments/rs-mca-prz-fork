# Cycle 97 Fixed-Prime Two-Support Audit

## Verdict

**BANKABLE_LEMMA / AUDIT_CORRECTION / EXACT_NEW_WALL.**

Cycle97 gives a useful bandwidth-`1` decomposition, but the literal raw
response omits one branch: repeated roots inside `H`. Codex local checking found
this immediately. After correction, the bankable content is:

```text
degree-(s+1) arbitrary-word lists decompose into:
  Type A: all s+1 roots in H;
  Type B_ext: s roots in H plus one external root theta notin H;
  Type B_H: s roots in H plus one extra root theta in H
            (including repeated-root cases theta in S).
```

The `theta in H` branch is only an `n`-sized union of bandwidth-`0` prefix
slices and is not the main wall. The main new object remains the active
external-root count.

## Raw Artifacts

Raw Fable artifacts were preserved under:

```text
experimental/notes/m1/cycle97_fixed_prime_two_support_raw/
```

Run metadata:

```text
run path: /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-49-07-277Z-cycle97-fixed-prime-two-support-89e17f9c
model: claude-opus-4-8
mode: artifact_stream
status: OK
elapsed: 883545 ms
cost: 4.588053500000001 USD
capture warning: none
stop reason: end_turn
```

Checksums were generated in:

```text
experimental/notes/m1/cycle97_fixed_prime_two_support_raw/SHA256SUMS.txt
```

## Corrected Bankable Lemma

```text
L-CYCLE97-BANDWIDTH1-ROOT-CONFIGURATION-DECOMPOSITION
```

Let `U` be monic of degree `s+1`, and let the top `sigma+1` coefficients define
the elementary-symmetric prefix target `c`. A degree-`<k` codeword `P` agreeing
with `U` on at least `s` points corresponds to:

```text
V = U - P,
```

where `V` is monic of degree `s+1`, has prescribed prefix `c`, and has at least
`s` roots in `H`.

The root configuration of `V` splits as:

1. **Type A:** `V=L_R`, `R subset H`, `|R|=s+1`, and
   `Phi_{sigma+1}(R)=c`.
2. **Type B:** `V=(X-theta)L_S`, `S subset H`, `|S|=s`, and
   `Phi_{sigma+1}(S)=c(theta)`, where:

```text
c(theta)_j = sum_{i=0}^j (-theta)^{j-i} c_i,  c_0=1.
```

The Type B branch must allow all `theta in F_p`, not only `theta notin H`.
When `theta in H\S`, the polynomial also appears in Type A. When `theta in S`,
`V` has a repeated root inside `H`; this is the omitted branch in the raw
Cycle97 answer.

## Audit Correction

The raw answer's external-only statement:

```text
Type B = exactly s roots in H and one external root theta in F_p \\ H
```

is false without an additional squarefreeness/no-repeated-root hypothesis.

Codex found a toy example over `F_17` where `V` has four distinct roots in `H`
and a repeated root at one of them. This is not Type A and not external Type B.
The corrected Type B with `theta in F_p` covers it.

This correction does not destroy the route:

- `theta in H` contributes at most `n` fixed-`theta` prefix slices;
- after the bandwidth-`0` local limit, that branch remains polynomial;
- the continuum branch `theta notin H` is still the real fixed-prime wall.

## Codex Local Follow-Up

Codex added and ran:

```text
experimental/scripts/cycle97_bandwidth1_decomposition_check.py
```

The script compares direct enumeration of degree-`<k` agreement lists against
the corrected Type A / Type B decomposition and verifies:

```text
theta = c_1 - e_1(S)
Phi_{sigma+1}(S) = c(theta)
```

Run result:

```text
cases_checked: 40
total_direct_list: 11
total_active_theta: 11
total_external_theta: 7
PASS
```

## Claim Level

Bank as:

```text
corrected bandwidth-1 decomposition
audit correction to raw external-only branch
not a proof of S1-B1
not a counterpacket
not a finite prize certificate
```

## Exact New Wall

```text
L-CYCLE98-B1-ACTIVE-EXTERNAL-ROOT-INCIDENCE
```

After charging Type A and `theta in H` through bandwidth-`0` prefix local
limits, prove or kill:

```text
#{ theta in F_p \\ H :
   Phi_{sigma+1}^{-1}(c(theta)) is nonempty and aperiodic }
   <= n^{O(1)}.
```

Equivalently, bound the intersection of the explicit degree-`sigma+1`
external-root curve `theta -> c(theta)` with the aperiodic prefix image of
`s`-subsets of `H`.

