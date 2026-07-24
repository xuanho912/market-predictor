# High Confidence Signal Report

Generated at: `2026-07-24T22:40:36.299884+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0079`, median `-0.0042`, brier `0.3422`, calibration_gap `0.3047`
- 5d: hit_rate `0.5000`, avg `-0.0143`, median `-0.0026`, brier `0.3429`, calibration_gap `0.3047`
- 10d: hit_rate `0.2500`, avg `-0.0064`, median `-0.0076`, brier `0.4968`, calibration_gap `0.5547`
- 20d: hit_rate `0.3750`, avg `0.0030`, median `-0.0018`, brier `0.4226`, calibration_gap `0.4297`
- 60d: hit_rate `0.5000`, avg `0.0111`, median `0.0078`, brier `0.3429`, calibration_gap `0.3047`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0067`, median `-0.0005`, brier `0.3383`, calibration_gap `0.2980`
- 5d: hit_rate `0.5000`, avg `-0.0105`, median `-0.0009`, brier `0.3391`, calibration_gap `0.2980`
- 10d: hit_rate `0.4375`, avg `-0.0016`, median `-0.0038`, brier `0.3796`, calibration_gap `0.3605`
- 20d: hit_rate `0.4375`, avg `0.0049`, median `-0.0018`, brier `0.3797`, calibration_gap `0.3605`
- 60d: hit_rate `0.5625`, avg `0.0241`, median `0.0352`, brier `0.3026`, calibration_gap `0.2355`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5833`, avg `-0.0027`, median `0.0013`, brier `0.2752`, calibration_gap `0.1726`
- 5d: hit_rate `0.5500`, avg `-0.0024`, median `0.0022`, brier `0.2954`, calibration_gap `0.2060`
- 10d: hit_rate `0.5667`, avg `0.0055`, median `0.0042`, brier `0.2996`, calibration_gap `0.1893`
- 20d: hit_rate `0.6500`, avg `0.0194`, median `0.0205`, brier `0.2443`, calibration_gap `0.1060`
- 60d: hit_rate `0.7167`, avg `0.0358`, median `0.0564`, brier `0.2086`, calibration_gap `0.0393`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0092`, median `-0.0151`, brier `0.3580`, calibration_gap `0.3778`
- 5d: hit_rate `0.3125`, avg `-0.0104`, median `-0.0152`, brier `0.3584`, calibration_gap `0.3778`
- 10d: hit_rate `0.6250`, avg `0.0001`, median `0.0174`, brier `0.2392`, calibration_gap `0.0653`
- 20d: hit_rate `0.4375`, avg `-0.0086`, median `-0.0075`, brier `0.3104`, calibration_gap `0.2528`
- 60d: hit_rate `0.5000`, avg `-0.0335`, median `-0.0468`, brier `0.2886`, calibration_gap `0.1903`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
