# High Confidence Edge Report

Generated at: `2026-10-06T01:31:01.693871+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `76`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `76`, gate `moderate_evidence`
- 5d: completed `76`, gate `moderate_evidence`
- 10d: completed `76`, gate `moderate_evidence`
- 20d: completed `76`, gate `moderate_evidence`
- 60d: completed `76`, gate `moderate_evidence`

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
- 3d: sample `20`, hit `0.75`, avg `0.008195`, median `0.012542`, mae `0.01603`
- 5d: sample `20`, hit `0.65`, avg `0.009581`, median `0.010241`, mae `0.01911`
- 10d: sample `20`, hit `0.75`, avg `0.015006`, median `0.020334`, mae `0.024662`
- 20d: sample `20`, hit `0.8`, avg `0.037957`, median `0.03801`, mae `0.041755`
- 60d: sample `20`, hit `0.95`, avg `0.094492`, median `0.109494`, mae `0.099088`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.3833`, avg `-0.004603`, median `-0.003676`, mae `0.016811`
- 5d: sample `60`, hit `0.4`, avg `-0.002373`, median `-0.005796`, mae `0.018963`
- 10d: sample `60`, hit `0.5833`, avg `0.002204`, median `0.003921`, mae `0.021451`
- 20d: sample `60`, hit `0.6833`, avg `0.017766`, median `0.027885`, mae `0.037355`
- 60d: sample `60`, hit `0.8833`, avg `0.080956`, median `0.103071`, mae `0.097067`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.008195, 'median_return': 0.012542, 'mean_absolute_return': 0.01603, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.031839}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.009581, 'median_return': 0.010241, 'mean_absolute_return': 0.01911, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.041233}, '10d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.015006, 'median_return': 0.020334, 'mean_absolute_return': 0.024662, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.037957, 'median_return': 0.03801, 'mean_absolute_return': 0.041755, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.089661}, '60d': {'sample_size': 20, 'hit_rate': 0.95, 'avg_return': 0.094492, 'median_return': 0.109494, 'mean_absolute_return': 0.099088, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.005815, 'median_return': 0.012272, 'mean_absolute_return': 0.014511, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.023651}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.006695, 'median_return': 0.009709, 'mean_absolute_return': 0.016592, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.027457}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.009347, 'median_return': 0.013069, 'mean_absolute_return': 0.017068, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.026788, 'median_return': 0.043456, 'mean_absolute_return': 0.034274, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.114868, 'median_return': 0.119272, 'mean_absolute_return': 0.114868, 'max_adverse_excursion': 0.099512, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.002205, 'median_return': -0.002225, 'mean_absolute_return': 0.016849, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -6e-05, 'median_return': -0.003796, 'mean_absolute_return': 0.019268, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.004967, 'median_return': 0.004196, 'mean_absolute_return': 0.02283, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.022372, 'median_return': 0.028881, 'mean_absolute_return': 0.03892, 'max_adverse_excursion': -0.082211, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 72, 'hit_rate': 0.8889, 'avg_return': 0.080948, 'median_return': 0.098256, 'mean_absolute_return': 0.09565, 'max_adverse_excursion': -0.099444, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.65}, '5d': {'sample_size': 80, 'hit_rate': 0.6125}, '10d': {'sample_size': 80, 'hit_rate': 0.5}, '20d': {'sample_size': 80, 'hit_rate': 0.4375}, '60d': {'sample_size': 80, 'hit_rate': 0.325}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.175, 'both_hit': 15, 'both_miss': 5}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.15, 'both_hit': 13, 'both_miss': 7}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.125, 'both_hit': 15, 'both_miss': 5}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': -0.275, 'both_hit': 16, 'both_miss': 4}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.9, 'primary_minus_secondary': -0.575, 'both_hit': 19, 'both_miss': 1}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.001776, 'median_return': 0.003757, 'mean_absolute_return': 0.015898, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': 0.003048, 'median_return': 0.003789, 'mean_absolute_return': 0.018505, 'max_adverse_excursion': -0.034174, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.007438, 'median_return': 0.005356, 'mean_absolute_return': 0.019276, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 60, 'hit_rate': 0.7833, 'avg_return': 0.030844, 'median_return': 0.031464, 'mean_absolute_return': 0.036808, 'max_adverse_excursion': -0.032124, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 60, 'hit_rate': 0.9333, 'avg_return': 0.085716, 'median_return': 0.099838, 'mean_absolute_return': 0.0934, 'max_adverse_excursion': -0.085385, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.2, 'avg_return': -0.01094, 'median_return': -0.01091, 'mean_absolute_return': 0.018767, 'max_adverse_excursion': -0.036767, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.006684, 'median_return': -0.005796, 'mean_absolute_return': 0.020486, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.000694, 'median_return': 0.000478, 'mean_absolute_return': 0.031185, 'max_adverse_excursion': -0.053986, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.001276, 'median_return': 0.017648, 'mean_absolute_return': 0.043396, 'max_adverse_excursion': -0.082211, 'max_favorable_excursion': 0.067793}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.080213, 'median_return': 0.113908, 'mean_absolute_return': 0.110088, 'max_adverse_excursion': -0.099444, 'max_favorable_excursion': 0.176653}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.3833`, avg `-0.004603`, median `-0.003676`, mae `0.016811`
- 5d: sample `60`, hit `0.4`, avg `-0.002373`, median `-0.005796`, mae `0.018963`
- 10d: sample `60`, hit `0.5833`, avg `0.002204`, median `0.003921`, mae `0.021451`
- 20d: sample `60`, hit `0.6833`, avg `0.017766`, median `0.027885`, mae `0.037355`
- 60d: sample `60`, hit `0.8833`, avg `0.080956`, median `0.103071`, mae `0.097067`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.002574`, median `-0.001227`, mae `0.020524`
- 5d: sample `20`, hit `0.4`, avg `4.3e-05`, median `-0.010111`, mae `0.022619`
- 10d: sample `20`, hit `0.5`, avg `0.00387`, median `0.00241`, mae `0.020141`
- 20d: sample `20`, hit `0.8`, avg `0.02931`, median `0.027885`, mae `0.033239`
- 60d: sample `20`, hit `0.9`, avg `0.067117`, median `0.073403`, mae `0.08349`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.008195`, median `0.012542`, mae `0.01603`
- 5d: sample `20`, hit `0.65`, avg `0.009581`, median `0.010241`, mae `0.01911`
- 10d: sample `20`, hit `0.75`, avg `0.015006`, median `0.020334`, mae `0.024662`
- 20d: sample `20`, hit `0.8`, avg `0.037957`, median `0.03801`, mae `0.041755`
- 60d: sample `20`, hit `0.95`, avg `0.094492`, median `0.109494`, mae `0.099088`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.3833`, avg `-0.004603`, median `-0.003676`, mae `0.016811`
- 5d: sample `60`, hit `0.4`, avg `-0.002373`, median `-0.005796`, mae `0.018963`
- 10d: sample `60`, hit `0.5833`, avg `0.002204`, median `0.003921`, mae `0.021451`
- 20d: sample `60`, hit `0.6833`, avg `0.017766`, median `0.027885`, mae `0.037355`
- 60d: sample `60`, hit `0.8833`, avg `0.080956`, median `0.103071`, mae `0.097067`

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
- 3d: sample `80`, hit `0.475`, avg `-0.001403`, median `-0.001058`, mae `0.016616`
- 5d: sample `80`, hit `0.4625`, avg `0.000615`, median `-0.002538`, mae `0.019`
- 10d: sample `80`, hit `0.625`, avg `0.005405`, median `0.004547`, mae `0.022254`
- 20d: sample `80`, hit `0.7125`, avg `0.022814`, median `0.028881`, mae `0.038455`
- 60d: sample `80`, hit `0.9`, avg `0.08434`, median `0.103071`, mae `0.097572`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.008195`, median `0.012542`, mae `0.01603`
- 5d: sample `20`, hit `0.65`, avg `0.009581`, median `0.010241`, mae `0.01911`
- 10d: sample `20`, hit `0.75`, avg `0.015006`, median `0.020334`, mae `0.024662`
- 20d: sample `20`, hit `0.8`, avg `0.037957`, median `0.03801`, mae `0.041755`
- 60d: sample `20`, hit `0.95`, avg `0.094492`, median `0.109494`, mae `0.099088`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.475`, avg `-0.001403`, median `-0.001058`, mae `0.016616`
- 5d: sample `80`, hit `0.4625`, avg `0.000615`, median `-0.002538`, mae `0.019`
- 10d: sample `80`, hit `0.625`, avg `0.005405`, median `0.004547`, mae `0.022254`
- 20d: sample `80`, hit `0.7125`, avg `0.022814`, median `0.028881`, mae `0.038455`
- 60d: sample `80`, hit `0.9`, avg `0.08434`, median `0.103071`, mae `0.097572`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.008195`, median `0.012542`, mae `0.01603`
- 5d: sample `20`, hit `0.65`, avg `0.009581`, median `0.010241`, mae `0.01911`
- 10d: sample `20`, hit `0.75`, avg `0.015006`, median `0.020334`, mae `0.024662`
- 20d: sample `20`, hit `0.8`, avg `0.037957`, median `0.03801`, mae `0.041755`
- 60d: sample `20`, hit `0.95`, avg `0.094492`, median `0.109494`, mae `0.099088`

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
