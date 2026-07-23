# High Confidence Edge Report

Generated at: `2026-07-23T00:12:29.644524+00:00`

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
- 3d: sample `20`, hit `0.4`, avg `-0.009316`, median `-0.009383`, mae `0.021831`
- 5d: sample `20`, hit `0.45`, avg `-0.011233`, median `-0.004438`, mae `0.023307`
- 10d: sample `20`, hit `0.35`, avg `-0.00227`, median `-0.007011`, mae `0.019173`
- 20d: sample `20`, hit `0.7`, avg `0.01574`, median `0.021759`, mae `0.040062`
- 60d: sample `20`, hit `0.75`, avg `0.042203`, median `0.059131`, mae `0.07353`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.4667`, avg `-0.004128`, median `-0.001428`, mae `0.013608`
- 5d: sample `60`, hit `0.4167`, avg `-0.005663`, median `-0.005958`, mae `0.016188`
- 10d: sample `60`, hit `0.4667`, avg `-0.003598`, median `-0.006957`, mae `0.026261`
- 20d: sample `60`, hit `0.6167`, avg `0.00048`, median `0.015416`, mae `0.042044`
- 60d: sample `60`, hit `0.5`, avg `-0.007845`, median `0.00483`, mae `0.080932`

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
- 3d: sample `8`, hit `0.375`, avg `-0.020804`, median `-0.030499`, mae `0.024014`
- 5d: sample `8`, hit `0.25`, avg `-0.028823`, median `-0.026253`, mae `0.030532`
- 10d: sample `8`, hit `0.125`, avg `-0.016415`, median `-0.01796`, mae `0.021223`
- 20d: sample `8`, hit `0.625`, avg `-0.00875`, median `0.020068`, mae `0.040476`
- 60d: sample `8`, hit `0.625`, avg `0.011496`, median `0.046132`, mae `0.068214`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.020804`, median `-0.030499`, mae `0.024014`
- 5d: sample `8`, hit `0.25`, avg `-0.028823`, median `-0.026253`, mae `0.030532`
- 10d: sample `8`, hit `0.125`, avg `-0.016415`, median `-0.01796`, mae `0.021223`
- 20d: sample `8`, hit `0.625`, avg `-0.00875`, median `0.020068`, mae `0.040476`
- 60d: sample `8`, hit `0.625`, avg `0.011496`, median `0.046132`, mae `0.068214`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.009316, 'median_return': -0.009383, 'mean_absolute_return': 0.021831, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.029522}, '5d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.011233, 'median_return': -0.004438, 'mean_absolute_return': 0.023307, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.046339}, '10d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.00227, 'median_return': -0.007011, 'mean_absolute_return': 0.019173, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.043492}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.01574, 'median_return': 0.021759, 'mean_absolute_return': 0.040062, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.086905}, '60d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.042203, 'median_return': 0.059131, 'mean_absolute_return': 0.07353, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.020804, 'median_return': -0.030499, 'mean_absolute_return': 0.024014, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.006714}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.028823, 'median_return': -0.026253, 'mean_absolute_return': 0.030532, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.003829}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.016415, 'median_return': -0.01796, 'mean_absolute_return': 0.021223, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.019233}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.00875, 'median_return': 0.020068, 'mean_absolute_return': 0.040476, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.043456}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.011496, 'median_return': 0.046132, 'mean_absolute_return': 0.068214, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.101282}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': -0.003716, 'median_return': -0.001658, 'mean_absolute_return': 0.014736, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.03592}, '5d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.004637, 'median_return': -0.004438, 'mean_absolute_return': 0.016572, 'max_adverse_excursion': -0.056697, 'max_favorable_excursion': 0.046339}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.001805, 'median_return': -0.00367, 'mean_absolute_return': 0.024852, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.058931}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.005744, 'median_return': 0.017237, 'mean_absolute_return': 0.041668, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.086905}, '60d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.003908, 'median_return': 0.024156, 'mean_absolute_return': 0.080289, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.144029}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.55}, '10d': {'sample_size': 80, 'hit_rate': 0.4875}, '20d': {'sample_size': 80, 'hit_rate': 0.4625}, '60d': {'sample_size': 80, 'hit_rate': 0.5625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.125, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.006369, 'median_return': -0.002441, 'mean_absolute_return': 0.017693, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.03592}, '5d': {'sample_size': 60, 'hit_rate': 0.4333, 'avg_return': -0.007486, 'median_return': -0.006464, 'mean_absolute_return': 0.019326, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.046339}, '10d': {'sample_size': 60, 'hit_rate': 0.4333, 'avg_return': -0.000323, 'median_return': -0.006957, 'mean_absolute_return': 0.022404, 'max_adverse_excursion': -0.043454, 'max_favorable_excursion': 0.058931}, '20d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.011528, 'median_return': 0.01983, 'mean_absolute_return': 0.035843, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.086905}, '60d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.021655, 'median_return': 0.037425, 'mean_absolute_return': 0.067283, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.002594, 'median_return': -0.0002, 'mean_absolute_return': 0.009575, 'max_adverse_excursion': -0.025004, 'max_favorable_excursion': 0.01687}, '5d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.005762, 'median_return': -0.000413, 'mean_absolute_return': 0.013891, 'max_adverse_excursion': -0.056697, 'max_favorable_excursion': 0.022754}, '10d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.012097, 'median_return': -0.0113, 'mean_absolute_return': 0.030746, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.050509}, '20d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.017404, 'median_return': 0.007748, 'mean_absolute_return': 0.058665, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.072047}, '60d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.046297, 'median_return': -0.00384, 'mean_absolute_return': 0.11448, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.118924}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.008526`, median `-0.008307`, mae `0.017421`
- 5d: sample `40`, hit `0.45`, avg `-0.010221`, median `-0.004438`, mae `0.019266`
- 10d: sample `40`, hit `0.325`, avg `-0.006788`, median `-0.009882`, mae `0.020525`
- 20d: sample `40`, hit `0.575`, avg `0.004351`, median `0.016745`, mae `0.036526`
- 60d: sample `40`, hit `0.625`, avg `0.025584`, median `0.037425`, mae `0.060593`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.002054`, median `0.006513`, mae `0.018236`
- 5d: sample `20`, hit `0.4`, avg `-0.002018`, median `-0.007381`, mae `0.019446`
- 10d: sample `20`, hit `0.65`, avg `0.012609`, median `0.01795`, mae `0.026162`
- 20d: sample `20`, hit `0.9`, avg `0.025881`, median `0.03392`, mae `0.034477`
- 60d: sample `20`, hit `0.6`, avg `0.013798`, median `0.043615`, mae `0.080662`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.009316`, median `-0.009383`, mae `0.021831`
- 5d: sample `20`, hit `0.45`, avg `-0.011233`, median `-0.004438`, mae `0.023307`
- 10d: sample `20`, hit `0.35`, avg `-0.00227`, median `-0.007011`, mae `0.019173`
- 20d: sample `20`, hit `0.7`, avg `0.01574`, median `0.021759`, mae `0.040062`
- 60d: sample `20`, hit `0.75`, avg `0.042203`, median `0.059131`, mae `0.07353`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.009316`, median `-0.009383`, mae `0.021831`
- 5d: sample `20`, hit `0.45`, avg `-0.011233`, median `-0.004438`, mae `0.023307`
- 10d: sample `20`, hit `0.35`, avg `-0.00227`, median `-0.007011`, mae `0.019173`
- 20d: sample `20`, hit `0.7`, avg `0.01574`, median `0.021759`, mae `0.040062`
- 60d: sample `20`, hit `0.75`, avg `0.042203`, median `0.059131`, mae `0.07353`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.002054`, median `0.006513`, mae `0.018236`
- 5d: sample `20`, hit `0.4`, avg `-0.002018`, median `-0.007381`, mae `0.019446`
- 10d: sample `20`, hit `0.65`, avg `0.012609`, median `0.01795`, mae `0.026162`
- 20d: sample `20`, hit `0.9`, avg `0.025881`, median `0.03392`, mae `0.034477`
- 60d: sample `20`, hit `0.6`, avg `0.013798`, median `0.043615`, mae `0.080662`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.009316`, median `-0.009383`, mae `0.021831`
- 5d: sample `20`, hit `0.45`, avg `-0.011233`, median `-0.004438`, mae `0.023307`
- 10d: sample `20`, hit `0.35`, avg `-0.00227`, median `-0.007011`, mae `0.019173`
- 20d: sample `20`, hit `0.7`, avg `0.01574`, median `0.021759`, mae `0.040062`
- 60d: sample `20`, hit `0.75`, avg `0.042203`, median `0.059131`, mae `0.07353`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.009316`, median `-0.009383`, mae `0.021831`
- 5d: sample `20`, hit `0.45`, avg `-0.011233`, median `-0.004438`, mae `0.023307`
- 10d: sample `20`, hit `0.35`, avg `-0.00227`, median `-0.007011`, mae `0.019173`
- 20d: sample `20`, hit `0.7`, avg `0.01574`, median `0.021759`, mae `0.040062`
- 60d: sample `20`, hit `0.75`, avg `0.042203`, median `0.059131`, mae `0.07353`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.002054`, median `0.006513`, mae `0.018236`
- 5d: sample `20`, hit `0.4`, avg `-0.002018`, median `-0.007381`, mae `0.019446`
- 10d: sample `20`, hit `0.65`, avg `0.012609`, median `0.01795`, mae `0.026162`
- 20d: sample `20`, hit `0.9`, avg `0.025881`, median `0.03392`, mae `0.034477`
- 60d: sample `20`, hit `0.6`, avg `0.013798`, median `0.043615`, mae `0.080662`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.45`, avg `-0.005425`, median `-0.002441`, mae `0.015663`
- 5d: sample `80`, hit `0.425`, avg `-0.007055`, median `-0.005958`, mae `0.017968`
- 10d: sample `80`, hit `0.4375`, avg `-0.003266`, median `-0.007011`, mae `0.024489`
- 20d: sample `80`, hit `0.6375`, avg `0.004295`, median `0.017237`, mae `0.041548`
- 60d: sample `80`, hit `0.5625`, avg `0.004667`, median `0.024156`, mae `0.079082`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.009316`, median `-0.009383`, mae `0.021831`
- 5d: sample `20`, hit `0.45`, avg `-0.011233`, median `-0.004438`, mae `0.023307`
- 10d: sample `20`, hit `0.35`, avg `-0.00227`, median `-0.007011`, mae `0.019173`
- 20d: sample `20`, hit `0.7`, avg `0.01574`, median `0.021759`, mae `0.040062`
- 60d: sample `20`, hit `0.75`, avg `0.042203`, median `0.059131`, mae `0.07353`

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
