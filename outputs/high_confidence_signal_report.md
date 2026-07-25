# High Confidence Signal Report

Generated at: `2026-07-25T04:32:29.258825+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0012`, median `0.0031`, brier `0.2394`, calibration_gap `0.0723`
- 5d: hit_rate `0.8750`, avg `0.0128`, median `0.0160`, brier `0.1446`, calibration_gap `-0.1777`
- 10d: hit_rate `0.7500`, avg `0.0121`, median `0.0178`, brier `0.1931`, calibration_gap `-0.0527`
- 20d: hit_rate `1.0000`, avg `0.0464`, median `0.0460`, brier `0.0917`, calibration_gap `-0.3027`
- 60d: hit_rate `1.0000`, avg `0.0867`, median `0.0922`, brier `0.0917`, calibration_gap `-0.3027`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0035`, median `0.0043`, brier `0.2389`, calibration_gap `0.0609`
- 5d: hit_rate `0.7500`, avg `0.0098`, median `0.0116`, brier `0.1876`, calibration_gap `-0.0641`
- 10d: hit_rate `0.8125`, avg `0.0144`, median `0.0178`, brier `0.1706`, calibration_gap `-0.1266`
- 20d: hit_rate `0.8750`, avg `0.0350`, median `0.0414`, brier `0.1408`, calibration_gap `-0.1891`
- 60d: hit_rate `0.9375`, avg `0.0804`, median `0.0958`, brier `0.1199`, calibration_gap `-0.2516`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6125`, avg `0.0046`, median `0.0051`, brier `0.2385`, calibration_gap `0.0295`
- 5d: hit_rate `0.6375`, avg `0.0088`, median `0.0089`, brier `0.2314`, calibration_gap `0.0045`
- 10d: hit_rate `0.7750`, avg `0.0166`, median `0.0210`, brier `0.1891`, calibration_gap `-0.1330`
- 20d: hit_rate `0.8375`, avg `0.0303`, median `0.0336`, brier `0.1744`, calibration_gap `-0.1955`
- 60d: hit_rate `0.7875`, avg `0.0465`, median `0.0741`, brier `0.1849`, calibration_gap `-0.1455`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0109`, median `0.0107`, brier `0.2359`, calibration_gap `-0.0170`
- 5d: hit_rate `0.7500`, avg `0.0161`, median `0.0150`, brier `0.2080`, calibration_gap `-0.1420`
- 10d: hit_rate `0.6250`, avg `0.0184`, median `0.0223`, brier `0.2350`, calibration_gap `-0.0170`
- 20d: hit_rate `0.8750`, avg `0.0293`, median `0.0340`, brier `0.1806`, calibration_gap `-0.2670`
- 60d: hit_rate `0.6875`, avg `0.0320`, median `0.0564`, brier `0.2204`, calibration_gap `-0.0795`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
