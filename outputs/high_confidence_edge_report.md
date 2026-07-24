# High Confidence Edge Report

Generated at: `2026-07-24T14:15:30.651365+00:00`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.005848`, median `0.000766`, mae `0.016227`
- 5d: sample `40`, hit `0.475`, avg `-0.008988`, median `-0.001429`, mae `0.01864`
- 10d: sample `40`, hit `0.4`, avg `-0.003441`, median `-0.006017`, mae `0.016616`
- 20d: sample `40`, hit `0.625`, avg `0.012338`, median `0.020226`, mae `0.035155`
- 60d: sample `40`, hit `0.7`, avg `0.035262`, median `0.050438`, mae `0.061495`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.001552`, median `0.000707`, mae `0.02159`
- 5d: sample `40`, hit `0.45`, avg `-0.002107`, median `-0.001129`, mae `0.026984`
- 10d: sample `40`, hit `0.725`, avg `0.013167`, median `0.027869`, mae `0.039012`
- 20d: sample `40`, hit `0.675`, avg `0.018702`, median `0.045022`, mae `0.058822`
- 60d: sample `40`, hit `0.6`, avg `0.009107`, median `0.068712`, mae `0.108101`

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
- 3d: sample `8`, hit `0.375`, avg `-0.006489`, median `-0.001658`, mae `0.022829`
- 5d: sample `8`, hit `0.5`, avg `-0.014113`, median `0.005072`, mae `0.02707`
- 10d: sample `8`, hit `0.25`, avg `-0.003292`, median `-0.006017`, mae `0.014534`
- 20d: sample `8`, hit `0.5`, avg `0.016195`, median `0.016745`, mae `0.038977`
- 60d: sample `8`, hit `0.625`, avg `0.04523`, median `0.050438`, mae `0.074392`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.006489`, median `-0.001658`, mae `0.022829`
- 5d: sample `8`, hit `0.5`, avg `-0.014113`, median `0.005072`, mae `0.02707`
- 10d: sample `8`, hit `0.25`, avg `-0.003292`, median `-0.006017`, mae `0.014534`
- 20d: sample `8`, hit `0.5`, avg `0.016195`, median `0.016745`, mae `0.038977`
- 60d: sample `8`, hit `0.625`, avg `0.04523`, median `0.050438`, mae `0.074392`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': -0.005848, 'median_return': 0.000766, 'mean_absolute_return': 0.016227, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.008988, 'median_return': -0.001429, 'mean_absolute_return': 0.01864, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.003441, 'median_return': -0.006017, 'mean_absolute_return': 0.016616, 'max_adverse_excursion': -0.040826, 'max_favorable_excursion': 0.035901}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.012338, 'median_return': 0.020226, 'mean_absolute_return': 0.035155, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.035262, 'median_return': 0.050438, 'mean_absolute_return': 0.061495, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.006489, 'median_return': -0.001658, 'mean_absolute_return': 0.022829, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.014113, 'median_return': 0.005072, 'mean_absolute_return': 0.02707, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.003292, 'median_return': -0.006017, 'mean_absolute_return': 0.014534, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.016195, 'median_return': 0.016745, 'mean_absolute_return': 0.038977, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.04523, 'median_return': 0.050438, 'mean_absolute_return': 0.074392, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': -0.00339, 'median_return': 0.000766, 'mean_absolute_return': 0.018473, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': -0.004596, 'median_return': -0.001429, 'mean_absolute_return': 0.022339, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.005769, 'median_return': 0.014312, 'mean_absolute_return': 0.02929, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.015445, 'median_return': 0.026005, 'mean_absolute_return': 0.047878, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.019624, 'median_return': 0.057625, 'mean_absolute_return': 0.085954, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.19082}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.5125}, '10d': {'sample_size': 80, 'hit_rate': 0.3375}, '20d': {'sample_size': 80, 'hit_rate': 0.475}, '60d': {'sample_size': 80, 'hit_rate': 0.55}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.325, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': -0.002612, 'median_return': 0.001405, 'mean_absolute_return': 0.018481, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': -0.002532, 'median_return': 0.001303, 'mean_absolute_return': 0.020478, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.051324}, '10d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.006528, 'median_return': 0.003815, 'mean_absolute_return': 0.024146, 'max_adverse_excursion': -0.068474, 'max_favorable_excursion': 0.061544}, '20d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.021575, 'median_return': 0.026113, 'mean_absolute_return': 0.042516, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.110689}, '60d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.038403, 'median_return': 0.058473, 'mean_absolute_return': 0.075373, 'max_adverse_excursion': -0.177732, 'max_favorable_excursion': 0.19082}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.006965, 'median_return': -0.005555, 'mean_absolute_return': 0.020191, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 20, 'hit_rate': 0.25, 'avg_return': -0.014592, 'median_return': -0.009549, 'mean_absolute_return': 0.029813, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.000135, 'median_return': 0.016791, 'mean_absolute_return': 0.038818, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.002644, 'median_return': 0.021735, 'mean_absolute_return': 0.060404, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.02647, 'median_return': -0.00384, 'mean_absolute_return': 0.113072, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.129489}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.005848`, median `0.000766`, mae `0.016227`
- 5d: sample `40`, hit `0.475`, avg `-0.008988`, median `-0.001429`, mae `0.01864`
- 10d: sample `40`, hit `0.4`, avg `-0.003441`, median `-0.006017`, mae `0.016616`
- 20d: sample `40`, hit `0.625`, avg `0.012338`, median `0.020226`, mae `0.035155`
- 60d: sample `40`, hit `0.7`, avg `0.035262`, median `0.050438`, mae `0.061495`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.001552`, median `0.000707`, mae `0.02159`
- 5d: sample `40`, hit `0.45`, avg `-0.002107`, median `-0.001129`, mae `0.026984`
- 10d: sample `40`, hit `0.725`, avg `0.013167`, median `0.027869`, mae `0.039012`
- 20d: sample `40`, hit `0.675`, avg `0.018702`, median `0.045022`, mae `0.058822`
- 60d: sample `40`, hit `0.6`, avg `0.009107`, median `0.068712`, mae `0.108101`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.005848`, median `0.000766`, mae `0.016227`
- 5d: sample `40`, hit `0.475`, avg `-0.008988`, median `-0.001429`, mae `0.01864`
- 10d: sample `40`, hit `0.4`, avg `-0.003441`, median `-0.006017`, mae `0.016616`
- 20d: sample `40`, hit `0.625`, avg `0.012338`, median `0.020226`, mae `0.035155`
- 60d: sample `40`, hit `0.7`, avg `0.035262`, median `0.050438`, mae `0.061495`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.005848`, median `0.000766`, mae `0.016227`
- 5d: sample `40`, hit `0.475`, avg `-0.008988`, median `-0.001429`, mae `0.01864`
- 10d: sample `40`, hit `0.4`, avg `-0.003441`, median `-0.006017`, mae `0.016616`
- 20d: sample `40`, hit `0.625`, avg `0.012338`, median `0.020226`, mae `0.035155`
- 60d: sample `40`, hit `0.7`, avg `0.035262`, median `0.050438`, mae `0.061495`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.005848`, median `0.000766`, mae `0.016227`
- 5d: sample `40`, hit `0.475`, avg `-0.008988`, median `-0.001429`, mae `0.01864`
- 10d: sample `40`, hit `0.4`, avg `-0.003441`, median `-0.006017`, mae `0.016616`
- 20d: sample `40`, hit `0.625`, avg `0.012338`, median `0.020226`, mae `0.035155`
- 60d: sample `40`, hit `0.7`, avg `0.035262`, median `0.050438`, mae `0.061495`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.005848`, median `0.000766`, mae `0.016227`
- 5d: sample `40`, hit `0.475`, avg `-0.008988`, median `-0.001429`, mae `0.01864`
- 10d: sample `40`, hit `0.4`, avg `-0.003441`, median `-0.006017`, mae `0.016616`
- 20d: sample `40`, hit `0.625`, avg `0.012338`, median `0.020226`, mae `0.035155`
- 60d: sample `40`, hit `0.7`, avg `0.035262`, median `0.050438`, mae `0.061495`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.001552`, median `0.000707`, mae `0.02159`
- 5d: sample `40`, hit `0.45`, avg `-0.002107`, median `-0.001129`, mae `0.026984`
- 10d: sample `40`, hit `0.725`, avg `0.013167`, median `0.027869`, mae `0.039012`
- 20d: sample `40`, hit `0.675`, avg `0.018702`, median `0.045022`, mae `0.058822`
- 60d: sample `40`, hit `0.6`, avg `0.009107`, median `0.068712`, mae `0.108101`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `-0.0037`, median `0.000707`, mae `0.018908`
- 5d: sample `80`, hit `0.4625`, avg `-0.005547`, median `-0.001429`, mae `0.022812`
- 10d: sample `80`, hit `0.5625`, avg `0.004863`, median `0.006208`, mae `0.027814`
- 20d: sample `80`, hit `0.65`, avg `0.01552`, median `0.021759`, mae `0.046988`
- 60d: sample `80`, hit `0.65`, avg `0.022185`, median `0.055167`, mae `0.084798`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.005848`, median `0.000766`, mae `0.016227`
- 5d: sample `40`, hit `0.475`, avg `-0.008988`, median `-0.001429`, mae `0.01864`
- 10d: sample `40`, hit `0.4`, avg `-0.003441`, median `-0.006017`, mae `0.016616`
- 20d: sample `40`, hit `0.625`, avg `0.012338`, median `0.020226`, mae `0.035155`
- 60d: sample `40`, hit `0.7`, avg `0.035262`, median `0.050438`, mae `0.061495`

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
