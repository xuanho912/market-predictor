# High Confidence Signal Report

Generated at: `2026-07-15T21:31:03.683629+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0009`, median `0.0004`, brier `0.2996`, calibration_gap `0.2205`
- 5d: hit_rate `0.6250`, avg `0.0017`, median `0.0096`, brier `0.2442`, calibration_gap `0.0955`
- 10d: hit_rate `0.6250`, avg `0.0063`, median `0.0129`, brier `0.2455`, calibration_gap `0.0955`
- 20d: hit_rate `0.7500`, avg `0.0075`, median `0.0140`, brier `0.1887`, calibration_gap `-0.0295`
- 60d: hit_rate `0.5000`, avg `-0.0148`, median `-0.0162`, brier `0.2981`, calibration_gap `0.2205`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0017`, median `0.0046`, brier `0.2451`, calibration_gap `0.0889`
- 5d: hit_rate `0.6875`, avg `0.0033`, median `0.0094`, brier `0.2174`, calibration_gap `0.0264`
- 10d: hit_rate `0.6250`, avg `0.0043`, median `0.0098`, brier `0.2437`, calibration_gap `0.0889`
- 20d: hit_rate `0.6250`, avg `0.0060`, median `0.0080`, brier `0.2405`, calibration_gap `0.0889`
- 60d: hit_rate `0.5000`, avg `-0.0022`, median `-0.0060`, brier `0.2949`, calibration_gap `0.2139`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6250`, avg `0.0035`, median `0.0054`, brier `0.2369`, calibration_gap `0.0623`
- 5d: hit_rate `0.5500`, avg `0.0025`, median `0.0053`, brier `0.2627`, calibration_gap `0.1373`
- 10d: hit_rate `0.5500`, avg `0.0035`, median `0.0043`, brier `0.2648`, calibration_gap `0.1373`
- 20d: hit_rate `0.6750`, avg `0.0009`, median `0.0076`, brier `0.2230`, calibration_gap `0.0123`
- 60d: hit_rate `0.5750`, avg `0.0127`, median `0.0160`, brier `0.2578`, calibration_gap `0.1123`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0023`, median `-0.0020`, brier `0.2989`, calibration_gap `0.2306`
- 5d: hit_rate `0.4375`, avg `-0.0083`, median `-0.0109`, brier `0.2980`, calibration_gap `0.2306`
- 10d: hit_rate `0.5000`, avg `-0.0039`, median `0.0018`, brier `0.2770`, calibration_gap `0.1681`
- 20d: hit_rate `0.6875`, avg `-0.0052`, median `0.0018`, brier `0.2159`, calibration_gap `-0.0194`
- 60d: hit_rate `0.3750`, avg `-0.0283`, median `-0.0364`, brier `0.3215`, calibration_gap `0.2931`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
