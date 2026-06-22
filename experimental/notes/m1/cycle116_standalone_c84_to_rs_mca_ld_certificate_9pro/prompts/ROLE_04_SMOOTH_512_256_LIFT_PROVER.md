# Role 04: Smooth `[512,256]` Lift Prover

Use the common prompt. No Internet.

Your job is to prove or break the smooth lift:

```text
F0 = F_17^16
eta has order 256
K = F0(theta), theta^2=eta = F_17^32
H=<theta>, |H|=512
C = RS[K,H,256]
```

Starting from the native Cycle85/Cycle84 line over `D0=<eta>`, prove that agreement-padding on `H=D0 union theta D0` preserves the numerator:

```text
LD_sw(RS[K,H,256],262) >= 52,747,567,092
epsilon_mca(C,125/256) >= 52,747,567,092 / 17^32.
```

You must explicitly verify:

- `eta` nonsquare and `theta` order `512`;
- choice of padding set `A` of size `119` and unused set `R`;
- polynomial multiplication by `L_A`;
- preserved agreement on `S_z union A`;
- preserved noncontainment after dividing by `L_A`;
- no hidden GRS/RS or field-extension loss.

If the lift is false, identify the first invalid line.
