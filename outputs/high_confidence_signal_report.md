# High Confidence Signal Report

Generated at: `2026-06-13T17:36:10.494759+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.2500`, avg `-0.0074`, median `-0.0040`, brier `0.4250`, calibration_gap `0.4875`
- 5d: hit_rate `0.5000`, avg `-0.0043`, median `-0.0020`, brier `0.3148`, calibration_gap `0.2375`
- 10d: hit_rate `0.5000`, avg `-0.0011`, median `0.0009`, brier `0.3100`, calibration_gap `0.2375`
- 20d: hit_rate `0.7500`, avg `0.0017`, median `0.0120`, brier `0.1845`, calibration_gap `-0.0125`
- 60d: hit_rate `0.2500`, avg `-0.0430`, median `-0.0650`, brier `0.4164`, calibration_gap `0.4875`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0084`, median `-0.0074`, brier `0.3885`, calibration_gap `0.4150`
- 5d: hit_rate `0.4375`, avg `-0.0067`, median `-0.0087`, brier `0.3336`, calibration_gap `0.2900`
- 10d: hit_rate `0.5000`, avg `-0.0001`, median `0.0009`, brier `0.3043`, calibration_gap `0.2275`
- 20d: hit_rate `0.7500`, avg `0.0094`, median `0.0142`, brier `0.1868`, calibration_gap `-0.0225`
- 60d: hit_rate `0.4375`, avg `-0.0091`, median `-0.0193`, brier `0.3302`, calibration_gap `0.2900`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4500`, avg `-0.0001`, median `-0.0017`, brier `0.3165`, calibration_gap `0.2428`
- 5d: hit_rate `0.5333`, avg `-0.0012`, median `0.0006`, brier `0.2799`, calibration_gap `0.1595`
- 10d: hit_rate `0.4500`, avg `0.0016`, median `-0.0018`, brier `0.3098`, calibration_gap `0.2428`
- 20d: hit_rate `0.6000`, avg `0.0064`, median `0.0120`, brier `0.2411`, calibration_gap `0.0928`
- 60d: hit_rate `0.5333`, avg `0.0147`, median `0.0151`, brier `0.2771`, calibration_gap `0.1595`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0103`, median `0.0065`, brier `0.2174`, calibration_gap `-0.0416`
- 5d: hit_rate `0.6250`, avg `0.0033`, median `0.0087`, brier `0.2356`, calibration_gap `0.0209`
- 10d: hit_rate `0.6250`, avg `0.0055`, median `0.0054`, brier `0.2338`, calibration_gap `0.0209`
- 20d: hit_rate `0.4375`, avg `0.0018`, median `-0.0029`, brier `0.2880`, calibration_gap `0.2084`
- 60d: hit_rate `0.4375`, avg `-0.0014`, median `-0.0024`, brier `0.2906`, calibration_gap `0.2084`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
