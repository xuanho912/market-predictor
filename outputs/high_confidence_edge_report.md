# High Confidence Edge Report

Generated at: `2026-07-19T13:56:11.620427+00:00`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `-0.002057`, median `0.004487`, mae `0.015636`
- 5d: sample `40`, hit `0.575`, avg `-0.001984`, median `0.003005`, mae `0.019106`
- 10d: sample `40`, hit `0.325`, avg `-0.003033`, median `-0.011432`, mae `0.024207`
- 20d: sample `40`, hit `0.725`, avg `0.01684`, median `0.020068`, mae `0.036455`
- 60d: sample `40`, hit `0.775`, avg `0.052529`, median `0.092892`, mae `0.087718`

### MODERATE_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `-0.000332`, median `0.001139`, mae `0.011143`
- 5d: sample `40`, hit `0.55`, avg `0.000841`, median `0.001303`, mae `0.014409`
- 10d: sample `40`, hit `0.55`, avg `0.002391`, median `0.001455`, mae `0.025885`
- 20d: sample `40`, hit `0.75`, avg `0.015876`, median `0.020226`, mae `0.034302`
- 60d: sample `40`, hit `0.55`, avg `0.022949`, median `0.046407`, mae `0.064805`

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
- 3d: sample `8`, hit `0.25`, avg `-0.014894`, median `-0.001658`, mae `0.016426`
- 5d: sample `8`, hit `0.5`, avg `-0.010839`, median `0.003829`, mae `0.021031`
- 10d: sample `8`, hit `0.375`, avg `-0.002733`, median `-0.0004`, mae `0.022516`
- 20d: sample `8`, hit `0.875`, avg `0.018363`, median `0.029166`, mae `0.032189`
- 60d: sample `8`, hit `0.875`, avg `0.053794`, median `0.059495`, mae `0.068012`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.014894`, median `-0.001658`, mae `0.016426`
- 5d: sample `8`, hit `0.5`, avg `-0.010839`, median `0.003829`, mae `0.021031`
- 10d: sample `8`, hit `0.375`, avg `-0.002733`, median `-0.0004`, mae `0.022516`
- 20d: sample `8`, hit `0.875`, avg `0.018363`, median `0.029166`, mae `0.032189`
- 60d: sample `8`, hit `0.875`, avg `0.053794`, median `0.059495`, mae `0.068012`

### confidence validation
- `{'strong_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': -0.002057, 'median_return': 0.004487, 'mean_absolute_return': 0.015636, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.023707}, '5d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': -0.001984, 'median_return': 0.003005, 'mean_absolute_return': 0.019106, 'max_adverse_excursion': -0.078114, 'max_favorable_excursion': 0.035465}, '10d': {'sample_size': 40, 'hit_rate': 0.325, 'avg_return': -0.003033, 'median_return': -0.011432, 'mean_absolute_return': 0.024207, 'max_adverse_excursion': -0.047759, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.01684, 'median_return': 0.020068, 'mean_absolute_return': 0.036455, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076981}, '60d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.052529, 'median_return': 0.092892, 'mean_absolute_return': 0.087718, 'max_adverse_excursion': -0.15079, 'max_favorable_excursion': 0.1448}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.014894, 'median_return': -0.001658, 'mean_absolute_return': 0.016426, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.003785}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.010839, 'median_return': 0.003829, 'mean_absolute_return': 0.021031, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.022634}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.002733, 'median_return': -0.0004, 'mean_absolute_return': 0.022516, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.036071}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.018363, 'median_return': 0.029166, 'mean_absolute_return': 0.032189, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.058396}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.053794, 'median_return': 0.059495, 'mean_absolute_return': 0.068012, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.121826}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.000328, 'median_return': 0.004815, 'mean_absolute_return': 0.013052, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.03592}, '5d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.00057, 'median_return': 0.002453, 'mean_absolute_return': 0.016282, 'max_adverse_excursion': -0.078114, 'max_favorable_excursion': 0.04835}, '10d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -5.3e-05, 'median_return': -0.006017, 'mean_absolute_return': 0.025327, 'max_adverse_excursion': -0.061742, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.016135, 'median_return': 0.020068, 'mean_absolute_return': 0.035733, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.086756}, '60d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.035955, 'median_return': 0.059104, 'mean_absolute_return': 0.077178, 'max_adverse_excursion': -0.15079, 'max_favorable_excursion': 0.21267}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6125}, '5d': {'sample_size': 80, 'hit_rate': 0.5625}, '10d': {'sample_size': 80, 'hit_rate': 0.3375}, '20d': {'sample_size': 80, 'hit_rate': 0.5125}, '60d': {'sample_size': 80, 'hit_rate': 0.6125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': 0.075, 'both_hit': 26, 'both_miss': 14}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': 0.05, 'both_hit': 23, 'both_miss': 17}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': -0.15, 'both_hit': 13, 'both_miss': 27}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': -0.2, 'both_hit': 29, 'both_miss': 11}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.05, 'both_hit': 31, 'both_miss': 9}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': -0.001194, 'median_return': 0.002067, 'mean_absolute_return': 0.013389, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.03592}, '5d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': -0.000571, 'median_return': 0.002453, 'mean_absolute_return': 0.016757, 'max_adverse_excursion': -0.078114, 'max_favorable_excursion': 0.04835}, '10d': {'sample_size': 80, 'hit_rate': 0.4375, 'avg_return': -0.000321, 'median_return': -0.006017, 'mean_absolute_return': 0.025046, 'max_adverse_excursion': -0.061742, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 80, 'hit_rate': 0.7375, 'avg_return': 0.016358, 'median_return': 0.020068, 'mean_absolute_return': 0.035379, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.086756}, '60d': {'sample_size': 80, 'hit_rate': 0.6625, 'avg_return': 0.037739, 'median_return': 0.059104, 'mean_absolute_return': 0.076262, 'max_adverse_excursion': -0.15079, 'max_favorable_excursion': 0.21267}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `-0.001492`, median `0.00234`, mae `0.013335`
- 5d: sample `60`, hit `0.5833`, avg `-0.001703`, median `0.002453`, mae `0.016432`
- 10d: sample `60`, hit `0.35`, avg `-0.004726`, median `-0.011432`, mae `0.02355`
- 20d: sample `60`, hit `0.6667`, avg `0.010797`, median `0.01983`, mae `0.035987`
- 60d: sample `60`, hit `0.6833`, avg `0.037956`, median `0.059104`, mae `0.07675`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.0003`, median `0.001122`, mae `0.013552`
- 5d: sample `20`, hit `0.5`, avg `0.002824`, median `0.002485`, mae `0.017734`
- 10d: sample `20`, hit `0.7`, avg `0.012895`, median `0.021815`, mae `0.029534`
- 20d: sample `20`, hit `0.95`, avg `0.03304`, median `0.041262`, mae `0.033553`
- 60d: sample `20`, hit `0.6`, avg `0.037086`, median `0.060145`, mae `0.074796`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `-0.001492`, median `0.00234`, mae `0.013335`
- 5d: sample `60`, hit `0.5833`, avg `-0.001703`, median `0.002453`, mae `0.016432`
- 10d: sample `60`, hit `0.35`, avg `-0.004726`, median `-0.011432`, mae `0.02355`
- 20d: sample `60`, hit `0.6667`, avg `0.010797`, median `0.01983`, mae `0.035987`
- 60d: sample `60`, hit `0.6833`, avg `0.037956`, median `0.059104`, mae `0.07675`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `-0.002057`, median `0.004487`, mae `0.015636`
- 5d: sample `40`, hit `0.575`, avg `-0.001984`, median `0.003005`, mae `0.019106`
- 10d: sample `40`, hit `0.325`, avg `-0.003033`, median `-0.011432`, mae `0.024207`
- 20d: sample `40`, hit `0.725`, avg `0.01684`, median `0.020068`, mae `0.036455`
- 60d: sample `40`, hit `0.775`, avg `0.052529`, median `0.092892`, mae `0.087718`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.0003`, median `0.001122`, mae `0.013552`
- 5d: sample `20`, hit `0.5`, avg `0.002824`, median `0.002485`, mae `0.017734`
- 10d: sample `20`, hit `0.7`, avg `0.012895`, median `0.021815`, mae `0.029534`
- 20d: sample `20`, hit `0.95`, avg `0.03304`, median `0.041262`, mae `0.033553`
- 60d: sample `20`, hit `0.6`, avg `0.037086`, median `0.060145`, mae `0.074796`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `-0.001492`, median `0.00234`, mae `0.013335`
- 5d: sample `60`, hit `0.5833`, avg `-0.001703`, median `0.002453`, mae `0.016432`
- 10d: sample `60`, hit `0.35`, avg `-0.004726`, median `-0.011432`, mae `0.02355`
- 20d: sample `60`, hit `0.6667`, avg `0.010797`, median `0.01983`, mae `0.035987`
- 60d: sample `60`, hit `0.6833`, avg `0.037956`, median `0.059104`, mae `0.07675`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `-0.002057`, median `0.004487`, mae `0.015636`
- 5d: sample `40`, hit `0.575`, avg `-0.001984`, median `0.003005`, mae `0.019106`
- 10d: sample `40`, hit `0.325`, avg `-0.003033`, median `-0.011432`, mae `0.024207`
- 20d: sample `40`, hit `0.725`, avg `0.01684`, median `0.020068`, mae `0.036455`
- 60d: sample `40`, hit `0.775`, avg `0.052529`, median `0.092892`, mae `0.087718`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.0003`, median `0.001122`, mae `0.013552`
- 5d: sample `20`, hit `0.5`, avg `0.002824`, median `0.002485`, mae `0.017734`
- 10d: sample `20`, hit `0.7`, avg `0.012895`, median `0.021815`, mae `0.029534`
- 20d: sample `20`, hit `0.95`, avg `0.03304`, median `0.041262`, mae `0.033553`
- 60d: sample `20`, hit `0.6`, avg `0.037086`, median `0.060145`, mae `0.074796`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `-0.002724`, median `0.001405`, mae `0.013234`
- 5d: sample `40`, hit `0.575`, avg `-0.004544`, median `0.001303`, mae `0.015105`
- 10d: sample `40`, hit `0.375`, avg `-0.005286`, median `-0.007117`, mae `0.021378`
- 20d: sample `40`, hit `0.625`, avg `0.005623`, median `0.01983`, mae `0.037534`
- 60d: sample `40`, hit `0.625`, avg `0.027148`, median `0.046132`, mae `0.066607`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `-0.001471`, median `0.003785`, mae `0.014941`
- 5d: sample `60`, hit `0.55`, avg `-0.000381`, median `0.002485`, mae `0.018649`
- 10d: sample `60`, hit `0.45`, avg `0.002276`, median `-0.003263`, mae `0.025983`
- 20d: sample `60`, hit `0.8`, avg `0.02224`, median `0.029166`, mae `0.035488`
- 60d: sample `60`, hit `0.7167`, avg `0.047381`, median `0.070559`, mae `0.083411`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `-0.002057`, median `0.004487`, mae `0.015636`
- 5d: sample `40`, hit `0.575`, avg `-0.001984`, median `0.003005`, mae `0.019106`
- 10d: sample `40`, hit `0.325`, avg `-0.003033`, median `-0.011432`, mae `0.024207`
- 20d: sample `40`, hit `0.725`, avg `0.01684`, median `0.020068`, mae `0.036455`
- 60d: sample `40`, hit `0.775`, avg `0.052529`, median `0.092892`, mae `0.087718`

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
