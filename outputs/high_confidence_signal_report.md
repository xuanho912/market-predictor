# High Confidence Signal Report

Generated at: `2026-10-26T18:44:10.979194+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0054`, median `0.0029`, brier `0.2649`, calibration_gap `0.1598`
- 5d: hit_rate `0.3750`, avg `0.0042`, median `-0.0077`, brier `0.4041`, calibration_gap `0.4098`
- 10d: hit_rate `0.7500`, avg `0.0162`, median `0.0143`, brier `0.1903`, calibration_gap `0.0348`
- 20d: hit_rate `0.8750`, avg `0.0351`, median `0.0314`, brier `0.1193`, calibration_gap `-0.0902`
- 60d: hit_rate `1.0000`, avg `0.0773`, median `0.0831`, brier `0.0464`, calibration_gap `-0.2152`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0051`, median `0.0029`, brier `0.2916`, calibration_gap `0.2097`
- 5d: hit_rate `0.3750`, avg `0.0024`, median `-0.0051`, brier `0.3925`, calibration_gap `0.3972`
- 10d: hit_rate `0.5625`, avg `0.0146`, median `0.0061`, brier `0.2881`, calibration_gap `0.2097`
- 20d: hit_rate `0.9375`, avg `0.0325`, median `0.0287`, brier `0.0886`, calibration_gap `-0.1653`
- 60d: hit_rate `1.0000`, avg `0.0776`, median `0.0780`, brier `0.0521`, calibration_gap `-0.2278`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6500`, avg `0.0045`, median `0.0063`, brier `0.2283`, calibration_gap `0.0391`
- 5d: hit_rate `0.6500`, avg `0.0075`, median `0.0093`, brier `0.2267`, calibration_gap `0.0391`
- 10d: hit_rate `0.7000`, avg `0.0122`, median `0.0120`, brier `0.2068`, calibration_gap `-0.0109`
- 20d: hit_rate `0.7000`, avg `0.0179`, median `0.0191`, brier `0.2113`, calibration_gap `-0.0109`
- 60d: hit_rate `0.8000`, avg `0.0266`, median `0.0314`, brier `0.1725`, calibration_gap `-0.1109`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0062`, median `0.0072`, brier `0.2581`, calibration_gap `0.1175`
- 5d: hit_rate `0.5625`, avg `0.0073`, median `0.0093`, brier `0.2586`, calibration_gap `0.1175`
- 10d: hit_rate `0.6250`, avg `0.0092`, median `0.0072`, brier `0.2364`, calibration_gap `0.0550`
- 20d: hit_rate `0.7500`, avg `0.0213`, median `0.0228`, brier `0.1932`, calibration_gap `-0.0700`
- 60d: hit_rate `0.7500`, avg `0.0251`, median `0.0396`, brier `0.1929`, calibration_gap `-0.0700`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
