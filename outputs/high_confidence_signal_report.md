# High Confidence Signal Report

Generated at: `2026-06-15T14:41:14.538218+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0039`, median `0.0002`, brier `0.2912`, calibration_gap `0.2132`
- 5d: hit_rate `0.3750`, avg `-0.0080`, median `-0.0157`, brier `0.3476`, calibration_gap `0.3382`
- 10d: hit_rate `0.8750`, avg `0.0096`, median `0.0075`, brier `0.1375`, calibration_gap `-0.1618`
- 20d: hit_rate `0.8750`, avg `0.0139`, median `0.0142`, brier `0.1339`, calibration_gap `-0.1618`
- 60d: hit_rate `0.3750`, avg `-0.0148`, median `-0.0282`, brier `0.3498`, calibration_gap `0.3382`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0038`, median `0.0002`, brier `0.2879`, calibration_gap `0.2017`
- 5d: hit_rate `0.3125`, avg `-0.0087`, median `-0.0104`, brier `0.3644`, calibration_gap `0.3892`
- 10d: hit_rate `0.8125`, avg `0.0093`, median `0.0103`, brier `0.1651`, calibration_gap `-0.1108`
- 20d: hit_rate `0.7500`, avg `0.0100`, median `0.0143`, brier `0.1871`, calibration_gap `-0.0483`
- 60d: hit_rate `0.5000`, avg `0.0076`, median `0.0064`, brier `0.2937`, calibration_gap `0.2017`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6375`, avg `0.0049`, median `0.0058`, brier `0.2369`, calibration_gap `0.0240`
- 5d: hit_rate `0.6375`, avg `0.0057`, median `0.0056`, brier `0.2398`, calibration_gap `0.0240`
- 10d: hit_rate `0.5875`, avg `0.0070`, median `0.0072`, brier `0.2458`, calibration_gap `0.0740`
- 20d: hit_rate `0.6875`, avg `0.0094`, median `0.0171`, brier `0.2119`, calibration_gap `-0.0260`
- 60d: hit_rate `0.5875`, avg `0.0281`, median `0.0338`, brier `0.2505`, calibration_gap `0.0740`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0055`, median `0.0118`, brier `0.2353`, calibration_gap `0.0021`
- 5d: hit_rate `0.6250`, avg `0.0045`, median `0.0079`, brier `0.2353`, calibration_gap `0.0021`
- 10d: hit_rate `0.5000`, avg `-0.0025`, median `0.0002`, brier `0.2656`, calibration_gap `0.1271`
- 20d: hit_rate `0.5000`, avg `-0.0050`, median `0.0020`, brier `0.2667`, calibration_gap `0.1271`
- 60d: hit_rate `0.5000`, avg `0.0216`, median `0.0115`, brier `0.2672`, calibration_gap `0.1271`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
