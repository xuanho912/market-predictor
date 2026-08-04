# High Confidence Signal Report

Generated at: `2026-08-04T06:18:30.721782+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `0.0053`, median `0.0022`, brier `0.2722`, calibration_gap `0.1796`
- 5d: hit_rate `0.6250`, avg `0.0041`, median `0.0072`, brier `0.2249`, calibration_gap `0.0546`
- 10d: hit_rate `0.5000`, avg `0.0063`, median `0.0088`, brier `0.2739`, calibration_gap `0.1796`
- 20d: hit_rate `1.0000`, avg `0.0376`, median `0.0386`, brier `0.1031`, calibration_gap `-0.3204`
- 60d: hit_rate `0.6250`, avg `0.0073`, median `0.0679`, brier `0.2460`, calibration_gap `0.0546`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0088`, median `0.0131`, brier `0.2169`, calibration_gap `-0.0264`
- 5d: hit_rate `0.5625`, avg `0.0059`, median `0.0046`, brier `0.2480`, calibration_gap `0.0986`
- 10d: hit_rate `0.6875`, avg `0.0132`, median `0.0221`, brier `0.2179`, calibration_gap `-0.0264`
- 20d: hit_rate `0.9375`, avg `0.0366`, median `0.0447`, brier `0.1325`, calibration_gap `-0.2764`
- 60d: hit_rate `0.6250`, avg `0.0214`, median `0.0679`, brier `0.2399`, calibration_gap `0.0361`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6750`, avg `0.0061`, median `0.0069`, brier `0.2230`, calibration_gap `-0.0589`
- 5d: hit_rate `0.6625`, avg `0.0088`, median `0.0080`, brier `0.2268`, calibration_gap `-0.0464`
- 10d: hit_rate `0.8000`, avg `0.0188`, median `0.0210`, brier `0.1967`, calibration_gap `-0.1839`
- 20d: hit_rate `0.8250`, avg `0.0314`, median `0.0323`, brier `0.1836`, calibration_gap `-0.2089`
- 60d: hit_rate `0.7625`, avg `0.0470`, median `0.0747`, brier `0.2075`, calibration_gap `-0.1464`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0002`, median `-0.0006`, brier `0.2571`, calibration_gap `0.0841`
- 5d: hit_rate `0.6250`, avg `0.0020`, median `0.0071`, brier `0.2359`, calibration_gap `-0.0409`
- 10d: hit_rate `0.7500`, avg `0.0136`, median `0.0124`, brier `0.2144`, calibration_gap `-0.1659`
- 20d: hit_rate `0.6875`, avg `0.0235`, median `0.0292`, brier `0.2250`, calibration_gap `-0.1034`
- 60d: hit_rate `0.7500`, avg `0.0517`, median `0.0751`, brier `0.2141`, calibration_gap `-0.1659`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
