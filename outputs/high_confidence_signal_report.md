# High Confidence Signal Report

Generated at: `2026-08-04T04:35:55.369943+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0102`, median `0.0156`, brier `0.1842`, calibration_gap `-0.0734`
- 5d: hit_rate `0.6250`, avg `0.0061`, median `0.0092`, brier `0.2332`, calibration_gap `0.0516`
- 10d: hit_rate `0.6250`, avg `0.0099`, median `0.0198`, brier `0.2320`, calibration_gap `0.0516`
- 20d: hit_rate `1.0000`, avg `0.0411`, median `0.0386`, brier `0.1052`, calibration_gap `-0.3234`
- 60d: hit_rate `0.6250`, avg `0.0062`, median `0.0654`, brier `0.2499`, calibration_gap `0.0516`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0114`, median `0.0143`, brier `0.1920`, calibration_gap `-0.0921`
- 5d: hit_rate `0.6875`, avg `0.0102`, median `0.0112`, brier `0.2186`, calibration_gap `-0.0296`
- 10d: hit_rate `0.7500`, avg `0.0200`, median `0.0232`, brier `0.1986`, calibration_gap `-0.0921`
- 20d: hit_rate `0.9375`, avg `0.0406`, median `0.0386`, brier `0.1343`, calibration_gap `-0.2796`
- 60d: hit_rate `0.7500`, avg `0.0397`, median `0.0791`, brier `0.2083`, calibration_gap `-0.0921`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.7250`, avg `0.0085`, median `0.0112`, brier `0.2099`, calibration_gap `-0.1116`
- 5d: hit_rate `0.6875`, avg `0.0106`, median `0.0103`, brier `0.2190`, calibration_gap `-0.0741`
- 10d: hit_rate `0.8000`, avg `0.0201`, median `0.0210`, brier `0.1965`, calibration_gap `-0.1866`
- 20d: hit_rate `0.8875`, avg `0.0341`, median `0.0309`, brier `0.1739`, calibration_gap `-0.2741`
- 60d: hit_rate `0.7625`, avg `0.0472`, median `0.0696`, brier `0.2065`, calibration_gap `-0.1491`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0039`, median `0.0036`, brier `0.2343`, calibration_gap `-0.0395`
- 5d: hit_rate `0.4375`, avg `0.0002`, median `-0.0095`, brier `0.2663`, calibration_gap `0.1480`
- 10d: hit_rate `0.6875`, avg `0.0116`, median `0.0118`, brier `0.2266`, calibration_gap `-0.1020`
- 20d: hit_rate `0.8125`, avg `0.0217`, median `0.0110`, brier `0.2041`, calibration_gap `-0.2270`
- 60d: hit_rate `0.6875`, avg `0.0301`, median `0.0211`, brier `0.2257`, calibration_gap `-0.1020`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
