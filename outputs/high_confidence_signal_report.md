# High Confidence Signal Report

Generated at: `2026-08-20T21:58:16.606308+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0048`, median `0.0027`, brier `0.1908`, calibration_gap `-0.0262`
- 5d: hit_rate `0.8750`, avg `0.0068`, median `0.0069`, brier `0.1308`, calibration_gap `-0.1512`
- 10d: hit_rate `0.6250`, avg `0.0058`, median `0.0187`, brier `0.2450`, calibration_gap `0.0988`
- 20d: hit_rate `0.3750`, avg `-0.0012`, median `-0.0075`, brier `0.3551`, calibration_gap `0.3488`
- 60d: hit_rate `0.5000`, avg `0.0061`, median `-0.0017`, brier `0.3009`, calibration_gap `0.2238`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `-0.0003`, median `0.0007`, brier `0.2152`, calibration_gap `0.0277`
- 5d: hit_rate `0.7500`, avg `0.0015`, median `0.0052`, brier `0.1850`, calibration_gap `-0.0348`
- 10d: hit_rate `0.5000`, avg `-0.0017`, median `0.0025`, brier `0.2939`, calibration_gap `0.2152`
- 20d: hit_rate `0.3750`, avg `-0.0059`, median `-0.0055`, brier `0.3506`, calibration_gap `0.3402`
- 60d: hit_rate `0.4375`, avg `0.0038`, median `-0.0108`, brier `0.3225`, calibration_gap `0.2777`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6667`, avg `0.0047`, median `0.0080`, brier `0.2243`, calibration_gap `0.0028`
- 5d: hit_rate `0.6500`, avg `0.0054`, median `0.0050`, brier `0.2301`, calibration_gap `0.0195`
- 10d: hit_rate `0.6000`, avg `0.0085`, median `0.0113`, brier `0.2436`, calibration_gap `0.0695`
- 20d: hit_rate `0.7000`, avg `0.0161`, median `0.0153`, brier `0.2115`, calibration_gap `-0.0305`
- 60d: hit_rate `0.6833`, avg `0.0357`, median `0.0498`, brier `0.2215`, calibration_gap `-0.0138`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.8125`, avg `0.0064`, median `0.0097`, brier `0.1784`, calibration_gap `-0.1618`
- 5d: hit_rate `0.8750`, avg `0.0104`, median `0.0143`, brier `0.1596`, calibration_gap `-0.2243`
- 10d: hit_rate `0.5625`, avg `0.0060`, median `0.0058`, brier `0.2539`, calibration_gap `0.0882`
- 20d: hit_rate `0.5625`, avg `0.0023`, median `0.0108`, brier `0.2534`, calibration_gap `0.0882`
- 60d: hit_rate `0.7500`, avg `0.0275`, median `0.0459`, brier `0.1969`, calibration_gap `-0.0993`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
