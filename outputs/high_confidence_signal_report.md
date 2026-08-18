# High Confidence Signal Report

Generated at: `2026-08-18T04:22:40.522421+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `60`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `6`
- 3d: hit_rate `0.5000`, avg `0.0001`, median `0.0004`, brier `0.2595`, calibration_gap `0.1454`
- 5d: hit_rate `0.3333`, avg `-0.0151`, median `-0.0228`, brier `0.3045`, calibration_gap `0.3121`
- 10d: hit_rate `0.5000`, avg `-0.0003`, median `-0.0027`, brier `0.2586`, calibration_gap `0.1454`
- 20d: hit_rate `0.8333`, avg `0.0162`, median `0.0146`, brier `0.1720`, calibration_gap `-0.1879`
- 60d: hit_rate `0.6667`, avg `0.0150`, median `0.0235`, brier `0.2169`, calibration_gap `-0.0213`

### top_20_confidence_signals
- sample_size: `12`
- 3d: hit_rate `0.5000`, avg `-0.0027`, median `0.0017`, brier `0.2636`, calibration_gap `0.1337`
- 5d: hit_rate `0.3333`, avg `-0.0138`, median `-0.0164`, brier `0.3060`, calibration_gap `0.3004`
- 10d: hit_rate `0.4167`, avg `-0.0006`, median `-0.0036`, brier `0.2811`, calibration_gap `0.2171`
- 20d: hit_rate `0.8333`, avg `0.0181`, median `0.0222`, brier `0.1788`, calibration_gap `-0.1996`
- 60d: hit_rate `0.6667`, avg `0.0094`, median `0.0297`, brier `0.2212`, calibration_gap `-0.0329`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.7167`, avg `0.0077`, median `0.0074`, brier `0.2212`, calibration_gap `-0.1187`
- 5d: hit_rate `0.6667`, avg `0.0102`, median `0.0125`, brier `0.2323`, calibration_gap `-0.0687`
- 10d: hit_rate `0.7167`, avg `0.0207`, median `0.0192`, brier `0.2216`, calibration_gap `-0.1187`
- 20d: hit_rate `0.9000`, avg `0.0385`, median `0.0316`, brier `0.1820`, calibration_gap `-0.3020`
- 60d: hit_rate `0.7500`, avg `0.0394`, median `0.0511`, brier `0.2112`, calibration_gap `-0.1520`

### low_confidence_reference
- sample_size: `12`
- 3d: hit_rate `0.8333`, avg `0.0191`, median `0.0220`, brier `0.2083`, calibration_gap `-0.2659`
- 5d: hit_rate `0.6667`, avg `0.0232`, median `0.0239`, brier `0.2306`, calibration_gap `-0.0993`
- 10d: hit_rate `0.7500`, avg `0.0359`, median `0.0422`, brier `0.2206`, calibration_gap `-0.1826`
- 20d: hit_rate `0.8333`, avg `0.0482`, median `0.0514`, brier `0.2098`, calibration_gap `-0.2659`
- 60d: hit_rate `0.5833`, avg `0.0161`, median `0.0568`, brier `0.2436`, calibration_gap `-0.0159`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
