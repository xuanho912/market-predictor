# High Confidence Edge Report

Generated at: `2026-11-05T01:56:06.793641+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `164`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `164`, gate `stronger_evidence`
- 5d: completed `164`, gate `stronger_evidence`
- 10d: completed `164`, gate `stronger_evidence`
- 20d: completed `164`, gate `stronger_evidence`
- 60d: completed `164`, gate `stronger_evidence`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.004828`, median `0.009859`, mae `0.020136`
- 5d: sample `80`, hit `0.5625`, avg `0.001975`, median `0.005387`, mae `0.025819`
- 10d: sample `80`, hit `0.4875`, avg `-0.003825`, median `-0.00304`, mae `0.040429`
- 20d: sample `80`, hit `0.4625`, avg `-0.011146`, median `-0.017316`, mae `0.045559`
- 60d: sample `80`, hit `0.8375`, avg `0.063218`, median `0.066018`, mae `0.072383`

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
- 3d: sample `8`, hit `0.5`, avg `0.004536`, median `0.017631`, mae `0.01986`
- 5d: sample `8`, hit `0.625`, avg `0.003249`, median `0.002812`, mae `0.027528`
- 10d: sample `8`, hit `0.5`, avg `0.002268`, median `0.036012`, mae `0.043349`
- 20d: sample `8`, hit `0.5`, avg `-0.004281`, median `0.02284`, mae `0.038002`
- 60d: sample `8`, hit `0.875`, avg `0.052016`, median `0.069082`, mae `0.054554`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.004536`, median `0.017631`, mae `0.01986`
- 5d: sample `8`, hit `0.625`, avg `0.003249`, median `0.002812`, mae `0.027528`
- 10d: sample `8`, hit `0.5`, avg `0.002268`, median `0.036012`, mae `0.043349`
- 20d: sample `8`, hit `0.5`, avg `-0.004281`, median `0.02284`, mae `0.038002`
- 60d: sample `8`, hit `0.875`, avg `0.052016`, median `0.069082`, mae `0.054554`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.004536, 'median_return': 0.017631, 'mean_absolute_return': 0.01986, 'max_adverse_excursion': -0.026722, 'max_favorable_excursion': 0.037129}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.003249, 'median_return': 0.002812, 'mean_absolute_return': 0.027528, 'max_adverse_excursion': -0.039725, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.002268, 'median_return': 0.036012, 'mean_absolute_return': 0.043349, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.054673}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.004281, 'median_return': 0.02284, 'mean_absolute_return': 0.038002, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.057759}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.052016, 'median_return': 0.069082, 'mean_absolute_return': 0.054554, 'max_adverse_excursion': -0.010153, 'max_favorable_excursion': 0.090399}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.004861, 'median_return': 0.009859, 'mean_absolute_return': 0.020166, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.001833, 'median_return': 0.006018, 'mean_absolute_return': 0.025629, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.059395}, '10d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.004501, 'median_return': -0.00304, 'mean_absolute_return': 0.040105, 'max_adverse_excursion': -0.120976, 'max_favorable_excursion': 0.080901}, '20d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': -0.011909, 'median_return': -0.017316, 'mean_absolute_return': 0.046399, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.086095}, '60d': {'sample_size': 72, 'hit_rate': 0.8333, 'avg_return': 0.064463, 'median_return': 0.066018, 'mean_absolute_return': 0.074364, 'max_adverse_excursion': -0.056636, 'max_favorable_excursion': 0.188608}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.475}, '5d': {'sample_size': 80, 'hit_rate': 0.4625}, '10d': {'sample_size': 80, 'hit_rate': 0.4375}, '20d': {'sample_size': 80, 'hit_rate': 0.4125}, '60d': {'sample_size': 80, 'hit_rate': 0.4375}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.004831, 'median_return': 0.008833, 'mean_absolute_return': 0.017909, 'max_adverse_excursion': -0.038555, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.001999, 'median_return': 0.002574, 'mean_absolute_return': 0.023846, 'max_adverse_excursion': -0.041734, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.005485, 'median_return': -0.008597, 'mean_absolute_return': 0.040679, 'max_adverse_excursion': -0.110898, 'max_favorable_excursion': 0.080901}, '20d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.012205, 'median_return': -0.019606, 'mean_absolute_return': 0.046801, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 60, 'hit_rate': 0.7833, 'avg_return': 0.048979, 'median_return': 0.055986, 'mean_absolute_return': 0.061198, 'max_adverse_excursion': -0.056636, 'max_favorable_excursion': 0.1437}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.00482, 'median_return': 0.01249, 'mean_absolute_return': 0.026816, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.044418}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.001902, 'median_return': 0.009561, 'mean_absolute_return': 0.031741, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.059395}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.001156, 'median_return': 0.009015, 'mean_absolute_return': 0.03968, 'max_adverse_excursion': -0.120976, 'max_favorable_excursion': 0.075219}, '20d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.00797, 'median_return': 0.000594, 'mean_absolute_return': 0.041835, 'max_adverse_excursion': -0.099264, 'max_favorable_excursion': 0.086095}, '60d': {'sample_size': 20, 'hit_rate': 1.0, 'avg_return': 0.105937, 'median_return': 0.109805, 'mean_absolute_return': 0.105937, 'max_adverse_excursion': 0.01793, 'max_favorable_excursion': 0.188608}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.004831`, median `0.008833`, mae `0.017909`
- 5d: sample `60`, hit `0.5333`, avg `0.001999`, median `0.002574`, mae `0.023846`
- 10d: sample `60`, hit `0.45`, avg `-0.005485`, median `-0.008597`, mae `0.040679`
- 20d: sample `60`, hit `0.45`, avg `-0.012205`, median `-0.019606`, mae `0.046801`
- 60d: sample `60`, hit `0.7833`, avg `0.048979`, median `0.055986`, mae `0.061198`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.00482`, median `0.01249`, mae `0.026816`
- 5d: sample `20`, hit `0.65`, avg `0.001902`, median `0.009561`, mae `0.031741`
- 10d: sample `20`, hit `0.6`, avg `0.001156`, median `0.009015`, mae `0.03968`
- 20d: sample `20`, hit `0.5`, avg `-0.00797`, median `0.000594`, mae `0.041835`
- 60d: sample `20`, hit `1.0`, avg `0.105937`, median `0.109805`, mae `0.105937`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.003221`, median `0.008174`, mae `0.017666`
- 5d: sample `40`, hit `0.525`, avg `0.000386`, median `0.002574`, mae `0.023619`
- 10d: sample `40`, hit `0.425`, avg `-0.005618`, median `-0.013567`, mae `0.039176`
- 20d: sample `40`, hit `0.375`, avg `-0.014161`, median `-0.021765`, mae `0.045937`
- 60d: sample `40`, hit `0.775`, avg `0.040648`, median `0.047238`, mae `0.050846`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.003221`, median `0.008174`, mae `0.017666`
- 5d: sample `40`, hit `0.525`, avg `0.000386`, median `0.002574`, mae `0.023619`
- 10d: sample `40`, hit `0.425`, avg `-0.005618`, median `-0.013567`, mae `0.039176`
- 20d: sample `40`, hit `0.375`, avg `-0.014161`, median `-0.021765`, mae `0.045937`
- 60d: sample `40`, hit `0.775`, avg `0.040648`, median `0.047238`, mae `0.050846`

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
- 3d: sample `20`, hit `0.65`, avg `0.00482`, median `0.01249`, mae `0.026816`
- 5d: sample `20`, hit `0.65`, avg `0.001902`, median `0.009561`, mae `0.031741`
- 10d: sample `20`, hit `0.6`, avg `0.001156`, median `0.009015`, mae `0.03968`
- 20d: sample `20`, hit `0.5`, avg `-0.00797`, median `0.000594`, mae `0.041835`
- 60d: sample `20`, hit `1.0`, avg `0.105937`, median `0.109805`, mae `0.105937`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.003221`, median `0.008174`, mae `0.017666`
- 5d: sample `40`, hit `0.525`, avg `0.000386`, median `0.002574`, mae `0.023619`
- 10d: sample `40`, hit `0.425`, avg `-0.005618`, median `-0.013567`, mae `0.039176`
- 20d: sample `40`, hit `0.375`, avg `-0.014161`, median `-0.021765`, mae `0.045937`
- 60d: sample `40`, hit `0.775`, avg `0.040648`, median `0.047238`, mae `0.050846`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008051`, median `0.010308`, mae `0.018394`
- 5d: sample `20`, hit `0.55`, avg `0.005225`, median `0.007168`, mae `0.0243`
- 10d: sample `20`, hit `0.5`, avg `-0.005218`, median `0.001411`, mae `0.043686`
- 20d: sample `20`, hit `0.6`, avg `-0.008291`, median `0.019563`, mae `0.048529`
- 60d: sample `20`, hit `0.8`, avg `0.065641`, median `0.096389`, mae `0.081904`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.003221`, median `0.008174`, mae `0.017666`
- 5d: sample `40`, hit `0.525`, avg `0.000386`, median `0.002574`, mae `0.023619`
- 10d: sample `40`, hit `0.425`, avg `-0.005618`, median `-0.013567`, mae `0.039176`
- 20d: sample `40`, hit `0.375`, avg `-0.014161`, median `-0.021765`, mae `0.045937`
- 60d: sample `40`, hit `0.775`, avg `0.040648`, median `0.047238`, mae `0.050846`

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
- 3d: sample `80`, hit `0.625`, avg `0.004828`, median `0.009859`, mae `0.020136`
- 5d: sample `80`, hit `0.5625`, avg `0.001975`, median `0.005387`, mae `0.025819`
- 10d: sample `80`, hit `0.4875`, avg `-0.003825`, median `-0.00304`, mae `0.040429`
- 20d: sample `80`, hit `0.4625`, avg `-0.011146`, median `-0.017316`, mae `0.045559`
- 60d: sample `80`, hit `0.8375`, avg `0.063218`, median `0.066018`, mae `0.072383`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.004828`, median `0.009859`, mae `0.020136`
- 5d: sample `80`, hit `0.5625`, avg `0.001975`, median `0.005387`, mae `0.025819`
- 10d: sample `80`, hit `0.4875`, avg `-0.003825`, median `-0.00304`, mae `0.040429`
- 20d: sample `80`, hit `0.4625`, avg `-0.011146`, median `-0.017316`, mae `0.045559`
- 60d: sample `80`, hit `0.8375`, avg `0.063218`, median `0.066018`, mae `0.072383`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.003221`, median `0.008174`, mae `0.017666`
- 5d: sample `40`, hit `0.525`, avg `0.000386`, median `0.002574`, mae `0.023619`
- 10d: sample `40`, hit `0.425`, avg `-0.005618`, median `-0.013567`, mae `0.039176`
- 20d: sample `40`, hit `0.375`, avg `-0.014161`, median `-0.021765`, mae `0.045937`
- 60d: sample `40`, hit `0.775`, avg `0.040648`, median `0.047238`, mae `0.050846`

### bounce_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.003221`, median `0.008174`, mae `0.017666`
- 5d: sample `40`, hit `0.525`, avg `0.000386`, median `0.002574`, mae `0.023619`
- 10d: sample `40`, hit `0.425`, avg `-0.005618`, median `-0.013567`, mae `0.039176`
- 20d: sample `40`, hit `0.375`, avg `-0.014161`, median `-0.021765`, mae `0.045937`
- 60d: sample `40`, hit `0.775`, avg `0.040648`, median `0.047238`, mae `0.050846`

### risk_path_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.006436`, median `0.010308`, mae `0.022605`
- 5d: sample `40`, hit `0.6`, avg `0.003563`, median `0.007257`, mae `0.02802`
- 10d: sample `40`, hit `0.55`, avg `-0.002031`, median `0.008188`, mae `0.041683`
- 20d: sample `40`, hit `0.55`, avg `-0.008131`, median `0.004568`, mae `0.045182`
- 60d: sample `40`, hit `0.9`, avg `0.085789`, median `0.100324`, mae `0.09392`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
