# High Confidence Signal Report

Generated at: `2026-06-19T00:14:28.628166+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0069`, median `-0.0015`, brier `0.3507`, calibration_gap `0.3460`
- 5d: hit_rate `0.1250`, avg `-0.0150`, median `-0.0176`, brier `0.4622`, calibration_gap `0.5960`
- 10d: hit_rate `0.8750`, avg `0.0123`, median `0.0135`, brier `0.1342`, calibration_gap `-0.1540`
- 20d: hit_rate `1.0000`, avg `0.0222`, median `0.0277`, brier `0.0779`, calibration_gap `-0.2790`
- 60d: hit_rate `0.6250`, avg `0.0242`, median `0.0380`, brier `0.2439`, calibration_gap `0.0960`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0007`, median `0.0002`, brier `0.2960`, calibration_gap `0.2092`
- 5d: hit_rate `0.2500`, avg `-0.0095`, median `-0.0130`, brier `0.4014`, calibration_gap `0.4592`
- 10d: hit_rate `0.6250`, avg `0.0063`, median `0.0061`, brier `0.2363`, calibration_gap `0.0842`
- 20d: hit_rate `0.8750`, avg `0.0190`, median `0.0233`, brier `0.1324`, calibration_gap `-0.1658`
- 60d: hit_rate `0.6875`, avg `0.0323`, median `0.0503`, brier `0.2168`, calibration_gap `0.0217`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.5500`, avg `0.0019`, median `0.0033`, brier `0.2624`, calibration_gap `0.1091`
- 5d: hit_rate `0.5250`, avg `0.0003`, median `0.0019`, brier `0.2763`, calibration_gap `0.1341`
- 10d: hit_rate `0.4750`, avg `0.0006`, median `-0.0017`, brier `0.2833`, calibration_gap `0.1841`
- 20d: hit_rate `0.6500`, avg `0.0041`, median `0.0158`, brier `0.2202`, calibration_gap `0.0091`
- 60d: hit_rate `0.6250`, avg `0.0237`, median `0.0328`, brier `0.2346`, calibration_gap `0.0341`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `0.0004`, median `-0.0039`, brier `0.2781`, calibration_gap `0.1801`
- 5d: hit_rate `0.4375`, avg `0.0007`, median `-0.0024`, brier `0.2779`, calibration_gap `0.1801`
- 10d: hit_rate `0.4375`, avg `-0.0028`, median `-0.0041`, brier `0.2787`, calibration_gap `0.1801`
- 20d: hit_rate `0.5625`, avg `-0.0020`, median `0.0028`, brier `0.2492`, calibration_gap `0.0551`
- 60d: hit_rate `0.6250`, avg `0.0181`, median `0.0192`, brier `0.2350`, calibration_gap `-0.0074`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
