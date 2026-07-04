# High Confidence Signal Report

Generated at: `2026-07-04T04:56:11.096875+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `0.0040`, median `0.0074`, brier `0.3045`, calibration_gap `0.2319`
- 5d: hit_rate `0.2500`, avg `-0.0101`, median `-0.0108`, brier `0.4202`, calibration_gap `0.4819`
- 10d: hit_rate `0.3750`, avg `0.0037`, median `-0.0016`, brier `0.3573`, calibration_gap `0.3569`
- 20d: hit_rate `0.8750`, avg `0.0249`, median `0.0299`, brier `0.1288`, calibration_gap `-0.1431`
- 60d: hit_rate `1.0000`, avg `0.0819`, median `0.0890`, brier `0.0719`, calibration_gap `-0.2681`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `0.0007`, median `-0.0012`, brier `0.3284`, calibration_gap `0.2868`
- 5d: hit_rate `0.2500`, avg `-0.0105`, median `-0.0108`, brier `0.4125`, calibration_gap `0.4743`
- 10d: hit_rate `0.3125`, avg `0.0003`, median `-0.0018`, brier `0.3815`, calibration_gap `0.4118`
- 20d: hit_rate `0.8125`, avg `0.0221`, median `0.0287`, brier `0.1586`, calibration_gap `-0.0882`
- 60d: hit_rate `0.8750`, avg `0.0638`, median `0.0776`, brier `0.1302`, calibration_gap `-0.1507`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.4500`, avg `-0.0019`, median `-0.0017`, brier `0.3029`, calibration_gap `0.2176`
- 5d: hit_rate `0.3750`, avg `-0.0063`, median `-0.0130`, brier `0.3345`, calibration_gap `0.2926`
- 10d: hit_rate `0.4500`, avg `0.0010`, median `-0.0012`, brier `0.3082`, calibration_gap `0.2176`
- 20d: hit_rate `0.8250`, avg `0.0250`, median `0.0291`, brier `0.1732`, calibration_gap `-0.1574`
- 60d: hit_rate `0.7500`, avg `0.0431`, median `0.0635`, brier `0.1842`, calibration_gap `-0.0824`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `0.0001`, median `-0.0037`, brier `0.2843`, calibration_gap `0.2214`
- 5d: hit_rate `0.4375`, avg `-0.0011`, median `-0.0038`, brier `0.2750`, calibration_gap `0.1589`
- 10d: hit_rate `0.5625`, avg `0.0004`, median `0.0046`, brier `0.2493`, calibration_gap `0.0339`
- 20d: hit_rate `0.5000`, avg `0.0159`, median `0.0132`, brier `0.2599`, calibration_gap `0.0964`
- 60d: hit_rate `0.6875`, avg `0.0412`, median `0.0729`, brier `0.2279`, calibration_gap `-0.0911`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
