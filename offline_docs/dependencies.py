"""Read dependencies."""

import sys
from pathlib import Path
from typing import Dict


import toml


def read_dependencies_poetry(pyproject_toml_path=Path) -> Dict[str, str]:
    dependencies = (
        toml.load(pyproject_toml_path)
        .get("tool")
        .get("poetry")
        .get("dependencies")
        .items()
    )
    return dependencies


def min_python_version(dependencies: Dict[str, str]) -> str:
    python_ver_raw = dependencies["python"]
    python_ver_stripped = python_ver_raw.strip("^")
    return python_ver_stripped


def read_running_python_version_full() -> str:
    major_minor_patch = sys.version.split(" ")[0]
    return major_minor_patch


def parse_major_minor(major_minor_patch: str) -> str:
    return major_minor_patch.split(".")[0] + "." + major_minor_patch.split(".")[1]
