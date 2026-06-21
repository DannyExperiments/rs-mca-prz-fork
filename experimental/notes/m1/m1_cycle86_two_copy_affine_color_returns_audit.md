# Cycle 86 Two-Copy Affine-Color Returns Audit

Date: 2026-06-21

Raw returns:

`experimental/notes/m1/cycle86_two_copy_affine_color_returns_raw/`

Dispatch receipt:

`experimental/notes/m1/cycle86_two_copy_affine_color_dispatch_receipt.md`

Context zip SHA-256:

`737f995c2604d9f6ee3d62022c7f91a085cfb2337de91c37651d32a3c6e00a7e`

## Verdict

**Status: BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT.**

Cycle86 is significant. It does not give a public replay-ready prize
counterpacket yet, but it changes the active route from "one-copy Cycle85 is a
large finite obstruction" to "there is a plausible official-scale two-copy
counterpacket, provided one explicit separator/domain certificate is
materialized."

The honest current status is:

```text
not official proof yet
not merely numerology
route-changing theorem candidate
next step is an explicit projective-separator checker/certificate
```

The most important correction is that the additive composition formula should
not be banked. The surviving composition is product/reciprocal-product after a
common affine normalization.

## Raw Preservation

The following visible ChatGPT page extracts were saved and checksummed:

- `ROLE_01_TWO_COPY_THEOREM_FORMALIZER_PAGE_RAW.md`
- `ROLE_02_CONTINUE_GENERIC_TRANSLATION_MATERIALIZER_PAGE_RAW.md`
- `ROLE_03_CERTIFICATE_ARCHITECT_PAGE_RAW.md`
- `ROLE_04_COUNTERPACKET_HUNTER_PAGE_RAW.md`
- `ROLE_05_CONTINUE_TENSOR_ROUTE_REDTEAM_PAGE_RAW.md`
- `ROLE_06_CONTINUE_SYNDROME_LINE_BUILDER_PAGE_RAW.md`
- `ROLE_07_FRONTIER_LEDGER_CHECKER_PAGE_RAW.md`
- `ROLE_08_RATE_DOMAIN_NORMALIZATION_AUDITOR_PAGE_RAW.md`
- `ROLE_09_CONTINUE_REFEREE_PROMOTE_OR_CUT_PAGE_RAW.md`
- `SHA256SUMS.txt`

`shasum -a 256 -c SHA256SUMS.txt` passed for the nine raw page extracts.

No separate generated/downloaded files were visible in the captured page text.

Important caveat: Role 09 is not a valid Cycle86 return. The extracted
conversation at `https://chatgpt.com/c/6a374508-40c8-83ec-98cd-8352c9268560`
is a stale Cycle85 Role05 adjudication lane. It is useful background for
one-copy transfer status, but it should not be counted as a Cycle86 two-copy
worker.

## Bankable Consensus

### One-copy transfer is real but not enough

Roles 02, 06, and the stale Role 09 agree on the corrected one-copy transfer:

```text
L-CYCLE85-EXACT-ROLE05-PACKET-SLOPE-OCCUPANCY
M_C0(6) >= Occ(beta) = 52,747,567,092
```

The slope coordinate is reciprocal/affine normalized, not literally the raw
Cycle84 product coordinate. This is a finite-model lower packet over the
Role05 field model, not by itself an official prize-frontier counterpacket.

### Direct tensoring is the wrong route

Role 05 cuts the naive tensor/direct-sum approach. A direct block product has
several independent color coordinates and becomes a higher-dimensional or
multi-line object, not a single `t=1` RS MCA line. Any official-scale
amplification must fuse the two copies into one RS-compatible affine/syndrome
line.

### Additive two-copy composition is false or unproved

Roles 01, 04, and 08 all push toward a two-copy construction, but Role 04
correctly red-teams the displayed additive identity. For block-separable
locators, restriction/locator data compose multiplicatively. The bankable form
is reciprocal product:

```text
slope approximately 1 / (rho_beta(T1) * P_T2(y))
```

up to a common affine normalization.

### Official-scale numerics are strong

Let

```text
P = 52,747,567,104
N = Occ(beta) = 52,747,567,092
q_line = 17^48
T_line = floor(q_line / 2^128)
       = 338,617,018,271,848,945,628
```

Then both main two-copy counts clear the finite target:

```text
P*N = 2,782,305,834,758,012,141,568 > T_line
N^2 = 2,782,305,834,125,041,336,464 > T_line
```

The margin is about a factor of 8.2. This is why Cycle86 matters: one-copy
Cycle85 was too small or normalization-inactive for the official field target;
two-copy amplification is numerically large enough.

### The remaining gap is geometric/certificational, not arithmetic

Role 07 states the correct promotion condition. To bank an official
counterpacket, the construction must be certified as:

```text
one GRS/RS code
one affine t=1 syndrome line
one explicit domain
one explicit separator parameter
distinct enough final slopes
transverse incidences
```

The currently missing object is an explicit coefficient-level separator and
domain certificate.

## Candidate Theorems

### Main candidate

```text
L-CYCLE86-TWO-BLOCK-GENERIC-TRANSLATE-RECIPROCAL-PRODUCT-COMPOSITION
```

Role 01 proposes a construction over `F_17^48` with parameters

```text
(n,k,sigma,j) = (560,280,6,274)
```

using two translated blocks plus 48 fixed padding points. It claims a generic
choice of `alpha` gives the product/reciprocal-product separator and a packet
of size `P*N` or `N^2`, depending on whether the unreduced or occupied first
coordinate is counted.

This is route-changing if correct, but it is not yet replay-ready because no
explicit good `alpha`, domain digest, or compact checker has been emitted.

### Cleaner candidate

```text
L-CYCLE86-TWO-BLOCK-SHORTENED-GENERIC-TRANSLATE-464
```

Role 08 proposes removing 24 universally unused coordinates from each block,
giving the smaller official-rate package

```text
(n,k,sigma,j) = (464,232,6,226)
```

This looks cleaner than the 560-point padded version if the shortening and
shared-six-jet claims survive verification. It should be the preferred target
for the next exact checker unless the proof algebra fails.

### Separator-checker formulation

Role 03 gives the most actionable checker wall:

```text
W-CYCLE86-EXPLICIT-PROJECTIVE-SEPARATOR-Y
V-CYCLE86-U-PROJECTIVE-MMAX8-CENSUS
```

For `y` in an extension over the Cycle84 base field, define the projective
multiplicity

```text
mu_proj(y) =
  max_kappa #{ T in P0 : [P_T(y)] = kappa in L^x / F0^x }.
```

If

```text
mu_proj(y) <= 8,
```

then the two-copy construction clears the official `2^-128` target. This is
the narrowest next task: materialize a concrete `y`, run the multiplicity
census, and splice it into the frontier ledger.

## Conflicts And Resolutions

### Conflict: Is this already an official counterpacket?

Roles 01, 02, 04, and 08 lean toward "yes, existentially." Role 03 and Role 07
say "not until the explicit separator/domain certificate is emitted." The audit
follows Role 03 and Role 07. The theorem candidate is strong, but promotion
requires a concrete replay artifact.

### Conflict: Does stale Role 09 cut Cycle86?

No. Role 09 is a Cycle85 one-copy adjudication. It correctly says the one-copy
packet is not official-frontier-moving by itself. It does not refute the
Cycle86 two-copy construction because it did not receive the Cycle86 packet.

### Conflict: Can we use additive colors?

No. Cut the additive identity from the banked route. The surviving mechanism is
product/reciprocal product.

### Conflict: Can direct tensor amplification be used?

No. Cut naive tensor/direct-sum amplification for a single `t=1` MCA line.
Two-copy progress must pass through one-line affine/syndrome fusion.

## Actionable Next Steps

1. Verify the Role 08 shortened package algebraically:

```text
(n,k,sigma,j) = (464,232,6,226)
```

Check that deleting the unused coordinates preserves the needed jet condition,
the one-line GRS interpretation, and transversality.

2. Implement the Role 03 separator checker:

```text
V-CYCLE86-U-PROJECTIVE-MMAX8-CENSUS
```

Start with the proposed cubic extension candidate, then search lexicographic
`y` if needed.

3. Emit a compact certificate with:

```text
base field model
extension field model
chosen y or alpha
domain digest
projective multiplicity maximum
packet count lower bound
T_line comparison
transversality check
normalization check
```

4. Only after that, add a frontier-ledger row:

```text
C-CYCLE86-OFFICIAL-TWO-COPY-MCA-FAIL-ROW
```

5. If the projective separator fails for all small structured candidates,
return to the existential root-count proof and force it into a constructive
search certificate.

## Significance

Cycle84 was the best finite-model computation so far: it closed
`m_max(beta)=2` for the seven-slot product model.

Cycle85 made that result mathematically honest in one-copy RS/MCA coordinates,
but it did not move the official frontier by itself.

Cycle86 is the first round that plausibly turns the Cycle84/Cycle85 finite
obstruction into an official-scale counterpacket by amplifying it to
`F_17^48` while preserving the single-line `t=1` MCA structure.

That is a major route upgrade. It should be reported to PRZ as a candidate
official-scale route with one missing explicit separator certificate, not as a
solved prize counterexample.

## Next Exact Lemma

```text
L-CYCLE86-EXPLICIT-TWO-COPY-SEPARATOR-CERTIFICATE
```

Prove, with a replayable checker, that a concrete separator `y` for the
two-copy construction has projective multiplicity at most 8 and that the
resulting supports form one transverse affine syndrome line of a single
official-rate GRS code.

If proved, this becomes an official finite MCA fail row. If killed, the route
falls back to searching for a different separator or to abandoning two-copy
affine-color fusion.
