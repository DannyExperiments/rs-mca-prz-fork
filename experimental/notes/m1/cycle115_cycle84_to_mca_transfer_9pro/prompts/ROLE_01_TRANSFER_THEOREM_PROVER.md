# Role 01: Transfer Theorem Prover

Use the common prompt. No Internet.

Your role is to prove the strongest source-valid transfer theorem you can from the Cycle84 finite certificate to a Reed--Solomon MCA / list / line-decoding statement.

Start from the candidate chain:

```text
Cycle84 finite color-filtered product spectrum
  -> Cycle85 one-copy finite slope occupancy over F_17^16
  -> Cycle88/89 two-copy or extension-row bridge over F_17^48
  -> support-wise MCA or line-decoding numerator over an RS/GRS code
```

Do not assume this chain is valid. Prove every arrow you use from the supplied definitions. If a full prize-facing transfer is impossible, prove the maximal finite/paper-facing theorem that is actually supported.

You should try to produce one of these:

1. A `PROOF` theorem with exact RS/GRS parameters `(F,D,n,k,delta,q_gen,q_code,q_line,q_chal)` and an exact bad-slope or line-decoding numerator.
2. A `BANKABLE_LEMMA` that states the transfer conditionally on named missing hypotheses, with no vague phrases.
3. A `ROUTE_CUT` locating the first false or unsupported arrow.

Mandatory checks:

- Does the reciprocal-affine map from product values to slopes stay injective after all normalizations?
- Does support-wise `def:mca` in `slackMCA_v3.tex` match the finite packet's color shell and witness sets?
- Is GRS-to-RS diagonal scaling harmless for the exact error notion?
- Is the row arbitrary-domain only, or smooth multiplicative subgroup/coset as required by the prize-facing RS setting?
- Does the numerator survive quotient/periodic/contained/same-slope/endpoint/tangent/affine-color charges?

Finish by writing the exact theorem statement that PRZ could review.
