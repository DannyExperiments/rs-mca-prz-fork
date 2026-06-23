# V-CYCLE120-OFFICIAL-SOURCE-GATE-AUDIT

Date: 2026-06-24

## Executive Verdict

The public Proximity Prize page makes the Cycle119 strict-263 row look
substantially closer to the official grand MCA challenge than the earlier
`SOURCE_CONTRACT_MISSING_NO_CLAIM` wording suggested.

Current status:

```text
FINITE_SOURCE_THEOREM: banked candidate
OFFICIAL_ROW_GATE: tentatively green from public site
OFFICIAL_PREDICATE_GATE: strongly supported by local ABF-linked sources, pending direct ABF PDF text
OFFICIAL_SAMPLER_GATE: strongly supported by local ABF-linked sources and screenshots, pending direct ABF PDF text
OFFICIAL_FILTER_GATE: tentatively green for the grand MCA challenge, pending direct ABF PDF text
FORMAL_PRIZE_SUBMISSION: not yet; needs human-edited public PDF and peer review
```

This is not a claim that the prize is solved. It is a claim that the
remaining work has narrowed to a source-definition/admissibility audit rather
than a new finite-algebra lemma.

## Sources Checked

Primary public prize site snapshot:

```text
https://proximityprize.org/
local snapshot:
experimental/notes/m1/cycle119_official_source_audit/proximityprize_20260624.html
sha256:
82618a3f0e407bef82e7e591cc316c89713c7fa2f48cdbc35bc2e6f589b7e5de
```

The public page says:

```text
The Proximity Prize offers $1,000,000 in awards to researchers who resolve
the grand challenges below.

The accompanying paper and problem statements are a preliminary version --
details may still change.

The prize targets two grand challenges formalised in the companion paper.

Grand MCA challenge:
C := RS[F, L, k] over some smooth evaluation domain L subset F.
rate k/|L| is one of {1/2, 1/4, 1/8, 1/16}.
For eps* = 2^-128, determine largest delta*_C such that
epsilon_mca(C, delta*_C) <= eps*.
```

Local source slices already used by previous checkers:

```text
tex/cs25_cap_v4.tex
sha256:
0903c5b104ef3ecbc939d7cad8c33608dfddc946d795d696452befad9636909a

tex/snarks_v4.tex
sha256:
3c5efb6c8a1a2ff47adf226d1cae5f4f53cc52978f46cc5590ff6488ba75f131
```

`tex/cs25_cap_v4.tex` explicitly says its support-wise MCA definition is
ABF26 Definition 4.3 up to notation, and defines:

```text
epsilon_mca(C, delta)
  = max_{f1,f2 in F^n} Pr_{gamma <- F}[
      exists S subset D, |S| >= (1-delta)n,
      dist_S(f1 + gamma f2, C) = 0,
      and dist_S((f1,f2), C^{==2}) > 0
    ].
```

This matches the Cycle119 support-wise same-support noncontainment predicate.

IACR/ePrint retrieval status:

```text
https://eprint.iacr.org/2026/680.pdf
  shell fetch: 403 Forbidden / bot verification

https://ia.cr/2026/680.pdf
  shell fetch: 404 Not Found

https://ia.cr/2026/680
  shell fetch: redirects to eprint bot verification
```

Therefore this audit has not yet directly extracted ABF26 Definition 4.3 from
the PDF. It uses the public prize site as primary evidence for the challenge
row/envelope and local ABF-linked source slices as strong secondary evidence
for the exact MCA predicate and sampler.

## Gate Table

### Gate 1: Row Form

Official public wording:

```text
C := RS[F, L, k] over some smooth evaluation domain L subset F.
```

Cycle119 row:

```text
K = F_{17^32}
H = <theta> subset K
|H| = 512
C = RS[K,H,256]
rate = 256/512 = 1/2
```

Verdict:

```text
TENTATIVE_PASS
```

The public text does not restrict to prime fields. It says finite field `F`.
The extension field row is syntactically an `RS[F,L,k]` row.

### Gate 2: Smooth Domain

Cycle119 domain:

```text
H = <theta>
ord(theta) = 512 = 2^9
```

Verdict:

```text
TENTATIVE_PASS
```

A multiplicative subgroup of power-of-two order is the standard FFT-smooth
case. A direct ABF PDF quote defining "smooth evaluation domain" is still
needed for final public language.

### Gate 3: Rate Envelope

Official public wording permits:

```text
rate in {1/2, 1/4, 1/8, 1/16}
```

Cycle119 row has:

```text
rate = 1/2
```

Verdict:

```text
PASS_FROM_PRIMARY_SITE
```

### Gate 4: Predicate

Cycle119 proves support-wise same-support noncontainment:

```text
exists support S where f + gamma g is code-explained,
but f and g are not simultaneously code-explained on that same S.
```

Local ABF-linked source `cs25_cap_v4.tex` identifies this with ABF26
Definition 4.3 up to notation.

Verdict:

```text
STRONG_TENTATIVE_PASS_PENDING_DIRECT_ABF_DEF_4_3
```

This is the most important clause to verify directly in the paper.

### Gate 5: Gamma / Line Sampler

Local ABF-linked source defines:

```text
Pr_{gamma <- F}
```

The judge tweet screenshot of Construction 6.2 also shows:

```text
Combination randomness: gamma <- F.
```

Verdict:

```text
STRONG_TENTATIVE_PASS_PENDING_DIRECT_ABF_DEF_4_3
```

No independent `q_chal` appears in the public grand MCA page.

### Gate 6: Extra Filters

The public grand MCA challenge states the inequality only through
`epsilon_mca(C, delta)`. It does not mention endpoint deletion, quotienting,
periodicity, duplicate-slope charge, or a retained-event filter.

Verdict:

```text
TENTATIVE_PASS_FOR_GRAND_MCA
```

Protocol-specific filters may exist in the toy protocol, but the prize
challenge as publicly stated is the grand MCA quantity, not a specific
protocol transcript experiment.

### Gate 7: Field Size Envelope

The public site only says:

```text
assuming |F| is sufficiently large so that such a delta*_C exists.
```

Local ABF-linked source states the challenge envelope as:

```text
k <= 2^40
|F| < 2^256
```

Cycle119 has:

```text
k = 256
|F| = 17^32 ~= 2^130.8
```

Verdict:

```text
TENTATIVE_PASS_PENDING_DIRECT_ABF_TEXT
```

The row is comfortably inside the local-source envelope.

## Impact on Cycle119

If Gates 1-7 all pass under the direct ABF/proximity-prize source text, then
Cycle119 gives:

```text
LD_sw(RS[F_17^32,H,256],263) >= 52,747,567,092
```

and therefore, under ABF Definition 4.3:

```text
epsilon_mca(C,125/256)
  >= 52,747,567,092 / 17^32
  > 2^-128.
```

The strict-radius issue is already resolved:

```text
agreement = 263
distance <= 512 - 263 = 249
249 < 250 = (125/256)*512.
```

This would be a counterexample candidate to any claim that this row has
`epsilon_mca(C,125/256) <= 2^-128`.

## Why PRZ Is Useful But Not Uniquely Capable

PRZ is not the only person who can answer the four gates. The public site and
paper can answer most of them.

PRZ is still useful because:

1. he can notice whether the community intends hidden restrictions not obvious
   in the public page;
2. he can verify that the notation in the paper really matches our
   support-wise predicate;
3. he can sanity-check whether an extension field `F_{17^32}` is socially and
   mathematically accepted as a challenge field;
4. he can help turn the note into field-standard human prose.

But waiting for PRZ is not mathematically necessary. The next self-contained
work item is direct extraction of ABF26 Definition 4.3 and the "smooth domain"
definition.

## Immediate Next Steps

1. Obtain the ABF26 PDF despite ePrint bot verification, preferably through a
   browser/manual download or an alternate author-hosted mirror.
2. Extract exact statements for:
   - Definition 4.3 `epsilon_mca`;
   - "smooth evaluation domain";
   - any field-size or degree envelope;
   - any challenge/sampler semantics.
3. Patch `THEOREM_NOTE.md` and the cold packet with exact ABF citations.
4. If all gates are green, draft a short public preprint-quality note with:
   - theorem statement;
   - two-ended lemma;
   - Cycle84 instantiation;
   - checker receipt;
   - relation to the Proximity Prize;
   - non-claims.

Do not upload a raw packet as an ePrint/arXiv timestamp. The prize page says
the first public version is the formal timestamp, but a major revision resets
the relevant timestamp. Priority is helped by publishing quickly, but not by
publishing something sloppy enough to require a major rewrite.

