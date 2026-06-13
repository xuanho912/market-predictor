from __future__ import annotations

import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
BACKEND_ROOT = PROJECT_ROOT / "backend"
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from app.services.analysis.historical_analogs import build_alpha_v1_analog_report
from app.services.validation.forward_alpha_tracker import alpha_status_payload, report_payload


SYMBOLS = ("SPY", "QQQ", "IWM", "DIA")


def main() -> int:
    public_dir = PROJECT_ROOT / "frontend" / "public"
    public_dir.mkdir(parents=True, exist_ok=True)

    alpha_status = alpha_status_payload()
    alpha_report = report_payload()
    analogs = {symbol: build_alpha_v1_analog_report(symbol, top_k=20) for symbol in SYMBOLS}

    (public_dir / "alpha-v1-status.json").write_text(
        json.dumps(
            {
                "generated_by": "scripts/export_static_alpha_v1.py",
                "source": "github_actions_forward_tracker_outputs",
                "alpha_status": alpha_status,
                "forward_report": alpha_report,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    (public_dir / "alpha-v1-analogs.json").write_text(
        json.dumps(
            {
                "generated_by": "scripts/export_static_alpha_v1.py",
                "source": "github_actions_forward_tracker_outputs",
                "analogs": analogs,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    print("wrote frontend/public/alpha-v1-status.json")
    print("wrote frontend/public/alpha-v1-analogs.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
