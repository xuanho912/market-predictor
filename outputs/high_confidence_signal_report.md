# High Confidence Signal Report

Generated at: `2026-09-10T16:27:27.473269+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0012`, median `0.0014`, brier `0.2600`, calibration_gap `0.1737`
- 5d: hit_rate `0.6250`, avg `0.0010`, median `0.0010`, brier `0.2658`, calibration_gap `0.1737`
- 10d: hit_rate `0.1250`, avg `-0.0157`, median `-0.0204`, brier `0.5657`, calibration_gap `0.6737`
- 20d: hit_rate `0.3750`, avg `-0.0101`, median `-0.0055`, brier `0.4192`, calibration_gap `0.4237`
- 60d: hit_rate `0.6250`, avg `0.0221`, median `0.0453`, brier `0.2624`, calibration_gap `0.1737`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0056`, median `0.0038`, brier `0.2244`, calibration_gap `0.0950`
- 5d: hit_rate `0.7500`, avg `0.0035`, median `0.0039`, brier `0.1937`, calibration_gap `0.0325`
- 10d: hit_rate `0.3125`, avg `-0.0095`, median `-0.0200`, brier `0.4424`, calibration_gap `0.4700`
- 20d: hit_rate `0.6250`, avg `0.0019`, median `0.0142`, brier `0.2704`, calibration_gap `0.1575`
- 60d: hit_rate `0.6250`, avg `0.0247`, median `0.0535`, brier `0.2584`, calibration_gap `0.1575`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.6500`, avg `0.0085`, median `0.0114`, brier `0.2279`, calibration_gap `0.0144`
- 5d: hit_rate `0.7000`, avg `0.0113`, median `0.0109`, brier `0.2119`, calibration_gap `-0.0356`
- 10d: hit_rate `0.7000`, avg `0.0166`, median `0.0188`, brier `0.2109`, calibration_gap `-0.0356`
- 20d: hit_rate `0.8000`, avg `0.0329`, median `0.0271`, brier `0.1773`, calibration_gap `-0.1356`
- 60d: hit_rate `0.9000`, avg `0.0803`, median `0.0878`, brier `0.1457`, calibration_gap `-0.2356`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0111`, median `0.0131`, brier `0.2140`, calibration_gap `-0.0266`
- 5d: hit_rate `0.7500`, avg `0.0155`, median `0.0156`, brier `0.1948`, calibration_gap `-0.0891`
- 10d: hit_rate `0.6875`, avg `0.0179`, median `0.0159`, brier `0.2163`, calibration_gap `-0.0266`
- 20d: hit_rate `0.8125`, avg `0.0322`, median `0.0216`, brier `0.1743`, calibration_gap `-0.1516`
- 60d: hit_rate `0.8750`, avg `0.0715`, median `0.0619`, brier `0.1562`, calibration_gap `-0.2141`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
