# High Confidence Edge Report

Generated at: `2026-08-12T21:12:00.405336+00:00`

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
- 3d: sample `40`, hit `0.65`, avg `0.00439`, median `0.006714`, mae `0.014591`
- 5d: sample `40`, hit `0.65`, avg `0.005036`, median `0.005523`, mae `0.015757`
- 10d: sample `40`, hit `0.65`, avg `0.009898`, median `0.011426`, mae `0.023824`
- 20d: sample `40`, hit `0.7`, avg `0.014678`, median `0.022652`, mae `0.042529`
- 60d: sample `40`, hit `0.6`, avg `0.022538`, median `0.046132`, mae `0.080273`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.001474`, median `0.002101`, mae `0.012654`
- 5d: sample `40`, hit `0.725`, avg `0.002571`, median `0.004787`, mae `0.01746`
- 10d: sample `40`, hit `0.575`, avg `0.0051`, median `0.006604`, mae `0.022943`
- 20d: sample `40`, hit `0.65`, avg `0.011211`, median `0.012117`, mae `0.033778`
- 60d: sample `40`, hit `0.55`, avg `0.017045`, median `0.018072`, mae `0.059666`

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
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.001218`, median `0.009229`, mae `0.01332`
- 5d: sample `8`, hit `0.625`, avg `0.000746`, median `0.005319`, mae `0.011913`
- 10d: sample `8`, hit `0.75`, avg `0.006792`, median `0.011426`, mae `0.015564`
- 20d: sample `8`, hit `0.75`, avg `0.019195`, median `0.024743`, mae `0.024874`
- 60d: sample `8`, hit `0.5`, avg `0.01915`, median `0.046132`, mae `0.056168`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.001218`, median `0.009229`, mae `0.01332`
- 5d: sample `8`, hit `0.625`, avg `0.000746`, median `0.005319`, mae `0.011913`
- 10d: sample `8`, hit `0.75`, avg `0.006792`, median `0.011426`, mae `0.015564`
- 20d: sample `8`, hit `0.75`, avg `0.019195`, median `0.024743`, mae `0.024874`
- 60d: sample `8`, hit `0.5`, avg `0.01915`, median `0.046132`, mae `0.056168`

### confidence validation
- `{'strong_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.00439, 'median_return': 0.006714, 'mean_absolute_return': 0.014591, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.005036, 'median_return': 0.005523, 'mean_absolute_return': 0.015757, 'max_adverse_excursion': -0.040484, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.009898, 'median_return': 0.011426, 'mean_absolute_return': 0.023824, 'max_adverse_excursion': -0.059371, 'max_favorable_excursion': 0.063488}, '20d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.014678, 'median_return': 0.022652, 'mean_absolute_return': 0.042529, 'max_adverse_excursion': -0.095545, 'max_favorable_excursion': 0.107803}, '60d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.022538, 'median_return': 0.046132, 'mean_absolute_return': 0.080273, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.322945}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.001474, 'median_return': 0.002101, 'mean_absolute_return': 0.012654, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.002571, 'median_return': 0.004787, 'mean_absolute_return': 0.01746, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.0051, 'median_return': 0.006604, 'mean_absolute_return': 0.022943, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.011211, 'median_return': 0.012117, 'mean_absolute_return': 0.033778, 'max_adverse_excursion': -0.136294, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.017045, 'median_return': 0.018072, 'mean_absolute_return': 0.059666, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.001218, 'median_return': 0.009229, 'mean_absolute_return': 0.01332, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.000746, 'median_return': 0.005319, 'mean_absolute_return': 0.011913, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.006792, 'median_return': 0.011426, 'mean_absolute_return': 0.015564, 'max_adverse_excursion': -0.01796, 'max_favorable_excursion': 0.025531}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.019195, 'median_return': 0.024743, 'mean_absolute_return': 0.024874, 'max_adverse_excursion': -0.015135, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.01915, 'median_return': 0.046132, 'mean_absolute_return': 0.056168, 'max_adverse_excursion': -0.045404, 'max_favorable_excursion': 0.087104}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.003122, 'median_return': 0.004542, 'mean_absolute_return': 0.013656, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.004143, 'median_return': 0.005084, 'mean_absolute_return': 0.01713, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.007578, 'median_return': 0.007952, 'mean_absolute_return': 0.024252, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.01225, 'median_return': 0.012291, 'mean_absolute_return': 0.039629, 'max_adverse_excursion': -0.136294, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.019863, 'median_return': 0.026715, 'mean_absolute_return': 0.071504, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.322945}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6125}, '5d': {'sample_size': 80, 'hit_rate': 0.6875}, '10d': {'sample_size': 80, 'hit_rate': 0.6125}, '20d': {'sample_size': 80, 'hit_rate': 0.675}, '60d': {'sample_size': 80, 'hit_rate': 0.575}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.0, 'both_hit': 49, 'both_miss': 31}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': 0.0, 'both_hit': 55, 'both_miss': 25}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.0, 'both_hit': 49, 'both_miss': 31}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': 0.0, 'both_hit': 54, 'both_miss': 26}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': 0.0, 'both_hit': 46, 'both_miss': 34}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.00662, 'median_return': 0.007802, 'mean_absolute_return': 0.014942, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.003496, 'median_return': 0.006133, 'mean_absolute_return': 0.020645, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.011022, 'median_return': 0.0106, 'mean_absolute_return': 0.029095, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.016, 'median_return': 0.012153, 'mean_absolute_return': 0.045198, 'max_adverse_excursion': -0.136294, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.037671, 'median_return': 0.045044, 'mean_absolute_return': 0.080058, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.322945}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.000756, 'median_return': 0.000201, 'mean_absolute_return': 0.012303, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.00411, 'median_return': 0.004606, 'mean_absolute_return': 0.012572, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.003976, 'median_return': 0.004187, 'mean_absolute_return': 0.017672, 'max_adverse_excursion': -0.059371, 'max_favorable_excursion': 0.050746}, '20d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.009889, 'median_return': 0.019193, 'mean_absolute_return': 0.031109, 'max_adverse_excursion': -0.095545, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': 0.001912, 'median_return': -0.004982, 'mean_absolute_return': 0.059882, 'max_adverse_excursion': -0.1263, 'max_favorable_excursion': 0.102896}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.002335`, median `0.004004`, mae `0.012417`
- 5d: sample `60`, hit `0.7`, avg `0.004677`, median `0.005319`, mae `0.013809`
- 10d: sample `60`, hit `0.6167`, avg `0.007783`, median `0.00903`, mae `0.020068`
- 20d: sample `60`, hit `0.6833`, avg `0.011231`, median `0.019193`, mae `0.035245`
- 60d: sample `60`, hit `0.5167`, avg `0.010639`, median `0.018072`, mae `0.071243`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.004722`, median `0.009966`, mae `0.01724`
- 5d: sample `20`, hit `0.65`, avg `0.001184`, median `0.004787`, mae `0.025007`
- 10d: sample `20`, hit `0.6`, avg `0.006646`, median `0.007952`, mae `0.033329`
- 20d: sample `20`, hit `0.65`, avg `0.018086`, median `0.012117`, mae `0.046879`
- 60d: sample `20`, hit `0.75`, avg `0.047247`, median `0.02999`, mae `0.066152`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.002335`, median `0.004004`, mae `0.012417`
- 5d: sample `60`, hit `0.7`, avg `0.004677`, median `0.005319`, mae `0.013809`
- 10d: sample `60`, hit `0.6167`, avg `0.007783`, median `0.00903`, mae `0.020068`
- 20d: sample `60`, hit `0.6833`, avg `0.011231`, median `0.019193`, mae `0.035245`
- 60d: sample `60`, hit `0.5167`, avg `0.010639`, median `0.018072`, mae `0.071243`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.004722`, median `0.009966`, mae `0.01724`
- 5d: sample `20`, hit `0.65`, avg `0.001184`, median `0.004787`, mae `0.025007`
- 10d: sample `20`, hit `0.6`, avg `0.006646`, median `0.007952`, mae `0.033329`
- 20d: sample `20`, hit `0.65`, avg `0.018086`, median `0.012117`, mae `0.046879`
- 60d: sample `20`, hit `0.75`, avg `0.047247`, median `0.02999`, mae `0.066152`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.002335`, median `0.004004`, mae `0.012417`
- 5d: sample `60`, hit `0.7`, avg `0.004677`, median `0.005319`, mae `0.013809`
- 10d: sample `60`, hit `0.6167`, avg `0.007783`, median `0.00903`, mae `0.020068`
- 20d: sample `60`, hit `0.6833`, avg `0.011231`, median `0.019193`, mae `0.035245`
- 60d: sample `60`, hit `0.5167`, avg `0.010639`, median `0.018072`, mae `0.071243`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.004722`, median `0.009966`, mae `0.01724`
- 5d: sample `20`, hit `0.65`, avg `0.001184`, median `0.004787`, mae `0.025007`
- 10d: sample `20`, hit `0.6`, avg `0.006646`, median `0.007952`, mae `0.033329`
- 20d: sample `20`, hit `0.65`, avg `0.018086`, median `0.012117`, mae `0.046879`
- 60d: sample `20`, hit `0.75`, avg `0.047247`, median `0.02999`, mae `0.066152`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.001775`, median `0.000145`, mae `0.008069`
- 5d: sample `20`, hit `0.8`, avg `0.003958`, median `0.005084`, mae `0.009913`
- 10d: sample `20`, hit `0.55`, avg `0.003554`, median `0.003491`, mae `0.012557`
- 20d: sample `20`, hit `0.65`, avg `0.004336`, median `0.012291`, mae `0.020677`
- 60d: sample `20`, hit `0.35`, avg `-0.013157`, median `-0.018455`, mae `0.053181`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.000262`, median `0.006714`, mae `0.016538`
- 5d: sample `20`, hit `0.6`, avg `0.004262`, median `0.004014`, mae `0.015231`
- 10d: sample `20`, hit `0.6`, avg `0.004399`, median `0.010691`, mae `0.022786`
- 20d: sample `20`, hit `0.75`, avg `0.015441`, median `0.024743`, mae `0.041541`
- 60d: sample `20`, hit `0.55`, avg `0.016981`, median `0.030553`, mae `0.066582`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.004722`, median `0.009966`, mae `0.01724`
- 5d: sample `20`, hit `0.65`, avg `0.001184`, median `0.004787`, mae `0.025007`
- 10d: sample `20`, hit `0.6`, avg `0.006646`, median `0.007952`, mae `0.033329`
- 20d: sample `20`, hit `0.65`, avg `0.018086`, median `0.012117`, mae `0.046879`
- 60d: sample `20`, hit `0.75`, avg `0.047247`, median `0.02999`, mae `0.066152`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.001775`, median `0.000145`, mae `0.008069`
- 5d: sample `20`, hit `0.8`, avg `0.003958`, median `0.005084`, mae `0.009913`
- 10d: sample `20`, hit `0.55`, avg `0.003554`, median `0.003491`, mae `0.012557`
- 20d: sample `20`, hit `0.65`, avg `0.004336`, median `0.012291`, mae `0.020677`
- 60d: sample `20`, hit `0.35`, avg `-0.013157`, median `-0.018455`, mae `0.053181`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.004722`, median `0.009966`, mae `0.01724`
- 5d: sample `20`, hit `0.65`, avg `0.001184`, median `0.004787`, mae `0.025007`
- 10d: sample `20`, hit `0.6`, avg `0.006646`, median `0.007952`, mae `0.033329`
- 20d: sample `20`, hit `0.65`, avg `0.018086`, median `0.012117`, mae `0.046879`
- 60d: sample `20`, hit `0.75`, avg `0.047247`, median `0.02999`, mae `0.066152`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.002932`, median `0.004542`, mae `0.013623`
- 5d: sample `80`, hit `0.6875`, avg `0.003803`, median `0.005084`, mae `0.016609`
- 10d: sample `80`, hit `0.6125`, avg `0.007499`, median `0.007952`, mae `0.023383`
- 20d: sample `80`, hit `0.675`, avg `0.012945`, median `0.013156`, mae `0.038153`
- 60d: sample `80`, hit `0.575`, avg `0.019791`, median `0.026715`, mae `0.06997`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.002932`, median `0.004542`, mae `0.013623`
- 5d: sample `80`, hit `0.6875`, avg `0.003803`, median `0.005084`, mae `0.016609`
- 10d: sample `80`, hit `0.6125`, avg `0.007499`, median `0.007952`, mae `0.023383`
- 20d: sample `80`, hit `0.675`, avg `0.012945`, median `0.013156`, mae `0.038153`
- 60d: sample `80`, hit `0.575`, avg `0.019791`, median `0.026715`, mae `0.06997`

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
