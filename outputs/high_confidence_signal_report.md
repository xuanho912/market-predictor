# High Confidence Signal Report

Generated at: `2026-09-09T23:30:56.094825+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0009`, median `-0.0004`, brier `0.3306`, calibration_gap `0.3004`
- 5d: hit_rate `0.5000`, avg `-0.0029`, median `-0.0009`, brier `0.3353`, calibration_gap `0.3004`
- 10d: hit_rate `0.1250`, avg `-0.0160`, median `-0.0204`, brier `0.5692`, calibration_gap `0.6754`
- 20d: hit_rate `0.3750`, avg `-0.0131`, median `-0.0055`, brier `0.4164`, calibration_gap `0.4254`
- 60d: hit_rate `0.6250`, avg `0.0207`, median `0.0453`, brier `0.2573`, calibration_gap `0.1754`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0038`, median `-0.0026`, brier `0.3951`, calibration_gap `0.4110`
- 5d: hit_rate `0.4375`, avg `-0.0075`, median `-0.0045`, brier `0.3639`, calibration_gap `0.3485`
- 10d: hit_rate `0.3125`, avg `-0.0078`, median `-0.0095`, brier `0.4454`, calibration_gap `0.4735`
- 20d: hit_rate `0.5625`, avg `-0.0035`, median `0.0122`, brier `0.3007`, calibration_gap `0.2235`
- 60d: hit_rate `0.6875`, avg `0.0292`, median `0.0519`, brier `0.2212`, calibration_gap `0.0985`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6333`, avg `0.0034`, median `0.0061`, brier `0.2452`, calibration_gap `0.0845`
- 5d: hit_rate `0.6333`, avg `0.0050`, median `0.0080`, brier `0.2434`, calibration_gap `0.0845`
- 10d: hit_rate `0.4667`, avg `0.0058`, median `-0.0022`, brier `0.3187`, calibration_gap `0.2512`
- 20d: hit_rate `0.7167`, avg `0.0203`, median `0.0276`, brier `0.2088`, calibration_gap `0.0012`
- 60d: hit_rate `0.8000`, avg `0.0512`, median `0.0618`, brier `0.1689`, calibration_gap `-0.0822`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0088`, median `0.0100`, brier `0.1912`, calibration_gap `-0.0678`
- 5d: hit_rate `0.6250`, avg `0.0117`, median `0.0119`, brier `0.2357`, calibration_gap `0.0572`
- 10d: hit_rate `0.6875`, avg `0.0286`, median `0.0270`, brier `0.2130`, calibration_gap `-0.0053`
- 20d: hit_rate `1.0000`, avg `0.0514`, median `0.0454`, brier `0.1010`, calibration_gap `-0.3178`
- 60d: hit_rate `0.8750`, avg `0.0947`, median `0.1033`, brier `0.1467`, calibration_gap `-0.1928`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
