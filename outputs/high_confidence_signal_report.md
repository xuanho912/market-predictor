# High Confidence Signal Report

Generated at: `2026-09-28T19:43:15.328110+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0064`, median `0.0085`, brier `0.1897`, calibration_gap `0.0814`
- 5d: hit_rate `0.7500`, avg `0.0022`, median `0.0068`, brier `0.1897`, calibration_gap `0.0814`
- 10d: hit_rate `0.6250`, avg `-0.0008`, median `0.0041`, brier `0.2784`, calibration_gap `0.2064`
- 20d: hit_rate `0.7500`, avg `0.0247`, median `0.0324`, brier `0.1940`, calibration_gap `0.0814`
- 60d: hit_rate `1.0000`, avg `0.0540`, median `0.0565`, brier `0.0285`, calibration_gap `-0.1686`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0043`, median `0.0088`, brier `0.2293`, calibration_gap `0.1332`
- 5d: hit_rate `0.6875`, avg `0.0043`, median `0.0076`, brier `0.2293`, calibration_gap `0.1332`
- 10d: hit_rate `0.6875`, avg `0.0010`, median `0.0060`, brier `0.2348`, calibration_gap `0.1332`
- 20d: hit_rate `0.7500`, avg `0.0164`, median `0.0173`, brier `0.1927`, calibration_gap `0.0707`
- 60d: hit_rate `0.9375`, avg `0.0643`, median `0.0625`, brier `0.0711`, calibration_gap `-0.1168`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5500`, avg `0.0009`, median `0.0030`, brier `0.2781`, calibration_gap `0.1873`
- 5d: hit_rate `0.6250`, avg `-0.0021`, median `0.0031`, brier `0.2524`, calibration_gap `0.1123`
- 10d: hit_rate `0.6250`, avg `0.0012`, median `0.0061`, brier `0.2569`, calibration_gap `0.1123`
- 20d: hit_rate `0.7500`, avg `0.0177`, median `0.0243`, brier `0.2078`, calibration_gap `-0.0127`
- 60d: hit_rate `0.8750`, avg `0.0497`, median `0.0557`, brier `0.1361`, calibration_gap `-0.1377`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0006`, median `0.0011`, brier `0.2741`, calibration_gap `0.1547`
- 5d: hit_rate `0.5625`, avg `-0.0053`, median `0.0012`, brier `0.2529`, calibration_gap `0.0922`
- 10d: hit_rate `0.6250`, avg `0.0059`, median `0.0154`, brier `0.2357`, calibration_gap `0.0297`
- 20d: hit_rate `0.8125`, avg `0.0258`, median `0.0343`, brier `0.1782`, calibration_gap `-0.1578`
- 60d: hit_rate `0.8750`, avg `0.0493`, median `0.0588`, brier `0.1576`, calibration_gap `-0.2203`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
