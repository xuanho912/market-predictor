# High Confidence Edge Report

Generated at: `2026-07-06T14:50:47.846203+00:00`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.002362`, median `-0.000317`, mae `0.014832`
- 5d: sample `40`, hit `0.45`, avg `-0.003901`, median `-0.002002`, mae `0.016174`
- 10d: sample `40`, hit `0.45`, avg `0.002907`, median `-0.003071`, mae `0.019651`
- 20d: sample `40`, hit `0.65`, avg `0.011435`, median `0.012958`, mae `0.033049`
- 60d: sample `40`, hit `0.625`, avg `0.033219`, median `0.052998`, mae `0.067774`

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.002489`, median `-0.001166`, mae `0.007996`
- 5d: sample `20`, hit `0.7`, avg `0.002442`, median `0.003888`, mae `0.0102`
- 10d: sample `20`, hit `0.55`, avg `0.003657`, median `0.003491`, mae `0.011899`
- 20d: sample `20`, hit `0.7`, avg `0.00558`, median `0.012291`, mae `0.021801`
- 60d: sample `20`, hit `0.2`, avg `-0.038559`, median `-0.03635`, mae `0.052016`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002412`, median `0.006632`, mae `0.015396`
- 5d: sample `20`, hit `0.5`, avg `-0.001068`, median `0.004655`, mae `0.021072`
- 10d: sample `20`, hit `0.55`, avg `0.00019`, median `0.005417`, mae `0.024134`
- 20d: sample `20`, hit `0.75`, avg `-0.004591`, median `0.007366`, mae `0.028809`
- 60d: sample `20`, hit `0.35`, avg `-0.015059`, median `-0.01215`, mae `0.048646`

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
- 3d: sample `8`, hit `0.125`, avg `-0.013768`, median `-0.010033`, mae `0.015446`
- 5d: sample `8`, hit `0.375`, avg `-0.011794`, median `-0.004438`, mae `0.015076`
- 10d: sample `8`, hit `0.0`, avg `-0.01387`, median `-0.010456`, mae `0.01387`
- 20d: sample `8`, hit `0.625`, avg `0.016823`, median `0.029166`, mae `0.040022`
- 60d: sample `8`, hit `0.625`, avg `0.026683`, median `0.046132`, mae `0.079296`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.125`, avg `-0.013768`, median `-0.010033`, mae `0.015446`
- 5d: sample `8`, hit `0.375`, avg `-0.011794`, median `-0.004438`, mae `0.015076`
- 10d: sample `8`, hit `0.0`, avg `-0.01387`, median `-0.010456`, mae `0.01387`
- 20d: sample `8`, hit `0.625`, avg `0.016823`, median `0.029166`, mae `0.040022`
- 60d: sample `8`, hit `0.625`, avg `0.026683`, median `0.046132`, mae `0.079296`

### confidence validation
- `{'strong_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.002362, 'median_return': -0.000317, 'mean_absolute_return': 0.014832, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.003901, 'median_return': -0.002002, 'mean_absolute_return': 0.016174, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.03091}, '10d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': 0.002907, 'median_return': -0.003071, 'mean_absolute_return': 0.019651, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.011435, 'median_return': 0.012958, 'mean_absolute_return': 0.033049, 'max_adverse_excursion': -0.070246, 'max_favorable_excursion': 0.083836}, '60d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.033219, 'median_return': 0.052998, 'mean_absolute_return': 0.067774, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.144029}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.002489, 'median_return': -0.001166, 'mean_absolute_return': 0.007996, 'max_adverse_excursion': -0.029603, 'max_favorable_excursion': 0.011957}, '5d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.002442, 'median_return': 0.003888, 'mean_absolute_return': 0.0102, 'max_adverse_excursion': -0.024669, 'max_favorable_excursion': 0.022174}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.003657, 'median_return': 0.003491, 'mean_absolute_return': 0.011899, 'max_adverse_excursion': -0.017864, 'max_favorable_excursion': 0.021584}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.00558, 'median_return': 0.012291, 'mean_absolute_return': 0.021801, 'max_adverse_excursion': -0.050277, 'max_favorable_excursion': 0.043353}, '60d': {'sample_size': 20, 'hit_rate': 0.2, 'avg_return': -0.038559, 'median_return': -0.03635, 'mean_absolute_return': 0.052016, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.048421}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.013768, 'median_return': -0.010033, 'mean_absolute_return': 0.015446, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.006714}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.011794, 'median_return': -0.004438, 'mean_absolute_return': 0.015076, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.0, 'avg_return': -0.01387, 'median_return': -0.010456, 'mean_absolute_return': 0.01387, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': -0.0004}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.016823, 'median_return': 0.029166, 'mean_absolute_return': 0.040022, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.026683, 'median_return': 0.046132, 'mean_absolute_return': 0.079296, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.000196, 'median_return': 0.001558, 'mean_absolute_return': 0.013022, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': -0.000475, 'median_return': 0.003026, 'mean_absolute_return': 0.015997, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.034374}, '10d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.004225, 'median_return': 0.003262, 'mean_absolute_return': 0.019386, 'max_adverse_excursion': -0.039317, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.004758, 'median_return': 0.010653, 'mean_absolute_return': 0.027972, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.083836}, '60d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': 0.000596, 'median_return': -0.01215, 'mean_absolute_return': 0.056803, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.130806}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.525}, '10d': {'sample_size': 80, 'hit_rate': 0.5}, '20d': {'sample_size': 80, 'hit_rate': 0.6875}, '60d': {'sample_size': 80, 'hit_rate': 0.45}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.05, 'both_hit': 28, 'both_miss': 32}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': 0.0, 'both_hit': 32, 'both_miss': 28}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.025, 'both_hit': 29, 'both_miss': 31}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': 0.125, 'both_hit': 40, 'both_miss': 20}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.075, 'both_hit': 29, 'both_miss': 31}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.004854, 'median_return': 0.004569, 'mean_absolute_return': 0.013677, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.001099, 'median_return': 0.003197, 'mean_absolute_return': 0.015911, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.03091}, '10d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.01129, 'median_return': 0.00903, 'mean_absolute_return': 0.023529, 'max_adverse_excursion': -0.026516, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.003452, 'median_return': 0.004543, 'mean_absolute_return': 0.034338, 'max_adverse_excursion': -0.070246, 'max_favorable_excursion': 0.083836}, '60d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.032187, 'median_return': 0.056189, 'mean_absolute_return': 0.066741, 'max_adverse_excursion': -0.085721, 'max_favorable_excursion': 0.114016}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.003218, 'median_return': -0.001658, 'mean_absolute_return': 0.013126, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': -0.002509, 'median_return': 0.001695, 'mean_absolute_return': 0.015903, 'max_adverse_excursion': -0.042983, 'max_favorable_excursion': 0.034374}, '10d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.000543, 'median_return': -0.001676, 'mean_absolute_return': 0.017269, 'max_adverse_excursion': -0.039317, 'max_favorable_excursion': 0.053454}, '20d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.006803, 'median_return': 0.012291, 'mean_absolute_return': 0.027456, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 60, 'hit_rate': 0.3833, 'avg_return': -0.006456, 'median_return': -0.016009, 'mean_absolute_return': 0.05649, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.144029}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.0012`, median `0.000145`, mae `0.013264`
- 5d: sample `80`, hit `0.525`, avg `-0.001607`, median `0.001695`, mae `0.015905`
- 10d: sample `80`, hit `0.5`, avg `0.002415`, median `0.000242`, mae `0.018834`
- 20d: sample `80`, hit `0.6875`, avg `0.005965`, median `0.010788`, mae `0.029177`
- 60d: sample `80`, hit `0.45`, avg `0.003205`, median `-0.009954`, mae `0.059053`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.0012`, median `0.000145`, mae `0.013264`
- 5d: sample `80`, hit `0.525`, avg `-0.001607`, median `0.001695`, mae `0.015905`
- 10d: sample `80`, hit `0.5`, avg `0.002415`, median `0.000242`, mae `0.018834`
- 20d: sample `80`, hit `0.6875`, avg `0.005965`, median `0.010788`, mae `0.029177`
- 60d: sample `80`, hit `0.45`, avg `0.003205`, median `-0.009954`, mae `0.059053`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5167`, avg `-0.000771`, median `0.000453`, mae `0.01502`
- 5d: sample `60`, hit `0.4667`, avg `-0.002957`, median `-0.002002`, mae `0.017807`
- 10d: sample `60`, hit `0.4833`, avg `0.002001`, median `-0.0004`, mae `0.021145`
- 20d: sample `60`, hit `0.6833`, avg `0.006093`, median `0.009812`, mae `0.031635`
- 60d: sample `60`, hit `0.5333`, avg `0.017126`, median `0.012273`, mae `0.061398`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.0012`, median `0.000145`, mae `0.013264`
- 5d: sample `80`, hit `0.525`, avg `-0.001607`, median `0.001695`, mae `0.015905`
- 10d: sample `80`, hit `0.5`, avg `0.002415`, median `0.000242`, mae `0.018834`
- 20d: sample `80`, hit `0.6875`, avg `0.005965`, median `0.010788`, mae `0.029177`
- 60d: sample `80`, hit `0.45`, avg `0.003205`, median `-0.009954`, mae `0.059053`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.5167`, avg `-0.000771`, median `0.000453`, mae `0.01502`
- 5d: sample `60`, hit `0.4667`, avg `-0.002957`, median `-0.002002`, mae `0.017807`
- 10d: sample `60`, hit `0.4833`, avg `0.002001`, median `-0.0004`, mae `0.021145`
- 20d: sample `60`, hit `0.6833`, avg `0.006093`, median `0.009812`, mae `0.031635`
- 60d: sample `60`, hit `0.5333`, avg `0.017126`, median `0.012273`, mae `0.061398`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.006034`, median `-0.002789`, mae `0.011992`
- 5d: sample `40`, hit `0.525`, avg `-0.00323`, median `0.001695`, mae `0.013318`
- 10d: sample `40`, hit `0.4`, avg `-0.00091`, median `-0.003071`, mae `0.013837`
- 20d: sample `40`, hit `0.725`, avg `0.012499`, median `0.015404`, mae `0.02678`
- 60d: sample `40`, hit `0.4`, avg `-0.002154`, median `-0.018455`, mae `0.060412`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.003633`, median `0.004569`, mae `0.014536`
- 5d: sample `40`, hit `0.525`, avg `1.6e-05`, median `0.003197`, mae `0.018492`
- 10d: sample `40`, hit `0.6`, avg `0.00574`, median `0.005417`, mae `0.023831`
- 20d: sample `40`, hit `0.65`, avg `-0.000569`, median `0.004543`, mae `0.031574`
- 60d: sample `40`, hit `0.5`, avg `0.008564`, median `0.003923`, mae `0.057693`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.006034`, median `-0.002789`, mae `0.011992`
- 5d: sample `40`, hit `0.525`, avg `-0.00323`, median `0.001695`, mae `0.013318`
- 10d: sample `40`, hit `0.4`, avg `-0.00091`, median `-0.003071`, mae `0.013837`
- 20d: sample `40`, hit `0.725`, avg `0.012499`, median `0.015404`, mae `0.02678`
- 60d: sample `40`, hit `0.4`, avg `-0.002154`, median `-0.018455`, mae `0.060412`

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
