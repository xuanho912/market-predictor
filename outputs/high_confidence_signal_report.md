# High Confidence Signal Report

Generated at: `2026-09-02T01:01:10.649942+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0013`, median `0.0014`, brier `0.2655`, calibration_gap `0.1923`
- 5d: hit_rate `0.6250`, avg `-0.0006`, median `0.0010`, brier `0.2710`, calibration_gap `0.1923`
- 10d: hit_rate `0.3750`, avg `-0.0015`, median `-0.0073`, brier `0.4410`, calibration_gap `0.4423`
- 20d: hit_rate `0.6250`, avg `0.0172`, median `0.0254`, brier `0.2773`, calibration_gap `0.1923`
- 60d: hit_rate `0.8750`, avg `0.0586`, median `0.0630`, brier `0.1158`, calibration_gap `-0.0577`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0031`, median `-0.0026`, brier `0.3675`, calibration_gap `0.3621`
- 5d: hit_rate `0.3750`, avg `-0.0078`, median `-0.0084`, brier `0.4065`, calibration_gap `0.4246`
- 10d: hit_rate `0.4375`, avg `-0.0010`, median `-0.0073`, brier `0.3857`, calibration_gap `0.3621`
- 20d: hit_rate `0.6875`, avg `0.0089`, median `0.0244`, brier `0.2340`, calibration_gap `0.1121`
- 60d: hit_rate `0.8125`, avg `0.0537`, median `0.0718`, brier `0.1532`, calibration_gap `-0.0129`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4667`, avg `-0.0007`, median `-0.0016`, brier `0.3282`, calibration_gap `0.2823`
- 5d: hit_rate `0.5000`, avg `-0.0038`, median `-0.0011`, brier `0.3144`, calibration_gap `0.2489`
- 10d: hit_rate `0.4167`, avg `-0.0001`, median `-0.0066`, brier `0.3564`, calibration_gap `0.3323`
- 20d: hit_rate `0.6500`, avg `0.0147`, median `0.0205`, brier `0.2388`, calibration_gap `0.0989`
- 60d: hit_rate `0.7667`, avg `0.0509`, median `0.0626`, brier `0.1867`, calibration_gap `-0.0177`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0020`, median `-0.0045`, brier `0.3092`, calibration_gap `0.2536`
- 5d: hit_rate `0.3750`, avg `-0.0028`, median `-0.0052`, brier `0.3367`, calibration_gap `0.3161`
- 10d: hit_rate `0.3750`, avg `-0.0026`, median `-0.0092`, brier `0.3364`, calibration_gap `0.3161`
- 20d: hit_rate `0.5625`, avg `0.0166`, median `0.0011`, brier `0.2654`, calibration_gap `0.1286`
- 60d: hit_rate `1.0000`, avg `0.0684`, median `0.0596`, brier `0.0956`, calibration_gap `-0.3089`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
