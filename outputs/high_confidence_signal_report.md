# High Confidence Signal Report

Generated at: `2026-11-05T20:01:18.015323+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0167`, median `0.0242`, brier `0.1917`, calibration_gap `0.0402`
- 5d: hit_rate `0.7500`, avg `0.0195`, median `0.0202`, brier `0.1834`, calibration_gap `0.0402`
- 10d: hit_rate `0.7500`, avg `0.0210`, median `0.0405`, brier `0.1917`, calibration_gap `0.0402`
- 20d: hit_rate `0.7500`, avg `0.0151`, median `0.0441`, brier `0.1917`, calibration_gap `0.0402`
- 60d: hit_rate `0.8750`, avg `0.0635`, median `0.0710`, brier `0.1211`, calibration_gap `-0.0848`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0111`, median `0.0151`, brier `0.2563`, calibration_gap `0.1538`
- 5d: hit_rate `0.6250`, avg `0.0119`, median `0.0175`, brier `0.2522`, calibration_gap `0.1538`
- 10d: hit_rate `0.6250`, avg `0.0178`, median `0.0388`, brier `0.2563`, calibration_gap `0.1538`
- 20d: hit_rate `0.6250`, avg `0.0135`, median `0.0427`, brier `0.2563`, calibration_gap `0.1538`
- 60d: hit_rate `0.8750`, avg `0.0586`, median `0.0680`, brier `0.1210`, calibration_gap `-0.0962`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6500`, avg `0.0076`, median `0.0114`, brier `0.2380`, calibration_gap `0.1058`
- 5d: hit_rate `0.6250`, avg `0.0103`, median `0.0129`, brier `0.2482`, calibration_gap `0.1308`
- 10d: hit_rate `0.5500`, avg `0.0123`, median `0.0099`, brier `0.2887`, calibration_gap `0.2058`
- 20d: hit_rate `0.6750`, avg `0.0168`, median `0.0289`, brier `0.2253`, calibration_gap `0.0808`
- 60d: hit_rate `0.8000`, avg `0.0471`, median `0.0534`, brier `0.1598`, calibration_gap `-0.0442`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0028`, median `-0.0042`, brier `0.2801`, calibration_gap `0.1790`
- 5d: hit_rate `0.5000`, avg `0.0008`, median `0.0018`, brier `0.2639`, calibration_gap `0.1165`
- 10d: hit_rate `0.6250`, avg `0.0054`, median `0.0265`, brier `0.2353`, calibration_gap `-0.0085`
- 20d: hit_rate `0.6250`, avg `0.0071`, median `0.0296`, brier `0.2351`, calibration_gap `-0.0085`
- 60d: hit_rate `0.6250`, avg `0.0366`, median `0.0500`, brier `0.2303`, calibration_gap `-0.0085`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
