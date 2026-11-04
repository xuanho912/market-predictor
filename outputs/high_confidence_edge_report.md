# High Confidence Edge Report

Generated at: `2026-11-04T07:32:37.638452+00:00`

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
- 3d: sample `80`, hit `0.5125`, avg `0.000532`, median `0.001471`, mae `0.019911`
- 5d: sample `80`, hit `0.525`, avg `0.00422`, median `0.004149`, mae `0.023645`
- 10d: sample `80`, hit `0.6625`, avg `0.014454`, median `0.019449`, mae `0.032275`
- 20d: sample `80`, hit `0.725`, avg `0.02856`, median `0.031196`, mae `0.044657`
- 60d: sample `80`, hit `0.8125`, avg `0.048645`, median `0.062764`, mae `0.06332`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.010974, 'median_return': 0.024354, 'mean_absolute_return': 0.018366, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.012405, 'median_return': 0.013109, 'mean_absolute_return': 0.019613, 'max_adverse_excursion': -0.016952, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.01888, 'median_return': 0.023979, 'mean_absolute_return': 0.028403, 'max_adverse_excursion': -0.021975, 'max_favorable_excursion': 0.060007}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.039147, 'median_return': 0.031658, 'mean_absolute_return': 0.041528, 'max_adverse_excursion': -0.009524, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.074623, 'median_return': 0.074055, 'mean_absolute_return': 0.074623, 'max_adverse_excursion': 0.025315, 'max_favorable_excursion': 0.105209}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.000629, 'median_return': 0.000543, 'mean_absolute_return': 0.020083, 'max_adverse_excursion': -0.083956, 'max_favorable_excursion': 0.049499}, '5d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.00331, 'median_return': 0.003248, 'mean_absolute_return': 0.024093, 'max_adverse_excursion': -0.177985, 'max_favorable_excursion': 0.076593}, '10d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.013962, 'median_return': 0.019449, 'mean_absolute_return': 0.032705, 'max_adverse_excursion': -0.094168, 'max_favorable_excursion': 0.090323}, '20d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.027384, 'median_return': 0.031196, 'mean_absolute_return': 0.045005, 'max_adverse_excursion': -0.086342, 'max_favorable_excursion': 0.112509}, '60d': {'sample_size': 72, 'hit_rate': 0.7917, 'avg_return': 0.045758, 'median_return': 0.060303, 'mean_absolute_return': 0.062064, 'max_adverse_excursion': -0.111282, 'max_favorable_excursion': 0.140054}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4875}, '5d': {'sample_size': 80, 'hit_rate': 0.475}, '10d': {'sample_size': 80, 'hit_rate': 0.325}, '20d': {'sample_size': 80, 'hit_rate': 0.275}, '60d': {'sample_size': 80, 'hit_rate': 0.1875}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.3375, 'both_hit': 0, 'both_miss': 1}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_minus_secondary': -0.45, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.1875, 'secondary_hit_rate': 0.8125, 'primary_minus_secondary': -0.625, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.004619, 'median_return': 0.006321, 'mean_absolute_return': 0.017425, 'max_adverse_excursion': -0.03272, 'max_favorable_excursion': 0.049499}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.005992, 'median_return': 0.006571, 'mean_absolute_return': 0.018085, 'max_adverse_excursion': -0.025448, 'max_favorable_excursion': 0.044138}, '10d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.013482, 'median_return': 0.014845, 'mean_absolute_return': 0.027808, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.076904}, '20d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.028677, 'median_return': 0.029234, 'mean_absolute_return': 0.039179, 'max_adverse_excursion': -0.045992, 'max_favorable_excursion': 0.085922}, '60d': {'sample_size': 40, 'hit_rate': 0.875, 'avg_return': 0.058036, 'median_return': 0.072365, 'mean_absolute_return': 0.066358, 'max_adverse_excursion': -0.076188, 'max_favorable_excursion': 0.10846}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.003556, 'median_return': 0.000543, 'mean_absolute_return': 0.022398, 'max_adverse_excursion': -0.083956, 'max_favorable_excursion': 0.044028}, '5d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.002447, 'median_return': 0.004149, 'mean_absolute_return': 0.029205, 'max_adverse_excursion': -0.177985, 'max_favorable_excursion': 0.076593}, '10d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.015426, 'median_return': 0.02025, 'mean_absolute_return': 0.036741, 'max_adverse_excursion': -0.094168, 'max_favorable_excursion': 0.090323}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.028444, 'median_return': 0.041918, 'mean_absolute_return': 0.050135, 'max_adverse_excursion': -0.086342, 'max_favorable_excursion': 0.112509}, '60d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.039254, 'median_return': 0.056005, 'mean_absolute_return': 0.060282, 'max_adverse_excursion': -0.111282, 'max_favorable_excursion': 0.140054}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.002296`, median `0.005726`, mae `0.018319`
- 5d: sample `60`, hit `0.5333`, avg `0.003412`, median `0.007479`, mae `0.023287`
- 10d: sample `60`, hit `0.65`, avg `0.012276`, median `0.014845`, mae `0.030617`
- 20d: sample `60`, hit `0.7`, avg `0.02373`, median `0.028626`, mae `0.041779`
- 60d: sample `60`, hit `0.8`, avg `0.04642`, median `0.057501`, mae `0.060954`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.004762`, median `-0.006406`, mae `0.024687`
- 5d: sample `20`, hit `0.5`, avg `0.006643`, median `0.001023`, mae `0.024717`
- 10d: sample `20`, hit `0.7`, avg `0.020986`, median `0.032111`, mae `0.037246`
- 20d: sample `20`, hit `0.8`, avg `0.043052`, median `0.053953`, mae `0.053292`
- 60d: sample `20`, hit `0.85`, avg `0.055319`, median `0.069634`, mae `0.070416`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.00962`, median `0.014973`, mae `0.020989`
- 5d: sample `20`, hit `0.5`, avg `0.009133`, median `0.011002`, mae `0.018485`
- 10d: sample `20`, hit `0.65`, avg `0.019636`, median `0.023979`, mae `0.030384`
- 20d: sample `20`, hit `0.85`, avg `0.033682`, median `0.031196`, mae `0.040467`
- 60d: sample `20`, hit `0.95`, avg `0.073821`, median `0.074055`, mae `0.074836`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.00962`, median `0.014973`, mae `0.020989`
- 5d: sample `20`, hit `0.5`, avg `0.009133`, median `0.011002`, mae `0.018485`
- 10d: sample `20`, hit `0.65`, avg `0.019636`, median `0.023979`, mae `0.030384`
- 20d: sample `20`, hit `0.85`, avg `0.033682`, median `0.031196`, mae `0.040467`
- 60d: sample `20`, hit `0.95`, avg `0.073821`, median `0.074055`, mae `0.074836`

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
- 3d: sample `20`, hit `0.55`, avg `-0.002351`, median `0.005726`, mae `0.020108`
- 5d: sample `20`, hit `0.6`, avg `-0.001748`, median `0.012136`, mae `0.033693`
- 10d: sample `20`, hit `0.75`, avg `0.009865`, median `0.015002`, mae `0.036235`
- 20d: sample `20`, hit `0.55`, avg `0.013835`, median `0.024146`, mae `0.046977`
- 60d: sample `20`, hit `0.65`, avg `0.023189`, median `0.030649`, mae `0.050148`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- 3d: sample `80`, hit `0.5125`, avg `0.000532`, median `0.001471`, mae `0.019911`
- 5d: sample `80`, hit `0.525`, avg `0.00422`, median `0.004149`, mae `0.023645`
- 10d: sample `80`, hit `0.6625`, avg `0.014454`, median `0.019449`, mae `0.032275`
- 20d: sample `80`, hit `0.725`, avg `0.02856`, median `0.031196`, mae `0.044657`
- 60d: sample `80`, hit `0.8125`, avg `0.048645`, median `0.062764`, mae `0.06332`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5125`, avg `0.000532`, median `0.001471`, mae `0.019911`
- 5d: sample `80`, hit `0.525`, avg `0.00422`, median `0.004149`, mae `0.023645`
- 10d: sample `80`, hit `0.6625`, avg `0.014454`, median `0.019449`, mae `0.032275`
- 20d: sample `80`, hit `0.725`, avg `0.02856`, median `0.031196`, mae `0.044657`
- 60d: sample `80`, hit `0.8125`, avg `0.048645`, median `0.062764`, mae `0.06332`

### bounce_with_flow_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_conflict
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### risk_path_with_flow_conflict
- sample_size: `80`
- 3d: sample `80`, hit `0.5125`, avg `0.000532`, median `0.001471`, mae `0.019911`
- 5d: sample `80`, hit `0.525`, avg `0.00422`, median `0.004149`, mae `0.023645`
- 10d: sample `80`, hit `0.6625`, avg `0.014454`, median `0.019449`, mae `0.032275`
- 20d: sample `80`, hit `0.725`, avg `0.02856`, median `0.031196`, mae `0.044657`
- 60d: sample `80`, hit `0.8125`, avg `0.048645`, median `0.062764`, mae `0.06332`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
