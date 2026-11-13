# High Confidence Signal Report

Generated at: `2026-11-13T11:34:44.677176+00:00`

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
- sample_size: `60`
- 3d: hit_rate `0.5333`, avg `0.0030`, median `0.0027`, brier `0.2945`, calibration_gap `0.1608`
- 5d: hit_rate `0.6667`, avg `0.0061`, median `0.0045`, brier `0.2294`, calibration_gap `0.0275`
- 10d: hit_rate `0.5333`, avg `0.0044`, median `0.0019`, brier `0.2943`, calibration_gap `0.1608`
- 20d: hit_rate `0.6667`, avg `0.0139`, median `0.0131`, brier `0.2391`, calibration_gap `0.0275`
- 60d: hit_rate `0.4167`, avg `-0.0041`, median `-0.0121`, brier `0.3420`, calibration_gap `0.2775`

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
