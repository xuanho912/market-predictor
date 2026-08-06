# High Confidence Signal Report

Generated at: `2026-08-06T14:37:34.793981+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0030`, median `0.0069`, brier `0.2415`, calibration_gap `0.1075`
- 5d: hit_rate `0.7500`, avg `0.0053`, median `0.0130`, brier `0.1857`, calibration_gap `-0.0175`
- 10d: hit_rate `0.7500`, avg `0.0095`, median `0.0160`, brier `0.1829`, calibration_gap `-0.0175`
- 20d: hit_rate `0.5000`, avg `0.0064`, median `-0.0030`, brier `0.3072`, calibration_gap `0.2325`
- 60d: hit_rate `0.3750`, avg `0.0007`, median `-0.0274`, brier `0.3658`, calibration_gap `0.3575`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0001`, median `-0.0005`, brier `0.2935`, calibration_gap `0.2211`
- 5d: hit_rate `0.7500`, avg `0.0069`, median `0.0062`, brier `0.1869`, calibration_gap `-0.0289`
- 10d: hit_rate `0.5625`, avg `0.0063`, median `0.0098`, brier `0.2642`, calibration_gap `0.1586`
- 20d: hit_rate `0.5625`, avg `0.0114`, median `0.0048`, brier `0.2742`, calibration_gap `0.1586`
- 60d: hit_rate `0.2500`, avg `-0.0087`, median `-0.0308`, brier `0.4088`, calibration_gap `0.4711`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6000`, avg `0.0022`, median `0.0043`, brier `0.2493`, calibration_gap `0.0925`
- 5d: hit_rate `0.6875`, avg `0.0043`, median `0.0055`, brier `0.2129`, calibration_gap `0.0050`
- 10d: hit_rate `0.5875`, avg `0.0061`, median `0.0065`, brier `0.2530`, calibration_gap `0.1050`
- 20d: hit_rate `0.7000`, avg `0.0136`, median `0.0146`, brier `0.2121`, calibration_gap `-0.0075`
- 60d: hit_rate `0.5625`, avg `0.0245`, median `0.0318`, brier `0.2688`, calibration_gap `0.1300`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0002`, median `0.0024`, brier `0.2582`, calibration_gap `0.1101`
- 5d: hit_rate `0.6875`, avg `0.0001`, median `0.0071`, brier `0.2147`, calibration_gap `-0.0149`
- 10d: hit_rate `0.6875`, avg `0.0024`, median `0.0107`, brier `0.2149`, calibration_gap `-0.0149`
- 20d: hit_rate `0.5625`, avg `-0.0021`, median `0.0092`, brier `0.2588`, calibration_gap `0.1101`
- 60d: hit_rate `0.6875`, avg `0.0298`, median `0.0612`, brier `0.2153`, calibration_gap `-0.0149`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
