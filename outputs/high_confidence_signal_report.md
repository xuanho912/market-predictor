# High Confidence Signal Report

Generated at: `2026-09-29T02:35:08.070328+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0064`, median `0.0085`, brier `0.1896`, calibration_gap `0.0827`
- 5d: hit_rate `0.7500`, avg `0.0022`, median `0.0068`, brier `0.1896`, calibration_gap `0.0827`
- 10d: hit_rate `0.6250`, avg `-0.0008`, median `0.0041`, brier `0.2789`, calibration_gap `0.2077`
- 20d: hit_rate `0.7500`, avg `0.0247`, median `0.0324`, brier `0.1943`, calibration_gap `0.0827`
- 60d: hit_rate `1.0000`, avg `0.0540`, median `0.0565`, brier `0.0281`, calibration_gap `-0.1673`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0043`, median `0.0088`, brier `0.2295`, calibration_gap `0.1341`
- 5d: hit_rate `0.6875`, avg `0.0043`, median `0.0076`, brier `0.2295`, calibration_gap `0.1341`
- 10d: hit_rate `0.6875`, avg `0.0010`, median `0.0060`, brier `0.2351`, calibration_gap `0.1341`
- 20d: hit_rate `0.7500`, avg `0.0164`, median `0.0173`, brier `0.1929`, calibration_gap `0.0716`
- 60d: hit_rate `0.9375`, avg `0.0643`, median `0.0625`, brier `0.0708`, calibration_gap `-0.1159`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5500`, avg `0.0009`, median `0.0030`, brier `0.2782`, calibration_gap `0.1877`
- 5d: hit_rate `0.6250`, avg `-0.0021`, median `0.0031`, brier `0.2526`, calibration_gap `0.1127`
- 10d: hit_rate `0.6250`, avg `0.0012`, median `0.0061`, brier `0.2572`, calibration_gap `0.1127`
- 20d: hit_rate `0.7500`, avg `0.0177`, median `0.0243`, brier `0.2080`, calibration_gap `-0.0123`
- 60d: hit_rate `0.8750`, avg `0.0497`, median `0.0557`, brier `0.1361`, calibration_gap `-0.1373`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0015`, median `-0.0027`, brier `0.2947`, calibration_gap `0.2171`
- 5d: hit_rate `0.5000`, avg `-0.0062`, median `-0.0003`, brier `0.2735`, calibration_gap `0.1546`
- 10d: hit_rate `0.5625`, avg `0.0014`, median `0.0141`, brier `0.2561`, calibration_gap `0.0921`
- 20d: hit_rate `0.7500`, avg `0.0236`, median `0.0322`, brier `0.1988`, calibration_gap `-0.0954`
- 60d: hit_rate `0.8750`, avg `0.0505`, median `0.0604`, brier `0.1578`, calibration_gap `-0.2204`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
