# High Confidence Signal Report

Generated at: `2026-11-09T22:24:38.093165+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `1.0000`, avg `0.0193`, median `0.0210`, brier `0.0495`, calibration_gap `-0.2225`
- 5d: hit_rate `0.8750`, avg `0.0210`, median `0.0257`, brier `0.1184`, calibration_gap `-0.0975`
- 10d: hit_rate `0.7500`, avg `0.0287`, median `0.0526`, brier `0.1860`, calibration_gap `0.0275`
- 20d: hit_rate `0.8750`, avg `0.0420`, median `0.0675`, brier `0.1192`, calibration_gap `-0.0975`
- 60d: hit_rate `0.8750`, avg `0.0571`, median `0.0669`, brier `0.1184`, calibration_gap `-0.0975`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0090`, median `0.0143`, brier `0.1844`, calibration_gap `0.0189`
- 5d: hit_rate `0.6250`, avg `0.0093`, median `0.0099`, brier `0.2517`, calibration_gap `0.1439`
- 10d: hit_rate `0.7500`, avg `0.0220`, median `0.0276`, brier `0.1871`, calibration_gap `0.0189`
- 20d: hit_rate `0.7500`, avg `0.0285`, median `0.0300`, brier `0.1865`, calibration_gap `0.0189`
- 60d: hit_rate `0.8750`, avg `0.0525`, median `0.0616`, brier `0.1208`, calibration_gap `-0.1061`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.6500`, avg `0.0030`, median `0.0093`, brier `0.2233`, calibration_gap `-0.0104`
- 5d: hit_rate `0.7500`, avg `0.0134`, median `0.0118`, brier `0.1967`, calibration_gap `-0.1104`
- 10d: hit_rate `0.8500`, avg `0.0253`, median `0.0210`, brier `0.1713`, calibration_gap `-0.2104`
- 20d: hit_rate `0.7000`, avg `0.0232`, median `0.0373`, brier `0.2102`, calibration_gap `-0.0604`
- 60d: hit_rate `0.7500`, avg `0.0463`, median `0.0546`, brier `0.1968`, calibration_gap `-0.1104`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0006`, median `0.0081`, brier `0.2517`, calibration_gap `0.0698`
- 5d: hit_rate `0.6875`, avg `0.0075`, median `0.0101`, brier `0.2184`, calibration_gap `-0.0552`
- 10d: hit_rate `0.8125`, avg `0.0171`, median `0.0172`, brier `0.1868`, calibration_gap `-0.1802`
- 20d: hit_rate `0.6250`, avg `0.0151`, median `0.0239`, brier `0.2353`, calibration_gap `0.0073`
- 60d: hit_rate `0.6875`, avg `0.0427`, median `0.0482`, brier `0.2186`, calibration_gap `-0.0552`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
