# High Confidence Edge Report

Generated at: `2026-06-30T23:48:02.965815+00:00`

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
- 3d: sample `60`, hit `0.4333`, avg `-0.002349`, median `-0.001811`, mae `0.012643`
- 5d: sample `60`, hit `0.4167`, avg `-0.004943`, median `-0.004461`, mae `0.017222`
- 10d: sample `60`, hit `0.4667`, avg `-0.000542`, median `-0.001932`, mae `0.02059`
- 20d: sample `60`, hit `0.6167`, avg `0.004846`, median `0.010788`, mae `0.033069`
- 60d: sample `60`, hit `0.55`, avg `0.024327`, median `0.029831`, mae `0.068969`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.25`, avg `-0.005303`, median `-0.006734`, mae `0.008731`
- 5d: sample `20`, hit `0.6`, avg `-0.00094`, median `0.003026`, mae `0.01073`
- 10d: sample `20`, hit `0.45`, avg `-0.001082`, median `-0.001676`, mae `0.012227`
- 20d: sample `20`, hit `0.6`, avg `-0.000442`, median `0.011728`, mae `0.025508`
- 60d: sample `20`, hit `0.2`, avg `-0.036757`, median `-0.041391`, mae `0.04867`

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
- 3d: sample `8`, hit `0.125`, avg `-0.013613`, median `-0.010378`, mae `0.016342`
- 5d: sample `8`, hit `0.125`, avg `-0.019931`, median `-0.022865`, mae `0.022359`
- 10d: sample `8`, hit `0.125`, avg `-0.006621`, median `-0.005891`, mae `0.01185`
- 20d: sample `8`, hit `0.75`, avg `0.022237`, median `0.031196`, mae `0.030667`
- 60d: sample `8`, hit `0.75`, avg `0.052494`, median `0.081091`, mae `0.074213`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.125`, avg `-0.013613`, median `-0.010378`, mae `0.016342`
- 5d: sample `8`, hit `0.125`, avg `-0.019931`, median `-0.022865`, mae `0.022359`
- 10d: sample `8`, hit `0.125`, avg `-0.006621`, median `-0.005891`, mae `0.01185`
- 20d: sample `8`, hit `0.75`, avg `0.022237`, median `0.031196`, mae `0.030667`
- 60d: sample `8`, hit `0.75`, avg `0.052494`, median `0.081091`, mae `0.074213`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4333, 'avg_return': -0.002349, 'median_return': -0.001811, 'mean_absolute_return': 0.012643, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.044644}, '5d': {'sample_size': 60, 'hit_rate': 0.4167, 'avg_return': -0.004943, 'median_return': -0.004461, 'mean_absolute_return': 0.017222, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.036593}, '10d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.000542, 'median_return': -0.001932, 'mean_absolute_return': 0.02059, 'max_adverse_excursion': -0.057921, 'max_favorable_excursion': 0.056454}, '20d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.004846, 'median_return': 0.010788, 'mean_absolute_return': 0.033069, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.083836}, '60d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.024327, 'median_return': 0.029831, 'mean_absolute_return': 0.068969, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.276706}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.013613, 'median_return': -0.010378, 'mean_absolute_return': 0.016342, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.010917}, '5d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.019931, 'median_return': -0.022865, 'mean_absolute_return': 0.022359, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.006621, 'median_return': -0.005891, 'mean_absolute_return': 0.01185, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.020918}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.022237, 'median_return': 0.031196, 'mean_absolute_return': 0.030667, 'max_adverse_excursion': -0.02149, 'max_favorable_excursion': 0.058396}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.052494, 'median_return': 0.081091, 'mean_absolute_return': 0.074213, 'max_adverse_excursion': -0.055789, 'max_favorable_excursion': 0.121826}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.001918, 'median_return': -0.002654, 'mean_absolute_return': 0.011145, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.044644}, '5d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.002166, 'median_return': 0.000415, 'mean_absolute_return': 0.014848, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.036593}, '10d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -1.7e-05, 'median_return': 0.000197, 'mean_absolute_return': 0.019238, 'max_adverse_excursion': -0.057921, 'max_favorable_excursion': 0.056454}, '20d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.001445, 'median_return': 0.007676, 'mean_absolute_return': 0.031236, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.083836}, '60d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': 0.004229, 'median_return': -0.009954, 'mean_absolute_return': 0.062747, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.276706}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5125}, '5d': {'sample_size': 80, 'hit_rate': 0.4125}, '10d': {'sample_size': 80, 'hit_rate': 0.4875}, '20d': {'sample_size': 80, 'hit_rate': 0.5625}, '60d': {'sample_size': 80, 'hit_rate': 0.6125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.3875, 'primary_minus_secondary': 0.125, 'both_hit': 6, 'both_miss': 14}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': -0.075, 'both_hit': 6, 'both_miss': 14}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.05, 'both_hit': 7, 'both_miss': 13}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': 0.0, 'both_hit': 15, 'both_miss': 5}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.125, 'both_hit': 14, 'both_miss': 6}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.003269, 'median_return': 0.006632, 'mean_absolute_return': 0.011086, 'max_adverse_excursion': -0.017591, 'max_favorable_excursion': 0.022897}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.003341, 'median_return': 0.005876, 'mean_absolute_return': 0.015986, 'max_adverse_excursion': -0.026896, 'max_favorable_excursion': 0.034374}, '10d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.003545, 'median_return': 0.003262, 'mean_absolute_return': 0.026335, 'max_adverse_excursion': -0.057921, 'max_favorable_excursion': 0.042758}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': -0.010681, 'median_return': 0.007676, 'mean_absolute_return': 0.035455, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.054455}, '60d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.023036, 'median_return': -0.01215, 'mean_absolute_return': 0.045856, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.071905}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.3, 'avg_return': -0.005207, 'median_return': -0.005568, 'mean_absolute_return': 0.011858, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.044644}, '5d': {'sample_size': 60, 'hit_rate': 0.4167, 'avg_return': -0.00637, 'median_return': -0.004389, 'mean_absolute_return': 0.01547, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.036593}, '10d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': 0.000279, 'median_return': -0.001932, 'mean_absolute_return': 0.015887, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.056454}, '20d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.008259, 'median_return': 0.012291, 'mean_absolute_return': 0.029754, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.083836}, '60d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': 0.019753, 'median_return': 0.018072, 'mean_absolute_return': 0.069906, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.276706}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.002349`, median `-0.001811`, mae `0.012643`
- 5d: sample `60`, hit `0.4167`, avg `-0.004943`, median `-0.004461`, mae `0.017222`
- 10d: sample `60`, hit `0.4667`, avg `-0.000542`, median `-0.001932`, mae `0.02059`
- 20d: sample `60`, hit `0.6167`, avg `0.004846`, median `0.010788`, mae `0.033069`
- 60d: sample `60`, hit `0.55`, avg `0.024327`, median `0.029831`, mae `0.068969`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.25`, avg `-0.005303`, median `-0.006734`, mae `0.008731`
- 5d: sample `20`, hit `0.6`, avg `-0.00094`, median `0.003026`, mae `0.01073`
- 10d: sample `20`, hit `0.45`, avg `-0.001082`, median `-0.001676`, mae `0.012227`
- 20d: sample `20`, hit `0.6`, avg `-0.000442`, median `0.011728`, mae `0.025508`
- 60d: sample `20`, hit `0.2`, avg `-0.036757`, median `-0.041391`, mae `0.04867`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.002349`, median `-0.001811`, mae `0.012643`
- 5d: sample `60`, hit `0.4167`, avg `-0.004943`, median `-0.004461`, mae `0.017222`
- 10d: sample `60`, hit `0.4667`, avg `-0.000542`, median `-0.001932`, mae `0.02059`
- 20d: sample `60`, hit `0.6167`, avg `0.004846`, median `0.010788`, mae `0.033069`
- 60d: sample `60`, hit `0.55`, avg `0.024327`, median `0.029831`, mae `0.068969`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.003434`, median `-0.001658`, mae `0.01351`
- 5d: sample `40`, hit `0.45`, avg `-0.004487`, median `-0.004461`, mae `0.017767`
- 10d: sample `40`, hit `0.425`, avg `-0.002735`, median `-0.005891`, mae `0.020789`
- 20d: sample `40`, hit `0.7`, avg `0.005011`, median `0.013156`, mae `0.034249`
- 60d: sample `40`, hit `0.5`, avg `0.012191`, median `0.003923`, mae `0.062126`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.002349`, median `-0.001811`, mae `0.012643`
- 5d: sample `60`, hit `0.4167`, avg `-0.004943`, median `-0.004461`, mae `0.017222`
- 10d: sample `60`, hit `0.4667`, avg `-0.000542`, median `-0.001932`, mae `0.02059`
- 20d: sample `60`, hit `0.6167`, avg `0.004846`, median `0.010788`, mae `0.033069`
- 60d: sample `60`, hit `0.55`, avg `0.024327`, median `0.029831`, mae `0.068969`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.003434`, median `-0.001658`, mae `0.01351`
- 5d: sample `40`, hit `0.45`, avg `-0.004487`, median `-0.004461`, mae `0.017767`
- 10d: sample `40`, hit `0.425`, avg `-0.002735`, median `-0.005891`, mae `0.020789`
- 20d: sample `40`, hit `0.7`, avg `0.005011`, median `0.013156`, mae `0.034249`
- 60d: sample `40`, hit `0.5`, avg `0.012191`, median `0.003923`, mae `0.062126`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.25`, avg `-0.005303`, median `-0.006734`, mae `0.008731`
- 5d: sample `20`, hit `0.6`, avg `-0.00094`, median `0.003026`, mae `0.01073`
- 10d: sample `20`, hit `0.45`, avg `-0.001082`, median `-0.001676`, mae `0.012227`
- 20d: sample `20`, hit `0.6`, avg `-0.000442`, median `0.011728`, mae `0.025508`
- 60d: sample `20`, hit `0.2`, avg `-0.036757`, median `-0.041391`, mae `0.04867`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.002349`, median `-0.001811`, mae `0.012643`
- 5d: sample `60`, hit `0.4167`, avg `-0.004943`, median `-0.004461`, mae `0.017222`
- 10d: sample `60`, hit `0.4667`, avg `-0.000542`, median `-0.001932`, mae `0.02059`
- 20d: sample `60`, hit `0.6167`, avg `0.004846`, median `0.010788`, mae `0.033069`
- 60d: sample `60`, hit `0.55`, avg `0.024327`, median `0.029831`, mae `0.068969`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.25`, avg `-0.005303`, median `-0.006734`, mae `0.008731`
- 5d: sample `20`, hit `0.6`, avg `-0.00094`, median `0.003026`, mae `0.01073`
- 10d: sample `20`, hit `0.45`, avg `-0.001082`, median `-0.001676`, mae `0.012227`
- 20d: sample `20`, hit `0.6`, avg `-0.000442`, median `0.011728`, mae `0.025508`
- 60d: sample `20`, hit `0.2`, avg `-0.036757`, median `-0.041391`, mae `0.04867`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.002349`, median `-0.001811`, mae `0.012643`
- 5d: sample `60`, hit `0.4167`, avg `-0.004943`, median `-0.004461`, mae `0.017222`
- 10d: sample `60`, hit `0.4667`, avg `-0.000542`, median `-0.001932`, mae `0.02059`
- 20d: sample `60`, hit `0.6167`, avg `0.004846`, median `0.010788`, mae `0.033069`
- 60d: sample `60`, hit `0.55`, avg `0.024327`, median `0.029831`, mae `0.068969`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.002349`, median `-0.001811`, mae `0.012643`
- 5d: sample `60`, hit `0.4167`, avg `-0.004943`, median `-0.004461`, mae `0.017222`
- 10d: sample `60`, hit `0.4667`, avg `-0.000542`, median `-0.001932`, mae `0.02059`
- 20d: sample `60`, hit `0.6167`, avg `0.004846`, median `0.010788`, mae `0.033069`
- 60d: sample `60`, hit `0.55`, avg `0.024327`, median `0.029831`, mae `0.068969`

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
