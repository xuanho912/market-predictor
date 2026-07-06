# High Confidence Signal Report

Generated at: `2026-07-06T15:57:37.402604+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.0000`, avg `-0.0137`, median `-0.0097`, brier `0.5129`, calibration_gap `0.7159`
- 5d: hit_rate `0.2500`, avg `-0.0124`, median `-0.0114`, brier `0.4100`, calibration_gap `0.4659`
- 10d: hit_rate `0.2500`, avg `-0.0103`, median `-0.0128`, brier `0.4072`, calibration_gap `0.4659`
- 20d: hit_rate `0.5000`, avg `-0.0062`, median `-0.0053`, brier `0.2879`, calibration_gap `0.2159`
- 60d: hit_rate `0.2500`, avg `-0.0384`, median `-0.0651`, brier `0.3935`, calibration_gap `0.4659`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.2500`, avg `-0.0064`, median `-0.0040`, brier `0.4012`, calibration_gap `0.4581`
- 5d: hit_rate `0.5625`, avg `-0.0015`, median `0.0017`, brier `0.2745`, calibration_gap `0.1456`
- 10d: hit_rate `0.4375`, avg `0.0014`, median `-0.0010`, brier `0.3235`, calibration_gap `0.2706`
- 20d: hit_rate `0.6875`, avg `0.0111`, median `0.0145`, brier `0.2143`, calibration_gap `0.0206`
- 60d: hit_rate `0.4375`, avg `-0.0038`, median `-0.0282`, brier `0.3163`, calibration_gap `0.2706`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.3500`, avg `-0.0096`, median `-0.0101`, brier `0.3547`, calibration_gap `0.3491`
- 5d: hit_rate `0.3500`, avg `-0.0087`, median `-0.0066`, brier `0.3523`, calibration_gap `0.3491`
- 10d: hit_rate `0.2500`, avg `-0.0058`, median `-0.0087`, brier `0.3944`, calibration_gap `0.4491`
- 20d: hit_rate `0.7000`, avg `0.0164`, median `0.0209`, brier `0.2095`, calibration_gap `-0.0009`
- 60d: hit_rate `0.6000`, avg `0.0279`, median `0.0210`, brier `0.2485`, calibration_gap `0.0991`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0037`, median `0.0030`, brier `0.2345`, calibration_gap `0.0183`
- 5d: hit_rate `0.4375`, avg `-0.0048`, median `-0.0064`, brier `0.2897`, calibration_gap `0.2058`
- 10d: hit_rate `0.3750`, avg `-0.0055`, median `-0.0169`, brier `0.3070`, calibration_gap `0.2683`
- 20d: hit_rate `0.6875`, avg `-0.0036`, median `0.0031`, brier `0.2173`, calibration_gap `-0.0442`
- 60d: hit_rate `0.5000`, avg `0.0043`, median `0.0018`, brier `0.2712`, calibration_gap `0.1433`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
