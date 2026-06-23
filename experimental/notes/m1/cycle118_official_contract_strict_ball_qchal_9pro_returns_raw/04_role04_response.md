LABEL:

**PROOF / BANKABLE_LEMMA / ROUTE_CUT**

`L-CYCLE118-STRICT-BALL-AGREEMENT-263-UPGRADE`

Finite, packet-pinned, support-wise `LD_sw` scope. Not official/prize-adopted scope.

EXECUTIVE VERDICT:

The strict-ball target is solved with a reduced but still security-sufficient numerator:

[
\boxed{\operatorname{LD}*{\rm sw}
\bigl(\operatorname{RS}[\mathbb F*{17^{32}},H,256],264\bigr)
\ge 2{,}630{,}383.}
]

Consequently,

[
\boxed{\operatorname{LD}*{\rm sw}
\bigl(\operatorname{RS}[\mathbb F*{17^{32}},H,256],263\bigr)
\ge 2{,}630{,}383.}
]

Every constructed line point has at most

[
512-264=248
]

errors, whereas the strict target is

[
\frac{125}{256}\cdot512=250.
]

Thus these witnesses lie strictly inside the ball:

[
248<250.
]

Moreover,

[
\epsilon_{\rm mca}!\left(C,\frac{125}{256}\right)
\ge \frac{2{,}630{,}383}{17^{32}}>2^{-128},
]

because (\lfloor17^{32}/2^{128}\rfloor=6).

The full Cycle84 numerator (52{,}747{,}567{,}092) is not preserved. The first failure in that route is exact: its seventh locator coefficient varies, and multiplication by fixed padding cannot eliminate that variation.

THEOREM / COUNTERPACKET / ROUTE CUT:

Let

[
F_0=\mathbb F_{17}[X]/(X^{16}+X^8+3),\qquad
\eta=6X^9,\qquad \beta=X+2,
]

and (D_0=\langle\eta\rangle), so (|D_0|=256) and (\eta^{16}=3).

For an eight-subset (B\subseteq\mathbb Z/16\mathbb Z), define (e_r(B)) as the (r)-th elementary symmetric function of

[
{3^b:b\in B}\subseteq\mathbb F_{17}^{\times}.
]

Set

[
\mathcal B_0={B:|B|=8,\ e_1(B)=e_3(B)=0},
]

and

[
\mathcal G={B\in\mathcal B_0:e_2(B)=9}.
]

Explicitly, (\mathcal G) consists of the following seven sets:

[
\begin{aligned}
&(0,1,2,3,6,7,11,13),\
&(0,1,2,7,8,9,10,15),\
&(0,1,4,5,6,8,10,11),\
&(0,2,3,8,9,12,13,14),\
&(1,2,4,6,9,10,12,14),\
&(1,3,4,7,9,11,12,15),\
&(3,5,8,9,10,11,14,15).
\end{aligned}
]

Define the ordered-pair family

[
\mathcal P=
{(B,C)\in\mathcal B_0^2:
e_2(B)+3e_2(C)=1}.
]

Then

[
|\mathcal P|=613.
]

Fix (G_0\in\mathcal G). Choose

[
(B_1,B_5)\in\mathcal P,\qquad
(B_2,B_6)\in\mathcal P,\qquad
B_3\in\mathcal G,
]

and put (B_4=B_7=G_0). This gives

[
613^2\cdot7=2{,}630{,}383
]

tuples.

For each (B), let

[
Y_B={y\in\langle\eta^8\rangle:
y^2\in{3^b:b\in B}},
]

and define

[
U_\tau=\bigcup_{t=1}^7\eta^tY_{B_t}.
]

Then (|U_\tau|=112), all locator polynomials have a common eight-jet, and the (2{,}630{,}383) values of their locators at (\beta) are distinct.

Therefore

[
\operatorname{LD}_{\rm sw}
\bigl(\operatorname{RS}[F_0,D_0,136],144\bigr)
\ge2{,}630{,}383.
]

The 120-point smooth lift then gives the asserted ([512,256]), agreement-264 theorem.

**Route cut for the full Cycle84 family.** After deleting its fixed singleton, the Cycle84 locator has the form

[
Q_\tau(Z)=Z^{112}+M(\tau)Z^{106}+O(Z^{104}),
]

and (M(\tau)) is not constant even on the color shell. Hence that family has only a common six-jet. If (R) is any fixed monic padding polynomial, then

[
\deg R(Q_\tau-Q_{\tau'})
=\deg R+\deg(Q_\tau-Q_{\tau'}),
]

so fixed padding preserves, rather than improves, the first variable coefficient. Thus the full Cycle84 numerator cannot reach agreement 263 through the unchanged fixed-padding/common-jet construction.

PROOF DETAILS:

For (B\in\mathcal B_0),

[
\prod_{b\in B}(Y-3^b)
=Y^8+e_2(B)Y^6+O(Y^4),
]

because (e_1(B)=e_3(B)=0).

The locator of the corresponding sixteen-point block in slot (t) is

[
R_{t,B}(Z)
=\prod_{b\in B}(Z^2-\eta^{2t}3^b)
=Z^{16}+e_2(B)\eta^{4t}Z^{12}+O(Z^8).
]

Let (\xi=\eta^4). Since (\xi^4=\eta^{16}=3), the product locator

[
Q_\tau(Z)=\prod_{t=1}^7R_{t,B_t}(Z)
]

satisfies

[
Q_\tau(Z)
=Z^{112}
+\left(\sum_{t=1}^7e_2(B_t)\xi^t\right)Z^{108}
+O(Z^{104}).
]

For the chosen tuple family,

[
\begin{aligned}
\sum_{t=1}^7e_2(B_t)\xi^t
&=\xi\bigl(e_2(B_1)+3e_2(B_5)\bigr)\
&\quad+\xi^2\bigl(e_2(B_2)+3e_2(B_6)\bigr)\
&\quad+\xi^3(9+3\cdot9)+3\cdot9\
&=10+\xi+\xi^2+2\xi^3,
\end{aligned}
]

which is independent of (\tau). Hence

[
\deg(Q_\tau-Q_{\tau'})\le104=112-8.
]

The fixed-jet theorem therefore applies with

[
(n,j,\sigma,r,k)=(256,112,8,120,136).
]

Its witness support has size

[
n-j=144.
]

The finite count (|\mathcal P|=613) follows from the exact distribution

[
\bigl|{B\in\mathcal B_0:e_2(B)=c}\bigr|_{c=0}^{16}
==================================================

(6,7,7,5,7,5,5,5,7,7,5,5,5,7,5,7,7),
]

since

[
|\mathcal P|
=\sum_{c\in\mathbb F_{17}}
N_c,N_{(1-c)/3}
=613.
]

The finite-field checker then verifies:

[
\begin{array}{c|r}
\text{family} & \text{distinct normalized products}\ \hline
(B_1,B_5)\in\mathcal P & 613\
(B_2,B_6)\in\mathcal P & 613\
\text{cross-products of the two pair families} & 375{,}769\
\text{after }B_3\in\mathcal G & 2{,}630{,}383
\end{array}
]

Slots (4) and (7) contribute a fixed nonzero factor, so they do not create collisions. Thus all (Q_\tau(\beta)) are distinct.

For the smooth lift, take

[
K=F_0(\theta)\cong\mathbb F_{17^{32}},
\qquad \theta^2=\eta,
\qquad H=\langle\theta\rangle.
]

Partition the odd coset using

[
A={\theta\eta^i:0\le i\le119},\qquad |A|=120,
]

and

[
R={\theta\eta^i:120\le i\le255},\qquad |R|=136.
]

Multiplication by the fixed locator (L_A) changes degree (<136) to degree (<256). Each native agreement support of size (144) becomes a lifted support of size

[
144+120=264.
]

If degree-(<256) polynomials simultaneously explained the lifted line generators on that support, both would vanish on (A), hence factor through (L_A). Division would produce simultaneous degree-(<136) native explanations, contradicting native noncontainment.

The lifted co-support ledger is therefore

[
j=112+136=248,\qquad
\sigma=(512-256)-248=8.
]

The construction has distance at most (248), which is strictly below the external threshold (250).

The reproducible finite certificate is here:

[Cycle118 strict-ball checker](sandbox:/mnt/data/cycle118_strict_ball_264_checker.py)

[Cycle118 strict-ball receipt](sandbox:/mnt/data/cycle118_strict_ball_264_receipt.json)

FIELD AND PARAMETER LEDGER:

| Quantity            |               Native row |        Smooth lifted row |
| ------------------- | -----------------------: | -----------------------: |
| Field               |    (\mathbb F_{17^{16}}) |    (\mathbb F_{17^{32}}) |
| Domain              | (D_0=\langle\eta\rangle) | (H=\langle\theta\rangle) |
| (n)                 |                      256 |                      512 |
| (k)                 |                      136 |                      256 |
| Co-support (j)      |                      112 |                      248 |
| Common jet (\sigma) |                        8 |                        8 |
| Agreement           |                      144 |                      264 |
| Errors              |                      112 |                      248 |
| Certified numerator |                2,630,383 |                2,630,383 |
| Padding size        |                        — |                      120 |

For the final row:

[
q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{32},
\qquad q_{\rm chal}=\mathrm{null}.
]

No challenge-field denominator was introduced.

SELF-AUDIT:

1. **Exact statement and scope.**
   I proved a finite, packet-pinned support-wise theorem:

   [
   LD_{\rm sw}(RS[\mathbb F_{17^{32}},H,256],264)
   \ge2{,}630{,}383.
   ]

   It implies the agreement-263 bound and strict-distance robustness. It is not an official/prize-adopted theorem.

2. **Field ledger.**
   The final generator, code and line fields are all (\mathbb F_{17^{32}}). The denominator is (q_{\rm line}=17^{32}). `q_chal` remains null.

3. **Event reductions.**
   Under the attached raw support-wise definition, there is no endpoint, quotient, periodic, tangent, affine-color or charge division. Contained-line witnesses are excluded by the fixed-jet noncontainment proof. An official event registry could still reduce the numerator; no official retention claim is made.

4. **Decoding notion.**
   This concerns support-wise (LD_{\rm sw}). It is not a fixed-word list-size lower bound. It also certifies (2{,}630{,}383) line points strictly within the radius, but the received words vary along one affine line.

5. **First missing official clause.**
   The first official gate remains the independently authenticated `authority` and `source_document` contract/trust pin, followed by explicit row admission, `q_chal`, and the exhaustive nine-rule event registry. None is supplied by the packet.

6. **Next worker target.**
   Attack

   [
   \texttt{L-CYCLE118-C84-RECIPROCAL-AFFINE-SEVENTH-MOMENT}.
   ]

   For the full Cycle84 shell, compute the largest subset satisfying

   [
   M(\tau)=a+bz_\tau,
   \qquad
   z_\tau=-\frac1{P_\tau(\beta)}.
   ]

   The extra syndrome coordinate in a one-row parity-check lift is affine in (z_\tau) exactly when this relation holds. This checker either recovers a large fraction of the Cycle84 numerator at agreement 263 or formally cuts every lift preserving the existing projected affine line.
