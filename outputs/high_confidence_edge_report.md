# High Confidence Edge Report

Generated at: `2026-08-04T14:42:18.753415+00:00`

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
- 3d: sample `80`, hit `0.65`, avg `0.002466`, median `0.004569`, mae `0.013794`
- 5d: sample `80`, hit `0.675`, avg `0.002752`, median `0.004613`, mae `0.016292`
- 10d: sample `80`, hit `0.4875`, avg `0.001985`, median `-0.001676`, mae `0.023717`
- 20d: sample `80`, hit `0.625`, avg `0.002127`, median `0.01011`, mae `0.035997`
- 60d: sample `80`, hit `0.5375`, avg `0.008387`, median `0.019715`, mae `0.072127`

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
- 3d: sample `8`, hit `0.625`, avg `0.002372`, median `0.006565`, mae `0.014407`
- 5d: sample `8`, hit `0.75`, avg `0.010834`, median `0.018358`, mae `0.017737`
- 10d: sample `8`, hit `0.75`, avg `0.01183`, median `0.021406`, mae `0.021896`
- 20d: sample `8`, hit `0.875`, avg `0.014043`, median `0.01666`, mae `0.018946`
- 60d: sample `8`, hit `0.75`, avg `0.047567`, median `0.069875`, mae `0.06143`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.01082`, median `-0.009383`, mae `0.01735`
- 5d: sample `8`, hit `0.5`, avg `-0.006248`, median `0.000415`, mae `0.017401`
- 10d: sample `8`, hit `0.25`, avg `-0.007474`, median `-0.015123`, mae `0.020674`
- 20d: sample `8`, hit `0.5`, avg `-0.005629`, median `0.020068`, mae `0.030233`
- 60d: sample `8`, hit `0.25`, avg `-0.030319`, median `-0.03081`, mae `0.044875`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.002466, 'median_return': 0.004569, 'mean_absolute_return': 0.013794, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.03592}, '5d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.002752, 'median_return': 0.004613, 'mean_absolute_return': 0.016292, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 80, 'hit_rate': 0.4875, 'avg_return': 0.001985, 'median_return': -0.001676, 'mean_absolute_return': 0.023717, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.002127, 'median_return': 0.01011, 'mean_absolute_return': 0.035997, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 80, 'hit_rate': 0.5375, 'avg_return': 0.008387, 'median_return': 0.019715, 'mean_absolute_return': 0.072127, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.19145}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.01082, 'median_return': -0.009383, 'mean_absolute_return': 0.01735, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.01018}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.006248, 'median_return': 0.000415, 'mean_absolute_return': 0.017401, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.007474, 'median_return': -0.015123, 'mean_absolute_return': 0.020674, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.005629, 'median_return': 0.020068, 'mean_absolute_return': 0.030233, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.029166}, '60d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.030319, 'median_return': -0.03081, 'mean_absolute_return': 0.044875, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.046132}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.003942, 'median_return': 0.005642, 'mean_absolute_return': 0.013399, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.03592}, '5d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.003752, 'median_return': 0.00609, 'mean_absolute_return': 0.016169, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.003036, 'median_return': 0.001935, 'mean_absolute_return': 0.024055, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.002989, 'median_return': 0.01011, 'mean_absolute_return': 0.036637, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.012688, 'median_return': 0.029831, 'mean_absolute_return': 0.075155, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.65}, '5d': {'sample_size': 80, 'hit_rate': 0.675}, '10d': {'sample_size': 80, 'hit_rate': 0.4875}, '20d': {'sample_size': 80, 'hit_rate': 0.625}, '60d': {'sample_size': 80, 'hit_rate': 0.5375}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.35, 'primary_minus_secondary': 0.3, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.325, 'primary_minus_secondary': 0.35, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.375, 'primary_minus_secondary': 0.25, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.075, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.002466, 'median_return': 0.004569, 'mean_absolute_return': 0.013794, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.03592}, '5d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.002752, 'median_return': 0.004613, 'mean_absolute_return': 0.016292, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 80, 'hit_rate': 0.4875, 'avg_return': 0.001985, 'median_return': -0.001676, 'mean_absolute_return': 0.023717, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.002127, 'median_return': 0.01011, 'mean_absolute_return': 0.035997, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 80, 'hit_rate': 0.5375, 'avg_return': 0.008387, 'median_return': 0.019715, 'mean_absolute_return': 0.072127, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.003106`, median `0.000603`, mae `0.011831`
- 5d: sample `40`, hit `0.625`, avg `-0.002478`, median `0.003005`, mae `0.013523`
- 10d: sample `40`, hit `0.375`, avg `-0.004757`, median `-0.007117`, mae `0.017306`
- 20d: sample `40`, hit `0.525`, avg `-0.002031`, median `0.001555`, mae `0.028092`
- 60d: sample `40`, hit `0.4`, avg `-0.005946`, median `-0.018455`, mae `0.055554`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.009928`, median `0.011125`, mae `0.017662`
- 5d: sample `20`, hit `0.7`, avg `0.009158`, median `0.01152`, mae `0.021515`
- 10d: sample `20`, hit `0.6`, avg `0.016853`, median `0.017789`, mae `0.031923`
- 20d: sample `20`, hit `0.8`, avg `0.024102`, median `0.030862`, mae `0.044586`
- 60d: sample `20`, hit `0.7`, avg `0.039514`, median `0.061844`, mae `0.089284`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.003106`, median `0.000603`, mae `0.011831`
- 5d: sample `40`, hit `0.625`, avg `-0.002478`, median `0.003005`, mae `0.013523`
- 10d: sample `40`, hit `0.375`, avg `-0.004757`, median `-0.007117`, mae `0.017306`
- 20d: sample `40`, hit `0.525`, avg `-0.002031`, median `0.001555`, mae `0.028092`
- 60d: sample `40`, hit `0.4`, avg `-0.005946`, median `-0.018455`, mae `0.055554`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.009928`, median `0.011125`, mae `0.017662`
- 5d: sample `20`, hit `0.7`, avg `0.009158`, median `0.01152`, mae `0.021515`
- 10d: sample `20`, hit `0.6`, avg `0.016853`, median `0.017789`, mae `0.031923`
- 20d: sample `20`, hit `0.8`, avg `0.024102`, median `0.030862`, mae `0.044586`
- 60d: sample `20`, hit `0.7`, avg `0.039514`, median `0.061844`, mae `0.089284`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.003106`, median `0.000603`, mae `0.011831`
- 5d: sample `40`, hit `0.625`, avg `-0.002478`, median `0.003005`, mae `0.013523`
- 10d: sample `40`, hit `0.375`, avg `-0.004757`, median `-0.007117`, mae `0.017306`
- 20d: sample `40`, hit `0.525`, avg `-0.002031`, median `0.001555`, mae `0.028092`
- 60d: sample `40`, hit `0.4`, avg `-0.005946`, median `-0.018455`, mae `0.055554`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.75`, avg `0.008039`, median `0.010664`, mae `0.015758`
- 5d: sample `40`, hit `0.725`, avg `0.007981`, median `0.010593`, mae `0.019062`
- 10d: sample `40`, hit `0.6`, avg `0.008727`, median `0.00903`, mae `0.030128`
- 20d: sample `40`, hit `0.725`, avg `0.006286`, median `0.015275`, mae `0.043901`
- 60d: sample `40`, hit `0.675`, avg `0.02272`, median `0.055465`, mae `0.088701`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.65`, avg `0.002466`, median `0.004569`, mae `0.013794`
- 5d: sample `80`, hit `0.675`, avg `0.002752`, median `0.004613`, mae `0.016292`
- 10d: sample `80`, hit `0.4875`, avg `0.001985`, median `-0.001676`, mae `0.023717`
- 20d: sample `80`, hit `0.625`, avg `0.002127`, median `0.01011`, mae `0.035997`
- 60d: sample `80`, hit `0.5375`, avg `0.008387`, median `0.019715`, mae `0.072127`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `80`
- 3d: sample `80`, hit `0.65`, avg `0.002466`, median `0.004569`, mae `0.013794`
- 5d: sample `80`, hit `0.675`, avg `0.002752`, median `0.004613`, mae `0.016292`
- 10d: sample `80`, hit `0.4875`, avg `0.001985`, median `-0.001676`, mae `0.023717`
- 20d: sample `80`, hit `0.625`, avg `0.002127`, median `0.01011`, mae `0.035997`
- 60d: sample `80`, hit `0.5375`, avg `0.008387`, median `0.019715`, mae `0.072127`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.002088`, median `0.000145`, mae `0.008559`
- 5d: sample `20`, hit `0.8`, avg `0.003889`, median `0.004606`, mae `0.009844`
- 10d: sample `20`, hit `0.4`, avg `-0.00226`, median `-0.002045`, mae `0.013814`
- 20d: sample `20`, hit `0.5`, avg `-0.001858`, median `0.001555`, mae `0.020727`
- 60d: sample `20`, hit `0.3`, avg `-0.014294`, median `-0.018455`, mae `0.045579`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.002088`, median `0.000145`, mae `0.008559`
- 5d: sample `20`, hit `0.8`, avg `0.003889`, median `0.004606`, mae `0.009844`
- 10d: sample `20`, hit `0.4`, avg `-0.00226`, median `-0.002045`, mae `0.013814`
- 20d: sample `20`, hit `0.5`, avg `-0.001858`, median `0.001555`, mae `0.020727`
- 60d: sample `20`, hit `0.3`, avg `-0.014294`, median `-0.018455`, mae `0.045579`

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
