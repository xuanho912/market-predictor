# High Confidence Signal Report

Generated at: `2026-11-13T03:00:34.091136+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.0000`, avg `-0.0138`, median `-0.0114`, brier `0.6429`, calibration_gap `0.8016`
- 5d: hit_rate `0.6250`, avg `-0.0055`, median `0.0011`, brier `0.2651`, calibration_gap `0.1766`
- 10d: hit_rate `0.0000`, avg `-0.0128`, median `-0.0128`, brier `0.6429`, calibration_gap `0.8016`
- 20d: hit_rate `0.3750`, avg `-0.0126`, median `-0.0227`, brier `0.4275`, calibration_gap `0.4266`
- 60d: hit_rate `0.1250`, avg `-0.0460`, median `-0.0556`, brier `0.5682`, calibration_gap `0.6766`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.1875`, avg `-0.0081`, median `-0.0090`, brier `0.5124`, calibration_gap `0.5945`
- 5d: hit_rate `0.5000`, avg `-0.0057`, median `-0.0007`, brier `0.3235`, calibration_gap `0.2820`
- 10d: hit_rate `0.1875`, avg `-0.0095`, median `-0.0105`, brier `0.5153`, calibration_gap `0.5945`
- 20d: hit_rate `0.5000`, avg `0.0006`, median `-0.0001`, brier `0.3418`, calibration_gap `0.2820`
- 60d: hit_rate `0.1250`, avg `-0.0322`, median `-0.0510`, brier `0.5418`, calibration_gap `0.6570`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6500`, avg `0.0063`, median `0.0084`, brier `0.2304`, calibration_gap `0.0156`
- 5d: hit_rate `0.6750`, avg `0.0092`, median `0.0108`, brier `0.2277`, calibration_gap `-0.0094`
- 10d: hit_rate `0.5750`, avg `0.0079`, median `0.0062`, brier `0.2646`, calibration_gap `0.0906`
- 20d: hit_rate `0.7500`, avg `0.0201`, median `0.0162`, brier `0.2006`, calibration_gap `-0.0844`
- 60d: hit_rate `0.5500`, avg `0.0102`, median `0.0043`, brier `0.2654`, calibration_gap `0.1156`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0098`, median `0.0118`, brier `0.2167`, calibration_gap `-0.0403`
- 5d: hit_rate `0.8750`, avg `0.0194`, median `0.0162`, brier `0.1615`, calibration_gap `-0.2278`
- 10d: hit_rate `0.8125`, avg `0.0247`, median `0.0267`, brier `0.1784`, calibration_gap `-0.1653`
- 20d: hit_rate `0.8750`, avg `0.0323`, median `0.0306`, brier `0.1614`, calibration_gap `-0.2278`
- 60d: hit_rate `0.6250`, avg `0.0030`, median `0.0482`, brier `0.2339`, calibration_gap `0.0222`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
