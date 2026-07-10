# High Confidence Signal Report

Generated at: `2026-07-10T15:04:32.643028+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0033`, median `-0.0009`, brier `0.3500`, calibration_gap `0.3380`
- 5d: hit_rate `0.5000`, avg `-0.0005`, median `0.0019`, brier `0.2989`, calibration_gap `0.2130`
- 10d: hit_rate `0.6250`, avg `0.0051`, median `0.0082`, brier `0.2455`, calibration_gap `0.0880`
- 20d: hit_rate `0.6250`, avg `0.0024`, median `0.0069`, brier `0.2416`, calibration_gap `0.0880`
- 60d: hit_rate `0.2500`, avg `-0.0329`, median `-0.0398`, brier `0.3964`, calibration_gap `0.4630`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0004`, median `0.0019`, brier `0.2954`, calibration_gap `0.2068`
- 5d: hit_rate `0.5000`, avg `0.0016`, median `0.0019`, brier `0.2949`, calibration_gap `0.2068`
- 10d: hit_rate `0.5000`, avg `0.0005`, median `0.0036`, brier `0.2928`, calibration_gap `0.2068`
- 20d: hit_rate `0.6250`, avg `-0.0003`, median `0.0083`, brier `0.2412`, calibration_gap `0.0818`
- 60d: hit_rate `0.3750`, avg `-0.0081`, median `-0.0305`, brier `0.3436`, calibration_gap `0.3318`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5000`, avg `-0.0023`, median `-0.0001`, brier `0.2864`, calibration_gap `0.1848`
- 5d: hit_rate `0.5333`, avg `-0.0025`, median `0.0028`, brier `0.2726`, calibration_gap `0.1515`
- 10d: hit_rate `0.5333`, avg `0.0029`, median `0.0025`, brier `0.2745`, calibration_gap `0.1515`
- 20d: hit_rate `0.7000`, avg `0.0078`, median `0.0126`, brier `0.2119`, calibration_gap `-0.0152`
- 60d: hit_rate `0.5500`, avg `0.0118`, median `0.0271`, brier `0.2689`, calibration_gap `0.1348`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0001`, median `0.0041`, brier `0.2566`, calibration_gap `0.0988`
- 5d: hit_rate `0.5000`, avg `-0.0005`, median `-0.0014`, brier `0.2773`, calibration_gap `0.1613`
- 10d: hit_rate `0.6250`, avg `0.0045`, median `0.0048`, brier `0.2361`, calibration_gap `0.0363`
- 20d: hit_rate `0.7500`, avg `0.0082`, median `0.0089`, brier `0.1954`, calibration_gap `-0.0887`
- 60d: hit_rate `0.6875`, avg `0.0343`, median `0.0392`, brier `0.2160`, calibration_gap `-0.0262`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
