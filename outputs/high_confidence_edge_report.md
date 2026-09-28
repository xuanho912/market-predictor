# High Confidence Edge Report

Generated at: `2026-09-28T19:43:15.332663+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `56`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `56`, gate `moderate_evidence`
- 5d: completed `56`, gate `moderate_evidence`
- 10d: completed `56`, gate `moderate_evidence`
- 20d: completed `56`, gate `moderate_evidence`
- 60d: completed `56`, gate `moderate_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.00283`, median `0.0054`, mae `0.014736`
- 5d: sample `20`, hit `0.6`, avg `-0.001374`, median `0.006609`, mae `0.018197`
- 10d: sample `20`, hit `0.6`, avg `-0.00473`, median `0.004196`, mae `0.020775`
- 20d: sample `20`, hit `0.65`, avg `0.009844`, median `0.015416`, mae `0.028962`
- 60d: sample `20`, hit `0.85`, avg `0.052197`, median `0.059104`, mae `0.068146`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.3333`, avg `-0.010151`, median `-0.010023`, mae `0.019106`
- 5d: sample `60`, hit `0.3833`, avg `-0.012954`, median `-0.007994`, mae `0.021191`
- 10d: sample `60`, hit `0.45`, avg `-0.005649`, median `-0.004767`, mae `0.029164`
- 20d: sample `60`, hit `0.6167`, avg `0.010769`, median `0.026113`, mae `0.04904`
- 60d: sample `60`, hit `0.8`, avg `0.049146`, median `0.072696`, mae `0.087929`

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
- 3d: sample `8`, hit `0.75`, avg `0.006361`, median `0.012217`, mae `0.014719`
- 5d: sample `8`, hit `0.75`, avg `0.002239`, median `0.007043`, mae `0.01236`
- 10d: sample `8`, hit `0.625`, avg `-0.000775`, median `0.007751`, mae `0.014605`
- 20d: sample `8`, hit `0.75`, avg `0.024693`, median `0.045453`, mae `0.030593`
- 60d: sample `8`, hit `1.0`, avg `0.054033`, median `0.059104`, mae `0.054033`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.006361`, median `0.012217`, mae `0.014719`
- 5d: sample `8`, hit `0.75`, avg `0.002239`, median `0.007043`, mae `0.01236`
- 10d: sample `8`, hit `0.625`, avg `-0.000775`, median `0.007751`, mae `0.014605`
- 20d: sample `8`, hit `0.75`, avg `0.024693`, median `0.045453`, mae `0.030593`
- 60d: sample `8`, hit `1.0`, avg `0.054033`, median `0.059104`, mae `0.054033`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.00283, 'median_return': 0.0054, 'mean_absolute_return': 0.014736, 'max_adverse_excursion': -0.029438, 'max_favorable_excursion': 0.026049}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.001374, 'median_return': 0.006609, 'mean_absolute_return': 0.018197, 'max_adverse_excursion': -0.049407, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.00473, 'median_return': 0.004196, 'mean_absolute_return': 0.020775, 'max_adverse_excursion': -0.06798, 'max_favorable_excursion': 0.035149}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.009844, 'median_return': 0.015416, 'mean_absolute_return': 0.028962, 'max_adverse_excursion': -0.051442, 'max_favorable_excursion': 0.057835}, '60d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.052197, 'median_return': 0.059104, 'mean_absolute_return': 0.068146, 'max_adverse_excursion': -0.089779, 'max_favorable_excursion': 0.142584}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.006361, 'median_return': 0.012217, 'mean_absolute_return': 0.014719, 'max_adverse_excursion': -0.029438, 'max_favorable_excursion': 0.023486}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.002239, 'median_return': 0.007043, 'mean_absolute_return': 0.01236, 'max_adverse_excursion': -0.027246, 'max_favorable_excursion': 0.018625}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.000775, 'median_return': 0.007751, 'mean_absolute_return': 0.014605, 'max_adverse_excursion': -0.025298, 'max_favorable_excursion': 0.018352}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.024693, 'median_return': 0.045453, 'mean_absolute_return': 0.030593, 'max_adverse_excursion': -0.015145, 'max_favorable_excursion': 0.056558}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.054033, 'median_return': 0.059104, 'mean_absolute_return': 0.054033, 'max_adverse_excursion': 0.002294, 'max_favorable_excursion': 0.114629}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.3611, 'avg_return': -0.00838, 'median_return': -0.006207, 'mean_absolute_return': 0.018379, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.033159}, '5d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.011425, 'median_return': -0.007994, 'mean_absolute_return': 0.021341, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.005935, 'median_return': -0.0004, 'mean_absolute_return': 0.028451, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.008965, 'median_return': 0.016745, 'mean_absolute_return': 0.045513, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.7917, 'avg_return': 0.04945, 'median_return': 0.065995, 'mean_absolute_return': 0.0862, 'max_adverse_excursion': -0.184447, 'max_favorable_excursion': 0.176653}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.65}, '5d': {'sample_size': 80, 'hit_rate': 0.6125}, '10d': {'sample_size': 80, 'hit_rate': 0.5625}, '20d': {'sample_size': 80, 'hit_rate': 0.45}, '60d': {'sample_size': 80, 'hit_rate': 0.3625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.35, 'primary_minus_secondary': 0.3, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_minus_secondary': 0.225, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.125, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.275, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': -0.002771, 'median_return': 0.001199, 'mean_absolute_return': 0.016995, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.033159}, '5d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': -0.007267, 'median_return': 0.000863, 'mean_absolute_return': 0.019113, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': -0.004814, 'median_return': 0.000397, 'mean_absolute_return': 0.021936, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.051039}, '20d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.011737, 'median_return': 0.021759, 'mean_absolute_return': 0.039311, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 60, 'hit_rate': 0.8167, 'avg_return': 0.044375, 'median_return': 0.057507, 'mean_absolute_return': 0.073664, 'max_adverse_excursion': -0.146095, 'max_favorable_excursion': 0.167846}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.1, 'avg_return': -0.019312, 'median_return': -0.014972, 'mean_absolute_return': 0.021069, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.011534}, '5d': {'sample_size': 20, 'hit_rate': 0.2, 'avg_return': -0.018436, 'median_return': -0.013229, 'mean_absolute_return': 0.024431, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.023861}, '10d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.007234, 'median_return': -0.006032, 'mean_absolute_return': 0.042458, 'max_adverse_excursion': -0.080172, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': 0.006937, 'median_return': -0.00045, 'mean_absolute_return': 0.058149, 'max_adverse_excursion': -0.082211, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.066508, 'median_return': 0.113908, 'mean_absolute_return': 0.110939, 'max_adverse_excursion': -0.184447, 'max_favorable_excursion': 0.176653}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.003689`, median `0.001199`, mae `0.019442`
- 5d: sample `40`, hit `0.45`, avg `-0.009478`, median `-0.007994`, mae `0.021957`
- 10d: sample `40`, hit `0.425`, avg `-0.010821`, median `-0.006017`, mae `0.022349`
- 20d: sample `40`, hit `0.6`, avg `0.004847`, median `0.015416`, mae `0.037835`
- 60d: sample `40`, hit `0.775`, avg `0.042938`, median `0.059104`, mae `0.077357`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.3`, avg `-0.010123`, median `-0.009843`, mae `0.016584`
- 5d: sample `40`, hit `0.425`, avg `-0.01064`, median `-0.002452`, mae `0.018928`
- 10d: sample `40`, hit `0.55`, avg `-1.7e-05`, median `0.006604`, mae `0.031784`
- 20d: sample `40`, hit `0.65`, avg `0.016227`, median `0.032102`, mae `0.050206`
- 60d: sample `40`, hit `0.85`, avg `0.056878`, median `0.075223`, mae `0.088609`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.00283`, median `0.0054`, mae `0.014736`
- 5d: sample `20`, hit `0.6`, avg `-0.001374`, median `0.006609`, mae `0.018197`
- 10d: sample `20`, hit `0.6`, avg `-0.00473`, median `0.004196`, mae `0.020775`
- 20d: sample `20`, hit `0.65`, avg `0.009844`, median `0.015416`, mae `0.028962`
- 60d: sample `20`, hit `0.85`, avg `0.052197`, median `0.059104`, mae `0.068146`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.00283`, median `0.0054`, mae `0.014736`
- 5d: sample `20`, hit `0.6`, avg `-0.001374`, median `0.006609`, mae `0.018197`
- 10d: sample `20`, hit `0.6`, avg `-0.00473`, median `0.004196`, mae `0.020775`
- 20d: sample `20`, hit `0.65`, avg `0.009844`, median `0.015416`, mae `0.028962`
- 60d: sample `20`, hit `0.85`, avg `0.052197`, median `0.059104`, mae `0.068146`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.00283`, median `0.0054`, mae `0.014736`
- 5d: sample `20`, hit `0.6`, avg `-0.001374`, median `0.006609`, mae `0.018197`
- 10d: sample `20`, hit `0.6`, avg `-0.00473`, median `0.004196`, mae `0.020775`
- 20d: sample `20`, hit `0.65`, avg `0.009844`, median `0.015416`, mae `0.028962`
- 60d: sample `20`, hit `0.85`, avg `0.052197`, median `0.059104`, mae `0.068146`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.00283`, median `0.0054`, mae `0.014736`
- 5d: sample `20`, hit `0.6`, avg `-0.001374`, median `0.006609`, mae `0.018197`
- 10d: sample `20`, hit `0.6`, avg `-0.00473`, median `0.004196`, mae `0.020775`
- 20d: sample `20`, hit `0.65`, avg `0.009844`, median `0.015416`, mae `0.028962`
- 60d: sample `20`, hit `0.85`, avg `0.052197`, median `0.059104`, mae `0.068146`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.3`, avg `-0.010123`, median `-0.009843`, mae `0.016584`
- 5d: sample `40`, hit `0.425`, avg `-0.01064`, median `-0.002452`, mae `0.018928`
- 10d: sample `40`, hit `0.55`, avg `-1.7e-05`, median `0.006604`, mae `0.031784`
- 20d: sample `40`, hit `0.65`, avg `0.016227`, median `0.032102`, mae `0.050206`
- 60d: sample `40`, hit `0.85`, avg `0.056878`, median `0.075223`, mae `0.088609`

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
- 3d: sample `80`, hit `0.4`, avg `-0.006906`, median `-0.003995`, mae `0.018013`
- 5d: sample `80`, hit `0.4375`, avg `-0.010059`, median `-0.005632`, mae `0.020443`
- 10d: sample `80`, hit `0.4875`, avg `-0.005419`, median `-0.000231`, mae `0.027067`
- 20d: sample `80`, hit `0.625`, avg `0.010537`, median `0.01927`, mae `0.044021`
- 60d: sample `80`, hit `0.8125`, avg `0.049908`, median `0.060702`, mae `0.082983`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.00283`, median `0.0054`, mae `0.014736`
- 5d: sample `20`, hit `0.6`, avg `-0.001374`, median `0.006609`, mae `0.018197`
- 10d: sample `20`, hit `0.6`, avg `-0.00473`, median `0.004196`, mae `0.020775`
- 20d: sample `20`, hit `0.65`, avg `0.009844`, median `0.015416`, mae `0.028962`
- 60d: sample `20`, hit `0.85`, avg `0.052197`, median `0.059104`, mae `0.068146`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.000934`, median `0.002101`, mae `0.0121`
- 5d: sample `20`, hit `0.65`, avg `-0.002844`, median `0.001654`, mae `0.013425`
- 10d: sample `20`, hit `0.65`, avg `0.0072`, median `0.012066`, mae `0.021111`
- 20d: sample `20`, hit `0.85`, avg `0.025518`, median `0.033164`, mae `0.042263`
- 60d: sample `20`, hit `0.9`, avg `0.047248`, median `0.057507`, mae `0.066278`

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
