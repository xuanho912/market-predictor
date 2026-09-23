# High Confidence Edge Report

Generated at: `2026-09-23T17:03:03.180313+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `40`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `40`, gate `early_evidence`
- 5d: completed `40`, gate `early_evidence`
- 10d: completed `40`, gate `early_evidence`
- 20d: completed `40`, gate `early_evidence`
- 60d: completed `40`, gate `early_evidence`

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
- 3d: sample `60`, hit `0.4833`, avg `-0.004481`, median `-0.001227`, mae `0.016053`
- 5d: sample `60`, hit `0.4667`, avg `-0.008664`, median `-0.001562`, mae `0.01744`
- 10d: sample `60`, hit `0.4`, avg `-0.00584`, median `-0.007011`, mae `0.020133`
- 20d: sample `60`, hit `0.6`, avg `0.009906`, median `0.016745`, mae `0.033123`
- 60d: sample `60`, hit `0.7`, avg `0.022049`, median `0.037425`, mae `0.056714`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.15`, avg `-0.012903`, median `-0.010273`, mae `0.018838`
- 5d: sample `20`, hit `0.15`, avg `-0.02056`, median `-0.022868`, mae `0.029026`
- 10d: sample `20`, hit `0.3`, avg `-0.022048`, median `-0.037905`, mae `0.044498`
- 20d: sample `20`, hit `0.45`, avg `0.003748`, median `-0.00018`, mae `0.058313`
- 60d: sample `20`, hit `0.75`, avg `0.042104`, median `0.079528`, mae `0.090423`

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
- 3d: sample `8`, hit `0.25`, avg `-0.016807`, median `-0.030499`, mae `0.024878`
- 5d: sample `8`, hit `0.375`, avg `-0.01718`, median `-0.016421`, mae `0.022862`
- 10d: sample `8`, hit `0.25`, avg `-0.012488`, median `-0.011432`, mae `0.015647`
- 20d: sample `8`, hit `0.75`, avg `0.014597`, median `0.029166`, mae `0.044724`
- 60d: sample `8`, hit `0.875`, avg `0.053341`, median `0.072696`, mae `0.088622`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.016807`, median `-0.030499`, mae `0.024878`
- 5d: sample `8`, hit `0.375`, avg `-0.01718`, median `-0.016421`, mae `0.022862`
- 10d: sample `8`, hit `0.25`, avg `-0.012488`, median `-0.011432`, mae `0.015647`
- 20d: sample `8`, hit `0.75`, avg `0.014597`, median `0.029166`, mae `0.044724`
- 60d: sample `8`, hit `0.875`, avg `0.053341`, median `0.072696`, mae `0.088622`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': -0.004481, 'median_return': -0.001227, 'mean_absolute_return': 0.016053, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.008664, 'median_return': -0.001562, 'mean_absolute_return': 0.01744, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 60, 'hit_rate': 0.4, 'avg_return': -0.00584, 'median_return': -0.007011, 'mean_absolute_return': 0.020133, 'max_adverse_excursion': -0.06798, 'max_favorable_excursion': 0.051845}, '20d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.009906, 'median_return': 0.016745, 'mean_absolute_return': 0.033123, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.022049, 'median_return': 0.037425, 'mean_absolute_return': 0.056714, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.016807, 'median_return': -0.030499, 'mean_absolute_return': 0.024878, 'max_adverse_excursion': -0.036428, 'max_favorable_excursion': 0.020012}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.01718, 'median_return': -0.016421, 'mean_absolute_return': 0.022862, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.012488, 'median_return': -0.011432, 'mean_absolute_return': 0.015647, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.011031}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.014597, 'median_return': 0.029166, 'mean_absolute_return': 0.044724, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.058396}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.053341, 'median_return': 0.072696, 'mean_absolute_return': 0.088622, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.005451, 'median_return': -0.003649, 'mean_absolute_return': 0.015846, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': -0.011022, 'median_return': -0.011925, 'mean_absolute_return': 0.020056, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': -0.009604, 'median_return': -0.007491, 'mean_absolute_return': 0.027399, 'max_adverse_excursion': -0.080172, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.007674, 'median_return': 0.013156, 'mean_absolute_return': 0.038831, 'max_adverse_excursion': -0.118199, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.024143, 'median_return': 0.041902, 'mean_absolute_return': 0.062533, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.145995}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.575}, '5d': {'sample_size': 80, 'hit_rate': 0.5625}, '10d': {'sample_size': 80, 'hit_rate': 0.475}, '20d': {'sample_size': 80, 'hit_rate': 0.5875}, '60d': {'sample_size': 80, 'hit_rate': 0.5875}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.075, 'both_hit': 23, 'both_miss': 17}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.075, 'both_hit': 22, 'both_miss': 18}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 20, 'both_miss': 20}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': 0.05, 'both_hit': 25, 'both_miss': 15}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.075, 'both_hit': 30, 'both_miss': 10}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.4, 'avg_return': -0.006587, 'median_return': -0.003676, 'mean_absolute_return': 0.016749, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 80, 'hit_rate': 0.3875, 'avg_return': -0.011638, 'median_return': -0.013229, 'mean_absolute_return': 0.020337, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 80, 'hit_rate': 0.375, 'avg_return': -0.009892, 'median_return': -0.009882, 'mean_absolute_return': 0.026224, 'max_adverse_excursion': -0.080172, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': 0.008367, 'median_return': 0.016027, 'mean_absolute_return': 0.03942, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 80, 'hit_rate': 0.7125, 'avg_return': 0.027063, 'median_return': 0.044683, 'mean_absolute_return': 0.065142, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.145995}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.003953`, median `0.001405`, mae `0.016312`
- 5d: sample `20`, hit `0.5`, avg `-0.006572`, median `0.000688`, mae `0.017611`
- 10d: sample `20`, hit `0.4`, avg `-0.011024`, median `-0.007491`, mae `0.020266`
- 20d: sample `20`, hit `0.6`, avg `0.0139`, median `0.01927`, mae `0.028499`
- 60d: sample `20`, hit `0.7`, avg `0.02155`, median `0.046407`, mae `0.048376`

### breadth_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4`, avg `-0.006587`, median `-0.003676`, mae `0.016749`
- 5d: sample `80`, hit `0.3875`, avg `-0.011638`, median `-0.013229`, mae `0.020337`
- 10d: sample `80`, hit `0.375`, avg `-0.009892`, median `-0.009882`, mae `0.026224`
- 20d: sample `80`, hit `0.5625`, avg `0.008367`, median `0.016027`, mae `0.03942`
- 60d: sample `80`, hit `0.7125`, avg `0.027063`, median `0.044683`, mae `0.065142`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.003953`, median `0.001405`, mae `0.016312`
- 5d: sample `20`, hit `0.5`, avg `-0.006572`, median `0.000688`, mae `0.017611`
- 10d: sample `20`, hit `0.4`, avg `-0.011024`, median `-0.007491`, mae `0.020266`
- 20d: sample `20`, hit `0.6`, avg `0.0139`, median `0.01927`, mae `0.028499`
- 60d: sample `20`, hit `0.7`, avg `0.02155`, median `0.046407`, mae `0.048376`

### breadth_conflicted_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4833`, avg `-0.004481`, median `-0.001227`, mae `0.016053`
- 5d: sample `60`, hit `0.4667`, avg `-0.008664`, median `-0.001562`, mae `0.01744`
- 10d: sample `60`, hit `0.4`, avg `-0.00584`, median `-0.007011`, mae `0.020133`
- 20d: sample `60`, hit `0.6`, avg `0.009906`, median `0.016745`, mae `0.033123`
- 60d: sample `60`, hit `0.7`, avg `0.022049`, median `0.037425`, mae `0.056714`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.004746`, median `-0.001658`, mae `0.015923`
- 5d: sample `40`, hit `0.45`, avg `-0.009711`, median `-0.001562`, mae `0.017355`
- 10d: sample `40`, hit `0.4`, avg `-0.003248`, median `-0.006017`, mae `0.020066`
- 20d: sample `40`, hit `0.6`, avg `0.007909`, median `0.016745`, mae `0.035435`
- 60d: sample `40`, hit `0.7`, avg `0.022299`, median `0.037425`, mae `0.060883`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.003953`, median `0.001405`, mae `0.016312`
- 5d: sample `20`, hit `0.5`, avg `-0.006572`, median `0.000688`, mae `0.017611`
- 10d: sample `20`, hit `0.4`, avg `-0.011024`, median `-0.007491`, mae `0.020266`
- 20d: sample `20`, hit `0.6`, avg `0.0139`, median `0.01927`, mae `0.028499`
- 60d: sample `20`, hit `0.7`, avg `0.02155`, median `0.046407`, mae `0.048376`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.004746`, median `-0.001658`, mae `0.015923`
- 5d: sample `40`, hit `0.45`, avg `-0.009711`, median `-0.001562`, mae `0.017355`
- 10d: sample `40`, hit `0.4`, avg `-0.003248`, median `-0.006017`, mae `0.020066`
- 20d: sample `40`, hit `0.6`, avg `0.007909`, median `0.016745`, mae `0.035435`
- 60d: sample `40`, hit `0.7`, avg `0.022299`, median `0.037425`, mae `0.060883`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.15`, avg `-0.012903`, median `-0.010273`, mae `0.018838`
- 5d: sample `20`, hit `0.15`, avg `-0.02056`, median `-0.022868`, mae `0.029026`
- 10d: sample `20`, hit `0.3`, avg `-0.022048`, median `-0.037905`, mae `0.044498`
- 20d: sample `20`, hit `0.45`, avg `0.003748`, median `-0.00018`, mae `0.058313`
- 60d: sample `20`, hit `0.75`, avg `0.042104`, median `0.079528`, mae `0.090423`

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
- 3d: sample `80`, hit `0.4`, avg `-0.006587`, median `-0.003676`, mae `0.016749`
- 5d: sample `80`, hit `0.3875`, avg `-0.011638`, median `-0.013229`, mae `0.020337`
- 10d: sample `80`, hit `0.375`, avg `-0.009892`, median `-0.009882`, mae `0.026224`
- 20d: sample `80`, hit `0.5625`, avg `0.008367`, median `0.016027`, mae `0.03942`
- 60d: sample `80`, hit `0.7125`, avg `0.027063`, median `0.044683`, mae `0.065142`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.4833`, avg `-0.004481`, median `-0.001227`, mae `0.016053`
- 5d: sample `60`, hit `0.4667`, avg `-0.008664`, median `-0.001562`, mae `0.01744`
- 10d: sample `60`, hit `0.4`, avg `-0.00584`, median `-0.007011`, mae `0.020133`
- 20d: sample `60`, hit `0.6`, avg `0.009906`, median `0.016745`, mae `0.033123`
- 60d: sample `60`, hit `0.7`, avg `0.022049`, median `0.037425`, mae `0.056714`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.004746`, median `-0.001658`, mae `0.015923`
- 5d: sample `40`, hit `0.45`, avg `-0.009711`, median `-0.001562`, mae `0.017355`
- 10d: sample `40`, hit `0.4`, avg `-0.003248`, median `-0.006017`, mae `0.020066`
- 20d: sample `40`, hit `0.6`, avg `0.007909`, median `0.016745`, mae `0.035435`
- 60d: sample `40`, hit `0.7`, avg `0.022299`, median `0.037425`, mae `0.060883`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.004746`, median `-0.001658`, mae `0.015923`
- 5d: sample `40`, hit `0.45`, avg `-0.009711`, median `-0.001562`, mae `0.017355`
- 10d: sample `40`, hit `0.4`, avg `-0.003248`, median `-0.006017`, mae `0.020066`
- 20d: sample `40`, hit `0.6`, avg `0.007909`, median `0.016745`, mae `0.035435`
- 60d: sample `40`, hit `0.7`, avg `0.022299`, median `0.037425`, mae `0.060883`

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
