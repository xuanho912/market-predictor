# High Confidence Edge Report

Generated at: `2026-11-19T02:47:19.370848+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `204`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `204`, gate `stronger_evidence`
- 5d: completed `204`, gate `stronger_evidence`
- 10d: completed `204`, gate `stronger_evidence`
- 20d: completed `204`, gate `stronger_evidence`
- 60d: completed `204`, gate `stronger_evidence`

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
- 3d: sample `80`, hit `0.6`, avg `0.007111`, median `0.01272`, mae `0.023676`
- 5d: sample `80`, hit `0.65`, avg `0.009283`, median `0.010394`, mae `0.025316`
- 10d: sample `80`, hit `0.6375`, avg `0.013417`, median `0.013222`, mae `0.032581`
- 20d: sample `80`, hit `0.65`, avg `0.015109`, median `0.029234`, mae `0.043602`
- 60d: sample `80`, hit `0.7`, avg `0.049258`, median `0.065834`, mae `0.076479`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.018561`, median `0.025423`, mae `0.029127`
- 5d: sample `8`, hit `0.625`, avg `0.023159`, median `0.032792`, mae `0.037463`
- 10d: sample `8`, hit `0.625`, avg `0.030345`, median `0.01609`, mae `0.044521`
- 20d: sample `8`, hit `1.0`, avg `0.046688`, median `0.036029`, mae `0.046688`
- 60d: sample `8`, hit `0.875`, avg `0.104204`, median `0.130037`, mae `0.110098`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.007704`, median `0.008733`, mae `0.016646`
- 5d: sample `8`, hit `0.75`, avg `0.007226`, median `0.002223`, mae `0.013124`
- 10d: sample `8`, hit `0.625`, avg `0.009285`, median `0.011432`, mae `0.028815`
- 20d: sample `8`, hit `0.625`, avg `0.017592`, median `0.033017`, mae `0.028213`
- 60d: sample `8`, hit `0.5`, avg `0.018306`, median `0.048963`, mae `0.059441`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.007704, 'median_return': 0.008733, 'mean_absolute_return': 0.016646, 'max_adverse_excursion': -0.030262, 'max_favorable_excursion': 0.034466}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.007226, 'median_return': 0.002223, 'mean_absolute_return': 0.013124, 'max_adverse_excursion': -0.021344, 'max_favorable_excursion': 0.047293}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.009285, 'median_return': 0.011432, 'mean_absolute_return': 0.028815, 'max_adverse_excursion': -0.038485, 'max_favorable_excursion': 0.059136}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.017592, 'median_return': 0.033017, 'mean_absolute_return': 0.028213, 'max_adverse_excursion': -0.034684, 'max_favorable_excursion': 0.061413}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.018306, 'median_return': 0.048963, 'mean_absolute_return': 0.059441, 'max_adverse_excursion': -0.061859, 'max_favorable_excursion': 0.109145}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.007045, 'median_return': 0.013397, 'mean_absolute_return': 0.024458, 'max_adverse_excursion': -0.063847, 'max_favorable_excursion': 0.059607}, '5d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.009512, 'median_return': 0.011143, 'mean_absolute_return': 0.02667, 'max_adverse_excursion': -0.075435, 'max_favorable_excursion': 0.115863}, '10d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.013876, 'median_return': 0.014135, 'mean_absolute_return': 0.033, 'max_adverse_excursion': -0.139978, 'max_favorable_excursion': 0.137031}, '20d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.014833, 'median_return': 0.029234, 'mean_absolute_return': 0.045312, 'max_adverse_excursion': -0.302412, 'max_favorable_excursion': 0.162865}, '60d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.052698, 'median_return': 0.067551, 'mean_absolute_return': 0.078372, 'max_adverse_excursion': -0.147091, 'max_favorable_excursion': 0.229735}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4}, '5d': {'sample_size': 80, 'hit_rate': 0.35}, '10d': {'sample_size': 80, 'hit_rate': 0.35}, '20d': {'sample_size': 80, 'hit_rate': 0.35}, '60d': {'sample_size': 80, 'hit_rate': 0.3}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.2, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.2875, 'both_hit': 0, 'both_miss': 1}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': -0.4, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.012001, 'median_return': 0.023822, 'mean_absolute_return': 0.031804, 'max_adverse_excursion': -0.063847, 'max_favorable_excursion': 0.058752}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.012002, 'median_return': 0.017332, 'mean_absolute_return': 0.035659, 'max_adverse_excursion': -0.075435, 'max_favorable_excursion': 0.115863}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.007271, 'median_return': 0.005477, 'mean_absolute_return': 0.048357, 'max_adverse_excursion': -0.139978, 'max_favorable_excursion': 0.137031}, '20d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.018767, 'median_return': 0.035803, 'mean_absolute_return': 0.05668, 'max_adverse_excursion': -0.302412, 'max_favorable_excursion': 0.162865}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.078703, 'median_return': 0.115379, 'mean_absolute_return': 0.098242, 'max_adverse_excursion': -0.142729, 'max_favorable_excursion': 0.193298}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.005481, 'median_return': 0.008733, 'mean_absolute_return': 0.020967, 'max_adverse_excursion': -0.05525, 'max_favorable_excursion': 0.059607}, '5d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.008377, 'median_return': 0.010394, 'mean_absolute_return': 0.021868, 'max_adverse_excursion': -0.05312, 'max_favorable_excursion': 0.063815}, '10d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.015465, 'median_return': 0.015974, 'mean_absolute_return': 0.027322, 'max_adverse_excursion': -0.039064, 'max_favorable_excursion': 0.077422}, '20d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.01389, 'median_return': 0.025178, 'mean_absolute_return': 0.039243, 'max_adverse_excursion': -0.098675, 'max_favorable_excursion': 0.101612}, '60d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.039444, 'median_return': 0.054522, 'mean_absolute_return': 0.069225, 'max_adverse_excursion': -0.147091, 'max_favorable_excursion': 0.229735}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.006548`, median `0.010671`, mae `0.024298`
- 5d: sample `40`, hit `0.55`, avg `0.005741`, median `0.000989`, mae `0.025119`
- 10d: sample `40`, hit `0.525`, avg `0.006507`, median `0.005477`, mae `0.034961`
- 20d: sample `40`, hit `0.65`, avg `0.015808`, median `0.030606`, mae `0.04435`
- 60d: sample `40`, hit `0.725`, avg `0.059506`, median `0.072891`, mae `0.082875`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5667`, avg `0.005481`, median `0.008733`, mae `0.020967`
- 5d: sample `60`, hit `0.6667`, avg `0.008377`, median `0.010394`, mae `0.021868`
- 10d: sample `60`, hit `0.6667`, avg `0.015465`, median `0.015974`, mae `0.027322`
- 20d: sample `60`, hit `0.6167`, avg `0.01389`, median `0.025178`, mae `0.039243`
- 60d: sample `60`, hit `0.6667`, avg `0.039444`, median `0.054522`, mae `0.069225`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.5667`, avg `0.005481`, median `0.008733`, mae `0.020967`
- 5d: sample `60`, hit `0.6667`, avg `0.008377`, median `0.010394`, mae `0.021868`
- 10d: sample `60`, hit `0.6667`, avg `0.015465`, median `0.015974`, mae `0.027322`
- 20d: sample `60`, hit `0.6167`, avg `0.01389`, median `0.025178`, mae `0.039243`
- 60d: sample `60`, hit `0.6667`, avg `0.039444`, median `0.054522`, mae `0.069225`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.005213`, median `0.007316`, mae `0.015856`
- 5d: sample `20`, hit `0.7`, avg `0.007105`, median `0.010394`, mae `0.01658`
- 10d: sample `20`, hit `0.65`, avg `0.010941`, median `0.011855`, mae `0.023905`
- 20d: sample `20`, hit `0.75`, avg `0.024086`, median `0.036447`, mae `0.030996`
- 60d: sample `20`, hit `0.75`, avg `0.038037`, median `0.049972`, mae `0.053147`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6`, avg `0.007111`, median `0.01272`, mae `0.023676`
- 5d: sample `80`, hit `0.65`, avg `0.009283`, median `0.010394`, mae `0.025316`
- 10d: sample `80`, hit `0.6375`, avg `0.013417`, median `0.013222`, mae `0.032581`
- 20d: sample `80`, hit `0.65`, avg `0.015109`, median `0.029234`, mae `0.043602`
- 60d: sample `80`, hit `0.7`, avg `0.049258`, median `0.065834`, mae `0.076479`

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
- 3d: sample `80`, hit `0.6`, avg `0.007111`, median `0.01272`, mae `0.023676`
- 5d: sample `80`, hit `0.65`, avg `0.009283`, median `0.010394`, mae `0.025316`
- 10d: sample `80`, hit `0.6375`, avg `0.013417`, median `0.013222`, mae `0.032581`
- 20d: sample `80`, hit `0.65`, avg `0.015109`, median `0.029234`, mae `0.043602`
- 60d: sample `80`, hit `0.7`, avg `0.049258`, median `0.065834`, mae `0.076479`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
