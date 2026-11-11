# High Confidence Signal Report

Generated at: `2026-11-11T02:19:57.276207+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0016`, median `-0.0001`, brier `0.3408`, calibration_gap `0.2971`
- 5d: hit_rate `0.3750`, avg `0.0009`, median `-0.0079`, brier `0.4169`, calibration_gap `0.4221`
- 10d: hit_rate `0.7500`, avg `0.0147`, median `0.0151`, brier `0.1898`, calibration_gap `0.0471`
- 20d: hit_rate `0.7500`, avg `0.0211`, median `0.0278`, brier `0.1870`, calibration_gap `0.0471`
- 60d: hit_rate `1.0000`, avg `0.0677`, median `0.0705`, brier `0.0412`, calibration_gap `-0.2029`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0014`, median `0.0021`, brier `0.2987`, calibration_gap `0.2217`
- 5d: hit_rate `0.3750`, avg `-0.0012`, median `-0.0071`, brier `0.4044`, calibration_gap `0.4092`
- 10d: hit_rate `0.6875`, avg `0.0104`, median `0.0111`, brier `0.2233`, calibration_gap `0.0967`
- 20d: hit_rate `0.6875`, avg `0.0173`, median `0.0261`, brier `0.2198`, calibration_gap `0.0967`
- 60d: hit_rate `0.8125`, avg `0.0470`, median `0.0669`, brier `0.1473`, calibration_gap `-0.0283`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5250`, avg `0.0001`, median `0.0021`, brier `0.2821`, calibration_gap `0.1725`
- 5d: hit_rate `0.5500`, avg `0.0035`, median `0.0065`, brier `0.2689`, calibration_gap `0.1475`
- 10d: hit_rate `0.6750`, avg `0.0118`, median `0.0145`, brier `0.2316`, calibration_gap `0.0225`
- 20d: hit_rate `0.7250`, avg `0.0212`, median `0.0251`, brier `0.1955`, calibration_gap `-0.0275`
- 60d: hit_rate `0.8000`, avg `0.0409`, median `0.0543`, brier `0.1652`, calibration_gap `-0.1025`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0017`, median `-0.0028`, brier `0.2712`, calibration_gap `0.1453`
- 5d: hit_rate `0.5000`, avg `0.0003`, median `0.0011`, brier `0.2694`, calibration_gap `0.1453`
- 10d: hit_rate `0.7500`, avg `0.0112`, median `0.0162`, brier `0.1996`, calibration_gap `-0.1047`
- 20d: hit_rate `0.6250`, avg `0.0193`, median `0.0172`, brier `0.2323`, calibration_gap `0.0203`
- 60d: hit_rate `0.6875`, avg `0.0357`, median `0.0521`, brier `0.2156`, calibration_gap `-0.0422`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
