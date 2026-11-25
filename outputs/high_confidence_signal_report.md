# High Confidence Signal Report

Generated at: `2026-11-25T04:34:18.181911+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0083`, median `-0.0051`, brier `0.4228`, calibration_gap `0.4355`
- 5d: hit_rate `0.5000`, avg `0.0048`, median `0.0019`, brier `0.3550`, calibration_gap `0.3105`
- 10d: hit_rate `0.7500`, avg `0.0164`, median `0.0106`, brier `0.1947`, calibration_gap `0.0605`
- 20d: hit_rate `0.5000`, avg `0.0096`, median `0.0010`, brier `0.3481`, calibration_gap `0.3105`
- 60d: hit_rate `0.7500`, avg `0.0459`, median `0.0670`, brier `0.1873`, calibration_gap `0.0605`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0020`, median `-0.0051`, brier `0.4139`, calibration_gap `0.4242`
- 5d: hit_rate `0.5625`, avg `0.0013`, median `0.0036`, brier `0.3079`, calibration_gap `0.2367`
- 10d: hit_rate `0.6875`, avg `0.0080`, median `0.0073`, brier `0.2278`, calibration_gap `0.1117`
- 20d: hit_rate `0.6250`, avg `0.0112`, median `0.0137`, brier `0.2686`, calibration_gap `0.1742`
- 60d: hit_rate `0.6875`, avg `0.0340`, median `0.0580`, brier `0.2238`, calibration_gap `0.1117`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.6000`, avg `0.0067`, median `0.0103`, brier `0.2419`, calibration_gap `0.0238`
- 5d: hit_rate `0.6500`, avg `0.0141`, median `0.0089`, brier `0.2285`, calibration_gap `-0.0262`
- 10d: hit_rate `0.6500`, avg `0.0201`, median `0.0087`, brier `0.2305`, calibration_gap `-0.0262`
- 20d: hit_rate `0.7000`, avg `0.0196`, median `0.0162`, brier `0.2098`, calibration_gap `-0.0762`
- 60d: hit_rate `0.8500`, avg `0.0845`, median `0.0547`, brier `0.1864`, calibration_gap `-0.2262`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0047`, median `0.0070`, brier `0.2491`, calibration_gap `0.0512`
- 5d: hit_rate `0.5625`, avg `0.0098`, median `0.0068`, brier `0.2490`, calibration_gap `0.0512`
- 10d: hit_rate `0.6250`, avg `0.0131`, median `0.0075`, brier `0.2347`, calibration_gap `-0.0113`
- 20d: hit_rate `0.5000`, avg `-0.0044`, median `-0.0011`, brier `0.2645`, calibration_gap `0.1137`
- 60d: hit_rate `1.0000`, avg `0.0842`, median `0.0707`, brier `0.1493`, calibration_gap `-0.3863`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
