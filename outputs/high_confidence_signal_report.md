# High Confidence Signal Report

Generated at: `2026-06-15T15:11:16.398820+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0003`, median `0.0031`, brier `0.2419`, calibration_gap `0.0879`
- 5d: hit_rate `0.5000`, avg `-0.0034`, median `-0.0047`, brier `0.2970`, calibration_gap `0.2129`
- 10d: hit_rate `0.8750`, avg `0.0113`, median `0.0135`, brier `0.1381`, calibration_gap `-0.1621`
- 20d: hit_rate `0.7500`, avg `0.0076`, median `0.0123`, brier `0.1848`, calibration_gap `-0.0371`
- 60d: hit_rate `0.2500`, avg `-0.0320`, median `-0.0398`, brier `0.4002`, calibration_gap `0.4629`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0017`, median `0.0028`, brier `0.2637`, calibration_gap `0.1382`
- 5d: hit_rate `0.3750`, avg `-0.0046`, median `-0.0068`, brier `0.3392`, calibration_gap `0.3257`
- 10d: hit_rate `0.7500`, avg `0.0073`, median `0.0075`, brier `0.1886`, calibration_gap `-0.0493`
- 20d: hit_rate `0.7500`, avg `0.0097`, median `0.0143`, brier `0.1883`, calibration_gap `-0.0493`
- 60d: hit_rate `0.4375`, avg `0.0019`, median `-0.0186`, brier `0.3180`, calibration_gap `0.2632`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6375`, avg `0.0047`, median `0.0051`, brier `0.2377`, calibration_gap `0.0246`
- 5d: hit_rate `0.6375`, avg `0.0058`, median `0.0052`, brier `0.2413`, calibration_gap `0.0246`
- 10d: hit_rate `0.6125`, avg `0.0080`, median `0.0075`, brier `0.2404`, calibration_gap `0.0496`
- 20d: hit_rate `0.7000`, avg `0.0093`, median `0.0173`, brier `0.2089`, calibration_gap `-0.0379`
- 60d: hit_rate `0.6000`, avg `0.0276`, median `0.0329`, brier `0.2474`, calibration_gap `0.0621`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0087`, median `0.0129`, brier `0.2034`, calibration_gap `-0.1215`
- 5d: hit_rate `0.8125`, avg `0.0151`, median `0.0126`, brier `0.1878`, calibration_gap `-0.1840`
- 10d: hit_rate `0.6250`, avg `0.0107`, median `0.0153`, brier `0.2366`, calibration_gap `0.0035`
- 20d: hit_rate `0.6250`, avg `0.0058`, median `0.0168`, brier `0.2354`, calibration_gap `0.0035`
- 60d: hit_rate `0.5625`, avg `0.0296`, median `0.0284`, brier `0.2507`, calibration_gap `0.0660`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
