"""Static leakage audit for market prediction research files.

This script is intentionally conservative. It flags patterns that often indicate
future leakage or invalid time-series validation and asks a researcher to review
them. It does not prove a pipeline is leakage-free.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


DEFAULT_PATTERNS: dict[str, str] = {
    "random_shuffle": r"shuffle\s*=\s*True",
    "train_test_split": r"train_test_split\s*\(",
    "negative_shift": r"\.shift\s*\(\s*-\d+",
    "centered_rolling": r"rolling\s*\([^)]*center\s*=\s*True",
    "backward_fill": r"\.(bfill|backfill)\s*\(",
    "full_sample_scaler": r"(StandardScaler|MinMaxScaler|RobustScaler)\s*\(",
    "full_sample_feature_selection": r"(SelectKBest|RFE|PCA)\s*\(",
    "random_kfold": r"\b(KFold|StratifiedKFold)\s*\(",
}

DEFAULT_EXTENSIONS = {".py", ".ipynb", ".sql", ".md", ".yaml", ".yml"}


def iter_files(root: Path, extensions: set[str]) -> list[Path]:
    if root.is_file():
        return [root] if root.suffix.lower() in extensions else []

    ignored_parts = {".git", ".venv", "node_modules", "__pycache__", ".pytest_cache"}
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in extensions:
            continue
        if ignored_parts.intersection(path.parts):
            continue
        files.append(path)
    return files


def audit_file(path: Path, patterns: dict[str, str]) -> list[tuple[str, int, str]]:
    findings: list[tuple[str, int, str]] = []
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    for index, line in enumerate(lines, start=1):
        if "audit-ignore" in line:
            continue
        for name, pattern in patterns.items():
            if re.search(pattern, line):
                findings.append((name, index, line.strip()))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit research files for common market prediction leakage patterns.")
    parser.add_argument("path", nargs="?", default=".", help="File or directory to audit.")
    parser.add_argument("--extension", action="append", help="Additional extension to scan, for example .txt")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    extensions = set(DEFAULT_EXTENSIONS)
    for extension in args.extension or []:
        extensions.add(extension if extension.startswith(".") else f".{extension}")

    total_findings = 0
    for path in iter_files(root, extensions):
        findings = audit_file(path, DEFAULT_PATTERNS)
        for name, line_number, snippet in findings:
            print(f"{path}:{line_number}: {name}: {snippet}")
        total_findings += len(findings)

    if total_findings:
        print(f"\nReview required: {total_findings} potential leakage or validation issues found.")
        return 1

    print("No obvious static leakage patterns found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
