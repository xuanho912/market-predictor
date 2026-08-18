# High Confidence Edge Report

Generated at: `2026-08-18T04:22:40.525170+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `60`
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
- sample_size: `60`
- 3d: sample `60`, hit `0.7167`, avg `0.007726`, median `0.00745`, mae `0.016326`
- 5d: sample `60`, hit `0.6667`, avg `0.010155`, median `0.012953`, mae `0.021883`
- 10d: sample `60`, hit `0.7167`, avg `0.02069`, median `0.019314`, mae `0.028562`
- 20d: sample `60`, hit `0.9`, avg `0.03854`, median `0.032102`, mae `0.04254`
- 60d: sample `60`, hit `0.75`, avg `0.039412`, median `0.053855`, mae `0.080047`

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
- sample_size: `6`
- 3d: sample `6`, hit `0.3333`, avg `-0.001592`, median `-0.001227`, mae `0.014002`
- 5d: sample `6`, hit `0.1667`, avg `-0.01503`, median `-0.014432`, mae `0.019427`
- 10d: sample `6`, hit `0.0`, avg `-0.01096`, median `-0.007019`, mae `0.01096`
- 20d: sample `6`, hit `1.0`, avg `0.025573`, median `0.032102`, mae `0.025573`
- 60d: sample `6`, hit `0.8333`, avg `0.004604`, median `0.02999`, mae `0.045333`

### confidence_score top 10%
- sample_size: `6`
- 3d: sample `6`, hit `0.3333`, avg `-0.012666`, median `-0.008613`, mae `0.020484`
- 5d: sample `6`, hit `0.1667`, avg `-0.021914`, median `-0.018783`, mae `0.028006`
- 10d: sample `6`, hit `0.6667`, avg `0.004445`, median `0.002896`, mae `0.016019`
- 20d: sample `6`, hit `0.6667`, avg `0.001676`, median `0.003625`, mae `0.009117`
- 60d: sample `6`, hit `0.1667`, avg `-0.026159`, median `-0.032965`, mae `0.04945`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.007726, 'median_return': 0.00745, 'mean_absolute_return': 0.016326, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.010155, 'median_return': 0.012953, 'mean_absolute_return': 0.021883, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.02069, 'median_return': 0.019314, 'mean_absolute_return': 0.028562, 'max_adverse_excursion': -0.045393, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 60, 'hit_rate': 0.9, 'avg_return': 0.03854, 'median_return': 0.032102, 'mean_absolute_return': 0.04254, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 60, 'hit_rate': 0.75, 'avg_return': 0.039412, 'median_return': 0.053855, 'mean_absolute_return': 0.080047, 'max_adverse_excursion': -0.195048, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 6, 'by_horizon': {'3d': {'sample_size': 6, 'hit_rate': 0.3333, 'avg_return': -0.012666, 'median_return': -0.008613, 'mean_absolute_return': 0.020484, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.018885}, '5d': {'sample_size': 6, 'hit_rate': 0.1667, 'avg_return': -0.021914, 'median_return': -0.018783, 'mean_absolute_return': 0.028006, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.018277}, '10d': {'sample_size': 6, 'hit_rate': 0.6667, 'avg_return': 0.004445, 'median_return': 0.002896, 'mean_absolute_return': 0.016019, 'max_adverse_excursion': -0.026516, 'max_favorable_excursion': 0.042458}, '20d': {'sample_size': 6, 'hit_rate': 0.6667, 'avg_return': 0.001676, 'median_return': 0.003625, 'mean_absolute_return': 0.009117, 'max_adverse_excursion': -0.020687, 'max_favorable_excursion': 0.01666}, '60d': {'sample_size': 6, 'hit_rate': 0.1667, 'avg_return': -0.026159, 'median_return': -0.032965, 'mean_absolute_return': 0.04945, 'max_adverse_excursion': -0.060736, 'max_favorable_excursion': 0.069875}}}, 'ordinary_confidence': {'sample_size': 54, 'by_horizon': {'3d': {'sample_size': 54, 'hit_rate': 0.7593, 'avg_return': 0.009992, 'median_return': 0.009204, 'mean_absolute_return': 0.015864, 'max_adverse_excursion': -0.034686, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 54, 'hit_rate': 0.7222, 'avg_return': 0.013718, 'median_return': 0.013411, 'mean_absolute_return': 0.021203, 'max_adverse_excursion': -0.034174, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 54, 'hit_rate': 0.7222, 'avg_return': 0.022495, 'median_return': 0.020503, 'mean_absolute_return': 0.029956, 'max_adverse_excursion': -0.045393, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 54, 'hit_rate': 0.9259, 'avg_return': 0.042636, 'median_return': 0.033597, 'mean_absolute_return': 0.046254, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 54, 'hit_rate': 0.8148, 'avg_return': 0.046698, 'median_return': 0.056874, 'mean_absolute_return': 0.083446, 'max_adverse_excursion': -0.195048, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 60, 'hit_rate': 0.7167}, '5d': {'sample_size': 60, 'hit_rate': 0.6667}, '10d': {'sample_size': 60, 'hit_rate': 0.7167}, '20d': {'sample_size': 60, 'hit_rate': 0.9}, '60d': {'sample_size': 60, 'hit_rate': 0.75}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 60, 'primary_hit_rate': 0.7167, 'secondary_hit_rate': 0.7167, 'primary_minus_secondary': 0.0, 'both_hit': 43, 'both_miss': 17}, '5d': {'sample_size': 60, 'primary_hit_rate': 0.6667, 'secondary_hit_rate': 0.6667, 'primary_minus_secondary': 0.0, 'both_hit': 40, 'both_miss': 20}, '10d': {'sample_size': 60, 'primary_hit_rate': 0.7167, 'secondary_hit_rate': 0.7167, 'primary_minus_secondary': 0.0, 'both_hit': 43, 'both_miss': 17}, '20d': {'sample_size': 60, 'primary_hit_rate': 0.9, 'secondary_hit_rate': 0.9, 'primary_minus_secondary': 0.0, 'both_hit': 54, 'both_miss': 6}, '60d': {'sample_size': 60, 'primary_hit_rate': 0.75, 'secondary_hit_rate': 0.75, 'primary_minus_secondary': 0.0, 'both_hit': 45, 'both_miss': 15}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.007726, 'median_return': 0.00745, 'mean_absolute_return': 0.016326, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.010155, 'median_return': 0.012953, 'mean_absolute_return': 0.021883, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.02069, 'median_return': 0.019314, 'mean_absolute_return': 0.028562, 'max_adverse_excursion': -0.045393, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 60, 'hit_rate': 0.9, 'avg_return': 0.03854, 'median_return': 0.032102, 'mean_absolute_return': 0.04254, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 60, 'hit_rate': 0.75, 'avg_return': 0.039412, 'median_return': 0.053855, 'mean_absolute_return': 0.080047, 'max_adverse_excursion': -0.195048, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.005021`, median `0.005804`, mae `0.008227`
- 5d: sample `20`, hit `0.75`, avg `0.009975`, median `0.012091`, mae `0.014715`
- 10d: sample `20`, hit `0.85`, avg `0.016016`, median `0.018352`, mae `0.016876`
- 20d: sample `20`, hit `1.0`, avg `0.030699`, median `0.033582`, mae `0.030699`
- 60d: sample `20`, hit `0.95`, avg `0.055448`, median `0.059104`, mae `0.05753`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008833`, median `0.016338`, mae `0.020983`
- 5d: sample `20`, hit `0.6`, avg `0.011208`, median `0.013193`, mae `0.024238`
- 10d: sample `20`, hit `0.55`, avg `0.024212`, median `0.037445`, mae `0.038735`
- 20d: sample `20`, hit `0.9`, avg `0.06102`, median `0.048862`, mae `0.062822`
- 60d: sample `20`, hit `0.75`, avg `0.046573`, median `0.04207`, mae `0.101363`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.005021`, median `0.005804`, mae `0.008227`
- 5d: sample `20`, hit `0.75`, avg `0.009975`, median `0.012091`, mae `0.014715`
- 10d: sample `20`, hit `0.85`, avg `0.016016`, median `0.018352`, mae `0.016876`
- 20d: sample `20`, hit `1.0`, avg `0.030699`, median `0.033582`, mae `0.030699`
- 60d: sample `20`, hit `0.95`, avg `0.055448`, median `0.059104`, mae `0.05753`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008833`, median `0.016338`, mae `0.020983`
- 5d: sample `20`, hit `0.6`, avg `0.011208`, median `0.013193`, mae `0.024238`
- 10d: sample `20`, hit `0.55`, avg `0.024212`, median `0.037445`, mae `0.038735`
- 20d: sample `20`, hit `0.9`, avg `0.06102`, median `0.048862`, mae `0.062822`
- 60d: sample `20`, hit `0.75`, avg `0.046573`, median `0.04207`, mae `0.101363`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.005021`, median `0.005804`, mae `0.008227`
- 5d: sample `20`, hit `0.75`, avg `0.009975`, median `0.012091`, mae `0.014715`
- 10d: sample `20`, hit `0.85`, avg `0.016016`, median `0.018352`, mae `0.016876`
- 20d: sample `20`, hit `1.0`, avg `0.030699`, median `0.033582`, mae `0.030699`
- 60d: sample `20`, hit `0.95`, avg `0.055448`, median `0.059104`, mae `0.05753`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008833`, median `0.016338`, mae `0.020983`
- 5d: sample `20`, hit `0.6`, avg `0.011208`, median `0.013193`, mae `0.024238`
- 10d: sample `20`, hit `0.55`, avg `0.024212`, median `0.037445`, mae `0.038735`
- 20d: sample `20`, hit `0.9`, avg `0.06102`, median `0.048862`, mae `0.062822`
- 60d: sample `20`, hit `0.75`, avg `0.046573`, median `0.04207`, mae `0.101363`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.005021`, median `0.005804`, mae `0.008227`
- 5d: sample `20`, hit `0.75`, avg `0.009975`, median `0.012091`, mae `0.014715`
- 10d: sample `20`, hit `0.85`, avg `0.016016`, median `0.018352`, mae `0.016876`
- 20d: sample `20`, hit `1.0`, avg `0.030699`, median `0.033582`, mae `0.030699`
- 60d: sample `20`, hit `0.95`, avg `0.055448`, median `0.059104`, mae `0.05753`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.009079`, median `0.016338`, mae `0.020376`
- 5d: sample `40`, hit `0.625`, avg `0.010245`, median `0.016537`, mae `0.025467`
- 10d: sample `40`, hit `0.65`, avg `0.023027`, median `0.021536`, mae `0.034406`
- 20d: sample `40`, hit `0.85`, avg `0.042461`, median `0.032102`, mae `0.048461`
- 60d: sample `40`, hit `0.65`, avg `0.031394`, median `0.04207`, mae `0.091305`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.005021`, median `0.005804`, mae `0.008227`
- 5d: sample `20`, hit `0.75`, avg `0.009975`, median `0.012091`, mae `0.014715`
- 10d: sample `20`, hit `0.85`, avg `0.016016`, median `0.018352`, mae `0.016876`
- 20d: sample `20`, hit `1.0`, avg `0.030699`, median `0.033582`, mae `0.030699`
- 60d: sample `20`, hit `0.95`, avg `0.055448`, median `0.059104`, mae `0.05753`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.7167`, avg `0.007726`, median `0.00745`, mae `0.016326`
- 5d: sample `60`, hit `0.6667`, avg `0.010155`, median `0.012953`, mae `0.021883`
- 10d: sample `60`, hit `0.7167`, avg `0.02069`, median `0.019314`, mae `0.028562`
- 20d: sample `60`, hit `0.9`, avg `0.03854`, median `0.032102`, mae `0.04254`
- 60d: sample `60`, hit `0.75`, avg `0.039412`, median `0.053855`, mae `0.080047`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.7167`, avg `0.007726`, median `0.00745`, mae `0.016326`
- 5d: sample `60`, hit `0.6667`, avg `0.010155`, median `0.012953`, mae `0.021883`
- 10d: sample `60`, hit `0.7167`, avg `0.02069`, median `0.019314`, mae `0.028562`
- 20d: sample `60`, hit `0.9`, avg `0.03854`, median `0.032102`, mae `0.04254`
- 60d: sample `60`, hit `0.75`, avg `0.039412`, median `0.053855`, mae `0.080047`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.7167`, avg `0.007726`, median `0.00745`, mae `0.016326`
- 5d: sample `60`, hit `0.6667`, avg `0.010155`, median `0.012953`, mae `0.021883`
- 10d: sample `60`, hit `0.7167`, avg `0.02069`, median `0.019314`, mae `0.028562`
- 20d: sample `60`, hit `0.9`, avg `0.03854`, median `0.032102`, mae `0.04254`
- 60d: sample `60`, hit `0.75`, avg `0.039412`, median `0.053855`, mae `0.080047`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.7167`, avg `0.007726`, median `0.00745`, mae `0.016326`
- 5d: sample `60`, hit `0.6667`, avg `0.010155`, median `0.012953`, mae `0.021883`
- 10d: sample `60`, hit `0.7167`, avg `0.02069`, median `0.019314`, mae `0.028562`
- 20d: sample `60`, hit `0.9`, avg `0.03854`, median `0.032102`, mae `0.04254`
- 60d: sample `60`, hit `0.75`, avg `0.039412`, median `0.053855`, mae `0.080047`

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
