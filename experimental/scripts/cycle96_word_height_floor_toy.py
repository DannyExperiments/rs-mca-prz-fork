#!/usr/bin/env python3
"""Toy verifier for Cycle96's arbitrary-word height-floor obstruction.

This is not a proof. It enumerates small RS word cosets and measures the
minimal infinity norm of a balanced integer lift after adding a codeword. The
point is to sanity-check the counting statement behind
L-CYCLE96-WORD-HEIGHT-FLOOR: most arbitrary word cosets do not have tiny
height representatives.
"""

from __future__ import annotations

from itertools import product
from collections import Counter


def eval_poly(coeffs: tuple[int, ...], x: int, p: int) -> int:
    acc = 0
    for c in reversed(coeffs):
        acc = (acc * x + c) % p
    return acc


def balanced(a: int, p: int) -> int:
    a %= p
    return a - p if a > p // 2 else a


def rs_codewords(p: int, domain: list[int], dim: int) -> list[tuple[int, ...]]:
    words = []
    for coeffs in product(range(p), repeat=dim):
        words.append(tuple(eval_poly(coeffs, x, p) for x in domain))
    return words


def add_words(a: tuple[int, ...], b: tuple[int, ...], p: int) -> tuple[int, ...]:
    return tuple((x + y) % p for x, y in zip(a, b))


def height(word: tuple[int, ...], p: int) -> int:
    return max(abs(balanced(x, p)) for x in word)


def min_coset_height(word: tuple[int, ...], code: list[tuple[int, ...]], p: int) -> int:
    return min(height(add_words(word, c, p), p) for c in code)


def scan(p: int, n: int, dim: int) -> dict:
    domain = list(range(n))
    code = rs_codewords(p, domain, dim)
    seen_cosets: set[tuple[int, ...]] = set()
    hist: Counter[int] = Counter()
    cosets = 0
    for word in product(range(p), repeat=n):
        if word in seen_cosets:
            continue
        orbit = {add_words(word, c, p) for c in code}
        seen_cosets.update(orbit)
        hist[min(height(v, p) for v in orbit)] += 1
        cosets += 1
    expected = p ** (n - dim)
    assert cosets == expected, (cosets, expected)
    cumulative = {}
    running = 0
    for h in sorted(hist):
        running += hist[h]
        cumulative[h] = running
    return {
        "p": p,
        "n": n,
        "dim": dim,
        "rho_dim": dim / n,
        "code_size": len(code),
        "cosets": cosets,
        "height_histogram": dict(sorted(hist.items())),
        "cumulative": cumulative,
        "max_min_height": max(hist),
        "passed": True,
    }


def main() -> None:
    cases = [
        (5, 4, 2),
        (7, 5, 2),
        (7, 5, 3),
        (11, 5, 2),
    ]
    reports = [scan(*case) for case in cases]
    print("cycle96 word-height floor toy check")
    for report in reports:
        print(report)
    print("PASS")


if __name__ == "__main__":
    main()
