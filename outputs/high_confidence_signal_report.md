# High Confidence Signal Report

Generated at: `2026-09-18T16:27:39.656398+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0024`, median `0.0100`, brier `0.1897`, calibration_gap `0.0763`
- 5d: hit_rate `0.6250`, avg `-0.0038`, median `0.0010`, brier `0.2740`, calibration_gap `0.2013`
- 10d: hit_rate `0.5000`, avg `-0.0012`, median `-0.0018`, brier `0.3591`, calibration_gap `0.3263`
- 20d: hit_rate `0.6250`, avg `0.0219`, median `0.0293`, brier `0.2739`, calibration_gap `0.2013`
- 60d: hit_rate `0.7500`, avg `0.0439`, median `0.0588`, brier `0.1938`, calibration_gap `0.0763`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0010`, median `0.0034`, brier `0.2267`, calibration_gap `0.1260`
- 5d: hit_rate `0.6250`, avg `-0.0014`, median `0.0040`, brier `0.2689`, calibration_gap `0.1885`
- 10d: hit_rate `0.4375`, avg `-0.0054`, median `-0.0039`, brier `0.3864`, calibration_gap `0.3760`
- 20d: hit_rate `0.6875`, avg `0.0270`, median `0.0358`, brier `0.2318`, calibration_gap `0.1260`
- 60d: hit_rate `0.8750`, avg `0.0554`, median `0.0618`, brier `0.1168`, calibration_gap `-0.0615`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.6500`, avg `0.0017`, median `0.0091`, brier `0.2263`, calibration_gap `0.0281`
- 5d: hit_rate `0.7500`, avg `0.0040`, median `0.0062`, brier `0.1909`, calibration_gap `-0.0719`
- 10d: hit_rate `0.6500`, avg `0.0122`, median `0.0121`, brier `0.2269`, calibration_gap `0.0281`
- 20d: hit_rate `0.7000`, avg `0.0210`, median `0.0127`, brier `0.2097`, calibration_gap `-0.0219`
- 60d: hit_rate `0.8000`, avg `0.0654`, median `0.0630`, brier `0.1744`, calibration_gap `-0.1220`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0062`, median `-0.0116`, brier `0.3258`, calibration_gap `0.2992`
- 5d: hit_rate `0.5625`, avg `-0.0056`, median `0.0008`, brier `0.2597`, calibration_gap `0.1117`
- 10d: hit_rate `0.5000`, avg `0.0040`, median `0.0016`, brier `0.2805`, calibration_gap `0.1742`
- 20d: hit_rate `0.6875`, avg `0.0276`, median `0.0133`, brier `0.2133`, calibration_gap `-0.0133`
- 60d: hit_rate `0.8750`, avg `0.0788`, median `0.0897`, brier `0.1479`, calibration_gap `-0.2008`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
