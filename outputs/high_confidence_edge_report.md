# High Confidence Edge Report

Generated at: `2026-10-21T23:36:04.126761+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `124`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `124`, gate `stronger_evidence`
- 5d: completed `124`, gate `stronger_evidence`
- 10d: completed `124`, gate `stronger_evidence`
- 20d: completed `124`, gate `stronger_evidence`
- 60d: completed `124`, gate `stronger_evidence`

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
- 3d: sample `40`, hit `0.5`, avg `-0.002522`, median `0.001534`, mae `0.011033`
- 5d: sample `40`, hit `0.5`, avg `-0.002873`, median `0.000415`, mae `0.014187`
- 10d: sample `40`, hit `0.5`, avg `0.000875`, median `0.002362`, mae `0.016829`
- 20d: sample `40`, hit `0.725`, avg `0.016259`, median `0.022652`, mae `0.027021`
- 60d: sample `40`, hit `0.575`, avg `0.014636`, median `0.024329`, mae `0.064867`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.000707`, median `0.007374`, mae `0.01584`
- 5d: sample `40`, hit `0.475`, avg `-8.5e-05`, median `0.0`, mae `0.020386`
- 10d: sample `40`, hit `0.5`, avg `-0.000549`, median `9.9e-05`, mae `0.028912`
- 20d: sample `40`, hit `0.7`, avg `0.016672`, median `0.019547`, mae `0.032426`
- 60d: sample `40`, hit `0.7`, avg `0.03999`, median `0.030828`, mae `0.063065`

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
- 3d: sample `8`, hit `0.375`, avg `-0.011386`, median `-0.009383`, mae `0.014905`
- 5d: sample `8`, hit `0.375`, avg `-0.008748`, median `-0.004438`, mae `0.015806`
- 10d: sample `8`, hit `0.25`, avg `-0.00992`, median `-0.015123`, mae `0.019533`
- 20d: sample `8`, hit `0.625`, avg `0.002441`, median `0.012958`, mae `0.02564`
- 60d: sample `8`, hit `0.5`, avg `0.00059`, median `0.029831`, mae `0.058234`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.011386`, median `-0.009383`, mae `0.014905`
- 5d: sample `8`, hit `0.375`, avg `-0.008748`, median `-0.004438`, mae `0.015806`
- 10d: sample `8`, hit `0.25`, avg `-0.00992`, median `-0.015123`, mae `0.019533`
- 20d: sample `8`, hit `0.625`, avg `0.002441`, median `0.012958`, mae `0.02564`
- 60d: sample `8`, hit `0.5`, avg `0.00059`, median `0.029831`, mae `0.058234`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.002522, 'median_return': 0.001534, 'mean_absolute_return': 0.011033, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.002873, 'median_return': 0.000415, 'mean_absolute_return': 0.014187, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.031236}, '10d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.000875, 'median_return': 0.002362, 'mean_absolute_return': 0.016829, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.032557}, '20d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.016259, 'median_return': 0.022652, 'mean_absolute_return': 0.027021, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.014636, 'median_return': 0.024329, 'mean_absolute_return': 0.064867, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.011386, 'median_return': -0.009383, 'mean_absolute_return': 0.014905, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.01018}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.008748, 'median_return': -0.004438, 'mean_absolute_return': 0.015806, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.00992, 'median_return': -0.015123, 'mean_absolute_return': 0.019533, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.002441, 'median_return': 0.012958, 'mean_absolute_return': 0.02564, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.043456}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.00059, 'median_return': 0.029831, 'mean_absolute_return': 0.058234, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.099838}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.000257, 'median_return': 0.003412, 'mean_absolute_return': 0.013273, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.000671, 'median_return': 0.000519, 'mean_absolute_return': 0.017451, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.045689}, '10d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.001284, 'median_return': 0.003491, 'mean_absolute_return': 0.023242, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.053454}, '20d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.018024, 'median_return': 0.022652, 'mean_absolute_return': 0.030177, 'max_adverse_excursion': -0.061156, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.030283, 'median_return': 0.029229, 'mean_absolute_return': 0.064603, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.167676}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.475}, '5d': {'sample_size': 80, 'hit_rate': 0.5}, '10d': {'sample_size': 80, 'hit_rate': 0.5}, '20d': {'sample_size': 80, 'hit_rate': 0.5125}, '60d': {'sample_size': 80, 'hit_rate': 0.4375}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.0125, 'both_hit': 0, 'both_miss': 1}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': -0.001158, 'median_return': 0.002018, 'mean_absolute_return': 0.011659, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': -0.001402, 'median_return': 0.000415, 'mean_absolute_return': 0.015011, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.032128}, '10d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.001546, 'median_return': 0.003491, 'mean_absolute_return': 0.01943, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.037669}, '20d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.017662, 'median_return': 0.020068, 'mean_absolute_return': 0.030873, 'max_adverse_excursion': -0.048112, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.023407, 'median_return': 0.024329, 'mean_absolute_return': 0.069643, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.167676}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.000154, 'median_return': 0.003412, 'mean_absolute_return': 0.018767, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.00171, 'median_return': -0.003888, 'mean_absolute_return': 0.024112, 'max_adverse_excursion': -0.036122, 'max_favorable_excursion': 0.045689}, '10d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.003986, 'median_return': -0.01314, 'mean_absolute_return': 0.033193, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.053454}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.012875, 'median_return': 0.023289, 'mean_absolute_return': 0.026274, 'max_adverse_excursion': -0.061156, 'max_favorable_excursion': 0.061437}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.039032, 'median_return': 0.042006, 'mean_absolute_return': 0.046935, 'max_adverse_excursion': -0.035018, 'max_favorable_excursion': 0.108246}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.002522`, median `0.001534`, mae `0.011033`
- 5d: sample `40`, hit `0.5`, avg `-0.002873`, median `0.000415`, mae `0.014187`
- 10d: sample `40`, hit `0.5`, avg `0.000875`, median `0.002362`, mae `0.016829`
- 20d: sample `40`, hit `0.725`, avg `0.016259`, median `0.022652`, mae `0.027021`
- 60d: sample `40`, hit `0.575`, avg `0.014636`, median `0.024329`, mae `0.064867`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.000707`, median `0.007374`, mae `0.01584`
- 5d: sample `40`, hit `0.475`, avg `-8.5e-05`, median `0.0`, mae `0.020386`
- 10d: sample `40`, hit `0.5`, avg `-0.000549`, median `9.9e-05`, mae `0.028912`
- 20d: sample `40`, hit `0.7`, avg `0.016672`, median `0.019547`, mae `0.032426`
- 60d: sample `40`, hit `0.7`, avg `0.03999`, median `0.030828`, mae `0.063065`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.002522`, median `0.001534`, mae `0.011033`
- 5d: sample `40`, hit `0.5`, avg `-0.002873`, median `0.000415`, mae `0.014187`
- 10d: sample `40`, hit `0.5`, avg `0.000875`, median `0.002362`, mae `0.016829`
- 20d: sample `40`, hit `0.725`, avg `0.016259`, median `0.022652`, mae `0.027021`
- 60d: sample `40`, hit `0.575`, avg `0.014636`, median `0.024329`, mae `0.064867`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.008505`, median `-0.009383`, mae `0.014312`
- 5d: sample `20`, hit `0.35`, avg `-0.00902`, median `-0.004989`, mae `0.015471`
- 10d: sample `20`, hit `0.3`, avg `-0.002297`, median `-0.006017`, mae `0.015689`
- 20d: sample `20`, hit `0.75`, avg `0.020468`, median `0.029166`, mae `0.032809`
- 60d: sample `20`, hit `0.6`, avg `0.030979`, median `0.046132`, mae `0.065536`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.001568`, median `0.007492`, mae `0.012913`
- 5d: sample `20`, hit `0.5`, avg `0.00154`, median `0.000519`, mae `0.016659`
- 10d: sample `20`, hit `0.6`, avg `0.002888`, median `0.006356`, mae `0.024631`
- 20d: sample `20`, hit `0.7`, avg `0.020469`, median `0.019547`, mae `0.038577`
- 60d: sample `20`, hit `0.6`, avg `0.040948`, median `0.030828`, mae `0.079194`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.002522`, median `0.001534`, mae `0.011033`
- 5d: sample `40`, hit `0.5`, avg `-0.002873`, median `0.000415`, mae `0.014187`
- 10d: sample `40`, hit `0.5`, avg `0.000875`, median `0.002362`, mae `0.016829`
- 20d: sample `40`, hit `0.725`, avg `0.016259`, median `0.022652`, mae `0.027021`
- 60d: sample `40`, hit `0.575`, avg `0.014636`, median `0.024329`, mae `0.064867`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.008505`, median `-0.009383`, mae `0.014312`
- 5d: sample `20`, hit `0.35`, avg `-0.00902`, median `-0.004989`, mae `0.015471`
- 10d: sample `20`, hit `0.3`, avg `-0.002297`, median `-0.006017`, mae `0.015689`
- 20d: sample `20`, hit `0.75`, avg `0.020468`, median `0.029166`, mae `0.032809`
- 60d: sample `20`, hit `0.6`, avg `0.030979`, median `0.046132`, mae `0.065536`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.000707`, median `0.007374`, mae `0.01584`
- 5d: sample `40`, hit `0.475`, avg `-8.5e-05`, median `0.0`, mae `0.020386`
- 10d: sample `40`, hit `0.5`, avg `-0.000549`, median `9.9e-05`, mae `0.028912`
- 20d: sample `40`, hit `0.7`, avg `0.016672`, median `0.019547`, mae `0.032426`
- 60d: sample `40`, hit `0.7`, avg `0.03999`, median `0.030828`, mae `0.063065`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

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
- 3d: sample `80`, hit `0.525`, avg `-0.000907`, median `0.002018`, mae `0.013436`
- 5d: sample `80`, hit `0.4875`, avg `-0.001479`, median `0.0`, mae `0.017286`
- 10d: sample `80`, hit `0.5`, avg `0.000163`, median `9.9e-05`, mae `0.022871`
- 20d: sample `80`, hit `0.7125`, avg `0.016466`, median `0.020068`, mae `0.029723`
- 60d: sample `80`, hit `0.6375`, avg `0.027313`, median `0.029229`, mae `0.063966`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.002522`, median `0.001534`, mae `0.011033`
- 5d: sample `40`, hit `0.5`, avg `-0.002873`, median `0.000415`, mae `0.014187`
- 10d: sample `40`, hit `0.5`, avg `0.000875`, median `0.002362`, mae `0.016829`
- 20d: sample `40`, hit `0.725`, avg `0.016259`, median `0.022652`, mae `0.027021`
- 60d: sample `40`, hit `0.575`, avg `0.014636`, median `0.024329`, mae `0.064867`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `-0.000907`, median `0.002018`, mae `0.013436`
- 5d: sample `80`, hit `0.4875`, avg `-0.001479`, median `0.0`, mae `0.017286`
- 10d: sample `80`, hit `0.5`, avg `0.000163`, median `9.9e-05`, mae `0.022871`
- 20d: sample `80`, hit `0.7125`, avg `0.016466`, median `0.020068`, mae `0.029723`
- 60d: sample `80`, hit `0.6375`, avg `0.027313`, median `0.029229`, mae `0.063966`

### bounce_with_flow_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.002522`, median `0.001534`, mae `0.011033`
- 5d: sample `40`, hit `0.5`, avg `-0.002873`, median `0.000415`, mae `0.014187`
- 10d: sample `40`, hit `0.5`, avg `0.000875`, median `0.002362`, mae `0.016829`
- 20d: sample `40`, hit `0.725`, avg `0.016259`, median `0.022652`, mae `0.027021`
- 60d: sample `40`, hit `0.575`, avg `0.014636`, median `0.024329`, mae `0.064867`

### risk_path_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.000707`, median `0.007374`, mae `0.01584`
- 5d: sample `40`, hit `0.475`, avg `-8.5e-05`, median `0.0`, mae `0.020386`
- 10d: sample `40`, hit `0.5`, avg `-0.000549`, median `9.9e-05`, mae `0.028912`
- 20d: sample `40`, hit `0.7`, avg `0.016672`, median `0.019547`, mae `0.032426`
- 60d: sample `40`, hit `0.7`, avg `0.03999`, median `0.030828`, mae `0.063065`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
