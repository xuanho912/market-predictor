# High Confidence Signal Report

Generated at: `2026-10-14T17:14:59.822006+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0071`, median `-0.0001`, brier `0.3155`, calibration_gap `0.2572`
- 5d: hit_rate `0.6250`, avg `0.0008`, median `0.0084`, brier `0.2529`, calibration_gap `0.1322`
- 10d: hit_rate `0.3750`, avg `-0.0033`, median `-0.0051`, brier `0.3794`, calibration_gap `0.3822`
- 20d: hit_rate `0.8750`, avg `0.0311`, median `0.0361`, brier `0.1229`, calibration_gap `-0.1178`
- 60d: hit_rate `1.0000`, avg `0.0526`, median `0.0501`, brier `0.0590`, calibration_gap `-0.2428`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0038`, median `-0.0001`, brier `0.3134`, calibration_gap `0.2515`
- 5d: hit_rate `0.5625`, avg `-0.0042`, median `0.0048`, brier `0.2821`, calibration_gap `0.1890`
- 10d: hit_rate `0.4375`, avg `-0.0052`, median `-0.0051`, brier `0.3444`, calibration_gap `0.3140`
- 20d: hit_rate `0.7500`, avg `0.0254`, median `0.0289`, brier `0.1865`, calibration_gap `0.0015`
- 60d: hit_rate `0.8750`, avg `0.0447`, median `0.0463`, brier `0.1237`, calibration_gap `-0.1235`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.4000`, avg `-0.0087`, median `-0.0101`, brier `0.3509`, calibration_gap `0.3298`
- 5d: hit_rate `0.3500`, avg `-0.0145`, median `-0.0162`, brier `0.3695`, calibration_gap `0.3798`
- 10d: hit_rate `0.3000`, avg `-0.0074`, median `-0.0109`, brier `0.3976`, calibration_gap `0.4298`
- 20d: hit_rate `0.6000`, avg `0.0120`, median `0.0193`, brier `0.2519`, calibration_gap `0.1298`
- 60d: hit_rate `0.7500`, avg `0.0465`, median `0.0593`, brier `0.1849`, calibration_gap `-0.0202`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0067`, median `-0.0121`, brier `0.3391`, calibration_gap `0.3555`
- 5d: hit_rate `0.1875`, avg `-0.0138`, median `-0.0219`, brier `0.3831`, calibration_gap `0.4805`
- 10d: hit_rate `0.4375`, avg `-0.0101`, median `-0.0194`, brier `0.2981`, calibration_gap `0.2305`
- 20d: hit_rate `0.4375`, avg `0.0060`, median `-0.0047`, brier `0.2976`, calibration_gap `0.2305`
- 60d: hit_rate `0.7500`, avg `0.0585`, median `0.0724`, brier `0.1958`, calibration_gap `-0.0820`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
