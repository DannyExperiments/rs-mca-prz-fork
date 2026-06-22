# Role 02 - P190 Source Replay Prosecutor

Your task is to replay P190 through the official source contract, if that
contract exists in the packet. Treat P190 as a hostile candidate
counterpacket and either certify it or kill it with a receipt.

Start from:

```text
p = q_line = 130 * 2^128 + 1
floor(q_line / 2^128) = 130
P190 displayed colors = 190
P190 after one endpoint = 189
P190 full natural t=1 zero-sum supports = 26980
P190 full natural raw colors = 26245
```

Apply, in order:

```text
source adapter
official AP_corr
endpoint convention
same-slope collapse
contained incidence exclusion
affine-color normalization
quotient/periodic exclusion or charge
final retained color/event map
charge registry and q_line allocation
```

Try to return:

```text
SOURCE_VALID_LOW_T1_COUNTERPACKET
```

The bar is exact: official source accepted, official APcorr true, final free
events above 130, and every official charge absent or paid without double
spending.

If P190 is rejected or compressed, return `SOURCE_REJECTED` or
`COLOR_COMPRESSED_OR_CHARGED` with the exact clause and arithmetic. If the
source root is not present, return `SOURCE_RECEIPT_MISSING_NO_CLAIM` with the
first missing receipt.

