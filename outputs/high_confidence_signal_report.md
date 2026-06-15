# High Confidence Signal Report

Generated at: `2026-06-15T17:16:56.762223+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0003`, median `0.0031`, brier `0.2427`, calibration_gap `0.0880`
- 5d: hit_rate `0.5000`, avg `-0.0034`, median `-0.0047`, brier `0.2966`, calibration_gap `0.2130`
- 10d: hit_rate `0.8750`, avg `0.0113`, median `0.0135`, brier `0.1384`, calibration_gap `-0.1620`
- 20d: hit_rate `0.7500`, avg `0.0076`, median `0.0123`, brier `0.1856`, calibration_gap `-0.0370`
- 60d: hit_rate `0.2500`, avg `-0.0320`, median `-0.0398`, brier `0.4009`, calibration_gap `0.4630`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0017`, median `0.0028`, brier `0.2636`, calibration_gap `0.1377`
- 5d: hit_rate `0.3750`, avg `-0.0044`, median `-0.0057`, brier `0.3380`, calibration_gap `0.3252`
- 10d: hit_rate `0.6875`, avg `0.0059`, median `0.0075`, brier `0.2118`, calibration_gap `0.0127`
- 20d: hit_rate `0.7500`, avg `0.0088`, median `0.0143`, brier `0.1891`, calibration_gap `-0.0498`
- 60d: hit_rate `0.3750`, avg `-0.0021`, median `-0.0252`, brier `0.3422`, calibration_gap `0.3252`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6125`, avg `0.0039`, median `0.0046`, brier `0.2459`, calibration_gap `0.0498`
- 5d: hit_rate `0.6375`, avg `0.0056`, median `0.0052`, brier `0.2407`, calibration_gap `0.0248`
- 10d: hit_rate `0.6000`, avg `0.0074`, median `0.0075`, brier `0.2447`, calibration_gap `0.0623`
- 20d: hit_rate `0.6750`, avg `0.0072`, median `0.0158`, brier `0.2179`, calibration_gap `-0.0127`
- 60d: hit_rate `0.5875`, avg `0.0248`, median `0.0314`, brier `0.2525`, calibration_gap `0.0748`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.8125`, avg `0.0085`, median `0.0136`, brier `0.1863`, calibration_gap `-0.1829`
- 5d: hit_rate `0.8750`, avg `0.0147`, median `0.0126`, brier `0.1703`, calibration_gap `-0.2454`
- 10d: hit_rate `0.7500`, avg `0.0159`, median `0.0214`, brier `0.2033`, calibration_gap `-0.1204`
- 20d: hit_rate `0.7500`, avg `0.0168`, median `0.0171`, brier `0.2027`, calibration_gap `-0.1204`
- 60d: hit_rate `0.6250`, avg `0.0385`, median `0.0462`, brier `0.2345`, calibration_gap `0.0046`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
