# High Confidence Signal Report

Generated at: `2026-08-04T14:42:18.749828+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0049`, median `-0.0023`, brier `0.3078`, calibration_gap `0.2354`
- 5d: hit_rate `0.8750`, avg `0.0056`, median `0.0069`, brier `0.1360`, calibration_gap `-0.1396`
- 10d: hit_rate `0.3750`, avg `-0.0008`, median `-0.0071`, brier `0.3662`, calibration_gap `0.3604`
- 20d: hit_rate `0.3750`, avg `-0.0057`, median `-0.0114`, brier `0.3607`, calibration_gap `0.3604`
- 60d: hit_rate `0.3750`, avg `-0.0180`, median `-0.0274`, brier `0.3607`, calibration_gap `0.3604`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0028`, median `-0.0005`, brier `0.3026`, calibration_gap `0.2267`
- 5d: hit_rate `0.7500`, avg `0.0010`, median `0.0047`, brier `0.1898`, calibration_gap `-0.0233`
- 10d: hit_rate `0.3750`, avg `-0.0026`, median `-0.0088`, brier `0.3591`, calibration_gap `0.3517`
- 20d: hit_rate `0.4375`, avg `-0.0086`, median `-0.0044`, brier `0.3292`, calibration_gap `0.2892`
- 60d: hit_rate `0.3125`, avg `-0.0153`, median `-0.0274`, brier `0.3837`, calibration_gap `0.4142`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6667`, avg `0.0047`, median `0.0061`, brier `0.2258`, calibration_gap `0.0319`
- 5d: hit_rate `0.7500`, avg `0.0066`, median `0.0077`, brier `0.1891`, calibration_gap `-0.0515`
- 10d: hit_rate `0.5333`, avg `0.0051`, median `0.0027`, brier `0.2765`, calibration_gap `0.1652`
- 20d: hit_rate `0.6500`, avg `0.0036`, median `0.0105`, brier `0.2301`, calibration_gap `0.0485`
- 60d: hit_rate `0.5500`, avg `0.0104`, median `0.0211`, brier `0.2740`, calibration_gap `0.1485`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0048`, median `0.0077`, brier `0.2163`, calibration_gap `-0.0106`
- 5d: hit_rate `0.7500`, avg `0.0036`, median `0.0071`, brier `0.1933`, calibration_gap `-0.0731`
- 10d: hit_rate `0.5000`, avg `-0.0052`, median `-0.0035`, brier `0.2802`, calibration_gap `0.1769`
- 20d: hit_rate `0.5000`, avg `-0.0216`, median `-0.0075`, brier `0.2818`, calibration_gap `0.1769`
- 60d: hit_rate `0.6250`, avg `-0.0041`, median `0.0542`, brier `0.2356`, calibration_gap `0.0519`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
