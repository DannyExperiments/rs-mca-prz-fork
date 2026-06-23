# Standalone Sampler-Map Certificate

## Theorem

Let `K = F_17^32`, `Q=|K|`, and let `B_116 subset K` be the exact certified Cycle116 bad-slope subset of size `N=52,747,567,092` at support-wise agreement 262 for `RS[K,H,256]`, `|H|=512`. Let an official sampler receipt define a finite uniform challenge space `Omega`, an exact line-parameter map `mu`, and an ordered event-retention pipeline.

1. If `Omega=K`, `mu=id_K`, and the pipeline counts all challenge occurrences without filtering, then the retained certified probability is `N/Q > 2^-128`.
2. If `mu:Omega->K` is balanced, meaning every fiber has size `|Omega|/Q`, and the pipeline has no loss, then the retained certified probability is exactly `N/Q > 2^-128`.
3. If `E/K` is proper, `Omega=E`, `mu=id_E`, and the original K-valued Cycle116 line is scalar-extended to `RS[E,H,256]`, then its entire support-wise bad set is the same subset of K as over K. Hence its total probability is at most `Q/|E| <= 1/Q < 2^-128`.
4. If an exact authenticated pipeline starts from an above-threshold pullback of the Cycle116-certified packet and ends with `R` satisfying `2^128 R <= |Omega|`, then this certificate route is at or below threshold. This does not upper-bound uncatalogued bad events.
5. Without an authenticated map and pullback/filter rule, no official probability follows from `q_chal`: for the nonempty proper set `B_116`, maps constant into `B_116`, constant into its complement, and balanced onto K yield probabilities 1, 0, and `N/Q`, respectively.

## Proof

For (1), the identity preimage of `B_116` is `B_116`, so its cardinality is N. The packet arithmetic gives `2^128 N > Q`.

For (2),

```text
|mu^-1(B_116)| = sum_{z in B_116} |mu^-1(z)|
                = N |Omega|/Q.
```

Dividing by `|Omega|` gives N/Q exactly. More generally, equal fibers may be replaced by the measure condition `mu_* P_Omega = Uniform(K)`.

For (3), choose a K-basis `1=e_1,e_2,...,e_r` of E and coordinate projections `pi_i:E->K`. If `z notin K` and an E-polynomial P of degree <256 explains `f+zg` on a support S, choose a nonzero non-first coordinate z_i. Then `z_i^{-1} pi_i(P)` explains g on S, and `pi_1(P)-z_1 z_i^{-1}pi_i(P)` explains f on S. Thus z is contained, not bad. For `z in K`, coefficient projection shows that E-explainability and simultaneous containment are equivalent to K-explainability and containment. Therefore `Bad_E(f,g)=Bad_K(f,g) subset K`. For a proper finite extension, `|E|>=Q^2`, so total density is at most `Q/Q^2=1/Q<2^-128` because `Q>2^128`.

For (4), the retained probability mass contributed by the certified packet is exactly `R/|Omega|`; the displayed integer inequality is equivalent to `R/|Omega| <= 2^-128`. No conclusion about additional bad outcomes follows without a full-event upper bound.

For (5), `0<N<Q`. Pick `b in B_116` and `c in K\B_116`. The constant maps `mu_b` and `mu_c` produce pullback probabilities 1 and 0 under every challenge distribution. A balanced map produces N/Q. Hence neither `q_chal` nor a challenge-space name determines the official event probability. Authentication is also necessary: a self-written receipt cannot establish what an external authority adopted.

## Scope

This is a finite source/model/checker theorem. It does not establish an official Proximity Prize claim, ordinary list decoding, protocol soundness, or an asymptotic theorem.
