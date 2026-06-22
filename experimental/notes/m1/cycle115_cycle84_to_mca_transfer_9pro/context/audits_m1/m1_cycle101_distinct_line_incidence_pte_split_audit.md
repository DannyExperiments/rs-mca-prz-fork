# Cycle 101 Distinct Line Incidence / PTE Split Audit

## Verdict

**BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL.**

Cycle101 does **not** prove the distinct-root bound

```text
|Theta_U| <= n^{O(1)}
```

and does **not** produce a counterpacket. It banks a sharper formulation of the
same wall and cuts the tempting min-distance-only route.

Important artifact caveat: `response.md` ends mid-sentence in section 6 after
`Ben-Sasson-Kopparty-Radhak`. The raw stream has normal `end_turn` status, but
the mathematical answer is visibly truncated. Do not treat the unfinished BKR
counterpacket discussion as complete evidence.

## Bankable Content

Cycle101 rewrites the active external-root target in DFT/indicator form. For
`H = mu_n <= F_p^*`, a complement witness `S' subset H` with indicator
`c:H->{0,1}` satisfies:

```text
p_j(S') = sum_{x in H} c(x) x^j = chat(j).
```

Thus:

```text
theta active
<=> exists c in {0,1}^H with chat(0)=m
    and chat(j)=theta^j-P_j for j=1,...,sigma+1.
```

This preserves the **distinct support** target:

```text
|Theta_U| = #{theta notin H : such an indicator exists},
```

and avoids reverting to the weighted count:

```text
N = sum_theta F(theta).
```

Cycle101 also records the reserve threshold:

```text
main <= 2^n / p^sigma = 2^(n - sigma log_2 p).
```

Therefore `main <= 1` once:

```text
sigma >= n / log_2 p.
```

In the corrected reserve range `sigma >= C n/log n`, the hard work is not the
first moment. It is the error/concentration term: whether a specific aperiodic
prefix can force many distinct external geometric windows to match spectra of
weight-`m` subgroup indicators.

## Route Cut

Cycle101 banks the pairwise witness-distance observation and, more importantly,
its insufficiency:

```text
theta != theta' active
=> |S'_theta triangle S'_theta'| >= 2sigma+2.
```

But binary constant-weight codes with distance `~2n/log n` can still be
superpolynomial. Therefore distance/packing alone cannot prove `L2`. The proof
must use the fact that the witnesses lie on the one-parameter reciprocal
affine line:

```text
ell = { ((-1)^i(W_i - theta W_{i-1}))_{i=1}^{sigma+1} : theta in F_p }.
```

## Exact New Wall

The next live wall is:

```text
L-CYCLE102-PADE-UNCERTAINTY-LINE-INCIDENCE
```

Equivalent forms:

```text
|ell cap E_m|_distinct <= n^{O(1)}
```

where:

```text
E_m = { ((-1)^i e_i(S'))_{i=1}^{sigma+1} :
        S' subset H, |S'|=m }.
```

Two precise attack lanes:

1. **Padé / Berlekamp-Massey lane.** For the window
   `(theta^j-P_j)_{j=1}^{sigma+1}`, construct the minimal recurrence
   denominator `Q_theta`. Active `theta` should force the recurrence to extend
   to a divisor of `X^n-1`. Prove that the rational family `Q_theta` can meet
   divisors of `X^n-1` for only `n^{O(1)}` external parameters, or produce a
   source-valid family where this divisibility condition is degenerate.

2. **Uncertainty lane.** Prove a quantitative finite-field uncertainty
   statement: a weight-`m` `0/1` indicator on `mu_n` cannot have its first
   `sigma+1` Fourier coefficients agree with many distinct external geometric
   windows, unless the prefix is quotient-periodic and already charged.

## Local Verification

Codex added and ran:

```text
experimental/scripts/cycle101_dft_line_incidence_check.py
```

The checker constructs small finite-field cases with active external roots and
verifies:

```text
p_j(S') = theta^j - P_j             for j=1,...,sigma+1
theta = p_1(S') + P_1
```

It also checks the pairwise distance lower bound whenever a case has multiple
distinct active roots.

Run result:

```text
cycle101 dft-line incidence check
cases_checked: 20
total_active_hits: 21
max_distinct_theta: 1
cases_with_multiple_theta: 0
PASS
```

This is a finite sanity check only. It verifies the algebraic normal form in
toy cases; it does not prove the polynomial incidence bound.

## What Is Not Proved

- No proof of `|Theta_U| <= n^{O(1)}`.
- No proof of the Padé divisibility/transversality bound.
- No proof of a quantitative finite-field uncertainty theorem.
- No valid aperiodic counterpacket.
- No official prize theorem.
- The section 6 BKR-style counterpacket discussion is incomplete due to
  response truncation.

## Next Exact Prompt

Attack the Padé/uncertainty wall directly:

```text
L-CYCLE102-PADE-UNCERTAINTY-LINE-INCIDENCE
```

The prompt should ask for one of:

```text
PROOF: |ell cap E_m|_distinct <= n^{O(1)}
COUNTERPACKET: aperiodic prefix P with superpolynomial distinct external theta
EXACT_NEW_WALL: the smallest missing Padé divisibility or uncertainty lemma
```

It must explicitly preserve the distinction between distinct support
`|Theta_U|` and weighted count `N=sum_theta F(theta)`.
