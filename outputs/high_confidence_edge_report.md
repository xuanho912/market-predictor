# High Confidence Edge Report

Generated at: `2026-10-22T08:56:52.788357+00:00`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.002522`, median `0.001534`, mae `0.011033`
- 5d: sample `40`, hit `0.5`, avg `-0.002873`, median `0.000415`, mae `0.014187`
- 10d: sample `40`, hit `0.5`, avg `0.000875`, median `0.002362`, mae `0.016829`
- 20d: sample `40`, hit `0.725`, avg `0.016259`, median `0.022652`, mae `0.027021`
- 60d: sample `40`, hit `0.575`, avg `0.014636`, median `0.024329`, mae `0.064867`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.000707`, median `0.007374`, mae `0.01584`
- 5d: sample `40`, hit `0.475`, avg `-8.5e-05`, median `0.0`, mae `0.020386`
- 10d: sample `40`, hit `0.5`, avg `-0.000549`, median `9.9e-05`, mae `0.028912`
- 20d: sample `40`, hit `0.7`, avg `0.016672`, median `0.019547`, mae `0.032426`
- 60d: sample `40`, hit `0.7`, avg `0.03999`, median `0.030828`, mae `0.063065`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.006601`, median `0.011414`, mae `0.009614`
- 5d: sample `8`, hit `0.875`, avg `0.009886`, median `0.012091`, mae `0.014466`
- 10d: sample `8`, hit `0.875`, avg `0.013971`, median `0.019702`, mae `0.014024`
- 20d: sample `8`, hit `0.625`, avg `0.00811`, median `0.019193`, mae `0.019536`
- 60d: sample `8`, hit `0.5`, avg `0.005145`, median `0.048421`, mae `0.074559`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.011386`, median `-0.009383`, mae `0.014905`
- 5d: sample `8`, hit `0.375`, avg `-0.008748`, median `-0.004438`, mae `0.015806`
- 10d: sample `8`, hit `0.25`, avg `-0.00992`, median `-0.015123`, mae `0.019533`
- 20d: sample `8`, hit `0.625`, avg `0.002441`, median `0.012958`, mae `0.02564`
- 60d: sample `8`, hit `0.5`, avg `0.00059`, median `0.029831`, mae `0.058234`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.011386, 'median_return': -0.009383, 'mean_absolute_return': 0.014905, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.01018}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.008748, 'median_return': -0.004438, 'mean_absolute_return': 0.015806, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.00992, 'median_return': -0.015123, 'mean_absolute_return': 0.019533, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.002441, 'median_return': 0.012958, 'mean_absolute_return': 0.02564, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.043456}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.00059, 'median_return': 0.029831, 'mean_absolute_return': 0.058234, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.099838}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.000257, 'median_return': 0.003412, 'mean_absolute_return': 0.013273, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.000671, 'median_return': 0.000519, 'mean_absolute_return': 0.017451, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.045689}, '10d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.001284, 'median_return': 0.003491, 'mean_absolute_return': 0.023242, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.053454}, '20d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.018024, 'median_return': 0.022652, 'mean_absolute_return': 0.030177, 'max_adverse_excursion': -0.061156, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.030283, 'median_return': 0.029229, 'mean_absolute_return': 0.064603, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.167676}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.55}, '5d': {'sample_size': 80, 'hit_rate': 0.575}, '10d': {'sample_size': 80, 'hit_rate': 0.6}, '20d': {'sample_size': 80, 'hit_rate': 0.3875}, '60d': {'sample_size': 80, 'hit_rate': 0.3875}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.4125, 'primary_minus_secondary': 0.1625, 'both_hit': 0, 'both_miss': 1}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_minus_secondary': 0.2, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.002522, 'median_return': 0.001534, 'mean_absolute_return': 0.011033, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.002873, 'median_return': 0.000415, 'mean_absolute_return': 0.014187, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.031236}, '10d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.000875, 'median_return': 0.002362, 'mean_absolute_return': 0.016829, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.032557}, '20d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.016259, 'median_return': 0.022652, 'mean_absolute_return': 0.027021, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.014636, 'median_return': 0.024329, 'mean_absolute_return': 0.064867, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.000707, 'median_return': 0.007374, 'mean_absolute_return': 0.01584, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -8.5e-05, 'median_return': 0.0, 'mean_absolute_return': 0.020386, 'max_adverse_excursion': -0.040291, 'max_favorable_excursion': 0.045689}, '10d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.000549, 'median_return': 9.9e-05, 'mean_absolute_return': 0.028912, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.053454}, '20d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.016672, 'median_return': 0.019547, 'mean_absolute_return': 0.032426, 'max_adverse_excursion': -0.061156, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.03999, 'median_return': 0.030828, 'mean_absolute_return': 0.063065, 'max_adverse_excursion': -0.118502, 'max_favorable_excursion': 0.167676}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.003461`, median `0.00469`, mae `0.007753`
- 5d: sample `20`, hit `0.65`, avg `0.003273`, median `0.007324`, mae `0.012903`
- 10d: sample `20`, hit `0.7`, avg `0.004048`, median `0.011`, mae `0.017969`
- 20d: sample `20`, hit `0.7`, avg `0.01205`, median `0.015404`, mae `0.021233`
- 60d: sample `20`, hit `0.55`, avg `-0.001706`, median `0.004698`, mae `0.064198`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.003461`, median `0.00469`, mae `0.007753`
- 5d: sample `20`, hit `0.65`, avg `0.003273`, median `0.007324`, mae `0.012903`
- 10d: sample `20`, hit `0.7`, avg `0.004048`, median `0.011`, mae `0.017969`
- 20d: sample `20`, hit `0.7`, avg `0.01205`, median `0.015404`, mae `0.021233`
- 60d: sample `20`, hit `0.55`, avg `-0.001706`, median `0.004698`, mae `0.064198`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.003461`, median `0.00469`, mae `0.007753`
- 5d: sample `20`, hit `0.65`, avg `0.003273`, median `0.007324`, mae `0.012903`
- 10d: sample `20`, hit `0.7`, avg `0.004048`, median `0.011`, mae `0.017969`
- 20d: sample `20`, hit `0.7`, avg `0.01205`, median `0.015404`, mae `0.021233`
- 60d: sample `20`, hit `0.55`, avg `-0.001706`, median `0.004698`, mae `0.064198`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.003461`, median `0.00469`, mae `0.007753`
- 5d: sample `20`, hit `0.65`, avg `0.003273`, median `0.007324`, mae `0.012903`
- 10d: sample `20`, hit `0.7`, avg `0.004048`, median `0.011`, mae `0.017969`
- 20d: sample `20`, hit `0.7`, avg `0.01205`, median `0.015404`, mae `0.021233`
- 60d: sample `20`, hit `0.55`, avg `-0.001706`, median `0.004698`, mae `0.064198`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.003461`, median `0.00469`, mae `0.007753`
- 5d: sample `20`, hit `0.65`, avg `0.003273`, median `0.007324`, mae `0.012903`
- 10d: sample `20`, hit `0.7`, avg `0.004048`, median `0.011`, mae `0.017969`
- 20d: sample `20`, hit `0.7`, avg `0.01205`, median `0.015404`, mae `0.021233`
- 60d: sample `20`, hit `0.55`, avg `-0.001706`, median `0.004698`, mae `0.064198`

### risk_path_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.4833`, avg `-0.002363`, median `-0.001658`, mae `0.015331`
- 5d: sample `60`, hit `0.4333`, avg `-0.003063`, median `-0.003452`, mae `0.018747`
- 10d: sample `60`, hit `0.4333`, avg `-0.001132`, median `-0.006017`, mae `0.024504`
- 20d: sample `60`, hit `0.7167`, avg `0.017937`, median `0.023289`, mae `0.032553`
- 60d: sample `60`, hit `0.6667`, avg `0.036986`, median `0.030828`, mae `0.063888`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
