# High Confidence Signal Report

Generated at: `2026-11-19T02:06:16.424352+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `0.0003`, median `0.0024`, brier `0.3171`, calibration_gap `0.2496`
- 5d: hit_rate `0.3750`, avg `-0.0009`, median `-0.0116`, brier `0.3931`, calibration_gap `0.3746`
- 10d: hit_rate `0.3750`, avg `-0.0095`, median `-0.0200`, brier `0.3931`, calibration_gap `0.3746`
- 20d: hit_rate `0.8750`, avg `0.0209`, median `0.0226`, brier `0.1219`, calibration_gap `-0.1254`
- 60d: hit_rate `0.8750`, avg `0.0707`, median `0.0776`, brier `0.1194`, calibration_gap `-0.1254`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0054`, median `-0.0082`, brier `0.3837`, calibration_gap `0.4173`
- 5d: hit_rate `0.2500`, avg `-0.0098`, median `-0.0150`, brier `0.4233`, calibration_gap `0.4798`
- 10d: hit_rate `0.3125`, avg `-0.0100`, median `-0.0150`, brier `0.3963`, calibration_gap `0.4173`
- 20d: hit_rate `0.8125`, avg `0.0277`, median `0.0330`, brier `0.1557`, calibration_gap `-0.0827`
- 60d: hit_rate `0.9375`, avg `0.0851`, median `0.0851`, brier `0.1018`, calibration_gap `-0.2077`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.5500`, avg `0.0055`, median `0.0052`, brier `0.2543`, calibration_gap `0.0134`
- 5d: hit_rate `0.5000`, avg `0.0018`, median `-0.0061`, brier `0.2685`, calibration_gap `0.0634`
- 10d: hit_rate `0.5500`, avg `0.0111`, median `0.0082`, brier `0.2632`, calibration_gap `0.0134`
- 20d: hit_rate `0.7000`, avg `0.0289`, median `0.0383`, brier `0.2222`, calibration_gap `-0.1366`
- 60d: hit_rate `0.7500`, avg `0.0906`, median `0.1185`, brier `0.2118`, calibration_gap `-0.1866`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0087`, median `0.0086`, brier `0.2429`, calibration_gap `-0.2381`
- 5d: hit_rate `0.6250`, avg `0.0131`, median `0.0128`, brier `0.2464`, calibration_gap `-0.1131`
- 10d: hit_rate `0.6875`, avg `0.0239`, median `0.0361`, brier `0.2445`, calibration_gap `-0.1756`
- 20d: hit_rate `0.6875`, avg `0.0550`, median `0.0553`, brier `0.2449`, calibration_gap `-0.1756`
- 60d: hit_rate `1.0000`, avg `0.1582`, median `0.1580`, brier `0.2384`, calibration_gap `-0.4881`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
