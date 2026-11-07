# High Confidence Signal Report

Generated at: `2026-11-07T10:42:54.029959+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0139`, median `0.0149`, brier `0.1954`, calibration_gap `0.0472`
- 5d: hit_rate `0.8750`, avg `0.0173`, median `0.0140`, brier `0.1157`, calibration_gap `-0.0778`
- 10d: hit_rate `0.3750`, avg `-0.0036`, median `-0.0122`, brier `0.4087`, calibration_gap `0.4222`
- 20d: hit_rate `0.7500`, avg `0.0071`, median `0.0267`, brier `0.1954`, calibration_gap `0.0472`
- 60d: hit_rate `0.8750`, avg `0.0567`, median `0.0710`, brier `0.1210`, calibration_gap `-0.0778`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0114`, median `0.0114`, brier `0.2265`, calibration_gap `0.0995`
- 5d: hit_rate `0.6875`, avg `0.0134`, median `0.0134`, brier `0.2218`, calibration_gap `0.0995`
- 10d: hit_rate `0.5625`, avg `0.0127`, median `0.0207`, brier `0.2984`, calibration_gap `0.2245`
- 20d: hit_rate `0.8125`, avg `0.0209`, median `0.0306`, brier `0.1574`, calibration_gap `-0.0255`
- 60d: hit_rate `0.9375`, avg `0.0721`, median `0.0710`, brier `0.0854`, calibration_gap `-0.1505`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.6500`, avg `0.0104`, median `0.0114`, brier `0.2463`, calibration_gap `0.1337`
- 5d: hit_rate `0.6500`, avg `0.0145`, median `0.0134`, brier `0.2425`, calibration_gap `0.1337`
- 10d: hit_rate `0.6000`, avg `0.0177`, median `0.0207`, brier `0.2764`, calibration_gap `0.1837`
- 20d: hit_rate `0.8000`, avg `0.0235`, median `0.0306`, brier `0.1638`, calibration_gap `-0.0163`
- 60d: hit_rate `0.9500`, avg `0.0735`, median `0.0732`, brier `0.0789`, calibration_gap `-0.1663`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0052`, median `0.0115`, brier `0.2176`, calibration_gap `-0.0710`
- 5d: hit_rate `0.7500`, avg `0.0173`, median `0.0281`, brier `0.2020`, calibration_gap `-0.1335`
- 10d: hit_rate `0.8125`, avg `0.0238`, median `0.0393`, brier `0.1882`, calibration_gap `-0.1960`
- 20d: hit_rate `0.7500`, avg `0.0211`, median `0.0509`, brier `0.2036`, calibration_gap `-0.1335`
- 60d: hit_rate `0.8125`, avg `0.0722`, median `0.0865`, brier `0.1882`, calibration_gap `-0.1960`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
