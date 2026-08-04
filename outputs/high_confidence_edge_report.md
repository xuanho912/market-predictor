# High Confidence Edge Report

Generated at: `2026-08-04T04:35:55.373697+00:00`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.7333`, avg `0.007296`, median `0.010897`, mae `0.015192`
- 5d: sample `60`, hit `0.7`, avg `0.009214`, median `0.011604`, mae `0.019962`
- 10d: sample `60`, hit `0.8`, avg `0.01788`, median `0.019171`, mae `0.024593`
- 20d: sample `60`, hit `0.9`, avg `0.031446`, median `0.029072`, mae `0.035475`
- 60d: sample `60`, hit `0.8167`, avg `0.056445`, median `0.074246`, mae `0.075261`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.011931`, median `0.01463`, mae `0.022821`
- 5d: sample `20`, hit `0.65`, avg `0.01473`, median `0.010394`, mae `0.023778`
- 10d: sample `20`, hit `0.8`, avg `0.02682`, median `0.031449`, mae `0.037641`
- 20d: sample `20`, hit `0.85`, avg `0.042034`, median `0.045973`, mae `0.044493`
- 60d: sample `20`, hit `0.6`, avg `0.019279`, median `0.068712`, mae `0.106266`

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
- 3d: sample `8`, hit `0.5`, avg `-0.000482`, median `0.012272`, mae `0.017505`
- 5d: sample `8`, hit `0.875`, avg `0.005892`, median `0.009709`, mae `0.012456`
- 10d: sample `8`, hit `0.625`, avg `0.005166`, median `0.011031`, mae `0.018274`
- 20d: sample `8`, hit `1.0`, avg `0.043557`, median `0.058396`, mae `0.043557`
- 60d: sample `8`, hit `0.875`, avg `0.078417`, median `0.099838`, mae `0.090152`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.000482`, median `0.012272`, mae `0.017505`
- 5d: sample `8`, hit `0.875`, avg `0.005892`, median `0.009709`, mae `0.012456`
- 10d: sample `8`, hit `0.625`, avg `0.005166`, median `0.011031`, mae `0.018274`
- 20d: sample `8`, hit `1.0`, avg `0.043557`, median `0.058396`, mae `0.043557`
- 60d: sample `8`, hit `0.875`, avg `0.078417`, median `0.099838`, mae `0.090152`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.007296, 'median_return': 0.010897, 'mean_absolute_return': 0.015192, 'max_adverse_excursion': -0.037817, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.009214, 'median_return': 0.011604, 'mean_absolute_return': 0.019962, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 60, 'hit_rate': 0.8, 'avg_return': 0.01788, 'median_return': 0.019171, 'mean_absolute_return': 0.024593, 'max_adverse_excursion': -0.036599, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 60, 'hit_rate': 0.9, 'avg_return': 0.031446, 'median_return': 0.029072, 'mean_absolute_return': 0.035475, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 60, 'hit_rate': 0.8167, 'avg_return': 0.056445, 'median_return': 0.074246, 'mean_absolute_return': 0.075261, 'max_adverse_excursion': -0.171649, 'max_favorable_excursion': 0.147541}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.000482, 'median_return': 0.012272, 'mean_absolute_return': 0.017505, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.005892, 'median_return': 0.009709, 'mean_absolute_return': 0.012456, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.005166, 'median_return': 0.011031, 'mean_absolute_return': 0.018274, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.043557, 'median_return': 0.058396, 'mean_absolute_return': 0.043557, 'max_adverse_excursion': 0.011428, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.078417, 'median_return': 0.099838, 'mean_absolute_return': 0.090152, 'max_adverse_excursion': -0.04694, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.75, 'avg_return': 0.009447, 'median_return': 0.011414, 'mean_absolute_return': 0.017055, 'max_adverse_excursion': -0.037817, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.011115, 'median_return': 0.012091, 'mean_absolute_return': 0.021856, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.062217}, '10d': {'sample_size': 72, 'hit_rate': 0.8194, 'avg_return': 0.021776, 'median_return': 0.021584, 'mean_absolute_return': 0.028919, 'max_adverse_excursion': -0.061742, 'max_favorable_excursion': 0.098213}, '20d': {'sample_size': 72, 'hit_rate': 0.875, 'avg_return': 0.033041, 'median_return': 0.030922, 'mean_absolute_return': 0.037082, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.110981}, '60d': {'sample_size': 72, 'hit_rate': 0.75, 'avg_return': 0.043679, 'median_return': 0.068712, 'mean_absolute_return': 0.082219, 'max_adverse_excursion': -0.179568, 'max_favorable_excursion': 0.220253}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.625}, '5d': {'sample_size': 80, 'hit_rate': 0.6125}, '10d': {'sample_size': 80, 'hit_rate': 0.65}, '20d': {'sample_size': 80, 'hit_rate': 0.7125}, '60d': {'sample_size': 80, 'hit_rate': 0.7125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.025, 'both_hit': 31, 'both_miss': 9}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.05, 'both_hit': 31, 'both_miss': 9}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': -0.05, 'both_hit': 34, 'both_miss': 6}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.7125, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': 0.0, 'both_hit': 37, 'both_miss': 3}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.7125, 'secondary_hit_rate': 0.7375, 'primary_minus_secondary': -0.025, 'both_hit': 38, 'both_miss': 2}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.009287, 'median_return': 0.013919, 'mean_absolute_return': 0.019804, 'max_adverse_excursion': -0.037817, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.011136, 'median_return': 0.010394, 'mean_absolute_return': 0.02332, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.062217}, '10d': {'sample_size': 60, 'hit_rate': 0.7667, 'avg_return': 0.021858, 'median_return': 0.024811, 'mean_absolute_return': 0.031921, 'max_adverse_excursion': -0.061742, 'max_favorable_excursion': 0.098213}, '20d': {'sample_size': 60, 'hit_rate': 0.8667, 'avg_return': 0.035923, 'median_return': 0.030931, 'mean_absolute_return': 0.040455, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.110981}, '60d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.043924, 'median_return': 0.074246, 'mean_absolute_return': 0.091042, 'max_adverse_excursion': -0.179568, 'max_favorable_excursion': 0.220253}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.005957, 'median_return': 0.006315, 'mean_absolute_return': 0.008987, 'max_adverse_excursion': -0.017627, 'max_favorable_excursion': 0.017982}, '5d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.008963, 'median_return': 0.011604, 'mean_absolute_return': 0.013704, 'max_adverse_excursion': -0.019909, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 20, 'hit_rate': 0.9, 'avg_return': 0.014887, 'median_return': 0.017201, 'mean_absolute_return': 0.015657, 'max_adverse_excursion': -0.007491, 'max_favorable_excursion': 0.037487}, '20d': {'sample_size': 20, 'hit_rate': 0.95, 'avg_return': 0.028602, 'median_return': 0.03107, 'mean_absolute_return': 0.029551, 'max_adverse_excursion': -0.009488, 'max_favorable_excursion': 0.053054}, '60d': {'sample_size': 20, 'hit_rate': 0.95, 'avg_return': 0.056842, 'median_return': 0.062103, 'mean_absolute_return': 0.058924, 'max_adverse_excursion': -0.020815, 'max_favorable_excursion': 0.10629}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.775`, avg `0.007489`, median `0.010897`, mae `0.013183`
- 5d: sample `40`, hit `0.775`, avg `0.011771`, median `0.012091`, mae `0.017475`
- 10d: sample `40`, hit `0.85`, avg `0.01729`, median `0.017636`, mae `0.020598`
- 20d: sample `40`, hit `0.925`, avg `0.036834`, median `0.033582`, mae `0.037808`
- 60d: sample `40`, hit `0.95`, avg `0.073206`, median `0.084597`, mae `0.076593`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.011931`, median `0.01463`, mae `0.022821`
- 5d: sample `20`, hit `0.65`, avg `0.01473`, median `0.010394`, mae `0.023778`
- 10d: sample `20`, hit `0.8`, avg `0.02682`, median `0.031449`, mae `0.037641`
- 20d: sample `20`, hit `0.85`, avg `0.042034`, median `0.045973`, mae `0.044493`
- 60d: sample `20`, hit `0.6`, avg `0.019279`, median `0.068712`, mae `0.106266`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.775`, avg `0.007489`, median `0.010897`, mae `0.013183`
- 5d: sample `40`, hit `0.775`, avg `0.011771`, median `0.012091`, mae `0.017475`
- 10d: sample `40`, hit `0.85`, avg `0.01729`, median `0.017636`, mae `0.020598`
- 20d: sample `40`, hit `0.925`, avg `0.036834`, median `0.033582`, mae `0.037808`
- 60d: sample `40`, hit `0.95`, avg `0.073206`, median `0.084597`, mae `0.076593`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.011931`, median `0.01463`, mae `0.022821`
- 5d: sample `20`, hit `0.65`, avg `0.01473`, median `0.010394`, mae `0.023778`
- 10d: sample `20`, hit `0.8`, avg `0.02682`, median `0.031449`, mae `0.037641`
- 20d: sample `20`, hit `0.85`, avg `0.042034`, median `0.045973`, mae `0.044493`
- 60d: sample `20`, hit `0.6`, avg `0.019279`, median `0.068712`, mae `0.106266`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.775`, avg `0.007489`, median `0.010897`, mae `0.013183`
- 5d: sample `40`, hit `0.775`, avg `0.011771`, median `0.012091`, mae `0.017475`
- 10d: sample `40`, hit `0.85`, avg `0.01729`, median `0.017636`, mae `0.020598`
- 20d: sample `40`, hit `0.925`, avg `0.036834`, median `0.033582`, mae `0.037808`
- 60d: sample `40`, hit `0.95`, avg `0.073206`, median `0.084597`, mae `0.076593`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.006908`, median `0.011534`, mae `0.019211`
- 5d: sample `20`, hit `0.55`, avg `0.004099`, median `0.008121`, mae `0.024936`
- 10d: sample `20`, hit `0.7`, avg `0.019061`, median `0.023905`, mae `0.032582`
- 20d: sample `20`, hit `0.85`, avg `0.020669`, median `0.017648`, mae `0.030807`
- 60d: sample `20`, hit `0.55`, avg `0.022923`, median `0.056874`, mae `0.072596`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.011931`, median `0.01463`, mae `0.022821`
- 5d: sample `20`, hit `0.65`, avg `0.01473`, median `0.010394`, mae `0.023778`
- 10d: sample `20`, hit `0.8`, avg `0.02682`, median `0.031449`, mae `0.037641`
- 20d: sample `20`, hit `0.85`, avg `0.042034`, median `0.045973`, mae `0.044493`
- 60d: sample `20`, hit `0.6`, avg `0.019279`, median `0.068712`, mae `0.106266`

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
- 3d: sample `80`, hit `0.725`, avg `0.008454`, median `0.011414`, mae `0.0171`
- 5d: sample `80`, hit `0.6875`, avg `0.010593`, median `0.010394`, mae `0.020916`
- 10d: sample `80`, hit `0.8`, avg `0.020115`, median `0.021536`, mae `0.027855`
- 20d: sample `80`, hit `0.8875`, avg `0.034093`, median `0.030931`, mae `0.037729`
- 60d: sample `80`, hit `0.7625`, avg `0.047153`, median `0.069875`, mae `0.083012`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.7333`, avg `0.007296`, median `0.010897`, mae `0.015192`
- 5d: sample `60`, hit `0.7`, avg `0.009214`, median `0.011604`, mae `0.019962`
- 10d: sample `60`, hit `0.8`, avg `0.01788`, median `0.019171`, mae `0.024593`
- 20d: sample `60`, hit `0.9`, avg `0.031446`, median `0.029072`, mae `0.035475`
- 60d: sample `60`, hit `0.8167`, avg `0.056445`, median `0.074246`, mae `0.075261`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.725`, avg `0.008454`, median `0.011414`, mae `0.0171`
- 5d: sample `80`, hit `0.6875`, avg `0.010593`, median `0.010394`, mae `0.020916`
- 10d: sample `80`, hit `0.8`, avg `0.020115`, median `0.021536`, mae `0.027855`
- 20d: sample `80`, hit `0.8875`, avg `0.034093`, median `0.030931`, mae `0.037729`
- 60d: sample `80`, hit `0.7625`, avg `0.047153`, median `0.069875`, mae `0.083012`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.7333`, avg `0.007296`, median `0.010897`, mae `0.015192`
- 5d: sample `60`, hit `0.7`, avg `0.009214`, median `0.011604`, mae `0.019962`
- 10d: sample `60`, hit `0.8`, avg `0.01788`, median `0.019171`, mae `0.024593`
- 20d: sample `60`, hit `0.9`, avg `0.031446`, median `0.029072`, mae `0.035475`
- 60d: sample `60`, hit `0.8167`, avg `0.056445`, median `0.074246`, mae `0.075261`

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
