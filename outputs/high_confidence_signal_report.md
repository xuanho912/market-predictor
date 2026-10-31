# High Confidence Signal Report

Generated at: `2026-10-31T01:56:04.627886+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `0.0059`, median `0.0017`, brier `0.3406`, calibration_gap `0.3069`
- 5d: hit_rate `0.5000`, avg `0.0094`, median `0.0049`, brier `0.3406`, calibration_gap `0.3069`
- 10d: hit_rate `0.6250`, avg `0.0218`, median `0.0224`, brier `0.2699`, calibration_gap `0.1819`
- 20d: hit_rate `0.8750`, avg `0.0395`, median `0.0314`, brier `0.1166`, calibration_gap `-0.0681`
- 60d: hit_rate `1.0000`, avg `0.0830`, median `0.0834`, brier `0.0374`, calibration_gap `-0.1931`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0079`, median `0.0075`, brier `0.2652`, calibration_gap `0.1692`
- 5d: hit_rate `0.5000`, avg `0.0084`, median `0.0038`, brier `0.3352`, calibration_gap `0.2942`
- 10d: hit_rate `0.6250`, avg `0.0220`, median `0.0224`, brier `0.2634`, calibration_gap `0.1692`
- 20d: hit_rate `0.9375`, avg `0.0375`, median `0.0299`, brier `0.0822`, calibration_gap `-0.1433`
- 60d: hit_rate `1.0000`, avg `0.0734`, median `0.0738`, brier `0.0426`, calibration_gap `-0.2058`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.5500`, avg `0.0045`, median `0.0046`, brier `0.2803`, calibration_gap `0.1718`
- 5d: hit_rate `0.6000`, avg `0.0094`, median `0.0083`, brier `0.2663`, calibration_gap `0.1218`
- 10d: hit_rate `0.7125`, avg `0.0198`, median `0.0198`, brier `0.2129`, calibration_gap `0.0093`
- 20d: hit_rate `0.7875`, avg `0.0332`, median `0.0414`, brier `0.1646`, calibration_gap `-0.0657`
- 60d: hit_rate `0.8375`, avg `0.0496`, median `0.0577`, brier `0.1413`, calibration_gap `-0.1157`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0046`, median `0.0025`, brier `0.2740`, calibration_gap `0.1533`
- 5d: hit_rate `0.7500`, avg `0.0115`, median `0.0147`, brier `0.1972`, calibration_gap `-0.0967`
- 10d: hit_rate `0.6875`, avg `0.0075`, median `0.0100`, brier `0.2156`, calibration_gap `-0.0342`
- 20d: hit_rate `0.4375`, avg `0.0035`, median `-0.0080`, brier `0.2942`, calibration_gap `0.2158`
- 60d: hit_rate `0.5625`, avg `0.0085`, median `0.0042`, brier `0.2559`, calibration_gap `0.0908`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
