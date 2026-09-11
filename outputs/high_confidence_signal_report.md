# High Confidence Signal Report

Generated at: `2026-09-11T16:31:46.565551+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0024`, median `0.0014`, brier `0.1879`, calibration_gap `0.0382`
- 5d: hit_rate `0.5000`, avg `-0.0019`, median `-0.0009`, brier `0.3270`, calibration_gap `0.2882`
- 10d: hit_rate `0.2500`, avg `-0.0095`, median `-0.0136`, brier `0.4847`, calibration_gap `0.5382`
- 20d: hit_rate `0.5000`, avg `0.0026`, median `0.0084`, brier `0.3410`, calibration_gap `0.2882`
- 60d: hit_rate `0.7500`, avg `0.0389`, median `0.0588`, brier `0.1870`, calibration_gap `0.0382`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0038`, median `0.0004`, brier `0.2836`, calibration_gap `0.2095`
- 5d: hit_rate `0.5000`, avg `-0.0087`, median `-0.0009`, brier `0.3209`, calibration_gap `0.2720`
- 10d: hit_rate `0.2500`, avg `-0.0123`, median `-0.0189`, brier `0.4641`, calibration_gap `0.5220`
- 20d: hit_rate `0.4375`, avg `-0.0066`, median `-0.0016`, brier `0.3591`, calibration_gap `0.3345`
- 60d: hit_rate `0.5000`, avg `0.0107`, median `0.0150`, brier `0.3136`, calibration_gap `0.2720`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5250`, avg `-0.0033`, median `0.0018`, brier `0.2872`, calibration_gap `0.1759`
- 5d: hit_rate `0.5250`, avg `-0.0047`, median `0.0007`, brier `0.2895`, calibration_gap `0.1759`
- 10d: hit_rate `0.4500`, avg `0.0063`, median `-0.0020`, brier `0.3250`, calibration_gap `0.2509`
- 20d: hit_rate `0.7000`, avg `0.0237`, median `0.0300`, brier `0.2184`, calibration_gap `0.0009`
- 60d: hit_rate `0.6750`, avg `0.0418`, median `0.0618`, brier `0.2240`, calibration_gap `0.0259`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0030`, median `0.0090`, brier `0.2324`, calibration_gap `0.0400`
- 5d: hit_rate `0.6875`, avg `0.0059`, median `0.0052`, brier `0.2155`, calibration_gap `-0.0225`
- 10d: hit_rate `0.6250`, avg `0.0166`, median `0.0169`, brier `0.2363`, calibration_gap `0.0400`
- 20d: hit_rate `0.8750`, avg `0.0328`, median `0.0323`, brier `0.1524`, calibration_gap `-0.2100`
- 60d: hit_rate `0.6875`, avg `0.0348`, median `0.0565`, brier `0.2165`, calibration_gap `-0.0225`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
