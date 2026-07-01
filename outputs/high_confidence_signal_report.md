# High Confidence Signal Report

Generated at: `2026-07-01T23:55:30.571706+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.2500`, avg `-0.0119`, median `-0.0064`, brier `0.4075`, calibration_gap `0.4641`
- 5d: hit_rate `0.5000`, avg `-0.0081`, median `-0.0089`, brier `0.3013`, calibration_gap `0.2141`
- 10d: hit_rate `0.2500`, avg `-0.0057`, median `-0.0061`, brier `0.4075`, calibration_gap `0.4641`
- 20d: hit_rate `0.8750`, avg `0.0306`, median `0.0314`, brier `0.1344`, calibration_gap `-0.1609`
- 60d: hit_rate `0.7500`, avg `0.0471`, median `0.0594`, brier `0.1861`, calibration_gap `-0.0359`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0087`, median `-0.0040`, brier `0.3733`, calibration_gap `0.3929`
- 5d: hit_rate `0.4375`, avg `-0.0108`, median `-0.0200`, brier `0.3194`, calibration_gap `0.2679`
- 10d: hit_rate `0.3750`, avg `-0.0019`, median `-0.0038`, brier `0.3476`, calibration_gap `0.3304`
- 20d: hit_rate `0.8125`, avg `0.0243`, median `0.0186`, brier `0.1624`, calibration_gap `-0.1071`
- 60d: hit_rate `0.5625`, avg `0.0246`, median `0.0449`, brier `0.2618`, calibration_gap `0.1429`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.3250`, avg `-0.0065`, median `-0.0063`, brier `0.3429`, calibration_gap `0.3414`
- 5d: hit_rate `0.3500`, avg `-0.0096`, median `-0.0083`, brier `0.3314`, calibration_gap `0.3164`
- 10d: hit_rate `0.4250`, avg `0.0005`, median `-0.0060`, brier `0.3136`, calibration_gap `0.2414`
- 20d: hit_rate `0.6250`, avg `0.0140`, median `0.0164`, brier `0.2341`, calibration_gap `0.0414`
- 60d: hit_rate `0.6500`, avg `0.0367`, median `0.0547`, brier `0.2249`, calibration_gap `0.0164`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0020`, median `0.0012`, brier `0.2503`, calibration_gap `0.0570`
- 5d: hit_rate `0.5000`, avg `-0.0046`, median `-0.0058`, brier `0.2658`, calibration_gap `0.1195`
- 10d: hit_rate `0.4375`, avg `-0.0035`, median `-0.0115`, brier `0.2796`, calibration_gap `0.1820`
- 20d: hit_rate `0.6875`, avg `-0.0092`, median `0.0033`, brier `0.2198`, calibration_gap `-0.0680`
- 60d: hit_rate `0.3750`, avg `0.0052`, median `-0.0136`, brier `0.2945`, calibration_gap `0.2445`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
