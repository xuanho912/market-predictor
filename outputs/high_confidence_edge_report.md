# High Confidence Edge Report

Generated at: `2026-08-27T14:48:27.840546+00:00`

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
- 3d: sample `80`, hit `0.5375`, avg `-0.000408`, median `0.002067`, mae `0.016155`
- 5d: sample `80`, hit `0.5375`, avg `-0.000913`, median `0.000873`, mae `0.018994`
- 10d: sample `80`, hit `0.4375`, avg `0.000942`, median `-0.007011`, mae `0.026106`
- 20d: sample `80`, hit `0.65`, avg `0.006942`, median `0.016175`, mae `0.034759`
- 60d: sample `80`, hit `0.675`, avg `0.02934`, median `0.032524`, mae `0.063389`

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
- 3d: sample `8`, hit `0.5`, avg `-0.006581`, median `0.001558`, mae `0.011047`
- 5d: sample `8`, hit `0.375`, avg `-0.0078`, median `-0.012956`, mae `0.014858`
- 10d: sample `8`, hit `0.625`, avg `0.005104`, median `0.019233`, mae `0.020541`
- 20d: sample `8`, hit `0.875`, avg `0.014801`, median `0.029166`, mae `0.02663`
- 60d: sample `8`, hit `0.75`, avg `0.038143`, median `0.059495`, mae `0.067965`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.006581`, median `0.001558`, mae `0.011047`
- 5d: sample `8`, hit `0.375`, avg `-0.0078`, median `-0.012956`, mae `0.014858`
- 10d: sample `8`, hit `0.625`, avg `0.005104`, median `0.019233`, mae `0.020541`
- 20d: sample `8`, hit `0.875`, avg `0.014801`, median `0.029166`, mae `0.02663`
- 60d: sample `8`, hit `0.75`, avg `0.038143`, median `0.059495`, mae `0.067965`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5375, 'avg_return': -0.000408, 'median_return': 0.002067, 'mean_absolute_return': 0.016155, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 80, 'hit_rate': 0.5375, 'avg_return': -0.000913, 'median_return': 0.000873, 'mean_absolute_return': 0.018994, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 80, 'hit_rate': 0.4375, 'avg_return': 0.000942, 'median_return': -0.007011, 'mean_absolute_return': 0.026106, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.006942, 'median_return': 0.016175, 'mean_absolute_return': 0.034759, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.02934, 'median_return': 0.032524, 'mean_absolute_return': 0.063389, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.006581, 'median_return': 0.001558, 'mean_absolute_return': 0.011047, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.01018}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.0078, 'median_return': -0.012956, 'mean_absolute_return': 0.014858, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.005104, 'median_return': 0.019233, 'mean_absolute_return': 0.020541, 'max_adverse_excursion': -0.023505, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.014801, 'median_return': 0.029166, 'mean_absolute_return': 0.02663, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.033999}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.038143, 'median_return': 0.059495, 'mean_absolute_return': 0.067965, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.101282}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.000278, 'median_return': 0.002329, 'mean_absolute_return': 0.016723, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': -0.000148, 'median_return': 0.001303, 'mean_absolute_return': 0.019454, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': 0.00048, 'median_return': -0.007117, 'mean_absolute_return': 0.026724, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.006069, 'median_return': 0.013877, 'mean_absolute_return': 0.035662, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.028362, 'median_return': 0.028986, 'mean_absolute_return': 0.062881, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5375}, '5d': {'sample_size': 80, 'hit_rate': 0.5375}, '10d': {'sample_size': 80, 'hit_rate': 0.4375}, '20d': {'sample_size': 80, 'hit_rate': 0.65}, '60d': {'sample_size': 80, 'hit_rate': 0.675}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.025, 'both_hit': 24, 'both_miss': 16}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': 0.025, 'both_hit': 22, 'both_miss': 18}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.15, 'both_hit': 21, 'both_miss': 19}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': 0.075, 'both_hit': 29, 'both_miss': 11}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': 0.075, 'both_hit': 31, 'both_miss': 9}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.000967, 'median_return': 0.002067, 'mean_absolute_return': 0.014916, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': -0.000684, 'median_return': 0.000873, 'mean_absolute_return': 0.01848, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': 0.002977, 'median_return': -0.00676, 'mean_absolute_return': 0.025796, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.009042, 'median_return': 0.018139, 'mean_absolute_return': 0.034939, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.043066, 'median_return': 0.057625, 'mean_absolute_return': 0.067518, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.004534, 'median_return': 0.003026, 'mean_absolute_return': 0.019874, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.026658}, '5d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.001599, 'median_return': 0.001239, 'mean_absolute_return': 0.020537, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.043092}, '10d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.005161, 'median_return': -0.010791, 'mean_absolute_return': 0.027037, 'max_adverse_excursion': -0.057499, 'max_favorable_excursion': 0.04908}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.000641, 'median_return': 0.013877, 'mean_absolute_return': 0.034217, 'max_adverse_excursion': -0.090764, 'max_favorable_excursion': 0.057038}, '60d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.011838, 'median_return': 0.002897, 'mean_absolute_return': 0.051003, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.107547}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.000967`, median `0.002067`, mae `0.014916`
- 5d: sample `60`, hit `0.55`, avg `-0.000684`, median `0.000873`, mae `0.01848`
- 10d: sample `60`, hit `0.45`, avg `0.002977`, median `-0.00676`, mae `0.025796`
- 20d: sample `60`, hit `0.6667`, avg `0.009042`, median `0.018139`, mae `0.034939`
- 60d: sample `60`, hit `0.7333`, avg `0.043066`, median `0.057625`, mae `0.067518`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.000967`, median `0.002067`, mae `0.014916`
- 5d: sample `60`, hit `0.55`, avg `-0.000684`, median `0.000873`, mae `0.01848`
- 10d: sample `60`, hit `0.45`, avg `0.002977`, median `-0.00676`, mae `0.025796`
- 20d: sample `60`, hit `0.6667`, avg `0.009042`, median `0.018139`, mae `0.034939`
- 60d: sample `60`, hit `0.7333`, avg `0.043066`, median `0.057625`, mae `0.067518`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.000985`, median `0.00234`, mae `0.013767`
- 5d: sample `20`, hit `0.5`, avg `-0.003692`, median `0.000208`, mae `0.015159`
- 10d: sample `20`, hit `0.45`, avg `0.004048`, median `-0.001222`, mae `0.020463`
- 20d: sample `20`, hit `0.75`, avg `0.014573`, median `0.026531`, mae `0.032149`
- 60d: sample `20`, hit `0.65`, avg `0.031153`, median `0.059495`, mae `0.068423`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.5375`, avg `-0.000408`, median `0.002067`, mae `0.016155`
- 5d: sample `80`, hit `0.5375`, avg `-0.000913`, median `0.000873`, mae `0.018994`
- 10d: sample `80`, hit `0.4375`, avg `0.000942`, median `-0.007011`, mae `0.026106`
- 20d: sample `80`, hit `0.65`, avg `0.006942`, median `0.016175`, mae `0.034759`
- 60d: sample `80`, hit `0.675`, avg `0.02934`, median `0.032524`, mae `0.063389`

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
- 3d: sample `80`, hit `0.5375`, avg `-0.000408`, median `0.002067`, mae `0.016155`
- 5d: sample `80`, hit `0.5375`, avg `-0.000913`, median `0.000873`, mae `0.018994`
- 10d: sample `80`, hit `0.4375`, avg `0.000942`, median `-0.007011`, mae `0.026106`
- 20d: sample `80`, hit `0.65`, avg `0.006942`, median `0.016175`, mae `0.034759`
- 60d: sample `80`, hit `0.675`, avg `0.02934`, median `0.032524`, mae `0.063389`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `80`
- 3d: sample `80`, hit `0.5375`, avg `-0.000408`, median `0.002067`, mae `0.016155`
- 5d: sample `80`, hit `0.5375`, avg `-0.000913`, median `0.000873`, mae `0.018994`
- 10d: sample `80`, hit `0.4375`, avg `0.000942`, median `-0.007011`, mae `0.026106`
- 20d: sample `80`, hit `0.65`, avg `0.006942`, median `0.016175`, mae `0.034759`
- 60d: sample `80`, hit `0.675`, avg `0.02934`, median `0.032524`, mae `0.063389`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5375`, avg `-0.000408`, median `0.002067`, mae `0.016155`
- 5d: sample `80`, hit `0.5375`, avg `-0.000913`, median `0.000873`, mae `0.018994`
- 10d: sample `80`, hit `0.4375`, avg `0.000942`, median `-0.007011`, mae `0.026106`
- 20d: sample `80`, hit `0.65`, avg `0.006942`, median `0.016175`, mae `0.034759`
- 60d: sample `80`, hit `0.675`, avg `0.02934`, median `0.032524`, mae `0.063389`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.5375`, avg `-0.000408`, median `0.002067`, mae `0.016155`
- 5d: sample `80`, hit `0.5375`, avg `-0.000913`, median `0.000873`, mae `0.018994`
- 10d: sample `80`, hit `0.4375`, avg `0.000942`, median `-0.007011`, mae `0.026106`
- 20d: sample `80`, hit `0.65`, avg `0.006942`, median `0.016175`, mae `0.034759`
- 60d: sample `80`, hit `0.675`, avg `0.02934`, median `0.032524`, mae `0.063389`

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
