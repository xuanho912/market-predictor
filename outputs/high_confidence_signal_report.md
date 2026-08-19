# High Confidence Signal Report

Generated at: `2026-08-19T02:35:21.868275+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `20`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `2`
- 3d: hit_rate `0.5000`, avg `0.0025`, median `0.0025`, brier `0.2773`, calibration_gap `0.1801`
- 5d: hit_rate `0.5000`, avg `0.0046`, median `0.0046`, brier `0.2773`, calibration_gap `0.1801`
- 10d: hit_rate `1.0000`, avg `0.0169`, median `0.0169`, brier `0.1024`, calibration_gap `-0.3199`
- 20d: hit_rate `0.5000`, avg `-0.0009`, median `-0.0009`, brier `0.2773`, calibration_gap `0.1801`
- 60d: hit_rate `0.5000`, avg `-0.0148`, median `-0.0148`, brier `0.2773`, calibration_gap `0.1801`

### top_20_confidence_signals
- sample_size: `4`
- 3d: hit_rate `0.5000`, avg `0.0061`, median `0.0025`, brier `0.2794`, calibration_gap `0.1757`
- 5d: hit_rate `0.7500`, avg `0.0092`, median `0.0084`, brier `0.1926`, calibration_gap `-0.0743`
- 10d: hit_rate `1.0000`, avg `0.0149`, median `0.0169`, brier `0.1052`, calibration_gap `-0.3243`
- 20d: hit_rate `0.5000`, avg `-0.0029`, median `-0.0049`, brier `0.2794`, calibration_gap `0.1757`
- 60d: hit_rate `0.7500`, avg `0.0329`, median `0.0602`, brier `0.1926`, calibration_gap `-0.0743`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.7000`, avg `0.0081`, median `0.0099`, brier `0.2132`, calibration_gap `-0.0391`
- 5d: hit_rate `0.8000`, avg `0.0087`, median `0.0103`, brier `0.1787`, calibration_gap `-0.1391`
- 10d: hit_rate `0.7000`, avg `0.0109`, median `0.0161`, brier `0.2086`, calibration_gap `-0.0391`
- 20d: hit_rate `0.7000`, avg `0.0075`, median `0.0212`, brier `0.2129`, calibration_gap `-0.0391`
- 60d: hit_rate `0.6500`, avg `0.0238`, median `0.0557`, brier `0.2267`, calibration_gap `0.0109`

### low_confidence_reference
- sample_size: `4`
- 3d: hit_rate `0.7500`, avg `0.0062`, median `0.0075`, brier `0.1975`, calibration_gap `-0.0990`
- 5d: hit_rate `0.5000`, avg `-0.0040`, median `-0.0055`, brier `0.2731`, calibration_gap `0.1510`
- 10d: hit_rate `0.2500`, avg `-0.0016`, median `-0.0132`, brier `0.3485`, calibration_gap `0.4010`
- 20d: hit_rate `0.5000`, avg `-0.0156`, median `-0.0039`, brier `0.2728`, calibration_gap `0.1510`
- 60d: hit_rate `0.7500`, avg `-0.0050`, median `0.0636`, brier `0.1974`, calibration_gap `-0.0990`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
