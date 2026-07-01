# High Confidence Edge Report

Generated at: `2026-07-01T23:55:30.574601+00:00`

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
- 3d: sample `60`, hit `0.4333`, avg `-0.003518`, median `-0.003036`, mae `0.013794`
- 5d: sample `60`, hit `0.4333`, avg `-0.005997`, median `-0.004438`, mae `0.017807`
- 10d: sample `60`, hit `0.4667`, avg `-7.7e-05`, median `-0.001932`, mae `0.020104`
- 20d: sample `60`, hit `0.65`, avg `0.007743`, median `0.010788`, mae `0.028936`
- 60d: sample `60`, hit `0.5333`, avg `0.01891`, median `0.012273`, mae `0.062061`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.2`, avg `-0.007043`, median `-0.007923`, mae `0.010014`
- 5d: sample `20`, hit `0.5`, avg `-0.005437`, median `0.001695`, mae `0.014035`
- 10d: sample `20`, hit `0.45`, avg `-0.005011`, median `-0.001676`, mae `0.014709`
- 20d: sample `20`, hit `0.6`, avg `-0.002027`, median `0.011728`, mae `0.027093`
- 60d: sample `20`, hit `0.25`, avg `-0.029323`, median `-0.03023`, mae `0.046744`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4333, 'avg_return': -0.003518, 'median_return': -0.003036, 'mean_absolute_return': 0.013794, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.044644}, '5d': {'sample_size': 60, 'hit_rate': 0.4333, 'avg_return': -0.005997, 'median_return': -0.004438, 'mean_absolute_return': 0.017807, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.036593}, '10d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -7.7e-05, 'median_return': -0.001932, 'mean_absolute_return': 0.020104, 'max_adverse_excursion': -0.060333, 'max_favorable_excursion': 0.056454}, '20d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.007743, 'median_return': 0.010788, 'mean_absolute_return': 0.028936, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.083836}, '60d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.01891, 'median_return': 0.012273, 'mean_absolute_return': 0.062061, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.270957}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.01179, 'median_return': -0.010094, 'mean_absolute_return': 0.020033, 'max_adverse_excursion': -0.033992, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.012668, 'median_return': -0.022865, 'mean_absolute_return': 0.023696, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.004832, 'median_return': -0.005891, 'mean_absolute_return': 0.015734, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.030838, 'median_return': 0.043456, 'mean_absolute_return': 0.039268, 'max_adverse_excursion': -0.02149, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.063648, 'median_return': 0.099838, 'mean_absolute_return': 0.085368, 'max_adverse_excursion': -0.055789, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': -0.003578, 'median_return': -0.005417, 'mean_absolute_return': 0.012051, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.044644}, '5d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': -0.005101, 'median_return': -0.002002, 'mean_absolute_return': 0.016105, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.036593}, '10d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.000919, 'median_return': -0.001676, 'mean_absolute_return': 0.019091, 'max_adverse_excursion': -0.081978, 'max_favorable_excursion': 0.056454}, '20d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.002463, 'median_return': 0.007676, 'mean_absolute_return': 0.027276, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.083836}, '60d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': 0.000541, 'median_return': -0.009954, 'mean_absolute_return': 0.055217, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.270957}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.45}, '10d': {'sample_size': 80, 'hit_rate': 0.4875}, '20d': {'sample_size': 80, 'hit_rate': 0.5875}, '60d': {'sample_size': 80, 'hit_rate': 0.5875}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.3, 'primary_minus_secondary': 0.225, 'both_hit': 13, 'both_miss': 27}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.4, 'primary_minus_secondary': 0.05, 'both_hit': 14, 'both_miss': 26}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.05, 'both_hit': 17, 'both_miss': 23}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': 0.05, 'both_hit': 25, 'both_miss': 15}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': 0.025, 'both_hit': 26, 'both_miss': 14}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.002402, 'median_return': 0.003924, 'mean_absolute_return': 0.01092, 'max_adverse_excursion': -0.017591, 'max_favorable_excursion': 0.022897}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.001283, 'median_return': 0.005876, 'mean_absolute_return': 0.016568, 'max_adverse_excursion': -0.030861, 'max_favorable_excursion': 0.034374}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.001218, 'median_return': 0.005417, 'mean_absolute_return': 0.022871, 'max_adverse_excursion': -0.039317, 'max_favorable_excursion': 0.042758}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': -0.004696, 'median_return': 0.007676, 'mean_absolute_return': 0.026974, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.048732}, '60d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.016663, 'median_return': -0.01215, 'mean_absolute_return': 0.040778, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.071905}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.2833, 'avg_return': -0.006666, 'median_return': -0.006734, 'mean_absolute_return': 0.013492, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.044644}, '5d': {'sample_size': 60, 'hit_rate': 0.4, 'avg_return': -0.008237, 'median_return': -0.004438, 'mean_absolute_return': 0.016963, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.036593}, '10d': {'sample_size': 60, 'hit_rate': 0.4333, 'avg_return': -0.001341, 'median_return': -0.004918, 'mean_absolute_return': 0.017383, 'max_adverse_excursion': -0.081978, 'max_favorable_excursion': 0.056454}, '20d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.008632, 'median_return': 0.012291, 'mean_absolute_return': 0.028976, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.083836}, '60d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': 0.014689, 'median_return': 0.018072, 'mean_absolute_return': 0.06405, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.270957}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.003518`, median `-0.003036`, mae `0.013794`
- 5d: sample `60`, hit `0.4333`, avg `-0.005997`, median `-0.004438`, mae `0.017807`
- 10d: sample `60`, hit `0.4667`, avg `-7.7e-05`, median `-0.001932`, mae `0.020104`
- 20d: sample `60`, hit `0.65`, avg `0.007743`, median `0.010788`, mae `0.028936`
- 60d: sample `60`, hit `0.5333`, avg `0.01891`, median `0.012273`, mae `0.062061`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.2`, avg `-0.007043`, median `-0.007923`, mae `0.010014`
- 5d: sample `20`, hit `0.5`, avg `-0.005437`, median `0.001695`, mae `0.014035`
- 10d: sample `20`, hit `0.45`, avg `-0.005011`, median `-0.001676`, mae `0.014709`
- 20d: sample `20`, hit `0.6`, avg `-0.002027`, median `0.011728`, mae `0.027093`
- 60d: sample `20`, hit `0.25`, avg `-0.029323`, median `-0.03023`, mae `0.046744`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.003518`, median `-0.003036`, mae `0.013794`
- 5d: sample `60`, hit `0.4333`, avg `-0.005997`, median `-0.004438`, mae `0.017807`
- 10d: sample `60`, hit `0.4667`, avg `-7.7e-05`, median `-0.001932`, mae `0.020104`
- 20d: sample `60`, hit `0.65`, avg `0.007743`, median `0.010788`, mae `0.028936`
- 60d: sample `60`, hit `0.5333`, avg `0.01891`, median `0.012273`, mae `0.062061`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.003518`, median `-0.003036`, mae `0.013794`
- 5d: sample `60`, hit `0.4333`, avg `-0.005997`, median `-0.004438`, mae `0.017807`
- 10d: sample `60`, hit `0.4667`, avg `-7.7e-05`, median `-0.001932`, mae `0.020104`
- 20d: sample `60`, hit `0.65`, avg `0.007743`, median `0.010788`, mae `0.028936`
- 60d: sample `60`, hit `0.5333`, avg `0.01891`, median `0.012273`, mae `0.062061`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.003518`, median `-0.003036`, mae `0.013794`
- 5d: sample `60`, hit `0.4333`, avg `-0.005997`, median `-0.004438`, mae `0.017807`
- 10d: sample `60`, hit `0.4667`, avg `-7.7e-05`, median `-0.001932`, mae `0.020104`
- 20d: sample `60`, hit `0.65`, avg `0.007743`, median `0.010788`, mae `0.028936`
- 60d: sample `60`, hit `0.5333`, avg `0.01891`, median `0.012273`, mae `0.062061`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.003518`, median `-0.003036`, mae `0.013794`
- 5d: sample `60`, hit `0.4333`, avg `-0.005997`, median `-0.004438`, mae `0.017807`
- 10d: sample `60`, hit `0.4667`, avg `-7.7e-05`, median `-0.001932`, mae `0.020104`
- 20d: sample `60`, hit `0.65`, avg `0.007743`, median `0.010788`, mae `0.028936`
- 60d: sample `60`, hit `0.5333`, avg `0.01891`, median `0.012273`, mae `0.062061`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.2`, avg `-0.007043`, median `-0.007923`, mae `0.010014`
- 5d: sample `20`, hit `0.5`, avg `-0.005437`, median `0.001695`, mae `0.014035`
- 10d: sample `20`, hit `0.45`, avg `-0.005011`, median `-0.001676`, mae `0.014709`
- 20d: sample `20`, hit `0.6`, avg `-0.002027`, median `0.011728`, mae `0.027093`
- 60d: sample `20`, hit `0.25`, avg `-0.029323`, median `-0.03023`, mae `0.046744`

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
- 3d: sample `60`, hit `0.4333`, avg `-0.003518`, median `-0.003036`, mae `0.013794`
- 5d: sample `60`, hit `0.4333`, avg `-0.005997`, median `-0.004438`, mae `0.017807`
- 10d: sample `60`, hit `0.4667`, avg `-7.7e-05`, median `-0.001932`, mae `0.020104`
- 20d: sample `60`, hit `0.65`, avg `0.007743`, median `0.010788`, mae `0.028936`
- 60d: sample `60`, hit `0.5333`, avg `0.01891`, median `0.012273`, mae `0.062061`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.2`, avg `-0.007043`, median `-0.007923`, mae `0.010014`
- 5d: sample `20`, hit `0.5`, avg `-0.005437`, median `0.001695`, mae `0.014035`
- 10d: sample `20`, hit `0.45`, avg `-0.005011`, median `-0.001676`, mae `0.014709`
- 20d: sample `20`, hit `0.6`, avg `-0.002027`, median `0.011728`, mae `0.027093`
- 60d: sample `20`, hit `0.25`, avg `-0.029323`, median `-0.03023`, mae `0.046744`

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
- 3d: sample `80`, hit `0.375`, avg `-0.004399`, median `-0.005568`, mae `0.012849`
- 5d: sample `80`, hit `0.45`, avg `-0.005857`, median `-0.004123`, mae `0.016864`
- 10d: sample `80`, hit `0.4625`, avg `-0.00131`, median `-0.001932`, mae `0.018755`
- 20d: sample `80`, hit `0.6375`, avg `0.0053`, median `0.010788`, mae `0.028475`
- 60d: sample `80`, hit `0.4625`, avg `0.006851`, median `-0.005523`, mae `0.058232`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.003518`, median `-0.003036`, mae `0.013794`
- 5d: sample `60`, hit `0.4333`, avg `-0.005997`, median `-0.004438`, mae `0.017807`
- 10d: sample `60`, hit `0.4667`, avg `-7.7e-05`, median `-0.001932`, mae `0.020104`
- 20d: sample `60`, hit `0.65`, avg `0.007743`, median `0.010788`, mae `0.028936`
- 60d: sample `60`, hit `0.5333`, avg `0.01891`, median `0.012273`, mae `0.062061`

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
