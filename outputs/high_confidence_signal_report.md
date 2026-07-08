# High Confidence Signal Report

Generated at: `2026-07-08T14:43:43.185778+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0063`, median `-0.0001`, brier `0.3206`, calibration_gap `0.2531`
- 5d: hit_rate `0.3750`, avg `-0.0106`, median `-0.0145`, brier `0.3784`, calibration_gap `0.3781`
- 10d: hit_rate `0.3750`, avg `-0.0016`, median `-0.0032`, brier `0.3838`, calibration_gap `0.3781`
- 20d: hit_rate `1.0000`, avg `0.0388`, median `0.0387`, brier `0.0611`, calibration_gap `-0.2469`
- 60d: hit_rate `1.0000`, avg `0.0904`, median `0.1006`, brier `0.0611`, calibration_gap `-0.2469`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0049`, median `-0.0001`, brier `0.3137`, calibration_gap `0.2452`
- 5d: hit_rate `0.4375`, avg `-0.0094`, median `-0.0130`, brier `0.3426`, calibration_gap `0.3077`
- 10d: hit_rate `0.3750`, avg `-0.0020`, median `-0.0036`, brier `0.3741`, calibration_gap `0.3702`
- 20d: hit_rate `0.8750`, avg `0.0300`, median `0.0326`, brier `0.1251`, calibration_gap `-0.1298`
- 60d: hit_rate `0.8750`, avg `0.0731`, median `0.0890`, brier `0.1246`, calibration_gap `-0.1298`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5333`, avg `-0.0011`, median `0.0012`, brier `0.2865`, calibration_gap `0.1664`
- 5d: hit_rate `0.4500`, avg `-0.0031`, median `-0.0021`, brier `0.3194`, calibration_gap `0.2498`
- 10d: hit_rate `0.5000`, avg `0.0018`, median `-0.0001`, brier `0.2978`, calibration_gap `0.1998`
- 20d: hit_rate `0.8000`, avg `0.0175`, median `0.0203`, brier `0.1694`, calibration_gap `-0.1002`
- 60d: hit_rate `0.6333`, avg `0.0289`, median `0.0449`, brier `0.2323`, calibration_gap `0.0664`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.8125`, avg `0.0060`, median `0.0053`, brier `0.1751`, calibration_gap `-0.1520`
- 5d: hit_rate `0.6875`, avg `0.0100`, median `0.0155`, brier `0.2147`, calibration_gap `-0.0270`
- 10d: hit_rate `0.6250`, avg `0.0071`, median `0.0133`, brier `0.2343`, calibration_gap `0.0355`
- 20d: hit_rate `0.8125`, avg `0.0126`, median `0.0240`, brier `0.1749`, calibration_gap `-0.1520`
- 60d: hit_rate `0.6250`, avg `0.0135`, median `0.0293`, brier `0.2348`, calibration_gap `0.0355`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
