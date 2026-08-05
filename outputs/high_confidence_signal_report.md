# High Confidence Signal Report

Generated at: `2026-08-05T14:35:57.949514+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0107`, median `0.0147`, brier `0.1291`, calibration_gap `-0.1395`
- 5d: hit_rate `0.8750`, avg `0.0149`, median `0.0155`, brier `0.1291`, calibration_gap `-0.1395`
- 10d: hit_rate `0.8750`, avg `0.0212`, median `0.0208`, brier `0.1291`, calibration_gap `-0.1395`
- 20d: hit_rate `0.6250`, avg `0.0297`, median `0.0257`, brier `0.2506`, calibration_gap `0.1105`
- 60d: hit_rate `0.5000`, avg `0.0302`, median `0.0136`, brier `0.3093`, calibration_gap `0.2355`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0058`, median `0.0068`, brier `0.2143`, calibration_gap `0.0407`
- 5d: hit_rate `0.8125`, avg `0.0120`, median `0.0155`, brier `0.1593`, calibration_gap `-0.0843`
- 10d: hit_rate `0.8125`, avg `0.0189`, median `0.0208`, brier `0.1580`, calibration_gap `-0.0843`
- 20d: hit_rate `0.6875`, avg `0.0205`, median `0.0197`, brier `0.2186`, calibration_gap `0.0407`
- 60d: hit_rate `0.4375`, avg `0.0213`, median `-0.0187`, brier `0.3312`, calibration_gap `0.2907`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6667`, avg `0.0039`, median `0.0093`, brier `0.2230`, calibration_gap `0.0323`
- 5d: hit_rate `0.6500`, avg `0.0050`, median `0.0071`, brier `0.2282`, calibration_gap `0.0489`
- 10d: hit_rate `0.5833`, avg `0.0054`, median `0.0099`, brier `0.2548`, calibration_gap `0.1156`
- 20d: hit_rate `0.7000`, avg `0.0121`, median `0.0155`, brier `0.2087`, calibration_gap `-0.0011`
- 60d: hit_rate `0.6500`, avg `0.0388`, median `0.0557`, brier `0.2325`, calibration_gap `0.0489`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0039`, median `0.0111`, brier `0.2154`, calibration_gap `-0.0068`
- 5d: hit_rate `0.6875`, avg `0.0068`, median `0.0105`, brier `0.2154`, calibration_gap `-0.0068`
- 10d: hit_rate `0.6250`, avg `0.0003`, median `0.0052`, brier `0.2386`, calibration_gap `0.0557`
- 20d: hit_rate `0.6875`, avg `0.0032`, median `0.0194`, brier `0.2150`, calibration_gap `-0.0068`
- 60d: hit_rate `0.7500`, avg `0.0380`, median `0.0627`, brier `0.1916`, calibration_gap `-0.0693`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
