# High Confidence Signal Report

Generated at: `2026-08-14T23:33:55.139223+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `20`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `2`
- 3d: hit_rate `1.0000`, avg `0.0080`, median `0.0080`, brier `0.0699`, calibration_gap `-0.2643`
- 5d: hit_rate `1.0000`, avg `0.0147`, median `0.0147`, brier `0.0699`, calibration_gap `-0.2643`
- 10d: hit_rate `1.0000`, avg `0.0199`, median `0.0199`, brier `0.0699`, calibration_gap `-0.2643`
- 20d: hit_rate `0.0000`, avg `-0.0184`, median `-0.0184`, brier `0.5412`, calibration_gap `0.7357`
- 60d: hit_rate `0.0000`, avg `-0.0398`, median `-0.0398`, brier `0.5412`, calibration_gap `0.7357`

### top_20_confidence_signals
- sample_size: `4`
- 3d: hit_rate `1.0000`, avg `0.0085`, median `0.0080`, brier `0.0751`, calibration_gap `-0.2738`
- 5d: hit_rate `1.0000`, avg `0.0130`, median `0.0112`, brier `0.0751`, calibration_gap `-0.2738`
- 10d: hit_rate `1.0000`, avg `0.0163`, median `0.0164`, brier `0.0751`, calibration_gap `-0.2738`
- 20d: hit_rate `0.5000`, avg `-0.0008`, median `-0.0036`, brier `0.3108`, calibration_gap `0.2262`
- 60d: hit_rate `0.2500`, avg `-0.0069`, median `-0.0336`, brier `0.4155`, calibration_gap `0.4762`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.5000`, avg `-0.0033`, median `-0.0005`, brier `0.2833`, calibration_gap `0.1986`
- 5d: hit_rate `0.7500`, avg `0.0029`, median `0.0048`, brier `0.1873`, calibration_gap `-0.0514`
- 10d: hit_rate `0.4500`, avg `0.0005`, median `-0.0009`, brier `0.3012`, calibration_gap `0.2486`
- 20d: hit_rate `0.6000`, avg `-0.0029`, median `0.0101`, brier `0.2520`, calibration_gap `0.0986`
- 60d: hit_rate `0.4000`, avg `-0.0048`, median `-0.0178`, brier `0.3315`, calibration_gap `0.2986`

### low_confidence_reference
- sample_size: `4`
- 3d: hit_rate `0.0000`, avg `-0.0175`, median `-0.0115`, brier `0.4695`, calibration_gap `0.6852`
- 5d: hit_rate `0.7500`, avg `-0.0018`, median `0.0013`, brier `0.1912`, calibration_gap `-0.0648`
- 10d: hit_rate `0.0000`, avg `-0.0211`, median `-0.0214`, brier `0.4695`, calibration_gap `0.6852`
- 20d: hit_rate `0.0000`, avg `-0.0586`, median `-0.0560`, brier `0.4695`, calibration_gap `0.6852`
- 60d: hit_rate `0.2500`, avg `-0.0401`, median `-0.0577`, brier `0.3774`, calibration_gap `0.4352`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
