# High Confidence Edge Report

Generated at: `2026-11-05T20:01:18.020853+00:00`

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
- 3d: sample `80`, hit `0.625`, avg `0.003785`, median `0.01024`, mae `0.021953`
- 5d: sample `80`, hit `0.6125`, avg `0.007207`, median `0.012762`, mae `0.028819`
- 10d: sample `80`, hit `0.6125`, avg `0.011867`, median `0.029984`, mae `0.04956`
- 20d: sample `80`, hit `0.675`, avg `0.016964`, median `0.042025`, mae `0.063091`
- 60d: sample `80`, hit `0.725`, avg `0.03988`, median `0.055989`, mae `0.081215`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.006992`, median `0.011636`, mae `0.011719`
- 5d: sample `8`, hit `0.625`, avg `0.006574`, median `0.020079`, mae `0.021622`
- 10d: sample `8`, hit `0.625`, avg `0.011358`, median `0.008301`, mae `0.030874`
- 20d: sample `8`, hit `0.625`, avg `0.019063`, median `0.028589`, mae `0.034483`
- 60d: sample `8`, hit `0.625`, avg `0.024882`, median `0.043989`, mae `0.055019`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.016683`, median `0.02763`, mae `0.025367`
- 5d: sample `8`, hit `0.75`, avg `0.019458`, median `0.025502`, mae `0.022157`
- 10d: sample `8`, hit `0.75`, avg `0.021028`, median `0.050979`, mae `0.053798`
- 20d: sample `8`, hit `0.75`, avg `0.015086`, median `0.055157`, mae `0.069402`
- 60d: sample `8`, hit `0.875`, avg `0.063497`, median `0.073586`, mae `0.076836`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.016683, 'median_return': 0.02763, 'mean_absolute_return': 0.025367, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.049499}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.019458, 'median_return': 0.025502, 'mean_absolute_return': 0.022157, 'max_adverse_excursion': -0.00855, 'max_favorable_excursion': 0.044138}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.021028, 'median_return': 0.050979, 'mean_absolute_return': 0.053798, 'max_adverse_excursion': -0.11923, 'max_favorable_excursion': 0.076904}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.015086, 'median_return': 0.055157, 'mean_absolute_return': 0.069402, 'max_adverse_excursion': -0.207737, 'max_favorable_excursion': 0.085922}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.063497, 'median_return': 0.073586, 'mean_absolute_return': 0.076836, 'max_adverse_excursion': -0.053355, 'max_favorable_excursion': 0.110811}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.002352, 'median_return': 0.010078, 'mean_absolute_return': 0.021574, 'max_adverse_excursion': -0.083565, 'max_favorable_excursion': 0.045561}, '5d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.005846, 'median_return': 0.012749, 'mean_absolute_return': 0.029559, 'max_adverse_excursion': -0.177985, 'max_favorable_excursion': 0.076593}, '10d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.010849, 'median_return': 0.024864, 'mean_absolute_return': 0.049089, 'max_adverse_excursion': -0.139978, 'max_favorable_excursion': 0.092667}, '20d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.017173, 'median_return': 0.042025, 'mean_absolute_return': 0.06239, 'max_adverse_excursion': -0.302412, 'max_favorable_excursion': 0.124329}, '60d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.037256, 'median_return': 0.052255, 'mean_absolute_return': 0.081702, 'max_adverse_excursion': -0.324011, 'max_favorable_excursion': 0.213753}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.375}, '5d': {'sample_size': 80, 'hit_rate': 0.3875}, '10d': {'sample_size': 80, 'hit_rate': 0.375}, '20d': {'sample_size': 80, 'hit_rate': 0.325}, '60d': {'sample_size': 80, 'hit_rate': 0.275}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.25, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.2375, 'both_hit': 0, 'both_miss': 1}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.35, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_minus_secondary': -0.45, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.007578, 'median_return': 0.011636, 'mean_absolute_return': 0.018828, 'max_adverse_excursion': -0.059623, 'max_favorable_excursion': 0.049499}, '5d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.010295, 'median_return': 0.013109, 'mean_absolute_return': 0.023712, 'max_adverse_excursion': -0.042113, 'max_favorable_excursion': 0.048375}, '10d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.012324, 'median_return': 0.011432, 'mean_absolute_return': 0.039553, 'max_adverse_excursion': -0.11923, 'max_favorable_excursion': 0.080901}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.016776, 'median_return': 0.029234, 'mean_absolute_return': 0.05421, 'max_adverse_excursion': -0.236646, 'max_favorable_excursion': 0.096037}, '60d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.047113, 'median_return': 0.054522, 'mean_absolute_return': 0.063346, 'max_adverse_excursion': -0.092242, 'max_favorable_excursion': 0.136738}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': -7e-06, 'median_return': 0.007915, 'mean_absolute_return': 0.025079, 'max_adverse_excursion': -0.083565, 'max_favorable_excursion': 0.044028}, '5d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.00412, 'median_return': 0.012749, 'mean_absolute_return': 0.033926, 'max_adverse_excursion': -0.177985, 'max_favorable_excursion': 0.076593}, '10d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.01141, 'median_return': 0.0362, 'mean_absolute_return': 0.059567, 'max_adverse_excursion': -0.139978, 'max_favorable_excursion': 0.092667}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.017152, 'median_return': 0.049262, 'mean_absolute_return': 0.071972, 'max_adverse_excursion': -0.302412, 'max_favorable_excursion': 0.124329}, '60d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.032647, 'median_return': 0.059797, 'mean_absolute_return': 0.099084, 'max_adverse_excursion': -0.324011, 'max_favorable_excursion': 0.213753}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.003917`, median `0.010078`, mae `0.02094`
- 5d: sample `60`, hit `0.5833`, avg `0.003143`, median `0.012625`, mae `0.02863`
- 10d: sample `60`, hit `0.55`, avg `0.003927`, median `0.011842`, mae `0.047914`
- 20d: sample `60`, hit `0.6167`, avg `0.007403`, median `0.028589`, mae `0.060985`
- 60d: sample `60`, hit `0.7167`, avg `0.031401`, median `0.052255`, mae `0.072335`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.003392`, median `0.011957`, mae `0.024993`
- 5d: sample `20`, hit `0.7`, avg `0.019399`, median `0.020777`, mae `0.029387`
- 10d: sample `20`, hit `0.8`, avg `0.035685`, median `0.057851`, mae `0.054498`
- 20d: sample `20`, hit `0.85`, avg `0.045646`, median `0.06573`, mae `0.069407`
- 60d: sample `20`, hit `0.75`, avg `0.065317`, median `0.099383`, mae `0.107855`

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
- 3d: sample `20`, hit `0.65`, avg `0.003392`, median `0.011957`, mae `0.024993`
- 5d: sample `20`, hit `0.7`, avg `0.019399`, median `0.020777`, mae `0.029387`
- 10d: sample `20`, hit `0.8`, avg `0.035685`, median `0.057851`, mae `0.054498`
- 20d: sample `20`, hit `0.85`, avg `0.045646`, median `0.06573`, mae `0.069407`
- 60d: sample `20`, hit `0.75`, avg `0.065317`, median `0.099383`, mae `0.107855`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.007578`, median `0.011636`, mae `0.018828`
- 5d: sample `40`, hit `0.625`, avg `0.010295`, median `0.013109`, mae `0.023712`
- 10d: sample `40`, hit `0.55`, avg `0.012324`, median `0.011432`, mae `0.039553`
- 20d: sample `40`, hit `0.675`, avg `0.016776`, median `0.029234`, mae `0.05421`
- 60d: sample `40`, hit `0.8`, avg `0.047113`, median `0.054522`, mae `0.063346`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.003406`, median `0.005555`, mae `0.025164`
- 5d: sample `20`, hit `0.5`, avg `-0.01116`, median `0.004527`, mae `0.038466`
- 10d: sample `20`, hit `0.55`, avg `-0.012865`, median `0.014392`, mae `0.064635`
- 20d: sample `20`, hit `0.5`, avg `-0.011342`, median `0.000515`, mae `0.074537`
- 60d: sample `20`, hit `0.55`, avg `-2.2e-05`, median `0.030649`, mae `0.090313`

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
- 3d: sample `80`, hit `0.625`, avg `0.003785`, median `0.01024`, mae `0.021953`
- 5d: sample `80`, hit `0.6125`, avg `0.007207`, median `0.012762`, mae `0.028819`
- 10d: sample `80`, hit `0.6125`, avg `0.011867`, median `0.029984`, mae `0.04956`
- 20d: sample `80`, hit `0.675`, avg `0.016964`, median `0.042025`, mae `0.063091`
- 60d: sample `80`, hit `0.725`, avg `0.03988`, median `0.055989`, mae `0.081215`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.003785`, median `0.01024`, mae `0.021953`
- 5d: sample `80`, hit `0.6125`, avg `0.007207`, median `0.012762`, mae `0.028819`
- 10d: sample `80`, hit `0.6125`, avg `0.011867`, median `0.029984`, mae `0.04956`
- 20d: sample `80`, hit `0.675`, avg `0.016964`, median `0.042025`, mae `0.063091`
- 60d: sample `80`, hit `0.725`, avg `0.03988`, median `0.055989`, mae `0.081215`

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
- 3d: sample `80`, hit `0.625`, avg `0.003785`, median `0.01024`, mae `0.021953`
- 5d: sample `80`, hit `0.6125`, avg `0.007207`, median `0.012762`, mae `0.028819`
- 10d: sample `80`, hit `0.6125`, avg `0.011867`, median `0.029984`, mae `0.04956`
- 20d: sample `80`, hit `0.675`, avg `0.016964`, median `0.042025`, mae `0.063091`
- 60d: sample `80`, hit `0.725`, avg `0.03988`, median `0.055989`, mae `0.081215`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
