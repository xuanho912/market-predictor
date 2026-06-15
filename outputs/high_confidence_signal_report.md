# High Confidence Signal Report

Generated at: `2026-06-15T14:29:10.103279+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0039`, median `0.0002`, brier `0.2909`, calibration_gap `0.2130`
- 5d: hit_rate `0.3750`, avg `-0.0080`, median `-0.0157`, brier `0.3475`, calibration_gap `0.3380`
- 10d: hit_rate `0.8750`, avg `0.0096`, median `0.0075`, brier `0.1374`, calibration_gap `-0.1620`
- 20d: hit_rate `0.8750`, avg `0.0139`, median `0.0142`, brier `0.1339`, calibration_gap `-0.1620`
- 60d: hit_rate `0.3750`, avg `-0.0148`, median `-0.0282`, brier `0.3497`, calibration_gap `0.3380`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0038`, median `0.0002`, brier `0.2878`, calibration_gap `0.2015`
- 5d: hit_rate `0.3125`, avg `-0.0087`, median `-0.0104`, brier `0.3643`, calibration_gap `0.3890`
- 10d: hit_rate `0.8125`, avg `0.0093`, median `0.0103`, brier `0.1650`, calibration_gap `-0.1110`
- 20d: hit_rate `0.7500`, avg `0.0100`, median `0.0143`, brier `0.1870`, calibration_gap `-0.0485`
- 60d: hit_rate `0.5000`, avg `0.0076`, median `0.0064`, brier `0.2936`, calibration_gap `0.2015`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6375`, avg `0.0049`, median `0.0058`, brier `0.2368`, calibration_gap `0.0236`
- 5d: hit_rate `0.6375`, avg `0.0057`, median `0.0056`, brier `0.2398`, calibration_gap `0.0236`
- 10d: hit_rate `0.6000`, avg `0.0078`, median `0.0075`, brier `0.2425`, calibration_gap `0.0611`
- 20d: hit_rate `0.7000`, avg `0.0109`, median `0.0177`, brier `0.2087`, calibration_gap `-0.0389`
- 60d: hit_rate `0.5875`, avg `0.0290`, median `0.0338`, brier `0.2503`, calibration_gap `0.0736`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0056`, median `0.0118`, brier `0.2354`, calibration_gap `0.0016`
- 5d: hit_rate `0.6250`, avg `0.0045`, median `0.0079`, brier `0.2354`, calibration_gap `0.0016`
- 10d: hit_rate `0.5625`, avg `0.0011`, median `0.0077`, brier `0.2499`, calibration_gap `0.0641`
- 20d: hit_rate `0.5625`, avg `0.0023`, median `0.0183`, brier `0.2508`, calibration_gap `0.0641`
- 60d: hit_rate `0.5000`, avg `0.0260`, median `0.0115`, brier `0.2668`, calibration_gap `0.1266`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
