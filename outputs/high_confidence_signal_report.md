# High Confidence Signal Report

Generated at: `2026-10-08T18:54:14.000967+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0027`, median `0.0051`, brier `0.1919`, calibration_gap `0.0478`
- 5d: hit_rate `0.7500`, avg `0.0046`, median `0.0068`, brier `0.1919`, calibration_gap `0.0478`
- 10d: hit_rate `0.5000`, avg `-0.0037`, median `-0.0065`, brier `0.3426`, calibration_gap `0.2978`
- 20d: hit_rate `0.8750`, avg `0.0271`, median `0.0305`, brier `0.1187`, calibration_gap `-0.0772`
- 60d: hit_rate `1.0000`, avg `0.0429`, median `0.0501`, brier `0.0409`, calibration_gap `-0.2022`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0033`, median `-0.0013`, brier `0.3311`, calibration_gap `0.2881`
- 5d: hit_rate `0.5000`, avg `-0.0056`, median `-0.0043`, brier `0.3311`, calibration_gap `0.2881`
- 10d: hit_rate `0.5625`, avg `-0.0056`, median `0.0003`, brier `0.3015`, calibration_gap `0.2256`
- 20d: hit_rate `0.6875`, avg `0.0187`, median `0.0240`, brier `0.2241`, calibration_gap `0.1006`
- 60d: hit_rate `0.8125`, avg `0.0335`, median `0.0501`, brier `0.1509`, calibration_gap `-0.0244`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.3375`, avg `-0.0071`, median `-0.0049`, brier `0.3672`, calibration_gap `0.3740`
- 5d: hit_rate `0.4000`, avg `-0.0109`, median `-0.0132`, brier `0.3420`, calibration_gap `0.3115`
- 10d: hit_rate `0.4375`, avg `-0.0102`, median `-0.0070`, brier `0.3281`, calibration_gap `0.2740`
- 20d: hit_rate `0.5750`, avg `0.0089`, median `0.0157`, brier `0.2632`, calibration_gap `0.1365`
- 60d: hit_rate `0.7500`, avg `0.0307`, median `0.0464`, brier `0.1872`, calibration_gap `-0.0385`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0046`, median `0.0040`, brier `0.2368`, calibration_gap `0.0275`
- 5d: hit_rate `0.6875`, avg `0.0018`, median `0.0036`, brier `0.2189`, calibration_gap `-0.0350`
- 10d: hit_rate `0.7500`, avg `0.0033`, median `0.0086`, brier `0.1983`, calibration_gap `-0.0975`
- 20d: hit_rate `0.5625`, avg `0.0007`, median `0.0067`, brier `0.2532`, calibration_gap `0.0900`
- 60d: hit_rate `0.6875`, avg `0.0079`, median `0.0290`, brier `0.2169`, calibration_gap `-0.0350`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
