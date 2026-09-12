# High Confidence Signal Report

Generated at: `2026-09-12T01:05:38.088823+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0092`, median `0.0116`, brier `0.1480`, calibration_gap `-0.1892`
- 5d: hit_rate `0.8750`, avg `0.0119`, median `0.0116`, brier `0.1556`, calibration_gap `-0.1892`
- 10d: hit_rate `0.7500`, avg `0.0094`, median `0.0074`, brier `0.2045`, calibration_gap `-0.0642`
- 20d: hit_rate `1.0000`, avg `0.0535`, median `0.0554`, brier `0.0991`, calibration_gap `-0.3142`
- 60d: hit_rate `0.8750`, avg `0.0775`, median `0.0753`, brier `0.1556`, calibration_gap `-0.1892`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0063`, median `0.0079`, brier `0.2083`, calibration_gap `-0.0247`
- 5d: hit_rate `0.7500`, avg `0.0085`, median `0.0116`, brier `0.1937`, calibration_gap `-0.0872`
- 10d: hit_rate `0.7500`, avg `0.0121`, median `0.0113`, brier `0.2019`, calibration_gap `-0.0872`
- 20d: hit_rate `0.9375`, avg `0.0480`, median `0.0535`, brier `0.1306`, calibration_gap `-0.2747`
- 60d: hit_rate `0.8750`, avg `0.0802`, median `0.0859`, brier `0.1590`, calibration_gap `-0.2122`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.7333`, avg `0.0086`, median `0.0128`, brier `0.2102`, calibration_gap `-0.1230`
- 5d: hit_rate `0.6833`, avg `0.0119`, median `0.0125`, brier `0.2212`, calibration_gap `-0.0730`
- 10d: hit_rate `0.7500`, avg `0.0185`, median `0.0178`, brier `0.2090`, calibration_gap `-0.1396`
- 20d: hit_rate `0.8667`, avg `0.0421`, median `0.0351`, brier `0.1802`, calibration_gap `-0.2563`
- 60d: hit_rate `0.8167`, avg `0.0734`, median `0.0914`, brier `0.1907`, calibration_gap `-0.2063`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0064`, median `-0.0111`, brier `0.2697`, calibration_gap `0.1914`
- 5d: hit_rate `0.5000`, avg `-0.0026`, median `-0.0027`, brier `0.2547`, calibration_gap `0.0664`
- 10d: hit_rate `0.5000`, avg `0.0093`, median `0.0098`, brier `0.2532`, calibration_gap `0.0664`
- 20d: hit_rate `0.8125`, avg `0.0325`, median `0.0176`, brier `0.2123`, calibration_gap `-0.2461`
- 60d: hit_rate `0.6250`, avg `0.0187`, median `0.0481`, brier `0.2385`, calibration_gap `-0.0586`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
