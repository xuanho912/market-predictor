# High Confidence Edge Report

Generated at: `2026-09-24T06:14:35.805684+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `43`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `43`, gate `early_evidence`
- 5d: completed `43`, gate `early_evidence`
- 10d: completed `43`, gate `early_evidence`
- 20d: completed `43`, gate `early_evidence`
- 60d: completed `43`, gate `early_evidence`

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
- 3d: sample `60`, hit `0.4833`, avg `-0.00412`, median `-0.001227`, mae `0.016414`
- 5d: sample `60`, hit `0.4833`, avg `-0.008167`, median `-0.000423`, mae `0.017402`
- 10d: sample `60`, hit `0.4`, avg `-0.005897`, median `-0.007011`, mae `0.020076`
- 20d: sample `60`, hit `0.6`, avg `0.009363`, median `0.016027`, mae `0.03258`
- 60d: sample `60`, hit `0.6833`, avg `0.019239`, median `0.031273`, mae `0.055719`

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
- 3d: sample `8`, hit `0.25`, avg `-0.015931`, median `-0.024029`, mae `0.024002`
- 5d: sample `8`, hit `0.375`, avg `-0.020884`, median `-0.024165`, mae `0.026566`
- 10d: sample `8`, hit `0.125`, avg `-0.02023`, median `-0.017071`, mae `0.022988`
- 20d: sample `8`, hit `0.625`, avg `0.003485`, median `0.029166`, mae `0.049309`
- 60d: sample `8`, hit `0.75`, avg `0.032624`, median `0.072696`, mae `0.094557`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.015931`, median `-0.024029`, mae `0.024002`
- 5d: sample `8`, hit `0.375`, avg `-0.020884`, median `-0.024165`, mae `0.026566`
- 10d: sample `8`, hit `0.125`, avg `-0.02023`, median `-0.017071`, mae `0.022988`
- 20d: sample `8`, hit `0.625`, avg `0.003485`, median `0.029166`, mae `0.049309`
- 60d: sample `8`, hit `0.75`, avg `0.032624`, median `0.072696`, mae `0.094557`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': -0.00412, 'median_return': -0.001227, 'mean_absolute_return': 0.016414, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.029069}, '5d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': -0.008167, 'median_return': -0.000423, 'mean_absolute_return': 0.017402, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 60, 'hit_rate': 0.4, 'avg_return': -0.005897, 'median_return': -0.007011, 'mean_absolute_return': 0.020076, 'max_adverse_excursion': -0.06798, 'max_favorable_excursion': 0.051845}, '20d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.009363, 'median_return': 0.016027, 'mean_absolute_return': 0.03258, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.019239, 'median_return': 0.031273, 'mean_absolute_return': 0.055719, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.015931, 'median_return': -0.024029, 'mean_absolute_return': 0.024002, 'max_adverse_excursion': -0.036428, 'max_favorable_excursion': 0.020012}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.020884, 'median_return': -0.024165, 'mean_absolute_return': 0.026566, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.02023, 'median_return': -0.017071, 'mean_absolute_return': 0.022988, 'max_adverse_excursion': -0.060333, 'max_favorable_excursion': 0.011031}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.003485, 'median_return': 0.029166, 'mean_absolute_return': 0.049309, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.058396}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.032624, 'median_return': 0.072696, 'mean_absolute_return': 0.094557, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.005247, 'median_return': -0.003649, 'mean_absolute_return': 0.016244, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.010197, 'median_return': -0.011684, 'mean_absolute_return': 0.019612, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.008791, 'median_return': -0.007314, 'mean_absolute_return': 0.026536, 'max_adverse_excursion': -0.080172, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.008457, 'median_return': 0.013156, 'mean_absolute_return': 0.037869, 'max_adverse_excursion': -0.118199, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.024103, 'median_return': 0.041902, 'mean_absolute_return': 0.061044, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.145995}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.525}, '10d': {'sample_size': 80, 'hit_rate': 0.425}, '20d': {'sample_size': 80, 'hit_rate': 0.5125}, '60d': {'sample_size': 80, 'hit_rate': 0.45}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.05, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.4, 'avg_return': -0.006316, 'median_return': -0.003676, 'mean_absolute_return': 0.01702, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 80, 'hit_rate': 0.4, 'avg_return': -0.011265, 'median_return': -0.011925, 'mean_absolute_return': 0.020308, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 80, 'hit_rate': 0.375, 'avg_return': -0.009935, 'median_return': -0.009882, 'mean_absolute_return': 0.026182, 'max_adverse_excursion': -0.080172, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': 0.007959, 'median_return': 0.015416, 'mean_absolute_return': 0.039013, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 80, 'hit_rate': 0.7, 'avg_return': 0.024955, 'median_return': 0.04207, 'mean_absolute_return': 0.064395, 'max_adverse_excursion': -0.203511, 'max_favorable_excursion': 0.145995}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `80`, hit `0.4`, avg `-0.006316`, median `-0.003676`, mae `0.01702`
- 5d: sample `80`, hit `0.4`, avg `-0.011265`, median `-0.011925`, mae `0.020308`
- 10d: sample `80`, hit `0.375`, avg `-0.009935`, median `-0.009882`, mae `0.026182`
- 20d: sample `80`, hit `0.5625`, avg `0.007959`, median `0.015416`, mae `0.039013`
- 60d: sample `80`, hit `0.7`, avg `0.024955`, median `0.04207`, mae `0.064395`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.007573`, median `-0.009383`, mae `0.019424`
- 5d: sample `40`, hit `0.425`, avg `-0.011758`, median `-0.015413`, mae `0.020713`
- 10d: sample `40`, hit `0.3`, avg `-0.012603`, median `-0.010456`, mae `0.01999`
- 20d: sample `40`, hit `0.575`, avg `0.007924`, median `0.016745`, mae `0.034328`
- 60d: sample `40`, hit `0.65`, avg `0.019539`, median `0.037425`, mae `0.060746`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.004204`, median `-0.001658`, mae `0.016465`
- 5d: sample `40`, hit `0.475`, avg `-0.008965`, median `-0.000423`, mae `0.017297`
- 10d: sample `40`, hit `0.4`, avg `-0.003333`, median `-0.006017`, mae `0.019981`
- 20d: sample `40`, hit `0.6`, avg `0.007095`, median `0.016027`, mae `0.03462`
- 60d: sample `40`, hit `0.675`, avg `0.018083`, median `0.031273`, mae `0.05939`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.007573`, median `-0.009383`, mae `0.019424`
- 5d: sample `40`, hit `0.425`, avg `-0.011758`, median `-0.015413`, mae `0.020713`
- 10d: sample `40`, hit `0.3`, avg `-0.012603`, median `-0.010456`, mae `0.01999`
- 20d: sample `40`, hit `0.575`, avg `0.007924`, median `0.016745`, mae `0.034328`
- 60d: sample `40`, hit `0.65`, avg `0.019539`, median `0.037425`, mae `0.060746`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.375`, avg `-0.005058`, median `-0.001797`, mae `0.014616`
- 5d: sample `40`, hit `0.375`, avg `-0.010773`, median `-0.011684`, mae `0.019902`
- 10d: sample `40`, hit `0.45`, avg `-0.007266`, median `-0.006389`, mae `0.032373`
- 20d: sample `40`, hit `0.55`, avg `0.007995`, median `0.013156`, mae `0.043698`
- 60d: sample `40`, hit `0.75`, avg `0.030371`, median `0.044683`, mae `0.068044`

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
- 3d: sample `80`, hit `0.4`, avg `-0.006316`, median `-0.003676`, mae `0.01702`
- 5d: sample `80`, hit `0.4`, avg `-0.011265`, median `-0.011925`, mae `0.020308`
- 10d: sample `80`, hit `0.375`, avg `-0.009935`, median `-0.009882`, mae `0.026182`
- 20d: sample `80`, hit `0.5625`, avg `0.007959`, median `0.015416`, mae `0.039013`
- 60d: sample `80`, hit `0.7`, avg `0.024955`, median `0.04207`, mae `0.064395`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.007573`, median `-0.009383`, mae `0.019424`
- 5d: sample `40`, hit `0.425`, avg `-0.011758`, median `-0.015413`, mae `0.020713`
- 10d: sample `40`, hit `0.3`, avg `-0.012603`, median `-0.010456`, mae `0.01999`
- 20d: sample `40`, hit `0.575`, avg `0.007924`, median `0.016745`, mae `0.034328`
- 60d: sample `40`, hit `0.65`, avg `0.019539`, median `0.037425`, mae `0.060746`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4`, avg `-0.006316`, median `-0.003676`, mae `0.01702`
- 5d: sample `80`, hit `0.4`, avg `-0.011265`, median `-0.011925`, mae `0.020308`
- 10d: sample `80`, hit `0.375`, avg `-0.009935`, median `-0.009882`, mae `0.026182`
- 20d: sample `80`, hit `0.5625`, avg `0.007959`, median `0.015416`, mae `0.039013`
- 60d: sample `80`, hit `0.7`, avg `0.024955`, median `0.04207`, mae `0.064395`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.007573`, median `-0.009383`, mae `0.019424`
- 5d: sample `40`, hit `0.425`, avg `-0.011758`, median `-0.015413`, mae `0.020713`
- 10d: sample `40`, hit `0.3`, avg `-0.012603`, median `-0.010456`, mae `0.01999`
- 20d: sample `40`, hit `0.575`, avg `0.007924`, median `0.016745`, mae `0.034328`
- 60d: sample `40`, hit `0.65`, avg `0.019539`, median `0.037425`, mae `0.060746`

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
