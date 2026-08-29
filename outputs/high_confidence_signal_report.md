# High Confidence Signal Report

Generated at: `2026-08-29T07:56:29.708180+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `-0.0010`, median `0.0144`, brier `0.1931`, calibration_gap `-0.0682`
- 5d: hit_rate `0.6250`, avg `-0.0034`, median `0.0130`, brier `0.2353`, calibration_gap `0.0568`
- 10d: hit_rate `0.6250`, avg `0.0035`, median `0.0169`, brier `0.2353`, calibration_gap `0.0568`
- 20d: hit_rate `0.7500`, avg `0.0204`, median `0.0296`, brier `0.1931`, calibration_gap `-0.0682`
- 60d: hit_rate `0.6250`, avg `0.0189`, median `0.0540`, brier `0.2353`, calibration_gap `0.0568`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.8125`, avg `0.0042`, median `0.0117`, brier `0.1765`, calibration_gap `-0.1436`
- 5d: hit_rate `0.7500`, avg `0.0080`, median `0.0179`, brier `0.1956`, calibration_gap `-0.0811`
- 10d: hit_rate `0.8125`, avg `0.0190`, median `0.0232`, brier `0.1768`, calibration_gap `-0.1436`
- 20d: hit_rate `0.8750`, avg `0.0293`, median `0.0323`, brier `0.1558`, calibration_gap `-0.2061`
- 60d: hit_rate `0.8125`, avg `0.0588`, median `0.0764`, brier `0.1768`, calibration_gap `-0.1436`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.7625`, avg `0.0096`, median `0.0125`, brier `0.2044`, calibration_gap `-0.1453`
- 5d: hit_rate `0.7500`, avg `0.0141`, median `0.0174`, brier `0.2069`, calibration_gap `-0.1328`
- 10d: hit_rate `0.7000`, avg `0.0185`, median `0.0223`, brier `0.2169`, calibration_gap `-0.0828`
- 20d: hit_rate `0.8000`, avg `0.0331`, median `0.0322`, brier `0.1942`, calibration_gap `-0.1828`
- 60d: hit_rate `0.7875`, avg `0.0631`, median `0.0818`, brier `0.1984`, calibration_gap `-0.1703`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.8125`, avg `0.0129`, median `0.0127`, brier `0.2093`, calibration_gap `-0.2363`
- 5d: hit_rate `0.8750`, avg `0.0179`, median `0.0162`, brier `0.1980`, calibration_gap `-0.2988`
- 10d: hit_rate `0.8750`, avg `0.0256`, median `0.0211`, brier `0.1986`, calibration_gap `-0.2988`
- 20d: hit_rate `0.9375`, avg `0.0337`, median `0.0275`, brier `0.1876`, calibration_gap `-0.3613`
- 60d: hit_rate `0.9375`, avg `0.0665`, median `0.0728`, brier `0.1904`, calibration_gap `-0.3613`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
