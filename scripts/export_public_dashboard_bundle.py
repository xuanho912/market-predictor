"""Create a sanitized static dashboard bundle for a public display repo.

This script copies the built frontend only. It deliberately refuses to publish
backend code, research scripts, Codex skills, environment files, source maps, or
secret-like strings.
"""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_DIR_NAMES = {
    ".agents",
    ".codex",
    ".github",
    ".git",
    "backend",
    "data",
    "models",
    "node_modules",
    "scripts",
}

FORBIDDEN_FILE_NAMES = {
    ".env",
    ".env.local",
    ".env.production",
    ".npmrc",
    "Dockerfile",
    "docker-compose.yml",
}

FORBIDDEN_TEXT_MARKERS = {
    "FINNHUB_API_KEY",
    "NEXT_PUBLIC_FINNHUB_API_KEY",
    "DASHBOARD_DEPLOY_TOKEN",
    "OPENAI_API_KEY",
    "SECRET_KEY",
    "PRIVATE_KEY",
    "BEGIN RSA PRIVATE KEY",
    "BEGIN OPENSSH PRIVATE KEY",
}

TEXT_EXTENSIONS = {
    ".css",
    ".html",
    ".js",
    ".json",
    ".md",
    ".svg",
    ".txt",
    ".webmanifest",
    ".xml",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export a public-only dashboard bundle.")
    parser.add_argument("--source", default="frontend/out", help="Built static frontend directory.")
    parser.add_argument("--dest", default="outputs/public_dashboard_site", help="Destination bundle directory.")
    return parser.parse_args()


def resolve_under_repo(path_value: str) -> Path:
    path = (REPO_ROOT / path_value).resolve()
    if not path.is_relative_to(REPO_ROOT):
        raise SystemExit(f"Refusing to use a path outside repo: {path}")
    return path


def copy_public_site(source: Path, dest: Path) -> None:
    if not source.exists():
        raise SystemExit(f"Static frontend build is missing: {source}")
    if not source.is_dir():
        raise SystemExit(f"Static frontend build is not a directory: {source}")
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(
        source,
        dest,
        ignore=shutil.ignore_patterns(
            "*.map",
            ".env",
            ".env.*",
            ".git",
            ".github",
            "backend",
            "scripts",
            ".agents",
            ".codex",
        ),
    )


def write_public_metadata(dest: Path) -> None:
    (dest / ".nojekyll").write_text("", encoding="utf-8")
    (dest / "README.md").write_text(
        "\n".join(
            [
                "# Market Predictor Dashboard",
                "",
                "This repository contains generated static dashboard output only.",
                "",
                "It intentionally does not contain backend code, model research scripts,",
                "Codex skills, local databases, caches, or API keys.",
                "",
                "Alpha v1 remains a RESEARCH ALPHA CANDIDATE and is only a forecast signal / bounce scenario input.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "bundle_type": "public_static_dashboard_only",
        "contains_core_source": False,
        "contains_api_keys": False,
        "alpha_v1_status": "RESEARCH ALPHA CANDIDATE",
    }
    (dest / "dashboard_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def scan_bundle(dest: Path) -> None:
    violations: list[str] = []
    for path in dest.rglob("*"):
        relative = path.relative_to(dest).as_posix()
        parts = set(path.relative_to(dest).parts)
        if path.is_dir():
            if path.name in FORBIDDEN_DIR_NAMES:
                violations.append(f"forbidden directory: {relative}")
            continue
        if path.name in FORBIDDEN_FILE_NAMES:
            violations.append(f"forbidden file: {relative}")
        if parts & FORBIDDEN_DIR_NAMES:
            violations.append(f"forbidden nested path: {relative}")
        if path.suffix == ".map":
            violations.append(f"source map not allowed: {relative}")
        if path.suffix.lower() in TEXT_EXTENSIONS:
            text = path.read_text(encoding="utf-8", errors="ignore")
            for marker in FORBIDDEN_TEXT_MARKERS:
                if marker in text:
                    violations.append(f"secret marker {marker!r} found in {relative}")
    if violations:
        detail = "\n".join(f"- {item}" for item in violations)
        raise SystemExit(f"Public dashboard bundle failed safety scan:\n{detail}")


def main() -> int:
    args = parse_args()
    source = resolve_under_repo(args.source)
    dest = resolve_under_repo(args.dest)
    copy_public_site(source, dest)
    write_public_metadata(dest)
    scan_bundle(dest)
    file_count = sum(1 for path in dest.rglob("*") if path.is_file())
    print(f"Public dashboard bundle ready: {dest} ({file_count} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
