# High Confidence Signal Report

Generated at: `2026-07-09T15:37:24.309735+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0104`, median `-0.0054`, brier `0.3599`, calibration_gap `0.3488`
- 5d: hit_rate `0.3750`, avg `-0.0100`, median `-0.0130`, brier `0.3584`, calibration_gap `0.3488`
- 10d: hit_rate `0.3750`, avg `-0.0036`, median `-0.0038`, brier `0.3621`, calibration_gap `0.3488`
- 20d: hit_rate `1.0000`, avg `0.0288`, median `0.0302`, brier `0.0765`, calibration_gap `-0.2762`
- 60d: hit_rate `1.0000`, avg `0.0730`, median `0.0761`, brier `0.0765`, calibration_gap `-0.2762`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0055`, median `-0.0003`, brier `0.3004`, calibration_gap `0.2158`
- 5d: hit_rate `0.4375`, avg `-0.0066`, median `-0.0104`, brier `0.3261`, calibration_gap `0.2783`
- 10d: hit_rate `0.5000`, avg `0.0018`, median `0.0035`, brier `0.3012`, calibration_gap `0.2158`
- 20d: hit_rate `0.8750`, avg `0.0179`, median `0.0237`, brier `0.1326`, calibration_gap `-0.1592`
- 60d: hit_rate `0.6875`, avg `0.0313`, median `0.0449`, brier `0.2104`, calibration_gap `0.0283`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.4875`, avg `-0.0012`, median `-0.0005`, brier `0.2941`, calibration_gap `0.1983`
- 5d: hit_rate `0.5000`, avg `-0.0030`, median `-0.0001`, brier `0.2876`, calibration_gap `0.1858`
- 10d: hit_rate `0.4750`, avg `0.0013`, median `-0.0014`, brier `0.3008`, calibration_gap `0.2108`
- 20d: hit_rate `0.6750`, avg `0.0044`, median `0.0115`, brier `0.2192`, calibration_gap `0.0108`
- 60d: hit_rate `0.5500`, avg `0.0132`, median `0.0152`, brier `0.2655`, calibration_gap `0.1358`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0034`, median `0.0037`, brier `0.2353`, calibration_gap `0.0271`
- 5d: hit_rate `0.5000`, avg `-0.0002`, median `0.0028`, brier `0.2740`, calibration_gap `0.1521`
- 10d: hit_rate `0.6875`, avg `0.0132`, median `0.0123`, brier `0.2178`, calibration_gap `-0.0354`
- 20d: hit_rate `0.8125`, avg `0.0115`, median `0.0143`, brier `0.1783`, calibration_gap `-0.1604`
- 60d: hit_rate `0.5625`, avg `0.0179`, median `0.0201`, brier `0.2547`, calibration_gap `0.0896`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
