from __future__ import annotations

import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]


DRIVER_GROUPS: dict[str, dict[str, Any]] = {
    "event_reaction_overlay": {
        "proposed_model_version": "challenger_v2_event_reaction_overlay",
        "drivers": (
            "news_event_driver_underweighted",
            "news_event_risk_underweighted",
            "risk_off_news_overweighted_or_resolved",
            "news_data_gap_limited_attribution",
        ),
        "hypothesis": "重大新闻只有在价格、VIX、信用或期货反应确认后，才应该提高短线情景权重；未确认新闻应快速衰减。",
        "expected_improvement": "减少新闻驱动日对 1d/3d/5d 主路径的低估或误判。",
        "required_validation": "至少 20 个已完成 1d/3d/5d 样本，并且 challenger 的主路径误差低于 baseline_v1。",
    },
    "volatility_repair_overlay": {
        "proposed_model_version": "challenger_v2_volatility_repair_overlay",
        "drivers": (
            "volatility_repair_underweighted",
            "volatility_or_tail_risk_underweighted",
        ),
        "hypothesis": "VIX term、VVIX、SKEW 的修复或恶化应更明确地区分反抽、失败反抽和风险扩散。",
        "expected_improvement": "提高恐慌释放后反抽路径，以及波动率重新恶化时风险路径的识别质量。",
        "required_validation": "至少 20 个 3d/5d 样本和 30 个 10d 样本证明路径排序优于 baseline_v1。",
    },
    "breadth_follow_through_overlay": {
        "proposed_model_version": "challenger_v2_breadth_follow_through_overlay",
        "drivers": (
            "breadth_follow_through_underweighted",
            "breadth_conflict_underweighted",
        ),
        "hypothesis": "指数反弹但内部参与不足时应提高失败反抽风险；内部共振连续改善时才提高趋势修复权重。",
        "expected_improvement": "降低只看指数表面导致的误判，改善 5d/10d/20d 路径排序。",
        "required_validation": "breadth confirmed 样本必须优于 breadth conflicted 样本，并且 primary-vs-secondary spread 为正。",
    },
    "flow_positioning_overlay": {
        "proposed_model_version": "challenger_v2_flow_positioning_overlay",
        "drivers": (
            "risk_on_flow_underweighted",
            "risk_off_flow_underweighted",
        ),
        "hypothesis": "成交量、风险偏好资产轮动、HYG/LQD、TLT/UUP 同向时，应影响短线弹性和风险路径权重。",
        "expected_improvement": "提高次日到 5d 的路径方向和波动区间判断。",
        "required_validation": "flow confirmed 高分样本必须在 1d/3d/5d 路径误差上优于普通样本。",
    },
    "price_structure_confirmation_overlay": {
        "proposed_model_version": "challenger_v2_price_structure_confirmation_overlay",
        "drivers": (
            "model_underestimated_upside_or_repair",
            "model_underestimated_downside_or_failed_bounce",
        ),
        "hypothesis": "当价格结构确认或否定主路径时，情景排序应更快反映确认价、失效价和风险接管价。",
        "expected_improvement": "减少路径已经被价格确认/否定但模型仍滞后的错误。",
        "required_validation": "主路径确认价后的样本必须比未确认样本有更高 primary hit rate。",
    },
}


def build_forecast_learning_queue(
    *,
    forecast_deviation_review: dict[str, Any],
    forecast_scorecard: dict[str, Any] | None = None,
    forecast_trust_gate: dict[str, Any] | None = None,
    dashboard: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Convert forecast errors into a safe challenger backlog.

    This module does not adjust baseline_v1. It creates an auditable queue of
    hypotheses that must run as shadow challengers before any model promotion.
    """

    scorecard = forecast_scorecard or {}
    trust_gate = forecast_trust_gate or {}
    summary = forecast_deviation_review.get("summary") or {}
    driver_counts = Counter({str(k): int(v) for k, v in (forecast_deviation_review.get("driver_counts") or {}).items()})
    reviewed = int(_float(summary.get("completed_outcomes_reviewed")) or 0)
    material = int(_float(summary.get("material_deviation_count")) or 0)
    evidence_level = str(summary.get("evidence_level") or _evidence_level(reviewed))
    trust_status = str(trust_gate.get("status") or "unknown")
    candidate_items = _candidate_items(driver_counts, reviewed, material)
    confidence_policy = _confidence_policy(scorecard, trust_gate, reviewed)
    blocked_reasons = _blocked_reasons(reviewed, material, trust_gate)

    return {
        "version": "forecast_learning_queue_v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "validation_type": "model_evolution_queue",
        "active_model": "baseline_v1",
        "baseline_policy": "frozen_do_not_modify_weights_or_rewrite_history",
        "alpha_v1_threshold_policy": "frozen_0.32534311",
        "evidence_level": evidence_level,
        "completed_outcomes_reviewed": reviewed,
        "material_deviation_count": material,
        "dominant_error_theme": summary.get("dominant_error_theme") or "not_enough_completed_outcomes",
        "trust_gate_status": trust_status,
        "global_learning_status": _global_learning_status(reviewed, material, candidate_items),
        "candidate_challengers": candidate_items,
        "confidence_policy": confidence_policy,
        "blocked_reasons": blocked_reasons,
        "next_best_actions": _next_best_actions(reviewed, material, candidate_items, blocked_reasons),
        "dashboard_surface": {
            "show_as": "model_learning_queue",
            "priority": "validation_section",
            "first_screen_allowed": False,
            "reason": "This is model evolution governance, not today's forecast decision layer.",
        },
        "guardrails": [
            "This queue does not change baseline_v1 or Alpha v1.",
            "Every learning item must become a challenger/shadow model before it can affect the active model.",
            "Historical replay may prioritize a challenger, but forward validation is required for promotion.",
            "No trading, PnL, buy/sell, entry or exit language is used.",
        ],
    }


def render_forecast_learning_queue_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# Forecast Learning Queue",
        "",
        f"Generated at: `{payload.get('generated_at')}`",
        "",
        "This report turns forecast deviations into safe challenger-model hypotheses. It does not alter baseline_v1.",
        "",
        "## Status",
        "",
        f"- active_model: `{payload.get('active_model')}`",
        f"- global_learning_status: `{payload.get('global_learning_status')}`",
        f"- evidence_level: `{payload.get('evidence_level')}`",
        f"- completed_outcomes_reviewed: `{payload.get('completed_outcomes_reviewed')}`",
        f"- material_deviation_count: `{payload.get('material_deviation_count')}`",
        f"- dominant_error_theme: `{payload.get('dominant_error_theme')}`",
        f"- trust_gate_status: `{payload.get('trust_gate_status')}`",
        "",
        "## Candidate Challengers",
        "",
    ]
    candidates = payload.get("candidate_challengers") or []
    if not candidates:
        lines.append("- No challenger candidates yet. More completed forward samples are needed.")
    for item in candidates:
        lines.extend(
            [
                f"### {item.get('candidate_id')}",
                "",
                f"- proposed_model_version: `{item.get('proposed_model_version')}`",
                f"- priority_score: `{item.get('priority_score')}`",
                f"- readiness: `{item.get('readiness')}`",
                f"- evidence_count: `{item.get('evidence_count')}`",
                f"- hypothesis: {item.get('hypothesis')}",
                f"- expected_improvement: {item.get('expected_improvement')}",
                f"- required_validation: {item.get('required_validation')}",
                f"- allowed_action: {item.get('allowed_action')}",
                f"- forbidden_action: {item.get('forbidden_action')}",
                "",
            ]
        )

    lines.extend(["## Confidence Policy", ""])
    for key, value in (payload.get("confidence_policy") or {}).items():
        lines.append(f"- {key}: `{value}`")

    lines.extend(["", "## Blocked Reasons", ""])
    blocked = payload.get("blocked_reasons") or []
    if not blocked:
        lines.append("- None.")
    for item in blocked:
        lines.append(f"- `{item.get('code')}`: {item.get('message')}")

    lines.extend(["", "## Next Best Actions", ""])
    for item in payload.get("next_best_actions") or []:
        lines.append(f"- {item}")

    lines.extend(["", "## Guardrails", ""])
    for item in payload.get("guardrails") or []:
        lines.append(f"- {item}")
    lines.append("")
    return "\n".join(lines)


def write_forecast_learning_queue_outputs(
    payload: dict[str, Any],
    *,
    public_dir: Path | None = None,
    outputs_dir: Path | None = None,
) -> None:
    public_dir = public_dir or PROJECT_ROOT / "frontend" / "public"
    outputs_dir = outputs_dir or PROJECT_ROOT / "outputs"
    public_dir.mkdir(parents=True, exist_ok=True)
    outputs_dir.mkdir(parents=True, exist_ok=True)
    (public_dir / "forecast-learning-queue.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (outputs_dir / "forecast_learning_queue.md").write_text(
        render_forecast_learning_queue_markdown(payload),
        encoding="utf-8",
    )


def _candidate_items(driver_counts: Counter[str], reviewed: int, material: int) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for candidate_id, config in DRIVER_GROUPS.items():
        counts = {driver: int(driver_counts.get(driver, 0)) for driver in config["drivers"]}
        evidence_count = sum(counts.values())
        if evidence_count == 0 and reviewed >= 20:
            continue
        priority = _priority_score(evidence_count, reviewed, material)
        items.append(
            {
                "candidate_id": candidate_id,
                "proposed_model_version": config["proposed_model_version"],
                "priority_score": priority,
                "readiness": _readiness(reviewed, material, evidence_count),
                "evidence_count": evidence_count,
                "driver_counts": counts,
                "hypothesis": config["hypothesis"],
                "expected_improvement": config["expected_improvement"],
                "required_validation": config["required_validation"],
                "allowed_action": "Run as shadow challenger and compare against baseline_v1 after future outcomes complete.",
                "forbidden_action": "Do not alter baseline_v1, Alpha v1 threshold, historical forecasts, or displayed probabilities based on this queue alone.",
            }
        )
    items.sort(key=lambda item: (int(item["priority_score"]), int(item["evidence_count"])), reverse=True)
    if reviewed < 20 and not items:
        items.append(
            {
                "candidate_id": "accumulate_forward_samples",
                "proposed_model_version": "none",
                "priority_score": 100,
                "readiness": "blocked_until_more_forward_outcomes",
                "evidence_count": 0,
                "driver_counts": {},
                "hypothesis": "样本不足时，最有价值的动作不是调模型，而是继续自动记录、回填和复盘。",
                "expected_improvement": "避免凭感觉过拟合，先让系统积累可验证的真实误差样本。",
                "required_validation": "至少 20 个已完成结果后再决定是否启动具体 challenger。",
                "allowed_action": "Keep daily forecast ledger, backfill outcomes, and review material deviations.",
                "forbidden_action": "Do not tune weights from anecdotal misses.",
            }
        )
    return items


def _priority_score(evidence_count: int, reviewed: int, material: int) -> int:
    if reviewed <= 0:
        return 0
    recurrence = min(60, evidence_count * 18)
    material_rate = min(25, int((material / max(1, reviewed)) * 100))
    sample_bonus = 15 if reviewed >= 50 else 8 if reviewed >= 20 else 0
    return max(0, min(100, recurrence + material_rate + sample_bonus))


def _readiness(reviewed: int, material: int, evidence_count: int) -> str:
    if reviewed < 20:
        return "insufficient_forward_evidence"
    if evidence_count < 2:
        return "needs_driver_recurrence"
    if material < 5:
        return "ready_for_shadow_spec_not_weight_change"
    return "ready_for_shadow_challenger"


def _global_learning_status(reviewed: int, material: int, candidates: list[dict[str, Any]]) -> str:
    if reviewed < 20:
        return "insufficient_forward_evidence"
    if material == 0:
        return "no_material_error_theme_yet"
    if any(item.get("readiness") == "ready_for_shadow_challenger" for item in candidates):
        return "shadow_challenger_queue_ready"
    return "error_themes_observed_but_not_promotable"


def _confidence_policy(
    scorecard: dict[str, Any],
    trust_gate: dict[str, Any],
    reviewed: int,
) -> dict[str, Any]:
    core = scorecard.get("core_questions") or {}
    high_conf = str(core.get("high_confidence_better") or "")
    trust_status = str(trust_gate.get("status") or "")
    cap_required = reviewed < 20 or "not" in high_conf.lower() or trust_status.startswith("RESEARCH_ONLY")
    return {
        "cap_displayed_confidence_until_validated": cap_required,
        "reason": (
            "Forward sample and high-confidence validation are insufficient."
            if cap_required
            else "Confidence buckets have early evidence, but promotion gates still apply."
        ),
        "high_confidence_question": high_conf or "missing",
        "trust_gate_status": trust_status or "missing",
    }


def _blocked_reasons(reviewed: int, material: int, trust_gate: dict[str, Any]) -> list[dict[str, str]]:
    reasons: list[dict[str, str]] = []
    if reviewed < 20:
        reasons.append(
            {
                "code": "sample_gate_not_met",
                "message": "已完成预测结果少于 20 个，不能据此调主模型权重。",
            }
        )
    if material == 0:
        reasons.append(
            {
                "code": "no_repeating_material_error_theme",
                "message": "还没有形成重复的实质偏差主题，不能判断哪类修正稳定有效。",
            }
        )
    for item in trust_gate.get("blockers") or []:
        reasons.append(
            {
                "code": str(item.get("code") or "trust_gate_blocker"),
                "message": str(item.get("message") or "Forecast trust gate is blocking reliance."),
            }
        )
    return reasons


def _next_best_actions(
    reviewed: int,
    material: int,
    candidates: list[dict[str, Any]],
    blocked_reasons: list[dict[str, str]],
) -> list[str]:
    if reviewed < 20:
        return [
            "保持 daily forward validation 自动运行，优先积累 1d/3d/5d 已完成样本。",
            "只回填 actual_return / primary_hit / path_error，不改写当时预测内容。",
            "不要基于单日错因调整 baseline_v1。",
        ]
    if material == 0:
        return [
            "继续观察，当前还没有足够重复的实质偏差主题。",
            "保持信任门槛；高置信预测未证明前不要提高 confidence。",
        ]
    top = next((item for item in candidates if item.get("proposed_model_version") != "none"), None)
    if top:
        return [
            f"优先把 `{top.get('candidate_id')}` 做成 shadow challenger：`{top.get('proposed_model_version')}`。",
            "让 challenger 与 baseline_v1 同时预测，未来用真实结果比较主路径命中率、路径误差和高置信样本表现。",
            "只有 forward validation 多数指标胜过 baseline_v1 后，才允许进入 promotion_candidate。",
        ]
    return ["继续自动复盘偏差；暂不启动新 challenger。"]


def _evidence_level(count: int) -> str:
    if count < 20:
        return "insufficient_samples"
    if count < 50:
        return "early_evidence"
    if count < 100:
        return "moderate_evidence"
    return "stronger_evidence"


def _float(value: Any) -> float | None:
    try:
        if value in (None, ""):
            return None
        return float(value)
    except Exception:
        return None


def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return parsed if isinstance(parsed, dict) else {}


if __name__ == "__main__":
    public_dir = PROJECT_ROOT / "frontend" / "public"
    review = _load_json(public_dir / "forecast-deviation-review.json")
    scorecard = _load_json(public_dir / "forecast-accuracy-scorecard.json")
    trust_gate = _load_json(public_dir / "forecast-trust-gate.json")
    payload = build_forecast_learning_queue(
        forecast_deviation_review=review,
        forecast_scorecard=scorecard,
        forecast_trust_gate=trust_gate,
    )
    write_forecast_learning_queue_outputs(payload)
    print("wrote outputs/forecast_learning_queue.md")
