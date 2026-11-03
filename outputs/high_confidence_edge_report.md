# High Confidence Edge Report

Generated at: `2026-11-03T19:31:43.058023+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `160`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `160`, gate `stronger_evidence`
- 5d: completed `160`, gate `stronger_evidence`
- 10d: completed `160`, gate `stronger_evidence`
- 20d: completed `160`, gate `stronger_evidence`
- 60d: completed `160`, gate `stronger_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `0.001879`, median `0.004243`, mae `0.018791`
- 5d: sample `80`, hit `0.55`, avg `0.007712`, median `0.006571`, mae `0.021209`
- 10d: sample `80`, hit `0.675`, avg `0.016218`, median `0.020244`, mae `0.031154`
- 20d: sample `80`, hit `0.725`, avg `0.029021`, median `0.031658`, mae `0.04468`
- 60d: sample `80`, hit `0.8125`, avg `0.049481`, median `0.062764`, mae `0.061825`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.00054`, median `-0.003228`, mae `0.013597`
- 5d: sample `8`, hit `0.375`, avg `0.000936`, median `-0.00891`, mae `0.017508`
- 10d: sample `8`, hit `0.375`, avg `-0.002318`, median `-0.002305`, mae `0.02932`
- 20d: sample `8`, hit `0.625`, avg `0.018122`, median `0.020066`, mae `0.032193`
- 60d: sample `8`, hit `0.75`, avg `0.027743`, median `0.041644`, mae `0.045939`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.010974`, median `0.024354`, mae `0.018366`
- 5d: sample `8`, hit `0.625`, avg `0.012405`, median `0.013109`, mae `0.019613`
- 10d: sample `8`, hit `0.5`, avg `0.01888`, median `0.023979`, mae `0.028403`
- 20d: sample `8`, hit `0.875`, avg `0.039147`, median `0.031658`, mae `0.041528`
- 60d: sample `8`, hit `1.0`, avg `0.074623`, median `0.074055`, mae `0.074623`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.010974, 'median_return': 0.024354, 'mean_absolute_return': 0.018366, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.012405, 'median_return': 0.013109, 'mean_absolute_return': 0.019613, 'max_adverse_excursion': -0.016952, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.01888, 'median_return': 0.023979, 'mean_absolute_return': 0.028403, 'max_adverse_excursion': -0.021975, 'max_favorable_excursion': 0.060007}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.039147, 'median_return': 0.031658, 'mean_absolute_return': 0.041528, 'max_adverse_excursion': -0.009524, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.074623, 'median_return': 0.074055, 'mean_absolute_return': 0.074623, 'max_adverse_excursion': 0.025315, 'max_favorable_excursion': 0.105209}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.000869, 'median_return': 0.001471, 'mean_absolute_return': 0.018838, 'max_adverse_excursion': -0.083956, 'max_favorable_excursion': 0.049499}, '5d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.007191, 'median_return': 0.004752, 'mean_absolute_return': 0.021387, 'max_adverse_excursion': -0.048929, 'max_favorable_excursion': 0.076593}, '10d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.015923, 'median_return': 0.020244, 'mean_absolute_return': 0.031459, 'max_adverse_excursion': -0.071498, 'max_favorable_excursion': 0.090323}, '20d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.027896, 'median_return': 0.032319, 'mean_absolute_return': 0.04503, 'max_adverse_excursion': -0.068819, 'max_favorable_excursion': 0.112509}, '60d': {'sample_size': 72, 'hit_rate': 0.7917, 'avg_return': 0.046687, 'median_return': 0.060303, 'mean_absolute_return': 0.060403, 'max_adverse_excursion': -0.111282, 'max_favorable_excursion': 0.140054}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.45}, '10d': {'sample_size': 80, 'hit_rate': 0.425}, '20d': {'sample_size': 80, 'hit_rate': 0.55}, '60d': {'sample_size': 80, 'hit_rate': 0.5625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.1375, 'both_hit': 0, 'both_miss': 1}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.125, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.004093, 'median_return': 0.006321, 'mean_absolute_return': 0.016825, 'max_adverse_excursion': -0.049442, 'max_favorable_excursion': 0.049499}, '5d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.008069, 'median_return': 0.011002, 'mean_absolute_return': 0.02004, 'max_adverse_excursion': -0.04049, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.014629, 'median_return': 0.015002, 'mean_absolute_return': 0.029123, 'max_adverse_excursion': -0.071498, 'max_favorable_excursion': 0.076904}, '20d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.024344, 'median_return': 0.029234, 'mean_absolute_return': 0.041809, 'max_adverse_excursion': -0.068819, 'max_favorable_excursion': 0.102899}, '60d': {'sample_size': 60, 'hit_rate': 0.8, 'avg_return': 0.047535, 'median_return': 0.057501, 'mean_absolute_return': 0.058961, 'max_adverse_excursion': -0.090957, 'max_favorable_excursion': 0.10846}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.004762, 'median_return': -0.006406, 'mean_absolute_return': 0.024687, 'max_adverse_excursion': -0.083956, 'max_favorable_excursion': 0.044028}, '5d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.006643, 'median_return': 0.001023, 'mean_absolute_return': 0.024717, 'max_adverse_excursion': -0.048929, 'max_favorable_excursion': 0.076593}, '10d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.020986, 'median_return': 0.032111, 'mean_absolute_return': 0.037246, 'max_adverse_excursion': -0.053431, 'max_favorable_excursion': 0.090323}, '20d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.043052, 'median_return': 0.053953, 'mean_absolute_return': 0.053292, 'max_adverse_excursion': -0.056594, 'max_favorable_excursion': 0.112509}, '60d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.055319, 'median_return': 0.069634, 'mean_absolute_return': 0.070416, 'max_adverse_excursion': -0.111282, 'max_favorable_excursion': 0.140054}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.004093`, median `0.006321`, mae `0.016825`
- 5d: sample `60`, hit `0.5667`, avg `0.008069`, median `0.011002`, mae `0.02004`
- 10d: sample `60`, hit `0.6667`, avg `0.014629`, median `0.015002`, mae `0.029123`
- 20d: sample `60`, hit `0.7`, avg `0.024344`, median `0.029234`, mae `0.041809`
- 60d: sample `60`, hit `0.8`, avg `0.047535`, median `0.057501`, mae `0.058961`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.004762`, median `-0.006406`, mae `0.024687`
- 5d: sample `20`, hit `0.5`, avg `0.006643`, median `0.001023`, mae `0.024717`
- 10d: sample `20`, hit `0.7`, avg `0.020986`, median `0.032111`, mae `0.037246`
- 20d: sample `20`, hit `0.8`, avg `0.043052`, median `0.053953`, mae `0.053292`
- 60d: sample `20`, hit `0.85`, avg `0.055319`, median `0.069634`, mae `0.070416`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.004619`, median `0.006321`, mae `0.017425`
- 5d: sample `40`, hit `0.5`, avg `0.005992`, median `0.006571`, mae `0.018085`
- 10d: sample `40`, hit `0.6`, avg `0.013482`, median `0.014845`, mae `0.027808`
- 20d: sample `40`, hit `0.775`, avg `0.028677`, median `0.029234`, mae `0.039179`
- 60d: sample `40`, hit `0.875`, avg `0.058036`, median `0.072365`, mae `0.066358`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.004619`, median `0.006321`, mae `0.017425`
- 5d: sample `40`, hit `0.5`, avg `0.005992`, median `0.006571`, mae `0.018085`
- 10d: sample `40`, hit `0.6`, avg `0.013482`, median `0.014845`, mae `0.027808`
- 20d: sample `40`, hit `0.775`, avg `0.028677`, median `0.029234`, mae `0.039179`
- 60d: sample `40`, hit `0.875`, avg `0.058036`, median `0.072365`, mae `0.066358`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.004619`, median `0.006321`, mae `0.017425`
- 5d: sample `40`, hit `0.5`, avg `0.005992`, median `0.006571`, mae `0.018085`
- 10d: sample `40`, hit `0.6`, avg `0.013482`, median `0.014845`, mae `0.027808`
- 20d: sample `40`, hit `0.775`, avg `0.028677`, median `0.029234`, mae `0.039179`
- 60d: sample `40`, hit `0.875`, avg `0.058036`, median `0.072365`, mae `0.066358`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.004619`, median `0.006321`, mae `0.017425`
- 5d: sample `40`, hit `0.5`, avg `0.005992`, median `0.006571`, mae `0.018085`
- 10d: sample `40`, hit `0.6`, avg `0.013482`, median `0.014845`, mae `0.027808`
- 20d: sample `40`, hit `0.775`, avg `0.028677`, median `0.029234`, mae `0.039179`
- 60d: sample `40`, hit `0.875`, avg `0.058036`, median `0.072365`, mae `0.066358`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.004762`, median `-0.006406`, mae `0.024687`
- 5d: sample `20`, hit `0.5`, avg `0.006643`, median `0.001023`, mae `0.024717`
- 10d: sample `20`, hit `0.7`, avg `0.020986`, median `0.032111`, mae `0.037246`
- 20d: sample `20`, hit `0.8`, avg `0.043052`, median `0.053953`, mae `0.053292`
- 60d: sample `20`, hit `0.85`, avg `0.055319`, median `0.069634`, mae `0.070416`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.004619`, median `0.006321`, mae `0.017425`
- 5d: sample `40`, hit `0.5`, avg `0.005992`, median `0.006571`, mae `0.018085`
- 10d: sample `40`, hit `0.6`, avg `0.013482`, median `0.014845`, mae `0.027808`
- 20d: sample `40`, hit `0.775`, avg `0.028677`, median `0.029234`, mae `0.039179`
- 60d: sample `40`, hit `0.875`, avg `0.058036`, median `0.072365`, mae `0.066358`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.003041`, median `0.007915`, mae `0.015627`
- 5d: sample `20`, hit `0.7`, avg `0.012222`, median `0.020876`, mae `0.023952`
- 10d: sample `20`, hit `0.8`, avg `0.016924`, median `0.019449`, mae `0.031752`
- 20d: sample `20`, hit `0.55`, avg `0.015678`, median `0.032319`, mae `0.047068`
- 60d: sample `20`, hit `0.65`, avg `0.026532`, median `0.030649`, mae `0.044168`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.004619`, median `0.006321`, mae `0.017425`
- 5d: sample `40`, hit `0.5`, avg `0.005992`, median `0.006571`, mae `0.018085`
- 10d: sample `40`, hit `0.6`, avg `0.013482`, median `0.014845`, mae `0.027808`
- 20d: sample `40`, hit `0.775`, avg `0.028677`, median `0.029234`, mae `0.039179`
- 60d: sample `40`, hit `0.875`, avg `0.058036`, median `0.072365`, mae `0.066358`

### bounce_surface_only
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `0.001879`, median `0.004243`, mae `0.018791`
- 5d: sample `80`, hit `0.55`, avg `0.007712`, median `0.006571`, mae `0.021209`
- 10d: sample `80`, hit `0.675`, avg `0.016218`, median `0.020244`, mae `0.031154`
- 20d: sample `80`, hit `0.725`, avg `0.029021`, median `0.031658`, mae `0.04468`
- 60d: sample `80`, hit `0.8125`, avg `0.049481`, median `0.062764`, mae `0.061825`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `0.001879`, median `0.004243`, mae `0.018791`
- 5d: sample `80`, hit `0.55`, avg `0.007712`, median `0.006571`, mae `0.021209`
- 10d: sample `80`, hit `0.675`, avg `0.016218`, median `0.020244`, mae `0.031154`
- 20d: sample `80`, hit `0.725`, avg `0.029021`, median `0.031658`, mae `0.04468`
- 60d: sample `80`, hit `0.8125`, avg `0.049481`, median `0.062764`, mae `0.061825`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.004619`, median `0.006321`, mae `0.017425`
- 5d: sample `40`, hit `0.5`, avg `0.005992`, median `0.006571`, mae `0.018085`
- 10d: sample `40`, hit `0.6`, avg `0.013482`, median `0.014845`, mae `0.027808`
- 20d: sample `40`, hit `0.775`, avg `0.028677`, median `0.029234`, mae `0.039179`
- 60d: sample `40`, hit `0.875`, avg `0.058036`, median `0.072365`, mae `0.066358`

### bounce_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.004619`, median `0.006321`, mae `0.017425`
- 5d: sample `40`, hit `0.5`, avg `0.005992`, median `0.006571`, mae `0.018085`
- 10d: sample `40`, hit `0.6`, avg `0.013482`, median `0.014845`, mae `0.027808`
- 20d: sample `40`, hit `0.775`, avg `0.028677`, median `0.029234`, mae `0.039179`
- 60d: sample `40`, hit `0.875`, avg `0.058036`, median `0.072365`, mae `0.066358`

### risk_path_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.000861`, median `0.001471`, mae `0.020157`
- 5d: sample `40`, hit `0.6`, avg `0.009433`, median `0.009101`, mae `0.024334`
- 10d: sample `40`, hit `0.75`, avg `0.018955`, median `0.022464`, mae `0.034499`
- 20d: sample `40`, hit `0.675`, avg `0.029365`, median `0.042224`, mae `0.05018`
- 60d: sample `40`, hit `0.75`, avg `0.040925`, median `0.056005`, mae `0.057292`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
