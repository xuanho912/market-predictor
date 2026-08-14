# High Confidence Signal Report

Generated at: `2026-08-14T21:55:01.129684+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `20`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `2`
- 3d: hit_rate `1.0000`, avg `0.0159`, median `0.0159`, brier `0.0776`, calibration_gap `-0.2785`
- 5d: hit_rate `1.0000`, avg `0.0155`, median `0.0155`, brier `0.0776`, calibration_gap `-0.2785`
- 10d: hit_rate `1.0000`, avg `0.0234`, median `0.0234`, brier `0.0776`, calibration_gap `-0.2785`
- 20d: hit_rate `0.5000`, avg `0.0277`, median `0.0277`, brier `0.2937`, calibration_gap `0.2215`
- 60d: hit_rate `0.5000`, avg `0.0244`, median `0.0244`, brier `0.2937`, calibration_gap `0.2215`

### top_20_confidence_signals
- sample_size: `4`
- 3d: hit_rate `1.0000`, avg `0.0114`, median `0.0109`, brier `0.0812`, calibration_gap `-0.2849`
- 5d: hit_rate `1.0000`, avg `0.0113`, median `0.0120`, brier `0.0812`, calibration_gap `-0.2849`
- 10d: hit_rate `1.0000`, avg `0.0185`, median `0.0234`, brier `0.0812`, calibration_gap `-0.2849`
- 20d: hit_rate `0.5000`, avg `0.0162`, median `0.0086`, brier `0.2948`, calibration_gap `0.2151`
- 60d: hit_rate `0.5000`, avg `0.0223`, median `0.0237`, brier `0.2948`, calibration_gap `0.2151`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.5000`, avg `-0.0000`, median `-0.0009`, brier `0.2817`, calibration_gap `0.1894`
- 5d: hit_rate `0.5000`, avg `0.0023`, median `0.0007`, brier `0.2798`, calibration_gap `0.1894`
- 10d: hit_rate `0.6500`, avg `0.0043`, median `0.0074`, brier `0.2242`, calibration_gap `0.0394`
- 20d: hit_rate `0.7500`, avg `0.0127`, median `0.0237`, brier `0.1939`, calibration_gap `-0.0606`
- 60d: hit_rate `0.5000`, avg `0.0114`, median `0.0128`, brier `0.2853`, calibration_gap `0.1894`

### low_confidence_reference
- sample_size: `4`
- 3d: hit_rate `0.5000`, avg `-0.0000`, median `0.0031`, brier `0.2771`, calibration_gap `0.1713`
- 5d: hit_rate `0.2500`, avg `-0.0042`, median `-0.0053`, brier `0.3649`, calibration_gap `0.4213`
- 10d: hit_rate `0.2500`, avg `-0.0112`, median `-0.0127`, brier `0.3649`, calibration_gap `0.4213`
- 20d: hit_rate `0.7500`, avg `0.0021`, median `0.0194`, brier `0.1928`, calibration_gap `-0.0787`
- 60d: hit_rate `0.5000`, avg `0.0058`, median `0.0398`, brier `0.2771`, calibration_gap `0.1713`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
