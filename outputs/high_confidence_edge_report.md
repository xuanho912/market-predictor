# High Confidence Edge Report

Generated at: `2026-11-12T11:52:15.399036+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `184`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `184`, gate `stronger_evidence`
- 5d: completed `184`, gate `stronger_evidence`
- 10d: completed `184`, gate `stronger_evidence`
- 20d: completed `184`, gate `stronger_evidence`
- 60d: completed `184`, gate `stronger_evidence`

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
- 3d: sample `60`, hit `0.4333`, avg `-0.001458`, median `-0.001811`, mae `0.015188`
- 5d: sample `60`, hit `0.4667`, avg `-0.001359`, median `-0.003328`, mae `0.018657`
- 10d: sample `60`, hit `0.5333`, avg `0.005688`, median `0.0076`, mae `0.02647`
- 20d: sample `60`, hit `0.8`, avg `0.021128`, median `0.024844`, mae `0.031984`
- 60d: sample `60`, hit `0.7333`, avg `0.038789`, median `0.057501`, mae `0.064641`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.003812`, median `-0.010522`, mae `0.018011`
- 5d: sample `20`, hit `0.5`, avg `-0.004469`, median `0.00338`, mae `0.02225`
- 10d: sample `20`, hit `0.65`, avg `0.003312`, median `0.010559`, mae `0.028066`
- 20d: sample `20`, hit `0.75`, avg `0.017965`, median `0.029038`, mae `0.037432`
- 60d: sample `20`, hit `0.8`, avg `0.050101`, median `0.065963`, mae `0.070487`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4333, 'avg_return': -0.001458, 'median_return': -0.001811, 'mean_absolute_return': 0.015188, 'max_adverse_excursion': -0.040531, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.001359, 'median_return': -0.003328, 'mean_absolute_return': 0.018657, 'max_adverse_excursion': -0.050569, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.005688, 'median_return': 0.0076, 'mean_absolute_return': 0.02647, 'max_adverse_excursion': -0.05959, 'max_favorable_excursion': 0.060007}, '20d': {'sample_size': 60, 'hit_rate': 0.8, 'avg_return': 0.021128, 'median_return': 0.024844, 'mean_absolute_return': 0.031984, 'max_adverse_excursion': -0.085064, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.038789, 'median_return': 0.057501, 'mean_absolute_return': 0.064641, 'max_adverse_excursion': -0.118502, 'max_favorable_excursion': 0.135457}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.006647, 'median_return': -0.003594, 'mean_absolute_return': 0.009338, 'max_adverse_excursion': -0.023751, 'max_favorable_excursion': 0.006372}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.009191, 'median_return': -0.010916, 'mean_absolute_return': 0.014947, 'max_adverse_excursion': -0.027002, 'max_favorable_excursion': 0.011571}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.002411, 'median_return': 0.009031, 'mean_absolute_return': 0.014671, 'max_adverse_excursion': -0.018368, 'max_favorable_excursion': 0.031945}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.016874, 'median_return': 0.020066, 'mean_absolute_return': 0.019685, 'max_adverse_excursion': -0.011242, 'max_favorable_excursion': 0.032327}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.057707, 'median_return': 0.078453, 'mean_absolute_return': 0.057707, 'max_adverse_excursion': 0.00377, 'max_favorable_excursion': 0.090554}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': -0.001535, 'median_return': -0.00518, 'mean_absolute_return': 0.016622, 'max_adverse_excursion': -0.040531, 'max_favorable_excursion': 0.039385}, '5d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.001353, 'median_return': 0.000208, 'mean_absolute_return': 0.020068, 'max_adverse_excursion': -0.050569, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.005392, 'median_return': 0.0076, 'mean_absolute_return': 0.028224, 'max_adverse_excursion': -0.05959, 'max_favorable_excursion': 0.061858}, '20d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.020722, 'median_return': 0.027684, 'mean_absolute_return': 0.034864, 'max_adverse_excursion': -0.085064, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.039829, 'median_return': 0.062764, 'mean_absolute_return': 0.067036, 'max_adverse_excursion': -0.118502, 'max_favorable_excursion': 0.166476}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4875}, '5d': {'sample_size': 80, 'hit_rate': 0.475}, '10d': {'sample_size': 80, 'hit_rate': 0.4875}, '20d': {'sample_size': 80, 'hit_rate': 0.6625}, '60d': {'sample_size': 80, 'hit_rate': 0.6}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.4125, 'primary_minus_secondary': 0.075, 'both_hit': 26, 'both_miss': 34}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.0, 'both_hit': 28, 'both_miss': 32}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.075, 'both_hit': 32, 'both_miss': 28}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.7875, 'primary_minus_secondary': -0.125, 'both_hit': 48, 'both_miss': 12}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.75, 'primary_minus_secondary': -0.15, 'both_hit': 44, 'both_miss': 16}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.003812, 'median_return': -0.010522, 'mean_absolute_return': 0.018011, 'max_adverse_excursion': -0.025828, 'max_favorable_excursion': 0.039385}, '5d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.004469, 'median_return': 0.00338, 'mean_absolute_return': 0.02225, 'max_adverse_excursion': -0.040262, 'max_favorable_excursion': 0.034788}, '10d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.003312, 'median_return': 0.010559, 'mean_absolute_return': 0.028066, 'max_adverse_excursion': -0.054711, 'max_favorable_excursion': 0.061858}, '20d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.017965, 'median_return': 0.029038, 'mean_absolute_return': 0.037432, 'max_adverse_excursion': -0.082605, 'max_favorable_excursion': 0.086431}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.050101, 'median_return': 0.065963, 'mean_absolute_return': 0.070487, 'max_adverse_excursion': -0.099346, 'max_favorable_excursion': 0.166476}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4333, 'avg_return': -0.001458, 'median_return': -0.001811, 'mean_absolute_return': 0.015188, 'max_adverse_excursion': -0.040531, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.001359, 'median_return': -0.003328, 'mean_absolute_return': 0.018657, 'max_adverse_excursion': -0.050569, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.005688, 'median_return': 0.0076, 'mean_absolute_return': 0.02647, 'max_adverse_excursion': -0.05959, 'max_favorable_excursion': 0.060007}, '20d': {'sample_size': 60, 'hit_rate': 0.8, 'avg_return': 0.021128, 'median_return': 0.024844, 'mean_absolute_return': 0.031984, 'max_adverse_excursion': -0.085064, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.038789, 'median_return': 0.057501, 'mean_absolute_return': 0.064641, 'max_adverse_excursion': -0.118502, 'max_favorable_excursion': 0.135457}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.001458`, median `-0.001811`, mae `0.015188`
- 5d: sample `60`, hit `0.4667`, avg `-0.001359`, median `-0.003328`, mae `0.018657`
- 10d: sample `60`, hit `0.5333`, avg `0.005688`, median `0.0076`, mae `0.02647`
- 20d: sample `60`, hit `0.8`, avg `0.021128`, median `0.024844`, mae `0.031984`
- 60d: sample `60`, hit `0.7333`, avg `0.038789`, median `0.057501`, mae `0.064641`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.003812`, median `-0.010522`, mae `0.018011`
- 5d: sample `20`, hit `0.5`, avg `-0.004469`, median `0.00338`, mae `0.02225`
- 10d: sample `20`, hit `0.65`, avg `0.003312`, median `0.010559`, mae `0.028066`
- 20d: sample `20`, hit `0.75`, avg `0.017965`, median `0.029038`, mae `0.037432`
- 60d: sample `20`, hit `0.8`, avg `0.050101`, median `0.065963`, mae `0.070487`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.001458`, median `-0.001811`, mae `0.015188`
- 5d: sample `60`, hit `0.4667`, avg `-0.001359`, median `-0.003328`, mae `0.018657`
- 10d: sample `60`, hit `0.5333`, avg `0.005688`, median `0.0076`, mae `0.02647`
- 20d: sample `60`, hit `0.8`, avg `0.021128`, median `0.024844`, mae `0.031984`
- 60d: sample `60`, hit `0.7333`, avg `0.038789`, median `0.057501`, mae `0.064641`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.001458`, median `-0.001811`, mae `0.015188`
- 5d: sample `60`, hit `0.4667`, avg `-0.001359`, median `-0.003328`, mae `0.018657`
- 10d: sample `60`, hit `0.5333`, avg `0.005688`, median `0.0076`, mae `0.02647`
- 20d: sample `60`, hit `0.8`, avg `0.021128`, median `0.024844`, mae `0.031984`
- 60d: sample `60`, hit `0.7333`, avg `0.038789`, median `0.057501`, mae `0.064641`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.001458`, median `-0.001811`, mae `0.015188`
- 5d: sample `60`, hit `0.4667`, avg `-0.001359`, median `-0.003328`, mae `0.018657`
- 10d: sample `60`, hit `0.5333`, avg `0.005688`, median `0.0076`, mae `0.02647`
- 20d: sample `60`, hit `0.8`, avg `0.021128`, median `0.024844`, mae `0.031984`
- 60d: sample `60`, hit `0.7333`, avg `0.038789`, median `0.057501`, mae `0.064641`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.001458`, median `-0.001811`, mae `0.015188`
- 5d: sample `60`, hit `0.4667`, avg `-0.001359`, median `-0.003328`, mae `0.018657`
- 10d: sample `60`, hit `0.5333`, avg `0.005688`, median `0.0076`, mae `0.02647`
- 20d: sample `60`, hit `0.8`, avg `0.021128`, median `0.024844`, mae `0.031984`
- 60d: sample `60`, hit `0.7333`, avg `0.038789`, median `0.057501`, mae `0.064641`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.003812`, median `-0.010522`, mae `0.018011`
- 5d: sample `20`, hit `0.5`, avg `-0.004469`, median `0.00338`, mae `0.02225`
- 10d: sample `20`, hit `0.65`, avg `0.003312`, median `0.010559`, mae `0.028066`
- 20d: sample `20`, hit `0.75`, avg `0.017965`, median `0.029038`, mae `0.037432`
- 60d: sample `20`, hit `0.8`, avg `0.050101`, median `0.065963`, mae `0.070487`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.002073`, median `-0.003594`, mae `0.014947`
- 5d: sample `40`, hit `0.45`, avg `-0.002087`, median `-0.007788`, mae `0.017364`
- 10d: sample `40`, hit `0.475`, avg `0.003329`, median `0.0`, mae `0.023549`
- 20d: sample `40`, hit `0.8`, avg `0.020795`, median `0.026531`, mae `0.028434`
- 60d: sample `40`, hit `0.725`, avg `0.035633`, median `0.052632`, mae `0.059456`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.000226`, median `0.002018`, mae `0.01567`
- 5d: sample `20`, hit `0.5`, avg `9.7e-05`, median `0.002543`, mae `0.021245`
- 10d: sample `20`, hit `0.65`, avg `0.010406`, median `0.021778`, mae `0.032312`
- 20d: sample `20`, hit `0.8`, avg `0.021793`, median `0.024844`, mae `0.039083`
- 60d: sample `20`, hit `0.75`, avg `0.045102`, median `0.067462`, mae `0.075012`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.002073`, median `-0.003594`, mae `0.014947`
- 5d: sample `40`, hit `0.45`, avg `-0.002087`, median `-0.007788`, mae `0.017364`
- 10d: sample `40`, hit `0.475`, avg `0.003329`, median `0.0`, mae `0.023549`
- 20d: sample `40`, hit `0.8`, avg `0.020795`, median `0.026531`, mae `0.028434`
- 60d: sample `40`, hit `0.725`, avg `0.035633`, median `0.052632`, mae `0.059456`

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
- 3d: sample `80`, hit `0.4125`, avg `-0.002046`, median `-0.00518`, mae `0.015894`
- 5d: sample `80`, hit `0.475`, avg `-0.002136`, median `-0.003328`, mae `0.019556`
- 10d: sample `80`, hit `0.5625`, avg `0.005094`, median `0.0076`, mae `0.026869`
- 20d: sample `80`, hit `0.7875`, avg `0.020337`, median `0.026531`, mae `0.033346`
- 60d: sample `80`, hit `0.75`, avg `0.041617`, median `0.062764`, mae `0.066103`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4125`, avg `-0.002046`, median `-0.00518`, mae `0.015894`
- 5d: sample `80`, hit `0.475`, avg `-0.002136`, median `-0.003328`, mae `0.019556`
- 10d: sample `80`, hit `0.5625`, avg `0.005094`, median `0.0076`, mae `0.026869`
- 20d: sample `80`, hit `0.7875`, avg `0.020337`, median `0.026531`, mae `0.033346`
- 60d: sample `80`, hit `0.75`, avg `0.041617`, median `0.062764`, mae `0.066103`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.001458`, median `-0.001811`, mae `0.015188`
- 5d: sample `60`, hit `0.4667`, avg `-0.001359`, median `-0.003328`, mae `0.018657`
- 10d: sample `60`, hit `0.5333`, avg `0.005688`, median `0.0076`, mae `0.02647`
- 20d: sample `60`, hit `0.8`, avg `0.021128`, median `0.024844`, mae `0.031984`
- 60d: sample `60`, hit `0.7333`, avg `0.038789`, median `0.057501`, mae `0.064641`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.001458`, median `-0.001811`, mae `0.015188`
- 5d: sample `60`, hit `0.4667`, avg `-0.001359`, median `-0.003328`, mae `0.018657`
- 10d: sample `60`, hit `0.5333`, avg `0.005688`, median `0.0076`, mae `0.02647`
- 20d: sample `60`, hit `0.8`, avg `0.021128`, median `0.024844`, mae `0.031984`
- 60d: sample `60`, hit `0.7333`, avg `0.038789`, median `0.057501`, mae `0.064641`

### risk_path_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.003812`, median `-0.010522`, mae `0.018011`
- 5d: sample `20`, hit `0.5`, avg `-0.004469`, median `0.00338`, mae `0.02225`
- 10d: sample `20`, hit `0.65`, avg `0.003312`, median `0.010559`, mae `0.028066`
- 20d: sample `20`, hit `0.75`, avg `0.017965`, median `0.029038`, mae `0.037432`
- 60d: sample `20`, hit `0.8`, avg `0.050101`, median `0.065963`, mae `0.070487`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
