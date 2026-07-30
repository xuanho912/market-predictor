# High Confidence Edge Report

Generated at: `2026-07-30T14:35:01.851570+00:00`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.001415`, median `0.006714`, mae `0.01713`
- 5d: sample `20`, hit `0.6`, avg `-0.004395`, median `0.002223`, mae `0.017434`
- 10d: sample `20`, hit `0.3`, avg `-0.002636`, median `-0.006017`, mae `0.01912`
- 20d: sample `20`, hit `0.65`, avg `0.019939`, median `0.029166`, mae `0.036275`
- 60d: sample `20`, hit `0.65`, avg `0.033758`, median `0.046132`, mae `0.06997`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.003955`, median `0.001502`, mae `0.012811`
- 5d: sample `60`, hit `0.6167`, avg `0.005269`, median `0.002451`, mae `0.01671`
- 10d: sample `60`, hit `0.5167`, avg `0.003363`, median `0.000937`, mae `0.029273`
- 20d: sample `60`, hit `0.6333`, avg `0.011747`, median `0.018939`, mae `0.046793`
- 60d: sample `60`, hit `0.5333`, avg `0.008785`, median `0.016026`, mae `0.078`

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
- 3d: sample `8`, hit `0.375`, avg `-0.014954`, median `-0.010033`, mae `0.021574`
- 5d: sample `8`, hit `0.375`, avg `-0.022298`, median `-0.022295`, mae `0.026792`
- 10d: sample `8`, hit `0.25`, avg `-0.005325`, median `-0.007011`, mae `0.017398`
- 20d: sample `8`, hit `0.625`, avg `0.011513`, median `0.020068`, mae `0.033878`
- 60d: sample `8`, hit `0.625`, avg `0.033239`, median `0.046132`, mae `0.0624`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.014954`, median `-0.010033`, mae `0.021574`
- 5d: sample `8`, hit `0.375`, avg `-0.022298`, median `-0.022295`, mae `0.026792`
- 10d: sample `8`, hit `0.25`, avg `-0.005325`, median `-0.007011`, mae `0.017398`
- 20d: sample `8`, hit `0.625`, avg `0.011513`, median `0.020068`, mae `0.033878`
- 60d: sample `8`, hit `0.625`, avg `0.033239`, median `0.046132`, mae `0.0624`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.001415, 'median_return': 0.006714, 'mean_absolute_return': 0.01713, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.029522}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.004395, 'median_return': 0.002223, 'mean_absolute_return': 0.017434, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.046339}, '10d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.002636, 'median_return': -0.006017, 'mean_absolute_return': 0.01912, 'max_adverse_excursion': -0.038485, 'max_favorable_excursion': 0.043492}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.019939, 'median_return': 0.029166, 'mean_absolute_return': 0.036275, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.086905}, '60d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.033758, 'median_return': 0.046132, 'mean_absolute_return': 0.06997, 'max_adverse_excursion': -0.071921, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.014954, 'median_return': -0.010033, 'mean_absolute_return': 0.021574, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.017427}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.022298, 'median_return': -0.022295, 'mean_absolute_return': 0.026792, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.011143}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.005325, 'median_return': -0.007011, 'mean_absolute_return': 0.017398, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.011513, 'median_return': 0.020068, 'mean_absolute_return': 0.033878, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.033239, 'median_return': 0.046132, 'mean_absolute_return': 0.0624, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.005351, 'median_return': 0.005296, 'mean_absolute_return': 0.013037, 'max_adverse_excursion': -0.0325, 'max_favorable_excursion': 0.040779}, '5d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.005648, 'median_return': 0.002451, 'mean_absolute_return': 0.015791, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': 0.002662, 'median_return': -0.000231, 'mean_absolute_return': 0.027772, 'max_adverse_excursion': -0.068474, 'max_favorable_excursion': 0.080212}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.014049, 'median_return': 0.020226, 'mean_absolute_return': 0.045306, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.013005, 'median_return': 0.022632, 'mean_absolute_return': 0.077503, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.21366}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.45}, '5d': {'sample_size': 80, 'hit_rate': 0.4375}, '10d': {'sample_size': 80, 'hit_rate': 0.4375}, '20d': {'sample_size': 80, 'hit_rate': 0.4375}, '60d': {'sample_size': 80, 'hit_rate': 0.5125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.002638, 'median_return': 0.003785, 'mean_absolute_return': 0.015118, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.040779}, '5d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.000523, 'median_return': 0.001695, 'mean_absolute_return': 0.017243, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.057302}, '10d': {'sample_size': 60, 'hit_rate': 0.4167, 'avg_return': 0.000233, 'median_return': -0.002081, 'mean_absolute_return': 0.024598, 'max_adverse_excursion': -0.068474, 'max_favorable_excursion': 0.080212}, '20d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.014845, 'median_return': 0.020068, 'mean_absolute_return': 0.03882, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.129427}, '60d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.031202, 'median_return': 0.037425, 'mean_absolute_return': 0.071421, 'max_adverse_excursion': -0.116615, 'max_favorable_excursion': 0.21366}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.005365, 'median_return': 0.001502, 'mean_absolute_return': 0.010209, 'max_adverse_excursion': -0.013908, 'max_favorable_excursion': 0.039325}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.009843, 'median_return': 0.004613, 'mean_absolute_return': 0.015834, 'max_adverse_excursion': -0.020263, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.006755, 'median_return': 0.014312, 'mean_absolute_return': 0.033145, 'max_adverse_excursion': -0.068262, 'max_favorable_excursion': 0.068253}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.010647, 'median_return': 0.022363, 'mean_absolute_return': 0.060193, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.033493, 'median_return': -0.003135, 'mean_absolute_return': 0.089708, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.109194}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.00107`, median `0.002067`, mae `0.01433`
- 5d: sample `40`, hit `0.625`, avg `-0.002856`, median `0.001303`, mae `0.013752`
- 10d: sample `40`, hit `0.3`, avg `-0.00619`, median `-0.007491`, mae `0.018754`
- 20d: sample `40`, hit `0.45`, avg `0.001297`, median `-0.001666`, mae `0.033209`
- 60d: sample `40`, hit `0.525`, avg `0.015565`, median `0.00361`, mae `0.056098`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.00557`, median `0.006247`, mae `0.013452`
- 5d: sample `40`, hit `0.6`, avg `0.008563`, median `0.004613`, mae `0.02003`
- 10d: sample `40`, hit `0.625`, avg `0.009917`, median `0.021538`, mae `0.034715`
- 20d: sample `40`, hit `0.825`, avg `0.026294`, median `0.041714`, mae `0.055118`
- 60d: sample `40`, hit `0.6`, avg `0.014492`, median `0.034026`, mae `0.095887`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.001415`, median `0.006714`, mae `0.01713`
- 5d: sample `20`, hit `0.6`, avg `-0.004395`, median `0.002223`, mae `0.017434`
- 10d: sample `20`, hit `0.3`, avg `-0.002636`, median `-0.006017`, mae `0.01912`
- 20d: sample `20`, hit `0.65`, avg `0.019939`, median `0.029166`, mae `0.036275`
- 60d: sample `20`, hit `0.65`, avg `0.033758`, median `0.046132`, mae `0.06997`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.001415`, median `0.006714`, mae `0.01713`
- 5d: sample `20`, hit `0.6`, avg `-0.004395`, median `0.002223`, mae `0.017434`
- 10d: sample `20`, hit `0.3`, avg `-0.002636`, median `-0.006017`, mae `0.01912`
- 20d: sample `20`, hit `0.65`, avg `0.019939`, median `0.029166`, mae `0.036275`
- 60d: sample `20`, hit `0.65`, avg `0.033758`, median `0.046132`, mae `0.06997`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.001415`, median `0.006714`, mae `0.01713`
- 5d: sample `20`, hit `0.6`, avg `-0.004395`, median `0.002223`, mae `0.017434`
- 10d: sample `20`, hit `0.3`, avg `-0.002636`, median `-0.006017`, mae `0.01912`
- 20d: sample `20`, hit `0.65`, avg `0.019939`, median `0.029166`, mae `0.036275`
- 60d: sample `20`, hit `0.65`, avg `0.033758`, median `0.046132`, mae `0.06997`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.001415`, median `0.006714`, mae `0.01713`
- 5d: sample `20`, hit `0.6`, avg `-0.004395`, median `0.002223`, mae `0.017434`
- 10d: sample `20`, hit `0.3`, avg `-0.002636`, median `-0.006017`, mae `0.01912`
- 20d: sample `20`, hit `0.65`, avg `0.019939`, median `0.029166`, mae `0.036275`
- 60d: sample `20`, hit `0.65`, avg `0.033758`, median `0.046132`, mae `0.06997`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.00557`, median `0.006247`, mae `0.013452`
- 5d: sample `40`, hit `0.6`, avg `0.008563`, median `0.004613`, mae `0.02003`
- 10d: sample `40`, hit `0.625`, avg `0.009917`, median `0.021538`, mae `0.034715`
- 20d: sample `40`, hit `0.825`, avg `0.026294`, median `0.041714`, mae `0.055118`
- 60d: sample `40`, hit `0.6`, avg `0.014492`, median `0.034026`, mae `0.095887`

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
- 3d: sample `80`, hit `0.625`, avg `0.00332`, median `0.00234`, mae `0.013891`
- 5d: sample `80`, hit `0.6125`, avg `0.002853`, median `0.002223`, mae `0.016891`
- 10d: sample `80`, hit `0.4625`, avg `0.001863`, median `-0.001222`, mae `0.026735`
- 20d: sample `80`, hit `0.6375`, avg `0.013795`, median `0.020068`, mae `0.044163`
- 60d: sample `80`, hit `0.5625`, avg `0.015028`, median `0.022632`, mae `0.075993`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.001415`, median `0.006714`, mae `0.01713`
- 5d: sample `20`, hit `0.6`, avg `-0.004395`, median `0.002223`, mae `0.017434`
- 10d: sample `20`, hit `0.3`, avg `-0.002636`, median `-0.006017`, mae `0.01912`
- 20d: sample `20`, hit `0.65`, avg `0.019939`, median `0.029166`, mae `0.036275`
- 60d: sample `20`, hit `0.65`, avg `0.033758`, median `0.046132`, mae `0.06997`

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
