# High Confidence Signal Report

Generated at: `2026-10-28T10:02:29.897833+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0056`, median `0.0029`, brier `0.2580`, calibration_gap `0.1338`
- 5d: hit_rate `0.5000`, avg `0.0064`, median `0.0012`, brier `0.3240`, calibration_gap `0.2588`
- 10d: hit_rate `0.6250`, avg `0.0152`, median `0.0143`, brier `0.2489`, calibration_gap `0.1338`
- 20d: hit_rate `0.8750`, avg `0.0334`, median `0.0299`, brier `0.1241`, calibration_gap `-0.1162`
- 60d: hit_rate `1.0000`, avg `0.0675`, median `0.0708`, brier `0.0582`, calibration_gap `-0.2412`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0054`, median `0.0004`, brier `0.3123`, calibration_gap `0.2484`
- 5d: hit_rate `0.4375`, avg `0.0033`, median `-0.0051`, brier `0.3461`, calibration_gap `0.3109`
- 10d: hit_rate `0.4375`, avg `0.0012`, median `-0.0018`, brier `0.3384`, calibration_gap `0.3109`
- 20d: hit_rate `0.7500`, avg `0.0164`, median `0.0205`, brier `0.1846`, calibration_gap `-0.0016`
- 60d: hit_rate `0.9375`, avg `0.0644`, median `0.0708`, brier `0.0932`, calibration_gap `-0.1891`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6250`, avg `0.0057`, median `0.0060`, brier `0.2453`, calibration_gap `0.0730`
- 5d: hit_rate `0.6500`, avg `0.0088`, median `0.0099`, brier `0.2400`, calibration_gap `0.0480`
- 10d: hit_rate `0.6875`, avg `0.0122`, median `0.0101`, brier `0.2220`, calibration_gap `0.0105`
- 20d: hit_rate `0.7125`, avg `0.0190`, median `0.0260`, brier `0.2017`, calibration_gap `-0.0145`
- 60d: hit_rate `0.7500`, avg `0.0339`, median `0.0475`, brier `0.1844`, calibration_gap `-0.0520`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0059`, median `0.0066`, brier `0.2183`, calibration_gap `-0.0415`
- 5d: hit_rate `0.8125`, avg `0.0125`, median `0.0180`, brier `0.1810`, calibration_gap `-0.1665`
- 10d: hit_rate `0.8125`, avg `0.0137`, median `0.0198`, brier `0.1795`, calibration_gap `-0.1665`
- 20d: hit_rate `0.5000`, avg `0.0036`, median `0.0043`, brier `0.2725`, calibration_gap `0.1460`
- 60d: hit_rate `0.6250`, avg `0.0125`, median `0.0276`, brier `0.2334`, calibration_gap `0.0210`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
