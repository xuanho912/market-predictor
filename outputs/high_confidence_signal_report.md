# High Confidence Signal Report

Generated at: `2026-08-23T13:04:31.686424+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0023`, median `0.0014`, brier `0.1950`, calibration_gap `-0.0200`
- 5d: hit_rate `0.7500`, avg `0.0038`, median `0.0039`, brier `0.1850`, calibration_gap `-0.0200`
- 10d: hit_rate `0.5000`, avg `-0.0019`, median `0.0053`, brier `0.3063`, calibration_gap `0.2300`
- 20d: hit_rate `0.2500`, avg `-0.0095`, median `-0.0075`, brier `0.4131`, calibration_gap `0.4800`
- 60d: hit_rate `0.5000`, avg `0.0035`, median `-0.0017`, brier `0.3018`, calibration_gap `0.2300`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0004`, median `0.0018`, brier `0.2183`, calibration_gap `0.0325`
- 5d: hit_rate `0.6875`, avg `0.0011`, median `0.0042`, brier `0.2130`, calibration_gap `0.0325`
- 10d: hit_rate `0.4375`, avg `-0.0026`, median `-0.0098`, brier `0.3258`, calibration_gap `0.2825`
- 20d: hit_rate `0.3125`, avg `-0.0131`, median `-0.0114`, brier `0.3798`, calibration_gap `0.4075`
- 60d: hit_rate `0.3750`, avg `-0.0117`, median `-0.0282`, brier `0.3502`, calibration_gap `0.3450`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6667`, avg `0.0045`, median `0.0066`, brier `0.2241`, calibration_gap `0.0048`
- 5d: hit_rate `0.5500`, avg `0.0038`, median `0.0023`, brier `0.2629`, calibration_gap `0.1215`
- 10d: hit_rate `0.6000`, avg `0.0084`, median `0.0109`, brier `0.2471`, calibration_gap `0.0715`
- 20d: hit_rate `0.6833`, avg `0.0133`, median `0.0153`, brier `0.2189`, calibration_gap `-0.0118`
- 60d: hit_rate `0.6333`, avg `0.0245`, median `0.0302`, brier `0.2381`, calibration_gap `0.0382`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0103`, median `0.0102`, brier `0.1979`, calibration_gap `-0.0979`
- 5d: hit_rate `0.5625`, avg `0.0070`, median `0.0063`, brier `0.2552`, calibration_gap `0.0896`
- 10d: hit_rate `0.8125`, avg `0.0178`, median `0.0195`, brier `0.1787`, calibration_gap `-0.1604`
- 20d: hit_rate `0.8125`, avg `0.0255`, median `0.0267`, brier `0.1783`, calibration_gap `-0.1604`
- 60d: hit_rate `0.6875`, avg `0.0357`, median `0.0347`, brier `0.2156`, calibration_gap `-0.0354`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
