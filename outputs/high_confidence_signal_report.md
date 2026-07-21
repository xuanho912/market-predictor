# High Confidence Signal Report

Generated at: `2026-07-21T04:35:38.936943+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0024`, median `0.0014`, brier `0.1878`, calibration_gap `0.0325`
- 5d: hit_rate `0.5000`, avg `-0.0019`, median `-0.0009`, brier `0.3250`, calibration_gap `0.2825`
- 10d: hit_rate `0.2500`, avg `-0.0095`, median `-0.0136`, brier `0.4737`, calibration_gap `0.5325`
- 20d: hit_rate `0.5000`, avg `0.0026`, median `0.0084`, brier `0.3298`, calibration_gap `0.2825`
- 60d: hit_rate `0.7500`, avg `0.0389`, median `0.0588`, brier `0.1885`, calibration_gap `0.0325`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `-0.0011`, median `0.0011`, brier `0.2523`, calibration_gap `0.1458`
- 5d: hit_rate `0.5000`, avg `-0.0064`, median `-0.0009`, brier `0.3209`, calibration_gap `0.2708`
- 10d: hit_rate `0.3750`, avg `-0.0078`, median `-0.0127`, brier `0.3950`, calibration_gap `0.3958`
- 20d: hit_rate `0.5625`, avg `0.0045`, median `0.0138`, brier `0.2903`, calibration_gap `0.2083`
- 60d: hit_rate `0.5625`, avg `0.0186`, median `0.0396`, brier `0.2842`, calibration_gap `0.2083`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5667`, avg `-0.0005`, median `0.0011`, brier `0.2695`, calibration_gap `0.1458`
- 5d: hit_rate `0.5500`, avg `0.0011`, median `0.0036`, brier `0.2781`, calibration_gap `0.1624`
- 10d: hit_rate `0.4833`, avg `0.0044`, median `-0.0003`, brier `0.3101`, calibration_gap `0.2291`
- 20d: hit_rate `0.6833`, avg `0.0204`, median `0.0324`, brier `0.2185`, calibration_gap `0.0291`
- 60d: hit_rate `0.6833`, avg `0.0382`, median `0.0714`, brier `0.2164`, calibration_gap `0.0291`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `0.0007`, median `-0.0121`, brier `0.3083`, calibration_gap `0.2517`
- 5d: hit_rate `0.5625`, avg `0.0060`, median `0.0065`, brier `0.2611`, calibration_gap `0.1267`
- 10d: hit_rate `0.6250`, avg `0.0096`, median `0.0266`, brier `0.2381`, calibration_gap `0.0642`
- 20d: hit_rate `0.6250`, avg `0.0168`, median `0.0228`, brier `0.2378`, calibration_gap `0.0642`
- 60d: hit_rate `0.6250`, avg `0.0186`, median `0.0414`, brier `0.2383`, calibration_gap `0.0642`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
