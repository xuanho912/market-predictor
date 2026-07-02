# High Confidence Edge Report

Generated at: `2026-07-02T23:42:32.556791+00:00`

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
- 3d: sample `60`, hit `0.4167`, avg `-0.002292`, median `-0.003036`, mae `0.014712`
- 5d: sample `60`, hit `0.4167`, avg `-0.005256`, median `-0.006511`, mae `0.018718`
- 10d: sample `60`, hit `0.4833`, avg `0.001446`, median `-0.0004`, mae `0.021772`
- 20d: sample `60`, hit `0.6333`, avg `0.010524`, median `0.01128`, mae `0.029703`
- 60d: sample `60`, hit `0.5833`, avg `0.02446`, median `0.037425`, mae `0.066109`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.00345`, median `-0.002789`, mae `0.008543`
- 5d: sample `20`, hit `0.6`, avg `0.000693`, median `0.003714`, mae `0.010826`
- 10d: sample `20`, hit `0.55`, avg `0.002697`, median `0.002362`, mae `0.009865`
- 20d: sample `20`, hit `0.7`, avg `0.009802`, median `0.015404`, mae `0.021176`
- 60d: sample `20`, hit `0.3`, avg `-0.032019`, median `-0.03635`, mae `0.05102`

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
- 3d: sample `8`, hit `0.25`, avg `-0.01179`, median `-0.010094`, mae `0.020033`
- 5d: sample `8`, hit `0.375`, avg `-0.012668`, median `-0.022865`, mae `0.023696`
- 10d: sample `8`, hit `0.25`, avg `-0.004832`, median `-0.005891`, mae `0.015734`
- 20d: sample `8`, hit `0.75`, avg `0.030838`, median `0.043456`, mae `0.039268`
- 60d: sample `8`, hit `0.75`, avg `0.063648`, median `0.099838`, mae `0.085368`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.01179`, median `-0.010094`, mae `0.020033`
- 5d: sample `8`, hit `0.375`, avg `-0.012668`, median `-0.022865`, mae `0.023696`
- 10d: sample `8`, hit `0.25`, avg `-0.004832`, median `-0.005891`, mae `0.015734`
- 20d: sample `8`, hit `0.75`, avg `0.030838`, median `0.043456`, mae `0.039268`
- 60d: sample `8`, hit `0.75`, avg `0.063648`, median `0.099838`, mae `0.085368`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4167, 'avg_return': -0.002292, 'median_return': -0.003036, 'mean_absolute_return': 0.014712, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.044644}, '5d': {'sample_size': 60, 'hit_rate': 0.4167, 'avg_return': -0.005256, 'median_return': -0.006511, 'mean_absolute_return': 0.018718, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': 0.001446, 'median_return': -0.0004, 'mean_absolute_return': 0.021772, 'max_adverse_excursion': -0.060333, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.010524, 'median_return': 0.01128, 'mean_absolute_return': 0.029703, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.083836}, '60d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.02446, 'median_return': 0.037425, 'mean_absolute_return': 0.066109, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.270957}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.01179, 'median_return': -0.010094, 'mean_absolute_return': 0.020033, 'max_adverse_excursion': -0.033992, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.012668, 'median_return': -0.022865, 'mean_absolute_return': 0.023696, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.004832, 'median_return': -0.005891, 'mean_absolute_return': 0.015734, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.030838, 'median_return': 0.043456, 'mean_absolute_return': 0.039268, 'max_adverse_excursion': -0.02149, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.063648, 'median_return': 0.099838, 'mean_absolute_return': 0.085368, 'max_adverse_excursion': -0.055789, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.001558, 'median_return': -0.002789, 'mean_absolute_return': 0.012407, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.044644}, '5d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.00278, 'median_return': -0.001796, 'mean_absolute_return': 0.015973, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.002491, 'median_return': 0.001607, 'mean_absolute_return': 0.019136, 'max_adverse_excursion': -0.060333, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.008066, 'median_return': 0.01128, 'mean_absolute_return': 0.026272, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.083836}, '60d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': 0.004417, 'median_return': -0.001675, 'mean_absolute_return': 0.059778, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.270957}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.475}, '5d': {'sample_size': 80, 'hit_rate': 0.4125}, '10d': {'sample_size': 80, 'hit_rate': 0.475}, '20d': {'sample_size': 80, 'hit_rate': 0.55}, '60d': {'sample_size': 80, 'hit_rate': 0.6125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.375, 'primary_minus_secondary': 0.1, 'both_hit': 14, 'both_miss': 26}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': -0.05, 'both_hit': 15, 'both_miss': 25}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.05, 'both_hit': 16, 'both_miss': 24}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': 0.025, 'both_hit': 23, 'both_miss': 17}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': 0.075, 'both_hit': 26, 'both_miss': 14}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.4, 'avg_return': -0.002581, 'median_return': -0.003036, 'mean_absolute_return': 0.013169, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.044644}, '5d': {'sample_size': 80, 'hit_rate': 0.4625, 'avg_return': -0.003769, 'median_return': -0.002002, 'mean_absolute_return': 0.016745, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 80, 'hit_rate': 0.5, 'avg_return': 0.001759, 'median_return': 0.000197, 'mean_absolute_return': 0.018795, 'max_adverse_excursion': -0.060333, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.010343, 'median_return': 0.012291, 'mean_absolute_return': 0.027571, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.083836}, '60d': {'sample_size': 80, 'hit_rate': 0.5125, 'avg_return': 0.01034, 'median_return': 0.007399, 'mean_absolute_return': 0.062337, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.270957}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4167`, avg `-0.002292`, median `-0.003036`, mae `0.014712`
- 5d: sample `60`, hit `0.4167`, avg `-0.005256`, median `-0.006511`, mae `0.018718`
- 10d: sample `60`, hit `0.4833`, avg `0.001446`, median `-0.0004`, mae `0.021772`
- 20d: sample `60`, hit `0.6333`, avg `0.010524`, median `0.01128`, mae `0.029703`
- 60d: sample `60`, hit `0.5833`, avg `0.02446`, median `0.037425`, mae `0.066109`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.00345`, median `-0.002789`, mae `0.008543`
- 5d: sample `20`, hit `0.6`, avg `0.000693`, median `0.003714`, mae `0.010826`
- 10d: sample `20`, hit `0.55`, avg `0.002697`, median `0.002362`, mae `0.009865`
- 20d: sample `20`, hit `0.7`, avg `0.009802`, median `0.015404`, mae `0.021176`
- 60d: sample `20`, hit `0.3`, avg `-0.032019`, median `-0.03635`, mae `0.05102`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4167`, avg `-0.002292`, median `-0.003036`, mae `0.014712`
- 5d: sample `60`, hit `0.4167`, avg `-0.005256`, median `-0.006511`, mae `0.018718`
- 10d: sample `60`, hit `0.4833`, avg `0.001446`, median `-0.0004`, mae `0.021772`
- 20d: sample `60`, hit `0.6333`, avg `0.010524`, median `0.01128`, mae `0.029703`
- 60d: sample `60`, hit `0.5833`, avg `0.02446`, median `0.037425`, mae `0.066109`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.35`, avg `-0.005196`, median `-0.005568`, mae `0.014738`
- 5d: sample `40`, hit `0.375`, avg `-0.008874`, median `-0.006511`, mae `0.017752`
- 10d: sample `40`, hit `0.4`, avg `-0.001052`, median `-0.006017`, mae `0.01835`
- 20d: sample `40`, hit `0.575`, avg `0.010738`, median `0.010788`, mae `0.029715`
- 60d: sample `40`, hit `0.65`, avg `0.035021`, median `0.059131`, mae `0.07351`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.4167`, avg `-0.002292`, median `-0.003036`, mae `0.014712`
- 5d: sample `60`, hit `0.4167`, avg `-0.005256`, median `-0.006511`, mae `0.018718`
- 10d: sample `60`, hit `0.4833`, avg `0.001446`, median `-0.0004`, mae `0.021772`
- 20d: sample `60`, hit `0.6333`, avg `0.010524`, median `0.01128`, mae `0.029703`
- 60d: sample `60`, hit `0.5833`, avg `0.02446`, median `0.037425`, mae `0.066109`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.35`, avg `-0.005196`, median `-0.005568`, mae `0.014738`
- 5d: sample `40`, hit `0.375`, avg `-0.008874`, median `-0.006511`, mae `0.017752`
- 10d: sample `40`, hit `0.4`, avg `-0.001052`, median `-0.006017`, mae `0.01835`
- 20d: sample `40`, hit `0.575`, avg `0.010738`, median `0.010788`, mae `0.029715`
- 60d: sample `40`, hit `0.65`, avg `0.035021`, median `0.059131`, mae `0.07351`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.00345`, median `-0.002789`, mae `0.008543`
- 5d: sample `20`, hit `0.6`, avg `0.000693`, median `0.003714`, mae `0.010826`
- 10d: sample `20`, hit `0.55`, avg `0.002697`, median `0.002362`, mae `0.009865`
- 20d: sample `20`, hit `0.7`, avg `0.009802`, median `0.015404`, mae `0.021176`
- 60d: sample `20`, hit `0.3`, avg `-0.032019`, median `-0.03635`, mae `0.05102`

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
- 3d: sample `60`, hit `0.4167`, avg `-0.002292`, median `-0.003036`, mae `0.014712`
- 5d: sample `60`, hit `0.4167`, avg `-0.005256`, median `-0.006511`, mae `0.018718`
- 10d: sample `60`, hit `0.4833`, avg `0.001446`, median `-0.0004`, mae `0.021772`
- 20d: sample `60`, hit `0.6333`, avg `0.010524`, median `0.01128`, mae `0.029703`
- 60d: sample `60`, hit `0.5833`, avg `0.02446`, median `0.037425`, mae `0.066109`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.00345`, median `-0.002789`, mae `0.008543`
- 5d: sample `20`, hit `0.6`, avg `0.000693`, median `0.003714`, mae `0.010826`
- 10d: sample `20`, hit `0.55`, avg `0.002697`, median `0.002362`, mae `0.009865`
- 20d: sample `20`, hit `0.7`, avg `0.009802`, median `0.015404`, mae `0.021176`
- 60d: sample `20`, hit `0.3`, avg `-0.032019`, median `-0.03635`, mae `0.05102`

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
- 3d: sample `80`, hit `0.4`, avg `-0.002581`, median `-0.003036`, mae `0.013169`
- 5d: sample `80`, hit `0.4625`, avg `-0.003769`, median `-0.002002`, mae `0.016745`
- 10d: sample `80`, hit `0.5`, avg `0.001759`, median `0.000197`, mae `0.018795`
- 20d: sample `80`, hit `0.65`, avg `0.010343`, median `0.012291`, mae `0.027571`
- 60d: sample `80`, hit `0.5125`, avg `0.01034`, median `0.007399`, mae `0.062337`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4`, avg `-0.002581`, median `-0.003036`, mae `0.013169`
- 5d: sample `80`, hit `0.4625`, avg `-0.003769`, median `-0.002002`, mae `0.016745`
- 10d: sample `80`, hit `0.5`, avg `0.001759`, median `0.000197`, mae `0.018795`
- 20d: sample `80`, hit `0.65`, avg `0.010343`, median `0.012291`, mae `0.027571`
- 60d: sample `80`, hit `0.5125`, avg `0.01034`, median `0.007399`, mae `0.062337`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.4167`, avg `-0.002292`, median `-0.003036`, mae `0.014712`
- 5d: sample `60`, hit `0.4167`, avg `-0.005256`, median `-0.006511`, mae `0.018718`
- 10d: sample `60`, hit `0.4833`, avg `0.001446`, median `-0.0004`, mae `0.021772`
- 20d: sample `60`, hit `0.6333`, avg `0.010524`, median `0.01128`, mae `0.029703`
- 60d: sample `60`, hit `0.5833`, avg `0.02446`, median `0.037425`, mae `0.066109`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.4167`, avg `-0.002292`, median `-0.003036`, mae `0.014712`
- 5d: sample `60`, hit `0.4167`, avg `-0.005256`, median `-0.006511`, mae `0.018718`
- 10d: sample `60`, hit `0.4833`, avg `0.001446`, median `-0.0004`, mae `0.021772`
- 20d: sample `60`, hit `0.6333`, avg `0.010524`, median `0.01128`, mae `0.029703`
- 60d: sample `60`, hit `0.5833`, avg `0.02446`, median `0.037425`, mae `0.066109`

### risk_path_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.00345`, median `-0.002789`, mae `0.008543`
- 5d: sample `20`, hit `0.6`, avg `0.000693`, median `0.003714`, mae `0.010826`
- 10d: sample `20`, hit `0.55`, avg `0.002697`, median `0.002362`, mae `0.009865`
- 20d: sample `20`, hit `0.7`, avg `0.009802`, median `0.015404`, mae `0.021176`
- 60d: sample `20`, hit `0.3`, avg `-0.032019`, median `-0.03635`, mae `0.05102`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
