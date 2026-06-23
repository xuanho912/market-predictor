# High Confidence Signal Report

Generated at: `2026-06-23T23:39:15.775351+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0079`, median `0.0189`, brier `0.2550`, calibration_gap `0.1313`
- 5d: hit_rate `0.3750`, avg `-0.0042`, median `-0.0077`, brier `0.3816`, calibration_gap `0.3813`
- 10d: hit_rate `0.3750`, avg `0.0024`, median `-0.0019`, brier `0.3752`, calibration_gap `0.3813`
- 20d: hit_rate `0.8750`, avg `0.0267`, median `0.0307`, brier `0.1232`, calibration_gap `-0.1187`
- 60d: hit_rate `1.0000`, avg `0.0802`, median `0.0890`, brier `0.0594`, calibration_gap `-0.2437`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0044`, median `0.0029`, brier `0.2813`, calibration_gap `0.1838`
- 5d: hit_rate `0.3750`, avg `-0.0032`, median `-0.0073`, brier `0.3750`, calibration_gap `0.3713`
- 10d: hit_rate `0.3750`, avg `0.0032`, median `-0.0015`, brier `0.3711`, calibration_gap `0.3713`
- 20d: hit_rate `0.9375`, avg `0.0306`, median `0.0295`, brier `0.0964`, calibration_gap `-0.1912`
- 60d: hit_rate `1.0000`, avg `0.0781`, median `0.0776`, brier `0.0645`, calibration_gap `-0.2537`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5000`, avg `0.0022`, median `0.0004`, brier `0.2811`, calibration_gap `0.1656`
- 5d: hit_rate `0.5000`, avg `0.0009`, median `-0.0001`, brier `0.2892`, calibration_gap `0.1656`
- 10d: hit_rate `0.4667`, avg `0.0023`, median `-0.0012`, brier `0.2981`, calibration_gap `0.1989`
- 20d: hit_rate `0.7833`, avg `0.0215`, median `0.0284`, brier `0.1752`, calibration_gap `-0.1177`
- 60d: hit_rate `0.7667`, avg `0.0496`, median `0.0705`, brier `0.1757`, calibration_gap `-0.1011`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0108`, median `0.0075`, brier `0.2358`, calibration_gap `-0.0137`
- 5d: hit_rate `0.6875`, avg `0.0091`, median `0.0106`, brier `0.2228`, calibration_gap `-0.0762`
- 10d: hit_rate `0.6250`, avg `0.0067`, median `0.0019`, brier `0.2360`, calibration_gap `-0.0137`
- 20d: hit_rate `0.6250`, avg `0.0124`, median `0.0123`, brier `0.2342`, calibration_gap `-0.0137`
- 60d: hit_rate `0.5625`, avg `0.0231`, median `0.0325`, brier `0.2487`, calibration_gap `0.0488`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
