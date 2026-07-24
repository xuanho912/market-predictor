# Forecast Learning Queue

Generated at: `2026-07-24T14:15:41.274010+00:00`

This report turns forecast deviations into safe challenger-model hypotheses. It does not alter baseline_v1.

## Status

- active_model: `baseline_v1`
- global_learning_status: `shadow_challenger_queue_ready`
- evidence_level: `stronger_evidence`
- completed_outcomes_reviewed: `424`
- material_deviation_count: `187`
- dominant_error_theme: `news_data_gap_limited_attribution`
- trust_gate_status: `RESEARCH_ONLY_FORWARD_VALIDATION_NEEDED`

## Candidate Challengers

### event_reaction_overlay

- proposed_model_version: `challenger_v2_event_reaction_overlay`
- priority_score: `100`
- readiness: `ready_for_shadow_challenger`
- evidence_count: `354`
- hypothesis: 重大新闻只有在价格、VIX、信用或期货反应确认后，才应该提高短线情景权重；未确认新闻应快速衰减。
- expected_improvement: 减少新闻驱动日对 1d/3d/5d 主路径的低估或误判。
- required_validation: 至少 20 个已完成 1d/3d/5d 样本，并且 challenger 的主路径误差低于 baseline_v1。
- allowed_action: Run as shadow challenger and compare against baseline_v1 after future outcomes complete.
- forbidden_action: Do not alter baseline_v1, Alpha v1 threshold, historical forecasts, or displayed probabilities based on this queue alone.

### price_structure_confirmation_overlay

- proposed_model_version: `challenger_v2_price_structure_confirmation_overlay`
- priority_score: `100`
- readiness: `ready_for_shadow_challenger`
- evidence_count: `187`
- hypothesis: 当价格结构确认或否定主路径时，情景排序应更快反映确认价、失效价和风险接管价。
- expected_improvement: 减少路径已经被价格确认/否定但模型仍滞后的错误。
- required_validation: 主路径确认价后的样本必须比未确认样本有更高 primary hit rate。
- allowed_action: Run as shadow challenger and compare against baseline_v1 after future outcomes complete.
- forbidden_action: Do not alter baseline_v1, Alpha v1 threshold, historical forecasts, or displayed probabilities based on this queue alone.

### breadth_follow_through_overlay

- proposed_model_version: `challenger_v2_breadth_follow_through_overlay`
- priority_score: `100`
- readiness: `ready_for_shadow_challenger`
- evidence_count: `45`
- hypothesis: 指数反弹但内部参与不足时应提高失败反抽风险；内部共振连续改善时才提高趋势修复权重。
- expected_improvement: 降低只看指数表面导致的误判，改善 5d/10d/20d 路径排序。
- required_validation: breadth confirmed 样本必须优于 breadth conflicted 样本，并且 primary-vs-secondary spread 为正。
- allowed_action: Run as shadow challenger and compare against baseline_v1 after future outcomes complete.
- forbidden_action: Do not alter baseline_v1, Alpha v1 threshold, historical forecasts, or displayed probabilities based on this queue alone.

### flow_positioning_overlay

- proposed_model_version: `challenger_v2_flow_positioning_overlay`
- priority_score: `100`
- readiness: `ready_for_shadow_challenger`
- evidence_count: `28`
- hypothesis: 成交量、风险偏好资产轮动、HYG/LQD、TLT/UUP 同向时，应影响短线弹性和风险路径权重。
- expected_improvement: 提高次日到 5d 的路径方向和波动区间判断。
- required_validation: flow confirmed 高分样本必须在 1d/3d/5d 路径误差上优于普通样本。
- allowed_action: Run as shadow challenger and compare against baseline_v1 after future outcomes complete.
- forbidden_action: Do not alter baseline_v1, Alpha v1 threshold, historical forecasts, or displayed probabilities based on this queue alone.

### volatility_repair_overlay

- proposed_model_version: `challenger_v2_volatility_repair_overlay`
- priority_score: `100`
- readiness: `ready_for_shadow_challenger`
- evidence_count: `18`
- hypothesis: VIX term、VVIX、SKEW 的修复或恶化应更明确地区分反抽、失败反抽和风险扩散。
- expected_improvement: 提高恐慌释放后反抽路径，以及波动率重新恶化时风险路径的识别质量。
- required_validation: 至少 20 个 3d/5d 样本和 30 个 10d 样本证明路径排序优于 baseline_v1。
- allowed_action: Run as shadow challenger and compare against baseline_v1 after future outcomes complete.
- forbidden_action: Do not alter baseline_v1, Alpha v1 threshold, historical forecasts, or displayed probabilities based on this queue alone.

## Confidence Policy

- cap_displayed_confidence_until_validated: `True`
- reason: `Forward sample and high-confidence validation are insufficient.`
- high_confidence_question: `insufficient_samples_for_high_confidence_validation`
- trust_gate_status: `RESEARCH_ONLY_FORWARD_VALIDATION_NEEDED`

## Blocked Reasons

- `insufficient_forward_samples`: Forward validation samples are not enough to rely on the model as a high-confidence forecasting system.
- `primary_path_not_validated`: Primary-vs-secondary path advantage is not yet proven on enough forward samples.

## Next Best Actions

- 优先把 `event_reaction_overlay` 做成 shadow challenger：`challenger_v2_event_reaction_overlay`。
- 让 challenger 与 baseline_v1 同时预测，未来用真实结果比较主路径命中率、路径误差和高置信样本表现。
- 只有 forward validation 多数指标胜过 baseline_v1 后，才允许进入 promotion_candidate。

## Guardrails

- This queue does not change baseline_v1 or Alpha v1.
- Every learning item must become a challenger/shadow model before it can affect the active model.
- Historical replay may prioritize a challenger, but forward validation is required for promotion.
- No trading, PnL, buy/sell, entry or exit language is used.
