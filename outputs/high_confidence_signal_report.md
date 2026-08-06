# High Confidence Signal Report

Generated at: `2026-08-06T00:09:50.772869+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0090`, median `0.0104`, brier `0.1284`, calibration_gap `-0.1317`
- 5d: hit_rate `0.8750`, avg `0.0112`, median `0.0155`, brier `0.1284`, calibration_gap `-0.1317`
- 10d: hit_rate `0.8750`, avg `0.0147`, median `0.0208`, brier `0.1284`, calibration_gap `-0.1317`
- 20d: hit_rate `0.6250`, avg `0.0140`, median `0.0178`, brier `0.2496`, calibration_gap `0.1183`
- 60d: hit_rate `0.3750`, avg `0.0040`, median `-0.0236`, brier `0.3709`, calibration_gap `0.3683`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0055`, median `0.0091`, brier `0.2156`, calibration_gap `0.0487`
- 5d: hit_rate `0.8125`, avg `0.0120`, median `0.0155`, brier `0.1590`, calibration_gap `-0.0763`
- 10d: hit_rate `0.8125`, avg `0.0185`, median `0.0208`, brier `0.1577`, calibration_gap `-0.0763`
- 20d: hit_rate `0.7500`, avg `0.0216`, median `0.0241`, brier `0.1895`, calibration_gap `-0.0138`
- 60d: hit_rate `0.4375`, avg `0.0178`, median `-0.0196`, brier `0.3363`, calibration_gap `0.2987`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6000`, avg `0.0014`, median `0.0038`, brier `0.2502`, calibration_gap `0.1057`
- 5d: hit_rate `0.6625`, avg `0.0035`, median `0.0052`, brier `0.2224`, calibration_gap `0.0432`
- 10d: hit_rate `0.5500`, avg `0.0042`, median `0.0052`, brier `0.2697`, calibration_gap `0.1557`
- 20d: hit_rate `0.6875`, avg `0.0095`, median `0.0131`, brier `0.2143`, calibration_gap `0.0182`
- 60d: hit_rate `0.5375`, avg `0.0211`, median `0.0191`, brier `0.2806`, calibration_gap `0.1682`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0056`, median `-0.0020`, brier `0.3072`, calibration_gap `0.2468`
- 5d: hit_rate `0.4375`, avg `-0.0061`, median `-0.0042`, brier `0.3086`, calibration_gap `0.2468`
- 10d: hit_rate `0.5625`, avg `-0.0070`, median `0.0025`, brier `0.2628`, calibration_gap `0.1218`
- 20d: hit_rate `0.6250`, avg `-0.0113`, median `0.0134`, brier `0.2366`, calibration_gap `0.0593`
- 60d: hit_rate `0.6875`, avg `0.0250`, median `0.0506`, brier `0.2152`, calibration_gap `-0.0032`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
