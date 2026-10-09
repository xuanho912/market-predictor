# High Confidence Signal Report

Generated at: `2026-10-09T01:25:47.374315+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0014`, median `0.0031`, brier `0.2635`, calibration_gap `0.1681`
- 5d: hit_rate `0.6250`, avg `-0.0019`, median `0.0056`, brier `0.2635`, calibration_gap `0.1681`
- 10d: hit_rate `0.3750`, avg `-0.0093`, median `-0.0116`, brier `0.4122`, calibration_gap `0.4181`
- 20d: hit_rate `0.8750`, avg `0.0255`, median `0.0258`, brier `0.1195`, calibration_gap `-0.0819`
- 60d: hit_rate `1.0000`, avg `0.0379`, median `0.0415`, brier `0.0429`, calibration_gap `-0.2069`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0043`, median `-0.0036`, brier `0.3623`, calibration_gap `0.3458`
- 5d: hit_rate `0.4375`, avg `-0.0079`, median `-0.0143`, brier `0.3623`, calibration_gap `0.3458`
- 10d: hit_rate `0.5625`, avg `-0.0056`, median `0.0003`, brier `0.3000`, calibration_gap `0.2208`
- 20d: hit_rate `0.6250`, avg `0.0143`, median `0.0173`, brier `0.2568`, calibration_gap `0.1583`
- 60d: hit_rate `0.8125`, avg `0.0359`, median `0.0501`, brier `0.1517`, calibration_gap `-0.0292`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.4375`, avg `-0.0029`, median `-0.0023`, brier `0.3252`, calibration_gap `0.2250`
- 5d: hit_rate `0.4250`, avg `-0.0048`, median `-0.0110`, brier `0.3188`, calibration_gap `0.2375`
- 10d: hit_rate `0.5250`, avg `-0.0005`, median `0.0010`, brier `0.2906`, calibration_gap `0.1375`
- 20d: hit_rate `0.7250`, avg `0.0294`, median `0.0290`, brier `0.2334`, calibration_gap `-0.0625`
- 60d: hit_rate `0.8375`, avg `0.0694`, median `0.0843`, brier `0.1713`, calibration_gap `-0.1750`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0039`, median `0.0081`, brier `0.2350`, calibration_gap `-0.0765`
- 5d: hit_rate `0.5625`, avg `0.0063`, median `0.0108`, brier `0.2407`, calibration_gap `-0.0140`
- 10d: hit_rate `0.6250`, avg `0.0168`, median `0.0036`, brier `0.2422`, calibration_gap `-0.0765`
- 20d: hit_rate `0.9375`, avg `0.0511`, median `0.0300`, brier `0.2086`, calibration_gap `-0.3890`
- 60d: hit_rate `0.6875`, avg `0.0843`, median `0.1097`, brier `0.2349`, calibration_gap `-0.1390`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
