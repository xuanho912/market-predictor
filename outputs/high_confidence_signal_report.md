# High Confidence Signal Report

Generated at: `2026-08-24T21:58:53.957564+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0009`, median `0.0012`, brier `0.1967`, calibration_gap `0.0129`
- 5d: hit_rate `0.5000`, avg `-0.0056`, median `-0.0048`, brier `0.3133`, calibration_gap `0.2629`
- 10d: hit_rate `0.3750`, avg `-0.0089`, median `-0.0134`, brier `0.3908`, calibration_gap `0.3879`
- 20d: hit_rate `0.5000`, avg `-0.0001`, median `0.0047`, brier `0.3163`, calibration_gap `0.2629`
- 60d: hit_rate `0.8750`, avg `0.0421`, median `0.0588`, brier `0.1221`, calibration_gap `-0.1121`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `-0.0006`, median `0.0018`, brier `0.2223`, calibration_gap `0.0637`
- 5d: hit_rate `0.4375`, avg `-0.0056`, median `-0.0045`, brier `0.3409`, calibration_gap `0.3137`
- 10d: hit_rate `0.3125`, avg `-0.0064`, median `-0.0188`, brier `0.4099`, calibration_gap `0.4387`
- 20d: hit_rate `0.5625`, avg `-0.0008`, median `0.0066`, brier `0.2817`, calibration_gap `0.1887`
- 60d: hit_rate `0.6250`, avg `0.0207`, median `0.0396`, brier `0.2448`, calibration_gap `0.1262`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5333`, avg `0.0008`, median `0.0019`, brier `0.2717`, calibration_gap `0.1663`
- 5d: hit_rate `0.5500`, avg `0.0021`, median `0.0016`, brier `0.2681`, calibration_gap `0.1496`
- 10d: hit_rate `0.5667`, avg `0.0080`, median `0.0100`, brier `0.2622`, calibration_gap `0.1329`
- 20d: hit_rate `0.7167`, avg `0.0156`, median `0.0260`, brier `0.2021`, calibration_gap `-0.0171`
- 60d: hit_rate `0.7667`, avg `0.0365`, median `0.0417`, brier `0.1886`, calibration_gap `-0.0671`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0039`, median `-0.0080`, brier `0.2997`, calibration_gap `0.2332`
- 5d: hit_rate `0.5000`, avg `0.0020`, median `0.0003`, brier `0.2782`, calibration_gap `0.1707`
- 10d: hit_rate `0.5000`, avg `0.0029`, median `0.0015`, brier `0.2798`, calibration_gap `0.1707`
- 20d: hit_rate `0.6875`, avg `0.0139`, median `0.0091`, brier `0.2163`, calibration_gap `-0.0168`
- 60d: hit_rate `0.9375`, avg `0.0676`, median `0.0547`, brier `0.1308`, calibration_gap `-0.2668`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
