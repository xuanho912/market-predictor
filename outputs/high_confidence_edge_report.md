# High Confidence Edge Report

Generated at: `2026-07-15T06:01:19.752355+00:00`

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
- 3d: sample `40`, hit `0.625`, avg `0.000145`, median `0.004573`, mae `0.014402`
- 5d: sample `40`, hit `0.55`, avg `0.000872`, median `0.006036`, mae `0.020104`
- 10d: sample `40`, hit `0.725`, avg `0.011217`, median `0.013307`, mae `0.02384`
- 20d: sample `40`, hit `0.85`, avg `0.021911`, median `0.02865`, mae `0.031276`
- 60d: sample `40`, hit `0.75`, avg `0.037403`, median `0.056874`, mae `0.065696`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.004768`, median `0.012355`, mae `0.018593`
- 5d: sample `40`, hit `0.55`, avg `0.006502`, median `0.007948`, mae `0.021771`
- 10d: sample `40`, hit `0.65`, avg `0.012769`, median `0.013997`, mae `0.024964`
- 20d: sample `40`, hit `0.925`, avg `0.036373`, median `0.032102`, mae `0.037701`
- 60d: sample `40`, hit `0.75`, avg `0.054583`, median `0.0765`, mae `0.073331`

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
- 3d: sample `8`, hit `0.375`, avg `-0.004536`, median `-0.0002`, mae `0.018959`
- 5d: sample `8`, hit `0.375`, avg `-0.006532`, median `-0.007916`, mae `0.026323`
- 10d: sample `8`, hit `0.625`, avg `0.015225`, median `0.034277`, mae `0.038541`
- 20d: sample `8`, hit `0.75`, avg `0.018395`, median `0.030922`, mae `0.04333`
- 60d: sample `8`, hit `0.625`, avg `0.045345`, median `0.092892`, mae `0.084311`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.875`, avg `0.006714`, median `0.00745`, mae `0.011121`
- 5d: sample `8`, hit `0.75`, avg `0.010629`, median `0.012091`, mae `0.012707`
- 10d: sample `8`, hit `0.875`, avg `0.018505`, median `0.021584`, mae `0.018558`
- 20d: sample `8`, hit `1.0`, avg `0.029348`, median `0.029072`, mae `0.029348`
- 60d: sample `8`, hit `1.0`, avg `0.066603`, median `0.062103`, mae `0.066603`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.000145, 'median_return': 0.004573, 'mean_absolute_return': 0.014402, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.000872, 'median_return': 0.006036, 'mean_absolute_return': 0.020104, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.011217, 'median_return': 0.013307, 'mean_absolute_return': 0.02384, 'max_adverse_excursion': -0.057499, 'max_favorable_excursion': 0.067122}, '20d': {'sample_size': 40, 'hit_rate': 0.85, 'avg_return': 0.021911, 'median_return': 0.02865, 'mean_absolute_return': 0.031276, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.072047}, '60d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.037403, 'median_return': 0.056874, 'mean_absolute_return': 0.065696, 'max_adverse_excursion': -0.123656, 'max_favorable_excursion': 0.129489}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.006714, 'median_return': 0.00745, 'mean_absolute_return': 0.011121, 'max_adverse_excursion': -0.017627, 'max_favorable_excursion': 0.017982}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.010629, 'median_return': 0.012091, 'mean_absolute_return': 0.012707, 'max_adverse_excursion': -0.00428, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.018505, 'median_return': 0.021584, 'mean_absolute_return': 0.018558, 'max_adverse_excursion': -0.000214, 'max_favorable_excursion': 0.035149}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.029348, 'median_return': 0.029072, 'mean_absolute_return': 0.029348, 'max_adverse_excursion': 0.019193, 'max_favorable_excursion': 0.04151}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.066603, 'median_return': 0.062103, 'mean_absolute_return': 0.066603, 'max_adverse_excursion': 0.043741, 'max_favorable_excursion': 0.10629}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.001984, 'median_return': 0.004815, 'mean_absolute_return': 0.017095, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.002916, 'median_return': 0.00413, 'mean_absolute_return': 0.021852, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.011269, 'median_return': 0.013307, 'mean_absolute_return': 0.025051, 'max_adverse_excursion': -0.057499, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 72, 'hit_rate': 0.875, 'avg_return': 0.029119, 'median_return': 0.030922, 'mean_absolute_return': 0.03506, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.089661}, '60d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.043703, 'median_return': 0.068712, 'mean_absolute_return': 0.069837, 'max_adverse_excursion': -0.123656, 'max_favorable_excursion': 0.147808}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5125}, '5d': {'sample_size': 80, 'hit_rate': 0.5}, '10d': {'sample_size': 80, 'hit_rate': 0.5375}, '20d': {'sample_size': 80, 'hit_rate': 0.4625}, '60d': {'sample_size': 80, 'hit_rate': 0.5}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.1, 'both_hit': 25, 'both_miss': 15}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.05, 'both_hit': 22, 'both_miss': 18}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.15, 'both_hit': 29, 'both_miss': 11}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.8875, 'primary_minus_secondary': -0.425, 'both_hit': 34, 'both_miss': 6}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.75, 'primary_minus_secondary': -0.25, 'both_hit': 30, 'both_miss': 10}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.002457, 'median_return': 0.005804, 'mean_absolute_return': 0.016497, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 80, 'hit_rate': 0.55, 'avg_return': 0.003687, 'median_return': 0.006036, 'mean_absolute_return': 0.020938, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': 0.011993, 'median_return': 0.013648, 'mean_absolute_return': 0.024402, 'max_adverse_excursion': -0.057499, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 80, 'hit_rate': 0.8875, 'avg_return': 0.029142, 'median_return': 0.029298, 'mean_absolute_return': 0.034488, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.089661}, '60d': {'sample_size': 80, 'hit_rate': 0.75, 'avg_return': 0.045993, 'median_return': 0.06423, 'mean_absolute_return': 0.069513, 'max_adverse_excursion': -0.123656, 'max_favorable_excursion': 0.147808}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.003285`, median `0.006198`, mae `0.014716`
- 5d: sample `40`, hit `0.575`, avg `0.005137`, median `0.006036`, mae `0.018175`
- 10d: sample `40`, hit `0.7`, avg `0.010547`, median `0.012215`, mae `0.018344`
- 20d: sample `40`, hit `0.925`, avg `0.024869`, median `0.027885`, mae `0.026407`
- 60d: sample `40`, hit `0.75`, avg `0.038587`, median `0.046407`, mae `0.056077`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6667`, avg `0.004932`, median `0.007259`, mae `0.015217`
- 5d: sample `60`, hit `0.6167`, avg `0.007362`, median `0.008981`, mae `0.019121`
- 10d: sample `60`, hit `0.7167`, avg `0.013154`, median `0.013997`, mae `0.021571`
- 20d: sample `60`, hit `0.9333`, avg `0.03311`, median `0.03107`, mae `0.034312`
- 60d: sample `60`, hit `0.8167`, avg `0.054535`, median `0.068712`, mae `0.067727`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.005258`, median `0.006198`, mae `0.008464`
- 5d: sample `20`, hit `0.75`, avg `0.009082`, median `0.011604`, mae `0.013822`
- 10d: sample `20`, hit `0.85`, avg `0.013924`, median `0.014276`, mae `0.014784`
- 20d: sample `20`, hit `0.95`, avg `0.026583`, median `0.029072`, mae `0.027532`
- 60d: sample `20`, hit `0.95`, avg `0.054438`, median `0.059104`, mae `0.05652`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.005258`, median `0.006198`, mae `0.008464`
- 5d: sample `20`, hit `0.75`, avg `0.009082`, median `0.011604`, mae `0.013822`
- 10d: sample `20`, hit `0.85`, avg `0.013924`, median `0.014276`, mae `0.014784`
- 20d: sample `20`, hit `0.95`, avg `0.026583`, median `0.029072`, mae `0.027532`
- 60d: sample `20`, hit `0.95`, avg `0.054438`, median `0.059104`, mae `0.05652`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.003285`, median `0.006198`, mae `0.014716`
- 5d: sample `40`, hit `0.575`, avg `0.005137`, median `0.006036`, mae `0.018175`
- 10d: sample `40`, hit `0.7`, avg `0.010547`, median `0.012215`, mae `0.018344`
- 20d: sample `40`, hit `0.925`, avg `0.024869`, median `0.027885`, mae `0.026407`
- 60d: sample `40`, hit `0.75`, avg `0.038587`, median `0.046407`, mae `0.056077`

### breadth_conflicted_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6667`, avg `0.004932`, median `0.007259`, mae `0.015217`
- 5d: sample `60`, hit `0.6167`, avg `0.007362`, median `0.008981`, mae `0.019121`
- 10d: sample `60`, hit `0.7167`, avg `0.013154`, median `0.013997`, mae `0.021571`
- 20d: sample `60`, hit `0.9333`, avg `0.03311`, median `0.03107`, mae `0.034312`
- 60d: sample `60`, hit `0.8167`, avg `0.054535`, median `0.068712`, mae `0.067727`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.005258`, median `0.006198`, mae `0.008464`
- 5d: sample `20`, hit `0.75`, avg `0.009082`, median `0.011604`, mae `0.013822`
- 10d: sample `20`, hit `0.85`, avg `0.013924`, median `0.014276`, mae `0.014784`
- 20d: sample `20`, hit `0.95`, avg `0.026583`, median `0.029072`, mae `0.027532`
- 60d: sample `20`, hit `0.95`, avg `0.054438`, median `0.059104`, mae `0.05652`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.004968`, median `-0.0002`, mae `0.020339`
- 5d: sample `20`, hit `0.35`, avg `-0.007337`, median `-0.008895`, mae `0.026386`
- 10d: sample `20`, hit `0.6`, avg `0.00851`, median `0.013307`, mae `0.032896`
- 20d: sample `20`, hit `0.75`, avg `0.017238`, median `0.026005`, mae `0.035019`
- 60d: sample `20`, hit `0.55`, avg `0.020368`, median `0.056874`, mae `0.074873`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.003285`, median `0.006198`, mae `0.014716`
- 5d: sample `40`, hit `0.575`, avg `0.005137`, median `0.006036`, mae `0.018175`
- 10d: sample `40`, hit `0.7`, avg `0.010547`, median `0.012215`, mae `0.018344`
- 20d: sample `40`, hit `0.925`, avg `0.024869`, median `0.027885`, mae `0.026407`
- 60d: sample `40`, hit `0.75`, avg `0.038587`, median `0.046407`, mae `0.056077`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.004768`, median `0.012355`, mae `0.018593`
- 5d: sample `40`, hit `0.55`, avg `0.006502`, median `0.007948`, mae `0.021771`
- 10d: sample `40`, hit `0.65`, avg `0.012769`, median `0.013997`, mae `0.024964`
- 20d: sample `40`, hit `0.925`, avg `0.036373`, median `0.032102`, mae `0.037701`
- 60d: sample `40`, hit `0.75`, avg `0.054583`, median `0.0765`, mae `0.073331`

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
- 3d: sample `20`, hit `0.8`, avg `0.005258`, median `0.006198`, mae `0.008464`
- 5d: sample `20`, hit `0.75`, avg `0.009082`, median `0.011604`, mae `0.013822`
- 10d: sample `20`, hit `0.85`, avg `0.013924`, median `0.014276`, mae `0.014784`
- 20d: sample `20`, hit `0.95`, avg `0.026583`, median `0.029072`, mae `0.027532`
- 60d: sample `20`, hit `0.95`, avg `0.054438`, median `0.059104`, mae `0.05652`

### surface_only_strength
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.004768`, median `0.012355`, mae `0.018593`
- 5d: sample `40`, hit `0.55`, avg `0.006502`, median `0.007948`, mae `0.021771`
- 10d: sample `40`, hit `0.65`, avg `0.012769`, median `0.013997`, mae `0.024964`
- 20d: sample `40`, hit `0.925`, avg `0.036373`, median `0.032102`, mae `0.037701`
- 60d: sample `40`, hit `0.75`, avg `0.054583`, median `0.0765`, mae `0.073331`

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
