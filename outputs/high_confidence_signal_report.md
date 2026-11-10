# High Confidence Signal Report

Generated at: `2026-11-10T19:47:04.325384+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0016`, median `-0.0001`, brier `0.3438`, calibration_gap `0.3012`
- 5d: hit_rate `0.3750`, avg `0.0009`, median `-0.0079`, brier `0.4192`, calibration_gap `0.4262`
- 10d: hit_rate `0.7500`, avg `0.0147`, median `0.0151`, brier `0.1911`, calibration_gap `0.0512`
- 20d: hit_rate `0.7500`, avg `0.0211`, median `0.0278`, brier `0.1886`, calibration_gap `0.0512`
- 60d: hit_rate `1.0000`, avg `0.0677`, median `0.0705`, brier `0.0396`, calibration_gap `-0.1988`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0003`, median `0.0004`, brier `0.3341`, calibration_gap `0.2875`
- 5d: hit_rate `0.3125`, avg `-0.0026`, median `-0.0071`, brier `0.4402`, calibration_gap `0.4750`
- 10d: hit_rate `0.6250`, avg `0.0090`, median `0.0085`, brier `0.2577`, calibration_gap `0.1625`
- 20d: hit_rate `0.7500`, avg `0.0188`, median `0.0261`, brier `0.1876`, calibration_gap `0.0375`
- 60d: hit_rate `0.8125`, avg `0.0447`, median `0.0642`, brier `0.1469`, calibration_gap `-0.0250`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.5500`, avg `0.0012`, median `0.0053`, brier `0.2526`, calibration_gap `0.0975`
- 5d: hit_rate `0.6500`, avg `0.0089`, median `0.0112`, brier `0.2256`, calibration_gap `-0.0025`
- 10d: hit_rate `0.7500`, avg `0.0178`, median `0.0201`, brier `0.1942`, calibration_gap `-0.1025`
- 20d: hit_rate `0.7000`, avg `0.0219`, median `0.0332`, brier `0.2077`, calibration_gap `-0.0525`
- 60d: hit_rate `0.7500`, avg `0.0420`, median `0.0559`, brier `0.1942`, calibration_gap `-0.1025`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0002`, median `0.0017`, brier `0.2691`, calibration_gap `0.1411`
- 5d: hit_rate `0.6250`, avg `0.0060`, median `0.0085`, brier `0.2358`, calibration_gap `0.0161`
- 10d: hit_rate `0.6875`, avg `0.0100`, median `0.0187`, brier `0.2160`, calibration_gap `-0.0464`
- 20d: hit_rate `0.6250`, avg `0.0144`, median `0.0172`, brier `0.2329`, calibration_gap `0.0161`
- 60d: hit_rate `0.6875`, avg `0.0434`, median `0.0626`, brier `0.2160`, calibration_gap `-0.0464`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
