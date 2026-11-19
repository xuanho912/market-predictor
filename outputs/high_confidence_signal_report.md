# High Confidence Signal Report

Generated at: `2026-11-19T20:40:57.729085+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `0.0033`, median `0.0013`, brier `0.3678`, calibration_gap `0.3208`
- 5d: hit_rate `0.7500`, avg `0.0149`, median `0.0122`, brier `0.1907`, calibration_gap `0.0708`
- 10d: hit_rate `0.7500`, avg `0.0292`, median `0.0394`, brier `0.1902`, calibration_gap `0.0708`
- 20d: hit_rate `0.6250`, avg `0.0288`, median `0.0188`, brier `0.2863`, calibration_gap `0.1958`
- 60d: hit_rate `0.7500`, avg `0.0423`, median `0.0258`, brier `0.1971`, calibration_gap `0.0708`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0074`, median `0.0073`, brier `0.3153`, calibration_gap `0.2417`
- 5d: hit_rate `0.6250`, avg `0.0045`, median `0.0033`, brier `0.2625`, calibration_gap `0.1792`
- 10d: hit_rate `0.5625`, avg `0.0107`, median `0.0122`, brier `0.2976`, calibration_gap `0.2417`
- 20d: hit_rate `0.6875`, avg `0.0257`, median `0.0201`, brier `0.2366`, calibration_gap `0.1167`
- 60d: hit_rate `0.6250`, avg `0.0288`, median `0.0030`, brier `0.2650`, calibration_gap `0.1792`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6750`, avg `0.0141`, median `0.0103`, brier `0.2432`, calibration_gap `0.0293`
- 5d: hit_rate `0.7000`, avg `0.0154`, median `0.0119`, brier `0.2262`, calibration_gap `0.0043`
- 10d: hit_rate `0.7750`, avg `0.0276`, median `0.0226`, brier `0.1978`, calibration_gap `-0.0707`
- 20d: hit_rate `0.8250`, avg `0.0479`, median `0.0463`, brier `0.1763`, calibration_gap `-0.1207`
- 60d: hit_rate `0.7500`, avg `0.0750`, median `0.0866`, brier `0.1927`, calibration_gap `-0.0457`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0087`, median `0.0144`, brier `0.2197`, calibration_gap `-0.0778`
- 5d: hit_rate `0.6250`, avg `0.0184`, median `0.0112`, brier `0.2350`, calibration_gap `-0.0153`
- 10d: hit_rate `0.6875`, avg `0.0248`, median `0.0308`, brier `0.2202`, calibration_gap `-0.0778`
- 20d: hit_rate `0.6875`, avg `0.0257`, median `0.0478`, brier `0.2201`, calibration_gap `-0.0778`
- 60d: hit_rate `0.6250`, avg `0.0373`, median `0.0746`, brier `0.2373`, calibration_gap `-0.0153`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
