# High Confidence Signal Report

Generated at: `2026-08-28T15:41:45.815485+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0055`, median `0.0012`, brier `0.2513`, calibration_gap `0.1157`
- 5d: hit_rate `0.6250`, avg `-0.0012`, median `0.0036`, brier `0.2496`, calibration_gap `0.1157`
- 10d: hit_rate `0.2500`, avg `-0.0104`, median `-0.0146`, brier `0.4294`, calibration_gap `0.4907`
- 20d: hit_rate `0.6250`, avg `0.0088`, median `0.0154`, brier `0.2451`, calibration_gap `0.1157`
- 60d: hit_rate `0.7500`, avg `0.0255`, median `0.0314`, brier `0.1848`, calibration_gap `-0.0093`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0017`, median `0.0007`, brier `0.2773`, calibration_gap `0.1718`
- 5d: hit_rate `0.6250`, avg `0.0006`, median `0.0011`, brier `0.2476`, calibration_gap `0.1093`
- 10d: hit_rate `0.3750`, avg `-0.0051`, median `-0.0093`, brier `0.3659`, calibration_gap `0.3593`
- 20d: hit_rate `0.6875`, avg `0.0085`, median `0.0159`, brier `0.2166`, calibration_gap `0.0468`
- 60d: hit_rate `0.6875`, avg `0.0256`, median `0.0314`, brier `0.2154`, calibration_gap `0.0468`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5333`, avg `-0.0020`, median `0.0017`, brier `0.2771`, calibration_gap `0.1641`
- 5d: hit_rate `0.5333`, avg `-0.0005`, median `0.0022`, brier `0.2775`, calibration_gap `0.1641`
- 10d: hit_rate `0.5833`, avg `0.0071`, median `0.0110`, brier `0.2591`, calibration_gap `0.1141`
- 20d: hit_rate `0.7000`, avg `0.0152`, median `0.0170`, brier `0.2091`, calibration_gap `-0.0026`
- 60d: hit_rate `0.6833`, avg `0.0379`, median `0.0479`, brier `0.2186`, calibration_gap `0.0141`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0016`, median `0.0094`, brier `0.2618`, calibration_gap `0.1101`
- 5d: hit_rate `0.5625`, avg `0.0019`, median `0.0070`, brier `0.2619`, calibration_gap `0.1101`
- 10d: hit_rate `0.7500`, avg `0.0154`, median `0.0130`, brier `0.1932`, calibration_gap `-0.0774`
- 20d: hit_rate `0.7500`, avg `0.0278`, median `0.0139`, brier `0.1954`, calibration_gap `-0.0774`
- 60d: hit_rate `0.8125`, avg `0.0668`, median `0.0793`, brier `0.1727`, calibration_gap `-0.1399`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
