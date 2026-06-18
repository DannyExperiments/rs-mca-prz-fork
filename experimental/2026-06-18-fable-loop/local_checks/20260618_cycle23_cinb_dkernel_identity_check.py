#!/usr/bin/env python3
"""Check the Cycle 23 c-in-B D-kernel factorization in tiny fields.

This is an experimental consistency checker, not a proof. It verifies the
closed-form identity used in the Cycle 23 audit:

    D = -mu^2 * (c^2/4 - d) * kappa

for B=F_p, F=F_{p^2}, c in B, d notin B, and off R0
(`kappa = u wedge b != 0`).
"""

from __future__ import annotations

from dataclasses import dataclass


def find_nonresidue(p: int) -> int:
    squares = {(i * i) % p for i in range(p)}
    for a in range(2, p):
        if a not in squares:
            return a
    raise ValueError(f"no nonresidue found for p={p}")


@dataclass(frozen=True)
class Fp2:
    a: int
    b: int
    p: int
    nr: int

    def __post_init__(self) -> None:
        object.__setattr__(self, "a", self.a % self.p)
        object.__setattr__(self, "b", self.b % self.p)

    def __add__(self, other: "Fp2") -> "Fp2":
        return Fp2(self.a + other.a, self.b + other.b, self.p, self.nr)

    def __sub__(self, other: "Fp2") -> "Fp2":
        return Fp2(self.a - other.a, self.b - other.b, self.p, self.nr)

    def __neg__(self) -> "Fp2":
        return Fp2(-self.a, -self.b, self.p, self.nr)

    def __mul__(self, other: "Fp2") -> "Fp2":
        return Fp2(
            self.a * other.a + self.nr * self.b * other.b,
            self.a * other.b + self.b * other.a,
            self.p,
            self.nr,
        )

    def __pow__(self, exponent: int) -> "Fp2":
        out = Fp2(1, 0, self.p, self.nr)
        base = self
        e = exponent
        while e:
            if e & 1:
                out = out * base
            base = base * base
            e >>= 1
        return out

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0

    def in_base(self) -> bool:
        return self.b == 0


def fp(p: int, nr: int, a: int, b: int = 0) -> Fp2:
    return Fp2(a, b, p, nr)


def a_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def a_sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def a_scalar(s, x):
    return (s * x[0], s * x[1])


def a_mul(x, y, c, d):
    # In F[X]/(X^2+cX+d), xi^2=-c xi-d.
    return (
        x[0] * y[0] - d * x[1] * y[1],
        x[0] * y[1] + x[1] * y[0] - c * x[1] * y[1],
    )


def a_pow_xi(power: int, c, d):
    one = (fp(c.p, c.nr, 1), fp(c.p, c.nr, 0))
    xi = (fp(c.p, c.nr, 0), fp(c.p, c.nr, 1))
    out = one
    base = xi
    e = power
    while e:
        if e & 1:
            out = a_mul(out, base, c, d)
        base = a_mul(base, base, c, d)
        e >>= 1
    return out


def wedge(x, y):
    return x[0] * y[1] - x[1] * y[0]


def p_e(x, y, c, d):
    return x[0] * y[0] - c * x[0] * y[1] + d * x[1] * y[1]


def run_prime(p: int) -> dict[str, int]:
    nr = find_nonresidue(p)
    two_inv = pow(2, -1, p)
    trials = 0
    checked = 0
    for c0 in range(p):
        c = fp(p, nr, c0)
        half_c = fp(p, nr, c0 * two_inv)
        sigma = (half_c, fp(p, nr, 1))
        sigma2 = c * c * fp(p, nr, pow(4, -1, p)) - fp(p, nr, 0)
        for d0 in range(p):
            for d1 in range(1, p):
                d = fp(p, nr, d0, d1)
                actual_sigma2 = a_mul(sigma, sigma, c, d)
                expected_sigma2 = (c * c * fp(p, nr, pow(4, -1, p)) - d, fp(p, nr, 0))
                assert actual_sigma2 == expected_sigma2
                assert not expected_sigma2[0].is_zero()

                xi_p = a_pow_xi(p, c, d)
                xi = (fp(p, nr, 0), fp(p, nr, 1))
                ell = a_sub(xi_p, xi)
                mu = ell[1]
                assert ell == a_scalar(mu, sigma)
                assert not mu.is_zero()

                # Deterministic spread of u,b samples.
                samples = [
                    ((1, 0), (0, 1)),
                    ((0, 1), (1, 0)),
                    ((1, 1), (2, 3)),
                    ((2, 1), (1, 4)),
                    ((3, 2), (5, 1)),
                ]
                for (u0, u1), (b0, b1) in samples:
                    u = (fp(p, nr, u0, u1 % p), fp(p, nr, u1, (u0 + 1) % p))
                    b = (fp(p, nr, b0, (b1 + 1) % p), fp(p, nr, b1, b0 % p))
                    kappa = wedge(u, b)
                    trials += 1
                    if kappa.is_zero():
                        continue
                    g1 = wedge(ell, b)
                    g2 = p_e(b, ell, c, d)
                    h1 = wedge(u, ell)
                    h2 = p_e(u, ell, c, d)
                    d_gate = g1 * h2 + g2 * h1
                    rhs = -(mu * mu) * expected_sigma2[0] * kappa
                    assert d_gate == rhs, (p, c, d, u, b, d_gate, rhs)
                    assert not d_gate.is_zero()
                    checked += 1
    return {"p": p, "trials": trials, "off_R0_checked": checked}


def main() -> None:
    results = [run_prime(p) for p in (3, 5, 7, 11)]
    for item in results:
        print(
            f"p={item['p']}: checked {item['off_R0_checked']} off-R0 samples "
            f"from {item['trials']} deterministic trials"
        )
    print("PASS: Cycle 23 D=-mu^2*(c^2/4-d)*kappa identity verified in sampled tiny fields.")


if __name__ == "__main__":
    main()
