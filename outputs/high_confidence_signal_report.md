# High Confidence Signal Report

Generated at: `2026-08-12T13:50:02.995789+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `60`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `6`
- 3d: hit_rate `0.8333`, avg `0.0065`, median `0.0117`, brier `0.1506`, calibration_gap `-0.1229`
- 5d: hit_rate `0.6667`, avg `-0.0012`, median `0.0024`, brier `0.2190`, calibration_gap `0.0437`
- 10d: hit_rate `0.6667`, avg `0.0099`, median `0.0166`, brier `0.2207`, calibration_gap `0.0437`
- 20d: hit_rate `0.3333`, avg `0.0055`, median `-0.0053`, brier `0.3622`, calibration_gap `0.3771`
- 60d: hit_rate `0.3333`, avg `-0.0096`, median `-0.0413`, brier `0.3622`, calibration_gap `0.3771`

### top_20_confidence_signals
- sample_size: `12`
- 3d: hit_rate `0.6667`, avg `0.0019`, median `0.0074`, brier `0.2175`, calibration_gap `0.0360`
- 5d: hit_rate `0.6667`, avg `-0.0026`, median `0.0028`, brier `0.2200`, calibration_gap `0.0360`
- 10d: hit_rate `0.6667`, avg `0.0057`, median `0.0113`, brier `0.2208`, calibration_gap `0.0360`
- 20d: hit_rate `0.6667`, avg `0.0131`, median `0.0130`, brier `0.2277`, calibration_gap `0.0360`
- 60d: hit_rate `0.5000`, avg `0.0099`, median `-0.0053`, brier `0.2921`, calibration_gap `0.2027`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6667`, avg `0.0054`, median `0.0093`, brier `0.2217`, calibration_gap `0.0110`
- 5d: hit_rate `0.6333`, avg `0.0055`, median `0.0053`, brier `0.2335`, calibration_gap `0.0443`
- 10d: hit_rate `0.6000`, avg `0.0074`, median `0.0099`, brier `0.2446`, calibration_gap `0.0777`
- 20d: hit_rate `0.6833`, avg `0.0129`, median `0.0162`, brier `0.2170`, calibration_gap `-0.0057`
- 60d: hit_rate `0.6500`, avg `0.0304`, median `0.0464`, brier `0.2305`, calibration_gap `0.0277`

### low_confidence_reference
- sample_size: `12`
- 3d: hit_rate `0.7500`, avg `0.0049`, median `0.0047`, brier `0.1955`, calibration_gap `-0.0888`
- 5d: hit_rate `0.7500`, avg `0.0023`, median `0.0057`, brier `0.1949`, calibration_gap `-0.0888`
- 10d: hit_rate `0.6667`, avg `-0.0014`, median `0.0086`, brier `0.2217`, calibration_gap `-0.0055`
- 20d: hit_rate `0.5833`, avg `0.0007`, median `0.0195`, brier `0.2496`, calibration_gap `0.0778`
- 60d: hit_rate `0.8333`, avg `0.0546`, median `0.0498`, brier `0.1691`, calibration_gap `-0.1722`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
