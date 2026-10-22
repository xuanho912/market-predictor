# High Confidence Signal Report

Generated at: `2026-10-22T00:27:10.495030+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0086`, median `0.0084`, brier `0.1433`, calibration_gap `-0.1981`
- 5d: hit_rate `0.8750`, avg `0.0109`, median `0.0118`, brier `0.1433`, calibration_gap `-0.1981`
- 10d: hit_rate `0.7500`, avg `0.0145`, median `0.0216`, brier `0.1847`, calibration_gap `-0.0731`
- 20d: hit_rate `0.8750`, avg `0.0282`, median `0.0301`, brier `0.1433`, calibration_gap `-0.1981`
- 60d: hit_rate `0.8750`, avg `0.0802`, median `0.0890`, brier `0.1462`, calibration_gap `-0.1981`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.8125`, avg `0.0091`, median `0.0104`, brier `0.1709`, calibration_gap `-0.1563`
- 5d: hit_rate `0.8750`, avg `0.0132`, median `0.0140`, brier `0.1546`, calibration_gap `-0.2188`
- 10d: hit_rate `0.7500`, avg `0.0160`, median `0.0223`, brier `0.1916`, calibration_gap `-0.0938`
- 20d: hit_rate `0.8750`, avg `0.0314`, median `0.0301`, brier `0.1546`, calibration_gap `-0.2188`
- 60d: hit_rate `0.9375`, avg `0.0788`, median `0.0906`, brier `0.1395`, calibration_gap `-0.2813`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.7333`, avg `0.0080`, median `0.0123`, brier `0.2060`, calibration_gap `-0.1227`
- 5d: hit_rate `0.7333`, avg `0.0081`, median `0.0118`, brier `0.2043`, calibration_gap `-0.1227`
- 10d: hit_rate `0.6000`, avg `0.0090`, median `0.0111`, brier `0.2334`, calibration_gap `0.0106`
- 20d: hit_rate `0.7333`, avg `0.0184`, median `0.0249`, brier `0.2053`, calibration_gap `-0.1227`
- 60d: hit_rate `0.8000`, avg `0.0644`, median `0.0708`, brier `0.1929`, calibration_gap `-0.1894`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0017`, median `0.0041`, brier `0.2388`, calibration_gap `-0.0550`
- 5d: hit_rate `0.5625`, avg `0.0009`, median `0.0066`, brier `0.2487`, calibration_gap `0.0075`
- 10d: hit_rate `0.6250`, avg `0.0113`, median `0.0237`, brier `0.2397`, calibration_gap `-0.0550`
- 20d: hit_rate `0.6875`, avg `0.0224`, median `0.0162`, brier `0.2292`, calibration_gap `-0.1175`
- 60d: hit_rate `0.7500`, avg `0.0732`, median `0.1153`, brier `0.2202`, calibration_gap `-0.1800`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
