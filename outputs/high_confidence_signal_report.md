# High Confidence Signal Report

Generated at: `2026-10-27T09:22:03.637239+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0054`, median `0.0029`, brier `0.2649`, calibration_gap `0.1597`
- 5d: hit_rate `0.3750`, avg `0.0042`, median `-0.0077`, brier `0.4041`, calibration_gap `0.4097`
- 10d: hit_rate `0.7500`, avg `0.0162`, median `0.0143`, brier `0.1905`, calibration_gap `0.0347`
- 20d: hit_rate `0.8750`, avg `0.0351`, median `0.0314`, brier `0.1194`, calibration_gap `-0.0903`
- 60d: hit_rate `1.0000`, avg `0.0773`, median `0.0831`, brier `0.0464`, calibration_gap `-0.2153`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0051`, median `0.0029`, brier `0.2916`, calibration_gap `0.2097`
- 5d: hit_rate `0.3750`, avg `0.0024`, median `-0.0051`, brier `0.3925`, calibration_gap `0.3972`
- 10d: hit_rate `0.5625`, avg `0.0146`, median `0.0061`, brier `0.2882`, calibration_gap `0.2097`
- 20d: hit_rate `0.9375`, avg `0.0325`, median `0.0287`, brier `0.0886`, calibration_gap `-0.1653`
- 60d: hit_rate `1.0000`, avg `0.0776`, median `0.0780`, brier `0.0521`, calibration_gap `-0.2278`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6500`, avg `0.0048`, median `0.0063`, brier `0.2286`, calibration_gap `0.0403`
- 5d: hit_rate `0.6500`, avg `0.0080`, median `0.0093`, brier `0.2264`, calibration_gap `0.0403`
- 10d: hit_rate `0.7000`, avg `0.0127`, median `0.0120`, brier `0.2063`, calibration_gap `-0.0097`
- 20d: hit_rate `0.7000`, avg `0.0191`, median `0.0191`, brier `0.2111`, calibration_gap `-0.0097`
- 60d: hit_rate `0.8250`, avg `0.0273`, median `0.0314`, brier `0.1631`, calibration_gap `-0.1347`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0031`, median `0.0037`, brier `0.2580`, calibration_gap `0.1175`
- 5d: hit_rate `0.5000`, avg `0.0022`, median `-0.0010`, brier `0.2816`, calibration_gap `0.1800`
- 10d: hit_rate `0.5000`, avg `-0.0008`, median `0.0029`, brier `0.2825`, calibration_gap `0.1800`
- 20d: hit_rate `0.6875`, avg `0.0152`, median `0.0170`, brier `0.2163`, calibration_gap `-0.0075`
- 60d: hit_rate `0.7500`, avg `0.0215`, median `0.0305`, brier `0.1933`, calibration_gap `-0.0700`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
