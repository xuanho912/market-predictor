# High Confidence Edge Report

Generated at: `2026-09-04T06:00:06.082666+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `0`
Forward validation notice: `当前高置信度还没有被前向样本验证，不应当视为稳定预测能力。`
Conclusion: `forward_validation_insufficient_keep_confidence_capped`

## Forward Sample Gates

- 3d: completed `0`, gate `insufficient`
- 5d: completed `0`, gate `insufficient`
- 10d: completed `0`, gate `insufficient`
- 20d: completed `0`, gate `insufficient`
- 60d: completed `0`, gate `insufficient`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.004762`, median `0.009349`, mae `0.01918`
- 5d: sample `80`, hit `0.6125`, avg `0.006319`, median `0.009709`, mae `0.021409`
- 10d: sample `80`, hit `0.6625`, avg `0.013032`, median `0.013913`, mae `0.027776`
- 20d: sample `80`, hit `0.7625`, avg `0.027055`, median `0.031464`, mae `0.035849`
- 60d: sample `80`, hit `0.725`, avg `0.05099`, median `0.073403`, mae `0.082495`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.001901`, median `-0.001591`, mae `0.014636`
- 5d: sample `8`, hit `0.75`, avg `0.006282`, median `0.009709`, mae `0.018419`
- 10d: sample `8`, hit `0.625`, avg `0.009959`, median `0.013069`, mae `0.019184`
- 20d: sample `8`, hit `0.875`, avg `0.042258`, median `0.058396`, mae `0.043435`
- 60d: sample `8`, hit `1.0`, avg `0.099899`, median `0.121826`, mae `0.099899`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.001901`, median `-0.001591`, mae `0.014636`
- 5d: sample `8`, hit `0.75`, avg `0.006282`, median `0.009709`, mae `0.018419`
- 10d: sample `8`, hit `0.625`, avg `0.009959`, median `0.013069`, mae `0.019184`
- 20d: sample `8`, hit `0.875`, avg `0.042258`, median `0.058396`, mae `0.043435`
- 60d: sample `8`, hit `1.0`, avg `0.099899`, median `0.121826`, mae `0.099899`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.004762, 'median_return': 0.009349, 'mean_absolute_return': 0.01918, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.047995}, '5d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.006319, 'median_return': 0.009709, 'mean_absolute_return': 0.021409, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.062217}, '10d': {'sample_size': 80, 'hit_rate': 0.6625, 'avg_return': 0.013032, 'median_return': 0.013913, 'mean_absolute_return': 0.027776, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.098213}, '20d': {'sample_size': 80, 'hit_rate': 0.7625, 'avg_return': 0.027055, 'median_return': 0.031464, 'mean_absolute_return': 0.035849, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.110981}, '60d': {'sample_size': 80, 'hit_rate': 0.725, 'avg_return': 0.05099, 'median_return': 0.073403, 'mean_absolute_return': 0.082495, 'max_adverse_excursion': -0.171649, 'max_favorable_excursion': 0.220253}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.001901, 'median_return': -0.001591, 'mean_absolute_return': 0.014636, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.006282, 'median_return': 0.009709, 'mean_absolute_return': 0.018419, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.027457}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.009959, 'median_return': 0.013069, 'mean_absolute_return': 0.019184, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.036071}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.042258, 'median_return': 0.058396, 'mean_absolute_return': 0.043435, 'max_adverse_excursion': -0.00471, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.099899, 'median_return': 0.121826, 'mean_absolute_return': 0.099899, 'max_adverse_excursion': 0.024156, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.005503, 'median_return': 0.010897, 'mean_absolute_return': 0.019685, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.047995}, '5d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.006324, 'median_return': 0.01152, 'mean_absolute_return': 0.021741, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.062217}, '10d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.013374, 'median_return': 0.015799, 'mean_absolute_return': 0.028731, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.098213}, '20d': {'sample_size': 72, 'hit_rate': 0.75, 'avg_return': 0.025366, 'median_return': 0.030922, 'mean_absolute_return': 0.035006, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.110981}, '60d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.045556, 'median_return': 0.068712, 'mean_absolute_return': 0.080561, 'max_adverse_excursion': -0.171649, 'max_favorable_excursion': 0.220253}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4875}, '5d': {'sample_size': 80, 'hit_rate': 0.5125}, '10d': {'sample_size': 80, 'hit_rate': 0.5625}, '20d': {'sample_size': 80, 'hit_rate': 0.6125}, '60d': {'sample_size': 80, 'hit_rate': 0.65}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.15, 'both_hit': 25, 'both_miss': 15}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.1, 'both_hit': 25, 'both_miss': 15}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.075, 'both_hit': 28, 'both_miss': 12}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.025, 'both_hit': 30, 'both_miss': 10}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.025, 'both_hit': 33, 'both_miss': 7}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.004762, 'median_return': 0.009349, 'mean_absolute_return': 0.01918, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.047995}, '5d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.006319, 'median_return': 0.009709, 'mean_absolute_return': 0.021409, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.062217}, '10d': {'sample_size': 80, 'hit_rate': 0.6625, 'avg_return': 0.013032, 'median_return': 0.013913, 'mean_absolute_return': 0.027776, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.098213}, '20d': {'sample_size': 80, 'hit_rate': 0.7625, 'avg_return': 0.027055, 'median_return': 0.031464, 'mean_absolute_return': 0.035849, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.110981}, '60d': {'sample_size': 80, 'hit_rate': 0.725, 'avg_return': 0.05099, 'median_return': 0.073403, 'mean_absolute_return': 0.082495, 'max_adverse_excursion': -0.171649, 'max_favorable_excursion': 0.220253}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6667`, avg `0.007791`, median `0.012272`, mae `0.01808`
- 5d: sample `60`, hit `0.65`, avg `0.009577`, median `0.012091`, mae `0.019667`
- 10d: sample `60`, hit `0.7`, avg `0.014847`, median `0.013913`, mae `0.024151`
- 20d: sample `60`, hit `0.7667`, avg `0.030783`, median `0.033582`, mae `0.03559`
- 60d: sample `60`, hit `0.7667`, avg `0.062029`, median `0.081673`, mae `0.082929`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.003528`, median `0.00745`, mae `0.015068`
- 5d: sample `40`, hit `0.625`, avg `0.005474`, median `0.008152`, mae `0.01559`
- 10d: sample `40`, hit `0.7`, avg `0.008879`, median `0.011619`, mae `0.018122`
- 20d: sample `40`, hit `0.75`, avg `0.027788`, median `0.031464`, mae `0.033588`
- 60d: sample `40`, hit `0.825`, avg `0.065226`, median `0.084216`, mae `0.077813`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.016319`, median `0.022897`, mae `0.024104`
- 5d: sample `20`, hit `0.7`, avg `0.017783`, median `0.026325`, mae `0.027821`
- 10d: sample `20`, hit `0.7`, avg `0.026784`, median `0.031449`, mae `0.036209`
- 20d: sample `20`, hit `0.8`, avg `0.036772`, median `0.034726`, mae `0.039594`
- 60d: sample `20`, hit `0.65`, avg `0.055634`, median `0.073403`, mae `0.093161`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.5667`, avg `0.00091`, median `0.003757`, mae `0.017538`
- 5d: sample `60`, hit `0.5833`, avg `0.002498`, median `0.00774`, mae `0.019272`
- 10d: sample `60`, hit `0.65`, avg `0.008449`, median `0.011619`, mae `0.024965`
- 20d: sample `60`, hit `0.75`, avg `0.023816`, median `0.029348`, mae `0.034601`
- 60d: sample `60`, hit `0.75`, avg `0.049442`, median `0.074246`, mae `0.078939`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.016319`, median `0.022897`, mae `0.024104`
- 5d: sample `20`, hit `0.7`, avg `0.017783`, median `0.026325`, mae `0.027821`
- 10d: sample `20`, hit `0.7`, avg `0.026784`, median `0.031449`, mae `0.036209`
- 20d: sample `20`, hit `0.8`, avg `0.036772`, median `0.034726`, mae `0.039594`
- 60d: sample `20`, hit `0.65`, avg `0.055634`, median `0.073403`, mae `0.093161`

## Internal Resonance Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Internal-resonance attribution is being tracked, but forward-only samples are still below the minimum gate.`

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
- 3d: sample `80`, hit `0.6125`, avg `0.004762`, median `0.009349`, mae `0.01918`
- 5d: sample `80`, hit `0.6125`, avg `0.006319`, median `0.009709`, mae `0.021409`
- 10d: sample `80`, hit `0.6625`, avg `0.013032`, median `0.013913`, mae `0.027776`
- 20d: sample `80`, hit `0.7625`, avg `0.027055`, median `0.031464`, mae `0.035849`
- 60d: sample `80`, hit `0.725`, avg `0.05099`, median `0.073403`, mae `0.082495`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.5667`, avg `0.00091`, median `0.003757`, mae `0.017538`
- 5d: sample `60`, hit `0.5833`, avg `0.002498`, median `0.00774`, mae `0.019272`
- 10d: sample `60`, hit `0.65`, avg `0.008449`, median `0.011619`, mae `0.024965`
- 20d: sample `60`, hit `0.75`, avg `0.023816`, median `0.029348`, mae `0.034601`
- 60d: sample `60`, hit `0.75`, avg `0.049442`, median `0.074246`, mae `0.078939`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001971`, median `0.0017`, mae `0.018285`
- 5d: sample `40`, hit `0.525`, avg `-0.001214`, median `0.004613`, mae `0.020262`
- 10d: sample `40`, hit `0.625`, avg `0.005732`, median `0.008908`, mae `0.027269`
- 20d: sample `40`, hit `0.75`, avg `0.020599`, median `0.029348`, mae `0.033804`
- 60d: sample `40`, hit `0.7`, avg `0.035694`, median `0.064124`, mae `0.073536`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001971`, median `0.0017`, mae `0.018285`
- 5d: sample `40`, hit `0.525`, avg `-0.001214`, median `0.004613`, mae `0.020262`
- 10d: sample `40`, hit `0.625`, avg `0.005732`, median `0.008908`, mae `0.027269`
- 20d: sample `40`, hit `0.75`, avg `0.020599`, median `0.029348`, mae `0.033804`
- 60d: sample `40`, hit `0.7`, avg `0.035694`, median `0.064124`, mae `0.073536`

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
