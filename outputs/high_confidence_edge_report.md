# High Confidence Edge Report

Generated at: `2026-07-06T15:57:37.405490+00:00`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.009582`, median `-0.010033`, mae `0.015983`
- 5d: sample `20`, hit `0.35`, avg `-0.008741`, median `-0.004989`, mae `0.016597`
- 10d: sample `20`, hit `0.25`, avg `-0.005755`, median `-0.007011`, mae `0.015495`
- 20d: sample `20`, hit `0.7`, avg `0.016416`, median `0.021759`, mae `0.028922`
- 60d: sample `20`, hit `0.6`, avg `0.027865`, median `0.029831`, mae `0.062422`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.000532`, median `0.001999`, mae `0.009904`
- 5d: sample `40`, hit `0.575`, avg `0.000686`, median `0.003197`, mae `0.01251`
- 10d: sample `40`, hit `0.6`, avg `0.005593`, median `0.003491`, mae `0.016529`
- 20d: sample `40`, hit `0.625`, avg `0.003691`, median `0.010653`, mae `0.026007`
- 60d: sample `40`, hit `0.425`, avg `-0.004385`, median `-0.018455`, mae `0.05719`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002649`, median `0.006632`, mae `0.015159`
- 5d: sample `20`, hit `0.5`, avg `-0.000869`, median `0.004655`, mae `0.020874`
- 10d: sample `20`, hit `0.5`, avg `-0.001198`, median `0.003262`, mae `0.024157`
- 20d: sample `20`, hit `0.75`, avg `-0.004071`, median `0.007676`, mae `0.029329`
- 60d: sample `20`, hit `0.4`, avg `-0.012884`, median `-0.009954`, mae `0.04947`

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
- `{'strong_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.009582, 'median_return': -0.010033, 'mean_absolute_return': 0.015983, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.008741, 'median_return': -0.004989, 'mean_absolute_return': 0.016597, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 20, 'hit_rate': 0.25, 'avg_return': -0.005755, 'median_return': -0.007011, 'mean_absolute_return': 0.015495, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.016416, 'median_return': 0.021759, 'mean_absolute_return': 0.028922, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.027865, 'median_return': 0.029831, 'mean_absolute_return': 0.062422, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.144029}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.000532, 'median_return': 0.001999, 'mean_absolute_return': 0.009904, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.025242}, '5d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.000686, 'median_return': 0.003197, 'mean_absolute_return': 0.01251, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.028217}, '10d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.005593, 'median_return': 0.003491, 'mean_absolute_return': 0.016529, 'max_adverse_excursion': -0.026516, 'max_favorable_excursion': 0.056454}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.003691, 'median_return': 0.010653, 'mean_absolute_return': 0.026007, 'max_adverse_excursion': -0.070246, 'max_favorable_excursion': 0.083836}, '60d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.004385, 'median_return': -0.018455, 'mean_absolute_return': 0.05719, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.105138}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.013768, 'median_return': -0.010033, 'mean_absolute_return': 0.015446, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.006714}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.011794, 'median_return': -0.004438, 'mean_absolute_return': 0.015076, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.0, 'avg_return': -0.01387, 'median_return': -0.010456, 'mean_absolute_return': 0.01387, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': -0.0004}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.016823, 'median_return': 0.029166, 'mean_absolute_return': 0.040022, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.026683, 'median_return': 0.046132, 'mean_absolute_return': 0.079296, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': -0.000101, 'median_return': 0.001558, 'mean_absolute_return': 0.012437, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': -0.000978, 'median_return': 0.002694, 'mean_absolute_return': 0.015684, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.034374}, '10d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.002717, 'median_return': 0.002896, 'mean_absolute_return': 0.018656, 'max_adverse_excursion': -0.039317, 'max_favorable_excursion': 0.056454}, '20d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.00361, 'median_return': 0.010653, 'mean_absolute_return': 0.026182, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.083836}, '60d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.00124, 'median_return': -0.009954, 'mean_absolute_return': 0.054043, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.124768}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.5}, '10d': {'sample_size': 80, 'hit_rate': 0.4875}, '20d': {'sample_size': 80, 'hit_rate': 0.675}, '60d': {'sample_size': 80, 'hit_rate': 0.4625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.075, 'both_hit': 17, 'both_miss': 23}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 20, 'both_miss': 20}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.05, 'both_hit': 17, 'both_miss': 23}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': 0.125, 'both_hit': 29, 'both_miss': 11}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.0, 'both_hit': 17, 'both_miss': 23}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5, 'avg_return': -0.001467, 'median_return': 0.000145, 'mean_absolute_return': 0.012738, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 80, 'hit_rate': 0.5, 'avg_return': -0.00206, 'median_return': 0.000415, 'mean_absolute_return': 0.015623, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.034374}, '10d': {'sample_size': 80, 'hit_rate': 0.4875, 'avg_return': 0.001058, 'median_return': -0.000214, 'mean_absolute_return': 0.018177, 'max_adverse_excursion': -0.039317, 'max_favorable_excursion': 0.056454}, '20d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.004932, 'median_return': 0.010788, 'mean_absolute_return': 0.027566, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.083836}, '60d': {'sample_size': 80, 'hit_rate': 0.4625, 'avg_return': 0.001553, 'median_return': -0.005523, 'mean_absolute_return': 0.056568, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.144029}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.001467`, median `0.000145`, mae `0.012738`
- 5d: sample `80`, hit `0.5`, avg `-0.00206`, median `0.000415`, mae `0.015623`
- 10d: sample `80`, hit `0.4875`, avg `0.001058`, median `-0.000214`, mae `0.018177`
- 20d: sample `80`, hit `0.675`, avg `0.004932`, median `0.010788`, mae `0.027566`
- 60d: sample `80`, hit `0.4625`, avg `0.001553`, median `-0.005523`, mae `0.056568`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.001467`, median `0.000145`, mae `0.012738`
- 5d: sample `80`, hit `0.5`, avg `-0.00206`, median `0.000415`, mae `0.015623`
- 10d: sample `80`, hit `0.4875`, avg `0.001058`, median `-0.000214`, mae `0.018177`
- 20d: sample `80`, hit `0.675`, avg `0.004932`, median `0.010788`, mae `0.027566`
- 60d: sample `80`, hit `0.4625`, avg `0.001553`, median `-0.005523`, mae `0.056568`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.003467`, median `-0.001658`, mae `0.015571`
- 5d: sample `40`, hit `0.425`, avg `-0.004805`, median `-0.004989`, mae `0.018736`
- 10d: sample `40`, hit `0.375`, avg `-0.003476`, median `-0.007011`, mae `0.019826`
- 20d: sample `40`, hit `0.725`, avg `0.006172`, median `0.012958`, mae `0.029126`
- 60d: sample `40`, hit `0.5`, avg `0.00749`, median `0.003095`, mae `0.055946`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.001467`, median `0.000145`, mae `0.012738`
- 5d: sample `80`, hit `0.5`, avg `-0.00206`, median `0.000415`, mae `0.015623`
- 10d: sample `80`, hit `0.4875`, avg `0.001058`, median `-0.000214`, mae `0.018177`
- 20d: sample `80`, hit `0.675`, avg `0.004932`, median `0.010788`, mae `0.027566`
- 60d: sample `80`, hit `0.4625`, avg `0.001553`, median `-0.005523`, mae `0.056568`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.003467`, median `-0.001658`, mae `0.015571`
- 5d: sample `40`, hit `0.425`, avg `-0.004805`, median `-0.004989`, mae `0.018736`
- 10d: sample `40`, hit `0.375`, avg `-0.003476`, median `-0.007011`, mae `0.019826`
- 20d: sample `40`, hit `0.725`, avg `0.006172`, median `0.012958`, mae `0.029126`
- 60d: sample `40`, hit `0.5`, avg `0.00749`, median `0.003095`, mae `0.055946`

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
- 3d: sample `40`, hit `0.425`, avg `-0.005373`, median `-0.002654`, mae `0.012218`
- 5d: sample `40`, hit `0.5`, avg `-0.003299`, median `0.000415`, mae `0.013463`
- 10d: sample `40`, hit `0.425`, avg `-0.000673`, median `-0.001676`, mae `0.013548`
- 20d: sample `40`, hit `0.725`, avg `0.012644`, median `0.015404`, mae `0.024897`
- 60d: sample `40`, hit `0.425`, avg `-0.003156`, median `-0.01711`, mae `0.057341`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.002439`, median `0.003538`, mae `0.013257`
- 5d: sample `40`, hit `0.5`, avg `-0.00082`, median `0.00127`, mae `0.017783`
- 10d: sample `40`, hit `0.55`, avg `0.002789`, median `0.002896`, mae `0.022807`
- 20d: sample `40`, hit `0.625`, avg `-0.002781`, median `0.004543`, mae `0.030236`
- 60d: sample `40`, hit `0.5`, avg `0.006261`, median `0.003923`, mae `0.055795`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.005373`, median `-0.002654`, mae `0.012218`
- 5d: sample `40`, hit `0.5`, avg `-0.003299`, median `0.000415`, mae `0.013463`
- 10d: sample `40`, hit `0.425`, avg `-0.000673`, median `-0.001676`, mae `0.013548`
- 20d: sample `40`, hit `0.725`, avg `0.012644`, median `0.015404`, mae `0.024897`
- 60d: sample `40`, hit `0.425`, avg `-0.003156`, median `-0.01711`, mae `0.057341`

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
