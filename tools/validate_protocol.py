#!/usr/bin/env python3
"""Advisory structural validator for ChatGPT Operational Memory.

This intentionally checks only machine-verifiable repository invariants.
Semantic questions remain part of the ChatGPT health check described in OPERATIONS.md.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Iterable

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML is required to run tools/validate_protocol.py")
    print("Install with: python -m pip install pyyaml")
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []


def error(message: str) -> None:
    ERRORS.append(message)


def warn(message: str) -> None:
    WARNINGS.append(message)


def require_file(path: str, role: str = "required file") -> Path:
    target = ROOT / path
    if not target.is_file():
        error(f"missing {role}: {path}")
    return target


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def ids_in(text: str, prefix: str) -> list[str]:
    return re.findall(rf"^###\s+({re.escape(prefix)}-\d+)\b", text, re.MULTILINE)


def check_unique_ids(path: Path, prefix: str) -> set[str]:
    text = read_text(path)
    ids = ids_in(text, prefix)
    seen: set[str] = set()
    for item in ids:
        if item in seen:
            error(f"duplicate {item} in {path.relative_to(ROOT)}")
        seen.add(item)
    return seen


def referenced_ids(value: str, prefix: str) -> Iterable[str]:
    if value.strip().lower() in {"none", "none.", "n/a", ""}:
        return []
    return re.findall(rf"\b{re.escape(prefix)}-\d+\b", value)


def check_references(path: Path, prefix: str) -> None:
    text = read_text(path)
    known = set(ids_in(text, prefix))
    for label in ("Supersedes", "Superseded by"):
        pattern = rf"^- \*\*{re.escape(label)}:\*\*\s*(.+)$"
        for match in re.finditer(pattern, text, re.MULTILINE):
            for ref in referenced_ids(match.group(1), prefix):
                if ref not in known:
                    error(
                        f"{path.relative_to(ROOT)} references missing {ref} in {label}"
                    )


def active_count(path: Path, prefix: str) -> int:
    text = read_text(path)
    blocks = re.split(rf"(?=^###\s+{re.escape(prefix)}-\d+\b)", text, flags=re.MULTILINE)
    count = 0
    for block in blocks:
        if not re.match(rf"^###\s+{re.escape(prefix)}-\d+\b", block):
            continue
        status = re.search(r"^- \*\*Status:\*\*\s*([^\n]+)", block, re.MULTILINE)
        if status and status.group(1).strip().lower().startswith("active"):
            count += 1
    return count


def budget_bytes(path: str, limit: int, label: str) -> None:
    target = ROOT / path
    if target.is_file() and target.stat().st_size > limit:
        warn(f"soft budget crossed: {label} is {target.stat().st_size} bytes > {limit}")


def load_manifest() -> dict:
    manifest_path = require_file("PROTOCOL.yaml", "protocol manifest")
    if not manifest_path.is_file():
        return {}
    try:
        data = yaml.safe_load(read_text(manifest_path)) or {}
    except Exception as exc:  # noqa: BLE001
        error(f"PROTOCOL.yaml cannot be parsed: {exc}")
        return {}
    if not isinstance(data, dict):
        error("PROTOCOL.yaml root must be a mapping")
        return {}
    return data


def registry_slugs(registry_path: Path) -> set[str]:
    text = read_text(registry_path)
    return set(re.findall(r"^###\s+([a-z0-9][a-z0-9-]*)\s+—", text, re.MULTILINE))


def project_dirs(root: Path) -> set[str]:
    if not root.is_dir():
        return set()
    return {
        item.name
        for item in root.iterdir()
        if item.is_dir() and item.name != "_TEMPLATE" and not item.name.startswith(".")
    }


def main() -> int:
    manifest = load_manifest()
    if not manifest:
        print_results()
        return 1

    version = str(manifest.get("protocol_version", "")).strip()
    if not version:
        error("PROTOCOL.yaml missing protocol_version")

    if manifest.get("canonical_branch") != "main":
        warn("canonical_branch is not main; confirm this is intentional")

    front_door = str(manifest.get("front_door", "START_HERE.md"))
    require_file(front_door, "front door")

    global_map = manifest.get("global", {}) or {}
    for key in ("current", "decisions", "knowledge", "working_style", "projects"):
        path = global_map.get(key)
        if not path:
            error(f"PROTOCOL.yaml global.{key} is missing")
        else:
            require_file(str(path), f"global.{key}")

    for key, path in (manifest.get("human_docs", {}) or {}).items():
        require_file(str(path), f"human_docs.{key}")

    compatibility = manifest.get("compatibility", {}) or {}
    if compatibility.get("required_chatgpt_plugin") != "GitHub":
        error("PROTOCOL.yaml compatibility.required_chatgpt_plugin must be GitHub")
    if compatibility.get("plugin_invocation") != "@GitHub":
        error("PROTOCOL.yaml compatibility.plugin_invocation must be @GitHub")
    codex_bootloader = compatibility.get("codex_bootloader")
    if not codex_bootloader:
        error("PROTOCOL.yaml compatibility.codex_bootloader is missing")
    else:
        require_file(str(codex_bootloader), "Codex bootloader")

    projects_cfg = manifest.get("projects", {}) or {}
    projects_root_rel = str(projects_cfg.get("root", "projects"))
    template_rel = str(projects_cfg.get("template", "projects/_TEMPLATE"))
    required_project_files = list(projects_cfg.get("required_files", []))

    projects_root = ROOT / projects_root_rel
    template_root = ROOT / template_rel
    if not projects_root.is_dir():
        error(f"missing projects root: {projects_root_rel}")
    if not template_root.is_dir():
        error(f"missing project template: {template_rel}")

    for filename in required_project_files:
        if not (template_root / filename).is_file():
            error(f"project template missing required file: {filename}")

    registry_path = ROOT / str(global_map.get("projects", "PROJECTS.md"))
    registered = registry_slugs(registry_path) if registry_path.is_file() else set()
    actual_projects = project_dirs(projects_root)

    for slug in sorted(registered - actual_projects):
        error(f"registered project directory missing: projects/{slug}")
    for slug in sorted(actual_projects - registered):
        error(f"project directory is not registered in PROJECTS.md: projects/{slug}")

    for slug in sorted(actual_projects):
        project_root = projects_root / slug
        for filename in required_project_files:
            if not (project_root / filename).is_file():
                error(f"projects/{slug} missing required file: {filename}")

    decision_paths = [ROOT / str(global_map.get("decisions", "DECISIONS.md"))]
    knowledge_paths = [ROOT / str(global_map.get("knowledge", "KNOWLEDGE.md"))]
    for slug in sorted(actual_projects):
        decision_paths.append(projects_root / slug / "DECISIONS.md")
        knowledge_paths.append(projects_root / slug / "KNOWLEDGE.md")

    for path in decision_paths:
        if path.is_file():
            check_unique_ids(path, "D")
            check_references(path, "D")
    for path in knowledge_paths:
        if path.is_file():
            check_unique_ids(path, "K")
            check_references(path, "K")

    style_path = ROOT / str(global_map.get("working_style", "WORKING_STYLE.md"))
    if style_path.is_file():
        check_unique_ids(style_path, "WS")
        check_references(style_path, "WS")

    budgets = manifest.get("soft_budgets", {}) or {}
    budget_bytes(front_door, int(budgets.get("START_HERE.md_bytes", 14000)), "START_HERE.md")
    budget_bytes(
        str(global_map.get("current", "CURRENT.md")),
        int(budgets.get("CURRENT.md_bytes", 7000)),
        "global CURRENT.md",
    )

    project_front_door_limit = int(budgets.get("PROJECT.md_bytes", 9000))
    project_current_limit = int(budgets.get("project_CURRENT.md_bytes", 7000))
    for slug in sorted(actual_projects):
        budget_bytes(
            f"{projects_root_rel}/{slug}/PROJECT.md",
            project_front_door_limit,
            f"projects/{slug}/PROJECT.md",
        )
        budget_bytes(
            f"{projects_root_rel}/{slug}/CURRENT.md",
            project_current_limit,
            f"projects/{slug}/CURRENT.md",
        )

    decision_limit = int(budgets.get("active_decisions_per_scope", 30))
    for path in decision_paths:
        if path.is_file() and active_count(path, "D") > decision_limit:
            warn(
                f"soft budget crossed: {path.relative_to(ROOT)} has more than "
                f"{decision_limit} active decisions"
            )

    knowledge_limit = int(budgets.get("active_knowledge_per_scope", 40))
    for path in knowledge_paths:
        if path.is_file() and active_count(path, "K") > knowledge_limit:
            warn(
                f"soft budget crossed: {path.relative_to(ROOT)} has more than "
                f"{knowledge_limit} active knowledge entries"
            )

    style_limit = int(budgets.get("active_working_style_entries", 20))
    if style_path.is_file() and active_count(style_path, "WS") > style_limit:
        warn(
            f"soft budget crossed: WORKING_STYLE.md has more than {style_limit} active entries"
        )

    setup_test = ROOT / "SETUP-TEST.md"
    if setup_test.exists():
        warn("SETUP-TEST.md still exists; remove it after setup validation")

    print_results(version)
    return 1 if ERRORS else 0


def print_results(version: str = "unknown") -> None:
    print(f"Operational-memory structural validation · protocol {version}")
    for message in WARNINGS:
        print(f"WARNING: {message}")
    for message in ERRORS:
        print(f"ERROR: {message}")
    if ERRORS:
        print(f"RESULT: FAIL ({len(ERRORS)} error(s), {len(WARNINGS)} warning(s))")
    elif WARNINGS:
        print(f"RESULT: PASS WITH WATCH SIGNALS ({len(WARNINGS)} warning(s))")
    else:
        print("RESULT: PASS")


if __name__ == "__main__":
    raise SystemExit(main())
