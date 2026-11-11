# High Confidence Edge Report

Generated at: `2026-11-11T19:38:46.237391+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `184`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `historical_proxy_supports_higher_confidence_but_forward_validation_required`

## Forward Sample Gates

- 3d: completed `184`, gate `stronger_evidence`
- 5d: completed `184`, gate `stronger_evidence`
- 10d: completed `184`, gate `stronger_evidence`
- 20d: completed `184`, gate `stronger_evidence`
- 60d: completed `184`, gate `stronger_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.000613`, median `-0.001641`, mae `0.014681`
- 5d: sample `60`, hit `0.4667`, avg `-0.000729`, median `-0.003328`, mae `0.018028`
- 10d: sample `60`, hit `0.55`, avg `0.006698`, median `0.0076`, mae `0.025493`
- 20d: sample `60`, hit `0.8`, avg `0.021733`, median `0.024844`, mae `0.031379`
- 60d: sample `60`, hit `0.7333`, avg `0.036901`, median `0.057501`, mae `0.06653`

### MODERATE_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.001511`, median `-0.008802`, mae `0.018317`
- 5d: sample `20`, hit `0.55`, avg `-0.003613`, median `0.004752`, mae `0.021653`
- 10d: sample `20`, hit `0.7`, avg `0.004748`, median `0.010559`, mae `0.027416`
- 20d: sample `20`, hit `0.8`, avg `0.022531`, median `0.036446`, mae `0.038922`
- 60d: sample `20`, hit `0.85`, avg `0.062547`, median `0.071679`, mae `0.072999`

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
- 3d: sample `8`, hit `0.375`, avg `-5e-05`, median `-0.001811`, mae `0.015409`
- 5d: sample `8`, hit `0.375`, avg `0.001194`, median `-0.00855`, mae `0.020848`
- 10d: sample `8`, hit `0.75`, avg `0.021796`, median `0.023979`, mae `0.025241`
- 20d: sample `8`, hit `0.875`, avg `0.033882`, median `0.031658`, mae `0.036263`
- 60d: sample `8`, hit `1.0`, avg `0.079187`, median `0.092646`, mae `0.079187`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.006647`, median `-0.003594`, mae `0.009338`
- 5d: sample `8`, hit `0.25`, avg `-0.009191`, median `-0.010916`, mae `0.014947`
- 10d: sample `8`, hit `0.5`, avg `0.002411`, median `0.009031`, mae `0.014671`
- 20d: sample `8`, hit `0.875`, avg `0.016874`, median `0.020066`, mae `0.019685`
- 60d: sample `8`, hit `1.0`, avg `0.057707`, median `0.078453`, mae `0.057707`

### confidence validation
- `{'strong_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.000613, 'median_return': -0.001641, 'mean_absolute_return': 0.014681, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.000729, 'median_return': -0.003328, 'mean_absolute_return': 0.018028, 'max_adverse_excursion': -0.042713, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.006698, 'median_return': 0.0076, 'mean_absolute_return': 0.025493, 'max_adverse_excursion': -0.058968, 'max_favorable_excursion': 0.060007}, '20d': {'sample_size': 60, 'hit_rate': 0.8, 'avg_return': 0.021733, 'median_return': 0.024844, 'mean_absolute_return': 0.031379, 'max_adverse_excursion': -0.052049, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.036901, 'median_return': 0.057501, 'mean_absolute_return': 0.06653, 'max_adverse_excursion': -0.154456, 'max_favorable_excursion': 0.135457}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.006647, 'median_return': -0.003594, 'mean_absolute_return': 0.009338, 'max_adverse_excursion': -0.023751, 'max_favorable_excursion': 0.006372}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.009191, 'median_return': -0.010916, 'mean_absolute_return': 0.014947, 'max_adverse_excursion': -0.027002, 'max_favorable_excursion': 0.011571}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.002411, 'median_return': 0.009031, 'mean_absolute_return': 0.014671, 'max_adverse_excursion': -0.018368, 'max_favorable_excursion': 0.031945}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.016874, 'median_return': 0.020066, 'mean_absolute_return': 0.019685, 'max_adverse_excursion': -0.011242, 'max_favorable_excursion': 0.032327}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.057707, 'median_return': 0.078453, 'mean_absolute_return': 0.057707, 'max_adverse_excursion': 0.00377, 'max_favorable_excursion': 0.090554}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': -0.000192, 'median_return': -0.000756, 'mean_absolute_return': 0.016285, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.039385}, '5d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': -0.00059, 'median_return': 0.002543, 'mean_absolute_return': 0.019377, 'max_adverse_excursion': -0.042713, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.006632, 'median_return': 0.0076, 'mean_absolute_return': 0.02723, 'max_adverse_excursion': -0.058968, 'max_favorable_excursion': 0.061858}, '20d': {'sample_size': 72, 'hit_rate': 0.7917, 'avg_return': 0.022494, 'median_return': 0.028264, 'mean_absolute_return': 0.034773, 'max_adverse_excursion': -0.082605, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.041713, 'median_return': 0.064194, 'mean_absolute_return': 0.069307, 'max_adverse_excursion': -0.154456, 'max_favorable_excursion': 0.166476}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4875}, '5d': {'sample_size': 80, 'hit_rate': 0.4625}, '10d': {'sample_size': 80, 'hit_rate': 0.4875}, '20d': {'sample_size': 80, 'hit_rate': 0.65}, '60d': {'sample_size': 80, 'hit_rate': 0.5875}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.05, 'both_hit': 27, 'both_miss': 33}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': -0.025, 'both_hit': 28, 'both_miss': 32}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.1, 'both_hit': 33, 'both_miss': 27}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.8, 'primary_minus_secondary': -0.15, 'both_hit': 48, 'both_miss': 12}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.7625, 'primary_minus_secondary': -0.175, 'both_hit': 44, 'both_miss': 16}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.000613, 'median_return': -0.001641, 'mean_absolute_return': 0.014681, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.000729, 'median_return': -0.003328, 'mean_absolute_return': 0.018028, 'max_adverse_excursion': -0.042713, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.006698, 'median_return': 0.0076, 'mean_absolute_return': 0.025493, 'max_adverse_excursion': -0.058968, 'max_favorable_excursion': 0.060007}, '20d': {'sample_size': 60, 'hit_rate': 0.8, 'avg_return': 0.021733, 'median_return': 0.024844, 'mean_absolute_return': 0.031379, 'max_adverse_excursion': -0.052049, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.036901, 'median_return': 0.057501, 'mean_absolute_return': 0.06653, 'max_adverse_excursion': -0.154456, 'max_favorable_excursion': 0.135457}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.001511, 'median_return': -0.008802, 'mean_absolute_return': 0.018317, 'max_adverse_excursion': -0.025828, 'max_favorable_excursion': 0.039385}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.003613, 'median_return': 0.004752, 'mean_absolute_return': 0.021653, 'max_adverse_excursion': -0.040262, 'max_favorable_excursion': 0.034788}, '10d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.004748, 'median_return': 0.010559, 'mean_absolute_return': 0.027416, 'max_adverse_excursion': -0.054711, 'max_favorable_excursion': 0.061858}, '20d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.022531, 'median_return': 0.036446, 'mean_absolute_return': 0.038922, 'max_adverse_excursion': -0.082605, 'max_favorable_excursion': 0.086431}, '60d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.062547, 'median_return': 0.071679, 'mean_absolute_return': 0.072999, 'max_adverse_excursion': -0.071316, 'max_favorable_excursion': 0.166476}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.000613`, median `-0.001641`, mae `0.014681`
- 5d: sample `60`, hit `0.4667`, avg `-0.000729`, median `-0.003328`, mae `0.018028`
- 10d: sample `60`, hit `0.55`, avg `0.006698`, median `0.0076`, mae `0.025493`
- 20d: sample `60`, hit `0.8`, avg `0.021733`, median `0.024844`, mae `0.031379`
- 60d: sample `60`, hit `0.7333`, avg `0.036901`, median `0.057501`, mae `0.06653`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.001511`, median `-0.008802`, mae `0.018317`
- 5d: sample `20`, hit `0.55`, avg `-0.003613`, median `0.004752`, mae `0.021653`
- 10d: sample `20`, hit `0.7`, avg `0.004748`, median `0.010559`, mae `0.027416`
- 20d: sample `20`, hit `0.8`, avg `0.022531`, median `0.036446`, mae `0.038922`
- 60d: sample `20`, hit `0.85`, avg `0.062547`, median `0.071679`, mae `0.072999`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.000613`, median `-0.001641`, mae `0.014681`
- 5d: sample `60`, hit `0.4667`, avg `-0.000729`, median `-0.003328`, mae `0.018028`
- 10d: sample `60`, hit `0.55`, avg `0.006698`, median `0.0076`, mae `0.025493`
- 20d: sample `60`, hit `0.8`, avg `0.021733`, median `0.024844`, mae `0.031379`
- 60d: sample `60`, hit `0.7333`, avg `0.036901`, median `0.057501`, mae `0.06653`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.000613`, median `-0.001641`, mae `0.014681`
- 5d: sample `60`, hit `0.4667`, avg `-0.000729`, median `-0.003328`, mae `0.018028`
- 10d: sample `60`, hit `0.55`, avg `0.006698`, median `0.0076`, mae `0.025493`
- 20d: sample `60`, hit `0.8`, avg `0.021733`, median `0.024844`, mae `0.031379`
- 60d: sample `60`, hit `0.7333`, avg `0.036901`, median `0.057501`, mae `0.06653`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.000613`, median `-0.001641`, mae `0.014681`
- 5d: sample `60`, hit `0.4667`, avg `-0.000729`, median `-0.003328`, mae `0.018028`
- 10d: sample `60`, hit `0.55`, avg `0.006698`, median `0.0076`, mae `0.025493`
- 20d: sample `60`, hit `0.8`, avg `0.021733`, median `0.024844`, mae `0.031379`
- 60d: sample `60`, hit `0.7333`, avg `0.036901`, median `0.057501`, mae `0.06653`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.000613`, median `-0.001641`, mae `0.014681`
- 5d: sample `60`, hit `0.4667`, avg `-0.000729`, median `-0.003328`, mae `0.018028`
- 10d: sample `60`, hit `0.55`, avg `0.006698`, median `0.0076`, mae `0.025493`
- 20d: sample `60`, hit `0.8`, avg `0.021733`, median `0.024844`, mae `0.031379`
- 60d: sample `60`, hit `0.7333`, avg `0.036901`, median `0.057501`, mae `0.06653`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.001511`, median `-0.008802`, mae `0.018317`
- 5d: sample `20`, hit `0.55`, avg `-0.003613`, median `0.004752`, mae `0.021653`
- 10d: sample `20`, hit `0.7`, avg `0.004748`, median `0.010559`, mae `0.027416`
- 20d: sample `20`, hit `0.8`, avg `0.022531`, median `0.036446`, mae `0.038922`
- 60d: sample `20`, hit `0.85`, avg `0.062547`, median `0.071679`, mae `0.072999`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.000613`, median `-0.001641`, mae `0.014681`
- 5d: sample `60`, hit `0.4667`, avg `-0.000729`, median `-0.003328`, mae `0.018028`
- 10d: sample `60`, hit `0.55`, avg `0.006698`, median `0.0076`, mae `0.025493`
- 20d: sample `60`, hit `0.8`, avg `0.021733`, median `0.024844`, mae `0.031379`
- 60d: sample `60`, hit `0.7333`, avg `0.036901`, median `0.057501`, mae `0.06653`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.001511`, median `-0.008802`, mae `0.018317`
- 5d: sample `20`, hit `0.55`, avg `-0.003613`, median `0.004752`, mae `0.021653`
- 10d: sample `20`, hit `0.7`, avg `0.004748`, median `0.010559`, mae `0.027416`
- 20d: sample `20`, hit `0.8`, avg `0.022531`, median `0.036446`, mae `0.038922`
- 60d: sample `20`, hit `0.85`, avg `0.062547`, median `0.071679`, mae `0.072999`

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
- 3d: sample `80`, hit `0.4375`, avg `-0.000838`, median `-0.001811`, mae `0.01559`
- 5d: sample `80`, hit `0.4875`, avg `-0.00145`, median `-0.000322`, mae `0.018934`
- 10d: sample `80`, hit `0.5875`, avg `0.00621`, median `0.0076`, mae `0.025974`
- 20d: sample `80`, hit `0.8`, avg `0.021932`, median `0.027684`, mae `0.033265`
- 60d: sample `80`, hit `0.7625`, avg `0.043313`, median `0.064194`, mae `0.068147`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4375`, avg `-0.000838`, median `-0.001811`, mae `0.01559`
- 5d: sample `80`, hit `0.4875`, avg `-0.00145`, median `-0.000322`, mae `0.018934`
- 10d: sample `80`, hit `0.5875`, avg `0.00621`, median `0.0076`, mae `0.025974`
- 20d: sample `80`, hit `0.8`, avg `0.021932`, median `0.027684`, mae `0.033265`
- 60d: sample `80`, hit `0.7625`, avg `0.043313`, median `0.064194`, mae `0.068147`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.000613`, median `-0.001641`, mae `0.014681`
- 5d: sample `60`, hit `0.4667`, avg `-0.000729`, median `-0.003328`, mae `0.018028`
- 10d: sample `60`, hit `0.55`, avg `0.006698`, median `0.0076`, mae `0.025493`
- 20d: sample `60`, hit `0.8`, avg `0.021733`, median `0.024844`, mae `0.031379`
- 60d: sample `60`, hit `0.7333`, avg `0.036901`, median `0.057501`, mae `0.06653`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.000613`, median `-0.001641`, mae `0.014681`
- 5d: sample `60`, hit `0.4667`, avg `-0.000729`, median `-0.003328`, mae `0.018028`
- 10d: sample `60`, hit `0.55`, avg `0.006698`, median `0.0076`, mae `0.025493`
- 20d: sample `60`, hit `0.8`, avg `0.021733`, median `0.024844`, mae `0.031379`
- 60d: sample `60`, hit `0.7333`, avg `0.036901`, median `0.057501`, mae `0.06653`

### risk_path_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.001511`, median `-0.008802`, mae `0.018317`
- 5d: sample `20`, hit `0.55`, avg `-0.003613`, median `0.004752`, mae `0.021653`
- 10d: sample `20`, hit `0.7`, avg `0.004748`, median `0.010559`, mae `0.027416`
- 20d: sample `20`, hit `0.8`, avg `0.022531`, median `0.036446`, mae `0.038922`
- 60d: sample `20`, hit `0.85`, avg `0.062547`, median `0.071679`, mae `0.072999`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
