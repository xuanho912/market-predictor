# High Confidence Edge Report

Generated at: `2026-08-24T23:12:48.457154+00:00`

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
- 3d: sample `80`, hit `0.525`, avg `0.000166`, median `0.000766`, mae `0.014357`
- 5d: sample `80`, hit `0.5625`, avg `0.000821`, median `0.000873`, mae `0.017019`
- 10d: sample `80`, hit `0.4875`, avg `0.003106`, median `-0.001222`, mae `0.023254`
- 20d: sample `80`, hit `0.625`, avg `0.006626`, median `0.017881`, mae `0.034791`
- 60d: sample `80`, hit `0.6625`, avg `0.02577`, median `0.034688`, mae `0.06227`

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
- 3d: sample `8`, hit `0.625`, avg `-0.006252`, median `0.00234`, mae `0.015075`
- 5d: sample `8`, hit `0.375`, avg `-0.011032`, median `-0.012956`, mae `0.020772`
- 10d: sample `8`, hit `0.625`, avg `0.005548`, median `0.019233`, mae `0.023076`
- 20d: sample `8`, hit `0.875`, avg `0.016823`, median `0.029166`, mae `0.030648`
- 60d: sample `8`, hit `0.75`, avg `0.046649`, median `0.059495`, mae `0.0659`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.006252`, median `0.00234`, mae `0.015075`
- 5d: sample `8`, hit `0.375`, avg `-0.011032`, median `-0.012956`, mae `0.020772`
- 10d: sample `8`, hit `0.625`, avg `0.005548`, median `0.019233`, mae `0.023076`
- 20d: sample `8`, hit `0.875`, avg `0.016823`, median `0.029166`, mae `0.030648`
- 60d: sample `8`, hit `0.75`, avg `0.046649`, median `0.059495`, mae `0.0659`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.525, 'avg_return': 0.000166, 'median_return': 0.000766, 'mean_absolute_return': 0.014357, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.040299}, '5d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': 0.000821, 'median_return': 0.000873, 'mean_absolute_return': 0.017019, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.049196}, '10d': {'sample_size': 80, 'hit_rate': 0.4875, 'avg_return': 0.003106, 'median_return': -0.001222, 'mean_absolute_return': 0.023254, 'max_adverse_excursion': -0.048357, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.006626, 'median_return': 0.017881, 'mean_absolute_return': 0.034791, 'max_adverse_excursion': -0.10356, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 80, 'hit_rate': 0.6625, 'avg_return': 0.02577, 'median_return': 0.034688, 'mean_absolute_return': 0.06227, 'max_adverse_excursion': -0.19689, 'max_favorable_excursion': 0.19145}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.006252, 'median_return': 0.00234, 'mean_absolute_return': 0.015075, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.017427}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.011032, 'median_return': -0.012956, 'mean_absolute_return': 0.020772, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.005548, 'median_return': 0.019233, 'mean_absolute_return': 0.023076, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.016823, 'median_return': 0.029166, 'mean_absolute_return': 0.030648, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.055822}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.046649, 'median_return': 0.059495, 'mean_absolute_return': 0.0659, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.120808}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.000879, 'median_return': 0.000603, 'mean_absolute_return': 0.014278, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.040299}, '5d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.002138, 'median_return': 0.001239, 'mean_absolute_return': 0.016602, 'max_adverse_excursion': -0.048238, 'max_favorable_excursion': 0.049196}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': 0.002834, 'median_return': -0.002081, 'mean_absolute_return': 0.023274, 'max_adverse_excursion': -0.048357, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.005493, 'median_return': 0.016109, 'mean_absolute_return': 0.035252, 'max_adverse_excursion': -0.10356, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.02345, 'median_return': 0.032982, 'mean_absolute_return': 0.061866, 'max_adverse_excursion': -0.19689, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.5625}, '10d': {'sample_size': 80, 'hit_rate': 0.4875}, '20d': {'sample_size': 80, 'hit_rate': 0.625}, '60d': {'sample_size': 80, 'hit_rate': 0.6625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.025, 'both_hit': 21, 'both_miss': 19}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.1, 'both_hit': 21, 'both_miss': 19}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.075, 'both_hit': 22, 'both_miss': 18}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.025, 'both_hit': 31, 'both_miss': 9}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.025, 'both_hit': 34, 'both_miss': 6}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.525, 'avg_return': 0.000166, 'median_return': 0.000766, 'mean_absolute_return': 0.014357, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.040299}, '5d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': 0.000821, 'median_return': 0.000873, 'mean_absolute_return': 0.017019, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.049196}, '10d': {'sample_size': 80, 'hit_rate': 0.4875, 'avg_return': 0.003106, 'median_return': -0.001222, 'mean_absolute_return': 0.023254, 'max_adverse_excursion': -0.048357, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.006626, 'median_return': 0.017881, 'mean_absolute_return': 0.034791, 'max_adverse_excursion': -0.10356, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 80, 'hit_rate': 0.6625, 'avg_return': 0.02577, 'median_return': 0.034688, 'mean_absolute_return': 0.06227, 'max_adverse_excursion': -0.19689, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.002336`, median `0.000603`, mae `0.01251`
- 5d: sample `40`, hit `0.575`, avg `-0.004611`, median `0.000688`, mae `0.014069`
- 10d: sample `40`, hit `0.375`, avg `-0.003159`, median `-0.007491`, mae `0.021094`
- 20d: sample `40`, hit `0.55`, avg `-0.001384`, median `0.012958`, mae `0.036135`
- 60d: sample `40`, hit `0.525`, avg `0.013564`, median `0.029831`, mae `0.059425`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.000191`, median `0.00234`, mae `0.017069`
- 5d: sample `40`, hit `0.525`, avg `-2.6e-05`, median `0.000415`, mae `0.020346`
- 10d: sample `40`, hit `0.55`, avg `0.007503`, median `0.0076`, mae `0.021406`
- 20d: sample `40`, hit `0.775`, avg `0.021023`, median `0.030297`, mae `0.031335`
- 60d: sample `40`, hit `0.85`, avg `0.057618`, median `0.064104`, mae `0.073011`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.002336`, median `0.000603`, mae `0.01251`
- 5d: sample `40`, hit `0.575`, avg `-0.004611`, median `0.000688`, mae `0.014069`
- 10d: sample `40`, hit `0.375`, avg `-0.003159`, median `-0.007491`, mae `0.021094`
- 20d: sample `40`, hit `0.55`, avg `-0.001384`, median `0.012958`, mae `0.036135`
- 60d: sample `40`, hit `0.525`, avg `0.013564`, median `0.029831`, mae `0.059425`

### breadth_conflicted_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.000191`, median `0.00234`, mae `0.017069`
- 5d: sample `40`, hit `0.525`, avg `-2.6e-05`, median `0.000415`, mae `0.020346`
- 10d: sample `40`, hit `0.55`, avg `0.007503`, median `0.0076`, mae `0.021406`
- 20d: sample `40`, hit `0.775`, avg `0.021023`, median `0.030297`, mae `0.031335`
- 60d: sample `40`, hit `0.85`, avg `0.057618`, median `0.064104`, mae `0.073011`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.002915`, median `0.00234`, mae `0.016411`
- 5d: sample `20`, hit `0.55`, avg `-0.006075`, median `0.000415`, mae `0.018251`
- 10d: sample `20`, hit `0.5`, avg `0.005392`, median `0.0076`, mae `0.020038`
- 20d: sample `20`, hit `0.75`, avg `0.017392`, median `0.030297`, mae `0.034301`
- 60d: sample `20`, hit `0.7`, avg `0.033683`, median `0.046132`, mae `0.064469`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.000191`, median `0.00234`, mae `0.017069`
- 5d: sample `40`, hit `0.525`, avg `-2.6e-05`, median `0.000415`, mae `0.020346`
- 10d: sample `40`, hit `0.55`, avg `0.007503`, median `0.0076`, mae `0.021406`
- 20d: sample `40`, hit `0.775`, avg `0.021023`, median `0.030297`, mae `0.031335`
- 60d: sample `40`, hit `0.85`, avg `0.057618`, median `0.064104`, mae `0.073011`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.002336`, median `0.000603`, mae `0.01251`
- 5d: sample `40`, hit `0.575`, avg `-0.004611`, median `0.000688`, mae `0.014069`
- 10d: sample `40`, hit `0.375`, avg `-0.003159`, median `-0.007491`, mae `0.021094`
- 20d: sample `40`, hit `0.55`, avg `-0.001384`, median `0.012958`, mae `0.036135`
- 60d: sample `40`, hit `0.525`, avg `0.013564`, median `0.029831`, mae `0.059425`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.002668`, median `0.003026`, mae `0.016204`
- 5d: sample `40`, hit `0.55`, avg `0.006252`, median `0.005493`, mae `0.019969`
- 10d: sample `40`, hit `0.6`, avg `0.009371`, median `0.013736`, mae `0.025414`
- 20d: sample `40`, hit `0.7`, avg `0.014636`, median `0.023289`, mae `0.033448`
- 60d: sample `40`, hit `0.8`, avg `0.037975`, median `0.043615`, mae `0.065115`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.002915`, median `0.00234`, mae `0.016411`
- 5d: sample `20`, hit `0.55`, avg `-0.006075`, median `0.000415`, mae `0.018251`
- 10d: sample `20`, hit `0.5`, avg `0.005392`, median `0.0076`, mae `0.020038`
- 20d: sample `20`, hit `0.75`, avg `0.017392`, median `0.030297`, mae `0.034301`
- 60d: sample `20`, hit `0.7`, avg `0.033683`, median `0.046132`, mae `0.064469`

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
- 3d: sample `80`, hit `0.525`, avg `0.000166`, median `0.000766`, mae `0.014357`
- 5d: sample `80`, hit `0.5625`, avg `0.000821`, median `0.000873`, mae `0.017019`
- 10d: sample `80`, hit `0.4875`, avg `0.003106`, median `-0.001222`, mae `0.023254`
- 20d: sample `80`, hit `0.625`, avg `0.006626`, median `0.017881`, mae `0.034791`
- 60d: sample `80`, hit `0.6625`, avg `0.02577`, median `0.034688`, mae `0.06227`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `0.000166`, median `0.000766`, mae `0.014357`
- 5d: sample `80`, hit `0.5625`, avg `0.000821`, median `0.000873`, mae `0.017019`
- 10d: sample `80`, hit `0.4875`, avg `0.003106`, median `-0.001222`, mae `0.023254`
- 20d: sample `80`, hit `0.625`, avg `0.006626`, median `0.017881`, mae `0.034791`
- 60d: sample `80`, hit `0.6625`, avg `0.02577`, median `0.034688`, mae `0.06227`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `0.000166`, median `0.000766`, mae `0.014357`
- 5d: sample `80`, hit `0.5625`, avg `0.000821`, median `0.000873`, mae `0.017019`
- 10d: sample `80`, hit `0.4875`, avg `0.003106`, median `-0.001222`, mae `0.023254`
- 20d: sample `80`, hit `0.625`, avg `0.006626`, median `0.017881`, mae `0.034791`
- 60d: sample `80`, hit `0.6625`, avg `0.02577`, median `0.034688`, mae `0.06227`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `0.000166`, median `0.000766`, mae `0.014357`
- 5d: sample `80`, hit `0.5625`, avg `0.000821`, median `0.000873`, mae `0.017019`
- 10d: sample `80`, hit `0.4875`, avg `0.003106`, median `-0.001222`, mae `0.023254`
- 20d: sample `80`, hit `0.625`, avg `0.006626`, median `0.017881`, mae `0.034791`
- 60d: sample `80`, hit `0.6625`, avg `0.02577`, median `0.034688`, mae `0.06227`

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
