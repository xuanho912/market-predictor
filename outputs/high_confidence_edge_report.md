# High Confidence Edge Report

Generated at: `2026-11-07T02:44:43.255278+00:00`

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
- 3d: sample `80`, hit `0.625`, avg `0.003729`, median `0.010078`, mae `0.022264`
- 5d: sample `80`, hit `0.6375`, avg `0.009408`, median `0.01371`, mae `0.02774`
- 10d: sample `80`, hit `0.6625`, avg `0.012481`, median `0.024864`, mae `0.048143`
- 20d: sample `80`, hit `0.7`, avg `0.017892`, median `0.04796`, mae `0.064729`
- 60d: sample `80`, hit `0.8`, avg `0.050863`, median `0.072891`, mae `0.087338`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.013863`, median `0.019501`, mae `0.022547`
- 5d: sample `8`, hit `0.875`, avg `0.017298`, median `0.014974`, mae `0.019435`
- 10d: sample `8`, hit `0.375`, avg `-0.003558`, median `-0.011849`, mae `0.043024`
- 20d: sample `8`, hit `0.75`, avg `0.00707`, median `0.028264`, mae `0.061385`
- 60d: sample `8`, hit `0.875`, avg `0.05666`, median `0.073586`, mae `0.069999`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.013863`, median `0.019501`, mae `0.022547`
- 5d: sample `8`, hit `0.875`, avg `0.017298`, median `0.014974`, mae `0.019435`
- 10d: sample `8`, hit `0.375`, avg `-0.003558`, median `-0.011849`, mae `0.043024`
- 20d: sample `8`, hit `0.75`, avg `0.00707`, median `0.028264`, mae `0.061385`
- 60d: sample `8`, hit `0.875`, avg `0.05666`, median `0.073586`, mae `0.069999`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.013863, 'median_return': 0.019501, 'mean_absolute_return': 0.022547, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.049499}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.017298, 'median_return': 0.014974, 'mean_absolute_return': 0.019435, 'max_adverse_excursion': -0.00855, 'max_favorable_excursion': 0.044138}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.003558, 'median_return': -0.011849, 'mean_absolute_return': 0.043024, 'max_adverse_excursion': -0.11923, 'max_favorable_excursion': 0.076904}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.00707, 'median_return': 0.028264, 'mean_absolute_return': 0.061385, 'max_adverse_excursion': -0.207737, 'max_favorable_excursion': 0.085922}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.05666, 'median_return': 0.073586, 'mean_absolute_return': 0.069999, 'max_adverse_excursion': -0.053355, 'max_favorable_excursion': 0.08517}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.002603, 'median_return': 0.007915, 'mean_absolute_return': 0.022233, 'max_adverse_excursion': -0.083565, 'max_favorable_excursion': 0.045561}, '5d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.008531, 'median_return': 0.01371, 'mean_absolute_return': 0.028663, 'max_adverse_excursion': -0.177985, 'max_favorable_excursion': 0.076593}, '10d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.014263, 'median_return': 0.032676, 'mean_absolute_return': 0.048712, 'max_adverse_excursion': -0.139978, 'max_favorable_excursion': 0.092667}, '20d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.019095, 'median_return': 0.049861, 'mean_absolute_return': 0.0651, 'max_adverse_excursion': -0.302412, 'max_favorable_excursion': 0.124329}, '60d': {'sample_size': 72, 'hit_rate': 0.7917, 'avg_return': 0.050219, 'median_return': 0.072891, 'mean_absolute_return': 0.089265, 'max_adverse_excursion': -0.324011, 'max_favorable_excursion': 0.213753}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.375}, '5d': {'sample_size': 80, 'hit_rate': 0.3625}, '10d': {'sample_size': 80, 'hit_rate': 0.325}, '20d': {'sample_size': 80, 'hit_rate': 0.3}, '60d': {'sample_size': 80, 'hit_rate': 0.2}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.25, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.275, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.3375, 'both_hit': 0, 'both_miss': 1}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': -0.4, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.2, 'secondary_hit_rate': 0.8, 'primary_minus_secondary': -0.6, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.006761, 'median_return': 0.011103, 'mean_absolute_return': 0.019217, 'max_adverse_excursion': -0.059623, 'max_favorable_excursion': 0.049499}, '5d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.010674, 'median_return': 0.012762, 'mean_absolute_return': 0.020171, 'max_adverse_excursion': -0.042113, 'max_favorable_excursion': 0.048375}, '10d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.011657, 'median_return': 0.016492, 'mean_absolute_return': 0.038829, 'max_adverse_excursion': -0.125677, 'max_favorable_excursion': 0.080901}, '20d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.014089, 'median_return': 0.029234, 'mean_absolute_return': 0.056375, 'max_adverse_excursion': -0.236646, 'max_favorable_excursion': 0.096037}, '60d': {'sample_size': 40, 'hit_rate': 0.825, 'avg_return': 0.050959, 'median_return': 0.068046, 'mean_absolute_return': 0.069481, 'max_adverse_excursion': -0.092242, 'max_favorable_excursion': 0.136738}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.000697, 'median_return': 0.007915, 'mean_absolute_return': 0.025312, 'max_adverse_excursion': -0.083565, 'max_favorable_excursion': 0.044028}, '5d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.008141, 'median_return': 0.020777, 'mean_absolute_return': 0.035309, 'max_adverse_excursion': -0.177985, 'max_favorable_excursion': 0.076593}, '10d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.013305, 'median_return': 0.038085, 'mean_absolute_return': 0.057457, 'max_adverse_excursion': -0.139978, 'max_favorable_excursion': 0.092667}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.021695, 'median_return': 0.052608, 'mean_absolute_return': 0.073083, 'max_adverse_excursion': -0.302412, 'max_favorable_excursion': 0.124329}, '60d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.050767, 'median_return': 0.084117, 'mean_absolute_return': 0.105195, 'max_adverse_excursion': -0.324011, 'max_favorable_excursion': 0.213753}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.003082`, median `0.007915`, mae `0.021541`
- 5d: sample `60`, hit `0.6`, avg `0.003767`, median `0.012625`, mae `0.026512`
- 10d: sample `60`, hit `0.6`, avg `0.003251`, median `0.011842`, mae `0.045487`
- 20d: sample `60`, hit `0.65`, avg `0.006984`, median `0.028264`, mae `0.06196`
- 60d: sample `60`, hit `0.7833`, avg `0.038392`, median `0.060303`, mae `0.075559`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.00567`, median `0.011957`, mae `0.024434`
- 5d: sample `20`, hit `0.75`, avg `0.02633`, median `0.030262`, mae `0.031424`
- 10d: sample `20`, hit `0.85`, avg `0.04017`, median `0.057851`, mae `0.056111`
- 20d: sample `20`, hit `0.85`, avg `0.050618`, median `0.069372`, mae `0.073036`
- 60d: sample `20`, hit `0.85`, avg `0.088274`, median `0.103237`, mae `0.122675`

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
- 3d: sample `20`, hit `0.7`, avg `0.00567`, median `0.011957`, mae `0.024434`
- 5d: sample `20`, hit `0.75`, avg `0.02633`, median `0.030262`, mae `0.031424`
- 10d: sample `20`, hit `0.85`, avg `0.04017`, median `0.057851`, mae `0.056111`
- 20d: sample `20`, hit `0.85`, avg `0.050618`, median `0.069372`, mae `0.073036`
- 60d: sample `20`, hit `0.85`, avg `0.088274`, median `0.103237`, mae `0.122675`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.006761`, median `0.011103`, mae `0.019217`
- 5d: sample `40`, hit `0.625`, avg `0.010674`, median `0.012762`, mae `0.020171`
- 10d: sample `40`, hit `0.6`, avg `0.011657`, median `0.016492`, mae `0.038829`
- 20d: sample `40`, hit `0.725`, avg `0.014089`, median `0.029234`, mae `0.056375`
- 60d: sample `40`, hit `0.825`, avg `0.050959`, median `0.068046`, mae `0.069481`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.004276`, median `0.005555`, mae `0.026189`
- 5d: sample `20`, hit `0.55`, avg `-0.010047`, median `0.004527`, mae `0.039194`
- 10d: sample `20`, hit `0.6`, avg `-0.01356`, median `0.011842`, mae `0.058804`
- 20d: sample `20`, hit `0.5`, avg `-0.007228`, median `0.000515`, mae `0.07313`
- 60d: sample `20`, hit `0.7`, avg `0.013259`, median `0.053187`, mae `0.087715`

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
- 3d: sample `80`, hit `0.625`, avg `0.003729`, median `0.010078`, mae `0.022264`
- 5d: sample `80`, hit `0.6375`, avg `0.009408`, median `0.01371`, mae `0.02774`
- 10d: sample `80`, hit `0.6625`, avg `0.012481`, median `0.024864`, mae `0.048143`
- 20d: sample `80`, hit `0.7`, avg `0.017892`, median `0.04796`, mae `0.064729`
- 60d: sample `80`, hit `0.8`, avg `0.050863`, median `0.072891`, mae `0.087338`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.003729`, median `0.010078`, mae `0.022264`
- 5d: sample `80`, hit `0.6375`, avg `0.009408`, median `0.01371`, mae `0.02774`
- 10d: sample `80`, hit `0.6625`, avg `0.012481`, median `0.024864`, mae `0.048143`
- 20d: sample `80`, hit `0.7`, avg `0.017892`, median `0.04796`, mae `0.064729`
- 60d: sample `80`, hit `0.8`, avg `0.050863`, median `0.072891`, mae `0.087338`

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
- 3d: sample `80`, hit `0.625`, avg `0.003729`, median `0.010078`, mae `0.022264`
- 5d: sample `80`, hit `0.6375`, avg `0.009408`, median `0.01371`, mae `0.02774`
- 10d: sample `80`, hit `0.6625`, avg `0.012481`, median `0.024864`, mae `0.048143`
- 20d: sample `80`, hit `0.7`, avg `0.017892`, median `0.04796`, mae `0.064729`
- 60d: sample `80`, hit `0.8`, avg `0.050863`, median `0.072891`, mae `0.087338`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
