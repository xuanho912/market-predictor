# High Confidence Signal Report

Generated at: `2026-09-03T08:19:30.686741+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0004`, median `0.0022`, brier `0.1895`, calibration_gap `0.0507`
- 5d: hit_rate `0.6250`, avg `-0.0031`, median `0.0010`, brier `0.2640`, calibration_gap `0.1757`
- 10d: hit_rate `0.1250`, avg `-0.0118`, median `-0.0189`, brier `0.5686`, calibration_gap `0.6757`
- 20d: hit_rate `0.6250`, avg `0.0148`, median `0.0105`, brier `0.2713`, calibration_gap `0.1757`
- 60d: hit_rate `0.8750`, avg `0.0528`, median `0.0586`, brier `0.1160`, calibration_gap `-0.0743`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0033`, median `0.0007`, brier `0.2927`, calibration_gap `0.2264`
- 5d: hit_rate `0.4375`, avg `-0.0080`, median `-0.0045`, brier `0.3645`, calibration_gap `0.3514`
- 10d: hit_rate `0.3125`, avg `-0.0063`, median `-0.0127`, brier `0.4480`, calibration_gap `0.4764`
- 20d: hit_rate `0.6250`, avg `0.0049`, median `0.0205`, brier `0.2642`, calibration_gap `0.1639`
- 60d: hit_rate `0.7500`, avg `0.0463`, median `0.0597`, brier `0.1866`, calibration_gap `0.0389`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.7000`, avg `0.0078`, median `0.0103`, brier `0.2128`, calibration_gap `0.0210`
- 5d: hit_rate `0.6500`, avg `0.0098`, median `0.0139`, brier `0.2404`, calibration_gap `0.0710`
- 10d: hit_rate `0.5500`, avg `0.0113`, median `0.0132`, brier `0.2807`, calibration_gap `0.1710`
- 20d: hit_rate `0.7500`, avg `0.0234`, median `0.0236`, brier `0.1913`, calibration_gap `-0.0290`
- 60d: hit_rate `0.9500`, avg `0.0720`, median `0.0665`, brier `0.1005`, calibration_gap `-0.2290`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0081`, median `0.0121`, brier `0.1914`, calibration_gap `-0.0382`
- 5d: hit_rate `0.8125`, avg `0.0150`, median `0.0232`, brier `0.1644`, calibration_gap `-0.1007`
- 10d: hit_rate `0.6875`, avg `0.0156`, median `0.0225`, brier `0.2172`, calibration_gap `0.0243`
- 20d: hit_rate `0.8750`, avg `0.0214`, median `0.0257`, brier `0.1361`, calibration_gap `-0.1632`
- 60d: hit_rate `0.8750`, avg `0.0444`, median `0.0693`, brier `0.1376`, calibration_gap `-0.1632`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
