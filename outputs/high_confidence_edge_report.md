# High Confidence Edge Report

Generated at: `2026-11-07T01:26:32.676494+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `172`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `172`, gate `stronger_evidence`
- 5d: completed `172`, gate `stronger_evidence`
- 10d: completed `172`, gate `stronger_evidence`
- 20d: completed `172`, gate `stronger_evidence`
- 60d: completed `172`, gate `stronger_evidence`

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
- 3d: sample `80`, hit `0.5`, avg `-0.003607`, median `0.000438`, mae `0.020136`
- 5d: sample `80`, hit `0.45`, avg `-0.002839`, median `-0.005615`, mae `0.025374`
- 10d: sample `80`, hit `0.3375`, avg `-0.008343`, median `-0.018077`, mae `0.042426`
- 20d: sample `80`, hit `0.3125`, avg `-0.025864`, median `-0.031798`, mae `0.051102`
- 60d: sample `80`, hit `0.775`, avg `0.054809`, median `0.059488`, mae `0.06664`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.003007`, median `-0.00163`, mae `0.019647`
- 5d: sample `8`, hit `0.5`, avg `-0.005605`, median `0.000169`, mae `0.027967`
- 10d: sample `8`, hit `0.375`, avg `0.001768`, median `-0.012607`, mae `0.046001`
- 20d: sample `8`, hit `0.375`, avg `-0.007427`, median `-0.027546`, mae `0.050575`
- 60d: sample `8`, hit `0.875`, avg `0.052162`, median `0.065766`, mae `0.054701`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.003007`, median `-0.00163`, mae `0.019647`
- 5d: sample `8`, hit `0.5`, avg `-0.005605`, median `0.000169`, mae `0.027967`
- 10d: sample `8`, hit `0.375`, avg `0.001768`, median `-0.012607`, mae `0.046001`
- 20d: sample `8`, hit `0.375`, avg `-0.007427`, median `-0.027546`, mae `0.050575`
- 60d: sample `8`, hit `0.875`, avg `0.052162`, median `0.065766`, mae `0.054701`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.003007, 'median_return': -0.00163, 'mean_absolute_return': 0.019647, 'max_adverse_excursion': -0.029317, 'max_favorable_excursion': 0.028169}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.005605, 'median_return': 0.000169, 'mean_absolute_return': 0.027967, 'max_adverse_excursion': -0.039725, 'max_favorable_excursion': 0.048375}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': 0.001768, 'median_return': -0.012607, 'mean_absolute_return': 0.046001, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.080901}, '20d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.007427, 'median_return': -0.027546, 'mean_absolute_return': 0.050575, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.059673}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.052162, 'median_return': 0.065766, 'mean_absolute_return': 0.054701, 'max_adverse_excursion': -0.010153, 'max_favorable_excursion': 0.110811}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': -0.003674, 'median_return': 0.001066, 'mean_absolute_return': 0.02019, 'max_adverse_excursion': -0.078197, 'max_favorable_excursion': 0.044418}, '5d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.002531, 'median_return': -0.005615, 'mean_absolute_return': 0.025086, 'max_adverse_excursion': -0.049979, 'max_favorable_excursion': 0.06431}, '10d': {'sample_size': 72, 'hit_rate': 0.3333, 'avg_return': -0.009466, 'median_return': -0.018077, 'mean_absolute_return': 0.042029, 'max_adverse_excursion': -0.120976, 'max_favorable_excursion': 0.109782}, '20d': {'sample_size': 72, 'hit_rate': 0.3056, 'avg_return': -0.027912, 'median_return': -0.033468, 'mean_absolute_return': 0.051161, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.086095}, '60d': {'sample_size': 72, 'hit_rate': 0.7639, 'avg_return': 0.055103, 'median_return': 0.059488, 'mean_absolute_return': 0.067967, 'max_adverse_excursion': -0.057863, 'max_favorable_excursion': 0.213753}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.55}, '10d': {'sample_size': 80, 'hit_rate': 0.6625}, '20d': {'sample_size': 80, 'hit_rate': 0.6875}, '60d': {'sample_size': 80, 'hit_rate': 0.225}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.3375, 'primary_minus_secondary': 0.325, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.3125, 'primary_minus_secondary': 0.375, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.225, 'secondary_hit_rate': 0.775, 'primary_minus_secondary': -0.55, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5, 'avg_return': -0.003607, 'median_return': 0.000438, 'mean_absolute_return': 0.020136, 'max_adverse_excursion': -0.078197, 'max_favorable_excursion': 0.044418}, '5d': {'sample_size': 80, 'hit_rate': 0.45, 'avg_return': -0.002839, 'median_return': -0.005615, 'mean_absolute_return': 0.025374, 'max_adverse_excursion': -0.049979, 'max_favorable_excursion': 0.06431}, '10d': {'sample_size': 80, 'hit_rate': 0.3375, 'avg_return': -0.008343, 'median_return': -0.018077, 'mean_absolute_return': 0.042426, 'max_adverse_excursion': -0.120976, 'max_favorable_excursion': 0.109782}, '20d': {'sample_size': 80, 'hit_rate': 0.3125, 'avg_return': -0.025864, 'median_return': -0.031798, 'mean_absolute_return': 0.051102, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.086095}, '60d': {'sample_size': 80, 'hit_rate': 0.775, 'avg_return': 0.054809, 'median_return': 0.059488, 'mean_absolute_return': 0.06664, 'max_adverse_excursion': -0.057863, 'max_favorable_excursion': 0.213753}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.006017`, median `-0.00446`, mae `0.018628`
- 5d: sample `60`, hit `0.3667`, avg `-0.007133`, median `-0.014235`, mae `0.023615`
- 10d: sample `60`, hit `0.2833`, avg `-0.014152`, median `-0.020732`, mae `0.03993`
- 20d: sample `60`, hit `0.3`, avg `-0.026671`, median `-0.030778`, mae `0.048627`
- 60d: sample `60`, hit `0.7`, avg `0.03899`, median `0.044344`, mae `0.054765`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.003624`, median `0.013238`, mae `0.024661`
- 5d: sample `20`, hit `0.7`, avg `0.010044`, median `0.007257`, mae `0.03065`
- 10d: sample `20`, hit `0.5`, avg `0.009083`, median `0.015642`, mae `0.049914`
- 20d: sample `20`, hit `0.35`, avg `-0.023442`, median `-0.03728`, mae `0.05853`
- 60d: sample `20`, hit `1.0`, avg `0.102265`, median `0.112786`, mae `0.102265`

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
- 3d: sample `20`, hit `0.65`, avg `0.003624`, median `0.013238`, mae `0.024661`
- 5d: sample `20`, hit `0.7`, avg `0.010044`, median `0.007257`, mae `0.03065`
- 10d: sample `20`, hit `0.5`, avg `0.009083`, median `0.015642`, mae `0.049914`
- 20d: sample `20`, hit `0.35`, avg `-0.023442`, median `-0.03728`, mae `0.05853`
- 60d: sample `20`, hit `1.0`, avg `0.102265`, median `0.112786`, mae `0.102265`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.003593`, median `-0.00446`, mae `0.018223`
- 5d: sample `40`, hit `0.425`, avg `-0.003506`, median `-0.00891`, mae `0.023378`
- 10d: sample `40`, hit `0.35`, avg `-0.007156`, median `-0.020732`, mae `0.037088`
- 20d: sample `40`, hit `0.3`, avg `-0.024089`, median `-0.028258`, mae `0.047417`
- 60d: sample `40`, hit `0.75`, avg `0.041101`, median `0.047238`, mae `0.049826`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.010865`, median `-0.003528`, mae `0.019436`
- 5d: sample `20`, hit `0.25`, avg `-0.014388`, median `-0.016389`, mae `0.024089`
- 10d: sample `20`, hit `0.15`, avg `-0.028143`, median `-0.018208`, mae `0.045615`
- 20d: sample `20`, hit `0.3`, avg `-0.031836`, median `-0.035792`, mae `0.051046`
- 60d: sample `20`, hit `0.6`, avg `0.03477`, median `0.027846`, mae `0.064644`

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
- 3d: sample `80`, hit `0.5`, avg `-0.003607`, median `0.000438`, mae `0.020136`
- 5d: sample `80`, hit `0.45`, avg `-0.002839`, median `-0.005615`, mae `0.025374`
- 10d: sample `80`, hit `0.3375`, avg `-0.008343`, median `-0.018077`, mae `0.042426`
- 20d: sample `80`, hit `0.3125`, avg `-0.025864`, median `-0.031798`, mae `0.051102`
- 60d: sample `80`, hit `0.775`, avg `0.054809`, median `0.059488`, mae `0.06664`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.003607`, median `0.000438`, mae `0.020136`
- 5d: sample `80`, hit `0.45`, avg `-0.002839`, median `-0.005615`, mae `0.025374`
- 10d: sample `80`, hit `0.3375`, avg `-0.008343`, median `-0.018077`, mae `0.042426`
- 20d: sample `80`, hit `0.3125`, avg `-0.025864`, median `-0.031798`, mae `0.051102`
- 60d: sample `80`, hit `0.775`, avg `0.054809`, median `0.059488`, mae `0.06664`

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
- 3d: sample `80`, hit `0.5`, avg `-0.003607`, median `0.000438`, mae `0.020136`
- 5d: sample `80`, hit `0.45`, avg `-0.002839`, median `-0.005615`, mae `0.025374`
- 10d: sample `80`, hit `0.3375`, avg `-0.008343`, median `-0.018077`, mae `0.042426`
- 20d: sample `80`, hit `0.3125`, avg `-0.025864`, median `-0.031798`, mae `0.051102`
- 60d: sample `80`, hit `0.775`, avg `0.054809`, median `0.059488`, mae `0.06664`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
