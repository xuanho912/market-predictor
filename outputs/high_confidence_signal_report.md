# High Confidence Signal Report

Generated at: `2026-07-28T14:40:59.342107+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.1250`, avg `-0.0201`, median `-0.0284`, brier `0.5447`, calibration_gap `0.6616`
- 5d: hit_rate `0.2500`, avg `-0.0260`, median `-0.0289`, brier `0.4741`, calibration_gap `0.5366`
- 10d: hit_rate `0.1250`, avg `-0.0117`, median `-0.0096`, brier `0.5493`, calibration_gap `0.6616`
- 20d: hit_rate `0.5000`, avg `0.0145`, median `0.0138`, brier `0.3366`, calibration_gap `0.2866`
- 60d: hit_rate `0.6250`, avg `0.0416`, median `0.0418`, brier `0.2624`, calibration_gap `0.1616`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0083`, median `-0.0054`, brier `0.3663`, calibration_gap `0.3416`
- 5d: hit_rate `0.5000`, avg `-0.0142`, median `-0.0074`, brier `0.3309`, calibration_gap `0.2791`
- 10d: hit_rate `0.2500`, avg `-0.0055`, median `-0.0074`, brier `0.4696`, calibration_gap `0.5291`
- 20d: hit_rate `0.6250`, avg `0.0129`, median `0.0205`, brier `0.2617`, calibration_gap `0.1541`
- 60d: hit_rate `0.7500`, avg `0.0432`, median `0.0483`, brier `0.1911`, calibration_gap `0.0291`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6500`, avg `0.0042`, median `0.0051`, brier `0.2359`, calibration_gap `0.0682`
- 5d: hit_rate `0.7000`, avg `0.0098`, median `0.0098`, brier `0.2202`, calibration_gap `0.0182`
- 10d: hit_rate `0.6750`, avg `0.0169`, median `0.0179`, brier `0.2371`, calibration_gap `0.0432`
- 20d: hit_rate `0.6500`, avg `0.0289`, median `0.0408`, brier `0.2419`, calibration_gap `0.0682`
- 60d: hit_rate `0.7000`, avg `0.0503`, median `0.0588`, brier `0.2193`, calibration_gap `0.0182`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0098`, median `0.0150`, brier `0.1914`, calibration_gap `-0.0678`
- 5d: hit_rate `0.7500`, avg `0.0156`, median `0.0194`, brier `0.1927`, calibration_gap `-0.0678`
- 10d: hit_rate `0.7500`, avg `0.0238`, median `0.0248`, brier `0.1927`, calibration_gap `-0.0678`
- 20d: hit_rate `0.6250`, avg `0.0248`, median `0.0463`, brier `0.2380`, calibration_gap `0.0572`
- 60d: hit_rate `0.6875`, avg `0.0576`, median `0.0865`, brier `0.2151`, calibration_gap `-0.0053`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
