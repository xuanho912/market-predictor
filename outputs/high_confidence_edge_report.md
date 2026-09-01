# High Confidence Edge Report

Generated at: `2026-09-01T01:49:07.323088+00:00`

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
- 3d: sample `60`, hit `0.4833`, avg `-0.001585`, median `-0.001428`, mae `0.014701`
- 5d: sample `60`, hit `0.5`, avg `-0.003092`, median `0.000208`, mae `0.018239`
- 10d: sample `60`, hit `0.4`, avg `-0.000231`, median `-0.007117`, mae `0.024761`
- 20d: sample `60`, hit `0.6667`, avg `0.01101`, median `0.020068`, mae `0.034764`
- 60d: sample `60`, hit `0.7`, avg `0.041623`, median `0.059495`, mae `0.07074`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.000438`, median `0.00979`, mae `0.020832`
- 5d: sample `20`, hit `0.6`, avg `0.002755`, median `0.00175`, mae `0.018657`
- 10d: sample `20`, hit `0.4`, avg `-0.00661`, median `-0.00659`, mae `0.022897`
- 20d: sample `20`, hit `0.55`, avg `0.000474`, median `0.007572`, mae `0.037129`
- 60d: sample `20`, hit `0.6`, avg `-0.010302`, median `0.008034`, mae `0.05055`

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
- 3d: sample `8`, hit `0.375`, avg `-0.008046`, median `-0.001811`, mae `0.011927`
- 5d: sample `8`, hit `0.25`, avg `-0.008834`, median `-0.012956`, mae `0.014934`
- 10d: sample `8`, hit `0.625`, avg `0.005749`, median `0.019233`, mae `0.019896`
- 20d: sample `8`, hit `0.75`, avg `0.010618`, median `0.029166`, mae `0.030759`
- 60d: sample `8`, hit `0.625`, avg `0.023768`, median `0.046132`, mae `0.067466`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.008046`, median `-0.001811`, mae `0.011927`
- 5d: sample `8`, hit `0.25`, avg `-0.008834`, median `-0.012956`, mae `0.014934`
- 10d: sample `8`, hit `0.625`, avg `0.005749`, median `0.019233`, mae `0.019896`
- 20d: sample `8`, hit `0.75`, avg `0.010618`, median `0.029166`, mae `0.030759`
- 60d: sample `8`, hit `0.625`, avg `0.023768`, median `0.046132`, mae `0.067466`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': -0.001585, 'median_return': -0.001428, 'mean_absolute_return': 0.014701, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': -0.003092, 'median_return': 0.000208, 'mean_absolute_return': 0.018239, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 60, 'hit_rate': 0.4, 'avg_return': -0.000231, 'median_return': -0.007117, 'mean_absolute_return': 0.024761, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.01101, 'median_return': 0.020068, 'mean_absolute_return': 0.034764, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.041623, 'median_return': 0.059495, 'mean_absolute_return': 0.07074, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.19145}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.008046, 'median_return': -0.001811, 'mean_absolute_return': 0.011927, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.01018}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.008834, 'median_return': -0.012956, 'mean_absolute_return': 0.014934, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.005749, 'median_return': 0.019233, 'mean_absolute_return': 0.019896, 'max_adverse_excursion': -0.023505, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.010618, 'median_return': 0.029166, 'mean_absolute_return': 0.030759, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.033999}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.023768, 'median_return': 0.046132, 'mean_absolute_return': 0.067466, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.101282}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': -0.000548, 'median_return': 0.000766, 'mean_absolute_return': 0.016712, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': -0.00083, 'median_return': 0.001239, 'mean_absolute_return': 0.018722, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 72, 'hit_rate': 0.375, 'avg_return': -0.002667, 'median_return': -0.007491, 'mean_absolute_return': 0.024784, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.008127, 'median_return': 0.014522, 'mean_absolute_return': 0.035866, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.029183, 'median_return': 0.031643, 'mean_absolute_return': 0.065496, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.475}, '5d': {'sample_size': 80, 'hit_rate': 0.475}, '10d': {'sample_size': 80, 'hit_rate': 0.45}, '20d': {'sample_size': 80, 'hit_rate': 0.6125}, '60d': {'sample_size': 80, 'hit_rate': 0.625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_minus_secondary': 0.225, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.375, 'primary_minus_secondary': 0.25, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5, 'avg_return': -0.001298, 'median_return': 0.000603, 'mean_absolute_return': 0.016233, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 80, 'hit_rate': 0.525, 'avg_return': -0.00163, 'median_return': 0.000548, 'mean_absolute_return': 0.018343, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 80, 'hit_rate': 0.4, 'avg_return': -0.001826, 'median_return': -0.007117, 'mean_absolute_return': 0.024295, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.008376, 'median_return': 0.015261, 'mean_absolute_return': 0.035355, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.028642, 'median_return': 0.031643, 'mean_absolute_return': 0.065693, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.002536`, median `-0.001641`, mae `0.007882`
- 5d: sample `20`, hit `0.55`, avg `-0.003361`, median `0.000873`, mae `0.009802`
- 10d: sample `20`, hit `0.3`, avg `-0.00764`, median `-0.01051`, mae `0.019841`
- 20d: sample `20`, hit `0.5`, avg `-0.008973`, median `0.006421`, mae `0.032741`
- 60d: sample `20`, hit `0.55`, avg `0.015897`, median `0.032982`, mae `0.058094`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001109`, median `0.002329`, mae `0.01811`
- 5d: sample `40`, hit `0.475`, avg `-0.002958`, median `-0.004367`, mae `0.022457`
- 10d: sample `40`, hit `0.45`, avg `0.003474`, median `-0.001932`, mae `0.02722`
- 20d: sample `40`, hit `0.75`, avg `0.021001`, median `0.026531`, mae `0.035775`
- 60d: sample `40`, hit `0.775`, avg `0.054487`, median `0.065295`, mae `0.077063`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.002536`, median `-0.001641`, mae `0.007882`
- 5d: sample `20`, hit `0.55`, avg `-0.003361`, median `0.000873`, mae `0.009802`
- 10d: sample `20`, hit `0.3`, avg `-0.00764`, median `-0.01051`, mae `0.019841`
- 20d: sample `20`, hit `0.5`, avg `-0.008973`, median `0.006421`, mae `0.032741`
- 60d: sample `20`, hit `0.55`, avg `0.015897`, median `0.032982`, mae `0.058094`

### breadth_conflicted_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001109`, median `0.002329`, mae `0.01811`
- 5d: sample `40`, hit `0.475`, avg `-0.002958`, median `-0.004367`, mae `0.022457`
- 10d: sample `40`, hit `0.45`, avg `0.003474`, median `-0.001932`, mae `0.02722`
- 20d: sample `40`, hit `0.75`, avg `0.021001`, median `0.026531`, mae `0.035775`
- 60d: sample `40`, hit `0.775`, avg `0.054487`, median `0.065295`, mae `0.077063`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.005118`, median `-0.001811`, mae `0.013752`
- 5d: sample `20`, hit `0.4`, avg `-0.009827`, median `-0.007788`, mae `0.015666`
- 10d: sample `20`, hit `0.35`, avg `-0.00125`, median `-0.006017`, mae `0.018148`
- 20d: sample `20`, hit `0.75`, avg `0.015702`, median `0.029166`, mae `0.033743`
- 60d: sample `20`, hit `0.7`, avg `0.038952`, median `0.065295`, mae `0.074889`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.002536`, median `-0.001641`, mae `0.007882`
- 5d: sample `20`, hit `0.55`, avg `-0.003361`, median `0.000873`, mae `0.009802`
- 10d: sample `20`, hit `0.3`, avg `-0.00764`, median `-0.01051`, mae `0.019841`
- 20d: sample `20`, hit `0.5`, avg `-0.008973`, median `0.006421`, mae `0.032741`
- 60d: sample `20`, hit `0.55`, avg `0.015897`, median `0.032982`, mae `0.058094`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001109`, median `0.002329`, mae `0.01811`
- 5d: sample `40`, hit `0.475`, avg `-0.002958`, median `-0.004367`, mae `0.022457`
- 10d: sample `40`, hit `0.45`, avg `0.003474`, median `-0.001932`, mae `0.02722`
- 20d: sample `40`, hit `0.75`, avg `0.021001`, median `0.026531`, mae `0.035775`
- 60d: sample `40`, hit `0.775`, avg `0.054487`, median `0.065295`, mae `0.077063`

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
- 3d: sample `80`, hit `0.5`, avg `-0.001298`, median `0.000603`, mae `0.016233`
- 5d: sample `80`, hit `0.525`, avg `-0.00163`, median `0.000548`, mae `0.018343`
- 10d: sample `80`, hit `0.4`, avg `-0.001826`, median `-0.007117`, mae `0.024295`
- 20d: sample `80`, hit `0.6375`, avg `0.008376`, median `0.015261`, mae `0.035355`
- 60d: sample `80`, hit `0.675`, avg `0.028642`, median `0.031643`, mae `0.065693`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.4833`, avg `-0.001585`, median `-0.001428`, mae `0.014701`
- 5d: sample `60`, hit `0.5`, avg `-0.003092`, median `0.000208`, mae `0.018239`
- 10d: sample `60`, hit `0.4`, avg `-0.000231`, median `-0.007117`, mae `0.024761`
- 20d: sample `60`, hit `0.6667`, avg `0.01101`, median `0.020068`, mae `0.034764`
- 60d: sample `60`, hit `0.7`, avg `0.041623`, median `0.059495`, mae `0.07074`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `-0.000885`, median `0.00234`, mae `0.019017`
- 5d: sample `60`, hit `0.5167`, avg `-0.001053`, median `0.000415`, mae `0.021191`
- 10d: sample `60`, hit `0.4333`, avg `0.000113`, median `-0.006017`, mae `0.025779`
- 20d: sample `60`, hit `0.6833`, avg `0.014159`, median `0.019547`, mae `0.036226`
- 60d: sample `60`, hit `0.7167`, avg `0.03289`, median `0.031643`, mae `0.068225`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001109`, median `0.002329`, mae `0.01811`
- 5d: sample `40`, hit `0.475`, avg `-0.002958`, median `-0.004367`, mae `0.022457`
- 10d: sample `40`, hit `0.45`, avg `0.003474`, median `-0.001932`, mae `0.02722`
- 20d: sample `40`, hit `0.75`, avg `0.021001`, median `0.026531`, mae `0.035775`
- 60d: sample `40`, hit `0.775`, avg `0.054487`, median `0.065295`, mae `0.077063`

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
