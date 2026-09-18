# High Confidence Edge Report

Generated at: `2026-09-18T00:54:01.609458+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `28`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `28`, gate `early_evidence`
- 5d: completed `28`, gate `early_evidence`
- 10d: completed `28`, gate `early_evidence`
- 20d: completed `28`, gate `early_evidence`
- 60d: completed `28`, gate `early_evidence`

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
- 3d: sample `60`, hit `0.65`, avg `0.005752`, median `0.009349`, mae `0.015073`
- 5d: sample `60`, hit `0.6167`, avg `0.007268`, median `0.010061`, mae `0.019411`
- 10d: sample `60`, hit `0.7`, avg `0.013729`, median `0.011619`, mae `0.023363`
- 20d: sample `60`, hit `0.8667`, avg `0.037694`, median `0.034704`, mae `0.040334`
- 60d: sample `60`, hit `0.8333`, avg `0.079898`, median `0.095628`, mae `0.085958`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.007944`, median `-0.001058`, mae `0.020318`
- 5d: sample `20`, hit `0.4`, avg `-0.008851`, median `-0.007916`, mae `0.024083`
- 10d: sample `20`, hit `0.55`, avg `-0.000479`, median `0.004306`, mae `0.032246`
- 20d: sample `20`, hit `0.65`, avg `0.015353`, median `0.039427`, mae `0.046914`
- 60d: sample `20`, hit `0.7`, avg `0.039197`, median `0.092008`, mae `0.087017`

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
- 3d: sample `8`, hit `0.625`, avg `0.009676`, median `0.012584`, mae `0.016481`
- 5d: sample `8`, hit `0.625`, avg `0.004274`, median `0.014114`, mae `0.026056`
- 10d: sample `8`, hit `0.5`, avg `0.018545`, median `0.018412`, mae `0.032103`
- 20d: sample `8`, hit `0.875`, avg `0.030206`, median `0.016027`, mae `0.031009`
- 60d: sample `8`, hit `0.75`, avg `0.058792`, median `0.02999`, mae `0.065283`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.001232`, median `0.003757`, mae `0.014907`
- 5d: sample `8`, hit `0.625`, avg `0.002193`, median `0.007948`, mae `0.016848`
- 10d: sample `8`, hit `0.625`, avg `0.007992`, median `0.013069`, mae `0.017217`
- 20d: sample `8`, hit `0.75`, avg `0.039454`, median `0.058396`, mae `0.041952`
- 60d: sample `8`, hit `1.0`, avg `0.108026`, median `0.121826`, mae `0.108026`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.005752, 'median_return': 0.009349, 'mean_absolute_return': 0.015073, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.007268, 'median_return': 0.010061, 'mean_absolute_return': 0.019411, 'max_adverse_excursion': -0.034174, 'max_favorable_excursion': 0.051659}, '10d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.013729, 'median_return': 0.011619, 'mean_absolute_return': 0.023363, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 60, 'hit_rate': 0.8667, 'avg_return': 0.037694, 'median_return': 0.034704, 'mean_absolute_return': 0.040334, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 60, 'hit_rate': 0.8333, 'avg_return': 0.079898, 'median_return': 0.095628, 'mean_absolute_return': 0.085958, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.001232, 'median_return': 0.003757, 'mean_absolute_return': 0.014907, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.002193, 'median_return': 0.007948, 'mean_absolute_return': 0.016848, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.027457}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.007992, 'median_return': 0.013069, 'mean_absolute_return': 0.017217, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.039454, 'median_return': 0.058396, 'mean_absolute_return': 0.041952, 'max_adverse_excursion': -0.005283, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.108026, 'median_return': 0.121826, 'mean_absolute_return': 0.108026, 'max_adverse_excursion': 0.024156, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.002723, 'median_return': 0.006632, 'mean_absolute_return': 0.016548, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.003354, 'median_return': 0.006609, 'mean_absolute_return': 0.020994, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.051659}, '10d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.01042, 'median_return': 0.008908, 'mean_absolute_return': 0.026514, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 72, 'hit_rate': 0.8194, 'avg_return': 0.031293, 'median_return': 0.0344, 'mean_absolute_return': 0.041982, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.065467, 'median_return': 0.084301, 'mean_absolute_return': 0.0838, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6375}, '5d': {'sample_size': 80, 'hit_rate': 0.6125}, '10d': {'sample_size': 80, 'hit_rate': 0.6375}, '20d': {'sample_size': 80, 'hit_rate': 0.7375}, '60d': {'sample_size': 80, 'hit_rate': 0.7}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.3625, 'primary_minus_secondary': 0.275, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_minus_secondary': 0.225, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.3625, 'primary_minus_secondary': 0.275, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.7375, 'secondary_hit_rate': 0.2625, 'primary_minus_secondary': 0.475, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.3, 'primary_minus_secondary': 0.4, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.002328, 'median_return': 0.006042, 'mean_absolute_return': 0.016384, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': 0.003238, 'median_return': 0.006609, 'mean_absolute_return': 0.020579, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.051659}, '10d': {'sample_size': 80, 'hit_rate': 0.6625, 'avg_return': 0.010177, 'median_return': 0.01029, 'mean_absolute_return': 0.025584, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 80, 'hit_rate': 0.8125, 'avg_return': 0.032109, 'median_return': 0.034704, 'mean_absolute_return': 0.041979, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 80, 'hit_rate': 0.8, 'avg_return': 0.069723, 'median_return': 0.092008, 'mean_absolute_return': 0.086223, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.002328`, median `0.006042`, mae `0.016384`
- 5d: sample `80`, hit `0.5625`, avg `0.003238`, median `0.006609`, mae `0.020579`
- 10d: sample `80`, hit `0.6625`, avg `0.010177`, median `0.01029`, mae `0.025584`
- 20d: sample `80`, hit `0.8125`, avg `0.032109`, median `0.034704`, mae `0.041979`
- 60d: sample `80`, hit `0.8`, avg `0.069723`, median `0.092008`, mae `0.086223`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.005752`, median `0.009349`, mae `0.015073`
- 5d: sample `60`, hit `0.6167`, avg `0.007268`, median `0.010061`, mae `0.019411`
- 10d: sample `60`, hit `0.7`, avg `0.013729`, median `0.011619`, mae `0.023363`
- 20d: sample `60`, hit `0.8667`, avg `0.037694`, median `0.034704`, mae `0.040334`
- 60d: sample `60`, hit `0.8333`, avg `0.079898`, median `0.095628`, mae `0.085958`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.007809`, median `0.012584`, mae `0.017472`
- 5d: sample `20`, hit `0.65`, avg `0.010249`, median `0.014114`, mae `0.025019`
- 10d: sample `20`, hit `0.65`, avg `0.024048`, median `0.030744`, mae `0.032905`
- 20d: sample `20`, hit `0.9`, avg `0.042067`, median `0.034158`, mae `0.043304`
- 60d: sample `20`, hit `0.7`, avg `0.07601`, median `0.0765`, mae `0.082955`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.005752`, median `0.009349`, mae `0.015073`
- 5d: sample `60`, hit `0.6167`, avg `0.007268`, median `0.010061`, mae `0.019411`
- 10d: sample `60`, hit `0.7`, avg `0.013729`, median `0.011619`, mae `0.023363`
- 20d: sample `60`, hit `0.8667`, avg `0.037694`, median `0.034704`, mae `0.040334`
- 60d: sample `60`, hit `0.8333`, avg `0.079898`, median `0.095628`, mae `0.085958`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.007944`, median `-0.001058`, mae `0.020318`
- 5d: sample `20`, hit `0.4`, avg `-0.008851`, median `-0.007916`, mae `0.024083`
- 10d: sample `20`, hit `0.55`, avg `-0.000479`, median `0.004306`, mae `0.032246`
- 20d: sample `20`, hit `0.65`, avg `0.015353`, median `0.039427`, mae `0.046914`
- 60d: sample `20`, hit `0.7`, avg `0.039197`, median `0.092008`, mae `0.087017`

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
- 3d: sample `80`, hit `0.5875`, avg `0.002328`, median `0.006042`, mae `0.016384`
- 5d: sample `80`, hit `0.5625`, avg `0.003238`, median `0.006609`, mae `0.020579`
- 10d: sample `80`, hit `0.6625`, avg `0.010177`, median `0.01029`, mae `0.025584`
- 20d: sample `80`, hit `0.8125`, avg `0.032109`, median `0.034704`, mae `0.041979`
- 60d: sample `80`, hit `0.8`, avg `0.069723`, median `0.092008`, mae `0.086223`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.005752`, median `0.009349`, mae `0.015073`
- 5d: sample `60`, hit `0.6167`, avg `0.007268`, median `0.010061`, mae `0.019411`
- 10d: sample `60`, hit `0.7`, avg `0.013729`, median `0.011619`, mae `0.023363`
- 20d: sample `60`, hit `0.8667`, avg `0.037694`, median `0.034704`, mae `0.040334`
- 60d: sample `60`, hit `0.8333`, avg `0.079898`, median `0.095628`, mae `0.085958`

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
