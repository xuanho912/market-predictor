# High Confidence Signal Report

Generated at: `2026-10-29T02:23:43.114351+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `0.0029`, median `-0.0001`, brier `0.3074`, calibration_gap `0.2386`
- 5d: hit_rate `0.3750`, avg `0.0046`, median `-0.0085`, brier `0.3714`, calibration_gap `0.3636`
- 10d: hit_rate `0.8750`, avg `0.0213`, median `0.0188`, brier `0.1268`, calibration_gap `-0.1364`
- 20d: hit_rate `0.6250`, avg `0.0196`, median `0.0221`, brier `0.2444`, calibration_gap `0.1136`
- 60d: hit_rate `0.8750`, avg `0.0651`, median `0.0831`, brier `0.1278`, calibration_gap `-0.1364`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0015`, median `-0.0001`, brier `0.3042`, calibration_gap `0.2315`
- 5d: hit_rate `0.4375`, avg `-0.0000`, median `-0.0085`, brier `0.3362`, calibration_gap `0.2940`
- 10d: hit_rate `0.6875`, avg `0.0048`, median `0.0079`, brier `0.2128`, calibration_gap `0.0440`
- 20d: hit_rate `0.6875`, avg `0.0153`, median `0.0197`, brier `0.2156`, calibration_gap `0.0440`
- 60d: hit_rate `0.8125`, avg `0.0553`, median `0.0670`, brier `0.1580`, calibration_gap `-0.0810`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6333`, avg `0.0045`, median `0.0047`, brier `0.2368`, calibration_gap `0.0467`
- 5d: hit_rate `0.6167`, avg `0.0071`, median `0.0087`, brier `0.2480`, calibration_gap `0.0633`
- 10d: hit_rate `0.7833`, avg `0.0160`, median `0.0196`, brier `0.1862`, calibration_gap `-0.1033`
- 20d: hit_rate `0.7500`, avg `0.0209`, median `0.0284`, brier `0.1863`, calibration_gap `-0.0700`
- 60d: hit_rate `0.7167`, avg `0.0319`, median `0.0552`, brier `0.2007`, calibration_gap `-0.0367`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0025`, median `0.0039`, brier `0.2528`, calibration_gap `0.0766`
- 5d: hit_rate `0.6875`, avg `0.0073`, median `0.0112`, brier `0.2181`, calibration_gap `-0.0484`
- 10d: hit_rate `0.8750`, avg `0.0177`, median `0.0187`, brier `0.1644`, calibration_gap `-0.2359`
- 20d: hit_rate `0.5625`, avg `0.0033`, median `0.0172`, brier `0.2503`, calibration_gap `0.0766`
- 60d: hit_rate `0.7500`, avg `0.0178`, median `0.0504`, brier `0.1971`, calibration_gap `-0.1109`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
