# High Confidence Edge Report

Generated at: `2026-09-08T16:41:26.126947+00:00`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.003432`, median `0.00099`, mae `0.016012`
- 5d: sample `20`, hit `0.6`, avg `0.002926`, median `0.008039`, mae `0.019148`
- 10d: sample `20`, hit `0.45`, avg `-0.002629`, median `-0.011208`, mae `0.028549`
- 20d: sample `20`, hit `0.6`, avg `0.004577`, median `0.007572`, mae `0.03696`
- 60d: sample `20`, hit `0.75`, avg `0.024541`, median `0.037213`, mae `0.06327`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.5`, avg `-8.2e-05`, median `0.000603`, mae `0.013213`
- 5d: sample `60`, hit `0.5167`, avg `-0.001899`, median `0.000415`, mae `0.016217`
- 10d: sample `60`, hit `0.3833`, avg `0.000507`, median `-0.007117`, mae `0.022748`
- 20d: sample `60`, hit `0.7`, avg `0.011571`, median `0.020226`, mae `0.03525`
- 60d: sample `60`, hit `0.6833`, avg `0.039747`, median `0.059495`, mae `0.07036`

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
- 3d: sample `8`, hit `0.625`, avg `0.002979`, median `0.012525`, mae `0.017213`
- 5d: sample `8`, hit `0.625`, avg `0.008595`, median `0.008039`, mae `0.016819`
- 10d: sample `8`, hit `0.5`, avg `-0.005178`, median `9.9e-05`, mae `0.019029`
- 20d: sample `8`, hit `0.625`, avg `-0.002322`, median `0.007572`, mae `0.032476`
- 60d: sample `8`, hit `0.75`, avg `0.004335`, median `0.008034`, mae `0.059904`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.008227`, median `-0.001811`, mae `0.011747`
- 5d: sample `8`, hit `0.375`, avg `-0.006347`, median `-0.004438`, mae `0.013405`
- 10d: sample `8`, hit `0.5`, avg `0.00081`, median `0.0076`, mae `0.020027`
- 20d: sample `8`, hit `0.75`, avg `0.006395`, median `0.026531`, mae `0.026536`
- 60d: sample `8`, hit `0.625`, avg `0.018545`, median `0.046132`, mae `0.062243`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.003432, 'median_return': 0.00099, 'mean_absolute_return': 0.016012, 'max_adverse_excursion': -0.052474, 'max_favorable_excursion': 0.026658}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.002926, 'median_return': 0.008039, 'mean_absolute_return': 0.019148, 'max_adverse_excursion': -0.04784, 'max_favorable_excursion': 0.043092}, '10d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.002629, 'median_return': -0.011208, 'mean_absolute_return': 0.028549, 'max_adverse_excursion': -0.05316, 'max_favorable_excursion': 0.046424}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.004577, 'median_return': 0.007572, 'mean_absolute_return': 0.03696, 'max_adverse_excursion': -0.090764, 'max_favorable_excursion': 0.062064}, '60d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.024541, 'median_return': 0.037213, 'mean_absolute_return': 0.06327, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.116107}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.008227, 'median_return': -0.001811, 'mean_absolute_return': 0.011747, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.01018}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.006347, 'median_return': -0.004438, 'mean_absolute_return': 0.013405, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.00081, 'median_return': 0.0076, 'mean_absolute_return': 0.020027, 'max_adverse_excursion': -0.023505, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.006395, 'median_return': 0.026531, 'mean_absolute_return': 0.026536, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.031658}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.018545, 'median_return': 0.046132, 'mean_absolute_return': 0.062243, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.095045}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': -0.000108, 'median_return': 0.000766, 'mean_absolute_return': 0.014153, 'max_adverse_excursion': -0.052474, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': -6.5e-05, 'median_return': 0.001303, 'mean_absolute_return': 0.017344, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': -0.000398, 'median_return': -0.007491, 'mean_absolute_return': 0.024662, 'max_adverse_excursion': -0.05316, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.010203, 'median_return': 0.016175, 'mean_absolute_return': 0.036693, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.037879, 'median_return': 0.057625, 'mean_absolute_return': 0.069292, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4625}, '5d': {'sample_size': 80, 'hit_rate': 0.5125}, '10d': {'sample_size': 80, 'hit_rate': 0.4}, '20d': {'sample_size': 80, 'hit_rate': 0.5}, '60d': {'sample_size': 80, 'hit_rate': 0.55}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.1, 'both_hit': 11, 'both_miss': 9}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.025, 'both_hit': 12, 'both_miss': 8}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.175, 'both_hit': 9, 'both_miss': 11}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.05, 'both_hit': 12, 'both_miss': 8}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.025, 'both_hit': 15, 'both_miss': 5}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5125, 'avg_return': -0.00092, 'median_return': 0.000616, 'mean_absolute_return': 0.013913, 'max_adverse_excursion': -0.052474, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 80, 'hit_rate': 0.5375, 'avg_return': -0.000693, 'median_return': 0.000873, 'mean_absolute_return': 0.01695, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 80, 'hit_rate': 0.4, 'avg_return': -0.000277, 'median_return': -0.007491, 'mean_absolute_return': 0.024198, 'max_adverse_excursion': -0.05316, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.009822, 'median_return': 0.016175, 'mean_absolute_return': 0.035677, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 80, 'hit_rate': 0.7, 'avg_return': 0.035945, 'median_return': 0.053843, 'mean_absolute_return': 0.068587, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.002498`, median `-0.001641`, mae `0.007963`
- 5d: sample `20`, hit `0.5`, avg `-0.004111`, median `0.000688`, mae `0.010091`
- 10d: sample `20`, hit `0.25`, avg `-0.009002`, median `-0.012383`, mae `0.0203`
- 20d: sample `20`, hit `0.45`, avg `-0.013876`, median `-0.003522`, mae `0.037002`
- 60d: sample `20`, hit `0.5`, avg `0.011253`, median `0.032982`, mae `0.062361`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001126`, median `0.00234`, mae `0.015838`
- 5d: sample `40`, hit `0.525`, avg `-0.000793`, median `0.000415`, mae `0.01928`
- 10d: sample `40`, hit `0.45`, avg `0.005261`, median `-0.001932`, mae `0.023972`
- 20d: sample `40`, hit `0.825`, avg `0.024294`, median `0.029029`, mae `0.034374`
- 60d: sample `40`, hit `0.775`, avg `0.053993`, median `0.065295`, mae `0.074359`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.002498`, median `-0.001641`, mae `0.007963`
- 5d: sample `20`, hit `0.5`, avg `-0.004111`, median `0.000688`, mae `0.010091`
- 10d: sample `20`, hit `0.25`, avg `-0.009002`, median `-0.012383`, mae `0.0203`
- 20d: sample `20`, hit `0.45`, avg `-0.013876`, median `-0.003522`, mae `0.037002`
- 60d: sample `20`, hit `0.5`, avg `0.011253`, median `0.032982`, mae `0.062361`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.002437`, median `0.001558`, mae `0.013178`
- 5d: sample `20`, hit `0.5`, avg `-0.006156`, median `0.000208`, mae `0.014425`
- 10d: sample `20`, hit `0.4`, avg `0.001113`, median `-0.001932`, mae `0.017661`
- 20d: sample `20`, hit `0.8`, avg `0.018214`, median `0.030297`, mae `0.035032`
- 60d: sample `20`, hit `0.75`, avg `0.041623`, median `0.065295`, mae `0.071981`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001126`, median `0.00234`, mae `0.015838`
- 5d: sample `40`, hit `0.525`, avg `-0.000793`, median `0.000415`, mae `0.01928`
- 10d: sample `40`, hit `0.45`, avg `0.005261`, median `-0.001932`, mae `0.023972`
- 20d: sample `40`, hit `0.825`, avg `0.024294`, median `0.029029`, mae `0.034374`
- 60d: sample `40`, hit `0.775`, avg `0.053993`, median `0.065295`, mae `0.074359`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.002498`, median `-0.001641`, mae `0.007963`
- 5d: sample `20`, hit `0.5`, avg `-0.004111`, median `0.000688`, mae `0.010091`
- 10d: sample `20`, hit `0.25`, avg `-0.009002`, median `-0.012383`, mae `0.0203`
- 20d: sample `20`, hit `0.45`, avg `-0.013876`, median `-0.003522`, mae `0.037002`
- 60d: sample `20`, hit `0.5`, avg `0.011253`, median `0.032982`, mae `0.062361`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.002935`, median `0.00099`, mae `0.014595`
- 5d: sample `40`, hit `0.55`, avg `-0.001615`, median `0.001239`, mae `0.016787`
- 10d: sample `40`, hit `0.425`, avg `-0.000758`, median `-0.006017`, mae `0.023105`
- 20d: sample `40`, hit `0.7`, avg `0.011395`, median `0.020068`, mae `0.035996`
- 60d: sample `40`, hit `0.75`, avg `0.033082`, median `0.046132`, mae `0.067626`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.004689`, median `0.009349`, mae `0.018498`
- 5d: sample `20`, hit `0.55`, avg `0.00457`, median `0.010908`, mae `0.024135`
- 10d: sample `20`, hit `0.5`, avg `0.009409`, median `0.001935`, mae `0.030282`
- 20d: sample `20`, hit `0.85`, avg `0.030375`, median `0.025442`, mae `0.033716`
- 60d: sample `20`, hit `0.8`, avg `0.066363`, median `0.069439`, mae `0.076738`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.002498`, median `-0.001641`, mae `0.007963`
- 5d: sample `20`, hit `0.5`, avg `-0.004111`, median `0.000688`, mae `0.010091`
- 10d: sample `20`, hit `0.25`, avg `-0.009002`, median `-0.012383`, mae `0.0203`
- 20d: sample `20`, hit `0.45`, avg `-0.013876`, median `-0.003522`, mae `0.037002`
- 60d: sample `20`, hit `0.5`, avg `0.011253`, median `0.032982`, mae `0.062361`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.004689`, median `0.009349`, mae `0.018498`
- 5d: sample `20`, hit `0.55`, avg `0.00457`, median `0.010908`, mae `0.024135`
- 10d: sample `20`, hit `0.5`, avg `0.009409`, median `0.001935`, mae `0.030282`
- 20d: sample `20`, hit `0.85`, avg `0.030375`, median `0.025442`, mae `0.033716`
- 60d: sample `20`, hit `0.8`, avg `0.066363`, median `0.069439`, mae `0.076738`

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

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

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
