"""Project-specific adapter for msitarzewski/agency-agents.

This script does not run prediction logic. It reads a curated set of upstream
agent role files from the `external/agency-agents` submodule and turns them into
a local review checklist for this Market Prediction Dashboard.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "config" / "agency_agents_manifest.json"
OUTPUT_MD = ROOT / "outputs" / "agency_agents_review.md"
OUTPUT_JSON = ROOT / "frontend" / "public" / "agency-agents-review.json"


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _submodule_commit(path: Path) -> str:
    if not path.exists():
        return "missing"
    try:
        result = subprocess.run(
            ["git", "-c", f"safe.directory={path}", "-C", str(path), "rev-parse", "--short", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def _first_heading(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            heading = stripped.lstrip("#").strip()
            ascii_heading = heading.encode("ascii", errors="ignore").decode("ascii").strip()
            return ascii_heading or heading
    return "No heading found"


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def build_review() -> dict[str, Any]:
    manifest = _read_json(MANIFEST_PATH)
    source_path = ROOT / manifest["source_path"]
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    roles: list[dict[str, Any]] = []

    for role in manifest["selected_roles"]:
        upstream_path = source_path / role["upstream_file"]
        status = "available" if upstream_path.exists() else "missing"
        text = upstream_path.read_text(encoding="utf-8", errors="replace") if upstream_path.exists() else ""
        roles.append(
            {
                "id": role["id"],
                "project_role": role["project_role"],
                "upstream_file": role["upstream_file"],
                "status": status,
                "upstream_heading": _first_heading(text) if text else None,
                "source_digest": _digest(text) if text else None,
                "use_for": role["use_for"],
                "required_outputs": role["required_outputs"],
            }
        )

    available = sum(1 for role in roles if role["status"] == "available")
    return {
        "generated_at": generated_at,
        "source_repository": manifest["source_repository"],
        "source_path": manifest["source_path"],
        "source_commit": _submodule_commit(source_path),
        "integration_purpose": manifest["integration_purpose"],
        "rules": manifest["rules"],
        "role_count": len(roles),
        "available_role_count": available,
        "missing_role_count": len(roles) - available,
        "roles": roles,
        "project_review_gates": [
            "forecast_impact",
            "data_freshness_and_source_status",
            "validation_and_ledger_impact",
            "user_facing_decision_impact",
            "security_and_secret_exposure_check",
        ],
    }


def write_outputs(review: dict[str, Any]) -> None:
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(review, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Agency Agents Review",
        "",
        f"Generated at: `{review['generated_at']}`",
        f"Source repository: {review['source_repository']}",
        f"Source path: `{review['source_path']}`",
        f"Source commit: `{review['source_commit']}`",
        "",
        "## Purpose",
        "",
        review["integration_purpose"],
        "",
        "## Guardrails",
        "",
    ]
    lines.extend(f"- {rule}" for rule in review["rules"])
    lines.extend(
        [
            "",
            "## Selected Roles",
            "",
            f"Available roles: {review['available_role_count']} / {review['role_count']}",
            "",
        ]
    )
    for role in review["roles"]:
        lines.extend(
            [
                f"### {role['project_role']}",
                "",
                f"- Role id: `{role['id']}`",
                f"- Upstream file: `{role['upstream_file']}`",
                f"- Status: `{role['status']}`",
                f"- Upstream heading: `{role['upstream_heading'] or 'missing'}`",
                "",
                "Use for:",
            ]
        )
        lines.extend(f"- {item}" for item in role["use_for"])
        lines.extend(["", "Required outputs:"])
        lines.extend(f"- `{item}`" for item in role["required_outputs"])
        lines.append("")

    lines.extend(
        [
            "## Project Review Gates",
            "",
        ]
    )
    lines.extend(f"- `{gate}`" for gate in review["project_review_gates"])
    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    review = build_review()
    write_outputs(review)
    print(
        "agency review generated:",
        f"{review['available_role_count']}/{review['role_count']} roles",
        f"source_commit={review['source_commit']}",
    )
    if review["missing_role_count"]:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
