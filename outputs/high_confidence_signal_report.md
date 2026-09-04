# High Confidence Signal Report

Generated at: `2026-09-04T00:58:06.275703+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0002`, median `0.0136`, brier `0.1979`, calibration_gap `-0.0681`
- 5d: hit_rate `0.7500`, avg `0.0073`, median `0.0179`, brier `0.1979`, calibration_gap `-0.0681`
- 10d: hit_rate `0.7500`, avg `0.0256`, median `0.0416`, brier `0.1979`, calibration_gap `-0.0681`
- 20d: hit_rate `0.7500`, avg `0.0350`, median `0.0514`, brier `0.1979`, calibration_gap `-0.0681`
- 60d: hit_rate `0.6250`, avg `0.0469`, median `0.0654`, brier `0.2459`, calibration_gap `0.0569`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0052`, median `0.0153`, brier `0.1948`, calibration_gap `-0.0796`
- 5d: hit_rate `0.6875`, avg `0.0084`, median `0.0157`, brier `0.2165`, calibration_gap `-0.0171`
- 10d: hit_rate `0.6875`, avg `0.0193`, median `0.0214`, brier `0.2149`, calibration_gap `-0.0171`
- 20d: hit_rate `0.8125`, avg `0.0327`, median `0.0441`, brier `0.1760`, calibration_gap `-0.1421`
- 60d: hit_rate `0.6250`, avg `0.0291`, median `0.0400`, brier `0.2398`, calibration_gap `0.0454`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6625`, avg `0.0052`, median `0.0093`, brier `0.2227`, calibration_gap `-0.0484`
- 5d: hit_rate `0.6750`, avg `0.0088`, median `0.0118`, brier `0.2218`, calibration_gap `-0.0609`
- 10d: hit_rate `0.6500`, avg `0.0125`, median `0.0184`, brier `0.2297`, calibration_gap `-0.0359`
- 20d: hit_rate `0.8000`, avg `0.0251`, median `0.0291`, brier `0.1945`, calibration_gap `-0.1859`
- 60d: hit_rate `0.7250`, avg `0.0444`, median `0.0631`, brier `0.2153`, calibration_gap `-0.1109`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0027`, median `0.0026`, brier `0.2476`, calibration_gap `0.0144`
- 5d: hit_rate `0.5625`, avg `0.0049`, median `0.0057`, brier `0.2477`, calibration_gap `0.0144`
- 10d: hit_rate `0.6250`, avg `0.0065`, median `0.0087`, brier `0.2382`, calibration_gap `-0.0481`
- 20d: hit_rate `0.6875`, avg `0.0140`, median `0.0209`, brier `0.2272`, calibration_gap `-0.1106`
- 60d: hit_rate `0.6875`, avg `0.0355`, median `0.0588`, brier `0.2282`, calibration_gap `-0.1106`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
