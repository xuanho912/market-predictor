# High Confidence Edge Report

Generated at: `2026-09-02T05:53:44.260642+00:00`

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
- 3d: sample `40`, hit `0.5`, avg `-0.001576`, median `0.000603`, mae `0.012612`
- 5d: sample `40`, hit `0.5`, avg `-0.007775`, median `0.000208`, mae `0.014813`
- 10d: sample `40`, hit `0.4`, avg `-0.00423`, median `-0.006017`, mae `0.019427`
- 20d: sample `40`, hit `0.675`, avg `0.014078`, median `0.02086`, mae `0.032995`
- 60d: sample `40`, hit `0.675`, avg `0.040588`, median `0.061042`, mae `0.07126`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.725`, avg `0.006513`, median `0.010018`, mae `0.01597`
- 5d: sample `40`, hit `0.625`, avg `0.007698`, median `0.009194`, mae `0.018623`
- 10d: sample `40`, hit `0.5`, avg `0.004968`, median `0.000937`, mae `0.030476`
- 20d: sample `40`, hit `0.7`, avg `0.017015`, median `0.03392`, mae `0.04119`
- 60d: sample `40`, hit `0.775`, avg `0.041176`, median `0.073651`, mae `0.09268`

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
- 3d: sample `8`, hit `0.375`, avg `-0.009181`, median `-0.001658`, mae `0.015069`
- 5d: sample `8`, hit `0.375`, avg `-0.013975`, median `-0.012956`, mae `0.020145`
- 10d: sample `8`, hit `0.375`, avg `-6e-05`, median `-0.0004`, mae `0.019072`
- 20d: sample `8`, hit `0.875`, avg `0.028723`, median `0.033999`, mae `0.042549`
- 60d: sample `8`, hit `0.875`, avg `0.078668`, median `0.101282`, mae `0.092886`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.009181`, median `-0.001658`, mae `0.015069`
- 5d: sample `8`, hit `0.375`, avg `-0.013975`, median `-0.012956`, mae `0.020145`
- 10d: sample `8`, hit `0.375`, avg `-6e-05`, median `-0.0004`, mae `0.019072`
- 20d: sample `8`, hit `0.875`, avg `0.028723`, median `0.033999`, mae `0.042549`
- 60d: sample `8`, hit `0.875`, avg `0.078668`, median `0.101282`, mae `0.092886`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.001576, 'median_return': 0.000603, 'mean_absolute_return': 0.012612, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.025832}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.007775, 'median_return': 0.000208, 'mean_absolute_return': 0.014813, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.00423, 'median_return': -0.006017, 'mean_absolute_return': 0.019427, 'max_adverse_excursion': -0.038485, 'max_favorable_excursion': 0.035901}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.014078, 'median_return': 0.02086, 'mean_absolute_return': 0.032995, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.040588, 'median_return': 0.061042, 'mean_absolute_return': 0.07126, 'max_adverse_excursion': -0.088557, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.009181, 'median_return': -0.001658, 'mean_absolute_return': 0.015069, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.017427}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.013975, 'median_return': -0.012956, 'mean_absolute_return': 0.020145, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.011143}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -6e-05, 'median_return': -0.0004, 'mean_absolute_return': 0.019072, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.028723, 'median_return': 0.033999, 'mean_absolute_return': 0.042549, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.078668, 'median_return': 0.101282, 'mean_absolute_return': 0.092886, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.003763, 'median_return': 0.00531, 'mean_absolute_return': 0.014204, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.00151, 'median_return': 0.00175, 'mean_absolute_return': 0.016337, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.045689}, '10d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': 0.000417, 'median_return': -0.005891, 'mean_absolute_return': 0.025604, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.014083, 'median_return': 0.023289, 'mean_absolute_return': 0.036486, 'max_adverse_excursion': -0.118199, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.036683, 'median_return': 0.065995, 'mean_absolute_return': 0.080757, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.3875}, '5d': {'sample_size': 80, 'hit_rate': 0.4375}, '10d': {'sample_size': 80, 'hit_rate': 0.55}, '20d': {'sample_size': 80, 'hit_rate': 0.3125}, '60d': {'sample_size': 80, 'hit_rate': 0.275}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.375, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_minus_secondary': -0.45, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.000635, 'median_return': 0.001558, 'mean_absolute_return': 0.01481, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': -0.002993, 'median_return': 0.000873, 'mean_absolute_return': 0.016997, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.045689}, '10d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': 0.001329, 'median_return': -0.001222, 'mean_absolute_return': 0.022667, 'max_adverse_excursion': -0.038485, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.019161, 'median_return': 0.027893, 'mean_absolute_return': 0.032955, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 60, 'hit_rate': 0.75, 'avg_return': 0.050013, 'median_return': 0.065995, 'mean_absolute_return': 0.07524, 'max_adverse_excursion': -0.108365, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.007968, 'median_return': 0.01152, 'mean_absolute_return': 0.012731, 'max_adverse_excursion': -0.017054, 'max_favorable_excursion': 0.035961}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.008827, 'median_return': 0.011391, 'mean_absolute_return': 0.015881, 'max_adverse_excursion': -0.027115, 'max_favorable_excursion': 0.035465}, '10d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.00251, 'median_return': -0.013321, 'mean_absolute_return': 0.031804, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.004704, 'median_return': 0.037853, 'mean_absolute_return': 0.049506, 'max_adverse_excursion': -0.118199, 'max_favorable_excursion': 0.070755}, '60d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.013489, 'median_return': 0.087998, 'mean_absolute_return': 0.102159, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.117141}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.001576`, median `0.000603`, mae `0.012612`
- 5d: sample `40`, hit `0.5`, avg `-0.007775`, median `0.000208`, mae `0.014813`
- 10d: sample `40`, hit `0.4`, avg `-0.00423`, median `-0.006017`, mae `0.019427`
- 20d: sample `40`, hit `0.675`, avg `0.014078`, median `0.02086`, mae `0.032995`
- 60d: sample `40`, hit `0.675`, avg `0.040588`, median `0.061042`, mae `0.07126`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.003106`, median `0.007289`, mae `0.016062`
- 5d: sample `60`, hit `0.5667`, avg `0.001332`, median `0.0019`, mae `0.018471`
- 10d: sample `60`, hit `0.45`, avg `0.002021`, median `-0.00367`, mae `0.026649`
- 20d: sample `60`, hit `0.7`, avg `0.018679`, median `0.031196`, mae `0.038344`
- 60d: sample `60`, hit `0.75`, avg `0.043772`, median `0.073651`, mae `0.088438`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.001576`, median `0.000603`, mae `0.012612`
- 5d: sample `40`, hit `0.5`, avg `-0.007775`, median `0.000208`, mae `0.014813`
- 10d: sample `40`, hit `0.4`, avg `-0.00423`, median `-0.006017`, mae `0.019427`
- 20d: sample `40`, hit `0.675`, avg `0.014078`, median `0.02086`, mae `0.032995`
- 60d: sample `40`, hit `0.675`, avg `0.040588`, median `0.061042`, mae `0.07126`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.000676`, median `0.003412`, mae `0.017727`
- 5d: sample `40`, hit `0.525`, avg `-0.002415`, median `0.001087`, mae `0.019766`
- 10d: sample `40`, hit `0.475`, avg `0.004287`, median `-0.0004`, mae `0.024072`
- 20d: sample `40`, hit `0.75`, avg `0.025666`, median `0.031196`, mae `0.032763`
- 60d: sample `40`, hit `0.8`, avg `0.058913`, median `0.073651`, mae `0.081578`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.001576`, median `0.000603`, mae `0.012612`
- 5d: sample `40`, hit `0.5`, avg `-0.007775`, median `0.000208`, mae `0.014813`
- 10d: sample `40`, hit `0.4`, avg `-0.00423`, median `-0.006017`, mae `0.019427`
- 20d: sample `40`, hit `0.675`, avg `0.014078`, median `0.02086`, mae `0.032995`
- 60d: sample `40`, hit `0.675`, avg `0.040588`, median `0.061042`, mae `0.07126`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.003106`, median `0.007289`, mae `0.016062`
- 5d: sample `60`, hit `0.5667`, avg `0.001332`, median `0.0019`, mae `0.018471`
- 10d: sample `60`, hit `0.45`, avg `0.002021`, median `-0.00367`, mae `0.026649`
- 20d: sample `60`, hit `0.7`, avg `0.018679`, median `0.031196`, mae `0.038344`
- 60d: sample `60`, hit `0.75`, avg `0.043772`, median `0.073651`, mae `0.088438`

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
- 3d: sample `80`, hit `0.6125`, avg `0.002469`, median `0.003412`, mae `0.014291`
- 5d: sample `80`, hit `0.5625`, avg `-3.8e-05`, median `0.001303`, mae `0.016718`
- 10d: sample `80`, hit `0.45`, avg `0.000369`, median `-0.005891`, mae `0.024951`
- 20d: sample `80`, hit `0.6875`, avg `0.015547`, median `0.027893`, mae `0.037092`
- 60d: sample `80`, hit `0.725`, avg `0.040882`, median `0.06608`, mae `0.08197`

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
