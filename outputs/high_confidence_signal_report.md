# High Confidence Signal Report

Generated at: `2026-10-03T00:51:16.800079+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0087`, median `0.0124`, brier `0.1927`, calibration_gap `0.0379`
- 5d: hit_rate `0.7500`, avg `0.0081`, median `0.0133`, brier `0.1927`, calibration_gap `0.0379`
- 10d: hit_rate `1.0000`, avg `0.0117`, median `0.0097`, brier `0.0452`, calibration_gap `-0.2121`
- 20d: hit_rate `0.7500`, avg `0.0240`, median `0.0258`, brier `0.1927`, calibration_gap `0.0379`
- 60d: hit_rate `1.0000`, avg `0.0991`, median `0.0940`, brier `0.0452`, calibration_gap `-0.2121`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0050`, median `0.0116`, brier `0.2157`, calibration_gap `0.0655`
- 5d: hit_rate `0.6875`, avg `0.0058`, median `0.0089`, brier `0.2135`, calibration_gap `0.0655`
- 10d: hit_rate `0.7500`, avg `0.0063`, median `0.0083`, brier `0.1651`, calibration_gap `0.0030`
- 20d: hit_rate `0.8750`, avg `0.0341`, median `0.0424`, brier `0.1366`, calibration_gap `-0.1220`
- 60d: hit_rate `0.9375`, avg `0.0930`, median `0.0940`, brier `0.0860`, calibration_gap `-0.1845`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5167`, avg `0.0006`, median `0.0008`, brier `0.2598`, calibration_gap `0.1186`
- 5d: hit_rate `0.5167`, avg `0.0018`, median `0.0031`, brier `0.2553`, calibration_gap `0.1186`
- 10d: hit_rate `0.6500`, avg `0.0073`, median `0.0081`, brier `0.2204`, calibration_gap `-0.0147`
- 20d: hit_rate `0.8167`, avg `0.0327`, median `0.0322`, brier `0.1944`, calibration_gap `-0.1814`
- 60d: hit_rate `0.9000`, avg `0.0812`, median `0.0896`, brier `0.1548`, calibration_gap `-0.2647`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0009`, median `-0.0017`, brier `0.2516`, calibration_gap `0.0329`
- 5d: hit_rate `0.4375`, avg `0.0042`, median `-0.0064`, brier `0.2522`, calibration_gap `0.0954`
- 10d: hit_rate `0.6875`, avg `0.0141`, median `0.0162`, brier `0.2381`, calibration_gap `-0.1546`
- 20d: hit_rate `0.8125`, avg `0.0399`, median `0.0318`, brier `0.2285`, calibration_gap `-0.2796`
- 60d: hit_rate `0.8125`, avg `0.0769`, median `0.0743`, brier `0.2273`, calibration_gap `-0.2796`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
