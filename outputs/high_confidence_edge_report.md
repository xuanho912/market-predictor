# High Confidence Edge Report

Generated at: `2026-09-02T01:01:10.654110+00:00`

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
- 3d: sample `60`, hit `0.55`, avg `4.4e-05`, median `0.000766`, mae `0.013512`
- 5d: sample `60`, hit `0.5667`, avg `-0.001768`, median `0.001303`, mae `0.015686`
- 10d: sample `60`, hit `0.3667`, avg `-0.004097`, median `-0.008511`, mae `0.020884`
- 20d: sample `60`, hit `0.5833`, avg `0.009605`, median `0.012958`, mae `0.034433`
- 60d: sample `60`, hit `0.7`, avg `0.033506`, median `0.057625`, mae `0.068248`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.004061`, median `0.008223`, mae `0.020008`
- 5d: sample `20`, hit `0.55`, avg `0.004862`, median `0.007909`, mae `0.023166`
- 10d: sample `20`, hit `0.5`, avg `0.007121`, median `0.001455`, mae `0.027657`
- 20d: sample `20`, hit `0.7`, avg `0.023026`, median `0.023289`, mae `0.027868`
- 60d: sample `20`, hit `0.95`, avg `0.074922`, median `0.064905`, mae `0.078424`

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
- 3d: sample `8`, hit `0.5`, avg `-0.004172`, median `0.001558`, mae `0.010449`
- 5d: sample `8`, hit `0.25`, avg `-0.012244`, median `-0.013034`, mae `0.015987`
- 10d: sample `8`, hit `0.625`, avg `0.007921`, median `0.019233`, mae `0.018985`
- 20d: sample `8`, hit `1.0`, avg `0.033913`, median `0.031658`, mae `0.033913`
- 60d: sample `8`, hit `1.0`, avg `0.086159`, median `0.095045`, mae `0.086159`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.004172`, median `0.001558`, mae `0.010449`
- 5d: sample `8`, hit `0.25`, avg `-0.012244`, median `-0.013034`, mae `0.015987`
- 10d: sample `8`, hit `0.625`, avg `0.007921`, median `0.019233`, mae `0.018985`
- 20d: sample `8`, hit `1.0`, avg `0.033913`, median `0.031658`, mae `0.033913`
- 60d: sample `8`, hit `1.0`, avg `0.086159`, median `0.095045`, mae `0.086159`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 4.4e-05, 'median_return': 0.000766, 'mean_absolute_return': 0.013512, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.035961}, '5d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': -0.001768, 'median_return': 0.001303, 'mean_absolute_return': 0.015686, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.035465}, '10d': {'sample_size': 60, 'hit_rate': 0.3667, 'avg_return': -0.004097, 'median_return': -0.008511, 'mean_absolute_return': 0.020884, 'max_adverse_excursion': -0.057499, 'max_favorable_excursion': 0.059577}, '20d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.009605, 'median_return': 0.012958, 'mean_absolute_return': 0.034433, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.033506, 'median_return': 0.057625, 'mean_absolute_return': 0.068248, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.004172, 'median_return': 0.001558, 'mean_absolute_return': 0.010449, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.017427}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.012244, 'median_return': -0.013034, 'mean_absolute_return': 0.015987, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.011143}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.007921, 'median_return': 0.019233, 'mean_absolute_return': 0.018985, 'max_adverse_excursion': -0.020281, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.033913, 'median_return': 0.031658, 'mean_absolute_return': 0.033913, 'max_adverse_excursion': 0.000213, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.086159, 'median_return': 0.095045, 'mean_absolute_return': 0.086159, 'max_adverse_excursion': 0.029831, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.001628, 'median_return': 0.00099, 'mean_absolute_return': 0.015657, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.001238, 'median_return': 0.0019, 'mean_absolute_return': 0.01773, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 72, 'hit_rate': 0.375, 'avg_return': -0.002316, 'median_return': -0.008511, 'mean_absolute_return': 0.022976, 'max_adverse_excursion': -0.057499, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.010632, 'median_return': 0.011528, 'mean_absolute_return': 0.032667, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.03916, 'median_return': 0.054272, 'mean_absolute_return': 0.069085, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.55}, '5d': {'sample_size': 80, 'hit_rate': 0.5625}, '10d': {'sample_size': 80, 'hit_rate': 0.4}, '20d': {'sample_size': 80, 'hit_rate': 0.6125}, '60d': {'sample_size': 80, 'hit_rate': 0.7625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.4, 'primary_minus_secondary': 0.15, 'both_hit': 8, 'both_miss': 12}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.3875, 'primary_minus_secondary': 0.175, 'both_hit': 8, 'both_miss': 12}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': -0.1, 'both_hit': 6, 'both_miss': 14}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.15, 'both_hit': 13, 'both_miss': 7}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.7625, 'secondary_hit_rate': 0.3375, 'primary_minus_secondary': 0.425, 'both_hit': 14, 'both_miss': 6}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.55, 'avg_return': 0.001048, 'median_return': 0.00099, 'mean_absolute_return': 0.015136, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': -0.00011, 'median_return': 0.001695, 'mean_absolute_return': 0.017556, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 80, 'hit_rate': 0.4, 'avg_return': -0.001293, 'median_return': -0.007491, 'mean_absolute_return': 0.022577, 'max_adverse_excursion': -0.057499, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.01296, 'median_return': 0.014522, 'mean_absolute_return': 0.032792, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 80, 'hit_rate': 0.7625, 'avg_return': 0.04386, 'median_return': 0.059495, 'mean_absolute_return': 0.070792, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.003028`, median `-0.001658`, mae `0.012387`
- 5d: sample `40`, hit `0.475`, avg `-0.008062`, median `-0.00244`, mae `0.014748`
- 10d: sample `40`, hit `0.375`, avg `-0.003768`, median `-0.007117`, mae `0.018309`
- 20d: sample `40`, hit `0.625`, avg `0.010519`, median `0.02086`, mae `0.033209`
- 60d: sample `40`, hit `0.675`, avg `0.038885`, median `0.061042`, mae `0.06884`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.000925`, median `-0.001658`, mae `0.017819`
- 5d: sample `40`, hit `0.475`, avg `-0.003528`, median `-0.004438`, mae `0.020628`
- 10d: sample `40`, hit `0.4`, avg `0.00157`, median `-0.005891`, mae `0.022726`
- 20d: sample `40`, hit `0.675`, avg `0.020198`, median `0.025442`, mae `0.029605`
- 60d: sample `40`, hit `0.825`, avg `0.060041`, median `0.064905`, mae `0.076969`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.003028`, median `-0.001658`, mae `0.012387`
- 5d: sample `40`, hit `0.475`, avg `-0.008062`, median `-0.00244`, mae `0.014748`
- 10d: sample `40`, hit `0.375`, avg `-0.003768`, median `-0.007117`, mae `0.018309`
- 20d: sample `40`, hit `0.625`, avg `0.010519`, median `0.02086`, mae `0.033209`
- 60d: sample `40`, hit `0.675`, avg `0.038885`, median `0.061042`, mae `0.06884`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.005912`, median `-0.001811`, mae `0.015629`
- 5d: sample `20`, hit `0.4`, avg `-0.011919`, median `-0.012956`, mae `0.01809`
- 10d: sample `20`, hit `0.3`, avg `-0.003982`, median `-0.006017`, mae `0.017795`
- 20d: sample `20`, hit `0.65`, avg `0.01737`, median `0.030297`, mae `0.031343`
- 60d: sample `20`, hit `0.7`, avg `0.045159`, median `0.067551`, mae `0.075515`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.003028`, median `-0.001658`, mae `0.012387`
- 5d: sample `40`, hit `0.475`, avg `-0.008062`, median `-0.00244`, mae `0.014748`
- 10d: sample `40`, hit `0.375`, avg `-0.003768`, median `-0.007117`, mae `0.018309`
- 20d: sample `40`, hit `0.625`, avg `0.010519`, median `0.02086`, mae `0.033209`
- 60d: sample `40`, hit `0.675`, avg `0.038885`, median `0.061042`, mae `0.06884`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.000925`, median `-0.001658`, mae `0.017819`
- 5d: sample `40`, hit `0.475`, avg `-0.003528`, median `-0.004438`, mae `0.020628`
- 10d: sample `40`, hit `0.4`, avg `0.00157`, median `-0.005891`, mae `0.022726`
- 20d: sample `40`, hit `0.675`, avg `0.020198`, median `0.025442`, mae `0.029605`
- 60d: sample `40`, hit `0.825`, avg `0.060041`, median `0.064905`, mae `0.076969`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.003028`, median `-0.001658`, mae `0.012387`
- 5d: sample `40`, hit `0.475`, avg `-0.008062`, median `-0.00244`, mae `0.014748`
- 10d: sample `40`, hit `0.375`, avg `-0.003768`, median `-0.007117`, mae `0.018309`
- 20d: sample `40`, hit `0.625`, avg `0.010519`, median `0.02086`, mae `0.033209`
- 60d: sample `40`, hit `0.675`, avg `0.038885`, median `0.061042`, mae `0.06884`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.006189`, median `0.01152`, mae `0.015762`
- 5d: sample `20`, hit `0.75`, avg `0.010821`, median `0.013131`, mae `0.017561`
- 10d: sample `20`, hit `0.35`, avg `-0.004756`, median `-0.013321`, mae `0.026035`
- 20d: sample `20`, hit `0.5`, avg `0.007778`, median `0.002095`, mae `0.036882`
- 60d: sample `20`, hit `0.75`, avg `0.022746`, median `0.03104`, mae `0.067064`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.003028`, median `-0.001658`, mae `0.012387`
- 5d: sample `40`, hit `0.475`, avg `-0.008062`, median `-0.00244`, mae `0.014748`
- 10d: sample `40`, hit `0.375`, avg `-0.003768`, median `-0.007117`, mae `0.018309`
- 20d: sample `40`, hit `0.625`, avg `0.010519`, median `0.02086`, mae `0.033209`
- 60d: sample `40`, hit `0.675`, avg `0.038885`, median `0.061042`, mae `0.06884`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.000144`, median `-0.001428`, mae `0.009145`
- 5d: sample `20`, hit `0.55`, avg `-0.004205`, median `0.000873`, mae `0.011405`
- 10d: sample `20`, hit `0.45`, avg `-0.003554`, median `-0.007117`, mae `0.018823`
- 20d: sample `20`, hit `0.6`, avg `0.003667`, median `0.020226`, mae `0.035075`
- 60d: sample `20`, hit `0.65`, avg `0.032612`, median `0.061042`, mae `0.062166`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
