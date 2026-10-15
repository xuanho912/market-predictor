# High Confidence Edge Report

Generated at: `2026-10-15T00:14:16.874017+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `104`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `104`, gate `stronger_evidence`
- 5d: completed `104`, gate `stronger_evidence`
- 10d: completed `104`, gate `stronger_evidence`
- 20d: completed `104`, gate `stronger_evidence`
- 60d: completed `104`, gate `stronger_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.725`, avg `0.007213`, median `0.011957`, mae `0.014606`
- 5d: sample `40`, hit `0.7`, avg `0.009037`, median `0.012091`, mae `0.017604`
- 10d: sample `40`, hit `0.75`, avg `0.013403`, median `0.015799`, mae `0.021842`
- 20d: sample `40`, hit `0.9`, avg `0.039746`, median `0.03801`, mae `0.041687`
- 60d: sample `40`, hit `0.925`, avg `0.078624`, median `0.087104`, mae `0.083721`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.000336`, median `-0.003676`, mae `0.019042`
- 5d: sample `20`, hit `0.45`, avg `-0.001556`, median `-0.0129`, mae `0.023494`
- 10d: sample `20`, hit `0.45`, avg `0.001752`, median `-0.000648`, mae `0.023161`
- 20d: sample `20`, hit `0.9`, avg `0.027711`, median `0.020326`, mae `0.028948`
- 60d: sample `20`, hit `0.65`, avg `0.056733`, median `0.042767`, mae `0.078558`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.008558`, median `0.006343`, mae `0.02065`
- 5d: sample `20`, hit `0.55`, avg `0.009488`, median `0.00288`, mae `0.024488`
- 10d: sample `20`, hit `0.55`, avg `0.00305`, median `0.004306`, mae `0.040603`
- 20d: sample `20`, hit `0.55`, avg `0.025812`, median `0.039427`, mae `0.058491`
- 60d: sample `20`, hit `0.95`, avg `0.131014`, median `0.132255`, mae `0.139184`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.005525`, median `0.017238`, mae `0.019156`
- 5d: sample `8`, hit `0.75`, avg `0.005819`, median `0.009709`, mae `0.013622`
- 10d: sample `8`, hit `0.625`, avg `0.009112`, median `0.015799`, mae `0.017899`
- 20d: sample `8`, hit `1.0`, avg `0.047306`, median `0.058396`, mae `0.047306`
- 60d: sample `8`, hit `0.75`, avg `0.063421`, median `0.099838`, mae `0.083703`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.005525`, median `0.017238`, mae `0.019156`
- 5d: sample `8`, hit `0.75`, avg `0.005819`, median `0.009709`, mae `0.013622`
- 10d: sample `8`, hit `0.625`, avg `0.009112`, median `0.015799`, mae `0.017899`
- 20d: sample `8`, hit `1.0`, avg `0.047306`, median `0.058396`, mae `0.047306`
- 60d: sample `8`, hit `0.75`, avg `0.063421`, median `0.099838`, mae `0.083703`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.007213, 'median_return': 0.011957, 'mean_absolute_return': 0.014606, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.032414}, '5d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.009037, 'median_return': 0.012091, 'mean_absolute_return': 0.017604, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.013403, 'median_return': 0.015799, 'mean_absolute_return': 0.021842, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.059044}, '20d': {'sample_size': 40, 'hit_rate': 0.9, 'avg_return': 0.039746, 'median_return': 0.03801, 'mean_absolute_return': 0.041687, 'max_adverse_excursion': -0.015145, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 40, 'hit_rate': 0.925, 'avg_return': 0.078624, 'median_return': 0.087104, 'mean_absolute_return': 0.083721, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.005525, 'median_return': 0.017238, 'mean_absolute_return': 0.019156, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.025934}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.005819, 'median_return': 0.009709, 'mean_absolute_return': 0.013622, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.009112, 'median_return': 0.015799, 'mean_absolute_return': 0.017899, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.047306, 'median_return': 0.058396, 'mean_absolute_return': 0.047306, 'max_adverse_excursion': 0.01983, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.063421, 'median_return': 0.099838, 'mean_absolute_return': 0.083703, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.005677, 'median_return': 0.006632, 'mean_absolute_return': 0.017011, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.060601}, '5d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.006578, 'median_return': 0.008152, 'mean_absolute_return': 0.021595, 'max_adverse_excursion': -0.040291, 'max_favorable_excursion': 0.075704}, '10d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.007767, 'median_return': 0.007751, 'mean_absolute_return': 0.027858, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.084731}, '20d': {'sample_size': 72, 'hit_rate': 0.7917, 'avg_return': 0.031692, 'median_return': 0.03339, 'mean_absolute_return': 0.042192, 'max_adverse_excursion': -0.070044, 'max_favorable_excursion': 0.101843}, '60d': {'sample_size': 72, 'hit_rate': 0.875, 'avg_return': 0.088785, 'median_return': 0.096597, 'mean_absolute_return': 0.097696, 'max_adverse_excursion': -0.081696, 'max_favorable_excursion': 0.212071}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6}, '5d': {'sample_size': 80, 'hit_rate': 0.6}, '10d': {'sample_size': 80, 'hit_rate': 0.625}, '20d': {'sample_size': 80, 'hit_rate': 0.5875}, '60d': {'sample_size': 80, 'hit_rate': 0.5625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_minus_secondary': 0.2, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_minus_secondary': 0.2, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.375, 'primary_minus_secondary': 0.25, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_minus_secondary': 0.175, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.125, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.007213, 'median_return': 0.011957, 'mean_absolute_return': 0.014606, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.032414}, '5d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.009037, 'median_return': 0.012091, 'mean_absolute_return': 0.017604, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.013403, 'median_return': 0.015799, 'mean_absolute_return': 0.021842, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.059044}, '20d': {'sample_size': 40, 'hit_rate': 0.9, 'avg_return': 0.039746, 'median_return': 0.03801, 'mean_absolute_return': 0.041687, 'max_adverse_excursion': -0.015145, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 40, 'hit_rate': 0.925, 'avg_return': 0.078624, 'median_return': 0.087104, 'mean_absolute_return': 0.083721, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.004111, 'median_return': 0.002315, 'mean_absolute_return': 0.019846, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.060601}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.003966, 'median_return': 0.000396, 'mean_absolute_return': 0.023991, 'max_adverse_excursion': -0.040291, 'max_favorable_excursion': 0.075704}, '10d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.002401, 'median_return': 0.003262, 'mean_absolute_return': 0.031882, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.084731}, '20d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.026761, 'median_return': 0.027885, 'mean_absolute_return': 0.043719, 'max_adverse_excursion': -0.070044, 'max_favorable_excursion': 0.101843}, '60d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.093874, 'median_return': 0.113908, 'mean_absolute_return': 0.108871, 'max_adverse_excursion': -0.081696, 'max_favorable_excursion': 0.212071}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.725`, avg `0.007213`, median `0.011957`, mae `0.014606`
- 5d: sample `40`, hit `0.7`, avg `0.009037`, median `0.012091`, mae `0.017604`
- 10d: sample `40`, hit `0.75`, avg `0.013403`, median `0.015799`, mae `0.021842`
- 20d: sample `40`, hit `0.9`, avg `0.039746`, median `0.03801`, mae `0.041687`
- 60d: sample `40`, hit `0.925`, avg `0.078624`, median `0.087104`, mae `0.083721`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.004111`, median `0.002315`, mae `0.019846`
- 5d: sample `40`, hit `0.5`, avg `0.003966`, median `0.000396`, mae `0.023991`
- 10d: sample `40`, hit `0.5`, avg `0.002401`, median `0.003262`, mae `0.031882`
- 20d: sample `40`, hit `0.725`, avg `0.026761`, median `0.027885`, mae `0.043719`
- 60d: sample `40`, hit `0.8`, avg `0.093874`, median `0.113908`, mae `0.108871`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.725`, avg `0.007213`, median `0.011957`, mae `0.014606`
- 5d: sample `40`, hit `0.7`, avg `0.009037`, median `0.012091`, mae `0.017604`
- 10d: sample `40`, hit `0.75`, avg `0.013403`, median `0.015799`, mae `0.021842`
- 20d: sample `40`, hit `0.9`, avg `0.039746`, median `0.03801`, mae `0.041687`
- 60d: sample `40`, hit `0.925`, avg `0.078624`, median `0.087104`, mae `0.083721`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.725`, avg `0.007213`, median `0.011957`, mae `0.014606`
- 5d: sample `40`, hit `0.7`, avg `0.009037`, median `0.012091`, mae `0.017604`
- 10d: sample `40`, hit `0.75`, avg `0.013403`, median `0.015799`, mae `0.021842`
- 20d: sample `40`, hit `0.9`, avg `0.039746`, median `0.03801`, mae `0.041687`
- 60d: sample `40`, hit `0.925`, avg `0.078624`, median `0.087104`, mae `0.083721`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.725`, avg `0.007213`, median `0.011957`, mae `0.014606`
- 5d: sample `40`, hit `0.7`, avg `0.009037`, median `0.012091`, mae `0.017604`
- 10d: sample `40`, hit `0.75`, avg `0.013403`, median `0.015799`, mae `0.021842`
- 20d: sample `40`, hit `0.9`, avg `0.039746`, median `0.03801`, mae `0.041687`
- 60d: sample `40`, hit `0.925`, avg `0.078624`, median `0.087104`, mae `0.083721`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.725`, avg `0.007213`, median `0.011957`, mae `0.014606`
- 5d: sample `40`, hit `0.7`, avg `0.009037`, median `0.012091`, mae `0.017604`
- 10d: sample `40`, hit `0.75`, avg `0.013403`, median `0.015799`, mae `0.021842`
- 20d: sample `40`, hit `0.9`, avg `0.039746`, median `0.03801`, mae `0.041687`
- 60d: sample `40`, hit `0.925`, avg `0.078624`, median `0.087104`, mae `0.083721`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.004111`, median `0.002315`, mae `0.019846`
- 5d: sample `40`, hit `0.5`, avg `0.003966`, median `0.000396`, mae `0.023991`
- 10d: sample `40`, hit `0.5`, avg `0.002401`, median `0.003262`, mae `0.031882`
- 20d: sample `40`, hit `0.725`, avg `0.026761`, median `0.027885`, mae `0.043719`
- 60d: sample `40`, hit `0.8`, avg `0.093874`, median `0.113908`, mae `0.108871`

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
- 3d: sample `80`, hit `0.625`, avg `0.005662`, median `0.007259`, mae `0.017226`
- 5d: sample `80`, hit `0.6`, avg `0.006502`, median `0.008152`, mae `0.020797`
- 10d: sample `80`, hit `0.625`, avg `0.007902`, median `0.008243`, mae `0.026862`
- 20d: sample `80`, hit `0.8125`, avg `0.033253`, median `0.034158`, mae `0.042703`
- 60d: sample `80`, hit `0.8625`, avg `0.086249`, median `0.096597`, mae `0.096296`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.725`, avg `0.007213`, median `0.011957`, mae `0.014606`
- 5d: sample `40`, hit `0.7`, avg `0.009037`, median `0.012091`, mae `0.017604`
- 10d: sample `40`, hit `0.75`, avg `0.013403`, median `0.015799`, mae `0.021842`
- 20d: sample `40`, hit `0.9`, avg `0.039746`, median `0.03801`, mae `0.041687`
- 60d: sample `40`, hit `0.925`, avg `0.078624`, median `0.087104`, mae `0.083721`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
