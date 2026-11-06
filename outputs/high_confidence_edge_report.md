# High Confidence Edge Report

Generated at: `2026-11-06T02:06:10.447726+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `168`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `168`, gate `stronger_evidence`
- 5d: completed `168`, gate `stronger_evidence`
- 10d: completed `168`, gate `stronger_evidence`
- 20d: completed `168`, gate `stronger_evidence`
- 60d: completed `168`, gate `stronger_evidence`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `-0.004141`, median `-0.003528`, mae `0.020924`
- 5d: sample `80`, hit `0.45`, avg `-0.003539`, median `-0.00891`, mae `0.025915`
- 10d: sample `80`, hit `0.3625`, avg `-0.002832`, median `-0.01595`, mae `0.040653`
- 20d: sample `80`, hit `0.35`, avg `-0.019327`, median `-0.030715`, mae `0.049829`
- 60d: sample `80`, hit `0.7625`, avg `0.056883`, median `0.06306`, mae `0.068751`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.008911`, median `-0.013999`, mae `0.021143`
- 5d: sample `8`, hit `0.375`, avg `-0.008802`, median `-0.021092`, mae `0.030461`
- 10d: sample `8`, hit `0.375`, avg `0.005541`, median `-0.012607`, mae `0.042228`
- 20d: sample `8`, hit `0.375`, avg `-0.014121`, median `-0.027546`, mae `0.057268`
- 60d: sample `8`, hit `0.875`, avg `0.04832`, median `0.035022`, mae `0.050858`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.008911`, median `-0.013999`, mae `0.021143`
- 5d: sample `8`, hit `0.375`, avg `-0.008802`, median `-0.021092`, mae `0.030461`
- 10d: sample `8`, hit `0.375`, avg `0.005541`, median `-0.012607`, mae `0.042228`
- 20d: sample `8`, hit `0.375`, avg `-0.014121`, median `-0.027546`, mae `0.057268`
- 60d: sample `8`, hit `0.875`, avg `0.04832`, median `0.035022`, mae `0.050858`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.008911, 'median_return': -0.013999, 'mean_absolute_return': 0.021143, 'max_adverse_excursion': -0.029605, 'max_favorable_excursion': 0.028169}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.008802, 'median_return': -0.021092, 'mean_absolute_return': 0.030461, 'max_adverse_excursion': -0.039725, 'max_favorable_excursion': 0.048375}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': 0.005541, 'median_return': -0.012607, 'mean_absolute_return': 0.042228, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.080901}, '20d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.014121, 'median_return': -0.027546, 'mean_absolute_return': 0.057268, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.059673}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.04832, 'median_return': 0.035022, 'mean_absolute_return': 0.050858, 'max_adverse_excursion': -0.010153, 'max_favorable_excursion': 0.110811}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.003611, 'median_return': -0.002277, 'mean_absolute_return': 0.0209, 'max_adverse_excursion': -0.078197, 'max_favorable_excursion': 0.044418}, '5d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': -0.002954, 'median_return': -0.005615, 'mean_absolute_return': 0.02541, 'max_adverse_excursion': -0.049979, 'max_favorable_excursion': 0.06431}, '10d': {'sample_size': 72, 'hit_rate': 0.3611, 'avg_return': -0.003762, 'median_return': -0.01595, 'mean_absolute_return': 0.040478, 'max_adverse_excursion': -0.104082, 'max_favorable_excursion': 0.109782}, '20d': {'sample_size': 72, 'hit_rate': 0.3472, 'avg_return': -0.019906, 'median_return': -0.030778, 'mean_absolute_return': 0.049002, 'max_adverse_excursion': -0.117769, 'max_favorable_excursion': 0.086095}, '60d': {'sample_size': 72, 'hit_rate': 0.75, 'avg_return': 0.057835, 'median_return': 0.063572, 'mean_absolute_return': 0.070739, 'max_adverse_excursion': -0.057863, 'max_favorable_excursion': 0.213753}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5375}, '5d': {'sample_size': 80, 'hit_rate': 0.55}, '10d': {'sample_size': 80, 'hit_rate': 0.6375}, '20d': {'sample_size': 80, 'hit_rate': 0.65}, '60d': {'sample_size': 80, 'hit_rate': 0.2375}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.075, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.3625, 'primary_minus_secondary': 0.275, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.35, 'primary_minus_secondary': 0.3, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.2375, 'secondary_hit_rate': 0.7625, 'primary_minus_secondary': -0.525, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.4625, 'avg_return': -0.004141, 'median_return': -0.003528, 'mean_absolute_return': 0.020924, 'max_adverse_excursion': -0.078197, 'max_favorable_excursion': 0.044418}, '5d': {'sample_size': 80, 'hit_rate': 0.45, 'avg_return': -0.003539, 'median_return': -0.00891, 'mean_absolute_return': 0.025915, 'max_adverse_excursion': -0.049979, 'max_favorable_excursion': 0.06431}, '10d': {'sample_size': 80, 'hit_rate': 0.3625, 'avg_return': -0.002832, 'median_return': -0.01595, 'mean_absolute_return': 0.040653, 'max_adverse_excursion': -0.104082, 'max_favorable_excursion': 0.109782}, '20d': {'sample_size': 80, 'hit_rate': 0.35, 'avg_return': -0.019327, 'median_return': -0.030715, 'mean_absolute_return': 0.049829, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.086095}, '60d': {'sample_size': 80, 'hit_rate': 0.7625, 'avg_return': 0.056883, 'median_return': 0.06306, 'mean_absolute_return': 0.068751, 'max_adverse_excursion': -0.057863, 'max_favorable_excursion': 0.213753}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4167`, avg `-0.00607`, median `-0.005017`, mae `0.019204`
- 5d: sample `60`, hit `0.3667`, avg `-0.007503`, median `-0.014463`, mae `0.02437`
- 10d: sample `60`, hit `0.3167`, avg `-0.009177`, median `-0.018077`, mae `0.038615`
- 20d: sample `60`, hit `0.35`, avg `-0.019191`, median `-0.02787`, mae `0.046439`
- 60d: sample `60`, hit `0.6833`, avg `0.04107`, median `0.047238`, mae `0.056893`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.001647`, median `0.013238`, mae `0.026084`
- 5d: sample `20`, hit `0.7`, avg `0.008353`, median `0.007257`, mae `0.030552`
- 10d: sample `20`, hit `0.5`, avg `0.016203`, median `0.015642`, mae `0.046768`
- 20d: sample `20`, hit `0.35`, avg `-0.019737`, median `-0.03728`, mae `0.059998`
- 60d: sample `20`, hit `1.0`, avg `0.104323`, median `0.112887`, mae `0.104323`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.001647`, median `0.013238`, mae `0.026084`
- 5d: sample `20`, hit `0.7`, avg `0.008353`, median `0.007257`, mae `0.030552`
- 10d: sample `20`, hit `0.5`, avg `0.016203`, median `0.015642`, mae `0.046768`
- 20d: sample `20`, hit `0.35`, avg `-0.019737`, median `-0.03728`, mae `0.059998`
- 60d: sample `20`, hit `1.0`, avg `0.104323`, median `0.112887`, mae `0.104323`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.003167`, median `-0.00446`, mae `0.01865`
- 5d: sample `40`, hit `0.425`, avg `-0.002961`, median `-0.00891`, mae `0.023923`
- 10d: sample `40`, hit `0.35`, avg `-0.006595`, median `-0.020732`, mae `0.037648`
- 20d: sample `40`, hit `0.325`, avg `-0.021797`, median `-0.027546`, mae `0.047275`
- 60d: sample `40`, hit `0.75`, avg `0.040137`, median `0.047238`, mae `0.048862`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.011878`, median `-0.009734`, mae `0.020312`
- 5d: sample `20`, hit `0.25`, avg `-0.016585`, median `-0.018532`, mae `0.025263`
- 10d: sample `20`, hit `0.25`, avg `-0.014339`, median `-0.016715`, mae `0.040549`
- 20d: sample `20`, hit `0.4`, avg `-0.013978`, median `-0.02787`, mae `0.044765`
- 60d: sample `20`, hit `0.55`, avg `0.042936`, median `0.057272`, mae `0.072955`

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

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `-0.004141`, median `-0.003528`, mae `0.020924`
- 5d: sample `80`, hit `0.45`, avg `-0.003539`, median `-0.00891`, mae `0.025915`
- 10d: sample `80`, hit `0.3625`, avg `-0.002832`, median `-0.01595`, mae `0.040653`
- 20d: sample `80`, hit `0.35`, avg `-0.019327`, median `-0.030715`, mae `0.049829`
- 60d: sample `80`, hit `0.7625`, avg `0.056883`, median `0.06306`, mae `0.068751`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `-0.004141`, median `-0.003528`, mae `0.020924`
- 5d: sample `80`, hit `0.45`, avg `-0.003539`, median `-0.00891`, mae `0.025915`
- 10d: sample `80`, hit `0.3625`, avg `-0.002832`, median `-0.01595`, mae `0.040653`
- 20d: sample `80`, hit `0.35`, avg `-0.019327`, median `-0.030715`, mae `0.049829`
- 60d: sample `80`, hit `0.7625`, avg `0.056883`, median `0.06306`, mae `0.068751`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `-0.004141`, median `-0.003528`, mae `0.020924`
- 5d: sample `80`, hit `0.45`, avg `-0.003539`, median `-0.00891`, mae `0.025915`
- 10d: sample `80`, hit `0.3625`, avg `-0.002832`, median `-0.01595`, mae `0.040653`
- 20d: sample `80`, hit `0.35`, avg `-0.019327`, median `-0.030715`, mae `0.049829`
- 60d: sample `80`, hit `0.7625`, avg `0.056883`, median `0.06306`, mae `0.068751`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
