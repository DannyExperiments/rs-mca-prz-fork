# Paper A Lean Formalization

This Lean package contains a formalization of the quotient-locator core of
`tex/RS_disproof_v3.tex` (Paper A).  The main file is
`RS_disproof_v3.lean`.

The package was edited by [Aristotle](https://aristotle.harmonic.fun).

## Formalized

- Restricted sumsets and the quotient locator polynomial.
- The locator decomposition
  `locator A a = X^(k+a) + (-sum A) X^k + R`, with `degree R < k`.
- The support-wise line-MCA predicates `RSagrees`, `badAt`, `badSet`, and
  `epsMca`.
- The no-low-degree explanation step for `x^k`.
- Monotonicity of `epsMca` in the radius.
- The quotient-locator lower bound
  `epsMca >= |ell^wedge Q| / |F|` under the smooth-quotient fiber hypothesis.
- The error-one consequence from a restricted-sumset coverage hypothesis.
- Full-domain specializations for `a = 1`.
- A density-to-MCA reduction for the cyclotomic-sieve branch, stated with the
  sieve density conclusion as an explicit hypothesis.

## Still Missing

This is not yet a complete formalization of Paper A.

- The Dias da Silva--Hamidoune coverage theorem is not formalized; coverage is
  passed as an explicit hypothesis.
- The Fermat digit lemma is not formalized.
- The cyclotomic sieve theorem and its Siegel--Walfisz input are not
  formalized; only the reduction from the resulting density statement to MCA is
  formalized.
- The BabyBear, KoalaBear, and `3*2^30+1` interval arithmetic is not
  formalized.
- The extension-field tower section is not formalized.
- The Appendix verification records V1--V5 are not formalized.
- The list lower-bound formalization currently gives the pigeonhole/agreement
  skeleton; it still needs the distinct-codeword injection needed for the full
  Paper A list-size theorem.
