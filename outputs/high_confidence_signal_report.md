# High Confidence Signal Report

Generated at: `2026-10-09T02:57:19.753446+00:00`

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
- 3d: hit_rate `0.3500`, avg `-0.0068`, median `-0.0045`, brier `0.3626`, calibration_gap `0.3604`
- 5d: hit_rate `0.4125`, avg `-0.0108`, median `-0.0132`, brier `0.3379`, calibration_gap `0.2979`
- 10d: hit_rate `0.4375`, avg `-0.0098`, median `-0.0070`, brier `0.3272`, calibration_gap `0.2729`
- 20d: hit_rate `0.5750`, avg `0.0087`, median `0.0157`, brier `0.2627`, calibration_gap `0.1354`
- 60d: hit_rate `0.7500`, avg `0.0307`, median `0.0463`, brier `0.1876`, calibration_gap `-0.0396`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0041`, median `0.0061`, brier `0.2189`, calibration_gap `-0.0322`
- 5d: hit_rate `0.7500`, avg `0.0003`, median `0.0040`, brier `0.2007`, calibration_gap `-0.0947`
- 10d: hit_rate `0.6875`, avg `0.0009`, median `0.0061`, brier `0.2203`, calibration_gap `-0.0322`
- 20d: hit_rate `0.5000`, avg `-0.0088`, median `-0.0005`, brier `0.2763`, calibration_gap `0.1553`
- 60d: hit_rate `0.6875`, avg `0.0129`, median `0.0290`, brier `0.2172`, calibration_gap `-0.0322`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
