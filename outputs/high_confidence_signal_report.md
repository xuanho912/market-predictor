# High Confidence Signal Report

Generated at: `2026-10-02T17:54:46.216713+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0116`, median `0.0124`, brier `0.1137`, calibration_gap `-0.0324`
- 5d: hit_rate `0.8750`, avg `0.0085`, median `0.0076`, brier `0.1137`, calibration_gap `-0.0324`
- 10d: hit_rate `0.7500`, avg `0.0062`, median `0.0097`, brier `0.1976`, calibration_gap `0.0926`
- 20d: hit_rate `0.7500`, avg `0.0225`, median `0.0235`, brier `0.1994`, calibration_gap `0.0926`
- 60d: hit_rate `1.0000`, avg `0.0682`, median `0.0717`, brier `0.0249`, calibration_gap `-0.1574`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0073`, median `0.0124`, brier `0.1920`, calibration_gap `0.0786`
- 5d: hit_rate `0.6875`, avg `0.0029`, median `0.0076`, brier `0.2308`, calibration_gap `0.1411`
- 10d: hit_rate `0.6875`, avg `-0.0010`, median `0.0060`, brier `0.2329`, calibration_gap `0.1411`
- 20d: hit_rate `0.6875`, avg `0.0131`, median `0.0122`, brier `0.2338`, calibration_gap `0.1411`
- 60d: hit_rate `0.9375`, avg `0.0667`, median `0.0751`, brier `0.0678`, calibration_gap `-0.1089`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `0.0002`, median `-0.0024`, brier `0.2836`, calibration_gap `0.1926`
- 5d: hit_rate `0.5625`, avg `-0.0023`, median `0.0021`, brier `0.2510`, calibration_gap `0.0676`
- 10d: hit_rate `0.6250`, avg `0.0072`, median `0.0074`, brier `0.2349`, calibration_gap `0.0051`
- 20d: hit_rate `0.6250`, avg `0.0078`, median `0.0126`, brier `0.2352`, calibration_gap `0.0051`
- 60d: hit_rate `0.8125`, avg `0.0199`, median `0.0320`, brier `0.1845`, calibration_gap `-0.1824`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
