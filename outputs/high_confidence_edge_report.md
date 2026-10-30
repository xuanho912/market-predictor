# High Confidence Edge Report

Generated at: `2026-10-30T23:56:58.258939+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `152`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `152`, gate `stronger_evidence`
- 5d: completed `152`, gate `stronger_evidence`
- 10d: completed `152`, gate `stronger_evidence`
- 20d: completed `152`, gate `stronger_evidence`
- 60d: completed `152`, gate `stronger_evidence`

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
- 3d: sample `60`, hit `0.55`, avg `0.003831`, median `0.004886`, mae `0.015382`
- 5d: sample `60`, hit `0.5833`, avg `0.008021`, median `0.007479`, mae `0.01768`
- 10d: sample `60`, hit `0.65`, avg `0.013115`, median `0.011431`, mae `0.027185`
- 20d: sample `60`, hit `0.7167`, avg `0.023111`, median `0.028589`, mae `0.039666`
- 60d: sample `60`, hit `0.8167`, avg `0.044112`, median `0.055364`, mae `0.056353`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.006408`, median `0.010441`, mae `0.021613`
- 5d: sample `20`, hit `0.65`, avg `0.013565`, median `0.025118`, mae `0.028815`
- 10d: sample `20`, hit `0.9`, avg `0.0397`, median `0.0362`, mae `0.041187`
- 20d: sample `20`, hit `1.0`, avg `0.063319`, median `0.057896`, mae `0.063319`
- 60d: sample `20`, hit `0.9`, avg `0.066127`, median `0.069634`, mae `0.070096`

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
- 3d: sample `8`, hit `0.5`, avg `0.005912`, median `0.004243`, mae `0.017339`
- 5d: sample `8`, hit `0.5`, avg `0.009411`, median `0.013109`, mae `0.019857`
- 10d: sample `8`, hit `0.625`, avg `0.021811`, median `0.023979`, mae `0.030702`
- 20d: sample `8`, hit `0.875`, avg `0.039468`, median `0.031658`, mae `0.041849`
- 60d: sample `8`, hit `1.0`, avg `0.08304`, median `0.092646`, mae `0.08304`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.005912`, median `0.004243`, mae `0.017339`
- 5d: sample `8`, hit `0.5`, avg `0.009411`, median `0.013109`, mae `0.019857`
- 10d: sample `8`, hit `0.625`, avg `0.021811`, median `0.023979`, mae `0.030702`
- 20d: sample `8`, hit `0.875`, avg `0.039468`, median `0.031658`, mae `0.041849`
- 60d: sample `8`, hit `1.0`, avg `0.08304`, median `0.092646`, mae `0.08304`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.003831, 'median_return': 0.004886, 'mean_absolute_return': 0.015382, 'max_adverse_excursion': -0.03272, 'max_favorable_excursion': 0.047232}, '5d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.008021, 'median_return': 0.007479, 'mean_absolute_return': 0.01768, 'max_adverse_excursion': -0.03028, 'max_favorable_excursion': 0.045434}, '10d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.013115, 'median_return': 0.011431, 'mean_absolute_return': 0.027185, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.023111, 'median_return': 0.028589, 'mean_absolute_return': 0.039666, 'max_adverse_excursion': -0.068819, 'max_favorable_excursion': 0.093998}, '60d': {'sample_size': 60, 'hit_rate': 0.8167, 'avg_return': 0.044112, 'median_return': 0.055364, 'mean_absolute_return': 0.056353, 'max_adverse_excursion': -0.090957, 'max_favorable_excursion': 0.10846}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.005912, 'median_return': 0.004243, 'mean_absolute_return': 0.017339, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.009411, 'median_return': 0.013109, 'mean_absolute_return': 0.019857, 'max_adverse_excursion': -0.016952, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.021811, 'median_return': 0.023979, 'mean_absolute_return': 0.030702, 'max_adverse_excursion': -0.021975, 'max_favorable_excursion': 0.060007}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.039468, 'median_return': 0.031658, 'mean_absolute_return': 0.041849, 'max_adverse_excursion': -0.009524, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.08304, 'median_return': 0.092646, 'mean_absolute_return': 0.08304, 'max_adverse_excursion': 0.054522, 'max_favorable_excursion': 0.105209}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.004315, 'median_return': 0.005726, 'mean_absolute_return': 0.016895, 'max_adverse_excursion': -0.043793, 'max_favorable_excursion': 0.047232}, '5d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.009406, 'median_return': 0.009101, 'mean_absolute_return': 0.020531, 'max_adverse_excursion': -0.045128, 'max_favorable_excursion': 0.076593}, '10d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.019534, 'median_return': 0.019449, 'mean_absolute_return': 0.030683, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.090323}, '20d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.032463, 'median_return': 0.041918, 'mean_absolute_return': 0.045994, 'max_adverse_excursion': -0.068819, 'max_favorable_excursion': 0.112509}, '60d': {'sample_size': 72, 'hit_rate': 0.8194, 'avg_return': 0.045902, 'median_return': 0.056005, 'mean_absolute_return': 0.057206, 'max_adverse_excursion': -0.090957, 'max_favorable_excursion': 0.140054}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.525}, '10d': {'sample_size': 80, 'hit_rate': 0.5125}, '20d': {'sample_size': 80, 'hit_rate': 0.5375}, '60d': {'sample_size': 80, 'hit_rate': 0.6375}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.025, 'both_hit': 33, 'both_miss': 27}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.075, 'both_hit': 35, 'both_miss': 25}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': -0.2, 'both_hit': 39, 'both_miss': 21}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.7875, 'primary_minus_secondary': -0.25, 'both_hit': 43, 'both_miss': 17}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.8375, 'primary_minus_secondary': -0.2, 'both_hit': 49, 'both_miss': 11}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.006398, 'median_return': 0.007176, 'mean_absolute_return': 0.018194, 'max_adverse_excursion': -0.043793, 'max_favorable_excursion': 0.047232}, '5d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.013833, 'median_return': 0.020876, 'mean_absolute_return': 0.023767, 'max_adverse_excursion': -0.045128, 'max_favorable_excursion': 0.076593}, '10d': {'sample_size': 40, 'hit_rate': 0.825, 'avg_return': 0.02766, 'median_return': 0.028008, 'mean_absolute_return': 0.033597, 'max_adverse_excursion': -0.036068, 'max_favorable_excursion': 0.090323}, '20d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.037332, 'median_return': 0.052608, 'mean_absolute_return': 0.052534, 'max_adverse_excursion': -0.068819, 'max_favorable_excursion': 0.112509}, '60d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.041582, 'median_return': 0.056005, 'mean_absolute_return': 0.054956, 'max_adverse_excursion': -0.090957, 'max_favorable_excursion': 0.140054}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.002552, 'median_return': 0.002484, 'mean_absolute_return': 0.015686, 'max_adverse_excursion': -0.03272, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.004981, 'median_return': 0.00633, 'mean_absolute_return': 0.017161, 'max_adverse_excursion': -0.03028, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.011863, 'median_return': 0.014227, 'mean_absolute_return': 0.027773, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.060273}, '20d': {'sample_size': 40, 'hit_rate': 0.825, 'avg_return': 0.028995, 'median_return': 0.028626, 'mean_absolute_return': 0.038625, 'max_adverse_excursion': -0.068457, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 40, 'hit_rate': 0.9, 'avg_return': 0.057649, 'median_return': 0.068046, 'mean_absolute_return': 0.064623, 'max_adverse_excursion': -0.056528, 'max_favorable_excursion': 0.10846}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.003831`, median `0.004886`, mae `0.015382`
- 5d: sample `60`, hit `0.5833`, avg `0.008021`, median `0.007479`, mae `0.01768`
- 10d: sample `60`, hit `0.65`, avg `0.013115`, median `0.011431`, mae `0.027185`
- 20d: sample `60`, hit `0.7167`, avg `0.023111`, median `0.028589`, mae `0.039666`
- 60d: sample `60`, hit `0.8167`, avg `0.044112`, median `0.055364`, mae `0.056353`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.006408`, median `0.010441`, mae `0.021613`
- 5d: sample `20`, hit `0.65`, avg `0.013565`, median `0.025118`, mae `0.028815`
- 10d: sample `20`, hit `0.9`, avg `0.0397`, median `0.0362`, mae `0.041187`
- 20d: sample `20`, hit `1.0`, avg `0.063319`, median `0.057896`, mae `0.063319`
- 60d: sample `20`, hit `0.9`, avg `0.066127`, median `0.069634`, mae `0.070096`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.003831`, median `0.004886`, mae `0.015382`
- 5d: sample `60`, hit `0.5833`, avg `0.008021`, median `0.007479`, mae `0.01768`
- 10d: sample `60`, hit `0.65`, avg `0.013115`, median `0.011431`, mae `0.027185`
- 20d: sample `60`, hit `0.7167`, avg `0.023111`, median `0.028589`, mae `0.039666`
- 60d: sample `60`, hit `0.8167`, avg `0.044112`, median `0.055364`, mae `0.056353`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.002552`, median `0.002484`, mae `0.015686`
- 5d: sample `40`, hit `0.5`, avg `0.004981`, median `0.00633`, mae `0.017161`
- 10d: sample `40`, hit `0.6`, avg `0.011863`, median `0.014227`, mae `0.027773`
- 20d: sample `40`, hit `0.825`, avg `0.028995`, median `0.028626`, mae `0.038625`
- 60d: sample `40`, hit `0.9`, avg `0.057649`, median `0.068046`, mae `0.064623`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.003831`, median `0.004886`, mae `0.015382`
- 5d: sample `60`, hit `0.5833`, avg `0.008021`, median `0.007479`, mae `0.01768`
- 10d: sample `60`, hit `0.65`, avg `0.013115`, median `0.011431`, mae `0.027185`
- 20d: sample `60`, hit `0.7167`, avg `0.023111`, median `0.028589`, mae `0.039666`
- 60d: sample `60`, hit `0.8167`, avg `0.044112`, median `0.055364`, mae `0.056353`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.002552`, median `0.002484`, mae `0.015686`
- 5d: sample `40`, hit `0.5`, avg `0.004981`, median `0.00633`, mae `0.017161`
- 10d: sample `40`, hit `0.6`, avg `0.011863`, median `0.014227`, mae `0.027773`
- 20d: sample `40`, hit `0.825`, avg `0.028995`, median `0.028626`, mae `0.038625`
- 60d: sample `40`, hit `0.9`, avg `0.057649`, median `0.068046`, mae `0.064623`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.006408`, median `0.010441`, mae `0.021613`
- 5d: sample `20`, hit `0.65`, avg `0.013565`, median `0.025118`, mae `0.028815`
- 10d: sample `20`, hit `0.9`, avg `0.0397`, median `0.0362`, mae `0.041187`
- 20d: sample `20`, hit `1.0`, avg `0.063319`, median `0.057896`, mae `0.063319`
- 60d: sample `20`, hit `0.9`, avg `0.066127`, median `0.069634`, mae `0.070096`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.002552`, median `0.002484`, mae `0.015686`
- 5d: sample `40`, hit `0.5`, avg `0.004981`, median `0.00633`, mae `0.017161`
- 10d: sample `40`, hit `0.6`, avg `0.011863`, median `0.014227`, mae `0.027773`
- 20d: sample `40`, hit `0.825`, avg `0.028995`, median `0.028626`, mae `0.038625`
- 60d: sample `40`, hit `0.9`, avg `0.057649`, median `0.068046`, mae `0.064623`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.006388`, median `0.007176`, mae `0.014775`
- 5d: sample `20`, hit `0.75`, avg `0.014102`, median `0.018679`, mae `0.018718`
- 10d: sample `20`, hit `0.75`, avg `0.015621`, median `0.011431`, mae `0.026008`
- 20d: sample `20`, hit `0.5`, avg `0.011344`, median `0.010428`, mae `0.041749`
- 60d: sample `20`, hit `0.65`, avg `0.017038`, median `0.022563`, mae `0.039815`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.002552`, median `0.002484`, mae `0.015686`
- 5d: sample `40`, hit `0.5`, avg `0.004981`, median `0.00633`, mae `0.017161`
- 10d: sample `40`, hit `0.6`, avg `0.011863`, median `0.014227`, mae `0.027773`
- 20d: sample `40`, hit `0.825`, avg `0.028995`, median `0.028626`, mae `0.038625`
- 60d: sample `40`, hit `0.9`, avg `0.057649`, median `0.068046`, mae `0.064623`

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
- 3d: sample `80`, hit `0.55`, avg `0.004475`, median `0.004886`, mae `0.01694`
- 5d: sample `80`, hit `0.6`, avg `0.009407`, median `0.009101`, mae `0.020464`
- 10d: sample `80`, hit `0.7125`, avg `0.019762`, median `0.020244`, mae `0.030685`
- 20d: sample `80`, hit `0.7875`, avg `0.033163`, median `0.041903`, mae `0.045579`
- 60d: sample `80`, hit `0.8375`, avg `0.049616`, median `0.05795`, mae `0.059789`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.55`, avg `0.004475`, median `0.004886`, mae `0.01694`
- 5d: sample `80`, hit `0.6`, avg `0.009407`, median `0.009101`, mae `0.020464`
- 10d: sample `80`, hit `0.7125`, avg `0.019762`, median `0.020244`, mae `0.030685`
- 20d: sample `80`, hit `0.7875`, avg `0.033163`, median `0.041903`, mae `0.045579`
- 60d: sample `80`, hit `0.8375`, avg `0.049616`, median `0.05795`, mae `0.059789`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.003831`, median `0.004886`, mae `0.015382`
- 5d: sample `60`, hit `0.5833`, avg `0.008021`, median `0.007479`, mae `0.01768`
- 10d: sample `60`, hit `0.65`, avg `0.013115`, median `0.011431`, mae `0.027185`
- 20d: sample `60`, hit `0.7167`, avg `0.023111`, median `0.028589`, mae `0.039666`
- 60d: sample `60`, hit `0.8167`, avg `0.044112`, median `0.055364`, mae `0.056353`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.003831`, median `0.004886`, mae `0.015382`
- 5d: sample `60`, hit `0.5833`, avg `0.008021`, median `0.007479`, mae `0.01768`
- 10d: sample `60`, hit `0.65`, avg `0.013115`, median `0.011431`, mae `0.027185`
- 20d: sample `60`, hit `0.7167`, avg `0.023111`, median `0.028589`, mae `0.039666`
- 60d: sample `60`, hit `0.8167`, avg `0.044112`, median `0.055364`, mae `0.056353`

### risk_path_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.006408`, median `0.010441`, mae `0.021613`
- 5d: sample `20`, hit `0.65`, avg `0.013565`, median `0.025118`, mae `0.028815`
- 10d: sample `20`, hit `0.9`, avg `0.0397`, median `0.0362`, mae `0.041187`
- 20d: sample `20`, hit `1.0`, avg `0.063319`, median `0.057896`, mae `0.063319`
- 60d: sample `20`, hit `0.9`, avg `0.066127`, median `0.069634`, mae `0.070096`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
