# High Confidence Edge Report

Generated at: `2026-08-27T04:07:53.224046+00:00`

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
- 3d: sample `60`, hit `0.5833`, avg `0.002297`, median `0.002329`, mae `0.01544`
- 5d: sample `60`, hit `0.4833`, avg `-0.000468`, median `-0.000996`, mae `0.019765`
- 10d: sample `60`, hit `0.55`, avg `0.006299`, median `0.009031`, mae `0.028821`
- 20d: sample `60`, hit `0.6333`, avg `0.009621`, median `0.020226`, mae `0.043648`
- 60d: sample `60`, hit `0.7`, avg `0.040136`, median `0.046132`, mae `0.069983`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002759`, median `0.003952`, mae `0.013625`
- 5d: sample `20`, hit `0.6`, avg `0.002148`, median `0.005327`, mae `0.017604`
- 10d: sample `20`, hit `0.45`, avg `-0.0051`, median `-0.010563`, mae `0.02718`
- 20d: sample `20`, hit `0.65`, avg `-0.001974`, median `0.017881`, mae `0.04084`
- 60d: sample `20`, hit `0.65`, avg `0.010806`, median `0.010071`, mae `0.057005`

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
- 3d: sample `8`, hit `0.625`, avg `-0.00267`, median `0.00234`, mae `0.009443`
- 5d: sample `8`, hit `0.375`, avg `-0.005701`, median `-0.012956`, mae `0.016957`
- 10d: sample `8`, hit `0.75`, avg `0.010786`, median `0.020918`, mae `0.020347`
- 20d: sample `8`, hit `0.875`, avg `0.019767`, median `0.029166`, mae `0.021663`
- 60d: sample `8`, hit `0.75`, avg `0.04575`, median `0.059495`, mae `0.060358`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.00267`, median `0.00234`, mae `0.009443`
- 5d: sample `8`, hit `0.375`, avg `-0.005701`, median `-0.012956`, mae `0.016957`
- 10d: sample `8`, hit `0.75`, avg `0.010786`, median `0.020918`, mae `0.020347`
- 20d: sample `8`, hit `0.875`, avg `0.019767`, median `0.029166`, mae `0.021663`
- 60d: sample `8`, hit `0.75`, avg `0.04575`, median `0.059495`, mae `0.060358`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.002297, 'median_return': 0.002329, 'mean_absolute_return': 0.01544, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': -0.000468, 'median_return': -0.000996, 'mean_absolute_return': 0.019765, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.006299, 'median_return': 0.009031, 'mean_absolute_return': 0.028821, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.009621, 'median_return': 0.020226, 'mean_absolute_return': 0.043648, 'max_adverse_excursion': -0.136294, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.040136, 'median_return': 0.046132, 'mean_absolute_return': 0.069983, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.19145}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.00267, 'median_return': 0.00234, 'mean_absolute_return': 0.009443, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.01018}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.005701, 'median_return': -0.012956, 'mean_absolute_return': 0.016957, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.010786, 'median_return': 0.020918, 'mean_absolute_return': 0.020347, 'max_adverse_excursion': -0.020281, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.019767, 'median_return': 0.029166, 'mean_absolute_return': 0.021663, 'max_adverse_excursion': -0.007581, 'max_favorable_excursion': 0.033999}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.04575, 'median_return': 0.059495, 'mean_absolute_return': 0.060358, 'max_adverse_excursion': -0.038302, 'max_favorable_excursion': 0.101282}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.002977, 'median_return': 0.003026, 'mean_absolute_return': 0.015603, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.00084, 'median_return': 0.000688, 'mean_absolute_return': 0.019477, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': 0.002634, 'median_return': 0.002558, 'mean_absolute_return': 0.029307, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.005273, 'median_return': 0.016109, 'mean_absolute_return': 0.045311, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.031365, 'median_return': 0.032982, 'mean_absolute_return': 0.067447, 'max_adverse_excursion': -0.15249, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5875}, '5d': {'sample_size': 80, 'hit_rate': 0.5125}, '10d': {'sample_size': 80, 'hit_rate': 0.525}, '20d': {'sample_size': 80, 'hit_rate': 0.6375}, '60d': {'sample_size': 80, 'hit_rate': 0.6875}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.1, 'both_hit': 23, 'both_miss': 17}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.05, 'both_hit': 19, 'both_miss': 21}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.075, 'both_hit': 25, 'both_miss': 15}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': 0.075, 'both_hit': 28, 'both_miss': 12}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.1, 'both_hit': 31, 'both_miss': 9}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.002413, 'median_return': 0.002889, 'mean_absolute_return': 0.014987, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 80, 'hit_rate': 0.5125, 'avg_return': 0.000186, 'median_return': 0.000579, 'mean_absolute_return': 0.019225, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.525, 'avg_return': 0.003449, 'median_return': 0.00479, 'mean_absolute_return': 0.028411, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.006722, 'median_return': 0.017881, 'mean_absolute_return': 0.042946, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': 0.032804, 'median_return': 0.034688, 'mean_absolute_return': 0.066738, 'max_adverse_excursion': -0.15249, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.00141`, median `0.001448`, mae `0.011351`
- 5d: sample `40`, hit `0.475`, avg `-0.004956`, median `-0.004989`, mae `0.013705`
- 10d: sample `40`, hit `0.525`, avg `0.001439`, median `0.00479`, mae `0.021131`
- 20d: sample `40`, hit `0.625`, avg `0.00318`, median `0.020226`, mae `0.034958`
- 60d: sample `40`, hit `0.6`, avg `0.018678`, median `0.03283`, mae `0.06132`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.00554`, median `0.005581`, mae `0.016299`
- 5d: sample `40`, hit `0.5`, avg `0.00164`, median `0.000579`, mae `0.021612`
- 10d: sample `40`, hit `0.5`, avg `0.004784`, median `0.002558`, mae `0.032539`
- 20d: sample `40`, hit `0.575`, avg `0.004676`, median `0.012337`, mae `0.049202`
- 60d: sample `40`, hit `0.725`, avg `0.046424`, median `0.059829`, mae `0.073018`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.00141`, median `0.001448`, mae `0.011351`
- 5d: sample `40`, hit `0.475`, avg `-0.004956`, median `-0.004989`, mae `0.013705`
- 10d: sample `40`, hit `0.525`, avg `0.001439`, median `0.00479`, mae `0.021131`
- 20d: sample `40`, hit `0.625`, avg `0.00318`, median `0.020226`, mae `0.034958`
- 60d: sample `40`, hit `0.6`, avg `0.018678`, median `0.03283`, mae `0.06132`

### breadth_conflicted_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.00554`, median `0.005581`, mae `0.016299`
- 5d: sample `40`, hit `0.5`, avg `0.00164`, median `0.000579`, mae `0.021612`
- 10d: sample `40`, hit `0.5`, avg `0.004784`, median `0.002558`, mae `0.032539`
- 20d: sample `40`, hit `0.575`, avg `0.004676`, median `0.012337`, mae `0.049202`
- 60d: sample `40`, hit `0.725`, avg `0.046424`, median `0.059829`, mae `0.073018`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.004188`, median `0.001448`, mae `0.013724`
- 5d: sample `20`, hit `0.45`, avg `-0.004685`, median `-0.004989`, mae `0.016072`
- 10d: sample `20`, hit `0.65`, avg `0.00933`, median `0.018754`, mae `0.021384`
- 20d: sample `20`, hit `0.75`, avg `0.019512`, median `0.031196`, mae `0.032539`
- 60d: sample `20`, hit `0.65`, avg `0.027561`, median `0.034688`, mae `0.063913`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.009712`, median `0.014223`, mae `0.023619`
- 5d: sample `20`, hit `0.5`, avg `0.008509`, median `0.018242`, mae `0.031886`
- 10d: sample `20`, hit `0.6`, avg `0.01602`, median `0.021169`, mae `0.0442`
- 20d: sample `20`, hit `0.65`, avg `0.022502`, median `0.023289`, mae `0.061027`
- 60d: sample `20`, hit `0.9`, avg `0.083054`, median `0.079427`, mae `0.087309`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.00141`, median `0.001448`, mae `0.011351`
- 5d: sample `40`, hit `0.475`, avg `-0.004956`, median `-0.004989`, mae `0.013705`
- 10d: sample `40`, hit `0.525`, avg `0.001439`, median `0.00479`, mae `0.021131`
- 20d: sample `40`, hit `0.625`, avg `0.00318`, median `0.020226`, mae `0.034958`
- 60d: sample `40`, hit `0.6`, avg `0.018678`, median `0.03283`, mae `0.06132`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.006235`, median `0.00979`, mae `0.018622`
- 5d: sample `40`, hit `0.55`, avg `0.005328`, median `0.005327`, mae `0.024745`
- 10d: sample `40`, hit `0.525`, avg `0.00546`, median `0.009955`, mae `0.03569`
- 20d: sample `40`, hit `0.65`, avg `0.010264`, median `0.017881`, mae `0.050933`
- 60d: sample `40`, hit `0.775`, avg `0.04693`, median `0.052998`, mae `0.072157`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.004188`, median `0.001448`, mae `0.013724`
- 5d: sample `20`, hit `0.45`, avg `-0.004685`, median `-0.004989`, mae `0.016072`
- 10d: sample `20`, hit `0.65`, avg `0.00933`, median `0.018754`, mae `0.021384`
- 20d: sample `20`, hit `0.75`, avg `0.019512`, median `0.031196`, mae `0.032539`
- 60d: sample `20`, hit `0.65`, avg `0.027561`, median `0.034688`, mae `0.063913`

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
- 3d: sample `80`, hit `0.5875`, avg `0.002413`, median `0.002889`, mae `0.014987`
- 5d: sample `80`, hit `0.5125`, avg `0.000186`, median `0.000579`, mae `0.019225`
- 10d: sample `80`, hit `0.525`, avg `0.003449`, median `0.00479`, mae `0.028411`
- 20d: sample `80`, hit `0.6375`, avg `0.006722`, median `0.017881`, mae `0.042946`
- 60d: sample `80`, hit `0.6875`, avg `0.032804`, median `0.034688`, mae `0.066738`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.002413`, median `0.002889`, mae `0.014987`
- 5d: sample `80`, hit `0.5125`, avg `0.000186`, median `0.000579`, mae `0.019225`
- 10d: sample `80`, hit `0.525`, avg `0.003449`, median `0.00479`, mae `0.028411`
- 20d: sample `80`, hit `0.6375`, avg `0.006722`, median `0.017881`, mae `0.042946`
- 60d: sample `80`, hit `0.6875`, avg `0.032804`, median `0.034688`, mae `0.066738`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.002413`, median `0.002889`, mae `0.014987`
- 5d: sample `80`, hit `0.5125`, avg `0.000186`, median `0.000579`, mae `0.019225`
- 10d: sample `80`, hit `0.525`, avg `0.003449`, median `0.00479`, mae `0.028411`
- 20d: sample `80`, hit `0.6375`, avg `0.006722`, median `0.017881`, mae `0.042946`
- 60d: sample `80`, hit `0.6875`, avg `0.032804`, median `0.034688`, mae `0.066738`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.002413`, median `0.002889`, mae `0.014987`
- 5d: sample `80`, hit `0.5125`, avg `0.000186`, median `0.000579`, mae `0.019225`
- 10d: sample `80`, hit `0.525`, avg `0.003449`, median `0.00479`, mae `0.028411`
- 20d: sample `80`, hit `0.6375`, avg `0.006722`, median `0.017881`, mae `0.042946`
- 60d: sample `80`, hit `0.6875`, avg `0.032804`, median `0.034688`, mae `0.066738`

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
