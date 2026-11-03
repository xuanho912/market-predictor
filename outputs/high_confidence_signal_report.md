# High Confidence Signal Report

Generated at: `2026-11-03T19:31:43.054529+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0110`, median `0.0143`, brier `0.2617`, calibration_gap `0.1692`
- 5d: hit_rate `0.6250`, avg `0.0124`, median `0.0121`, brier `0.2617`, calibration_gap `0.1692`
- 10d: hit_rate `0.5000`, avg `0.0189`, median `0.0111`, brier `0.3332`, calibration_gap `0.2942`
- 20d: hit_rate `0.8750`, avg `0.0391`, median `0.0301`, brier `0.1196`, calibration_gap `-0.0808`
- 60d: hit_rate `1.0000`, avg `0.0746`, median `0.0738`, brier `0.0425`, calibration_gap `-0.2058`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0047`, median `0.0017`, brier `0.3261`, calibration_gap `0.2816`
- 5d: hit_rate `0.5000`, avg `0.0085`, median `0.0038`, brier `0.3261`, calibration_gap `0.2816`
- 10d: hit_rate `0.6250`, avg `0.0176`, median `0.0224`, brier `0.2613`, calibration_gap `0.1566`
- 20d: hit_rate `0.8125`, avg `0.0325`, median `0.0299`, brier `0.1538`, calibration_gap `-0.0309`
- 60d: hit_rate `0.9375`, avg `0.0718`, median `0.0737`, brier `0.0822`, calibration_gap `-0.1559`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6000`, avg `0.0063`, median `0.0085`, brier `0.2551`, calibration_gap `0.0846`
- 5d: hit_rate `0.6000`, avg `0.0107`, median `0.0126`, brier `0.2713`, calibration_gap `0.0846`
- 10d: hit_rate `0.7250`, avg `0.0183`, median `0.0198`, brier `0.2249`, calibration_gap `-0.0404`
- 20d: hit_rate `0.7000`, avg `0.0247`, median `0.0299`, brier `0.1885`, calibration_gap `-0.0154`
- 60d: hit_rate `0.8000`, avg `0.0502`, median `0.0622`, brier `0.1517`, calibration_gap `-0.1155`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0067`, median `0.0085`, brier `0.2307`, calibration_gap `-0.0400`
- 5d: hit_rate `0.6875`, avg `0.0142`, median `0.0186`, brier `0.2219`, calibration_gap `-0.1025`
- 10d: hit_rate `0.8125`, avg `0.0157`, median `0.0172`, brier `0.2032`, calibration_gap `-0.2275`
- 20d: hit_rate `0.5000`, avg `0.0134`, median `0.0108`, brier `0.2525`, calibration_gap `0.0850`
- 60d: hit_rate `0.6250`, avg `0.0228`, median `0.0242`, brier `0.2321`, calibration_gap `-0.0400`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
