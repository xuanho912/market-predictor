# High Confidence Signal Report

Generated at: `2026-09-23T09:08:45.705895+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0067`, median `0.0116`, brier `0.1846`, calibration_gap `-0.0631`
- 5d: hit_rate `0.7500`, avg `0.0036`, median `0.0089`, brier `0.2045`, calibration_gap `-0.0631`
- 10d: hit_rate `0.6250`, avg `-0.0009`, median `0.0021`, brier `0.2463`, calibration_gap `0.0619`
- 20d: hit_rate `0.8750`, avg `0.0422`, median `0.0548`, brier `0.1428`, calibration_gap `-0.1881`
- 60d: hit_rate `0.8750`, avg `0.0683`, median `0.0751`, brier `0.1604`, calibration_gap `-0.1881`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0001`, median `0.0047`, brier `0.2276`, calibration_gap `0.0397`
- 5d: hit_rate `0.5625`, avg `-0.0030`, median `0.0073`, brier `0.2556`, calibration_gap `0.1022`
- 10d: hit_rate `0.5625`, avg `-0.0043`, median `0.0002`, brier `0.2584`, calibration_gap `0.1022`
- 20d: hit_rate `0.8750`, avg `0.0323`, median `0.0445`, brier `0.1528`, calibration_gap `-0.2103`
- 60d: hit_rate `0.9375`, avg `0.0710`, median `0.0738`, brier `0.1441`, calibration_gap `-0.2728`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6250`, avg `0.0053`, median `0.0108`, brier `0.2347`, calibration_gap `-0.0237`
- 5d: hit_rate `0.6125`, avg `0.0059`, median `0.0109`, brier `0.2418`, calibration_gap `-0.0112`
- 10d: hit_rate `0.6125`, avg `0.0087`, median `0.0119`, brier `0.2449`, calibration_gap `-0.0112`
- 20d: hit_rate `0.7875`, avg `0.0313`, median `0.0326`, brier `0.2022`, calibration_gap `-0.1862`
- 60d: hit_rate `0.8250`, avg `0.0660`, median `0.0793`, brier `0.1965`, calibration_gap `-0.2237`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0003`, median `0.0007`, brier `0.2527`, calibration_gap `0.0478`
- 5d: hit_rate `0.5625`, avg `0.0030`, median `0.0090`, brier `0.2482`, calibration_gap `-0.0147`
- 10d: hit_rate `0.6250`, avg `0.0070`, median `0.0281`, brier `0.2451`, calibration_gap `-0.0772`
- 20d: hit_rate `0.7500`, avg `0.0260`, median `0.0320`, brier `0.2335`, calibration_gap `-0.2022`
- 60d: hit_rate `0.8750`, avg `0.0815`, median `0.0817`, brier `0.2176`, calibration_gap `-0.3272`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
