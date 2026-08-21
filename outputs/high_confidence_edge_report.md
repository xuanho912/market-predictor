# High Confidence Edge Report

Generated at: `2026-08-21T23:36:47.526043+00:00`

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
- 3d: sample `80`, hit `0.675`, avg `0.003808`, median `0.00558`, mae `0.014461`
- 5d: sample `80`, hit `0.575`, avg `0.002807`, median `0.001654`, mae `0.018442`
- 10d: sample `80`, hit `0.5125`, avg `0.003161`, median `0.004304`, mae `0.028247`
- 20d: sample `80`, hit `0.575`, avg `0.0036`, median `0.010656`, mae `0.042752`
- 60d: sample `80`, hit `0.5625`, avg `0.014634`, median `0.02283`, mae `0.065371`

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
- 3d: sample `8`, hit `0.75`, avg `-0.002548`, median `0.003785`, mae `0.014743`
- 5d: sample `8`, hit `0.5`, avg `-0.0069`, median `0.004014`, mae `0.021665`
- 10d: sample `8`, hit `0.75`, avg `0.010019`, median `0.021953`, mae `0.022476`
- 20d: sample `8`, hit `0.625`, avg `0.010949`, median `0.026531`, mae `0.030454`
- 60d: sample `8`, hit `0.5`, avg `0.012955`, median `0.029831`, mae `0.053132`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `-0.002548`, median `0.003785`, mae `0.014743`
- 5d: sample `8`, hit `0.5`, avg `-0.0069`, median `0.004014`, mae `0.021665`
- 10d: sample `8`, hit `0.75`, avg `0.010019`, median `0.021953`, mae `0.022476`
- 20d: sample `8`, hit `0.625`, avg `0.010949`, median `0.026531`, mae `0.030454`
- 60d: sample `8`, hit `0.5`, avg `0.012955`, median `0.029831`, mae `0.053132`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.003808, 'median_return': 0.00558, 'mean_absolute_return': 0.014461, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 80, 'hit_rate': 0.575, 'avg_return': 0.002807, 'median_return': 0.001654, 'mean_absolute_return': 0.018442, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.5125, 'avg_return': 0.003161, 'median_return': 0.004304, 'mean_absolute_return': 0.028247, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.575, 'avg_return': 0.0036, 'median_return': 0.010656, 'mean_absolute_return': 0.042752, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': 0.014634, 'median_return': 0.02283, 'mean_absolute_return': 0.065371, 'max_adverse_excursion': -0.195048, 'max_favorable_excursion': 0.171512}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': -0.002548, 'median_return': 0.003785, 'mean_absolute_return': 0.014743, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.0069, 'median_return': 0.004014, 'mean_absolute_return': 0.021665, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.010019, 'median_return': 0.021953, 'mean_absolute_return': 0.022476, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.010949, 'median_return': 0.026531, 'mean_absolute_return': 0.030454, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.012955, 'median_return': 0.029831, 'mean_absolute_return': 0.053132, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.101282}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.004514, 'median_return': 0.005581, 'mean_absolute_return': 0.014429, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.003886, 'median_return': 0.001654, 'mean_absolute_return': 0.018084, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': 0.002399, 'median_return': -0.000629, 'mean_absolute_return': 0.028889, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.002784, 'median_return': 0.009812, 'mean_absolute_return': 0.044118, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.014821, 'median_return': 0.02283, 'mean_absolute_return': 0.066731, 'max_adverse_excursion': -0.195048, 'max_favorable_excursion': 0.171512}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.675}, '5d': {'sample_size': 80, 'hit_rate': 0.575}, '10d': {'sample_size': 80, 'hit_rate': 0.5125}, '20d': {'sample_size': 80, 'hit_rate': 0.575}, '60d': {'sample_size': 80, 'hit_rate': 0.5625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': 0.1, 'both_hit': 40, 'both_miss': 20}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.075, 'both_hit': 33, 'both_miss': 27}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.125, 'both_hit': 36, 'both_miss': 24}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': -0.125, 'both_hit': 41, 'both_miss': 19}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.075, 'both_hit': 38, 'both_miss': 22}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.009086, 'median_return': 0.00979, 'mean_absolute_return': 0.017576, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.006951, 'median_return': 0.005327, 'mean_absolute_return': 0.025253, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.011748, 'median_return': 0.016085, 'mean_absolute_return': 0.035955, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.017421, 'median_return': 0.021696, 'mean_absolute_return': 0.050246, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.035457, 'median_return': 0.052998, 'mean_absolute_return': 0.078424, 'max_adverse_excursion': -0.195048, 'max_favorable_excursion': 0.171512}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': -0.00147, 'median_return': 0.001448, 'mean_absolute_return': 0.011345, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.022679}, '5d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': -0.001336, 'median_return': 0.000873, 'mean_absolute_return': 0.011632, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.032969}, '10d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.005425, 'median_return': -0.012383, 'mean_absolute_return': 0.02054, 'max_adverse_excursion': -0.043454, 'max_favorable_excursion': 0.04237}, '20d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.010221, 'median_return': -0.003522, 'mean_absolute_return': 0.035258, 'max_adverse_excursion': -0.10356, 'max_favorable_excursion': 0.07754}, '60d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.006189, 'median_return': -0.02013, 'mean_absolute_return': 0.052317, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.101282}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `-0.00147`, median `0.001448`, mae `0.011345`
- 5d: sample `40`, hit `0.575`, avg `-0.001336`, median `0.000873`, mae `0.011632`
- 10d: sample `40`, hit `0.4`, avg `-0.005425`, median `-0.012383`, mae `0.02054`
- 20d: sample `40`, hit `0.45`, avg `-0.010221`, median `-0.003522`, mae `0.035258`
- 60d: sample `40`, hit `0.425`, avg `-0.006189`, median `-0.02013`, mae `0.052317`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.001412`, median `0.003785`, mae `0.01685`
- 5d: sample `40`, hit `0.5`, avg `0.00028`, median `0.000415`, mae `0.02032`
- 10d: sample `40`, hit `0.6`, avg `0.0085`, median `0.011168`, mae `0.029745`
- 20d: sample `40`, hit `0.7`, avg `0.018772`, median `0.020068`, mae `0.045992`
- 60d: sample `40`, hit `0.625`, avg `0.030657`, median `0.026795`, mae `0.068631`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `-0.00147`, median `0.001448`, mae `0.011345`
- 5d: sample `40`, hit `0.575`, avg `-0.001336`, median `0.000873`, mae `0.011632`
- 10d: sample `40`, hit `0.4`, avg `-0.005425`, median `-0.012383`, mae `0.02054`
- 20d: sample `40`, hit `0.45`, avg `-0.010221`, median `-0.003522`, mae `0.035258`
- 60d: sample `40`, hit `0.425`, avg `-0.006189`, median `-0.02013`, mae `0.052317`

### breadth_conflicted_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.001412`, median `0.003785`, mae `0.01685`
- 5d: sample `40`, hit `0.5`, avg `0.00028`, median `0.000415`, mae `0.02032`
- 10d: sample `40`, hit `0.6`, avg `0.0085`, median `0.011168`, mae `0.029745`
- 20d: sample `40`, hit `0.7`, avg `0.018772`, median `0.020068`, mae `0.045992`
- 60d: sample `40`, hit `0.625`, avg `0.030657`, median `0.026795`, mae `0.068631`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.004709`, median `0.001448`, mae `0.01387`
- 5d: sample `20`, hit `0.5`, avg `-0.00256`, median `0.000415`, mae `0.013629`
- 10d: sample `20`, hit `0.55`, avg `0.001577`, median `0.0076`, mae `0.020351`
- 20d: sample `20`, hit `0.65`, avg `0.005019`, median `0.012958`, mae `0.033663`
- 60d: sample `20`, hit `0.5`, avg `0.002491`, median `0.012092`, mae `0.049683`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.001412`, median `0.003785`, mae `0.01685`
- 5d: sample `40`, hit `0.5`, avg `0.00028`, median `0.000415`, mae `0.02032`
- 10d: sample `40`, hit `0.6`, avg `0.0085`, median `0.011168`, mae `0.029745`
- 20d: sample `40`, hit `0.7`, avg `0.018772`, median `0.020068`, mae `0.045992`
- 60d: sample `40`, hit `0.625`, avg `0.030657`, median `0.026795`, mae `0.068631`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `-0.00147`, median `0.001448`, mae `0.011345`
- 5d: sample `40`, hit `0.575`, avg `-0.001336`, median `0.000873`, mae `0.011632`
- 10d: sample `40`, hit `0.4`, avg `-0.005425`, median `-0.012383`, mae `0.02054`
- 20d: sample `40`, hit `0.45`, avg `-0.010221`, median `-0.003522`, mae `0.035258`
- 60d: sample `40`, hit `0.425`, avg `-0.006189`, median `-0.02013`, mae `0.052317`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.725`, avg `0.009086`, median `0.00979`, mae `0.017576`
- 5d: sample `40`, hit `0.575`, avg `0.006951`, median `0.005327`, mae `0.025253`
- 10d: sample `40`, hit `0.625`, avg `0.011748`, median `0.016085`, mae `0.035955`
- 20d: sample `40`, hit `0.7`, avg `0.017421`, median `0.021696`, mae `0.050246`
- 60d: sample `40`, hit `0.7`, avg `0.035457`, median `0.052998`, mae `0.078424`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.004709`, median `0.001448`, mae `0.01387`
- 5d: sample `20`, hit `0.5`, avg `-0.00256`, median `0.000415`, mae `0.013629`
- 10d: sample `20`, hit `0.55`, avg `0.001577`, median `0.0076`, mae `0.020351`
- 20d: sample `20`, hit `0.65`, avg `0.005019`, median `0.012958`, mae `0.033663`
- 60d: sample `20`, hit `0.5`, avg `0.002491`, median `0.012092`, mae `0.049683`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `-0.00147`, median `0.001448`, mae `0.011345`
- 5d: sample `40`, hit `0.575`, avg `-0.001336`, median `0.000873`, mae `0.011632`
- 10d: sample `40`, hit `0.4`, avg `-0.005425`, median `-0.012383`, mae `0.02054`
- 20d: sample `40`, hit `0.45`, avg `-0.010221`, median `-0.003522`, mae `0.035258`
- 60d: sample `40`, hit `0.425`, avg `-0.006189`, median `-0.02013`, mae `0.052317`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.675`, avg `0.003808`, median `0.00558`, mae `0.014461`
- 5d: sample `80`, hit `0.575`, avg `0.002807`, median `0.001654`, mae `0.018442`
- 10d: sample `80`, hit `0.5125`, avg `0.003161`, median `0.004304`, mae `0.028247`
- 20d: sample `80`, hit `0.575`, avg `0.0036`, median `0.010656`, mae `0.042752`
- 60d: sample `80`, hit `0.5625`, avg `0.014634`, median `0.02283`, mae `0.065371`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.675`, avg `0.003808`, median `0.00558`, mae `0.014461`
- 5d: sample `80`, hit `0.575`, avg `0.002807`, median `0.001654`, mae `0.018442`
- 10d: sample `80`, hit `0.5125`, avg `0.003161`, median `0.004304`, mae `0.028247`
- 20d: sample `80`, hit `0.575`, avg `0.0036`, median `0.010656`, mae `0.042752`
- 60d: sample `80`, hit `0.5625`, avg `0.014634`, median `0.02283`, mae `0.065371`

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
