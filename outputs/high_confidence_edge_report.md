# High Confidence Edge Report

Generated at: `2026-07-24T21:35:48.677306+00:00`

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
- 3d: sample `40`, hit `0.575`, avg `-0.005026`, median `0.001139`, mae `0.016587`
- 5d: sample `40`, hit `0.5`, avg `-0.008456`, median `0.000688`, mae `0.019188`
- 10d: sample `40`, hit `0.425`, avg `-0.004364`, median `-0.006017`, mae `0.017765`
- 20d: sample `40`, hit `0.625`, avg `0.010637`, median `0.020068`, mae `0.036505`
- 60d: sample `40`, hit `0.7`, avg `0.033692`, median `0.050438`, mae `0.065101`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.003201`, median `-0.001058`, mae `0.021984`
- 5d: sample `40`, hit `0.45`, avg `-0.002409`, median `-0.001129`, mae `0.027229`
- 10d: sample `40`, hit `0.725`, avg `0.012896`, median `0.027869`, mae `0.038741`
- 20d: sample `40`, hit `0.65`, avg `0.01694`, median `0.035693`, mae `0.0577`
- 60d: sample `40`, hit `0.625`, avg `0.011168`, median `0.068712`, mae `0.106343`

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
- 3d: sample `8`, hit `0.25`, avg `-0.01363`, median `-0.010033`, mae `0.024795`
- 5d: sample `8`, hit `0.375`, avg `-0.025133`, median `-0.022295`, mae `0.031476`
- 10d: sample `8`, hit `0.125`, avg `-0.011762`, median `-0.007755`, mae `0.014861`
- 20d: sample `8`, hit `0.375`, avg `-0.007317`, median `-0.001666`, mae `0.045176`
- 60d: sample `8`, hit `0.5`, avg `0.011993`, median `0.037425`, mae `0.076436`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.01363`, median `-0.010033`, mae `0.024795`
- 5d: sample `8`, hit `0.375`, avg `-0.025133`, median `-0.022295`, mae `0.031476`
- 10d: sample `8`, hit `0.125`, avg `-0.011762`, median `-0.007755`, mae `0.014861`
- 20d: sample `8`, hit `0.375`, avg `-0.007317`, median `-0.001666`, mae `0.045176`
- 60d: sample `8`, hit `0.5`, avg `0.011993`, median `0.037425`, mae `0.076436`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': -0.005026, 'median_return': 0.001139, 'mean_absolute_return': 0.016587, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.008456, 'median_return': 0.000688, 'mean_absolute_return': 0.019188, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.004364, 'median_return': -0.006017, 'mean_absolute_return': 0.017765, 'max_adverse_excursion': -0.064399, 'max_favorable_excursion': 0.035901}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.010637, 'median_return': 0.020068, 'mean_absolute_return': 0.036505, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.033692, 'median_return': 0.050438, 'mean_absolute_return': 0.065101, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.01363, 'median_return': -0.010033, 'mean_absolute_return': 0.024795, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.025133, 'median_return': -0.022295, 'mean_absolute_return': 0.031476, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.010589}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.011762, 'median_return': -0.007755, 'mean_absolute_return': 0.014861, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.012396}, '20d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.007317, 'median_return': -0.001666, 'mean_absolute_return': 0.045176, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.011993, 'median_return': 0.037425, 'mean_absolute_return': 0.076436, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': -0.003056, 'median_return': 0.000766, 'mean_absolute_return': 0.018674, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.003244, 'median_return': -0.000123, 'mean_absolute_return': 0.02229, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.006047, 'median_return': 0.016212, 'mean_absolute_return': 0.029741, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.016134, 'median_return': 0.026005, 'mean_absolute_return': 0.047317, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.02359, 'median_return': 0.058473, 'mean_absolute_return': 0.086754, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.19082}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5625}, '5d': {'sample_size': 80, 'hit_rate': 0.525}, '10d': {'sample_size': 80, 'hit_rate': 0.35}, '20d': {'sample_size': 80, 'hit_rate': 0.4875}, '60d': {'sample_size': 80, 'hit_rate': 0.5375}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.125, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.05, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.075, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': -0.00271, 'median_return': 0.001405, 'mean_absolute_return': 0.019093, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': -0.002361, 'median_return': 0.003005, 'mean_absolute_return': 0.021026, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.051324}, '10d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.005471, 'median_return': 0.004547, 'mean_absolute_return': 0.02447, 'max_adverse_excursion': -0.068474, 'max_favorable_excursion': 0.061544}, '20d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.019447, 'median_return': 0.02086, 'mean_absolute_return': 0.042849, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.110689}, '60d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.035819, 'median_return': 0.057625, 'mean_absolute_return': 0.076241, 'max_adverse_excursion': -0.177732, 'max_favorable_excursion': 0.19082}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.008325, 'median_return': -0.01019, 'mean_absolute_return': 0.019864, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 20, 'hit_rate': 0.25, 'avg_return': -0.01465, 'median_return': -0.009549, 'mean_absolute_return': 0.029756, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.000649, 'median_return': 0.021567, 'mean_absolute_return': 0.039602, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.003186, 'median_return': 0.021735, 'mean_absolute_return': 0.059862, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.017738, 'median_return': 0.027637, 'mean_absolute_return': 0.114166, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.129489}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `-0.005026`, median `0.001139`, mae `0.016587`
- 5d: sample `40`, hit `0.5`, avg `-0.008456`, median `0.000688`, mae `0.019188`
- 10d: sample `40`, hit `0.425`, avg `-0.004364`, median `-0.006017`, mae `0.017765`
- 20d: sample `40`, hit `0.625`, avg `0.010637`, median `0.020068`, mae `0.036505`
- 60d: sample `40`, hit `0.7`, avg `0.033692`, median `0.050438`, mae `0.065101`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.003201`, median `-0.001058`, mae `0.021984`
- 5d: sample `40`, hit `0.45`, avg `-0.002409`, median `-0.001129`, mae `0.027229`
- 10d: sample `40`, hit `0.725`, avg `0.012896`, median `0.027869`, mae `0.038741`
- 20d: sample `40`, hit `0.65`, avg `0.01694`, median `0.035693`, mae `0.0577`
- 60d: sample `40`, hit `0.625`, avg `0.011168`, median `0.068712`, mae `0.106343`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `-0.005026`, median `0.001139`, mae `0.016587`
- 5d: sample `40`, hit `0.5`, avg `-0.008456`, median `0.000688`, mae `0.019188`
- 10d: sample `40`, hit `0.425`, avg `-0.004364`, median `-0.006017`, mae `0.017765`
- 20d: sample `40`, hit `0.625`, avg `0.010637`, median `0.020068`, mae `0.036505`
- 60d: sample `40`, hit `0.7`, avg `0.033692`, median `0.050438`, mae `0.065101`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `-0.005026`, median `0.001139`, mae `0.016587`
- 5d: sample `40`, hit `0.5`, avg `-0.008456`, median `0.000688`, mae `0.019188`
- 10d: sample `40`, hit `0.425`, avg `-0.004364`, median `-0.006017`, mae `0.017765`
- 20d: sample `40`, hit `0.625`, avg `0.010637`, median `0.020068`, mae `0.036505`
- 60d: sample `40`, hit `0.7`, avg `0.033692`, median `0.050438`, mae `0.065101`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `-0.005026`, median `0.001139`, mae `0.016587`
- 5d: sample `40`, hit `0.5`, avg `-0.008456`, median `0.000688`, mae `0.019188`
- 10d: sample `40`, hit `0.425`, avg `-0.004364`, median `-0.006017`, mae `0.017765`
- 20d: sample `40`, hit `0.625`, avg `0.010637`, median `0.020068`, mae `0.036505`
- 60d: sample `40`, hit `0.7`, avg `0.033692`, median `0.050438`, mae `0.065101`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `-0.005026`, median `0.001139`, mae `0.016587`
- 5d: sample `40`, hit `0.5`, avg `-0.008456`, median `0.000688`, mae `0.019188`
- 10d: sample `40`, hit `0.425`, avg `-0.004364`, median `-0.006017`, mae `0.017765`
- 20d: sample `40`, hit `0.625`, avg `0.010637`, median `0.020068`, mae `0.036505`
- 60d: sample `40`, hit `0.7`, avg `0.033692`, median `0.050438`, mae `0.065101`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.003201`, median `-0.001058`, mae `0.021984`
- 5d: sample `40`, hit `0.45`, avg `-0.002409`, median `-0.001129`, mae `0.027229`
- 10d: sample `40`, hit `0.725`, avg `0.012896`, median `0.027869`, mae `0.038741`
- 20d: sample `40`, hit `0.65`, avg `0.01694`, median `0.035693`, mae `0.0577`
- 60d: sample `40`, hit `0.625`, avg `0.011168`, median `0.068712`, mae `0.106343`

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
- 3d: sample `80`, hit `0.5125`, avg `-0.004114`, median `0.000603`, mae `0.019286`
- 5d: sample `80`, hit `0.475`, avg `-0.005433`, median `-0.001129`, mae `0.023208`
- 10d: sample `80`, hit `0.575`, avg `0.004266`, median `0.006208`, mae `0.028253`
- 20d: sample `80`, hit `0.6375`, avg `0.013789`, median `0.02086`, mae `0.047102`
- 60d: sample `80`, hit `0.6625`, avg `0.02243`, median `0.055167`, mae `0.085722`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `-0.005026`, median `0.001139`, mae `0.016587`
- 5d: sample `40`, hit `0.5`, avg `-0.008456`, median `0.000688`, mae `0.019188`
- 10d: sample `40`, hit `0.425`, avg `-0.004364`, median `-0.006017`, mae `0.017765`
- 20d: sample `40`, hit `0.625`, avg `0.010637`, median `0.020068`, mae `0.036505`
- 60d: sample `40`, hit `0.7`, avg `0.033692`, median `0.050438`, mae `0.065101`

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
