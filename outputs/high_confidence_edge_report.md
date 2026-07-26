# High Confidence Edge Report

Generated at: `2026-07-26T13:59:39.584999+00:00`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.001791`, median `0.004815`, mae `0.017442`
- 5d: sample `60`, hit `0.6333`, avg `0.006454`, median `0.006609`, mae `0.02004`
- 10d: sample `60`, hit `0.6833`, avg `0.012552`, median `0.017778`, mae `0.027429`
- 20d: sample `60`, hit `0.6833`, avg `0.026775`, median `0.02865`, mae `0.041694`
- 60d: sample `60`, hit `0.7833`, avg `0.050485`, median `0.059948`, mae `0.079392`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.3`, avg `-0.008325`, median `-0.01019`, mae `0.019864`
- 5d: sample `20`, hit `0.25`, avg `-0.01465`, median `-0.009549`, mae `0.029756`
- 10d: sample `20`, hit `0.6`, avg `0.000649`, median `0.021567`, mae `0.039602`
- 20d: sample `20`, hit `0.6`, avg `-0.003186`, median `0.021735`, mae `0.059862`
- 60d: sample `20`, hit `0.5`, avg `-0.017738`, median `0.027637`, mae `0.114166`

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
- 3d: sample `8`, hit `0.5`, avg `0.00231`, median `0.012272`, mae `0.016338`
- 5d: sample `8`, hit `0.875`, avg `0.011766`, median `0.021578`, mae `0.018329`
- 10d: sample `8`, hit `0.75`, avg `0.011279`, median `0.013069`, mae `0.019001`
- 20d: sample `8`, hit `0.875`, avg `0.034564`, median `0.043456`, mae `0.035742`
- 60d: sample `8`, hit `1.0`, avg `0.096074`, median `0.119272`, mae `0.096074`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.00231`, median `0.012272`, mae `0.016338`
- 5d: sample `8`, hit `0.875`, avg `0.011766`, median `0.021578`, mae `0.018329`
- 10d: sample `8`, hit `0.75`, avg `0.011279`, median `0.013069`, mae `0.019001`
- 20d: sample `8`, hit `0.875`, avg `0.034564`, median `0.043456`, mae `0.035742`
- 60d: sample `8`, hit `1.0`, avg `0.096074`, median `0.119272`, mae `0.096074`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.001791, 'median_return': 0.004815, 'mean_absolute_return': 0.017442, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.006454, 'median_return': 0.006609, 'mean_absolute_return': 0.02004, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.051324}, '10d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.012552, 'median_return': 0.017778, 'mean_absolute_return': 0.027429, 'max_adverse_excursion': -0.068474, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.026775, 'median_return': 0.02865, 'mean_absolute_return': 0.041694, 'max_adverse_excursion': -0.0919, 'max_favorable_excursion': 0.110689}, '60d': {'sample_size': 60, 'hit_rate': 0.7833, 'avg_return': 0.050485, 'median_return': 0.059948, 'mean_absolute_return': 0.079392, 'max_adverse_excursion': -0.177732, 'max_favorable_excursion': 0.19082}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.00231, 'median_return': 0.012272, 'mean_absolute_return': 0.016338, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.023651}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.011766, 'median_return': 0.021578, 'mean_absolute_return': 0.018329, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.027457}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.011279, 'median_return': 0.013069, 'mean_absolute_return': 0.019001, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.036071}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.034564, 'median_return': 0.043456, 'mean_absolute_return': 0.035742, 'max_adverse_excursion': -0.00471, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.096074, 'median_return': 0.119272, 'mean_absolute_return': 0.096074, 'max_adverse_excursion': 0.024156, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': -0.001077, 'median_return': 0.000766, 'mean_absolute_return': 0.018238, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': 1e-06, 'median_return': 0.000588, 'mean_absolute_return': 0.022929, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.009387, 'median_return': 0.01795, 'mean_absolute_return': 0.031747, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.017587, 'median_return': 0.021735, 'mean_absolute_return': 0.047402, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.026469, 'median_return': 0.057625, 'mean_absolute_return': 0.087198, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.19082}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5875}, '5d': {'sample_size': 80, 'hit_rate': 0.5875}, '10d': {'sample_size': 80, 'hit_rate': 0.4375}, '20d': {'sample_size': 80, 'hit_rate': 0.5125}, '60d': {'sample_size': 80, 'hit_rate': 0.5875}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.125, 'both_hit': 12, 'both_miss': 8}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': 0.075, 'both_hit': 14, 'both_miss': 6}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.225, 'both_hit': 14, 'both_miss': 6}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.125, 'both_hit': 16, 'both_miss': 4}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.05, 'both_hit': 19, 'both_miss': 1}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.001791, 'median_return': 0.004815, 'mean_absolute_return': 0.017442, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.006454, 'median_return': 0.006609, 'mean_absolute_return': 0.02004, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.051324}, '10d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.012552, 'median_return': 0.017778, 'mean_absolute_return': 0.027429, 'max_adverse_excursion': -0.068474, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.026775, 'median_return': 0.02865, 'mean_absolute_return': 0.041694, 'max_adverse_excursion': -0.0919, 'max_favorable_excursion': 0.110689}, '60d': {'sample_size': 60, 'hit_rate': 0.7833, 'avg_return': 0.050485, 'median_return': 0.059948, 'mean_absolute_return': 0.079392, 'max_adverse_excursion': -0.177732, 'max_favorable_excursion': 0.19082}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.008325, 'median_return': -0.01019, 'mean_absolute_return': 0.019864, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 20, 'hit_rate': 0.25, 'avg_return': -0.01465, 'median_return': -0.009549, 'mean_absolute_return': 0.029756, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.000649, 'median_return': 0.021567, 'mean_absolute_return': 0.039602, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.003186, 'median_return': 0.021735, 'mean_absolute_return': 0.059862, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.017738, 'median_return': 0.027637, 'mean_absolute_return': 0.114166, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.129489}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.001724`, median `0.002957`, mae `0.014111`
- 5d: sample `40`, hit `0.625`, avg `0.004765`, median `0.006452`, mae `0.017709`
- 10d: sample `40`, hit `0.6`, avg `0.006258`, median `0.005691`, mae `0.022204`
- 20d: sample `40`, hit `0.675`, avg `0.021629`, median `0.02086`, mae `0.034772`
- 60d: sample `40`, hit `0.8`, avg `0.055691`, median `0.059104`, mae `0.069828`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.003201`, median `-0.001058`, mae `0.021984`
- 5d: sample `40`, hit `0.45`, avg `-0.002409`, median `-0.001129`, mae `0.027229`
- 10d: sample `40`, hit `0.725`, avg `0.012896`, median `0.027869`, mae `0.038741`
- 20d: sample `40`, hit `0.65`, avg `0.01694`, median `0.035693`, mae `0.0577`
- 60d: sample `40`, hit `0.625`, avg `0.011168`, median `0.068712`, mae `0.106343`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.001724`, median `0.002957`, mae `0.014111`
- 5d: sample `40`, hit `0.625`, avg `0.004765`, median `0.006452`, mae `0.017709`
- 10d: sample `40`, hit `0.6`, avg `0.006258`, median `0.005691`, mae `0.022204`
- 20d: sample `40`, hit `0.675`, avg `0.021629`, median `0.02086`, mae `0.034772`
- 60d: sample `40`, hit `0.8`, avg `0.055691`, median `0.059104`, mae `0.069828`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.001724`, median `0.002957`, mae `0.014111`
- 5d: sample `40`, hit `0.625`, avg `0.004765`, median `0.006452`, mae `0.017709`
- 10d: sample `40`, hit `0.6`, avg `0.006258`, median `0.005691`, mae `0.022204`
- 20d: sample `40`, hit `0.675`, avg `0.021629`, median `0.02086`, mae `0.034772`
- 60d: sample `40`, hit `0.8`, avg `0.055691`, median `0.059104`, mae `0.069828`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.001924`, median `0.009701`, mae `0.024105`
- 5d: sample `20`, hit `0.65`, avg `0.009831`, median `0.011927`, mae `0.024702`
- 10d: sample `20`, hit `0.85`, avg `0.025142`, median `0.031521`, mae `0.03788`
- 20d: sample `20`, hit `0.7`, avg `0.037066`, median `0.059014`, mae `0.055538`
- 60d: sample `20`, hit `0.75`, avg `0.040074`, median `0.072268`, mae `0.09852`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.001724`, median `0.002957`, mae `0.014111`
- 5d: sample `40`, hit `0.625`, avg `0.004765`, median `0.006452`, mae `0.017709`
- 10d: sample `40`, hit `0.6`, avg `0.006258`, median `0.005691`, mae `0.022204`
- 20d: sample `40`, hit `0.675`, avg `0.021629`, median `0.02086`, mae `0.034772`
- 60d: sample `40`, hit `0.8`, avg `0.055691`, median `0.059104`, mae `0.069828`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.001724`, median `0.002957`, mae `0.014111`
- 5d: sample `40`, hit `0.625`, avg `0.004765`, median `0.006452`, mae `0.017709`
- 10d: sample `40`, hit `0.6`, avg `0.006258`, median `0.005691`, mae `0.022204`
- 20d: sample `40`, hit `0.675`, avg `0.021629`, median `0.02086`, mae `0.034772`
- 60d: sample `40`, hit `0.8`, avg `0.055691`, median `0.059104`, mae `0.069828`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.003201`, median `-0.001058`, mae `0.021984`
- 5d: sample `40`, hit `0.45`, avg `-0.002409`, median `-0.001129`, mae `0.027229`
- 10d: sample `40`, hit `0.725`, avg `0.012896`, median `0.027869`, mae `0.038741`
- 20d: sample `40`, hit `0.65`, avg `0.01694`, median `0.035693`, mae `0.0577`
- 60d: sample `40`, hit `0.625`, avg `0.011168`, median `0.068712`, mae `0.106343`

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
- 3d: sample `80`, hit `0.5375`, avg `-0.000738`, median `0.000766`, mae `0.018048`
- 5d: sample `80`, hit `0.5375`, avg `0.001178`, median `0.001303`, mae `0.022469`
- 10d: sample `80`, hit `0.6625`, avg `0.009577`, median `0.017778`, mae `0.030472`
- 20d: sample `80`, hit `0.6625`, avg `0.019284`, median `0.021735`, mae `0.046236`
- 60d: sample `80`, hit `0.7125`, avg `0.033429`, median `0.059104`, mae `0.088086`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.001724`, median `0.002957`, mae `0.014111`
- 5d: sample `40`, hit `0.625`, avg `0.004765`, median `0.006452`, mae `0.017709`
- 10d: sample `40`, hit `0.6`, avg `0.006258`, median `0.005691`, mae `0.022204`
- 20d: sample `40`, hit `0.675`, avg `0.021629`, median `0.02086`, mae `0.034772`
- 60d: sample `40`, hit `0.8`, avg `0.055691`, median `0.059104`, mae `0.069828`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.001924`, median `0.009701`, mae `0.024105`
- 5d: sample `20`, hit `0.65`, avg `0.009831`, median `0.011927`, mae `0.024702`
- 10d: sample `20`, hit `0.85`, avg `0.025142`, median `0.031521`, mae `0.03788`
- 20d: sample `20`, hit `0.7`, avg `0.037066`, median `0.059014`, mae `0.055538`
- 60d: sample `20`, hit `0.75`, avg `0.040074`, median `0.072268`, mae `0.09852`

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
