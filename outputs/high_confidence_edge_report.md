# High Confidence Edge Report

Generated at: `2026-07-13T21:28:19.861778+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `0`
Forward validation notice: `当前高置信度还没有被前向样本验证，不应当视为稳定预测能力。`
Conclusion: `forward_validation_insufficient_keep_confidence_capped`

## Forward Sample Gates

- 3d: completed `0`, gate `insufficient`
- 5d: completed `0`, gate `insufficient`
- 10d: completed `0`, gate `insufficient`
- 20d: completed `0`, gate `insufficient`
- 60d: completed `0`, gate `insufficient`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, hit `0.4875`, avg `-0.004548`, median `-0.0002`, mae `0.017057`
- 5d: sample `80`, hit `0.4875`, avg `-0.005435`, median `-0.000371`, mae `0.021497`
- 10d: sample `80`, hit `0.4375`, avg `-0.00253`, median `-0.003263`, mae `0.024807`
- 20d: sample `80`, hit `0.7`, avg `0.011535`, median `0.018431`, mae `0.036538`
- 60d: sample `80`, hit `0.6375`, avg `0.02519`, median `0.046407`, mae `0.076743`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.01428`, median `-0.001658`, mae `0.020815`
- 5d: sample `8`, hit `0.375`, avg `-0.021322`, median `-0.016062`, mae `0.025974`
- 10d: sample `8`, hit `0.125`, avg `-0.016048`, median `-0.01796`, mae `0.020857`
- 20d: sample `8`, hit `0.625`, avg `-0.001322`, median `0.029166`, mae `0.04263`
- 60d: sample `8`, hit `0.75`, avg `0.0335`, median `0.059495`, mae `0.083`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.01428`, median `-0.001658`, mae `0.020815`
- 5d: sample `8`, hit `0.375`, avg `-0.021322`, median `-0.016062`, mae `0.025974`
- 10d: sample `8`, hit `0.125`, avg `-0.016048`, median `-0.01796`, mae `0.020857`
- 20d: sample `8`, hit `0.625`, avg `-0.001322`, median `0.029166`, mae `0.04263`
- 60d: sample `8`, hit `0.75`, avg `0.0335`, median `0.059495`, mae `0.083`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.4875, 'avg_return': -0.004548, 'median_return': -0.0002, 'mean_absolute_return': 0.017057, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 80, 'hit_rate': 0.4875, 'avg_return': -0.005435, 'median_return': -0.000371, 'mean_absolute_return': 0.021497, 'max_adverse_excursion': -0.078114, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 80, 'hit_rate': 0.4375, 'avg_return': -0.00253, 'median_return': -0.003263, 'mean_absolute_return': 0.024807, 'max_adverse_excursion': -0.081978, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 80, 'hit_rate': 0.7, 'avg_return': 0.011535, 'median_return': 0.018431, 'mean_absolute_return': 0.036538, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076981}, '60d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.02519, 'median_return': 0.046407, 'mean_absolute_return': 0.076743, 'max_adverse_excursion': -0.15079, 'max_favorable_excursion': 0.19082}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.01428, 'median_return': -0.001658, 'mean_absolute_return': 0.020815, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.020012}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.021322, 'median_return': -0.016062, 'mean_absolute_return': 0.025974, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.016048, 'median_return': -0.01796, 'mean_absolute_return': 0.020857, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.019233}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.001322, 'median_return': 0.029166, 'mean_absolute_return': 0.04263, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.058396}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.0335, 'median_return': 0.059495, 'mean_absolute_return': 0.083, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.121826}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.003467, 'median_return': 0.000496, 'mean_absolute_return': 0.016639, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.00367, 'median_return': 0.001104, 'mean_absolute_return': 0.020999, 'max_adverse_excursion': -0.078114, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.001028, 'median_return': -0.000231, 'mean_absolute_return': 0.025246, 'max_adverse_excursion': -0.081978, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.012963, 'median_return': 0.018431, 'mean_absolute_return': 0.035861, 'max_adverse_excursion': -0.102353, 'max_favorable_excursion': 0.076981}, '60d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.024267, 'median_return': 0.046407, 'mean_absolute_return': 0.076048, 'max_adverse_excursion': -0.15079, 'max_favorable_excursion': 0.19082}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4875}, '5d': {'sample_size': 80, 'hit_rate': 0.4875}, '10d': {'sample_size': 80, 'hit_rate': 0.4375}, '20d': {'sample_size': 80, 'hit_rate': 0.7}, '60d': {'sample_size': 80, 'hit_rate': 0.6375}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 30, 'both_miss': 30}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.025, 'both_hit': 28, 'both_miss': 32}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': -0.05, 'both_hit': 27, 'both_miss': 33}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': 0.075, 'both_hit': 43, 'both_miss': 17}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.025, 'both_hit': 40, 'both_miss': 20}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.4875, 'avg_return': -0.004548, 'median_return': -0.0002, 'mean_absolute_return': 0.017057, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 80, 'hit_rate': 0.4875, 'avg_return': -0.005435, 'median_return': -0.000371, 'mean_absolute_return': 0.021497, 'max_adverse_excursion': -0.078114, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 80, 'hit_rate': 0.4375, 'avg_return': -0.00253, 'median_return': -0.003263, 'mean_absolute_return': 0.024807, 'max_adverse_excursion': -0.081978, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 80, 'hit_rate': 0.7, 'avg_return': 0.011535, 'median_return': 0.018431, 'mean_absolute_return': 0.036538, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076981}, '60d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.02519, 'median_return': 0.046407, 'mean_absolute_return': 0.076743, 'max_adverse_excursion': -0.15079, 'max_favorable_excursion': 0.19082}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4667`, avg `-0.004467`, median `-0.002441`, mae `0.016515`
- 5d: sample `60`, hit `0.5167`, avg `-0.0044`, median `0.001303`, mae `0.02134`
- 10d: sample `60`, hit `0.4667`, avg `-0.000906`, median `-0.000231`, mae `0.0235`
- 20d: sample `60`, hit `0.7`, avg `0.011551`, median `0.018431`, mae `0.03504`
- 60d: sample `60`, hit `0.6667`, avg `0.027689`, median `0.046407`, mae `0.073497`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.002079`, median `0.000603`, mae `0.015032`
- 5d: sample `40`, hit `0.575`, avg `0.000491`, median `0.003727`, mae `0.020953`
- 10d: sample `40`, hit `0.55`, avg `0.002073`, median `0.003262`, mae `0.02561`
- 20d: sample `40`, hit `0.7`, avg `0.010116`, median `0.014918`, mae `0.031734`
- 60d: sample `40`, hit `0.625`, avg `0.019542`, median `0.043741`, mae `0.06868`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4667`, avg `-0.004467`, median `-0.002441`, mae `0.016515`
- 5d: sample `60`, hit `0.5167`, avg `-0.0044`, median `0.001303`, mae `0.02134`
- 10d: sample `60`, hit `0.4667`, avg `-0.000906`, median `-0.000231`, mae `0.0235`
- 20d: sample `60`, hit `0.7`, avg `0.011551`, median `0.018431`, mae `0.03504`
- 60d: sample `60`, hit `0.6667`, avg `0.027689`, median `0.046407`, mae `0.073497`

### breadth_conflicted_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.002079`, median `0.000603`, mae `0.015032`
- 5d: sample `40`, hit `0.575`, avg `0.000491`, median `0.003727`, mae `0.020953`
- 10d: sample `40`, hit `0.55`, avg `0.002073`, median `0.003262`, mae `0.02561`
- 20d: sample `40`, hit `0.7`, avg `0.010116`, median `0.014918`, mae `0.031734`
- 60d: sample `40`, hit `0.625`, avg `0.019542`, median `0.043741`, mae `0.06868`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.002766`, median `-0.001658`, mae `0.018739`
- 5d: sample `40`, hit `0.5`, avg `-0.003633`, median `0.001104`, mae `0.022053`
- 10d: sample `40`, hit `0.5`, avg `0.003327`, median `0.001455`, mae `0.023474`
- 20d: sample `40`, hit `0.725`, avg `0.020371`, median `0.021759`, mae `0.035634`
- 60d: sample `40`, hit `0.725`, avg `0.04944`, median `0.068712`, mae `0.079127`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.003709`, median `0.007619`, mae `0.017997`
- 5d: sample `20`, hit `0.6`, avg `0.006914`, median `0.003727`, mae `0.021992`
- 10d: sample `20`, hit `0.7`, avg `0.013518`, median `0.018751`, mae `0.027668`
- 20d: sample `20`, hit `0.75`, avg `0.026322`, median `0.018431`, mae `0.029616`
- 60d: sample `20`, hit `0.7`, avg `0.054897`, median `0.071518`, mae `0.075122`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.4667`, avg `-0.004467`, median `-0.002441`, mae `0.016515`
- 5d: sample `60`, hit `0.5167`, avg `-0.0044`, median `0.001303`, mae `0.02134`
- 10d: sample `60`, hit `0.4667`, avg `-0.000906`, median `-0.000231`, mae `0.0235`
- 20d: sample `60`, hit `0.7`, avg `0.011551`, median `0.018431`, mae `0.03504`
- 60d: sample `60`, hit `0.6667`, avg `0.027689`, median `0.046407`, mae `0.073497`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.004793`, median `0.000744`, mae `0.018681`
- 5d: sample `20`, hit `0.4`, avg `-0.008541`, median `-0.000413`, mae `0.021967`
- 10d: sample `20`, hit `0.35`, avg `-0.007402`, median `-0.014881`, mae `0.028727`
- 20d: sample `20`, hit `0.7`, avg `0.011486`, median `0.026005`, mae `0.041031`
- 60d: sample `20`, hit `0.55`, avg `0.017693`, median `0.048484`, mae `0.086483`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.002766`, median `-0.001658`, mae `0.018739`
- 5d: sample `40`, hit `0.5`, avg `-0.003633`, median `0.001104`, mae `0.022053`
- 10d: sample `40`, hit `0.5`, avg `0.003327`, median `0.001455`, mae `0.023474`
- 20d: sample `40`, hit `0.725`, avg `0.020371`, median `0.021759`, mae `0.035634`
- 60d: sample `40`, hit `0.725`, avg `0.04944`, median `0.068712`, mae `0.079127`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Internal Resonance Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Internal-resonance attribution is being tracked, but forward-only samples are still below the minimum gate.`

### aligned_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.008555`, median `-0.002789`, mae `0.015774`
- 5d: sample `40`, hit `0.475`, avg `-0.010056`, median `-0.001429`, mae `0.021014`
- 10d: sample `40`, hit `0.35`, avg `-0.008118`, median `-0.005891`, mae `0.021416`
- 20d: sample `40`, hit `0.675`, avg `0.004165`, median `0.019193`, mae `0.037752`
- 60d: sample `40`, hit `0.65`, avg `0.014085`, median `0.043741`, mae `0.072685`

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

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
