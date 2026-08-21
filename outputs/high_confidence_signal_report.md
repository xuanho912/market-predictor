# High Confidence Signal Report

Generated at: `2026-08-21T13:13:29.649564+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0051`, median `0.0033`, brier `0.1923`, calibration_gap `-0.0257`
- 5d: hit_rate `0.8750`, avg `0.0077`, median `0.0069`, brier `0.1295`, calibration_gap `-0.1507`
- 10d: hit_rate `0.6250`, avg `0.0046`, median `0.0199`, brier `0.2457`, calibration_gap `0.0993`
- 20d: hit_rate `0.2500`, avg `-0.0051`, median `-0.0114`, brier `0.4100`, calibration_gap `0.4743`
- 60d: hit_rate `0.3750`, avg `-0.0082`, median `-0.0373`, brier `0.3566`, calibration_gap `0.3493`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.8125`, avg `0.0050`, median `0.0033`, brier `0.1650`, calibration_gap `-0.0982`
- 5d: hit_rate `0.8125`, avg `0.0067`, median `0.0069`, brier `0.1600`, calibration_gap `-0.0982`
- 10d: hit_rate `0.5625`, avg `0.0029`, median `0.0127`, brier `0.2689`, calibration_gap `0.1518`
- 20d: hit_rate `0.3750`, avg `-0.0064`, median `-0.0075`, brier `0.3511`, calibration_gap `0.3393`
- 60d: hit_rate `0.3750`, avg `-0.0061`, median `-0.0255`, brier `0.3475`, calibration_gap `0.3393`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6250`, avg `0.0052`, median `0.0061`, brier `0.2355`, calibration_gap `0.0335`
- 5d: hit_rate `0.5000`, avg `0.0035`, median `0.0003`, brier `0.2756`, calibration_gap `0.1585`
- 10d: hit_rate `0.6500`, avg `0.0087`, median `0.0106`, brier `0.2310`, calibration_gap `0.0085`
- 20d: hit_rate `0.7500`, avg `0.0215`, median `0.0176`, brier `0.1964`, calibration_gap `-0.0915`
- 60d: hit_rate `0.7500`, avg `0.0399`, median `0.0637`, brier `0.1953`, calibration_gap `-0.0915`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0044`, median `0.0061`, brier `0.2350`, calibration_gap `0.0207`
- 5d: hit_rate `0.5000`, avg `0.0037`, median `-0.0016`, brier `0.2719`, calibration_gap `0.1457`
- 10d: hit_rate `0.8125`, avg `0.0109`, median `0.0120`, brier `0.1799`, calibration_gap `-0.1668`
- 20d: hit_rate `0.8125`, avg `0.0169`, median `0.0151`, brier `0.1798`, calibration_gap `-0.1668`
- 60d: hit_rate `0.6875`, avg `0.0112`, median `0.0562`, brier `0.2166`, calibration_gap `-0.0418`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
