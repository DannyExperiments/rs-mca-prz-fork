# Cycle118 two-ended agreement-263 checker specification

## Success terminal

```text
CYCLE118_TWO_ENDED_AGREEMENT_263_TRANSFER_VERIFIED
```

The success terminal certifies only the finite attached-packet/source-scoped support-wise theorem. It does not certify ordinary list decoding, protocol soundness, asymptotics, or official Proximity Prize status.

## Exit decisions

| Decision | Exit code | Meaning |
|---|---:|---|
| `CYCLE118_TWO_ENDED_AGREEMENT_263_TRANSFER_VERIFIED` | 0 | Every imported hash, finite identity, symbolic-lemma hypothesis, row parameter, and strict-distance check passed. |
| `CERTIFICATE_REJECTED` | 1 | A named mathematical or ledger clause failed. |
| `MALFORMED_INPUT` | 2 | JSON, schema, field representation, or required value was malformed. |
| `MISSING_TWO_ENDED_CERTIFICATE` | 3 | The Cycle118 input is absent. |
| `MISSING_BASE_INPUT` | 4 | A required Cycle116 base input is absent. |

## Inputs

1. `inputs/two_ended_certificate.json`
   - pins the Role05 response hash and the Cycle116 manifest hash;
   - pins the new ranges `A*=[0,119]`, `R*=[120,255]`;
   - pins `n=512`, `j=249`, `sigma=7`, `r=k=256`, agreement `263`;
   - pins `q_gen=q_code=q_line=17^32` and `q_chal=null`.

2. `base_cycle116/inputs/cycle84_anchor.json`
   - hash-binds the Cycle84 master certificate, slot logs, light receipt, and finite note;
   - imports `52,747,567,092` without rerunning the full census.

3. `base_cycle116/inputs/fixed_jet_certificate.json`
   - pins the field, `eta`, `beta`, block templates, colors, shell, and reference tuple.

## Executable finite checks

The checker verifies, fail-closed:

```text
Cycle84 occupancy N=52,747,567,092 and m_max=2
master color filter is exactly total color 4 mod 16
all 336 slot field/log/color identities
all 336 slot constants L_(t,i,a)(0)=3^(t+color)
all 336 block evaluations L_(t,i,a)(beta)=3^t u_t(i,a)
Cycle84 shell count 52,747,567,104 by 16-state DP
reference P_T(0)=-1 and P_T(beta)=4(beta-1)Phi(T)
A*,R* partition the odd coset with sizes 120,136
P_R*(0)!=0 and P_R*(beta)!=0
reference J_T* size 249 and agreement support size 263
136+107=243=249-7+1
P_T*(beta)=fixed_nonzero_scalar*Phi(T)
selected evaluator coordinates 0,250,...,255
7x7 evaluator matrix triangularity and invertibility
seven evaluator-basis identities and seven annihilator identities
n=512,k=256,j=249,sigma=7,agreement=263
beta outside H and 250 distinct Vandermonde columns fit in dimension 256
249<250=(125/256)*512
N/17^32>2^-128
```

## Symbolic implications

The executable does not enumerate all shell tuples. The universal steps are proved in `SYMBOLIC_LEMMAS.md`:

```text
slot gap X^16+O(X^10) => P_T=X^113-X^112+O(X^107)
shell constant identities => P_T(0)=-1 for every tuple
common top six + common nonzero constant => seven-dimensional evaluator
weighted Vandermonde kernel equals RS[K,H,256]
explicit inverse-DFT formula constructs the one common affine line
y0+z_T y1 in W_(J_T*) constructs every explaining codeword
Vandermonde independence proves support-wise noncontainment
fixed nonzero scalar preserves all N distinct evaluations
```

The checker explicitly uses the constant coordinate. It never assumes a common seventh top jet.

## qchal discipline

No independent challenge is introduced:

```text
q_gen=q_code=q_line=17^32
q_chal=null
challenge_space=null
challenge_distribution=null
challenge_to_line_parameter_map=null
```

The denominator in the finite attached-source MCA statement is `q_line`. No official challenge-map claim is made.
