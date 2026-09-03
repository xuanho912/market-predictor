# High Confidence Signal Report

Generated at: `2026-09-03T01:07:41.840751+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0150`, median `0.0131`, brier `0.1473`, calibration_gap `-0.1891`
- 5d: hit_rate `0.7500`, avg `0.0168`, median `0.0136`, brier `0.2000`, calibration_gap `-0.0641`
- 10d: hit_rate `0.6250`, avg `0.0238`, median `0.0163`, brier `0.2483`, calibration_gap `0.0609`
- 20d: hit_rate `0.8750`, avg `0.0412`, median `0.0561`, brier `0.1444`, calibration_gap `-0.1891`
- 60d: hit_rate `0.6250`, avg `0.0608`, median `0.0601`, brier `0.2412`, calibration_gap `0.0609`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0026`, median `0.0116`, brier `0.2106`, calibration_gap `-0.0159`
- 5d: hit_rate `0.6875`, avg `0.0082`, median `0.0136`, brier `0.2174`, calibration_gap `-0.0159`
- 10d: hit_rate `0.6250`, avg `0.0113`, median `0.0198`, brier `0.2415`, calibration_gap `0.0466`
- 20d: hit_rate `0.8125`, avg `0.0314`, median `0.0414`, brier `0.1693`, calibration_gap `-0.1409`
- 60d: hit_rate `0.6875`, avg `0.0436`, median `0.0615`, brier `0.2177`, calibration_gap `-0.0159`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6500`, avg `0.0054`, median `0.0112`, brier `0.2265`, calibration_gap `-0.0299`
- 5d: hit_rate `0.6500`, avg `0.0084`, median `0.0123`, brier `0.2281`, calibration_gap `-0.0299`
- 10d: hit_rate `0.6875`, avg `0.0162`, median `0.0184`, brier `0.2219`, calibration_gap `-0.0674`
- 20d: hit_rate `0.8500`, avg `0.0344`, median `0.0337`, brier `0.1801`, calibration_gap `-0.2299`
- 60d: hit_rate `0.7250`, avg `0.0520`, median `0.0754`, brier `0.2116`, calibration_gap `-0.1049`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0048`, median `0.0120`, brier `0.2354`, calibration_gap `-0.0414`
- 5d: hit_rate `0.6875`, avg `0.0123`, median `0.0184`, brier `0.2259`, calibration_gap `-0.1039`
- 10d: hit_rate `0.7500`, avg `0.0152`, median `0.0184`, brier `0.2143`, calibration_gap `-0.1664`
- 20d: hit_rate `0.8125`, avg `0.0278`, median `0.0247`, brier `0.2036`, calibration_gap `-0.2289`
- 60d: hit_rate `0.7500`, avg `0.0604`, median `0.0815`, brier `0.2159`, calibration_gap `-0.1664`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
