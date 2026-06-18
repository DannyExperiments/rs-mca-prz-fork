# Cycle 42 corrected characteristic-zero and density certificate

## Ledger

- `q_gen = p`
- `B = F_p`
- `F = F_{p^2} = B(alpha)`, `alpha^2=-1`
- `q_line = p^2`
- `q_chal` is unused
- `D=F_p`, `n=p`, `t=sigma=2`, `j=4`, `a=p-4`, `k=p-6`

## Characteristic-zero line models

On `z_0=z_1=s`, the primitive quartics are

```text
P_A = 4*s**3*x**4 + 12*s**3*x**2 + 4*s**3 - 2*s**2*x**4 - 12*s**2*x**3 - 14*s**2*x**2 - 28*s**2*x - 22*s**2 - 11*s*x**4 + 24*s*x**3 - 11*s*x**2 + 60*s*x + 35*s + 9*x**4 - 12*x**3 + 13*x**2 - 35*x - 17
P_B = 4*s**4*x**4 + 12*s**4*x**2 + 4*s**4 - 4*s**3*x**4 + 8*s**3*x**3 - 4*s**3*x**2 + 32*s**3*x + 20*s**3 + 10*s**2*x**4 - 52*s**2*x**3 + 38*s**2*x**2 - 120*s**2*x + 62*s**2 - 32*s*x**4 + 56*s*x**3 - 120*s*x**2 + 152*s*x - 244*s + 19*x**4 - 4*x**3 + 99*x**2 - 62*x + 205
```

Their Cramer determinants are

```text
Delta_A = -(s - 1)**2*(4*s**2 + 2*s - 9)
Delta_B = -4*s**4 + 4*s**3 - 10*s**2 + 32*s - 19
```

Their binary discriminants and reduced branch polynomials are

```text
disc_X(P_A) = (s - 1)**2*(1638400*s**16 - 4587520*s**15 - 34881536*s**14 + 73072640*s**13 + 358903808*s**12 - 641441792*s**11 - 2127262720*s**10 + 2484816896*s**9 + 17489308160*s**8 - 39769366016*s**7 - 20116857792*s**6 + 194165722432*s**5 - 347849758128*s**4 + 331010951712*s**3 - 184759775360*s**2 + 57468880452*s - 7749383319)
R_A = (s - 1)*(1638400*s**16 - 4587520*s**15 - 34881536*s**14 + 73072640*s**13 + 358903808*s**12 - 641441792*s**11 - 2127262720*s**10 + 2484816896*s**9 + 17489308160*s**8 - 39769366016*s**7 - 20116857792*s**6 + 194165722432*s**5 - 347849758128*s**4 + 331010951712*s**3 - 184759775360*s**2 + 57468880452*s - 7749383319)

disc_X(P_B) = 16*(102400*s**24 - 491520*s**23 + 1859584*s**22 - 3764224*s**21 + 51914752*s**20 - 192626688*s**19 + 477325312*s**18 - 2008282112*s**17 + 7446446592*s**16 - 20807045120*s**15 + 59079347712*s**14 - 185639798528*s**13 + 512758278912*s**12 - 1116174999552*s**11 + 2298634344064*s**10 - 5753999742784*s**9 + 14592594673376*s**8 - 28990435945600*s**7 + 41864795175328*s**6 - 43894177136944*s**5 + 33781948075336*s**4 - 19154923131744*s**3 + 7820247111000*s**2 - 2096953679988*s + 276965239259)
R_B = 102400*s**24 - 491520*s**23 + 1859584*s**22 - 3764224*s**21 + 51914752*s**20 - 192626688*s**19 + 477325312*s**18 - 2008282112*s**17 + 7446446592*s**16 - 20807045120*s**15 + 59079347712*s**14 - 185639798528*s**13 + 512758278912*s**12 - 1116174999552*s**11 + 2298634344064*s**10 - 5753999742784*s**9 + 14592594673376*s**8 - 28990435945600*s**7 + 41864795175328*s**6 - 43894177136944*s**5 + 33781948075336*s**4 - 19154923131744*s**3 + 7820247111000*s**2 - 2096953679988*s + 276965239259
```

The Cycle-41 raw numerator identities are

```text
Delta_A^6 disc_X(L_A) = (s - 1)**8*(1638400*s**16 - 4587520*s**15 - 34881536*s**14 + 73072640*s**13 + 358903808*s**12 - 641441792*s**11 - 2127262720*s**10 + 2484816896*s**9 + 17489308160*s**8 - 39769366016*s**7 - 20116857792*s**6 + 194165722432*s**5 - 347849758128*s**4 + 331010951712*s**3 - 184759775360*s**2 + 57468880452*s - 7749383319)
Delta_B^6 disc_X(L_B) = 16*(102400*s**24 - 491520*s**23 + 1859584*s**22 - 3764224*s**21 + 51914752*s**20 - 192626688*s**19 + 477325312*s**18 - 2008282112*s**17 + 7446446592*s**16 - 20807045120*s**15 + 59079347712*s**14 - 185639798528*s**13 + 512758278912*s**12 - 1116174999552*s**11 + 2298634344064*s**10 - 5753999742784*s**9 + 14592594673376*s**8 - 28990435945600*s**7 + 41864795175328*s**6 - 43894177136944*s**5 + 33781948075336*s**4 - 19154923131744*s**3 + 7820247111000*s**2 - 2096953679988*s + 276965239259)
```

Thus A fails the Cycle-41 gate identically because the raw objects have a common repeated factor at `s=1`; the reduced branch support is squarefree.

## A16

```text
1638400*s**16 - 4587520*s**15 - 34881536*s**14 + 73072640*s**13 + 358903808*s**12 - 641441792*s**11 - 2127262720*s**10 + 2484816896*s**9 + 17489308160*s**8 - 39769366016*s**7 - 20116857792*s**6 + 194165722432*s**5 - 347849758128*s**4 + 331010951712*s**3 - 184759775360*s**2 + 57468880452*s - 7749383319
```

## B24

```text
102400*s**24 - 491520*s**23 + 1859584*s**22 - 3764224*s**21 + 51914752*s**20 - 192626688*s**19 + 477325312*s**18 - 2008282112*s**17 + 7446446592*s**16 - 20807045120*s**15 + 59079347712*s**14 - 185639798528*s**13 + 512758278912*s**12 - 1116174999552*s**11 + 2298634344064*s**10 - 5753999742784*s**9 + 14592594673376*s**8 - 28990435945600*s**7 + 41864795175328*s**6 - 43894177136944*s**5 + 33781948075336*s**4 - 19154923131744*s**3 + 7820247111000*s**2 - 2096953679988*s + 276965239259
```

## Direct characteristic-zero S4 certificates

A at `s=4`:

```json
{
  "S4_certificate": true,
  "cubic_resolvent": "343*y**3 - 931*y**2 + 56*y - 51",
  "quartic": "7*x**4 - 4*x**3 + 19*x**2 - 9*x + 1",
  "quartic_discriminant": -1308871,
  "quartic_discriminant_factorization": {
    "241": 1,
    "5431": 1
  },
  "quartic_discriminant_nonsquare": true,
  "quartic_irreducibility_prime": 3,
  "quartic_irreducible_mod_prime": true,
  "quartic_mod_prime": "x**4 - x**3 + x**2 + 1",
  "resolvent_irreducibility_prime": 2,
  "resolvent_irreducible_mod_prime": true,
  "resolvent_mod_prime": "y**3 + y**2 + 1",
  "s": 4
}
```

B at `s=2`:

```json
{
  "S4_certificate": true,
  "cubic_resolvent": "9*y**3 - 57*y**2 - 260*y + 1480",
  "quartic": "3*x**4 - 4*x**3 + 19*x**2 + 2*x + 21",
  "quartic_discriminant": 79061040,
  "quartic_discriminant_factorization": {
    "109807": 1,
    "2": 4,
    "3": 2,
    "5": 1
  },
  "quartic_discriminant_nonsquare": true,
  "quartic_irreducibility_prime": 17,
  "quartic_irreducible_mod_prime": true,
  "quartic_mod_prime": "3*x**4 - 4*x**3 + 2*x**2 + 2*x + 4",
  "resolvent_irreducibility_prime": 7,
  "resolvent_irreducible_mod_prime": true,
  "resolvent_mod_prime": "2*y**3 - y**2 - y + 3",
  "s": 2
}
```

## Corrected tame good-reduction certificates

At `p=7`,

```text
R_A mod 7 = (s-1)(s^2-2s+2)(s^3+2s^2+3)
            (s^11-2s^9-3s^8-s^7-3s^6-2s^5-3s^4+3s^3+s^2+2s-1),
```

all factors with exponent one. The exceptional point `s=1` has reciprocal local equation

```text
4*tloc**3*yloc**4 + 12*tloc**3*yloc**2 + 4*tloc**3 - 10*tloc**2*yloc**4 - 28*tloc**2*yloc**3 + 22*tloc**2*yloc**2 - 12*tloc**2*yloc + 10*tloc**2 + 3*tloc*yloc**4 + 4*tloc*yloc**3 - 3*tloc*yloc**2 - 3*tloc - 3*yloc**3
```

with `dH/dt(0,0)=-3` and special fiber `H(0,y)=-3y^3`, hence tame index 3.

At `p=19`,

```text
R_B mod 19 = 9(s^2+8s+6)(s^3-6s^2+5s-5)
             (s^19-3s^18-8s^17+3s^16-5s^15+8s^14-s^13+8s^12
              +7s^11-2s^10-3s^9+8s^8-8s^7+5s^6+2s^5-9s^4
              +s^3+8s^2+4s+6),
```

again squarefree. The fiber at `s=infinity` in both models is
`4(x^4+3x^2+1)`, discriminant `1638400`, so it is unramified at 7 and 19.

## Sufficient bad-prime supports

Up to sign,

```text
Disc(R_A) = {2: 288, 3: 106, 5: 4, 1031: 2, 136189: 2, 169114662857729621: 3, 29920018492819343403247709: 1}
Disc(R_B) = {2: 384, 3: 99, 5: 4, 11: 3, 29: 1, 41: 3, 2063: 30, 234007: 2, 4711367: 1, 1149593: 1, 429182827: 2, 986904239: 3, 6003144422654343011: 3, 87979847046285199339509999686219951947: 1}
```

A sufficient Gaussian bad-ideal set is the set of prime ideals of `Z[i]` dividing
`24 Disc(R_A)` or `24 Disc(R_B)`, respectively. This set is sufficient, not claimed minimal.

Relevant rational bad primes in the source congruence classes are

```text
A (p mod 20 in {3,7}): [3]
B (p mod 20 in {11,19}): [11, 986904239, 6003144422654343011]
```

## Finite checks

```json
A p=7: {"S4_hist_gate": true, "hist": {"112": 1, "13": 2, "4": 1}, "p": 7, "singular": 3, "witness_13": 0, "witness_4": 3}
B p=19: {"S4_hist_gate": true, "hist": {"1111": 1, "112": 3, "13": 4, "22": 5, "4": 4}, "p": 19, "singular": 2, "witness_13": 2, "witness_4": 6}
```

## Density conclusion

For every relevant prime outside the sufficient bad set, the line cover has geometric group `S4`; hence the two-dimensional surface cover has geometric group `S4`. If `Y_p -> U_p` is its degree-24 Galois closure over the off-branch open, Lang--Weil gives

```text
#Y_p(F_p)=p^2+O(p^(3/2)),
N_split(p)=p^2/24+O(p^(3/2)).
```

Since `q_line=p^2`, this is `N_split/q_line=1/24+O(p^(-1/2))`.
