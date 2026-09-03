# High Confidence Edge Report

Generated at: `2026-09-03T16:28:19.382826+00:00`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `-0.00011`, median `0.000616`, mae `0.014495`
- 5d: sample `80`, hit `0.575`, avg `0.001808`, median `0.001303`, mae `0.016799`
- 10d: sample `80`, hit `0.4125`, avg `-0.001015`, median `-0.007117`, mae `0.022509`
- 20d: sample `80`, hit `0.6125`, avg `0.005439`, median `0.013877`, mae `0.033634`
- 60d: sample `80`, hit `0.7`, avg `0.029985`, median `0.046132`, mae `0.065296`

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
- 3d: sample `8`, hit `0.5`, avg `-0.008657`, median `0.001558`, mae `0.013123`
- 5d: sample `8`, hit `0.25`, avg `-0.014544`, median `-0.013034`, mae `0.021498`
- 10d: sample `8`, hit `0.625`, avg `0.004059`, median `0.019233`, mae `0.021586`
- 20d: sample `8`, hit `0.875`, avg `0.013802`, median `0.029166`, mae `0.027628`
- 60d: sample `8`, hit `0.75`, avg `0.043429`, median `0.059495`, mae `0.062679`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.008657`, median `0.001558`, mae `0.013123`
- 5d: sample `8`, hit `0.25`, avg `-0.014544`, median `-0.013034`, mae `0.021498`
- 10d: sample `8`, hit `0.625`, avg `0.004059`, median `0.019233`, mae `0.021586`
- 20d: sample `8`, hit `0.875`, avg `0.013802`, median `0.029166`, mae `0.027628`
- 60d: sample `8`, hit `0.75`, avg `0.043429`, median `0.059495`, mae `0.062679`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.008657, 'median_return': 0.001558, 'mean_absolute_return': 0.013123, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.01018}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.014544, 'median_return': -0.013034, 'mean_absolute_return': 0.021498, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.004059, 'median_return': 0.019233, 'mean_absolute_return': 0.021586, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.013802, 'median_return': 0.029166, 'mean_absolute_return': 0.027628, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.033999}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.043429, 'median_return': 0.059495, 'mean_absolute_return': 0.062679, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.101282}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.00084, 'median_return': 0.000616, 'mean_absolute_return': 0.014648, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.003625, 'median_return': 0.002786, 'mean_absolute_return': 0.016276, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': -0.001578, 'median_return': -0.007491, 'mean_absolute_return': 0.022612, 'max_adverse_excursion': -0.057499, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.00451, 'median_return': 0.012337, 'mean_absolute_return': 0.034302, 'max_adverse_excursion': -0.10356, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.028491, 'median_return': 0.043615, 'mean_absolute_return': 0.065587, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.475}, '5d': {'sample_size': 80, 'hit_rate': 0.425}, '10d': {'sample_size': 80, 'hit_rate': 0.5875}, '20d': {'sample_size': 80, 'hit_rate': 0.3875}, '60d': {'sample_size': 80, 'hit_rate': 0.3}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_minus_secondary': 0.175, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': -0.4, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.000908, 'median_return': 0.00234, 'mean_absolute_return': 0.016576, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.003012, 'median_return': 0.003829, 'mean_absolute_return': 0.019232, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': 0.003476, 'median_return': 0.000655, 'mean_absolute_return': 0.022869, 'max_adverse_excursion': -0.057499, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.016575, 'median_return': 0.025442, 'mean_absolute_return': 0.031532, 'max_adverse_excursion': -0.090764, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 60, 'hit_rate': 0.8333, 'avg_return': 0.045463, 'median_return': 0.061806, 'mean_absolute_return': 0.068911, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.003162, 'median_return': -0.001428, 'mean_absolute_return': 0.008254, 'max_adverse_excursion': -0.024978, 'max_favorable_excursion': 0.011487}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.001804, 'median_return': 0.000873, 'mean_absolute_return': 0.009499, 'max_adverse_excursion': -0.035525, 'max_favorable_excursion': 0.022174}, '10d': {'sample_size': 20, 'hit_rate': 0.15, 'avg_return': -0.014486, 'median_return': -0.016376, 'mean_absolute_return': 0.021428, 'max_adverse_excursion': -0.043454, 'max_favorable_excursion': 0.031945}, '20d': {'sample_size': 20, 'hit_rate': 0.25, 'avg_return': -0.027969, 'median_return': -0.016058, 'mean_absolute_return': 0.03994, 'max_adverse_excursion': -0.10356, 'max_favorable_excursion': 0.039296}, '60d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.016448, 'median_return': -0.020815, 'mean_absolute_return': 0.054451, 'max_adverse_excursion': -0.090808, 'max_favorable_excursion': 0.085951}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `60`, hit `0.5`, avg `3.2e-05`, median `0.000201`, mae `0.013925`
- 5d: sample `60`, hit `0.55`, avg `0.000259`, median `0.000762`, mae `0.015906`
- 10d: sample `60`, hit `0.3667`, avg `-0.001376`, median `-0.007491`, mae `0.022438`
- 20d: sample `60`, hit `0.6167`, avg `0.005215`, median `0.014522`, mae `0.03398`
- 60d: sample `60`, hit `0.6833`, avg `0.032472`, median `0.053843`, mae `0.064995`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.001629`, median `0.00234`, mae `0.016761`
- 5d: sample `40`, hit `0.525`, avg `0.001291`, median `0.000415`, mae `0.019109`
- 10d: sample `40`, hit `0.475`, avg `0.005178`, median `-0.0004`, mae `0.022943`
- 20d: sample `40`, hit `0.8`, avg `0.021806`, median `0.028324`, mae `0.031001`
- 60d: sample `40`, hit `0.875`, avg `0.056932`, median `0.065295`, mae `0.070267`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.5`, avg `3.2e-05`, median `0.000201`, mae `0.013925`
- 5d: sample `60`, hit `0.55`, avg `0.000259`, median `0.000762`, mae `0.015906`
- 10d: sample `60`, hit `0.3667`, avg `-0.001376`, median `-0.007491`, mae `0.022438`
- 20d: sample `60`, hit `0.6167`, avg `0.005215`, median `0.014522`, mae `0.03398`
- 60d: sample `60`, hit `0.6833`, avg `0.032472`, median `0.053843`, mae `0.064995`

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
- 3d: sample `80`, hit `0.525`, avg `-0.00011`, median `0.000616`, mae `0.014495`
- 5d: sample `80`, hit `0.575`, avg `0.001808`, median `0.001303`, mae `0.016799`
- 10d: sample `80`, hit `0.4125`, avg `-0.001015`, median `-0.007117`, mae `0.022509`
- 20d: sample `80`, hit `0.6125`, avg `0.005439`, median `0.013877`, mae `0.033634`
- 60d: sample `80`, hit `0.7`, avg `0.029985`, median `0.046132`, mae `0.065296`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.003162`, median `-0.001428`, mae `0.008254`
- 5d: sample `20`, hit `0.6`, avg `-0.001804`, median `0.000873`, mae `0.009499`
- 10d: sample `20`, hit `0.15`, avg `-0.014486`, median `-0.016376`, mae `0.021428`
- 20d: sample `20`, hit `0.25`, avg `-0.027969`, median `-0.016058`, mae `0.03994`
- 60d: sample `20`, hit `0.3`, avg `-0.016448`, median `-0.020815`, mae `0.054451`

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
