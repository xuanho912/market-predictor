# High Confidence Edge Report

Generated at: `2026-09-25T01:13:05.742047+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `47`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `47`, gate `early_evidence`
- 5d: completed `47`, gate `early_evidence`
- 10d: completed `47`, gate `early_evidence`
- 20d: completed `47`, gate `early_evidence`
- 60d: completed `47`, gate `early_evidence`

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
- 3d: sample `60`, hit `0.5167`, avg `0.000334`, median `0.001405`, mae `0.015822`
- 5d: sample `60`, hit `0.5167`, avg `0.002394`, median `0.00374`, mae `0.018179`
- 10d: sample `60`, hit `0.6833`, avg `0.007697`, median `0.008464`, mae `0.020067`
- 20d: sample `60`, hit `0.7833`, avg `0.031056`, median `0.032102`, mae `0.03702`
- 60d: sample `60`, hit `0.9333`, avg `0.086003`, median `0.099838`, mae `0.092604`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.3`, avg `-0.006919`, median `-0.009843`, mae `0.016414`
- 5d: sample `20`, hit `0.35`, avg `-0.004012`, median `-0.005632`, mae `0.018455`
- 10d: sample `20`, hit `0.5`, avg `0.001084`, median `0.000478`, mae `0.029406`
- 20d: sample `20`, hit `0.5`, avg `-0.004381`, median `0.017648`, mae `0.046501`
- 60d: sample `20`, hit `0.85`, avg `0.094366`, median `0.114377`, mae `0.10916`

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
- 3d: sample `8`, hit `0.75`, avg `0.005815`, median `0.012272`, mae `0.014511`
- 5d: sample `8`, hit `0.625`, avg `0.006695`, median `0.009709`, mae `0.016592`
- 10d: sample `8`, hit `0.75`, avg `0.009347`, median `0.013069`, mae `0.017068`
- 20d: sample `8`, hit `0.625`, avg `0.026788`, median `0.043456`, mae `0.034274`
- 60d: sample `8`, hit `1.0`, avg `0.114868`, median `0.119272`, mae `0.114868`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.005815`, median `0.012272`, mae `0.014511`
- 5d: sample `8`, hit `0.625`, avg `0.006695`, median `0.009709`, mae `0.016592`
- 10d: sample `8`, hit `0.75`, avg `0.009347`, median `0.013069`, mae `0.017068`
- 20d: sample `8`, hit `0.625`, avg `0.026788`, median `0.043456`, mae `0.034274`
- 60d: sample `8`, hit `1.0`, avg `0.114868`, median `0.119272`, mae `0.114868`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': 0.000334, 'median_return': 0.001405, 'mean_absolute_return': 0.015822, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': 0.002394, 'median_return': 0.00374, 'mean_absolute_return': 0.018179, 'max_adverse_excursion': -0.034174, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.007697, 'median_return': 0.008464, 'mean_absolute_return': 0.020067, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 60, 'hit_rate': 0.7833, 'avg_return': 0.031056, 'median_return': 0.032102, 'mean_absolute_return': 0.03702, 'max_adverse_excursion': -0.032124, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 60, 'hit_rate': 0.9333, 'avg_return': 0.086003, 'median_return': 0.099838, 'mean_absolute_return': 0.092604, 'max_adverse_excursion': -0.085385, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.005815, 'median_return': 0.012272, 'mean_absolute_return': 0.014511, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.023651}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.006695, 'median_return': 0.009709, 'mean_absolute_return': 0.016592, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.027457}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.009347, 'median_return': 0.013069, 'mean_absolute_return': 0.017068, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.026788, 'median_return': 0.043456, 'mean_absolute_return': 0.034274, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.114868, 'median_return': 0.119272, 'mean_absolute_return': 0.114868, 'max_adverse_excursion': 0.099512, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': -0.00229, 'median_return': -0.002225, 'mean_absolute_return': 0.016133, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': 0.000137, 'median_return': -0.002452, 'mean_absolute_return': 0.018432, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.005677, 'median_return': 0.005165, 'mean_absolute_return': 0.022994, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.021686, 'median_return': 0.028881, 'mean_absolute_return': 0.039959, 'max_adverse_excursion': -0.082211, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 72, 'hit_rate': 0.9028, 'avg_return': 0.085119, 'median_return': 0.098256, 'mean_absolute_return': 0.094729, 'max_adverse_excursion': -0.097109, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6125}, '5d': {'sample_size': 80, 'hit_rate': 0.625}, '10d': {'sample_size': 80, 'hit_rate': 0.6375}, '20d': {'sample_size': 80, 'hit_rate': 0.5625}, '60d': {'sample_size': 80, 'hit_rate': 0.5625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.15, 'both_hit': 13, 'both_miss': 7}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.175, 'both_hit': 13, 'both_miss': 7}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.15, 'both_hit': 15, 'both_miss': 5}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.025, 'both_hit': 16, 'both_miss': 4}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.125, 'both_hit': 20, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': 0.000334, 'median_return': 0.001405, 'mean_absolute_return': 0.015822, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': 0.002394, 'median_return': 0.00374, 'mean_absolute_return': 0.018179, 'max_adverse_excursion': -0.034174, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.007697, 'median_return': 0.008464, 'mean_absolute_return': 0.020067, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 60, 'hit_rate': 0.7833, 'avg_return': 0.031056, 'median_return': 0.032102, 'mean_absolute_return': 0.03702, 'max_adverse_excursion': -0.032124, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 60, 'hit_rate': 0.9333, 'avg_return': 0.086003, 'median_return': 0.099838, 'mean_absolute_return': 0.092604, 'max_adverse_excursion': -0.085385, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.006919, 'median_return': -0.009843, 'mean_absolute_return': 0.016414, 'max_adverse_excursion': -0.036265, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.004012, 'median_return': -0.005632, 'mean_absolute_return': 0.018455, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.001084, 'median_return': 0.000478, 'mean_absolute_return': 0.029406, 'max_adverse_excursion': -0.053986, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.004381, 'median_return': 0.017648, 'mean_absolute_return': 0.046501, 'max_adverse_excursion': -0.082211, 'max_favorable_excursion': 0.067793}, '60d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.094366, 'median_return': 0.114377, 'mean_absolute_return': 0.10916, 'max_adverse_excursion': -0.097109, 'max_favorable_excursion': 0.176653}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `-0.001479`, median `-0.001227`, mae `0.01597`
- 5d: sample `80`, hit `0.475`, avg `0.000793`, median `-0.001129`, mae `0.018248`
- 10d: sample `80`, hit `0.6375`, avg `0.006044`, median `0.005356`, mae `0.022401`
- 20d: sample `80`, hit `0.7125`, avg `0.022197`, median `0.028881`, mae `0.03939`
- 60d: sample `80`, hit `0.9125`, avg `0.088093`, median `0.10344`, mae `0.096743`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.00262`, median `0.003757`, mae `0.012615`
- 5d: sample `40`, hit `0.6`, avg `0.004557`, median `0.006609`, mae `0.015426`
- 10d: sample `40`, hit `0.775`, avg `0.00969`, median `0.008908`, mae `0.017957`
- 20d: sample `40`, hit `0.775`, avg `0.030439`, median `0.03801`, mae `0.037421`
- 60d: sample `40`, hit `0.975`, avg `0.096722`, median `0.108121`, mae `0.097763`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.002177`, median `-0.002225`, mae `0.016601`
- 5d: sample `40`, hit `0.45`, avg `-0.000547`, median `-0.002538`, mae `0.018264`
- 10d: sample `40`, hit `0.65`, avg `0.004776`, median `0.005356`, mae `0.018248`
- 20d: sample `40`, hit `0.775`, avg `0.028963`, median `0.032102`, mae `0.03601`
- 60d: sample `40`, hit `0.9`, avg `0.079339`, median `0.084216`, mae `0.089241`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.00262`, median `0.003757`, mae `0.012615`
- 5d: sample `40`, hit `0.6`, avg `0.004557`, median `0.006609`, mae `0.015426`
- 10d: sample `40`, hit `0.775`, avg `0.00969`, median `0.008908`, mae `0.017957`
- 20d: sample `40`, hit `0.775`, avg `0.030439`, median `0.03801`, mae `0.037421`
- 60d: sample `40`, hit `0.975`, avg `0.096722`, median `0.108121`, mae `0.097763`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.35`, avg `-0.005578`, median `-0.009843`, mae `0.019326`
- 5d: sample `40`, hit `0.35`, avg `-0.002971`, median `-0.00693`, mae `0.02107`
- 10d: sample `40`, hit `0.5`, avg `0.002397`, median `0.000478`, mae `0.026846`
- 20d: sample `40`, hit `0.65`, avg `0.013954`, median `0.026005`, mae `0.04136`
- 60d: sample `40`, hit `0.85`, avg `0.079465`, median `0.098256`, mae `0.095723`

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
- 3d: sample `80`, hit `0.4625`, avg `-0.001479`, median `-0.001227`, mae `0.01597`
- 5d: sample `80`, hit `0.475`, avg `0.000793`, median `-0.001129`, mae `0.018248`
- 10d: sample `80`, hit `0.6375`, avg `0.006044`, median `0.005356`, mae `0.022401`
- 20d: sample `80`, hit `0.7125`, avg `0.022197`, median `0.028881`, mae `0.03939`
- 60d: sample `80`, hit `0.9125`, avg `0.088093`, median `0.10344`, mae `0.096743`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.00262`, median `0.003757`, mae `0.012615`
- 5d: sample `40`, hit `0.6`, avg `0.004557`, median `0.006609`, mae `0.015426`
- 10d: sample `40`, hit `0.775`, avg `0.00969`, median `0.008908`, mae `0.017957`
- 20d: sample `40`, hit `0.775`, avg `0.030439`, median `0.03801`, mae `0.037421`
- 60d: sample `40`, hit `0.975`, avg `0.096722`, median `0.108121`, mae `0.097763`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4625`, avg `-0.001479`, median `-0.001227`, mae `0.01597`
- 5d: sample `80`, hit `0.475`, avg `0.000793`, median `-0.001129`, mae `0.018248`
- 10d: sample `80`, hit `0.6375`, avg `0.006044`, median `0.005356`, mae `0.022401`
- 20d: sample `80`, hit `0.7125`, avg `0.022197`, median `0.028881`, mae `0.03939`
- 60d: sample `80`, hit `0.9125`, avg `0.088093`, median `0.10344`, mae `0.096743`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.00262`, median `0.003757`, mae `0.012615`
- 5d: sample `40`, hit `0.6`, avg `0.004557`, median `0.006609`, mae `0.015426`
- 10d: sample `40`, hit `0.775`, avg `0.00969`, median `0.008908`, mae `0.017957`
- 20d: sample `40`, hit `0.775`, avg `0.030439`, median `0.03801`, mae `0.037421`
- 60d: sample `40`, hit `0.975`, avg `0.096722`, median `0.108121`, mae `0.097763`

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
