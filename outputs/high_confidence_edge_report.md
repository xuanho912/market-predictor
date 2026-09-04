# High Confidence Edge Report

Generated at: `2026-09-04T16:25:31.539061+00:00`

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
- 3d: sample `40`, hit `0.525`, avg `-0.003716`, median `0.001558`, mae `0.015116`
- 5d: sample `40`, hit `0.55`, avg `-0.002084`, median `0.001239`, mae `0.018198`
- 10d: sample `40`, hit `0.4`, avg `0.000363`, median `-0.00676`, mae `0.02355`
- 20d: sample `40`, hit `0.75`, avg `0.015773`, median `0.029166`, mae `0.034512`
- 60d: sample `40`, hit `0.675`, avg `0.030659`, median `0.059495`, mae `0.074951`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.001845`, median `-0.001641`, mae `0.013491`
- 5d: sample `40`, hit `0.5`, avg `-0.000553`, median `0.000688`, mae `0.014613`
- 10d: sample `40`, hit `0.325`, avg `-0.003546`, median `-0.012383`, mae `0.025843`
- 20d: sample `40`, hit `0.5`, avg `-0.004231`, median `9.2e-05`, mae `0.035502`
- 60d: sample `40`, hit `0.6`, avg `0.018959`, median `0.032982`, mae `0.061502`

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
- 3d: sample `8`, hit `0.75`, avg `0.004554`, median `0.00979`, mae `0.01269`
- 5d: sample `8`, hit `0.875`, avg `0.010971`, median `0.008039`, mae `0.014164`
- 10d: sample `8`, hit `0.5`, avg `0.002929`, median `0.013736`, mae `0.020472`
- 20d: sample `8`, hit `0.75`, avg `0.011715`, median `0.038303`, mae `0.040885`
- 60d: sample `8`, hit `0.5`, avg `-0.014287`, median `0.007953`, mae `0.063995`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.007591`, median `0.00234`, mae `0.013736`
- 5d: sample `8`, hit `0.375`, avg `-0.01205`, median `-0.012956`, mae `0.019755`
- 10d: sample `8`, hit `0.5`, avg `0.000185`, median `0.0076`, mae `0.019465`
- 20d: sample `8`, hit `0.875`, avg `0.012354`, median `0.026531`, mae `0.026179`
- 60d: sample `8`, hit `0.75`, avg `0.03306`, median `0.046132`, mae `0.05231`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.003716, 'median_return': 0.001558, 'mean_absolute_return': 0.015116, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.026658}, '5d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': -0.002084, 'median_return': 0.001239, 'mean_absolute_return': 0.018198, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.043092}, '10d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': 0.000363, 'median_return': -0.00676, 'mean_absolute_return': 0.02355, 'max_adverse_excursion': -0.057499, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.015773, 'median_return': 0.029166, 'mean_absolute_return': 0.034512, 'max_adverse_excursion': -0.090764, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.030659, 'median_return': 0.059495, 'mean_absolute_return': 0.074951, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.007591, 'median_return': 0.00234, 'mean_absolute_return': 0.013736, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.01018}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.01205, 'median_return': -0.012956, 'mean_absolute_return': 0.019755, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.000185, 'median_return': 0.0076, 'mean_absolute_return': 0.019465, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.012354, 'median_return': 0.026531, 'mean_absolute_return': 0.026179, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.033999}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.03306, 'median_return': 0.046132, 'mean_absolute_return': 0.05231, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.101282}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.002246, 'median_return': -0.001617, 'mean_absolute_return': 0.014367, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': -0.000126, 'median_return': 0.000762, 'mean_absolute_return': 0.016033, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 72, 'hit_rate': 0.3472, 'avg_return': -0.001789, 'median_return': -0.010456, 'mean_absolute_return': 0.025277, 'max_adverse_excursion': -0.057499, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.00504, 'median_return': 0.016437, 'mean_absolute_return': 0.035988, 'max_adverse_excursion': -0.10356, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.023892, 'median_return': 0.043615, 'mean_absolute_return': 0.069995, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5125}, '5d': {'sample_size': 80, 'hit_rate': 0.475}, '10d': {'sample_size': 80, 'hit_rate': 0.6375}, '20d': {'sample_size': 80, 'hit_rate': 0.375}, '60d': {'sample_size': 80, 'hit_rate': 0.3625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.3625, 'primary_minus_secondary': 0.275, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.25, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.275, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': -0.001969, 'median_return': 0.001558, 'mean_absolute_return': 0.016018, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': -0.000376, 'median_return': 0.000415, 'mean_absolute_return': 0.018666, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': 0.003208, 'median_return': -0.00367, 'mean_absolute_return': 0.02594, 'max_adverse_excursion': -0.057499, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.016336, 'median_return': 0.025442, 'mean_absolute_return': 0.03319, 'max_adverse_excursion': -0.090764, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.037654, 'median_return': 0.062363, 'mean_absolute_return': 0.073123, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.005217, 'median_return': -0.001641, 'mean_absolute_return': 0.00916, 'max_adverse_excursion': -0.029603, 'max_favorable_excursion': 0.010897}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.004146, 'median_return': 0.000762, 'mean_absolute_return': 0.009624, 'max_adverse_excursion': -0.035525, 'max_favorable_excursion': 0.019686}, '10d': {'sample_size': 20, 'hit_rate': 0.1, 'avg_return': -0.015992, 'median_return': -0.016376, 'mean_absolute_return': 0.020964, 'max_adverse_excursion': -0.043454, 'max_favorable_excursion': 0.031945}, '20d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.025923, 'median_return': -0.016058, 'mean_absolute_return': 0.040459, 'max_adverse_excursion': -0.10356, 'max_favorable_excursion': 0.039296}, '60d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.013727, 'median_return': -0.018455, 'mean_absolute_return': 0.053537, 'max_adverse_excursion': -0.090808, 'max_favorable_excursion': 0.085951}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `60`, hit `0.45`, avg `-0.002788`, median `-0.001658`, mae `0.013436`
- 5d: sample `60`, hit `0.4833`, avg `-0.003083`, median `-0.00244`, mae `0.014622`
- 10d: sample `60`, hit `0.3333`, avg `-0.002772`, median `-0.010413`, mae `0.023269`
- 20d: sample `60`, hit `0.5833`, avg `0.003526`, median `0.014522`, mae `0.03521`
- 60d: sample `60`, hit `0.65`, avg `0.02854`, median `0.049712`, mae `0.066484`

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
- 3d: sample `40`, hit `0.475`, avg `-0.001573`, median `-0.001658`, mae `0.015574`
- 5d: sample `40`, hit `0.45`, avg `-0.002551`, median `-0.005477`, mae `0.017121`
- 10d: sample `40`, hit `0.45`, avg `0.003838`, median `-0.001222`, mae `0.024421`
- 20d: sample `40`, hit `0.725`, avg `0.01825`, median `0.026531`, mae `0.032586`
- 60d: sample `40`, hit `0.8`, avg `0.049674`, median `0.064905`, mae `0.072957`

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
- 3d: sample `60`, hit `0.45`, avg `-0.002788`, median `-0.001658`, mae `0.013436`
- 5d: sample `60`, hit `0.4833`, avg `-0.003083`, median `-0.00244`, mae `0.014622`
- 10d: sample `60`, hit `0.3333`, avg `-0.002772`, median `-0.010413`, mae `0.023269`
- 20d: sample `60`, hit `0.5833`, avg `0.003526`, median `0.014522`, mae `0.03521`
- 60d: sample `60`, hit `0.65`, avg `0.02854`, median `0.049712`, mae `0.066484`

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
- 3d: sample `80`, hit `0.4875`, avg `-0.002781`, median `-0.001428`, mae `0.014303`
- 5d: sample `80`, hit `0.525`, avg `-0.001319`, median `0.000688`, mae `0.016406`
- 10d: sample `80`, hit `0.3625`, avg `-0.001592`, median `-0.010413`, mae `0.024696`
- 20d: sample `80`, hit `0.625`, avg `0.005771`, median `0.017881`, mae `0.035007`
- 60d: sample `80`, hit `0.6375`, avg `0.024809`, median `0.043615`, mae `0.068226`

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
